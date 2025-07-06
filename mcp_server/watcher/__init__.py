# watcher/__init__.py
from .file_watcher import ChangeHandler, start_file_watcher, WATCH_PATHS
from .idle_watcher import monitor_sessions, run_git, pending_changes
