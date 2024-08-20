import pytest
import ttnn
import torch
import torch_ttnn
import collections
from tests.utils import calculate_accuracy
import time
from pathlib import Path
import os
import pickle
from torch_ttnn import mem_utils


@pytest.fixture(scope="session")
def device():
    device = ttnn.open_device(device_id=0)
    yield device
    ttnn.close_device(device)


@pytest.fixture(autouse=True)
def reset_torch_dynamo():
    # PyTorch caches models. Start a fresh compile for each parameter of the test case.
    torch._dynamo.reset()
    yield


@pytest.fixture(autouse=True)
def compile_and_run(device, reset_torch_dynamo, request):
    try:
        start = time.perf_counter() * 1000
        yield
        end = time.perf_counter() * 1000
        runtime_metrics = {"success": True, "run_time": round(end - start, 2)}
    except Exception as e:
        runtime_metrics = {"success": False}
        print(f"{model_name} original failed to run. Raised exception: {e}")
        raise
    finally:
        record = dict(request.node.user_properties)
        model_path = Path(request.node.location[0])
        runtime_metrics["model_path"] = str(model_path.parent)
        if "model_name" in record:
            model_name = record["model_name"]
            p = Path(f"metrics/{model_name}")
            os.makedirs(p, exist_ok=True)

            original_metrics_path = p / f"original-run_time_metrics.pickle"
            with open(original_metrics_path, "wb") as f:
                pickle.dump(runtime_metrics, f)

    if "torch_ttnn" in record:
        model, inputs, outputs = record["torch_ttnn"]
        try:
            # check that model contains a forward function
            assert "forward" in dir(model), f"forward() not implemented in {model_name}"
            # Compile model with ttnn backend
            option = torch_ttnn.TorchTtnnOption(
                device=device,
                gen_graphviz=True,
                run_mem_analysis=True,
                metrics_path=model_name,
            )
            m = torch.compile(model, backend=torch_ttnn.backend, options=option)

            start = time.perf_counter() * 1000
            if isinstance(inputs, collections.Mapping):
                outputs_after = m(**inputs)
            elif isinstance(inputs, collections.Sequence):
                outputs_after = m(*inputs)
            else:
                outputs_after = m(inputs)
            end = time.perf_counter() * 1000
            comp_runtime_metrics = {"success": True, "run_time": round(end - start, 2)}
            option._out_fx_graphs[0].print_tabular()
            accuracy = calculate_accuracy(outputs, outputs_after)
            if accuracy:
                comp_runtime_metrics["accuracy"] = accuracy

            # Memory analysis
            mm = option.memory_manager
            # Convert bytes to MB
            peak_usage = mm.peak_sram_usage / 1048576
            comp_runtime_metrics["peak_sram_usage"] = peak_usage

            if mem_utils.check_sram_overflow(mm) is True:
                comp_runtime_metrics["fits_in_memory"] = "No"
            else:
                comp_runtime_metrics["fits_in_memory"] = "Yes"

            # These are for plotting charts for later inspection
            from tools.plot_chart import (
                plot_mem_footprint_bar_chart,
                plot_mem_footprint_line_chart,
            )

            bar_chart_file = f"metrics/{model_name}/bar_chart.png"
            line_chart_file = f"metrics/{model_name}/line_chart.png"
            plot_mem_footprint_bar_chart(mm.data_points, bar_chart_file)
            plot_mem_footprint_line_chart(mm.data_points, line_chart_file)

            log_file = f"metrics/{model_name}/memory_footprint.txt"
            with open(log_file, "w") as f:
                f.write(mm.logs)

        except Exception as e:
            comp_runtime_metrics = {
                "success": False,
                "fits_in_memory": "N/A",
                "peak_sram_usage": 0,
            }
            print(f"{model_name} compiled failed to run. Raised exception: {e}")
            raise

        finally:
            compiled_metrics_path = p / f"compiled-run_time_metrics.pickle"
            with open(compiled_metrics_path, "wb") as f:
                pickle.dump(comp_runtime_metrics, f)
