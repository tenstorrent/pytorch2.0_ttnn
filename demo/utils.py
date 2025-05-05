import ttnn
import sys
import io
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)  # This is necessary to import torch_ttnn

import torch_ttnn
import torch
import streamlit as st
import time
import matplotlib.pyplot as plt


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
    start_time = time.time()
    logged_times = []
    for i in range(iterations - 1):
        if mapping:
            _ = model(**inputs)
        else:
            _ = model(inputs)
        curr_time = time.time()
        logged_times.append(curr_time - start_time)
        start_time = curr_time
        pct = int(step_percent * (i + 1))
        if pct == 100:
            bar.progress(pct, text="Compilation complete")
        else:
            bar.progress(pct, text=f"Compiling & warming up: {pct}%")
    iterations = list(range(1, len(logged_times) + 1))  # x-axis: iteration numbers

    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    ax.plot(iterations, logged_times, marker="o", label="Execution Time (s)")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Time (s)")
    ax.set_title("Execution Time vs Warm-up Iteration")
    ax.legend()
    ax.grid(True)

    # Display the plot in Streamlit
    st.pyplot(fig)
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
