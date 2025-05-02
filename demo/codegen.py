from utils import *
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
import torch
import time
import torch_ttnn


@capture_output
def generate_code(prompt, input_length, max_new_tokens=500, num_return_sequences=1, use_ttnn=True, iterations=1):
    model_name = "Salesforce/codegen-350M-mono"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.eos_token_id
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=input_length,
        padding="max_length",
        truncation=True,
    )
    max_length = input_length + max_new_tokens
    if use_ttnn:
        device = compile_ttnn(model, iterations, inputs)
    st.write("Running model generation (May take a few minutes)")
    start_time = time.time()
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,
        eos_token_id=None,
    )
    num_generated_tokens = len(outputs[0])  # Count tokens in first sequence
    end_time = time.time()
    inference_time = end_time - start_time
    generated_codes = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    if use_ttnn:
        ttnn.close_device(device)
    return generated_codes, inference_time, num_generated_tokens
