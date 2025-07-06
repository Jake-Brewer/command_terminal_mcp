import pytest
import time
from pathlib import Path
from mcp_server.watcher import pending_changes, ChangeHandler, start_file_watcher


class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory


def test_change_handler_adds_new_file(tmp_path):
    pending_changes.clear()
    handler = ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in pending_changes


@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")

        returncode = 0

    async def fake_exec(*args, **kw):
        return FakeProc()

    monkeypatch.setattr(start_file_watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await start_file_watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
