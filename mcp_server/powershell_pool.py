# powershell_pool.py
import asyncio
from mcp_server.config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec


async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        init,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    )
    await proc.stdout.readline()
    return proc


async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
