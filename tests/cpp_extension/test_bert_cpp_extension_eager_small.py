from transformers import BertModel, BertTokenizer
import torch
import torch_ttnn
import ttnn
from torch_ttnn.cpp_extension import ttnn_module

model = BertModel.from_pretrained("bert-large-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-large-uncased")
model.eval()

text = "Hello, this is a test sentence for BERT."
inputs = tokenizer(text, return_tensors="pt")

device = ttnn.open_device(
    device_id=0,
    l1_small_size=0,
    trace_region_size=0,
    dispatch_core_config=ttnn.DispatchCoreConfig(ttnn.DispatchCoreType.ETH),
    worker_l1_size=0
)

torch_device = ttnn_module.as_torch_device(device)

model = model.to(torch.bfloat16)
model = model.to(torch_device)

option = torch_ttnn.TorchTtnnOption(
    device=device,
    gen_graphviz=False,
    run_mem_analysis=False,
    metrics_path="bert-large-uncased",
    verbose=True,
    load_params_once=False,
)

inputs = {k: v.to(torch.bfloat16).to(torch_device) for k, v in inputs.items()}

with torch.no_grad():
    try:
        output = model(**inputs)
        print(f"Model forward pass completed successfully!")
        print(f"Final output shape: {output.last_hidden_state.shape}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally: