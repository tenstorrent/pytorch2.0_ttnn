import torch
import torchvision
import torch_ttnn
import ttnn


if __name__ == "__main__":
    # Open device 0
    device: ttnn.Device = ttnn.open_device(device_id=0)

    # Download model from cloud
    model = torchvision.models.get_model("resnet18", pretrained=True)
    model.eval()
    model = model.to(torch.bfloat16)

    # Create random input tensor
    input_batch = torch.rand((1, 3, 224, 224), dtype=torch.bfloat16)

    metrics_path = "ResNet18"

    # Compile the model
    option = torch_ttnn.TorchTtnnOption(
        device=device, metrics_path=metrics_path
    )
    option.gen_graphviz = True
    option.run_mem_analysis = True
    model = torch.compile(model, backend=torch_ttnn.backend, options=option)
    # Run inference with the compiled model
    with torch.no_grad():
        output_after = model(input_batch)

    # These are for plotting charts for later inspection
    from tools.memory_models.plot_chart import plot_bar_chart, plot_line_chart
    src_file = "./data/memory/memory_footprint.txt"
    bar_chart_file = "./tools/memory_models/assets/resnet_bar_chart.png"
    line_chart_file = "./tools/memory_models/assets/resnet_line_chart.png"
    plot_bar_chart(src_file, bar_chart_file)
    plot_line_chart(src_file, line_chart_file)

    # Close the device
    ttnn.close_device(device)
