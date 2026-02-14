import json
import sys
import time
import signal
import io
from contextlib import redirect_stdout

def timeout_handler(signum, frame):
    raise TimeoutError("Time limit exceeded")

# Set a signal for timeouts
signal.signal(signal.SIGALRM, timeout_handler)

def main():
    try:
        # Read the payload from the evaluation.py script
        input_data = sys.stdin.read()
        if not input_data:
            return
        
        payload = json.loads(input_data)
        code = payload["code"]
        test_input = payload["input"]
        time_limit = int(payload.get("time_limit_ms", 2000) / 1000)
        
        # 1. Mock stdin: Put the test case string into a buffer
        sys.stdin = io.StringIO(test_input)
        
        # 2. Mock stdout: Capture everything the script prints
        output_buffer = io.StringIO()
        
        # 3. Execution environment
        namespace = {"__name__": "__main__"}
        
        signal.alarm(max(1, time_limit))
        start_time = time.perf_counter()

        try:
            with redirect_stdout(output_buffer):
                exec(code, namespace)
            status = "ok"
            error_msg = None
        except TimeoutError:
            status = "TLE"
            error_msg = "Time Limit Exceeded"
        except Exception as e:
            status = "runtime_error"
            error_msg = str(e)
        finally:
            signal.alarm(0)

        runtime_ms = (time.perf_counter() - start_time) * 1000

        # Return the results as JSON
        print(json.dumps({
            "status": status,
            "result": output_buffer.getvalue().strip(),
            "runtime_ms": runtime_ms,
            "error": error_msg
        }))

    except Exception as e:
        print(json.dumps({"status": "system_error", "error": str(e)}))

if __name__ == "__main__":
    main()