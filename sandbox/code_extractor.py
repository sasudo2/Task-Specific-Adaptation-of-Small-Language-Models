import re
import inspect

def extract_function(code: str, fn_name: str) -> str:
    """Extract function code from model output and return as string"""
    pattern = rf"(def {fn_name}\([\s\S]*?)(?=\ndef\s|\nclass\s|$)"
    match = re.search(pattern, code)
    if not match:
        raise ValueError(f"Function {fn_name} not found in code")
    print(match.group(1).strip())
    return match.group(1).strip()
