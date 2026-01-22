import json
import subprocess
from model_runner import generate_code
from code_extractor import extract_function

IMAGE = "leetcode-sandbox"

def run_in_docker(code, fn_name, test, limits):
    payload = {
        "code": code,
        "fn_name": fn_name,
        "input": test["input"],
        "time_limit_ms": limits["time_limit_ms"]
    }

    cmd = [
        "docker", "run", "--rm",
        "--network", "none",
        "--memory", f"{limits['memory_limit_kb']}k",
        "--cpus", "1",
        IMAGE
    ]

    proc = subprocess.run(
        cmd,
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        timeout=limits["time_limit_ms"] / 1000 + 2
    )

    return json.loads(proc.stdout)

def run_problem(problem):
    prompt = f"{problem['prompt']}\n{problem['function_signature']}"
    model_output = generate_code(prompt)

    fn_name = problem["function_signature"].split("(")[0].replace("def ", "")
    try:
        code = model_output
    except Exception:
        return {"id": problem["id"], "status": "compile_error"}

    for test in problem["hidden_tests"]:
        result = run_in_docker(
            code,
            fn_name,
            test,
            problem
        )

        if result["status"] != "ok":
            return {"id": problem["id"], "status": result["status"]}

        if result["result"] != test["output"]:
            return {"id": problem["id"], "status": "wrong_answer"}

    return {"id": problem["id"], "status": "accepted"}

def main():
    problems = json.load(open("leetcode_eval_set.json"))
    results = [run_problem(p) for p in problems]

    json.dump(results, open("results.json", "w"), indent=2)
    print("Evaluation finished")

if __name__ == "__main__":
    main()
