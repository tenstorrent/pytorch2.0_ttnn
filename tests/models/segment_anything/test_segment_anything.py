# Reference: https://github.com/facebookresearch/segment-anything-2
# Hugging Face version: https://huggingface.co/facebook/sam2-hiera-tiny

import torch
import requests
from PIL import Image


@pytest.mark.skip(
    reason="Failed to install sam2. sam2 requires Python >=3.10.0 but the default version on Ubuntu 20.04 is 3.8. We found no other pytorch implementation of segment-anything."
)
def test_segment_anything(record_property):
    from sam2.sam2_image_predictor import SAM2ImagePredictor

    record_property("model_name", "segment-anything")

    predictor = SAM2ImagePredictor.from_pretrained("facebook/sam2-hiera-small")

    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    prompt = "Beautiful thing"

    with torch.no_grad():
        predictor.set_image(image)
        outputs = predictor.predict(prompt)

    record_property("torch_ttnn", (predictor, prompt, outputs))
