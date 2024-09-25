# Reference: https://huggingface.co/docs/transformers/en/model_doc/squeezebert#transformers.SqueezeBertForSequenceClassification

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pytest


def test_squeeze_bert(record_property):
    record_property("model_name", "SqueezeBERT")

    tokenizer = AutoTokenizer.from_pretrained("squeezebert/squeezebert-mnli", torch_dtype=torch.bfloat16)
    model = AutoModelForSequenceClassification.from_pretrained("squeezebert/squeezebert-mnli", torch_dtype=torch.bfloat16)

    inputs = tokenizer.encode_plus(
        "Hello, my dog is cute",
        add_special_tokens=True,
        return_tensors='pt',
        max_length=256,
        padding="max_length",
        truncation=True,
    )

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    predicted_class_id = logits.argmax().item()

    record_property("torch_ttnn", (model, inputs, outputs))
