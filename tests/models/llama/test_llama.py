import torch
import pytest

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM


@pytest.mark.compilation_xfail
def test_llama(record_property):
    record_property("model_name", "Llama")

    # Download model from cloud
    model_name = "huggyllama/llama-7b"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    tokenizer.pad_token = tokenizer.eos_token
    m = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    for param in m.parameters():
        param.requires_grad = False
    m.eval()

    # Set up sample input
    test_input = "This is a sample text from "
    inputs = tokenizer.encode_plus(
        test_input,
        return_tensors="pt",
        max_length=32,
        padding="max_length",
        add_special_tokens=True,
        truncation=True,
    )

    # Run inference with the original model
    with torch.no_grad():
        outputs = m(**inputs)

    # Helper function to decode output to human-readable text
    def decode_output(outputs):
        next_token_logits = outputs.logits[:, -1]
        next_token = next_token_logits.softmax(dim=-1).argmax()
        return tokenizer.decode([next_token])

    decoded_output = decode_output(outputs)

    print(
        f"""
    model_name: {model_name}
    input: {test_input}
    output before: {decoded_output}
    """
    )

    record_property("torch_ttnn", (m, inputs, outputs))
