import pytest
from mcp_server.schemas import SCHEMAS
from jsonschema import validate, ValidationError


def test_start_session_schema_accepts_sync_flag():
    schema = SCHEMAS["startSession"]
    valid = {"id": 1, "action": "startSession", "sync": False}
    validate(valid, schema)


def test_run_command_schema_rejects_invalid_types():
    schema = SCHEMAS["runCommand"]
    invalid = {"id": 2, "action": "runCommand", "sessionId": 123, "command": None}
    with pytest.raises(ValidationError):
        validate(invalid, schema)
