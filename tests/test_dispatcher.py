import pytest
import asyncio
from mcp_server.dispatcher import dispatch, init_pool_manager


@pytest.mark.asyncio
async def test_start_session_immediate(free_pool):
    init_pool_manager(free_pool)
    await free_pool.put(object())
    req = {"id": 1, "action": "startSession"}
    resp = await dispatch(req)
    assert "sessionId" in resp


@pytest.mark.asyncio
async def test_schema_error():
    init_pool_manager(asyncio.Queue())
    req = {"id": 2, "action": "runCommand", "sessionId": 123, "command": None}
    resp = await dispatch(req)
    assert "Invalid request" in resp["error"]


@pytest.mark.asyncio
async def test_unknown_action():
    init_pool_manager(asyncio.Queue())
    req = {"id": 3, "action": "doesNotExist"}
    resp = await dispatch(req)
    assert "Unknown action" in resp["error"]
