import torch
import numpy as np
from PIL import Image
import requests
from transformers import GLPNImageProcessor, GLPNForDepthEstimation
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.processor = GLPNImageProcessor.from_pretrained("vinvino02/glpn-kitti")
        model = GLPNForDepthEstimation.from_pretrained("vinvino02/glpn-kitti", torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self):
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        self.image = Image.open(requests.get(url, stream=True).raw)
        # prepare image for the model
        inputs = self.processor(images=self.image, return_tensors="pt")
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_glpn_kitti(record_property, mode):
    model_name = "GLPN-KITTI"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        predicted_depth = results.predicted_depth

        # interpolate to original size
        prediction = torch.nn.functional.interpolate(
            predicted_depth.unsqueeze(1),
            size=tester.image.size[::-1],
            mode="bicubic",
            align_corners=False,
        )

        # visualize the prediction
        output = prediction.squeeze().cpu().numpy()
        formatted = (output * 255 / np.max(output)).astype("uint8")
        depth = Image.fromarray(formatted)

    record_property("torch_ttnn", (tester, results))
