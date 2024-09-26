import torch
import pytest
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from tests.utils import run_for_train_mode, run_for_eval_mode

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


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
def test_mnist_train(record_property, mode):
    model_name = f"Mnist ({mode})"
    record_property("model_name", model_name)

    transform = transforms.Compose([transforms.ToTensor()])

    train_dataset = datasets.MNIST(root="./data", train=True, transform=transform, download=True)
    dataloader = DataLoader(train_dataset, batch_size=1)

    m = MnistModel()

    test_input, _ = next(iter(dataloader))

    if mode == "train":
        results = run_for_train_mode(model_name, m, test_input)
    elif mode == "eval":
        results = run_for_eval_mode(model_name, m, test_input)
    else:
        raise ValueError(f"Invalid mode: {mode}")

    record_property("mode", mode)
    record_property("torch_ttnn", (m, test_input, results))
