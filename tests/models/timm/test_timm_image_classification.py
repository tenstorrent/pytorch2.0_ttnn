# Reference: https://huggingface.co/timm
# PyTorch Image Models (timm) is a collection of image models, layers, utilities, optimizers, schedulers, data-loaders / augmentations, and reference training / validation scripts that aim to pull together a wide variety of SOTA models with ability to reproduce ImageNet training results.

from urllib.request import urlopen
from PIL import Image
import torch
import pytest
from tests.utils import ModelTester

dependencies = ["timm==1.0.9"]


class ThisTester(ModelTester):
    def _load_model(self):
        import timm

        model = timm.create_model(self.model_name, pretrained=True)
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        import timm

        img = Image.open(
            urlopen(
                "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png"
            )
        )
        # get model specific transforms (normalization, resize)
        data_config = timm.data.resolve_model_data_config(self.model)
        transforms = timm.data.create_transform(**data_config, is_training=False)
        input_batch = transforms(img).unsqueeze(0)  # unsqueeze single image into batch of 1
        input_batch = input_batch.to(torch.bfloat16)
        return input_batch


model_and_mode_list = [
    pytest.param(["tf_efficientnet_lite0.in1k", "train"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite1.in1k", "train"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite2.in1k", "train"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite3.in1k", "train"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite4.in1k", "train"], marks=pytest.mark.compilation_xfail),
    pytest.param(["ghostnet_100.in1k", "train"], marks=pytest.mark.compilation_xfail),
    pytest.param(["ghostnetv2_100.in1k", "train"], marks=pytest.mark.compilation_xfail),
    ["inception_v4.tf_in1k", "train"],
    pytest.param(["mixer_b16_224.goog_in21k", "train"], marks=pytest.mark.compilation_xfail),
    ["mobilenetv1_100.ra4_e3600_r224_in1k", "train"],
    ["ese_vovnet19b_dw.ra_in1k", "train"],
    ["xception71.tf_in1k", "train"],
    ["dla34.in1k", "train"],
    pytest.param(["hrnet_w18.ms_aug_in1k", "train"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite0.in1k", "eval"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite1.in1k", "eval"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite2.in1k", "eval"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite3.in1k", "eval"], marks=pytest.mark.compilation_xfail),
    pytest.param(["tf_efficientnet_lite4.in1k", "eval"], marks=pytest.mark.compilation_xfail),
    ["ghostnet_100.in1k", "eval"],
    ["ghostnetv2_100.in1k", "eval"],
    ["inception_v4.tf_in1k", "eval"],
    ["mixer_b16_224.goog_in21k", "eval"],
    ["mobilenetv1_100.ra4_e3600_r224_in1k", "eval"],
    ["ese_vovnet19b_dw.ra_in1k", "eval"],
    ["xception71.tf_in1k", "eval"],
    ["dla34.in1k", "eval"],
    ["hrnet_w18.ms_aug_in1k", "eval"],
]


@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.parametrize("model_and_mode", model_and_mode_list)
def test_timm_image_classification(record_property, model_and_mode):
    model_name = model_and_mode[0]
    mode = model_and_mode[1]
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        top5_probabilities, top5_class_indices = torch.topk(results.softmax(dim=1) * 100, k=5)

        print(
            f"Model: {model_name} | Predicted class ID: {top5_class_indices[0]} | Probabiliy: {top5_probabilities[0]}"
        )

    record_property("torch_ttnn", (tester, results))
