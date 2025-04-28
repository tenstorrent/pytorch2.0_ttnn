# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
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
    ["tf_efficientnet_lite0.in1k", "train"],
    ["tf_efficientnet_lite1.in1k", "train"],
    ["tf_efficientnet_lite2.in1k", "train"],
    ["tf_efficientnet_lite3.in1k", "train"],
    pytest.param(
        ["tf_efficientnet_lite4.in1k", "train"], marks=pytest.mark.xfail(reason="OOM with program cache enabled")
    ),
    ["ghostnet_100.in1k", "train"],
    ["ghostnetv2_100.in1k", "train"],
    pytest.param(["inception_v4.tf_in1k", "train"], marks=pytest.mark.xfail(reason="OOM with program cache enabled")),
    ["mixer_b16_224.goog_in21k", "train"],
    ["mobilenetv1_100.ra4_e3600_r224_in1k", "train"],
    ["ese_vovnet19b_dw.ra_in1k", "train"],
    pytest.param(["xception71.tf_in1k", "train"], marks=pytest.mark.xfail(reason="OOM with program cache enabled")),
    ["dla34.in1k", "train"],
    ["hrnet_w18.ms_aug_in1k", "train"],
    pytest.param(["tf_efficientnet_lite0.in1k", "eval"], marks=pytest.mark.converted_end_to_end),
    pytest.param(["tf_efficientnet_lite1.in1k", "eval"], marks=pytest.mark.converted_end_to_end),
    pytest.param(["tf_efficientnet_lite2.in1k", "eval"], marks=pytest.mark.converted_end_to_end),
    ["tf_efficientnet_lite3.in1k", "eval"],
    pytest.param(
        ["tf_efficientnet_lite4.in1k", "eval"], marks=pytest.mark.xfail(reason="OOM with program cache enabled")
    ),
    pytest.param(["ghostnet_100.in1k", "eval"], marks=pytest.mark.converted_end_to_end),
    ["ghostnetv2_100.in1k", "eval"],
    pytest.param(["inception_v4.tf_in1k", "eval"], marks=pytest.mark.xfail(reason="OOM with program cache enabled")),
    ["mixer_b16_224.goog_in21k", "eval"],
    pytest.param(["mobilenetv1_100.ra4_e3600_r224_in1k", "eval"], marks=pytest.mark.converted_end_to_end),
    pytest.param(["ese_vovnet19b_dw.ra_in1k", "eval"], marks=pytest.mark.converted_end_to_end),
    pytest.param(["xception71.tf_in1k", "eval"], marks=pytest.mark.xfail(reason="OOM with program cache enabled")),
    pytest.param(["dla34.in1k", "eval"], marks=pytest.mark.converted_end_to_end),
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
