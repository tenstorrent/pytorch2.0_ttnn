import torch
import pytest
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


def test_mnist_train(record_property):
    record_property("model_name", "Mnist (Train)")

    # Fixing the random seed for reproducibility to ease debugging.
    #
    # Training processes involve more randomness compared to evaluation,
    # such as random initialization of weights.
    # Setting a fixed random seed is crucial for consistent testing
    # and debugging during the training process.
    torch.manual_seed(99)

    transform = transforms.Compose([transforms.ToTensor()])

    train_dataset = datasets.MNIST(root="./data", train=True, transform=transform, download=True)
    dataloader = DataLoader(train_dataset, batch_size=1)

    m = MnistModel()
    m = m.to(torch.bfloat16)
    m.train()

    # Eliminating randomness from Dropout to ensure consistent results.
    #
    # This is necessary for comparing the two training rounds:
    # one using PyTorch native code and the other using the PyTorch Dynamo TT backend.
    # Without this, the results would differ, making it impossible to compare the two implementations.
    for layer in m.modules():
        if isinstance(layer, nn.Dropout):
            layer.p = 0  # Set dropout probability to 0

    test_input, _ = next(iter(dataloader))
    test_input = test_input.to(torch.bfloat16)

    # Setting input tensor's `requires_grad` attribute to true.
    #
    # This allows us to use the gradient of the input as the golden result for the training process.
    # For further details, refer to the file `conftest.py` regarding the rationale behind.
    test_input.requires_grad = True

    outputs = m(test_input)  # Forward pass
    loss = torch.mean(outputs)  # Loss function
    loss.backward()  # Backward pass

    # Again, use the gradient of the input (`test_input.grad`) as the golden result for the training process.
    record_property("torch_ttnn", (m, test_input, test_input.grad))


def test_mnist_eval(record_property):
    record_property("model_name", "Mnist (Eval)")

    transform = transforms.Compose([transforms.ToTensor()])

    test_dataset = datasets.MNIST(root="./data", train=False, transform=transform, download=True)
    dataloader = DataLoader(test_dataset, batch_size=1)

    m = MnistModel()
    m = m.to(torch.bfloat16)
    m.eval()

    test_input, _ = next(iter(dataloader))
    test_input = test_input.to(torch.bfloat16)
    with torch.no_grad():
        outputs = m(test_input)

    record_property("torch_ttnn", (m, test_input, outputs))
