import torch
import pytest

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM


@pytest.mark.xfail
def test_bloom(record_property):
    record_property("model_name", "Bloom")

    # Download model from cloud
    model_name = "bigscience/bloom-1b1"
    tokenizer = AutoTokenizer.from_pretrained(
        model_name, padding_side="left", torch_dtype=torch.bfloat16
    )
    m = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    m.eval()

    # Set up sample input
    test_input = "This is a sample text from "
    inputs = tokenizer(test_input, return_tensors="pt")

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
    output: {decoded_output}
    """
    )

    record_property("torch_ttnn", (m, inputs, outputs))
