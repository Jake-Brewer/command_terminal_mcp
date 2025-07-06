import pytest
from aiohttp import web
from mcp_server.metrics import metrics_handler
from dispatcher.router import init_pool_manager
from mcp_server.powershell_pool import spawn_ps
import asyncio


@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get("/metrics", metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get("/metrics")
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
