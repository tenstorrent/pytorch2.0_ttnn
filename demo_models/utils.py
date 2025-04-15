import ttnn
import sys
import io
import torch_ttnn
import torch

def get_dispatch_core_type():
    return ttnn.device.DispatchCoreType.ETH


def get_dispatch_core_axis():
    return ttnn.DispatchCoreAxis.ROW


def get_dispatch_core_config():
    dispatch_core_type = get_dispatch_core_type()
    dispatch_core_axis = get_dispatch_core_axis()
    dispatch_core_config = ttnn.DispatchCoreConfig(dispatch_core_type, dispatch_core_axis)
    return dispatch_core_config

def capture_output(func):
    def wrapper(*args, **kwargs):
        old_stdout = sys.stdout
        sys.stdout = output = io.StringIO()
        try:
            result = func(*args, **kwargs)
            output_str = output.getvalue()
            words = output_str.split()
            if len(words) > 200:
                output_str = " ".join(words[:200]) + " [Truncated...]"
            return result, output_str
        finally:
            sys.stdout = old_stdout
    return wrapper

def stream_response(response):
    for char in response:
        yield char

def compile_ttnn(model, iterations, inputs, mapping=True):
    print("Opening TTNN device...")
    dispatch_core_config = get_dispatch_core_config()
    device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
    ttnn.enable_program_cache(device)
    print("Compiling model with TTNN...")
    option = torch_ttnn.TorchTtnnOption(device=device)
    model = torch.compile(model, backend=torch_ttnn.backend, options=option)
    for i in range(iterations - 1):
        if mapping:
            _ = model(**inputs)
        else:
            _ = model(inputs)
    return device # This is necessary to make sure device is included in the scope of the model script (So it can be closed in the model script)

def compile_ttnn_clm(model, iterations, max_length, inputs):
    print("Opening TTNN device...")
    dispatch_core_config = get_dispatch_core_config()
    device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
    ttnn.enable_program_cache(device)
    print("Compiling model with TTNN...")
    option = torch_ttnn.TorchTtnnOption(device=device)
    model = torch.compile(model, backend=torch_ttnn.backend, options=option)
    print("Initial TTNN generation...")
    for i in range(iterations - 1):
        _ = model.generate(
            **inputs,
            max_length=max_length,
            num_return_sequences=1,
            do_sample=True,
        )
    return device # This is necessary to make sure device is included in the scope of the model script (So it can be closed in the model script)