import pytest
import asyncio
from mcp_server.jobs import run_background, jobs


@pytest.mark.asyncio
async def test_run_background_success(monkeypatch):
    sessions = {"s1": {"proc": object()}}

    async def fake_run(proc, cmd):
        return ("BGOUT", "", 0)

    monkeypatch.setattr("mcp_server.jobs.run_command", fake_run)

    jid = await run_background(sessions, "s1", "cmd")
    assert jid in jobs
    await asyncio.sleep(0.1)
    assert jobs[jid]["result"]["stdout"] == "BGOUT"


@pytest.mark.asyncio
async def test_run_background_error(monkeypatch):
    sessions = {"s2": {"proc": object()}}

    async def bad_run(proc, cmd):
        raise RuntimeError("boom")

    monkeypatch.setattr("mcp_server.jobs.run_command", bad_run)

    jid = await run_background(sessions, "s2", "bad")
    await asyncio.sleep(0.1)
    assert "error" in jobs[jid]
    assert "boom" in jobs[jid]["error"]
