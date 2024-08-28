# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForSequenceClassification

from transformers import AlbertTokenizer, AlbertForSequenceClassification
import torch
import pytest


@pytest.mark.parametrize("model_name", ["textattack/albert-base-v2-imdb"])
@pytest.mark.compilation_xfail
def test_albert_sequence_classification(record_property, model_name):
    record_property("model_name", model_name)

    tokenizer = AlbertTokenizer.from_pretrained(model_name)
    model = AlbertForSequenceClassification.from_pretrained(model_name)

    input_text = "Hello, my dog is cute."
    inputs = tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        output = model(**inputs)

    logits = output.logits
    predicted_class_id = logits.argmax().item()
    predicted_label = model.config.id2label[predicted_class_id]

    print(f"Model: {model_name} | Input: {input_text} | Label: {predicted_label}")

    record_property("torch_ttnn", (model, inputs, output))
