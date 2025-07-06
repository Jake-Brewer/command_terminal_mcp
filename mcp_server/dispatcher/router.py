# router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError

from mcp_server.schemas import SCHEMAS
from mcp_server.powershell_pool import run_command
from mcp_server.jobs import run_background, jobs
from mcp_server.pool_manager import PoolManager

pm: PoolManager = None


def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)


async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
