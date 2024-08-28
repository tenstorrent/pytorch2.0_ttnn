# Reference: https://huggingface.co/timm
# PyTorch Image Models (timm) is a collection of image models, layers, utilities, optimizers, schedulers, data-loaders / augmentations, and reference training / validation scripts that aim to pull together a wide variety of SOTA models with ability to reproduce ImageNet training results.

from urllib.request import urlopen
from PIL import Image
import timm
import torch
import pytest


@pytest.mark.parametrize(
    "model_name",
    [
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
    ],
)
@pytest.mark.compilation_xfail
def test_timm_image_classification(record_property, model_name):
    record_property("model_name", model_name)

    img = Image.open(
        urlopen("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png")
    )

    model = timm.create_model(model_name, pretrained=True)
    model = model.eval()

    # get model specific transforms (normalization, resize)
    data_config = timm.data.resolve_model_data_config(model)
    transforms = timm.data.create_transform(**data_config, is_training=False)
    input_batch = transforms(img).unsqueeze(0)  # unsqueeze single image into batch of 1

    with torch.no_grad():
        output = model(input_batch)

    top5_probabilities, top5_class_indices = torch.topk(output.softmax(dim=1) * 100, k=5)

    print(f"Model: {model_name} | Predicted class ID: {top5_class_indices[0]} | Probabiliy: {top5_probabilities[0]}")

    record_property("torch_ttnn", (model, input_batch, output))
