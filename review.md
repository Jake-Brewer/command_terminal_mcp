# Code Review Findings

## 1. Undefined Variable: `pending_changes` in `mcp_server/watcher`

### Problem

The variable `pending_changes` is referenced in multiple files within the `mcp_server/watcher` module:

- `file_watcher.py` (used in `ChangeHandler` and imported from `.`)
- `idle_watcher.py` (imported from `.file_watcher`)
- `__init__.py` (re-exported from `idle_watcher`)

However, **`pending_changes` is never defined in any of these files**. This will result in an `ImportError` or `NameError` at runtime whenever any watcher logic is invoked.

### How to Reproduce

1. Attempt to start the server or import any watcher module:

   ```python
   from watcher import start_file_watcher
   # or
   from watcher import monitor_sessions
   ```

2. You will receive an error similar to:

   ```
   ImportError: cannot import name 'pending_changes' from 'mcp_server.watcher.idle_watcher' (...)
   # or
   NameError: name 'pending_changes' is not defined
   ```

### Why This Happens

- `pending_changes` is used as if it is a shared set or list to track changed files, but it is never actually created.
- All references assume it is defined at the module or package level, but no such definition exists.

### How to View/Verify

- Open `mcp_server/watcher/file_watcher.py`, `idle_watcher.py`, and `__init__.py`.
- Search for `pending_changes` and note the lack of any assignment like `pending_changes = set()` or similar.

### Suggested Fix

- Define `pending_changes = set()` (or appropriate collection) in a single location, such as `mcp_server/watcher/__init__.py`, and import it everywhere it is needed.

---

## 2. Potential Test Failure: Unexpected Assertion in `test_e2e_logic.py`

### Problem

In `tests/test_e2e_logic.py`, the following assertion is made after running a PowerShell command:

```python
assert "line1" in r2["stdout"]
```

However, the command being run is:

```python
{"id": 2, "action": "runCommand", "sessionId": sid, "command": "echo hi"}
```

The output of `echo hi` in PowerShell is expected to be `hi`, not `line1`. This assertion will likely fail unless the PowerShell environment or the `run_command` function is specifically modified to prepend `line1` to the output, which is not evident in the codebase.

### How to Reproduce

1. Run the test suite:

   ```powershell
   pytest tests/test_e2e_logic.py
   ```

2. Observe the failure at the assertion:

   ```
   assert "line1" in r2["stdout"]
   AssertionError: ...
   ```

### Why This Happens

- The test expects the output to contain `line1`, but the actual output of `echo hi` is just `hi`.
- There is no code in `run_command` or the PowerShell pool logic that would prepend or transform the output to include `line1`.

### How to View/Verify

- Open `tests/test_e2e_logic.py` and review the assertion.
- Check the implementation of `run_command` in `mcp_server/powershell_pool.py` to confirm the output is not altered.
- Manually run `echo hi` in PowerShell to see the output is `hi`.

### Suggested Fix

- Update the assertion to:

  ```python
  assert "hi" in r2["stdout"]
  ```

- Or, if the output is expected to be different, ensure the test and implementation are aligned.

---

## 3. Integration Test Failure: `pending_changes` Not Defined in `test_integration_file_watcher.py`

### Problem

In `tests/test_integration_file_watcher.py`, the test directly accesses `watcher.pending_changes`:

```python
watcher.pending_changes.clear()
...
assert str(new_file) in watcher.pending_changes
```

However, as previously documented, `pending_changes` is **not defined anywhere in the watcher module**. This will cause an `AttributeError` when the test is run.

### How to Reproduce

1. Run the test suite:

   ```powershell
   pytest tests/test_integration_file_watcher.py
   ```

2. Observe the failure:

   ```
   AttributeError: module 'watcher' has no attribute 'pending_changes'
   ```

### Why This Happens

- The test expects `pending_changes` to be a set or similar collection defined at the module level in `watcher`, but it is missing from the codebase.

### How to View/Verify

- Open `tests/test_integration_file_watcher.py` and note the direct access to `watcher.pending_changes`.
- Check the `mcp_server/watcher` package and confirm there is no definition or assignment for `pending_changes`.

### Suggested Fix

- Define `pending_changes = set()` in `mcp_server/watcher/__init__.py` and ensure it is imported and used consistently throughout the watcher module and tests.

---

## 4. Incomplete Test: Truncated Assertion in `test_integration_metrics.py`

### Problem

In `tests/test_integration_metrics.py`, the last line of the test is:

```python
assert "estimated_wait_next_sync_sec
```

This line is incomplete and will cause a `SyntaxError` or `IndentationError` when the test is run. The assertion is not finished and is missing the closing quote, parenthesis, and the actual assertion logic.

### How to Reproduce

1. Run the test suite:

   ```powershell
   pytest tests/test_integration_metrics.py
   ```

2. Observe the failure:

   ```
   SyntaxError: EOL while scanning string literal
   # or
   IndentationError: unexpected EOF while parsing
   ```

### Why This Happens

- The test file is truncated or was not saved completely, resulting in an incomplete assertion.

### How to View/Verify

- Open `tests/test_integration_metrics.py` and scroll to the last line to see the incomplete assertion.

### Suggested Fix

- Complete the assertion, for example:

  ```python
  assert "estimated_wait_next_sync_sec" in data
  ```

- Review the rest of the test to ensure all assertions are present and correct.

---

## 5. Test Failure: `pending_changes` Not Defined in `test_watcher.py`

### Problem

In `tests/test_watcher.py`, the test directly accesses `watcher.pending_changes`:

```python
watcher.pending_changes.clear()
...
assert str(fake_file) in watcher.pending_changes
```

As previously documented, `pending_changes` is **not defined anywhere in the watcher module**. This will cause an `AttributeError` when the test is run.

### How to Reproduce

1. Run the test suite:

   ```powershell
   pytest tests/test_watcher.py
   ```

2. Observe the failure:

   ```
   AttributeError: module 'watcher' has no attribute 'pending_changes'
   ```

### Why This Happens

- The test expects `pending_changes` to be a set or similar collection defined at the module level in `watcher`, but it is missing from the codebase.

### How to View/Verify

- Open `tests/test_watcher.py` and note the direct access to `watcher.pending_changes`.
- Check the `mcp_server/watcher` package and confirm there is no definition or assignment for `pending_changes`.

### Suggested Fix

- Define `pending_changes = set()` in `mcp_server/watcher/__init__.py` and ensure it is imported and used consistently throughout the watcher module and tests.

---

## 6. Test Failure: Unexpected Assertion in `test_powershell_pool.py`

### Problem

In `tests/test_powershell_pool.py`, the following assertion is made after running a PowerShell command:

```python
assert "line1" in out
```

However, the command being run is:

```python
out, err, code = await run_command(fake_proc, "echo hi")
```

The output of `echo hi` in PowerShell is expected to be `hi`, not `line1`. This assertion will likely fail unless the PowerShell environment or the `run_command` function is specifically modified to prepend `line1` to the output, which is not evident in the codebase.

### How to Reproduce

1. Run the test suite:

   ```powershell
   pytest tests/test_powershell_pool.py
   ```

2. Observe the failure at the assertion:

   ```
   assert "line1" in out
   AssertionError: ...
   ```

### Why This Happens

- The test expects the output to contain `line1`, but the actual output of `echo hi` is just `hi`.
- There is no code in `run_command` or the PowerShell pool logic that would prepend or transform the output to include `line1`.

### How to View/Verify

- Open `tests/test_powershell_pool.py` and review the assertion.
- Check the implementation of `run_command` in `mcp_server/powershell_pool.py` to confirm the output is not altered.
- Manually run `echo hi` in PowerShell to see the output is `hi`.

### Suggested Fix

- Update the assertion to:

  ```python
  assert "hi" in out
  ```

- Or, if the output is expected to be different, ensure the test and implementation are aligned.

---

## 7. Test Fixture Quirk: `fake_proc` Feeds 'line1' Into Output in `conftest.py`

### Problem

In `tests/conftest.py`, the `fake_proc` fixture feeds the string `line1` into the fake PowerShell process output:

```python
proc.stdout.feed_data(b"line1\n")
proc.stdout.feed_data(powershell_pool.PROMPT_TOKEN.encode() + b"\n")
```

This means that any test using `fake_proc` will see `line1` in the output, regardless of the command being run. This explains why some tests expect 'line1' in the output, even though the real PowerShell output would be different (e.g., `hi` for `echo hi`).

### How to Reproduce

- Review the `fake_proc` fixture in `tests/conftest.py`.
- Run any test that uses `fake_proc` and observe that `line1` appears in the output.

### Why This Happens

- The fixture is designed to simulate a PowerShell process, but it always outputs `line1` followed by the prompt token, regardless of the command.
- This can mask real output differences and reduce the reliability of tests that check for actual command output.

### How to View/Verify

- Open `tests/conftest.py` and review the `fake_proc` fixture.
- Check tests that use `fake_proc` and see if they assert on `line1` in the output.

### Suggested Fix

- Update the fixture to allow customizable output based on the command, or ensure that tests check for the correct simulated output.
- Align test assertions with the intended behavior of the fixture and the real PowerShell output.

---

## 8. Potential Startup Issue: `start_file_watcher()` Is Not Awaited in `__main__.py`

### Problem

In `mcp_server/__main__.py`, the function `start_file_watcher()` is called without `await`, while `monitor_sessions()` is awaited as part of `asyncio.gather`:

```python
init_pool_manager(free_pool)
start_file_watcher()
...
await asyncio.gather(handle_stdio(), monitor_sessions(pm.sessions))
```

If `start_file_watcher()` is not asynchronous but performs blocking operations, this could block the event loop or cause unexpected behavior. If it is intended to be asynchronous, it should be awaited or scheduled as a task.

### How to Reproduce

- Review the implementation of `start_file_watcher()` in `mcp_server/watcher/file_watcher.py`.
- Run the server and observe if the event loop is blocked or if file watching does not work as expected.

### Why This Happens

- `start_file_watcher()` is a synchronous function that starts a daemon thread for file watching using `watchdog`. This is generally safe, but if the function is ever refactored to be asynchronous or to perform blocking work, this pattern could cause issues.

### How to View/Verify

- Open `mcp_server/__main__.py` and review the startup sequence.
- Open `mcp_server/watcher/file_watcher.py` and confirm the implementation of `start_file_watcher()`.

### Suggested Fix

- If `start_file_watcher()` remains synchronous and non-blocking, document this clearly.
- If it is refactored to be asynchronous, ensure it is properly awaited or scheduled as a background task.

---

## 9. Potential Subprocess Termination Issue in `PoolManager.release_session`

### Problem

In `mcp_server/pool_manager/session.py`, the `release_session` method calls `proc.terminate()` if `cancelAfterNext` is set:

```python
if info.get("cancelAfterNext"):
    proc.terminate()
```

However, `proc` is an `asyncio.subprocess.Process` object, and `terminate()` may not work as expected on Windows, especially for PowerShell processes. Additionally, this call is not awaited or checked for errors, and abrupt termination can leave resources uncleaned or orphaned.

### How to Reproduce

- Trigger a session cancellation that sets `cancelAfterNext` to `True` and observe whether the PowerShell process is actually terminated on Windows.
- Check for orphaned processes or resource leaks after repeated session cancellations.

### Why This Happens

- `asyncio.subprocess.Process.terminate()` sends a SIGTERM signal, which is not always supported or effective on Windows, especially for non-console processes.
- There is no error handling or confirmation that the process was actually terminated.

### How to View/Verify

- Open `mcp_server/pool_manager/session.py` and review the `release_session` method.
- Monitor system processes after session cancellation to see if PowerShell processes remain.

### Suggested Fix

- Use platform-specific logic to terminate subprocesses reliably on Windows (e.g., use `taskkill` or ensure the process is a child of the Python process).
- Add error handling and confirmation that the process was terminated.
- Consider using `await proc.wait()` after termination to ensure cleanup.

---

## 10. Error Output Ignored in `run_command` in `powershell_pool.py`

### Problem

In `mcp_server/powershell_pool.py`, the `run_command` function always returns an empty string for `stderr`, regardless of what the PowerShell process actually outputs to stderr:

```python
return "".join(out_lines).rstrip(), "", 0
```

This means that any errors or warnings written to stderr by PowerShell commands are silently ignored and not surfaced to the caller.

### How to Reproduce

- Run a command that produces output on stderr (e.g., an invalid command) using `run_command`.
- Observe that the returned `stderr` value is always `""`, even if the command failed or produced error output.

### Why This Happens

- The function only reads from `proc.stdout` and never reads from `proc.stderr`.
- The returned tuple always has `""` for the stderr value.

### How to View/Verify

- Open `mcp_server/powershell_pool.py` and review the `run_command` function.
- Add a test or manual call to `run_command` with a command that produces stderr output and observe the result.

### Suggested Fix

- Read from `proc.stderr` in addition to `proc.stdout` and return the actual error output.
- Update the return statement to include the real stderr value.

---

## 11. Missing Session Validation in `dispatch` in `router.py`

### Problem

In `mcp_server/dispatcher/router.py`, the `dispatch` function does not check whether the provided `sessionId` exists in `pm.sessions` before accessing it:

```python
sid = req["sessionId"]
out, err, code = await run_command(pm.sessions[sid]["proc"], req["command"])
```

If a request is made with an invalid or missing `sessionId`, this will raise a `KeyError` and potentially crash the server or cause an unhandled exception.

### How to Reproduce

- Send a `runCommand`, `runBackground`, or `endSession` request with an invalid or missing `sessionId`.
- Observe the server logs or response for a `KeyError`.

### Why This Happens

- There is no validation or error handling for the presence of `sessionId` in `pm.sessions`.

### How to View/Verify

- Open `mcp_server/dispatcher/router.py` and review the `dispatch` function.
- Check the code paths for `runCommand`, `runBackground`, and `endSession` actions.

### Suggested Fix

- Add validation to check if `sid` exists in `pm.sessions` before accessing it.
- Return a meaningful error message if the session is not found.

---

## 12. Potential Concurrency Issue with `clients` List in `sse.py`

### Problem

In `mcp_server/sse.py`, the global `clients` list is modified (appended to and removed from) by different coroutines without any synchronization:

```python
clients.append(resp)
...
clients.remove(resp)
...
for resp in clients:
    await resp.write(data.encode())
```

If a client disconnects while `push_sse` is iterating over `clients`, this could raise a `RuntimeError` due to concurrent modification, or result in missed or duplicated messages.

### How to Reproduce

- Open multiple SSE connections and trigger events while clients are connecting/disconnecting.
- Observe for `RuntimeError: list changed size during iteration` or missed events.

### Why This Happens

- The list is not protected by a lock or any concurrency mechanism, so modifications during iteration can cause errors.

### How to View/Verify

- Open `mcp_server/sse.py` and review the use of the `clients` list.
- Simulate rapid connect/disconnect and event pushes.

### Suggested Fix

- Use an `asyncio.Lock` to protect access to the `clients` list, or use a thread-safe collection.
- Consider iterating over a copy of the list in `push_sse` to avoid modification during iteration.

---

## 13. Global State Dependency in `metrics_handler` in `metrics.py`

### Problem

In `mcp_server/metrics.py`, the `metrics_handler` function relies on the global `pm` variable imported from `dispatcher.router`:

```python
from dispatcher.router import pm
...
if pm is None:
    return web.json_response({"error": "PoolManager not initialized"}, status=500)
```

If the server is not started via `__main__.py` (e.g., during tests or in a different context), `pm` may not be initialized, causing the handler to always return an error.

### How to Reproduce

- Call the `/metrics` endpoint before `init_pool_manager` is called, or in a test that does not initialize the pool manager.
- Observe that the response is always an error about the pool manager not being initialized.

### Why This Happens

- The handler depends on a global variable that is only set by a specific startup sequence.

### How to View/Verify

- Open `mcp_server/metrics.py` and review the use of `pm`.
- Run the server or tests without calling `init_pool_manager` and access the `/metrics` endpoint.

### Suggested Fix

- Refactor to avoid reliance on global state, or ensure that `init_pool_manager` is always called before the handler is used.
- Consider dependency injection or application context for better testability and reliability.

---

## 14. ImportError: `pending_changes` Not Defined in `watcher/__init__.py`

### Problem

In `mcp_server/watcher/__init__.py`, the following import is present:

```python
from .idle_watcher import monitor_sessions, run_git, pending_changes
```

However, `pending_changes` is **not defined** in `idle_watcher.py`, nor in any other file in the watcher package. This will cause an `ImportError` at runtime or when importing the watcher module.

### How to Reproduce

- Attempt to import anything from `mcp_server.watcher`:

  ```python
  from watcher import monitor_sessions
  ```

- Observe the error:

  ```
  ImportError: cannot import name 'pending_changes' from 'mcp_server.watcher.idle_watcher' (...)
  ```

### Why This Happens

- The import statement expects `pending_changes` to be defined in `idle_watcher.py`, but it is not present anywhere in the codebase.

### How to View/Verify

- Open `mcp_server/watcher/__init__.py` and `idle_watcher.py` and search for `pending_changes`.
- Attempt to import the watcher module in a Python shell or script.

### Suggested Fix

- Define `pending_changes = set()` in a single location (e.g., `__init__.py`) and import it everywhere it is needed.
- Remove or correct the faulty import.

---

## 15. ImportError: `pending_changes` Not Defined in `file_watcher.py`

### Problem

In `mcp_server/watcher/file_watcher.py`, the following import is present:

```python
from . import pending_changes
```

However, `pending_changes` is **not defined** anywhere in the watcher package. This will cause an `ImportError` at runtime or when importing the file_watcher module.

### How to Reproduce

- Attempt to import anything from `mcp_server.watcher.file_watcher`:

  ```python
  from watcher.file_watcher import ChangeHandler
  ```

- Observe the error:

  ```
  ImportError: cannot import name 'pending_changes' from 'mcp_server.watcher' (...)
  ```

### Why This Happens

- The import statement expects `pending_changes` to be defined at the package level, but it is not present anywhere in the codebase.

### How to View/Verify

- Open `mcp_server/watcher/file_watcher.py` and search for `pending_changes`.
- Attempt to import the file_watcher module in a Python shell or script.

### Suggested Fix

- Define `pending_changes = set()` in a single location (e.g., `__init__.py`) and import it everywhere it is needed.
- Remove or correct the faulty import.

---

## 16. ImportError: `pending_changes` Not Defined in `idle_watcher.py`

### Problem

In `mcp_server/watcher/idle_watcher.py`, the following import is present:

```python
from .file_watcher import pending_changes
```

However, `pending_changes` is **not defined** in `file_watcher.py`, nor in any other file in the watcher package. This will cause an `ImportError` at runtime or when importing the idle_watcher module.

### How to Reproduce

- Attempt to import anything from `mcp_server.watcher.idle_watcher`:

  ```python
  from watcher.idle_watcher import monitor_sessions
  ```

- Observe the error:

  ```
  ImportError: cannot import name 'pending_changes' from 'mcp_server.watcher.file_watcher' (...)
  ```

### Why This Happens

- The import statement expects `pending_changes` to be defined in `file_watcher.py`, but it is not present anywhere in the codebase.

### How to View/Verify

- Open `mcp_server/watcher/idle_watcher.py` and `file_watcher.py` and search for `pending_changes`.
- Attempt to import the idle_watcher module in a Python shell or script.

### Suggested Fix

- Define `pending_changes = set()` in a single location (e.g., `__init__.py`) and import it everywhere it is needed.
- Remove or correct the faulty import.

---

## 17. Unhandled Exceptions in `handle_stdio` in `rpc_stdio.py`

### Problem

In `mcp_server/dispatcher/rpc_stdio.py`, the `handle_stdio` function reads and parses JSON from stdin, but does not handle `json.JSONDecodeError` or other exceptions:

```python
req = json.loads(raw)
resp = await dispatch(req)
```

If malformed JSON is received, or if `dispatch` raises an exception, the process will crash or terminate unexpectedly.

### How to Reproduce

- Send malformed JSON to the process's stdin.
- Observe that the process crashes with a traceback.

### Why This Happens

- There is no try/except block around the JSON parsing or dispatch call.

### How to View/Verify

- Open `mcp_server/dispatcher/rpc_stdio.py` and review the `handle_stdio` function.
- Manually send invalid JSON to the process and observe the result.

### Suggested Fix

- Add try/except blocks to handle `json.JSONDecodeError` and other exceptions, and return a structured error response instead of crashing.

---

## 18. Hardcoded Windows Paths in `config.py`

### Problem

In `mcp_server/config.py`, the `WATCH_PATHS` and `GIT_REPO_ROOT` variables are hardcoded to Windows-style paths:

```python
WATCH_PATHS = [r"C:\external\path"]
GIT_REPO_ROOT = r"C:\your\git\repo"
```

This will not work on non-Windows platforms (e.g., Linux, macOS) and may cause errors or unexpected behavior if the code is run in a cross-platform environment.

### How to Reproduce

- Run the code on a non-Windows platform (e.g., Linux or macOS).
- Observe errors related to invalid paths or inability to watch or access the specified directories.

### Why This Happens

- The configuration is not platform-agnostic and assumes a specific directory structure and path separator.

### How to View/Verify

- Open `mcp_server/config.py` and review the values of `WATCH_PATHS` and `GIT_REPO_ROOT`.
- Attempt to run the code on a non-Windows system.

### Suggested Fix

- Use `os.path.join` or `pathlib.Path` to construct paths in a platform-independent way.
- Allow configuration via environment variables or a config file for better portability.

---

## 19. Missing Session Validation in `run_background` in `jobs.py`

### Problem

In `mcp_server/jobs.py`, the `run_background` function does not check whether the provided `sid` exists in the `sessions` dictionary before accessing it:

```python
out, err, code = await run_command(sessions[sid]["proc"], cmd)
```

If a request is made with an invalid or missing `sid`, this will raise a `KeyError` and potentially crash the background task or cause an unhandled exception.

### How to Reproduce

- Call `run_background` with a `sid` that does not exist in `sessions`.
- Observe the error in logs or the job result.

### Why This Happens

- There is no validation or error handling for the presence of `sid` in `sessions`.

### How to View/Verify

- Open `mcp_server/jobs.py` and review the `run_background` function.
- Check the code path for job creation and execution.

### Suggested Fix

- Add validation to check if `sid` exists in `sessions` before accessing it.
- Return a meaningful error message if the session is not found.

---

(Review complete. All major code and test files have been analyzed. See above for actionable findings.)
