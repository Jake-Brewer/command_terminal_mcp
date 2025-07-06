# idle_watcher.py
import asyncio
from datetime import datetime
from .file_watcher import pending_changes
from mcp_server.config import IDLE_LIMIT_SEC, BACKUP_IDLE_SEC, GIT_REPO_ROOT
from mcp_server.sse import push_sse
from asyncio.subprocess import create_subprocess_exec

last_activity = datetime.now()


async def run_git(*args):
    proc = await create_subprocess_exec(
        "git",
        "-C",
        GIT_REPO_ROOT,
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate()
    return out.decode(), err.decode(), proc.returncode


async def monitor_sessions(sessions):
    global last_activity
    while True:
        now = datetime.now()

        # Abandoned sessions
        for sid, info in list(sessions.items()):
            idle = (now - info["lastActive"]).total_seconds()
            if idle > IDLE_LIMIT_SEC and not info.get("reportedAbandoned"):
                info["reportedAbandoned"] = True
                await push_sse(
                    {
                        "jsonrpc": "2.0",
                        "method": "mcp/sessionAbandoned",
                        "params": {
                            "sessionId": sid,
                            "idleSeconds": idle,
                            "message": f"Session {sid} idle > {int(idle)}s",
                        },
                    }
                )

        # Git backup
        if pending_changes and (now - last_activity).total_seconds() > BACKUP_IDLE_SEC:
            out1, err1, _ = await run_git("add", ".")
            out2, err2, _ = await run_git(
                "commit", "-m", f"Auto-backup: {len(pending_changes)} files changed"
            )
            await push_sse(
                {
                    "jsonrpc": "2.0",
                    "method": "mcp/backupCompleted",
                    "params": {
                        "stdout": out1 + out2,
                        "stderr": err1 + err2,
                        "message": f"Backed up {len(pending_changes)} files",
                    },
                }
            )
            pending_changes.clear()
            last_activity = now

        await asyncio.sleep(5)
