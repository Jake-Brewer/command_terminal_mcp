# jobs.py
import asyncio
import uuid
from mcp_server.powershell_pool import run_command
from mcp_server.sse import push_sse

jobs = {}


async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}

    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
                "jsonrpc": "2.0",
                "method": "mcp/jobFinished",
                "params": {
                    "jobId": job_id,
                    "stdout": out,
                    "stderr": err,
                    "exitCode": code,
                },
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
                "jsonrpc": "2.0",
                "method": "mcp/jobFailed",
                "params": {"jobId": job_id, "error": str(e)},
            }
        await push_sse(payload)

    asyncio.create_task(_task())
    return job_id
