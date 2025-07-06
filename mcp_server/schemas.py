# schemas.py

SCHEMAS = {
    "startSession": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "action": {"const": "startSession"},
            "sync": {"type": "boolean"},
        },
        "required": ["id", "action"],
    },
    "queryPosition": {
        "type": "object",
        "properties": {"id": {"type": "number"}, "action": {"const": "queryPosition"}},
        "required": ["id", "action"],
    },
    "changeRequestType": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "action": {"const": "changeRequestType"},
            "sync": {"type": "boolean"},
        },
        "required": ["id", "action", "sync"],
    },
    "cancelRequest": {
        "type": "object",
        "properties": {"id": {"type": "number"}, "action": {"const": "cancelRequest"}},
        "required": ["id", "action"],
    },
    "runCommand": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "action": {"const": "runCommand"},
            "sessionId": {"type": "string"},
            "command": {"type": "string"},
        },
        "required": ["id", "action", "sessionId", "command"],
    },
    "runBackground": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "action": {"const": "runBackground"},
            "sessionId": {"type": "string"},
            "command": {"type": "string"},
        },
        "required": ["id", "action", "sessionId", "command"],
    },
    "getResult": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "action": {"const": "getResult"},
            "jobId": {"type": "string"},
        },
        "required": ["id", "action", "jobId"],
    },
    "endSession": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "action": {"const": "endSession"},
            "sessionId": {"type": "string"},
        },
        "required": ["id", "action", "sessionId"],
    },
}
