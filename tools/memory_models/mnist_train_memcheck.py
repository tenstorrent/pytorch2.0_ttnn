import torch
import torch_ttnn
import unittest
import ttnn
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
    train_dataset = datasets.MNIST(
        root="./data", train=True, transform=transform, download=True
    )
    dataloader = DataLoader(train_dataset, batch_size=1)

    m = MnistModel()
    m = m.to(torch.bfloat16)
    m.train()

    metrics_path = "Mnist (Train)"
    test_input, _ = next(iter(dataloader))

    # Compile model with ttnn backend
    option = torch_ttnn.TorchTtnnOption(device=device, metrics_path=metrics_path)
    option.gen_graphviz = True
    option.run_mem_analysis = True
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    # These are for plotting charts for later inspection
    from tools.memory_models.plot_chart import plot_bar_chart, plot_line_chart

    src_file = "./data/memory/memory_footprint.txt"
    bar_chart_file = "./tools/memory_models/assets/mnist_train_bar_chart.png"
    line_chart_file = "./tools/memory_models/assets/mnist_train_line_chart.png"
    plot_bar_chart(src_file, bar_chart_file)
    plot_line_chart(src_file, line_chart_file)

    # Run inference with the compiled model
    m(test_input.to(torch.bfloat16))

    # Close the device
    ttnn.close_device(device)
