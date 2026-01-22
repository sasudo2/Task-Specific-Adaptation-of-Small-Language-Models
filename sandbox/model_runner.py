from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


model_name = "meta-llama/Llama-2-7b-hf"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",      
    torch_dtype=torch.float16,
    load_in_8bit=True,
    llm_int8_enable_fp32_cpu_offload=True
)

def generate_code(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=256,
        temperature=0.2,
        do_sample=False
    )
    code = tokenizer.decode(output[0], skip_special_tokens=True)
    return code
