import pytest
import json
from aiohttp import web
from mcp_server.sse import sse_handler, push_sse, clients


@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get("/events", sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get("/events")
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: ") : -2])
    assert parsed == payload

    clients.clear()
