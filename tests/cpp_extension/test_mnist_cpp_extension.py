import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import torch_ttnn
from torch_ttnn.cpp_extension import ttnn_module
import pytest


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
        x = F.log_softmax(x, dim=1)
        return x


@pytest.mark.skip(reason="Does not support conv for now")
def test_mnist_with_cpp_extension(device):
    model_name = "Mnist"
    transform = transforms.Compose([transforms.ToTensor()])
    test_dataset = datasets.MNIST(root="./data", train=False, transform=transform, download=True)
    dataloader = DataLoader(test_dataset, batch_size=1)
    test_input, _ = next(iter(dataloader))
    test_input = test_input.to(torch.bfloat16)

    # Copy weights and biases to ttnn
    torch.utils.rename_privateuse1_backend("ttnn")
    ttnn_device = ttnn_module.custom_device_from_ttnn(device)

    option = torch_ttnn.TorchTtnnOption(
        device=device,
        gen_graphviz=False,
        run_mem_analysis=False,
        metrics_path=model_name,
        verbose=True,
    )

    model = MnistModel()
    model = model.to(torch.bfloat16)
    test_input = test_input.to(ttnn_device)
    model.to(ttnn_device)

    model = torch.compile(model, backend=torch_ttnn.backend, options=option)
    results = model(test_input)
