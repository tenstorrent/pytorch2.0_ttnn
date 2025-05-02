from utils import *
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, set_seed
import torch
import time
import torch_ttnn
import ttnn


@capture_output
def ask_question(context, question, use_ttnn=True, iterations=1, sequence_length=256):
    model_name = "phiyodr/bert-large-finetuned-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    inputs = tokenizer.encode_plus(
        question,
        context,
        add_special_tokens=True,
        return_tensors="pt",
        max_length=sequence_length,
        padding="max_length",
        truncation=True,
    )
    total_token_count = sequence_length
    if use_ttnn:
        device = compile_ttnn(model, iterations, inputs)
    inference_time, outputs = get_inference_latency(model, inputs)

    def decode_output(outputs):
        response_start = torch.argmax(outputs.start_logits)
        response_end = torch.argmax(outputs.end_logits) + 1
        response_tokens = inputs.input_ids[0, response_start:response_end]
        return tokenizer.decode(response_tokens)

    answer = decode_output(outputs)
    if use_ttnn:
        ttnn.close_device(device)
    return answer, inference_time, total_token_count
