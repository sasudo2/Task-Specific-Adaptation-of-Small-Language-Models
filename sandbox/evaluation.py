import json
import subprocess
import requests
from code_extractor import extract_function

IMAGE = "python-sandbox"

def generate_code(prompt):
    response = requests.post('http://localhost:5000/generate', json={'prompt': prompt})
    return response.json()['code']

def run_in_docker(code, fn_name, test, limits):
    payload = {
        "code": code,
        "fn_name": fn_name,
        "input": test["input"],
        "time_limit_ms": limits["time_limit_ms"]
    }

    cmd = [
        "docker", "run", "--rm", "-i",
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

    if proc.returncode != 0:
        print(f"Docker error: {proc.stderr}")
        return {"status": "docker_error", "error": proc.stderr}
    
    if not proc.stdout.strip():
        print(f"Empty docker output for fn {fn_name}")
        return {"status": "docker_error", "error": "Empty output"}
    
    return json.loads(proc.stdout)

def run_problem(problem):
    prompt = f"{problem['prompt']}\n{problem['function_signature']}"
    model_output = generate_code(prompt)
    
    # Append generated output to file
    with open("generated_outputs.txt", "a") as f:
        f.write(f"\n{'='*80}\n")
        f.write(f"Problem ID: {problem['id']}\n")
        f.write(f"{'='*80}\n")
        f.write(model_output)
        f.write("\n")

    fn_name = problem["function_signature"].split("(")[0].replace("def ", "").strip()
    try:
        code = extract_function(model_output, fn_name)
    except Exception as e:
        print(f"Extraction error for {fn_name}: {e}")
        return {"id": problem["id"], "status": "compile_error", "error": str(e)}

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
