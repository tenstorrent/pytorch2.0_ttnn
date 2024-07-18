import torch
import torch_ttnn
import unittest
import ttnn
from torch_ttnn.utils import RunTimeMetrics
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


if __name__ == "__main__":
    # Open device 0
    device: ttnn.Device = ttnn.open_device(device_id=0)
    # Setup dataset
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

    # Compile model with ttnn backend
    option = torch_ttnn.TorchTtnnOption(
        device=device, metrics_path=metrics_path
    )
    option.gen_graphviz = True
    m = torch.compile(m, backend=torch_ttnn.memory_backend, options=option)

    # Run inference with the compiled model
    m(test_input.to(torch.bfloat16))

    # with torch.no_grad():
    #     outputs_after = RunTimeMetrics(
    #         metrics_path, "compiled", lambda: m(test_input.to(torch.bfloat16))
    #     )
    option._out_fx_graphs[0].print_tabular()

    # Close the device
    ttnn.close_device(device)
