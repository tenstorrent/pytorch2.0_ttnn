from utils import *
import torch
import torch.nn.functional as F
import torch.nn as nn
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import time
import streamlit as st


class MnistModel(nn.Module):
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


@capture_output
def classify_mnist(use_ttnn=False, iterations=1):
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    mnist_test = datasets.MNIST(root="./data", train=False, download=True, transform=transform)
    image, label = mnist_test[0]
    input_tensor = image.unsqueeze(0)
    model = MnistModel()
    for param in model.parameters():
        param.requires_grad = False  # This is necessary to convert to numpy, so the logits can be displayed.
    model.eval()
    display_image = (image * 0.3081) + 0.1307
    display_image = display_image.clamp(0, 1)
    st.image(display_image.squeeze().numpy(), caption=f"Sample MNIST Digit (Label: {label})", width=100)
    if use_ttnn:
        device = compile_ttnn(model, iterations, input_tensor, mapping=False)
    inference_time, logits = get_inference_latency(model, input_tensor, mapping=False)
    probabilities = torch.exp(logits)
    confidence, predicted_idx = torch.max(probabilities, 1)
    predicted_label = predicted_idx.item()
    confidence_score = confidence.item() * 100
    if use_ttnn:
        ttnn.close_device(device)
    return logits, predicted_label, confidence_score, inference_time
