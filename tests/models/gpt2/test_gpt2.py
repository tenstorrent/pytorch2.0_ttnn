import torch
import torch_ttnn
import pytest
from torch_ttnn.metrics import RunTimeMetrics

# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification


@pytest.mark.xfail
def test_gpt2(device):
    # Download model from cloud
    model_name = "mnoukhov/gpt2-imdb-sentiment-classifier"
    tokenizer = AutoTokenizer.from_pretrained(
        model_name, padding_side="left", torch_dtype=torch.bfloat16
    )
    m = AutoModelForSequenceClassification.from_pretrained(
        model_name, torch_dtype=torch.bfloat16
    )
    m.eval()

    # Set up sample input
    test_input = "This is a sample text from "
    inputs = tokenizer(test_input, return_tensors="pt")

    metrics_path = "GPT-2"
    # Run inference with the original model
    with torch.no_grad():
        outputs_before = RunTimeMetrics(metrics_path, "original", lambda: m(**inputs))

    # Helper function to decode output to human-readable text
    def decode_output(outputs):
        normalized = outputs.logits.softmax(dim=-1)
        return normalized.argmax().item()

    decoded_output_before = decode_output(outputs_before)

    # Compile model with ttnn backend
    option = torch_ttnn.TorchTtnnOption(device=device, metrics_path=metrics_path)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    # Run inference with the compiled model
    with torch.no_grad():
        outputs_after = RunTimeMetrics(metrics_path, "compiled", lambda: m(**inputs))

    option._out_fx_graphs[0].print_tabular()

    decoded_output_after = decode_output(outputs_after)

    print(
        f"""
    model_name: {model_name}
    input: {test_input}
    output before: {decoded_output_before}
    output after: {decoded_output_after}
    """
    )

    # TODO: Add more checks for the compiled graph

    # Check inference result
    assert decoded_output_before == decoded_output_after
