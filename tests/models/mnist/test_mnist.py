import torch
import torch_ttnn
import pytest
from torch_ttnn.metrics import RunTimeMetrics
from tests.utils import check_with_pcc
from torchvision import transforms, datasets
from torch.utils.data import DataLoader

import torch.nn as nn
import torch.nn.functional as F


# adapted from https://github.com/pytorch/examples/blob/main/mnist/main.py
class MnistModel(torch.nn.Module):
    def __init__(self):
        super(MnistModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output


def test_mnist_train(device):
    transform = transforms.Compose([transforms.ToTensor()])

    train_dataset = datasets.MNIST(
        root="./data", train=True, transform=transform, download=True
    )
    dataloader = DataLoader(train_dataset, batch_size=1)

    m = MnistModel()
    m = m.to(torch.bfloat16)
    m.train()

    metrics_path = "Mnist (Train)"
    test_input, target = next(iter(dataloader))
    # Run train with the original model
    outputs_before = RunTimeMetrics(
        metrics_path, "original", lambda: m(test_input.to(torch.bfloat16))
    )

    # Compile model with ttnn backend
    option = torch_ttnn.TorchTtnnOption(device=device, metrics_path=metrics_path)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    # Run train with the compiled model
    outputs_after = RunTimeMetrics(
        metrics_path, "compiled", lambda: m(test_input.to(torch.bfloat16))
    )

    option._out_fx_graphs[0].print_tabular()

    # TODO: Since only one loop of training is done, the outputs could have greater differences.
    # Consider adding more loops.


@pytest.mark.xfail
def test_mnist_eval(device):
    transform = transforms.Compose([transforms.ToTensor()])

    test_dataset = datasets.MNIST(
        root="./data", train=False, transform=transform, download=True
    )
    dataloader = DataLoader(test_dataset, batch_size=1)

    m = MnistModel()
    m = m.to(torch.bfloat16)
    m.eval()

    metrics_path = "Mnist (Eval)"
    test_input, _ = next(iter(dataloader))
    # Run inference with the original model
    with torch.no_grad():
        outputs_before = RunTimeMetrics(
            metrics_path, "original", lambda: m(test_input.to(torch.bfloat16))
        )

    # Compile model with ttnn backend
    option = torch_ttnn.TorchTtnnOption(device=device, metrics_path=metrics_path)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    # Run inference with the compiled model
    with torch.no_grad():
        outputs_after = RunTimeMetrics(
            metrics_path, "compiled", lambda: m(test_input.to(torch.bfloat16))
        )

    option._out_fx_graphs[0].print_tabular()

    assert check_with_pcc(outputs_before, outputs_after)
