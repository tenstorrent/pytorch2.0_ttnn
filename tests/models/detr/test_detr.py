from PIL import Image
import requests
import torch
import numpy as np
from torchvision import transforms
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        """
        The model is from https://github.com/facebookresearch/detr
        """
        # Model
        model = torch.hub.load("facebookresearch/detr:main", "detr_resnet50", pretrained=True)
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        # Images
        img_url = "https://ultralytics.com/images/zidane.jpg"  # batch of images
        input_image = Image.open(requests.get(img_url, stream=True).raw)
        m, s = np.mean(input_image, axis=(0, 1)), np.std(input_image, axis=(0, 1))
        preprocess = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(mean=m, std=s),
            ]
        )
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)
        input_batch = input_batch.to(torch.bfloat16)
        return input_batch

    def set_inputs_train(self, inputs):
        inputs.requires_grad_(True)
        return inputs

    def append_fake_loss_function(self, outputs):
        return torch.mean(outputs["pred_logits"]) + torch.mean(outputs["pred_boxes"])

    def get_results_train(self, model, inputs, outputs):
        return inputs.grad


@pytest.mark.parametrize(
    "mode",
    [
        pytest.param(
            "train",
            marks=pytest.mark.skip(reason="model has no training mode(A view was created in no_grad)"),
        ),
        "eval",
    ],
)
@pytest.mark.compilation_xfail
def test_detr(record_property, mode):
    model_name = "DETR"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        # Results
        print(results)

    record_property("torch_ttnn", (tester, results))
