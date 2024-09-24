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
import torch_ttnn.metrics as metrics
import subprocess
import sys

mb_in_bytes = 1048576


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
def skip_by_platform(request, device):
    platforms = {
        "grayskull": ttnn.device.is_grayskull(device),
        "wormhole_b0": ttnn.device.is_wormhole_b0(device),
    }
    if skip_platform := request.node.get_closest_marker("skip_platform"):
        if skip_platform.args:
            arch = skip_platform.args[0]
            if current_platform := platforms.get(arch):
                pytest.skip(f"Skipped on {arch}")
            elif current_platform == None:
                raise ValueError(f'pytest.skip_platform arch: "{arch}" not valid.')
            # if false, then continue with test
        else:
            raise ValueError(
                f'pytest.skip_platform missing arch argument string, i.e. pytest.skip_platform("grayskull")'
            )


@pytest.fixture(autouse=True)
def compile_and_run(device, reset_torch_dynamo, request):
    # Initialize early to ensure it's defined
    runtime_metrics = {"success": False}  # Initialize early to ensure it's defined
    comp_runtime_metrics = {
        "success": False,
        "fits_in_memory": "N/A",
        "peak_sram_usage": 0,
    }
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
            # Why `inputs.requires_grad`?
            #
            # Backward pass computes gradients for all trainable weight tensors.
            # However, verifying every gradient can be costly, especially for
            # large models with many parameters.
            #
            # Instead of checking each gradient, we check the gradient
            # of the "model input" tensor only. Computing the input gradient
            # serves as an indicator for the health of all other gradients.
            # Based on the "chain rule", the input gradient depends on all other
            # gradients, so any incorrect gradient computation should reflect here.
            is_backward_checked = True if model.training and inputs.requires_grad else False
        except Exception as e:
            # Exception to handle unsupported case of multiple model inputs.
            # Currently, we assume the model has a single input for backward pass checks.
            is_backward_checked = False

        try:
            # Compile model with ttnn backend
            option = torch_ttnn.TorchTtnnOption(
                device=device,
                gen_graphviz=True,
                run_mem_analysis=False,
                metrics_path=model_name,
                verbose=True,
            )
            m = torch.compile(model, backend=torch_ttnn.backend, options=option)

            start = time.perf_counter() * 1000

            if is_backward_checked:
                # Reset gradients before each backward pass.
                #
                # Gradients are accumulated by default.
                # Without resetting, two backward passes with the same input values
                # may yield different gradients, making it impossible to compare against
                # the expected (golden) results.
                inputs.grad = None
                m.zero_grad()

                # Forward pass
                forward_output = m(inputs)

                # Using `torch.mean` as the loss function for testing purposes.
                #
                # Loss functions typically produce a scalar loss, and `torch.mean`
                # is one valid option in this category. While it may not be the best
                # choice for training effective models, it simplifies our testing process.
                #
                # Since our goal is to verify gradient computation rather than to
                # train a high-performing model, applying `torch.mean` uniformly
                # across all models under test eases the testing procedure.
                loss = torch.mean(forward_output)

                # Backward pass
                loss.backward()

                # Using the gradient of the model input as the output data for comparison.
                # This gradient serves as the basis for comparing against the golden values,
                # helping to verify the correctness of gradient computations during testing.
                outputs_after = inputs.grad
            else:
                outputs_after = run_model(m, inputs)

            end = time.perf_counter() * 1000
            comp_runtime_metrics = {"success": True, "run_time": round(end - start, 2)}
            option._out_fx_graphs[0].print_tabular()
            accuracy = calculate_accuracy(outputs, outputs_after)
            if accuracy:
                comp_runtime_metrics["accuracy"] = accuracy
            # dump compiled aten schemas
            metrics.save_pickle(
                [x.dict() for x in option.compiled_schema_list],
                option.metrics_path,
                "compiled-schema_list",
            )

            # # Memory analysis
            # TODO: re-enable memory analysis

            # mm = option.memory_manager
            # # Convert bytes to MB
            # peak_usage = mm.peak_sram_usage / mb_in_bytes
            # comp_runtime_metrics["peak_sram_usage"] = peak_usage

            # if mem_utils.check_sram_overflow(mm) is True:
            #     comp_runtime_metrics["fits_in_memory"] = "No"
            # else:
            #     comp_runtime_metrics["fits_in_memory"] = "Yes"

            # # These are for plotting charts for later inspection
            # from tools.plot_chart import (
            #     plot_mem_footprint_bar_chart,
            #     plot_mem_footprint_line_chart,
            # )

            # bar_chart_file = f"metrics/{model_name}/bar_chart.png"
            # line_chart_file = f"metrics/{model_name}/line_chart.png"
            # plot_mem_footprint_bar_chart(mm.data_points, bar_chart_file)
            # plot_mem_footprint_line_chart(mm.data_points, line_chart_file)

            # log_file = f"metrics/{model_name}/memory_footprint.txt"
            # with open(log_file, "w") as f:
            #     f.write(mm.logs)

        except Exception as e:
            comp_runtime_metrics = {
                "success": False,
                "fits_in_memory": "N/A",
                "peak_sram_usage": 0,
            }
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
            metrics.save_pickle(
                [x.dict() for x in option.original_schema_list],
                option.metrics_path,
                "original-schema_list",
            )
            compiled_metrics_path = p / f"compiled-run_time_metrics.pickle"
            with open(compiled_metrics_path, "wb") as f:
                pickle.dump(comp_runtime_metrics, f)
            # dump compiled aten schemas
            metrics.save_pickle(
                [x.dict() for x in option.compiled_schema_list],
                option.metrics_path,
                "compiled-schema_list",
            )


def run_model(model, inputs):
    if isinstance(inputs, collections.Mapping):
        return model(**inputs)
    elif isinstance(inputs, collections.Sequence):
        return model(*inputs)
    else:
        return model(inputs)


@pytest.fixture(scope="module")
def manage_dependencies(request):
    dependencies = getattr(request.module, "dependencies", [])
    # Install dependencies
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + dependencies)
    yield
    # Uninstall dependencies
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y"] + dependencies)
