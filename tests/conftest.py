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
import torch_ttnn.metrics as metrics


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
    runtime_metrics = {"success": False}  # Initialize early to ensure it's defined
    comp_runtime_metrics = {"success": False}  # Initialize compiled metrics
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
            # Compile model with ttnn backend
            option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True, metrics_path=model_name)
            m = torch.compile(model, backend=torch_ttnn.backend, options=option)

            start = time.perf_counter() * 1000
            outputs_after = run_model(m, inputs)
            end = time.perf_counter() * 1000
            comp_runtime_metrics = {"success": True, "run_time": round(end - start, 2)}
            option._out_fx_graphs[0].print_tabular()
            accuracy = calculate_accuracy(outputs, outputs_after)
            if accuracy:
                comp_runtime_metrics["accuracy"] = accuracy

            # dump compiled aten schemas
            metrics.save_pickle(option.compiled_schema_list, option.metrics_path, "compiled-schema_list")
        except Exception as e:
            comp_runtime_metrics = {"success": False}
            try:
                # Rerun with bypass option to collect aten op metrics
                torch._dynamo.reset()
                option.bypass_compile = True
                option.reset_containers()
                m = torch.compile(model, backend=torch_ttnn.backend, options=option)
                run_model(m, inputs)
            except Exception as e2:
                err_msg = f"{model_name} - Torch run with bypass compilation failed. "
                err_msg += "Please check whether `model` or `model.generate` is passed to `record_property`."
                raise TypeError(err_msg) from e2
            else:
                if request.node.get_closest_marker("compilation_xfail"):
                    pytest.xfail()
                else:
                    raise TypeError(f"{model_name} compiled failed to run.") from e
        finally:
            # dump original aten schemas
            metrics.save_pickle(option.original_schema_list, option.metrics_path, "original-schema_list")
            compiled_metrics_path = p / f"compiled-run_time_metrics.pickle"
            with open(compiled_metrics_path, "wb") as f:
                pickle.dump(comp_runtime_metrics, f)


def run_model(model, inputs):
    if isinstance(inputs, collections.Mapping):
        return model(**inputs)
    elif isinstance(inputs, collections.Sequence):
        return model(*inputs)
    else:
        return model(inputs)
