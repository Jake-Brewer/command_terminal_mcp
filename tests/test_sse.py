import pytest
import json
from mcp_server.sse import push_sse, clients


class DummyResp:
    def __init__(self):
        self.written = []

    async def write(self, data):
        self.written.append(data)


@pytest.mark.asyncio
async def test_push_sse_sends_to_all_clients():
    r1, r2 = DummyResp(), DummyResp()
    clients.extend([r1, r2])

    payload = {"jsonrpc": "2.0", "method": "test", "params": {"x": 1}}
    await push_sse(payload)

    expected = ("data: " + json.dumps(payload) + "\n\n").encode()
    assert expected in r1.written
    assert expected in r2.written

    clients.clear()
