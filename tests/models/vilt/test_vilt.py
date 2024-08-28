# Reference: https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image
import pytest


@pytest.mark.compilation_xfail
def test_vilt(record_property):
    record_property("model_name", "ViLT")

    # prepare image + question
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    text = "How many cats are there?"

    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    print("Predicted answer:", model.config.id2label[idx])

    record_property("torch_ttnn", (model, encoding, outputs))
