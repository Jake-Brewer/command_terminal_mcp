import pytest
import asyncio
from mcp_server.dispatcher import init_pool_manager, dispatch
from mcp_server.sse import clients


@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # 1. startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    assert "sessionId" in r1
    sid = r1["sessionId"]

    # 2. runCommand
    r2 = await dispatch(
        {"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"}
    )
    assert "line1" in r2["stdout"]

    # 3. endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
