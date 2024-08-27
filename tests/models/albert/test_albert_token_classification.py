# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForTokenClassification

from transformers import AutoTokenizer, AlbertForTokenClassification
import torch
import pytest


@pytest.mark.parametrize("model_name", ["albert/albert-base-v2"])
@pytest.mark.torch_only
def test_albert_token_classification(record_property, model_name):
    record_property("model_name", model_name)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AlbertForTokenClassification.from_pretrained(model_name)

    text = "HuggingFace is a company based in Paris and New York."
    inputs = tokenizer(text, add_special_tokens=False, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs)

    logits = output.logits
    predicted_token_class_ids = logits.argmax(-1)

    # Note that tokens are classified rather then input words which means that
    # there might be more predicted token classes than words.
    # Multiple token classes might account for the same word
    predicted_tokens_classes = [model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]

    input_ids = inputs["input_ids"]
    tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
    print(f"Model: {model_name} | Tokens: {tokens} | Predictions: {predicted_tokens_classes}")

    record_property("torch_ttnn", (model, inputs, output))
