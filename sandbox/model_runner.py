from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch


model_name = "meta-llama/Llama-2-7b-hf"

# 4-bit quantization config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",      
    quantization_config=bnb_config
)

def generate_code(prompt: str) -> str:
    system_prompt = """You are an expert Python programmer. Your task is to generate correct, efficient Python code.
- Write only the function implementation
- Do not include markdown code blocks
- Do not include explanations
- The code must be syntactically correct
- There must be proper indentation.
- you will be given function signature create the program that fints into the function signature."""
    
    # Combine system prompt with user prompt
    full_prompt = f"[INST]<<SYS>>\n{system_prompt}<</SYS>>\n{prompt} [/INST]"
    print(f"{full_prompt}")
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.,
        top_p=0.95,
        repetition_penalty = 1.1
    )
    code = tokenizer.decode(output[0], skip_special_tokens=True)
    return code
