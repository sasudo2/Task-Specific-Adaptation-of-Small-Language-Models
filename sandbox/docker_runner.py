import json
import sys
import time
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Time limit exceeded")

signal.signal(signal.SIGALRM, timeout_handler)

def main():
    payload = json.load(sys.stdin)
    code = payload["code"]
    fn_name = payload["fn_name"]
    test_input = payload["input"]
    time_limit = payload["time_limit_ms"] / 1000

    namespace = {}

    try:
        exec(code, namespace)
        fn = namespace[fn_name]
    except Exception as e:
        print(json.dumps({"status": "compile_error", "error": str(e)}))
        return

    signal.alarm(int(time_limit) + 1)
    start = time.perf_counter()

    try:
        result = fn(*test_input)
    except TimeoutError:
        print(json.dumps({"status": "TLE"}))
        return
    except Exception as e:
        print(json.dumps({"status": "runtime_error", "error": str(e)}))
        return
    finally:
        signal.alarm(0)

    elapsed = (time.perf_counter() - start) * 1000

    print(json.dumps({
        "status": "ok",
        "result": result,
        "runtime_ms": elapsed
    }))

if __name__ == "__main__":
    main()
