import ttnn
import sys
import io
import torch_ttnn
import torch
import streamlit as st
import time


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
    dispatch_core_config = get_dispatch_core_config()
    device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
    ttnn.enable_program_cache(device)
    option = torch_ttnn.TorchTtnnOption(device=device)
    model = torch.compile(model, backend=torch_ttnn.backend, options=option)
    bar = st.progress(0, text="Compiling & warming up …")
    step_percent = 100 / (iterations - 1)
    for i in range(iterations - 1):
        if mapping:
            _ = model(**inputs)
        else:
            _ = model(inputs)
        pct = int(step_percent * (i + 1))
        if pct == 100:
            bar.progress(pct, text="Compilation complete")
        else:
            bar.progress(pct, text=f"Compiling & warming up: {pct}%")
    return device  # This is necessary to make sure device is included in the scope of the model script (So it can be closed in the model script)


def compile_ttnn_clm(model, iterations, max_length, inputs):
    dispatch_core_config = get_dispatch_core_config()
    device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
    ttnn.enable_program_cache(device)
    option = torch_ttnn.TorchTtnnOption(device=device)
    model = torch.compile(model, backend=torch_ttnn.backend, options=option)
    bar = st.progress(0, text="Compiling & warming up (may take a few minutes)")
    step_percent = 100 / (iterations - 1)
    start_time = time.time()
    for i in range(iterations - 1):
        _ = model.generate(
            **inputs,
            max_length=max_length,
            num_return_sequences=1,
            do_sample=True,
        )
        current_time = time.time()
        step_time = current_time - start_time
        estimated_total_time = (step_time / (i + 1)) * iterations
        estimated_time_remaining = estimated_total_time - step_time
        estimated_minutes_remaining = estimated_time_remaining / 60
        pct = int(step_percent * (i + 1))
        bar.progress(
            pct,
            text=f"Compiling & warming up: {pct}% (Estimated time remaining: {estimated_minutes_remaining:.2f} minutes)",
        )

    return device  # This is necessary to make sure device is included in the scope of the model script (So it can be closed in the model script)


def get_inference_latency(model, inputs, mapping=True):
    st.write("Getting model latency...")
    start_time = time.time()
    if mapping:
        outputs = model(**inputs)
    else:
        outputs = model(inputs)
    end_time = time.time()
    inference_time = end_time - start_time
    return inference_time, outputs
