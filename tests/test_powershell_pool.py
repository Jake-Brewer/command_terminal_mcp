import pytest
from mcp_server.powershell_pool import spawn_ps, run_command, PROMPT_TOKEN


@pytest.mark.asyncio
async def test_spawn_ps_returns_proc(fake_proc):
    proc = await spawn_ps()
    assert hasattr(proc, "stdin")
    assert hasattr(proc, "stdout")


@pytest.mark.asyncio
async def test_run_command_reads_until_prompt(fake_proc):
    out, err, code = await run_command(fake_proc, "echo hi")
    assert "line1" in out
    assert err == ""
    assert code == 0
    fake_proc.stdout.feed_eof()
    out2, _, _ = await run_command(fake_proc, "cmd")
    assert out2 == ""
