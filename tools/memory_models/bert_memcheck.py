import torch
import torch_ttnn
import ttnn

# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering


if __name__ == "__main__":
    # Open device 0
    device: ttnn.Device = ttnn.open_device(device_id=0)

    # Download model from cloud
    model_name = "phiyodr/bert-large-finetuned-squad2"
    tokenizer = AutoTokenizer.from_pretrained(
        model_name, padding_side="left", torch_dtype=torch.bfloat16
    )
    m = AutoModelForQuestionAnswering.from_pretrained(
        model_name, torch_dtype=torch.bfloat16
    )
    m.eval()

    # Set up sample input
    context = 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '
    question = "What discipline did Winkelmann create?"

    inputs = tokenizer.encode_plus(
        question,
        context,
        add_special_tokens=True,
        return_tensors="pt",
        max_length=256,
        padding="max_length",
        truncation=True,
    )

    metrics_path = "BERT"

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
    bar_chart_file = "./tools/memory_models/assets/bert_bar_chart.png"
    line_chart_file = "./tools/memory_models/assets/bert_line_chart.png"
    plot_bar_chart(src_file, bar_chart_file)
    plot_line_chart(src_file, line_chart_file)

    # Close the device
    ttnn.close_device(device)
