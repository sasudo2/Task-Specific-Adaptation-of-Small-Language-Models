import json
import subprocess
import os

IMAGE = "python-sandbox"


def run_in_docker(code, test_input, limits):

    wrapped_code = f"""
import sys
import ast

# -------- USER CODE --------
{code}
# ---------------------------

# Find solve() function
tree = ast.parse(\"\"\"{code}\"\"\")
has_solve = False

for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name == "solve":
        has_solve = True
        break

if not has_solve:
    print("NO_SOLVE_FUNCTION")
    exit()

# Read full input as ONE string
data = sys.stdin.read()

# Call solve(data)
try:
    result = solve(data)
except Exception as e:
    print("RUNTIME_ERROR:", e)
    exit()

# Print output
if result is not None:
    print(result)
"""

    payload = {
        "code": wrapped_code,
        "input": test_input,
        "time_limit_ms": limits.get("time_limit_ms", 2000)
    }

    cmd = [
        "docker", "run", "--rm", "-i",
        "--network", "none",
        "--memory", "256m",
        IMAGE
    ]

    try:
        proc = subprocess.run(
            cmd,
            input=json.dumps(payload),
            text=True,
            capture_output=True,
            timeout=(payload["time_limit_ms"] / 1000) + 2
        )

        if proc.returncode != 0:
            return {"status": "docker_error", "error": proc.stderr}

        return json.loads(proc.stdout)

    except subprocess.TimeoutExpired:
        return {"status": "TLE", "error": "Timeout"}

    except Exception as e:
        return {"status": "error", "error": str(e)}


def test_solution(problem_data, student_code):

    print(f"\n--- Testing Problem: {problem_data['name']} ---")

    all_passed = True

    for i, test in enumerate(problem_data["tests"]):

        response = run_in_docker(
            student_code,
            test["input"],
            problem_data
        )

        actual = str(response.get("result", "")).strip()
        expected = str(test["output"]).strip()

        if response.get("status") == "ok" and actual == expected:

            print(f"Test {i}: PASSED ({response['runtime_ms']:.2f} ms)")

        else:
            all_passed = False

            print(f"Test {i}: FAILED")
            print(f"   Status:   {response.get('status')}")
            print(f"   Error:    {response.get('error')}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {actual}")

    return all_passed


if __name__ == "__main__":

    # Load problems
    with open("codecontests_bell_200.json", "r") as f:
        problems = json.load(f)

    # Load generated model code
    with open("generated_code.txt", "r") as f:
        code_to_test = f.read()

    # Test first problem
    success = test_solution(problems[0], code_to_test)

    print("\nOverall Result:", "SUCCESS" if success else "FAILURE")
