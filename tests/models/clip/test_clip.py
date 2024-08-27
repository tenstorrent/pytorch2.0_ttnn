from PIL import Image
import requests
import torch
from transformers import CLIPProcessor, CLIPModel
import pytest


@pytest.mark.torch_only
def test_clip(record_property):
    record_property("model_name", "CLIP")

    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32", torch_dtype=torch.bfloat16)
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32", torch_dtype=torch.bfloat16)

    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)

    inputs = processor(
        text=["a photo of a cat", "a photo of a dog"],
        images=image,
        return_tensors="pt",
        padding=True,
    )

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities

    record_property("torch_ttnn", (model, inputs, outputs))
