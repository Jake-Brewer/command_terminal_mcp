# metrics.py
from aiohttp import web
from mcp_server.dispatcher import pm


async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)

    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    m["estimated_wait_next_sync_sec"] = round(pm.estimate_wait(depth + 1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth + 1, False), 2)
    return web.json_response(m)
