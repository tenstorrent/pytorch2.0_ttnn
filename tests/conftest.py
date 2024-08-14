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

    try:
        torch_ttnn_flag = False
        if "torch_ttnn" in record:
            model, inputs, outputs = record["torch_ttnn"]
            # check that model contains a forward function
            assert "forward" in dir(model), f"forward() not implemented in {model_name}"
            # Compile model with ttnn backend
            option = torch_ttnn.TorchTtnnOption(
                device=device, gen_graphviz=True, metrics_path=model_name
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
            torch_ttnn_flag = True

        memory_analysis_flag = False
        if "memory_analysis" in record:
            model, inputs = record["memory_analysis"]
            # check that model contains a forward function
            assert "forward" in dir(model), f"forward() not implemented in {model_name}"
            # Compile model with ttnn backend
            option = torch_ttnn.TorchTtnnOption(
                device=device, gen_graphviz=True, metrics_path=model_name
            )
            option.run_mem_analysis = True
            m = torch.compile(model, backend=torch_ttnn.backend, options=option)

            if isinstance(inputs, collections.Mapping):
                outputs_after = m(**inputs)
            elif isinstance(inputs, collections.Sequence):
                outputs_after = m(*inputs)
            else:
                outputs_after = m(inputs)

            mm = option._memory_manager
            compiled_memory_metric = {}
            if mem_utils.check_sram_overflow(mm) is True:
                compiled_memory_metric = {"fits_in_memory": "No"}
            else:
                compiled_memory_metric = {"fits_in_memory": "Yes"}
            memory_analysis_flag = True
        
    except Exception as e:
        if not (torch_ttnn_flag is True and memory_analysis_flag is False):
            comp_runtime_metrics = {"success": False}
        compiled_memory_metric = {"fits_in_memory": "N/A"}
        print(f"{model_name} compiled failed to run. Raised exception: {e}")
        raise

    finally:
        # For tests with no calls to record_property
        if record == {}:
            return
        compiled_metrics_path = p / f"compiled-run_time_metrics.pickle"
        with open(compiled_metrics_path, "wb") as f:
            pickle.dump(comp_runtime_metrics, f)
        compiled_memory_metrics_path = p / f"compiled_memory_metrics.pickle"
        with open(compiled_memory_metrics_path, "wb") as f:
            pickle.dump(compiled_memory_metric, f)

    
