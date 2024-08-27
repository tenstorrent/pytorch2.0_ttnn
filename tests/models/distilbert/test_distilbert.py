from transformers import DistilBertTokenizer, DistilBertModel
import torch
import pytest


@pytest.mark.parametrize("model_name", ["distilbert-base-uncased"])
@pytest.mark.torch_only
def test_distilbert(record_property, model_name):
    record_property("model_name", model_name)

    tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    model = DistilBertModel.from_pretrained(model_name)

    text = "Transformers provide state-of-the-art results in NLP."
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs)

    print(f"Model: {model_name} | Input: {text} | Output: {output}")

    record_property("torch_ttnn", (model, inputs, output))
