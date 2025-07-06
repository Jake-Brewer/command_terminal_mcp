# session.py
import uuid
import asyncio
from datetime import datetime
from mcp_server.config import PROMPT_TOKEN, MAX_CONCURRENT_SESSIONS, POOL_SIZE
from mcp_server.powershell_pool import spawn_ps
from mcp_server.sse import push_sse
from .queue import RequestEntry


class PoolManager:
    def __init__(self, free_pool):
        self.free_pool = free_pool
        self.sessions = {}
        self.request_list = []
        self.request_map = {}

        # EMA state
        self.avg_wait_sync = 0.0
        self.avg_wait_async = 0.0

        self.peak_sessions = 0
        self.peak_queue = 0

    async def start_session(self, req):
        rid = req["id"]
        sync = req.get("sync", True)

        self.peak_queue = max(self.peak_queue, len(self.request_list) + 1)

        if len(self.sessions) < MAX_CONCURRENT_SESSIONS and not self.free_pool.empty():
            return await self._alloc_session(req, rid)

        entry = RequestEntry(req, sync)
        self.request_list.append(entry)
        self.request_map[rid] = entry

        if sync:
            pos = sum(
                1
                for e in self.request_list
                if e.sync and e.enqueue_time <= entry.enqueue_time
            )
        else:
            pos = len(self.request_list)

        await push_sse(
            {
                "jsonrpc": "2.0",
                "method": "mcp/sessionQueued",
                "params": {
                    "requestId": rid,
                    "position": pos,
                    "message": (
                        f"All {MAX_CONCURRENT_SESSIONS} busy—You're #{pos}. "
                        f"ETA ~{round(self.estimate_wait(pos, sync))}s."
                    ),
                },
            }
        )

        return {"id": rid, "status": "queued", "position": pos}

    async def _alloc_session(self, req, rid, proc=None):
        if not proc:
            proc = await self.free_pool.get()
        sid = str(uuid.uuid4())
        self.sessions[sid] = {
            "proc": proc,
            "lastActive": datetime.now(),
            "requestId": rid,
            "cancelAfterNext": False,
        }

        self.peak_sessions = max(self.peak_sessions, len(self.sessions))

        entry = self.request_map.pop(rid, None)
        if entry:
            waited = (datetime.now() - entry.enqueue_time).total_seconds()
            alpha = 0.1
            if entry.sync:
                self.avg_wait_sync = (1 - alpha) * self.avg_wait_sync + alpha * waited
            else:
                self.avg_wait_async = (1 - alpha) * self.avg_wait_async + alpha * waited
            if entry in self.request_list:
                self.request_list.remove(entry)

        return {"requestId": rid, "sessionId": sid, "prompt": PROMPT_TOKEN}

    def get_average_wait(self, sync=True) -> float:
        return self.avg_wait_sync if sync else self.avg_wait_async

    def estimate_wait(self, position: int, sync=True) -> float:
        return self.get_average_wait(sync) * position

    def get_metrics(self) -> dict:
        return {
            "active_sessions": len(self.sessions),
            "free_slots": POOL_SIZE - len(self.sessions),
            "current_queue_depth": len(self.request_list),
            "peak_sessions": self.peak_sessions,
            "peak_queue_depth": self.peak_queue,
            "avg_wait_sync": round(self.avg_wait_sync, 2),
            "avg_wait_async": round(self.avg_wait_async, 2),
        }

    def query_position(self, req):
        rid = req["id"]
        entry = self.request_map.get(rid)
        if not entry or entry not in self.request_list:
            return {"id": rid, "message": "Not queued or already allocated."}
        if entry.sync:
            pos = sum(
                1
                for e in self.request_list
                if e.sync and e.enqueue_time <= entry.enqueue_time
            )
        else:
            pos = len(self.request_list)
        return {"id": rid, "position": pos}

    async def change_request_type(self, req):
        rid = req["id"]
        new_sync = req.get("sync", True)
        entry = self.request_map.get(rid)
        if not entry or entry not in self.request_list:
            return {"id": rid, "error": "Unknown or allocated requestId"}
        entry.sync = new_sync
        if new_sync:
            entry.enqueue_time = datetime.now()
        return self.query_position(req)

    async def cancel_request(self, req):
        rid = req["id"]
        entry = self.request_map.pop(rid, None)
        if entry and entry in self.request_list:
            self.request_list.remove(entry)
            await push_sse(
                {
                    "jsonrpc": "2.0",
                    "method": "mcp/requestCancelled",
                    "params": {
                        "requestId": rid,
                        "message": "Your queued request was cancelled.",
                    },
                }
            )
            return {"id": rid, "ok": True}

        for sid, info in self.sessions.items():
            if info.get("requestId") == rid:
                info["cancelAfterNext"] = True
                return {
                    "id": rid,
                    "ok": True,
                    "message": "Will close session after current command.",
                }

        return {"id": rid, "error": "Unknown requestId"}

    async def release_session(self, sid):
        info = self.sessions.pop(sid, None)
        if not info:
            return
        proc = info["proc"]
        if info.get("cancelAfterNext"):
            proc.terminate()

        next_entry = None
        for e in self.request_list:
            if e.sync:
                next_entry = e
                break
        if not next_entry and self.request_list:
            next_entry = self.request_list[0]

        if next_entry:
            self.request_list.remove(next_entry)
            rid = next_entry.req["id"]
            del self.request_map[rid]
            alloc = await self._alloc_session(next_entry.req, rid, proc)
            await push_sse(
                {"jsonrpc": "2.0", "method": "mcp/sessionReady", "params": alloc}
            )
            return

        await self.free_pool.put(proc)
