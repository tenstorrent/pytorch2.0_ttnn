import torch
from mlp_mixer_pytorch import MLPMixer
import pytest


@pytest.mark.compilation_xfail
def test_mlpmixer(record_property):
    record_property("model_name", "MLPMixer")

    """
    https://github.com/lucidrains/mlp-mixer-pytorch
    """
    model = MLPMixer(image_size=256, channels=3, patch_size=16, dim=512, depth=12, num_classes=1000)

    img = torch.randn(1, 3, 256, 256)
    pred = model(img)  # (1, 1000)

    record_property("torch_ttnn", (model, img, pred))
