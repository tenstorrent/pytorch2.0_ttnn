import torch
import torch_ttnn
import ttnn
from PIL import Image
import requests

# Load model directly
from transformers import AutoImageProcessor, AutoModelForObjectDetection


if __name__ == "__main__":
    # Open device 0
    device: ttnn.Device = ttnn.open_device(device_id=0)

    # Download model from cloud
    model_name = "hustvl/yolos-tiny"
    image_processor = AutoImageProcessor.from_pretrained(
        model_name,
    )
    m = AutoModelForObjectDetection.from_pretrained(
        model_name,
    )
    m.eval()

    # Set up sample input
    test_input = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(test_input, stream=True).raw)
    inputs = image_processor(images=image, return_tensors="pt")

    metrics_path = "yolo"

    # Compile model with ttnn backend
    option = torch_ttnn.TorchTtnnOption(
        device=device, metrics_path=metrics_path
    )
    m = torch.compile(m, backend=torch_ttnn.memory_backend, options=option)

    # Run inference with the compiled model
    with torch.no_grad():
        outputs_after = m(**inputs)
    
     # These are for plotting charts for later inspection
    from tools.memory_models.plot_chart import plot_bar_chart, plot_line_chart
    src_file = "./data/memory/memory_footprint.txt"
    bar_chart_file = "./tools/memory_models/assets/yolo_bar_chart.png"
    line_chart_file = "./tools/memory_models/assets/yolo_line_chart.png"
    plot_bar_chart(src_file, bar_chart_file)
    plot_line_chart(src_file, line_chart_file)
        
    # Close the device
    ttnn.close_device(device)
