import re

def extract_function(code: str, fn_name: str):
    pattern = rf"(def {fn_name}\\(.*?:[\\s\\S]+)"
    match = re.search(pattern, code)
    if not match:
        raise ValueError("Function not found")

    namespace = {}
    exec(match.group(1), namespace)
    return namespace[fn_name]
