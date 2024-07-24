import torch
import torchvision
import torch_ttnn
import pytest
from torch_ttnn.metrics import RunTimeMetrics
from tests.utils import check_with_pcc


def test_resnet(device):
    # Download model from cloud
    model = torchvision.models.get_model("resnet18", pretrained=True)
    model.eval()
    model = model.to(torch.bfloat16)

    # Create random input tensor
    input_batch = torch.rand((1, 3, 224, 224), dtype=torch.bfloat16)

    metrics_path = "ResNet18"
    # Run inference with the original model
    with torch.no_grad():
        output_before = RunTimeMetrics(
            metrics_path, "original", lambda: model(input_batch)
        )

    # Compile the model
    option = torch_ttnn.TorchTtnnOption(device=device, metrics_path=metrics_path)
    option.gen_graphviz = True
    model = torch.compile(model, backend=torch_ttnn.backend, options=option)

    # Run inference with the compiled model
    with torch.no_grad():
        output_after = RunTimeMetrics(
            metrics_path, "compiled", lambda: model(input_batch)
        )

    option._out_fx_graphs[0].print_tabular()

    # TODO: Check the graph has be rewritten and contain ttnn ops

    # Check inference result
    assert check_with_pcc(output_before, output_after)
