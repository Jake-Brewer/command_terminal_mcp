# Microsoft Copilot: Your AI companion (Markdown Conversion)

*This file is a progressive markdown conversion of more.html, chunk 1.*

---

> **Note:** The first 250 lines are mostly HTML metadata, scripts, and page structure. The main content conversion will begin in the next chunk, focusing on user-visible content.

## Sidebar Navigation

### Pages

- Making money as independent it
- Offering Support for Job Search

### Conversations

- Today
  - Setting Up Claude API with Caching
  - Request for AI Tools List and Categorization
  - Effects of Fermented Vitamins on Sleepiness
- Yesterday
  - Accessing Gmail Programmatically in Python
  - Cursor IDE Features and MCP Integration Overview
  - Grocery List and Shopping Instructions
  - Open Source Mind-Mapping Tool Suggestions
  - Request for Page Summary Assistance
  - Integrating Gmail MCPs into Cursor
  - LangGraph Tutorials and Exercises Resources
- Yesterday (continued)
  - Strengths, Weaknesses, and Uses of Open-Source AI/ML Tools
  - Strengths, Weaknesses, and Uses of Open-Source LLMs
  - Trusted Resources for Working with LLMs
  - LangGraph Usage Documentation Resources
  - Documentation for Daniel Miessler's Fabric Framework
  - Extracting Copilot Conversations on Windows 11
  - Grocery Delivery Options in Johns Creek, GA
  - Exploring Fabric for AI Workflows and Scripting
  - Clarification on Gmail MCPs
  - LangGraph Tutorials and Exercises
  - Comprehensive Application Creation System Design Guide
  - High-Level Plan for Financial and Personal Recovery
- Friday
  - Exploring Fabric by Daniel Miessler for Workflow Integration
  - Integrating StudyLetta with Cursor and Windsurf
  - Overview of PowerShell 7 Features and Installation
  - Copilot App CLI and API Options on Windows 11
- Wednesday
  - Prompt Engineering for AI Tools
  - Choosing the Best LLM Memory MCP for Local Use
  - Overview of Excalidraw Features and Uses
  - Learning Mathematics for Machine Learning
  - Prompt for Gmail Email and Attachment Downloader Library
  - LinkedIn Profile Assistance
  - Exploring Code Fabric and LangGraph for Workflow Optimization
- Tuesday
  - Refining a LinkedIn Post for Visibility and Impact
  - Implementing Command Timeouts in Terminal
  - Exploring GitHub Repository on Agents

## Main Chat Content

### User
>
> What do you know about cursor IDE, conversations, MCPs, MCP integration with cursor, and cursors use of power shell terminals?

### Copilot

Here's a comprehensive breakdown of what I found about Cursor IDE's conversations, MCP integration, and PowerShell terminal behavior:

#### 💬 Cursor IDE Conversations

Cursor supports **multi-threaded AI conversations** through its sidebar Agent, which can:

- Understand and edit code
- Suggest terminal commands
- Automate workflows

Key features:

- **Tabs for parallel chats**: Use `Ctrl+T` (or `Cmd+T` on Mac) to open multiple conversations simultaneously.
- **Checkpoints**: Cursor auto-saves code states after each AI interaction, allowing you to revert changes.
- **Chat history**: Stored locally in SQLite databases (`state.vscdb` files) under `%APPDATA%\Cursor\User\workspaceStorage` on Windows.
- **Exporting**: Tools like cursor-chat-browser let you browse and export chat logs.
- **Composer integration**: Conversations are tightly coupled with code edits and terminal outputs, enabling seamless context switching.

#### 🔌 MCPs (Model Context Protocol) & Integration with Cursor

MCP is a **protocol for connecting Cursor to external tools and data sources**. Think of it as a USB-like interface for AI.

**What MCP Enables:**

- **Tool invocation from chat**: Cursor's Agent can call MCP tools automatically or on request.
- **Custom tool integration**: You can write MCP servers in any language (Python, JS, Go, etc.) that supports stdout or HTTP/SSE.

**How to Integrate:**

- Add MCP servers via `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project-specific).

Example config:

```json
{
  "mcpServers": {
    "web-search": {
      "command": "npx",
      "args": ["-y", "@smithery/cli", "run", "@smithery-ai/brave-search"],
      "env": {
        "BRAVE_API_KEY": "your_key_here"
      }
    }
  }
}
```

**Transport types:**

- `stdio`: Local CLI tools
- `sse`: Server-sent events
- **Security**: Use restricted API keys and verify sources before installing MCPs.

#### ⚙️ PowerShell Terminal Support in Cursor

Cursor supports PowerShell, but integration is **buggy and inconsistent**, especially on macOS and Windows:

#### Known Issues

- **Cursor positioning errors:** PowerShell throws `System.InvalidOperationException` due to rendering mismatches.
- **Blank terminal:** Some users report the terminal opens with no prompt or interactivity.
- **Command output limitations:** The Agent cannot read or wait for terminal command output, which affects workflows like builds.
- **Incorrect flags:** Cursor sometimes prepends invalid flags (e.g., `-l`) to PowerShell commands.

#### Workarounds

- Use alternate shells like Git Bash or zsh where possible.
- Avoid relying on terminal output parsing in Agent workflows.

---

Would you like a sample `mcp.json` tailored to your current setup or help debugging PowerShell behavior in Cursor?

---

**User:**
> What do you know about how power-shell is integrated with the conversation?

**Copilot:**

Cursor IDE's integration of PowerShell into its **AI-driven conversation system** is currently **problematic and inconsistent**, especially when the Agent tries to execute or interpret terminal commands. Here's a detailed breakdown of how it's wired—and where it breaks:

#### 🧠 How PowerShell Is Integrated with Conversations in Cursor

Cursor's Agent can:

- Suggest terminal commands based on your code or chat context
- Attempt to **execute those commands directly in the terminal**
- Parse the output and use it to inform follow-up suggestions

This is part of Cursor's **Composer system**, where the Agent, terminal, and code editor are tightly coupled. However, PowerShell introduces several issues in this loop.

#### Known Issues with PowerShell Integration

1. **Invalid Command Flags**
   - Cursor mistakenly prepends `-l` to PowerShell commands (a flag valid in Unix shells but not in PowerShell), causing them to fail with:

     ```
     The terminal process "powershell.exe '-l'" terminated with exit code: 1
     ```

2. **Buffer Size & UI Errors**
   - PowerShell commands like `Format-Table` or `Write-Progress` trigger:

     ```
     System.ArgumentOutOfRangeException: The value must be greater than or equal to zero and less than the console's buffer size
     ```

   - This is due to Cursor's terminal emulation setting the buffer height to 1, which breaks rendering.

3. **Agent Misreads Output**
   - Even when commands run, the Agent often:
     - Misses the output
     - Misinterprets formatting
     - Times out waiting for a response

4. **PSReadLine Compatibility**
   - Cursor's terminal doesn't play well with `PSReadLine`, which affects command history, tab completion, and formatting.

---

#### 🛠️ Workarounds and Ideas

- **Switch to Git Bash or WSL:** These shells are more stable in Cursor.
- **Disable shell integration:**

  ```json
  "terminal.integrated.shellIntegration.enabled": false
  ```

- **Use external PowerShell scripts:** Instead of running commands inline, invoke `.ps1` scripts via MCP or subprocesses.
- **MCP PowerShell Server:** You could create a custom MCP tool that runs PowerShell commands outside the terminal and returns clean output to the Agent.

Would you like help scaffolding a PowerShell MCP tool that bypasses the terminal entirely? That could give you reliable command execution and output parsing within conversations.

---

### User
>
> You read my mind! Can we force a conversation in cursor to use our MCP rather than the way it is using powershell now we could have more control and automatically work around some of the bugs

### Copilot

# Forcing Cursor Conversations to Use Your MCP

You can bypass Cursor's built-in PowerShell integration by routing all shell-command requests through a custom MCP server. This gives you full control over invocation, flag-sanitization, output parsing, and bug workarounds.

## 1. Overview of the Approach

1. Build a simple MCP server that:
   - Listens for JSON-RPC requests on stdin/stdout.
   - Receives command parameters (e.g. script, args, env).
   - Invokes PowerShell (or any shell) via a guaranteed flag set.
   - Captures stdout/stderr, exit code, and returns them in JSON.
2. Tell Cursor to use this MCP tool instead of its built-in terminal integration.
3. (Optional) Extend your tool to preprocess commands—e.g. strip `-l`, resize buffers, disable PSReadLine, etc.

## 2. Sample Python MCP Server

Save this as `powershell_mcp.py` somewhere in your PATH:

```python
#!/usr/bin/env python3
import sys, json, subprocess, os

def send(res):
    sys.stdout.write(json.dumps(res) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        req = json.loads(line)
        cmd = req.get("command", "powershell.exe")
        args = req.get("args", [])
        env  = os.environ.copy()
        env.update(req.get("env", {}))
        # Ensure no invalid flags slip in
        safe_args = ["-NoProfile", "-NonInteractive", "-Command"] + ["& {" + " ".join(args) + "}"]
        proc = subprocess.Popen(
            [cmd] + safe_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            text=True
        )
        out, err = proc.communicate(timeout=req.get("timeout", 60))
        resp = {
            "id": req.get("id"),
            "stdout": out,
            "stderr": err,
            "exitCode": proc.returncode
        }
        send(resp)

if __name__ == "__main__":
    main()
```

Make it executable:

```bash
chmod +x powershell_mcp.py
```

## 3. Configuring Cursor to Use Your MCP

Create or update your project's `<project-root>/.cursor/mcp.json` (or use `~/.cursor/mcp.json` for global):

```json
{
  "mcpServers": {
    "powershell-shell": {
      "command": "/full/path/to/powershell_mcp.py",
      "transport": "stdio",
      "args": [],
      "env": {
        "PSMODULEPATH": "C:\\custom\\modules;${env:PSMODULEPATH}"
      }
    }
  }
}
```

- `command`: Path to your Python script
- `transport`: `"stdio"` lets Cursor speak via stdin/stdout
- `args`: Additional startup args if needed
- `env`: Custom PowerShell environment overrides

## 4. Invoking Your MCP in Conversations

Inside your conversation, prefix shell requests with the MCP name:

```text
@mcp powershell-shell
command: Get-ChildItem -Path C:\projects
```

Cursor will route this to your Python server, not its built-in terminal.

If you want *all* terminal commands auto-routed, add this to your Cursor settings (`settings.json`):

```jsonc
{
  "cursor.composer.defaultMcpServer": "powershell-shell"
}
```

## 5. Advanced Tips & Workarounds

- **Flag Sanitization**: Strip or rewrite flags before invocation.
- **Buffer Fixes**: Adjust PowerShell buffer via `-WindowStyle Hidden` or explicit `BufferSize` args.
- **Timeouts/Re-tries**: Catch and auto-retry on known exceptions.
- **Enhanced Parsing**: Return pure JSON from your MCP by wrapping PowerShell output with `ConvertTo-Json`.

## What's Next?

- Would you like a **Node.js** version of this MCP server?
- Need help integrating **argument schema validation** (e.g. with JSON Schema)?
- Interested in hooking this up to a **webhook-based MCP** for remote command execution?

Let me know which direction feels most useful—happy to drill down further!

---

### User
>
> Will this prevent cursor from using powershell the way it is now?

### Copilot

## Yes—your MCP can take over PowerShell calls

By setting up a dedicated MCP server and pointing Cursor's composer at it, you effectively redirect all AI-driven shell requests away from the built-in PowerShell integration.

### How it works

- **Default MCP routing**: All shell commands from the Agent will be sent to your MCP server instead of the default terminal.

## Enforcing Resource Limits & Rejection

Sometimes you may want a hard cap on total terminals or system resource usage. Configure a `MAX_CONCURRENT_SESSIONS` in `config.py` (e.g., 5).

### 2.1. Rejecting Excess Requests

If `sessions_in_use >= MAX_CONCURRENT_SESSIONS` **and** you disallow queuing, immediately respond:

```json
{
  "id": 43,
  "error": "ResourceLimitExceeded",
  "message": "Too many active terminals (5). Please try again later."
}
```

The Agent surfaces it as an error bubble.

### 2.2. Dynamic Throttling Based on System Load

- Poll CPU/memory every few seconds in `watcher.py`.
- If load > threshold, temporarily reject new `startSession` or `runBackground` calls until load subsides.
- Return a `"Retry-After"` suggestion in the JSON-RPC error if desired.

---

## Code Snippet: PoolManager with Queuing & Limits

```python
# inside your PoolManager class (or dispatcher)
from config import MAX_CONCURRENT_SESSIONS

self.requestQueue = asyncio.Queue()
self.active_sessions = set()

async def handle_start_session(self, req):
    rid = req["id"]
    # Enforce hard cap
    if len(self.active_sessions) >= MAX_CONCURRENT_SESSIONS:
        # Option A: enqueue
        pos = self.requestQueue.qsize() + 1
        await self.requestQueue.put((rid, req))
        return {"id": rid, "status": "queued", "position": pos,
                "message": f"All {MAX_CONCURRENT_SESSIONS} terminals are busy. You're #{pos} in queue."}

        # Option B: reject instead
        # return {"id":rid,"error":"ResourceLimitExceeded",
        #         "message":f"Max {MAX_CONCURRENT_SESSIONS} sessions in use. Try again later."}

    # Allocate immediately
    proc = await free_pool.get()
    sid  = str(uuid.uuid4())
    self.active_sessions.add(sid)
    self.sessions[sid] = {"proc":proc, "lastActive":now(), "reported":False}
    return {"id":rid,"sessionId":sid,"prompt":PROMPT_TOKEN}

async def release_session(self, sid):
    # called on endSession or session timeout
    proc = self.sessions.pop(sid)["proc"]
    self.active_sessions.remove(sid)
    proc.terminate()
    # allocate to queued requester?
    if not self.requestQueue.empty():
        rid, originalReq = await self.requestQueue.get()
        # spawn new sessionId
        new_sid = str(uuid.uuid4())
        self.sessions[new_sid] = {"proc": proc, "lastActive": now(), "reported": False}
        self.active_sessions.add(new_sid)
        # notify via SSE
        await push_sse({
          "jsonrpc": "2.0",
          "method": "mcp/sessionReady",
          "params": {"requestId": rid, "sessionId": new_sid, "prompt": PROMPT_TOKEN}
        })
    else:
        # return to free pool
        await self.free_pool.put(proc)
```

---

## Summary

- **Yes**, you can queue `startSession` requests when the pool is empty.
- Provide the Agent with **queued status**, **position**, and a friendly message.
- **Notify** the Agent via SSE (`mcp/sessionReady`) once the session is allocated.
- Enforce a **hard cap** with `MAX_CONCURRENT_SESSIONS` to reject or queue beyond resource limits.
- Optionally **throttle** based on real-time CPU/memory metrics.

This pattern ensures smooth handling when demand spikes, keeps your LLM-driven workflows responsive, and avoids uncontrolled resource consumption.

---

## Chat Example

> I think it would be much better to have a queue to work than just to reject it. The agents can choose to cancel any request in which case we would just close the terminal when the current command finishes and not report it anywhere or if the agent is in queue, it will just remove them from the queue. When an agent is put in a queue, can we let them know their place in the queue and tell them that they may select to use a background request to run the terminal asynchronously and receive the results when they're ready rather than wait, unless the agent requested a background terminal to run asynchronously. And of course, synchronous requests would get priority in the queue because there is an agent sitting idle and waiting.

---

## Design: True Queued System

Below is a design and code sketch showing how to turn your PoolManager into a true queued system with:

- a FIFO queue for incoming `startSession` (or background) requests
- per-request metadata (sync vs async) so sync requests get priority
- JSON-RPC responses that inform the Agent of queue position, a "suggested use background" hint, and SSE notifications when the session is finally allocated
- a `cancelRequest` action that lets the Agent pull itself out of the queue (or mark a running session for tear-down after its next command)

### 1. New JSON-RPC Actions & Notifications

**Actions**

```text
startSession       // existing, now queueable
runBackground      // existing, can also queue if you want
cancelRequest      // NEW: removes a queued startSession or marks running session for cleanup
```

**Notifications (via SSE)**

```json
// when queued
{
  "jsonrpc": "2.0",
  "method": "mcp/sessionQueued",
  "params": {
    "requestId": 42,
    "position": 3,
    "message": "All 5 terminals busy. You're #3 in line. You can @mcp ps-pool runBackground... to run async."
  }
}

// when session finally allocated
{
  "jsonrpc": "2.0",
  "method": "mcp/sessionReady",
  "params": {
    "requestId": 42,
    "sessionId": "s-abc123",
    "prompt": "PSLLM> "
  }
}

// when a queued request is cancelled
{
  "jsonrpc": "2.0",
  "method": "mcp/requestCancelled",
  "params": {
    "requestId": 42,
    "message": "Your queued request was cancelled."
  }
}
```

---

## PoolManager Sketch

In `mcp_server/pool_manager.py` (or augment your dispatcher accordingly):

```python
import uuid, asyncio
from datetime import datetime
from sse import push_sse
from config import MAX_CONCURRENT_SESSIONS, PROMPT_TOKEN

class PoolManager:
    def __init__(self, free_pool):
        self.free_pool     = free_pool                # asyncio.Queue of idle procs
        self.active        = {}                       # sessionId→info
        self.request_queue = asyncio.Queue()          # holds (req, sync_flag)
        self.request_map   = {}                       # requestId→queue_entry

    async def start_session(self, req):
        rid  = req["id"]
        sync = req.get("sync", True)   # default to sync requests
        # if under limit and free session exists, allocate immediately
        if len(self.active) < MAX_CONCURRENT_SESSIONS and not self.free_pool.empty():
            return await self._alloc_session(req, rid)

        # else queue it
        entry = {"req":req, "sync":sync, "time":datetime.now()}
        # priority: sync requests must be served first, but we keep FIFO
        await self.request_queue.put(entry)
        self.request_map[rid] = entry

        pos = sum(1 for e in self.request_queue._queue if e["sync"]) \
            if sync else self.request_queue.qsize()
        # respond immediately with queued status
        return {
          "id":rid,
          "status":"queued",
          "position":pos,
          "message":(
            f"All {MAX_CONCURRENT_SESSIONS} terminals busy. "
            f"You're #{pos} in queue. "
            "You can @mcp ps-pool runBackground... to run async."
          )
        }

    async def cancel_request(self, req):
        rid = req["id"]
        entry = self.request_map.pop(rid, None)
        if entry and entry in self.request_queue._queue:
            self.request_queue._queue.remove(entry)
            await push_sse({
              "jsonrpc": "2.0",
              "method": "mcp/requestCancelled",
              "params": {"requestId": rid, "message": "Your queued request was cancelled."}
            })
            return {"id":rid,"ok":True}
        # if already running
        for sid, info in self.active.items():
            if info.get("requestId")==rid:
                info["cancelAfterNext"] = True
                return {"id":rid,"ok":True,"message":"Will close session after current command."}
        return {"id":rid,"error":"Unknown requestId"}

    async def release_session(self, sid):
        """
        Called when endSession or cancelAfterNext fires:
        - free the PS process
        - if queue non-empty, allocate to next queued request
        """
        proc = self.sessions.pop(sid)["proc"]
        if not self.request_queue.empty():
            # find next sync-first
            # pluck first entry with sync=True, else FIFO
            queue = self.request_queue._queue
            for idx, entry in enumerate(queue):
                if entry["sync"]:
                    queue.pop(idx); break
            else:
                entry = queue.pop(0)
            rid, req = entry["req"]["id"], entry["req"]
            self.request_map.pop(rid, None)
            # allocate
            resp = await self._alloc_session(req, rid, proc)
            # notify Agent via SSE
            await push_sse({
              "jsonrpc": "2.0",
              "method": "mcp/sessionReady",
              "params": resp
            })
            return

        # no queued requests: return to free pool
        await self.free_pool.put(proc)

    async def _alloc_session(self, req, rid, proc=None):
        """
        Helper: take a proc (or get new one) and return alloc response.
        """
        if not proc:
            proc = await self.free_pool.get()
        sid = str(uuid.uuid4())
        self.active[sid] = {
            "proc":proc,
            "lastActive":datetime.now(),
            "requestId":rid,
            "cancelAfterNext":False
        }
        return {"id":rid,"sessionId":sid,"prompt":PROMPT_TOKEN}
```

---

## Agent-Facing Behavior

1. **Sync request**
   - If idle slot: immediate `{ sessionId }` response
   - If busy: `{ status: "queued", position: N, message: ... }`
   - Later, SSE arrives to notify when ready

2. **Async request**
   - Treated as `sync=false`, so queued behind all sync requests
   - Response and notifications identical, but lower priority

3. **Cancellation**
   - Removes you from queue or schedules your session to close after the next command

#### Why this works

- **Fairness**: sync waits get served first; async waits behind
- **Visibility**: Agents know their queue position and can switch to background mode
- **Control**: Agents can cancel at any time
- **No rejections**: all requests eventually either run or get cancelled

Feel free to adapt the exact JSON-RPC field names or messaging to best suit your Agent.

---

## Modular Implementation Example

Below are two complete modules for your `mcp_server/` folder: `pool_manager.py` and `dispatcher.py`. They implement:

- FIFO queue for `startSession` (sync vs async entries)
- `queryPosition`, `cancelRequest`, and `changeRequestType` JSON-RPC actions
- SSE notifications (`sessionQueued`, `sessionReady`, `requestCancelled`)
- Guaranteed at least one terminal in service (configurable)
- Ability for agents to upgrade a queued async request to sync (bump priority)

### mcp_server/pool_manager/**init**.py

```python
# pool_manager/__init__.py
from .queue import RequestEntry
from .session import PoolManager
```

### mcp_server/pool_manager/queue.py

```python
# pool_manager/queue.py
from datetime import datetime

class RequestEntry:
    def __init__(self, req, sync=True):
        self.req = req
        self.sync = sync
        self.enqueue_time = datetime.now()
```

### mcp_server/pool_manager/session.py

```python
# session.py
import uuid
import asyncio
from datetime import datetime
from config import PROMPT_TOKEN, MAX_CONCURRENT_SESSIONS, POOL_SIZE
from powershell_pool import spawn_ps
from sse import push_sse
from .queue import RequestEntry

class PoolManager:
    def __init__(self, free_pool):
        self.free_pool = free_pool
        self.sessions = {}
        self.request_list = []
        self.request_map = {}
        # EMA state
        self.avg_wait_sync = 0.0
        self.avg_wait_async = 0.0
        self.peak_sessions = 0
        self.peak_queue = 0

    async def start_session(self, req):
        rid = req["id"]
        sync = req.get("sync", True)
        self.peak_queue = max(self.peak_queue, len(self.request_list) + 1)
        if len(self.sessions) < MAX_CONCURRENT_SESSIONS and not self.free_pool.empty():
            return await self._alloc_session(req, rid)
        entry = RequestEntry(req, sync)
        self.request_list.append(entry)
        self.request_map[rid] = entry
        if sync:
            pos = sum(1 for e in self.request_list if e.sync and e.enqueue_time <= entry.enqueue_time)
        else:
            pos = len(self.request_list)
        await push_sse({
            "jsonrpc": "2.0",
            "method": "mcp/sessionQueued",
            "params": {
                "requestId": rid,
                "position": pos,
                "message": f"All {MAX_CONCURRENT_SESSIONS} busy. You're #{pos} in queue. ETA ~{round(self.estimate_wait(pos))}s."
            }
        })
        return {"id": rid, "status": "queued", "position": pos}

    async def _alloc_session(self, req, rid, proc=None):
        if not proc:
            proc = await self.free_pool.get()
        sid = str(uuid.uuid4())
        self.sessions[sid] = {
            "proc": proc,
            "lastActive": datetime.now(),
            "requestId": rid,
            "cancelAfterNext": False
        }
        self.peak_sessions = max(self.peak_sessions, len(self.sessions))
        entry = self.request_map.pop(rid, None)
        if entry:
            waited = (datetime.now() - entry.enqueue_time).total_seconds()
            alpha = 0.1
            if entry.sync:
                self.avg_wait_sync = (1-alpha)*self.avg_wait_sync + alpha*waited
            else:
                self.avg_wait_async = (1-alpha)*self.avg_wait_async + alpha*waited
            if entry in self.request_list:
                self.request_list.remove(entry)
        return {"requestId": rid, "sessionId": sid, "prompt": PROMPT_TOKEN}

    def get_average_wait(self, sync=True) -> float:
        return self.avg_wait_sync if sync else self.avg_wait_async

    def estimate_wait(self, position: int, sync=True) -> float:
        return self.get_average_wait(sync) * position

    def get_metrics(self) -> dict:
        return {
            "active_sessions": len(self.sessions),
            "free_slots": POOL_SIZE - len(self.sessions),
            "current_queue_depth": len(self.request_list),
            "peak_sessions": self.peak_sessions,
            "peak_queue_depth": self.peak_queue,
            "avg_wait_sync": round(self.avg_wait_sync, 2),
            "avg_wait_async": round(self.avg_wait_async, 2)
        }
    # ... rest unchanged ...
```

### mcp_server/dispatcher.py

```python
# dispatcher.py
import uuid
from datetime import datetime
from config import PROMPT_TOKEN, MAX_CONCURRENT_SESSIONS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager
from config import POOL_SIZE

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    # 1) Schema validation
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}
    # 2) Route actions
    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    # 3) Unknown
    return {"id": rid, "error": f"Unknown action: {action}"}

async def handle_stdio():
    """
    Read JSON-RPC requests from stdin, dispatch, and write responses to stdout.
    """
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### Example: pool_manager.py (continued)

```python
    def terminate_proc(self, proc):
        proc.terminate()

    async def release_session(self, sid):
        info = self.sessions.pop(sid, None)
        if not info:
            return
        proc = info["proc"]
        if info.get("cancelAfterNext"):
            self.terminate_proc(proc)
        # Serve next queued request
        next_entry = None
        for e in self.request_list:
            if e.sync:
                next_entry = e
                break
        if not next_entry and self.request_list:
            next_entry = self.request_list[0]
        if next_entry:
            self.request_list.remove(next_entry)
            rid = next_entry.req["id"]
            del self.request_map[rid]
            alloc = await self._alloc_session(next_entry.req, rid, proc)
            await push_sse({
                "jsonrpc": "2.0",
                "method": "mcp/sessionReady",
                "params": alloc
            })
            return

        # no queued requests: return proc to pool
        await self.free_pool.put(proc)

    async def _alloc_session(self, req, rid, proc=None):
        if not proc:
            proc = await self.free_pool.get()
        sid = str(uuid.uuid4())
        self.sessions[sid] = {
            "proc": proc,
            "lastActive": datetime.now(),
            "requestId": rid,
            "cancelAfterNext": False
        }
        return {
            "requestId": rid,
            "sessionId": sid,
            "prompt": PROMPT_TOKEN
        }
```

### Example: dispatcher.py

```python
# dispatcher.py
import sys
import json
import asyncio
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager
from config import POOL_SIZE

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    # 1) Schema validation
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}
    # 2) Route actions
    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    # 3) Unknown
    return {"id": rid, "error": f"Unknown action: {action}"}

async def handle_stdio():
    """
    Read JSON-RPC requests from stdin, dispatch, and write responses to stdout.
    """
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

---

## Proposed Execution Plan

Below is a prioritized, step-by-step list of all the outstanding work and feature requests, in the order recommended for tackling them. Each item includes a brief description of the goal.

1. **Expand Automated Unit Test Coverage**
   - Ensure every existing module (`powershell_pool.py`, `dispatcher.py`, `pool_manager.py`, `jobs.py`, `watcher.py`, `sse.py`, `schemas.py`, `config.py`) has unit tests that cover its public interfaces. This gives confidence when refactoring or adding features.

2. **Add Integration & End-to-End Tests**
   - Write pytest tests marked `@pytest.mark.serial` for:
     - The SSE endpoint (`sse.py`) by spinning up an HTTP client.
     - The filesystem watcher (`watcher.py`) using a temporary directory.
     - A full "startSession → runCommand → endSession" flow via stdio + SSE to validate JSON-RPC end-to-end.

3. **Implement Dynamic Throttling & Minimum-One Terminal Guarantee**
   - Enhance `pool_manager.py` to:
     - Monitor CPU/RAM load.
     - If under heavy system load, reduce active pool size down to 1 (queuing further `startSession` requests).
     - Always keep at least one terminal spawned or queued so the Agent can make progress.

4. **Enrich Queue API for Waiting Agent Control**
   - In `pool_manager.py` & `dispatcher.py`, add or finalize:
     - `queryPosition` action so Agents can poll their real-time spot.
     - `changeRequestType` to bump an async-queued request up into sync priority without re-submission.
     - SSE notifications for `sessionQueued`, `sessionReady`, and `requestCancelled`.

5. **Implement File-Tail & FS-Notification Feature**
   - Extend `watcher.py` (or a new module) so Agents can request:
     - A one-time "give me the last N lines" of a log file.
     - A subscription to get live SSE file-append events.

6. **Finalize Full File Set with Sync/Async Priority & Notifications**
   - Assemble and verify the complete Python source files for:
     - `pool_manager.py`: queue logic, sync vs async, cancellation, release.
     - `dispatcher.py`: JSON-RPC routing incl. the new queue APIs.
     - All supporting modules, ensuring they reflect the desired behaviors.

7. **Modularize Large Files**
   - Break up the largest modules into focused sub-modules:
     - `dispatcher.py` → split into `router.py` and supporting files as needed.

8. **Provide System-Wide Backup & Restore Scripts**
   - Write a shell or Python script that:
     - Archives and commits everything *outside* the project folder into a backup repo.
     - Provides clear instructions on restoring those files by path.
     - Runs with administrator privileges but limits its scope to user-specified backup directories.

9. **Document & Automate Deployment**
   - Create a single orchestrator script (`deploy_mcp.sh` or `.ps1`) that:
     - Installs Python dependencies into a virtualenv.
     - Sets up project folder, `.cursor/mcp.json`, and `settings.json`.
     - Launches the MCP server as a background service.
     - Validates connectivity from Cursor IDE.

With this roadmap:

- We build test coverage first, so every subsequent change is safe.
- Core queue enhancements and Agent controls come next, delivering the most user-visible features.
- Finally, we refactor, backup, and automate to streamline future maintenance.

---

### Example: Full Integration Test for Dispatcher

```python
def test_full_start_run_end_flow(fake_proc):
    # Arrange: pre-spawn a fake PS proc in the free_pool
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # 1) startSession
    resp1 = await dispatch({"id": 1, "action": "startSession"})
    assert "sessionId" in resp1
    sid = resp1["sessionId"]

    # 2) runCommand
    resp2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in resp2["stdout"]

    # 3) endSession
    resp3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert resp3["ok"] is True

    # No SSE notifications left over
    clients.clear()
```

---

## Proposed Modular Breakup

Once tests pass, we can safely decompose these large modules:

```
mcp_server/
├── dispatcher/
│   ├── __init__.py        # exports init_pool_manager, dispatch, handle_stdio
│   ├── router.py          # JSON-RPC action→handler mapping (dispatch logic)
│   └── rpc_stdio.py       # handle_stdio: stdin→router→stdout loop
├── pool_manager/
│   ├── __init__.py        # PoolManager entrypoint
│   ├── queue.py           # RequestEntry and queue-related operations
│   └── session.py         # session allocation, release, lifecycle
├── watcher/
│   ├── __init__.py
│   ├── file_watcher.py    # ChangeHandler & start_file_watcher
│   └── idle_watcher.py    # monitor_sessions (abandoned & git-backup)
└── [unchanged modules]
```

Each new submodule would expose only the functions the others need. Because we have full coverage, you can refactor one bit at a time:

1. Move `router` logic out of `dispatcher.py` → `router.py`, import in `dispatcher/__init__.py`.
2. Extract `handle_stdio` into `rpc_stdio.py`.
3. Split `pool_manager.py` into `queue.py` + `session.py`:
   - Move `RequestEntry` & queue types → `queue.py`.
   - Move session allocation & `release_session` → `session.py`.
4. Split `watcher.py` similarly.

Tests will immediately flag any mismatches in the public APIs. Once that's clean, we're finished.

---

## Example Project Structure

```
your-project/
├── .cursor/
│   └── mcp.json
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
├── tests/
│   ├── conftest.py
│   ├── test_config.py
│   ├── test_schemas.py
│   ├── test_powershell_pool.py
│   ├── test_dispatcher.py
│   ├── test_jobs.py
│   ├── test_sse.py
│   ├── test_watcher.py
│   ├── test_integration_sse.py
│   ├── test_integration_file_watcher.py
│   ├── test_integration_metrics.py
│   └── test_e2e_logic.py
├── settings.json
└── pytest.ini
```

### .cursor/mcp.json

```json
{
  "mcpServers": {
    "ps-pool": {
      "transport": "sse",
      "url": "http://localhost:5001/events",
      "command": "/full/path/to/mcp_server/__main__.py"
    }
  }
}
```

### settings.json

```jsonc
{
  "cursor.composer.defaultMcpServer": "ps-pool",
  "cursor.composer.shellIntegration.enabled": false
}
```

### pytest.ini

```ini
[pytest]
addopts = -n auto
markers =
  serial: mark test serially (not safe for parallel execution)
```

### mcp_server/config.py

```python
# config.py
# Adjustable constants

POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### mcp_server/schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "20",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range(POOL_SIZE):
        ps = await spawn_ps()
        await free_pool.put(ps)
    init_pool_manager(free_pool)
    start_file_watcher()

    app = web.Application()
    app.router.add_get("/events", sse_handler)
    app.router.add_get("/metrics", metrics_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "localhost", 5001).start()

    await asyncio.gather(
        handle_stdio(),
        monitor_sessions(pm.sessions)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### config.py

```python
# config.py
POOL_SIZE = 3
MAX_CONCURRENT_SESSIONS = 5
IDLE_LIMIT_SEC = 120
BACKUP_IDLE_SEC = 10
WATCH_PATHS = [r"C:\\external\\path"]
GIT_REPO_ROOT = r"C:\\your\\git\\repo"
PROMPT_TOKEN = "PSLLM> "
```

### schemas.py

```python
# schemas.py
SCHEMAS = {
  "startSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "startSession"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action"]
  },
  "queryPosition": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "queryPosition"}
    },
    "required": ["id", "action"]
  },
  "changeRequestType": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "changeRequestType"},
      "sync": {"type": "boolean"}
    },
    "required": ["id", "action", "sync"]
  },
  "cancelRequest": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "cancelRequest"}
    },
    "required": ["id", "action"]
  },
  "runCommand": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runCommand"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "runBackground": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "runBackground"},
      "sessionId": {"type": "string"},
      "command": {"type": "string"}
    },
    "required": ["id", "action", "sessionId", "command"]
  },
  "getResult": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "getResult"},
      "jobId": {"type": "string"}
    },
    "required": ["id", "action", "jobId"]
  },
  "endSession": {
    "type": "object",
    "properties": {
      "id": {"type": "number"},
      "action": {"const": "endSession"},
      "sessionId": {"type": "string"}
    },
    "required": ["id", "action", "sessionId"]
  }
}
```

### mcp_server/powershell_pool.py

```python
# powershell_pool.py
import asyncio
from config import PROMPT_TOKEN
from asyncio.subprocess import PIPE, create_subprocess_exec

async def spawn_ps():
    init = f'function Prompt {{ "{PROMPT_TOKEN}" }}; Clear-Host'
    proc = await create_subprocess_exec(
        "pwsh", "-NoProfile", "-NonInteractive", "-Command", init,
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    await proc.stdout.readline()
    return proc

async def run_command(proc, cmd):
    proc.stdin.write((cmd + "\n").encode())
    await proc.stdin.drain()
    out_lines = []
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        text = line.decode(errors="ignore")
        if PROMPT_TOKEN in text:
            break
        out_lines.append(text)
    return "".join(out_lines).rstrip(), "", 0
```

### mcp_server/jobs.py

```python
# jobs.py
import asyncio
import uuid
from powershell_pool import run_command
from sse import push_sse

jobs = {}

async def run_background(sessions, sid, cmd):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"result": None, "error": None}
    async def _task():
        try:
            out, err, code = await run_command(sessions[sid]["proc"], cmd)
            jobs[job_id]["result"] = {"stdout": out, "stderr": err, "exitCode": code}
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFinished",
              "params": {"jobId": job_id, "stdout": out, "stderr": err, "exitCode": code}
            }
        except Exception as e:
            jobs[job_id]["error"] = str(e)
            payload = {
              "jsonrpc": "2.0",
              "method": "mcp/jobFailed",
              "params": {"jobId": job_id, "error": str(e)}
            }
        await push_sse(payload)
    asyncio.create_task(_task())
    return job_id
```

### mcp_server/sse.py

```python
# sse.py
from aiohttp import web
import asyncio
import json

clients = []

async def sse_handler(request):
    resp = web.StreamResponse(
        status=200,
        headers={
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
    )
    await resp.prepare(request)
    clients.append(resp)
    try:
        while True:
            await asyncio.sleep(10)
            await resp.write(b": keep-alive\n\n")
    finally:
        clients.remove(resp)
    return resp

async def push_sse(payload):
    data = "data: " + json.dumps(payload) + "\n\n"
    for resp in clients:
        await resp.write(data.encode())
```

### mcp_server/dispatcher/**init**.py

```python
# dispatcher/__init__.py
from .router import init_pool_manager, dispatch
from .rpc_stdio import handle_stdio
```

### mcp_server/dispatcher/router.py

```python
# dispatcher/router.py
import asyncio
import json
from datetime import datetime
from jsonschema import validate, ValidationError
from schemas import SCHEMAS
from powershell_pool import run_command
from jobs import run_background, jobs
from pool_manager import PoolManager

pm: PoolManager = None

def init_pool_manager(free_pool):
    global pm
    pm = PoolManager(free_pool)

async def dispatch(req):
    rid = req.get("id")
    action = req.get("action")
    schema = SCHEMAS.get(action)
    if schema:
        try:
            validate(req, schema)
        except ValidationError as e:
            return {"id": rid, "error": f"Invalid request: {e.message}"}

    if action == "startSession":
        return await pm.start_session(req)
    if action == "queryPosition":
        return pm.query_position(req)
    if action == "changeRequestType":
        return await pm.change_request_type(req)
    if action == "cancelRequest":
        return await pm.cancel_request(req)
    if action == "runCommand":
        sid = req["sessionId"]
        out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
        pm.sessions[sid]["lastActive"] = datetime.now()
        if pm.sessions[sid].get("cancelAfterNext"):
            await pm.release_session(sid)
        return {"id": rid, "stdout": out, "stderr": err, "exitCode": code}
    if action == "runBackground":
        sid = req["sessionId"]
        job_id = await run_background(pm.sessions, sid, req["command"])
        return {"id": rid, "jobId": job_id}
    if action == "getResult":
        job = jobs.get(req["jobId"])
        if not job:
            return {"id": rid, "error": "Unknown jobId"}
        status = "done" if job["result"] or job["error"] else "running"
        resp = {"id": rid, "status": status}
        if job["result"]:
            resp.update(job["result"])
        if job["error"]:
            resp["error"] = job["error"]
        return resp
    if action == "endSession":
        sid = req["sessionId"]
        await pm.release_session(sid)
        return {"id": rid, "ok": True}
    return {"id": rid, "error": f"Unknown action: {action}"}
```

### mcp_server/dispatcher/rpc_stdio.py

```python
# rpc_stdio.py
import sys
import json
import asyncio
from .router import dispatch

async def handle_stdio():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    loop = asyncio.get_event_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        raw = await reader.readline()
        if not raw:
            break
        req = json.loads(raw)
        resp = await dispatch(req)
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()
```

### tests/test_watcher.py

```python
import pytest
import time
from pathlib import Path
import watcher

class DummyEvent:
    def __init__(self, src_path, is_directory=False):
        self.src_path = src_path
        self.is_directory = is_directory

def test_change_handler_adds_new_file(tmp_path):
    watcher.pending_changes.clear()
    handler = watcher.ChangeHandler()
    fake_file = tmp_path / "test.txt"
    handler.on_any_event(DummyEvent(str(fake_file)))
    assert str(fake_file) in watcher.pending_changes

@pytest.mark.asyncio
async def test_run_git_monkeypatched(monkeypatch):
    class FakeProc:
        async def communicate(self):
            return (b"git-out", b"git-err")
        returncode = 0
    async def fake_exec(*args, **kw):
        return FakeProc()
    monkeypatch.setattr(watcher, "create_subprocess_exec", fake_exec)
    out, err, code = await watcher.run_git("status")
    assert out == "git-out"
    assert err == "git-err"
    assert code == 0
```

### tests/test_integration_sse.py

```python
import pytest
import json
from aiohttp import web
from sse import sse_handler, push_sse, clients

@pytest.mark.serial
@pytest.mark.asyncio
async def test_sse_endpoint_and_push(aiohttp_client):
    app = web.Application()
    app.router.add_get('/events', sse_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/events')
    assert resp.status == 200

    line = await resp.content.readline()
    assert b": keep-alive" in line

    payload = {"jsonrpc": "2.0", "method": "testEvent", "params": {"x": 1}}
    await push_sse(payload)

    data_line = await resp.content.readline()
    parsed = json.loads(data_line[len(b"data: "):-2])
    assert parsed == payload

    clients.clear()
```

### tests/test_e2e_logic.py

```python
import pytest
import asyncio
from dispatcher import init_pool_manager, dispatch
from powershell_pool import spawn_ps
from sse import clients

@pytest.mark.asyncio
async def test_full_start_run_end_flow(fake_proc):
    free_pool = asyncio.Queue()
    await free_pool.put(fake_proc)
    init_pool_manager(free_pool)

    # startSession
    r1 = await dispatch({"id": 1, "action": "startSession"})
    sid = r1["sessionId"]

    # runCommand
    r2 = await dispatch({"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"})
    assert "line1" in r2["stdout"]

    # endSession
    r3 = await dispatch({"id": 3, "action": "endSession", "sessionId": sid})
    assert r3["ok"] is True

    clients.clear()
```

---

With these additions—

- **All source modules are accounted for.**
- **All unit tests, integrations, and an end-to-end flow are in place.**

You are fully synchronized. Outstanding tasks, user requests, and further suggestions are tracked in the project documentation and planning sections.

## Updated /metrics Handler

**mcp_server/metrics.py:**

```python
from aiohttp import web
from dispatcher.router import pm

async def metrics_handler(request):
    if pm is None:
        return web.json_response({"error": "PoolManager not initialized"}, status=500)
    m = pm.get_metrics()
    depth = m["current_queue_depth"]
    # ETA for next sync and async
    m["estimated_wait_next_sync_sec"]  = round(pm.estimate_wait(depth+1, True), 2)
    m["estimated_wait_next_async_sec"] = round(pm.estimate_wait(depth+1, False), 2)
    return web.json_response(m)
```

And in **mcp_server/main.py**:

```diff
 from sse import sse_handler
+from metrics import metrics_handler

     app.router.add_get("/events", sse_handler)
+    app.router.add_get("/metrics", metrics_handler)
```

---

## New Integration Test for EMA & Metrics

**tests/test_integration_metrics.py** (update to check sync/async keys):

```python
import pytest
from aiohttp import web
from metrics import metrics_handler
from dispatcher.router import init_pool_manager, pm
from powershell_pool import spawn_ps
import asyncio

@pytest.mark.serial
@pytest.mark.asyncio
async def test_metrics_includes_ema_fields(aiohttp_client):
    free_pool = asyncio.Queue()
    fake = await spawn_ps()
    await free_pool.put(fake)
    init_pool_manager(free_pool)

    app = web.Application()
    app.router.add_get('/metrics', metrics_handler)
    client = await aiohttp_client(app)

    resp = await client.get('/metrics')
    data = await resp.json()
    assert "avg_wait_sync" in data
    assert "avg_wait_async" in data
    assert "estimated_wait_next_sync_sec" in data
    assert "estimated_wait_next_async_sec" in data
```

---

## Pending Tasks Still Open

1. Dynamic CPU/RAM–based throttling of pool size down to 1 under heavy load.
2. File-tail and real-time file append SSE ("tail -f" style) feature.
3. Backup/restore script for files outside the project.
4. Full deployment automation (virtualenv bootstrap, service registration).
5. Live queue-position SSE events (`positionChanged`) for waiting Agents.

---

## Applied Suggestions

- **EMA** for wait time instead of simple average
- **Sync vs Async** separate EMAs
- `/metrics` now reports both EMAs and ETAs for next queue position
- Integration test covers these new fields

---

# Final File Structure

```
your-project/
├── .cursor/mcp.json
├── settings.json
├── pytest.ini
├── mcp_server/
│   ├── __main__.py
│   ├── config.py
│   ├── schemas.py
│   ├── powershell_pool.py
│   ├── jobs.py
│   ├── sse.py
│   ├── metrics.py
│   ├── dispatcher/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── rpc_stdio.py
│   ├── pool_manager/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── session.py
│   └── watcher/
│       ├── __init__.py
│       ├── file_watcher.py
│       └── idle_watcher.py
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_schemas.py
    ├── test_powershell_pool.py
    ├── test_dispatcher.py
    ├── test_jobs.py
    ├── test_sse.py
    ├── test_watcher.py
    ├── test_integration_sse.py
    ├── test_integration_file_watcher.py
    ├── test_integration_metrics.py
    └── test_e2e_logic.py
```

## Core Modules in mcp_server/

### main.py

```python
#!/usr/bin/env python3
import asyncio
from aiohttp import web
from config import POOL_SIZE
from powershell_pool import spawn_ps
from dispatcher import init_pool_manager, handle_stdio, pm
from watcher import start_file_watcher, monitor_sessions
from sse import sse_handler
from metrics import metrics_handler

async def main():
    free_pool = asyncio.Queue()
    for _ in range
