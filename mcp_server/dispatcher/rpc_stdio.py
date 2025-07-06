# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch


async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
