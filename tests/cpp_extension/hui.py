from transformers import BertModel, BertTokenizer
import torch
import torch_ttnn
import ttnn
from torch_ttnn.cpp_extension import ttnn_module
import types
import math

model = BertModel.from_pretrained("bert-large-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-large-uncased")
model.eval()

# Debug BERT model configuration
print("=== BERT Model Configuration ===")
print(f"Hidden size: {model.config.hidden_size}")
print(f"Number of attention heads: {model.config.num_attention_heads}")
print(f"Attention head size: {model.config.hidden_size // model.config.num_attention_heads}")
print(f"Sqrt of attention head size: {math.sqrt(model.config.hidden_size // model.config.num_attention_heads)}")
print(f"================================")

text = "Hello, this is a test sentence for BERT."
inputs = tokenizer(text, return_tensors="pt")

# Debug: Print input shapes before device conversion
print("Original input shapes:")
for k, v in inputs.items():
    print(f"  {k}: {v.shape}")

device = ttnn.open_device(
    device_id=0,
    l1_small_size=0,
    trace_region_size=0,
    dispatch_core_config=ttnn.DispatchCoreConfig(ttnn.DispatchCoreType.ETH),
    worker_l1_size=0
)

torch_device = ttnn_module.as_torch_device(device)

# Convert model to bfloat16 before moving to TTNN device
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

# Debug: Print input shapes after device conversion
print("TTNN device input shapes:")
for k, v in inputs.items():
    print(f"  {k}: {v.shape}")

# Enhanced debugging hook to catch tensor shapes at different stages
def debug_linear_hook(module, input, output):
    print(f"=== Linear layer debug ===")
    print(f"Module: {module}")
    print(f"Input tensor shape: {input[0].shape}")
    print(f"Input tensor dtype: {input[0].dtype}")
    print(f"Input tensor device: {input[0].device}")
    if hasattr(module, 'weight'):
        print(f"Weight shape: {module.weight.shape}")
        print(f"Weight dtype: {module.weight.dtype}")
        print(f"Weight device: {module.weight.device}")
    if hasattr(module, 'bias') and module.bias is not None:
        print(f"Bias shape: {module.bias.shape}")
        print(f"Bias dtype: {module.bias.dtype}")
        print(f"Bias device: {module.bias.device}")
    print(f"Output shape: {output.shape}")
    print(f"========================")
    return output

# Hook to debug embeddings layer
def debug_embeddings_hook(module, input, output):
    print(f"=== Embeddings debug ===")
    print(f"Input shape: {input[0].shape if len(input) > 0 else 'No input'}")
    print(f"Output shape: {output.shape}")
    print(f"Output dtype: {output.dtype}")
    print(f"Output device: {output.device}")
    print(f"========================")
    return output

# Hook to debug attention mechanism
def debug_attention_hook(module, input, output):
    print(f"=== Attention debug ===")
    print(f"Module: {module}")
    print(f"Input tensor shape: {input[0].shape}")
    print(f"Input tensor dtype: {input[0].dtype}")
    print(f"Input tensor device: {input[0].device}")
    if len(output) > 0:
        print(f"Output tensor shape: {output[0].shape}")
        print(f"Output tensor dtype: {output[0].dtype}")
        print(f"Output tensor device: {output[0].device}")
    print(f"=======================")
    return output

# Hook to debug matmul operations
def debug_matmul_hook(name):
    def hook(module, input, output):
        print(f"=== {name} debug ===")
        print(f"Input 1 shape: {input[0].shape}")
        print(f"Input 1 dtype: {input[0].dtype}")
        print(f"Input 1 device: {input[0].device}")
        if len(input) > 1:
            print(f"Input 2 shape: {input[1].shape}")
            print(f"Input 2 dtype: {input[1].dtype}")
            print(f"Input 2 device: {input[1].device}")
        print(f"Output shape: {output.shape}")
        print(f"Output dtype: {output.dtype}")
        print(f"Output device: {output.device}")
        print(f"=======================")
        return output
    return hook

# Hook to debug division operations
def debug_division_hook(name):
    def hook_fn(original_fn):
        def wrapper(*args, **kwargs):
            print(f"=== {name} Division Operation Debug ===")
            print(f"Function: {original_fn}")
            print(f"Args: {len(args)}")
            for i, arg in enumerate(args):
                if hasattr(arg, 'shape'):
                    print(f"  Arg {i}: shape={arg.shape}, dtype={arg.dtype}, device={arg.device}")
                else:
                    print(f"  Arg {i}: {arg} (type: {type(arg)})")
            print(f"Kwargs: {kwargs}")
            try:
                result = original_fn(*args, **kwargs)
                print(f"Result shape: {result.shape}")
                print(f"Result dtype: {result.dtype}")
                print(f"Result device: {result.device}")
                print(f"=======================================")
                return result
            except Exception as e:
                print(f"ERROR in {name}: {e}")
                print(f"=======================================")
                raise
        return wrapper
    return hook_fn

# Monkey patch torch division operations to debug
original_div = torch.div
original_truediv = torch.Tensor.__truediv__
original_rtruediv = torch.Tensor.__rtruediv__

torch.div = debug_division_hook("torch.div")(original_div)
torch.Tensor.__truediv__ = debug_division_hook("tensor.__truediv__")(original_truediv)
torch.Tensor.__rtruediv__ = debug_division_hook("tensor.__rtruediv__")(original_rtruediv)

# Register hooks on multiple layers to trace the flow
model.embeddings.register_forward_hook(debug_embeddings_hook)
model.embeddings.word_embeddings.register_forward_hook(debug_linear_hook)

# Hook the first attention layer
first_attention_layer = model.encoder.layer[0].attention.self
first_attention_layer.register_forward_hook(debug_attention_hook)
first_attention_layer.query.register_forward_hook(debug_linear_hook)
first_attention_layer.key.register_forward_hook(debug_linear_hook)
first_attention_layer.value.register_forward_hook(debug_linear_hook)

with torch.no_grad():
    try:
        print("Starting model forward pass...")
        output = model(**inputs)
        print("Model forward pass completed successfully!")
        print(f"Final output shape: {output.last_hidden_state.shape}")
        print(f"Final output dtype: {output.last_hidden_state.dtype}")
        print(f"Final output device: {output.last_hidden_state.device}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        
        # Try to get more info about the current tensor states
        print("\n=== Additional Debug Info ===")
        print(f"Input tensors are on device: {[v.device for v in inputs.values()]}")
        print(f"Model device: {next(model.parameters()).device}")
        
        # Check if the F.linear operation is mapped
        try:
            import torch.nn.functional as F
            print(f"F.linear function: {F.linear}")
        except:
            print("Could not access F.linear")
            
        # Try to get specific attention layer info
        try:
            attention_layer = model.encoder.layer[0].attention.self
            print(f"Attention layer device: {next(attention_layer.parameters()).device}")
            print(f"Attention head size: {attention_layer.attention_head_size}")
        except Exception as inner_e:
            print(f"Could not get attention layer info: {inner_e}")
            
        # Check current tensor memory usage
        try:
            import gc
            gc.collect()
            print(f"Current TTNN tensors in memory: {len([obj for obj in gc.get_objects() if 'ttnn' in str(type(obj))])}")
        except:
            pass
            
    finally:
        # Restore original functions
        torch.div = original_div
        torch.Tensor.__truediv__ = original_truediv
        torch.Tensor.__rtruediv__ = original_rtruediv
        
        # Close the device
        ttnn.close_device(device)