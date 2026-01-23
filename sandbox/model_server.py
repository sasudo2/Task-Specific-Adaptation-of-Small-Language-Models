from flask import Flask, request, jsonify
from model_runner import model, tokenizer

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_code():
    data = request.json
    prompt = data['prompt']
    system_prompt = """You are an expert Python programmer. Your task is to generate correct, efficient Python code.
- Write only the function implementation
- Do not include markdown code blocks
- Do not include explanations
- The code must be syntactically correct
- There must be proper indentation.
- you will be given function signature 
- create the program that fits into the function signature.
- always enclose code only between ``` and ```.
- Do not reason
- Do not give any examples
"""
    
    # Combine system prompt with user prompt
    full_prompt = f"[INST]<<SYS>>{system_prompt}<</SYS>>\n{prompt}[/INST]"
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=1024,
        do_sample=True,
        temperature=0.1,
        top_p=0.5,
        repetition_penalty = 1.1
    )
    code = tokenizer.decode(output[0], skip_special_tokens=True)
    return jsonify({'code': code})


if __name__ == '__main__':
    print("Model loaded, starting server...")
    app.run(host='0.0.0.0', port=5000)