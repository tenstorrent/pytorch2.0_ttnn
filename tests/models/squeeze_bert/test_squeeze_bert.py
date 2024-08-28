# Reference: https://huggingface.co/docs/transformers/en/model_doc/squeezebert#transformers.SqueezeBertForSequenceClassification

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pytest


@pytest.mark.compilation_xfail
def test_squeeze_bert(record_property):
    record_property("model_name", "SqueezeBERT")

    tokenizer = AutoTokenizer.from_pretrained("squeezebert/squeezebert-mnli")
    model = AutoModelForSequenceClassification.from_pretrained("squeezebert/squeezebert-mnli")

    inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    predicted_class_id = logits.argmax().item()

    record_property("torch_ttnn", (model, inputs, outputs))
