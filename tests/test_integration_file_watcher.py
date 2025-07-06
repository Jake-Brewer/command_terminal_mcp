import pytest
import time
from pathlib import Path
import mcp_server.watcher as watcher
from mcp_server.watcher import ChangeHandler, start_file_watcher, WATCH_PATHS


@pytest.mark.serial
def test_file_watcher_triggers(tmp_path, monkeypatch):
    monkeypatch.setattr(watcher, "WATCH_PATHS", [str(tmp_path)])
    watcher.pending_changes.clear()
    watcher.start_file_watcher()

    new_file = tmp_path / "hello.txt"
    new_file.write_text("hi")

    time.sleep(1)
    assert str(new_file) in watcher.pending_changes
