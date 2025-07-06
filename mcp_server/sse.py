# sse.py
from aiohttp import web
import asyncio
import json

clients = []


async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
            "Content-Type": "text/event-stream",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp


async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
