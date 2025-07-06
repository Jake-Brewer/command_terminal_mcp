#!/usr/bin/env python3
import asyncio
from aiohttp import web

from mcp_server.config import POOL_SIZE
from mcp_server.powershell_pool import spawn_ps
from mcp_server.dispatcher import init_pool_manager, handle_stdio, pm
from mcp_server.watcher import start_file_watcher, monitor_sessions
from mcp_server.sse import sse_handler
from mcp_server.metrics import metrics_handler


async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)

    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(handle_stdio(), monitor_sessions(pm.sessions))


if __name__ == "__main__":
    asyncio.run(main())
