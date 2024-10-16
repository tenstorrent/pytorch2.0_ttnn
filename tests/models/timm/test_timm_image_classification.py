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


model_list = [
    "tf_efficientnet_lite0.in1k",
    "tf_efficientnet_lite1.in1k",
    "tf_efficientnet_lite2.in1k",
    "tf_efficientnet_lite3.in1k",
    "tf_efficientnet_lite4.in1k",
    "ghostnet_100.in1k",
    "ghostnetv2_100.in1k",
    "inception_v4.tf_in1k",
    "mixer_b16_224.goog_in21k",
    "mobilenetv1_100.ra4_e3600_r224_in1k",
    "ese_vovnet19b_dw.ra_in1k",
    "xception71.tf_in1k",
    "dla34.in1k",
    "hrnet_w18.ms_aug_in1k",
]
mode_list = ["train", "eval"]
model_and_mode_list = []
for model in model_list:
    for mode in mode_list:
        if (
            (model == "ghostnet_100.in1k" and mode == "eval")
            or (model == "inception_v4.tf_in1k")
            or (model == "mixer_b16_224.goog_in21k" and mode == "eval")
            or (model == "mobilenetv1_100.ra4_e3600_r224_in1k")
            or (model == "ese_vovnet19b_dw.ra_in1k")
            or (model == "xception71.tf_in1k")
            or (model == "dla34.in1k")
        ):
            model_and_mode_list.append([model, mode])
        else:
            model_and_mode_list.append(pytest.param([model, mode], marks=pytest.mark.compilation_xfail))


@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.parametrize("model_and_mode", model_and_mode_list)
def test_timm_image_classification(record_property, model_and_mode):
    model_name = model_and_mode[0]
    mode = model_and_mode[1]
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        top5_probabilities, top5_class_indices = torch.topk(results.softmax(dim=1) * 100, k=5)

        print(
            f"Model: {model_name} | Predicted class ID: {top5_class_indices[0]} | Probabiliy: {top5_probabilities[0]}"
        )

    record_property("torch_ttnn", (tester, results))
