import torch
import torchvision


def test_resnet(record_property):
    record_property("model_name", "ResNet18")

    # Download model from cloud
    model = torchvision.models.get_model("resnet18", pretrained=True)
    model.eval()
    model = model.to(torch.bfloat16)

    # Create random input tensor
    input_batch = torch.rand((1, 3, 224, 224), dtype=torch.bfloat16)

    # Run inference with the original model
    with torch.no_grad():
        output = model(input_batch)

    # Check inference result
    record_property("torch_ttnn", (model, input_batch, output))

    # Memory analysis
    record_property("memory_analysis", (model, input_batch))
