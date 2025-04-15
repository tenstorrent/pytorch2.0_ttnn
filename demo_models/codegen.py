from demo_models.utils import *
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
import torch
import time
import torch_ttnn



@capture_output
def generate_code(prompt, max_length=500, num_return_sequences=1, use_ttnn=True, iterations=1):
    model_name = "Salesforce/codegen-350M-mono"
    print(f"Loading tokenizer and model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.eos_token_id
    print("Encoding prompt...")
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=256,
        padding="max_length",
        truncation=True,
    )
    set_seed(42)
    if use_ttnn:
        device = compile_ttnn_clm(model, iterations, max_length, inputs)
    print(f"Generating code for {iterations} iterations...")
    start_time = time.time()
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,
    )
    num_generated_tokens = len(outputs[0])  # Count tokens in first sequence
    end_time = time.time()
    inference_time = end_time - start_time
    generated_codes = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    print(f"Generated code (first sequence): {generated_codes[0][:100]}...")
    print(f"Generated tokens: {num_generated_tokens}")
    if use_ttnn:
        ttnn.close_device(device)
        print("TTNN device closed.")
    return generated_codes, inference_time, num_generated_tokens