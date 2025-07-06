# file_watcher.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from mcp_server.config import WATCH_PATHS

pending_changes = set()


class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if not event.is_directory:
            pending_changes.add(event.src_path)


def start_file_watcher():
    obs = Observer()
    handler = ChangeHandler()
    for path in WATCH_PATHS:
        obs.schedule(handler, path, recursive=True)
    obs.daemon = True
    obs.start()
