from mcp_server.config import *


def test_config_constants_have_expected_types():
    assert isinstance(POOL_SIZE, int)
    assert isinstance(MAX_CONCURRENT_SESSIONS, int)
    assert isinstance(IDLE_LIMIT_SEC, int)
    assert isinstance(BACKUP_IDLE_SEC, int)
    assert isinstance(WATCH_PATHS, list)
    assert isinstance(GIT_REPO_ROOT, str)
    assert isinstance(PROMPT_TOKEN, str)
