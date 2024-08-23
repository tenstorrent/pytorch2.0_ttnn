import torch
import requests
import torchvision.models as models
from torchvision import transforms
from PIL import Image


def test_resnet(record_property):
    record_property("model_name", "ResNet50")

    # Load the ResNet-50 model with updated API
    weights = models.ResNet50_Weights.DEFAULT
    model = models.resnet50(weights=weights)    
    model.eval()  # Set the model to evaluation mode
    model = model.to(torch.bfloat16)

    # Define a transformation to preprocess the input image using the weights transforms
    preprocess = weights.transforms()

    # Load and preprocess the image
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    img_t = preprocess(image)
    batch_t = torch.unsqueeze(img_t, 0)

    # Perform inference
    with torch.no_grad():
        output = model(batch_t)

    # Print the top 5 predictions
    _, indices = torch.topk(output, 5)
    print(f"Top 5 predictions: {indices[0].tolist()}")

    record_property("torch_ttnn", (model, batch_t, output))


# Empty property record_property
def empty_record_property(a, b):
    pass


# Run pytorch implementation
if __name__ == "__main__":
    test_resnet(empty_record_property)
