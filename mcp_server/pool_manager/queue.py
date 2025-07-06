# pool_manager/queue.py
from datetime import datetime


class RequestEntry:
    def __init__(self, req, sync=True):
        self.req = req
        self.sync = sync
        self.enqueue_time = datetime.now()
