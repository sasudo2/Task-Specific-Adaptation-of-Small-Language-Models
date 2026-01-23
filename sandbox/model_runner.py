from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch


model_name = "meta-llama/Llama-2-7b-chat-hf"

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

