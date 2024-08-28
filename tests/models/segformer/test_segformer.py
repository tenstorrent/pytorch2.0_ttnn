# Reference: https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512

from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation
from PIL import Image
import requests
import pytest


@pytest.mark.compilation_xfail
def test_segformer(record_property):
    record_property("model_name", "SegFormer")

    processor = SegformerImageProcessor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
    model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")

    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits  # shape (batch_size, num_labels, height/4, width/4)

    record_property("torch_ttnn", (model, inputs, outputs))
