import torch
import torchvision
import pytest
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        model = torchvision.models.get_model("resnet18", pretrained=True)
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        inputs = torch.rand((1, 3, 224, 224), dtype=torch.bfloat16)
        inputs = inputs.to(torch.bfloat16)
        return inputs


@pytest.mark.parametrize(
    "mode",
    [
        "train",
        pytest.param("eval", marks=pytest.mark.converted_end_to_end),
    ],
)
def test_resnet(record_property, mode, get_batch_size):
    model_name = "ResNet18"
    record_property("model_name", model_name)
    record_property("mode", mode)
    batch_size = get_batch_size
    if batch_size is not None:
        batch_size = int(batch_size)
    validate_batch_size(batch_size)

    tester = ThisTester(model_name, mode)
    results = tester.test_model(batch_size=batch_size)
    batch_object_inputs(tester, batch_size)

    # Check inference result
    record_property("torch_ttnn", (tester, results))
