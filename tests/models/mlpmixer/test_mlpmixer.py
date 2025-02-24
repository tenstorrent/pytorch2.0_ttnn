import torch
from mlp_mixer_pytorch import MLPMixer
import pytest
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        """
        https://github.com/lucidrains/mlp-mixer-pytorch
        """
        model = MLPMixer(image_size=256, channels=3, patch_size=16, dim=512, depth=12, num_classes=1000)
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        img = torch.randn(1, 3, 256, 256)
        img = img.to(torch.bfloat16)
        return img


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
def test_mlpmixer(record_property, mode, get_batch_size):
    model_name = "MLPMixer"
    record_property("model_name", model_name)
    record_property("mode", mode)

    batch_size = get_batch_size
    if batch_size is not None:
        batch_size = int(batch_size)
    validate_batch_size(batch_size)

    tester = ThisTester(model_name, mode)
    results = tester.test_model(batch_size=batch_size)
    batch_object_inputs(tester, batch_size)  # This is necessary to avoid shape mismatch errors in tester processing
    record_property("torch_ttnn", (tester, results))
