import asyncio
import pytest
from types import SimpleNamespace

from mcp_server import powershell_pool
from mcp_server import dispatcher
from mcp_server import jobs
from mcp_server import sse


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def isolate_state(monkeypatch):
    dispatcher.pm = None
    jobs.jobs.clear()
    sse.clients.clear()
    yield


@pytest.fixture
async def fake_proc(monkeypatch):
    class FakeProc:
        def __init__(self):
            self.stdin = SimpleNamespace(
                write=lambda data: None, drain=lambda: asyncio.sleep(0)
            )
            self.stdout = asyncio.StreamReader()

        async def communicate(self, **kw):
            return ("fake-out", "fake-err")

        @property
        def returncode(self):
            return 0

    proc = FakeProc()
    proc.stdout.feed_data(b"line1\n")
    proc.stdout.feed_data(powershell_pool.PROMPT_TOKEN.encode() + b"\n")
    proc.stdout.feed_eof()

    async def fake_spawn(*args, **kwargs):
        return proc

    monkeypatch.setattr(powershell_pool, "spawn_ps", fake_spawn)
    monkeypatch.setattr(powershell_pool, "create_subprocess_exec", fake_spawn)
    return proc
