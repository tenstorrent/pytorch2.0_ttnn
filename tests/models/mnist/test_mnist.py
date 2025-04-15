# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest
from torchvision import transforms, datasets
from torch.utils.data import DataLoader

import torch.nn as nn
import torch.nn.functional as F
from tests.utils import ModelTester


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


class ThisTester(ModelTester):
    def _load_model(self):
        model = MnistModel()
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        transform = transforms.Compose([transforms.ToTensor()])
        test_dataset = datasets.MNIST(root="./data", train=False, transform=transform, download=True)
        dataloader = DataLoader(test_dataset, batch_size=128)
        test_input, _ = next(iter(dataloader))
        test_input = test_input.to(torch.bfloat16)
        return test_input


@pytest.mark.parametrize(
    "mode",
    ["eval"],
    # ["train", pytest.param("eval", marks=pytest.mark.converted_end_to_end)],
)
def test_mnist_train(record_property, mode):
    model_name = "Mnist"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))
