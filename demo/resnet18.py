from utils import *
import torchvision.models as models
import torchvision.transforms as transforms
import torch
import time
from PIL import Image
import torch_ttnn


@capture_output
def classify_image(image, use_ttnn=True, iterations=1):
    classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    model = models.resnet18(pretrained=True)
    model.fc = torch.nn.Linear(model.fc.in_features, 10)
    model.eval()
    transform = transforms.Compose(
        [transforms.Resize((32, 32)), transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
    )
    input_tensor = transform(image).unsqueeze(0)
    if use_ttnn:
        device = compile_ttnn(model, iterations, input_tensor, mapping=False)
    inference_time, outputs = get_inference_latency(model, inputs, mapping=False)
    probabilities = torch.nn.functional.softmax(outputs, dim=1)
    confidence, predicted_idx = torch.max(probabilities, 1)
    label = classes[predicted_idx.item()]
    confidence_score = confidence.item() * 100
    if use_ttnn:
        ttnn.close_device(device)
    return label, confidence_score, inference_time
