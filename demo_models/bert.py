from demo_models.utils import *
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, set_seed
import torch
import time
import torch_ttnn
import ttnn

@capture_output
def ask_question(context, question, use_ttnn=True, iterations=1):
    model_name = "phiyodr/bert-large-finetuned-squad2"
    print(f"Loading tokenizer and model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    print("Encoding inputs...")
    inputs = tokenizer.encode_plus(
        question,
        context,
        add_special_tokens=True,
        return_tensors="pt",
        max_length=256,
        padding="max_length",
        truncation=True,
    )
    total_token_count = inputs["input_ids"].ne(tokenizer.pad_token_id).sum().item()  # Count non-padding tokens
    if use_ttnn:
        device = compile_ttnn(model, iterations, inputs)
    start_time = time.time()
    outputs = model(**inputs)
    end_time = time.time()
    inference_time = end_time - start_time

    def decode_output(outputs):
        response_start = torch.argmax(outputs.start_logits)
        response_end = torch.argmax(outputs.end_logits) + 1
        response_tokens = inputs.input_ids[0, response_start:response_end]
        return tokenizer.decode(response_tokens)

    answer = decode_output(outputs)
    print(f"Answer: {answer}")
    print(f"Total tokens (context + question): {total_token_count}")
    if use_ttnn:
        ttnn.close_device(device)
        print("TTNN device closed.")
    return answer, inference_time, total_token_count
