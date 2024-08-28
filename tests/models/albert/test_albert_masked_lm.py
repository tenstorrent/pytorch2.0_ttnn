# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForMaskedLM

from transformers import AutoTokenizer, AlbertForMaskedLM
import torch
import pytest


@pytest.mark.parametrize(
    "model_name",
    ["albert/albert-base-v2", "albert/albert-large-v2", "albert/albert-xlarge-v2", "albert/albert-xxlarge-v2"],
)
@pytest.mark.compilation_xfail
def test_albert_masked_lm(record_property, model_name):
    record_property("model_name", model_name)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AlbertForMaskedLM.from_pretrained(model_name)

    text = "The capital of [MASK] is Paris."
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs)

    # retrieve index of [MASK]
    logits = output.logits
    mask_token_index = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]
    predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
    predicted_tokens = tokenizer.decode(predicted_token_id)

    print(f"Model: {model_name} | Input: {text} | Mask: {predicted_tokens}")

    record_property("torch_ttnn", (model, inputs, output))
