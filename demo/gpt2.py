from utils import *
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
import torch
import time
import torch_ttnn


@capture_output
def generate_text(prompt, input_length, max_new_tokens=500, use_ttnn=True, iterations=1):
    model_name = "gpt2"
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
    if use_ttnn:
        device = compile_ttnn(model, iterations, inputs)
    st.write("Running model generation (May take a few minutes)")
    start_time = time.time()
    max_length = input_length + max_new_tokens
    outputs = model.generate(
        **inputs, max_length=max_length, do_sample=True, eos_token_id=None, pad_token_id=tokenizer.pad_token_id
    )
    num_generated_tokens = len(outputs[0])  # Count tokens in first sequence
    end_time = time.time()
    inference_time = end_time - start_time
    generated_texts = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    if use_ttnn:
        ttnn.close_device(device)
    return generated_texts, inference_time, num_generated_tokens
