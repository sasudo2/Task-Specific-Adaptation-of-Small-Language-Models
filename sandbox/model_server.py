from flask import Flask, request, jsonify
from model_runner import model, tokenizer

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_code():
    data = request.json
    prompt = data['prompt']
    
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
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