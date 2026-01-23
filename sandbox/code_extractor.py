import re
import inspect

def extract_function(code: str, fn_name: str) -> str:
    """Extract function code from model output and return as string"""
    pattern = r"```(?!\.)?\n([\s\S]*?)```"
    match = re.search(pattern, code)
    print(len(match.groups()))
    if match == None:
        raise ValueError(f"No code was detected")
    else:
        with open("generated_code.txt", "a") as f:
            f.write(f"\n#{'='*80}\n")
            f.write(f"#Problem ID: {fn_name}\n")
            f.write(f"#{'='*80}\n")
            f.write(match.group(1).strip())
            f.write("\n")
        return match.group(1).strip()

