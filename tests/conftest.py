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
import logging

mb_in_bytes = 1048576

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("test_fixture.log"), logging.StreamHandler()],
)


def pytest_addoption(parser):
    parser.addoption("--input_var_only_native", action="store_true")
    parser.addoption("--input_var_check_ttnn", action="store_true")
    parser.addoption("--input_var_check_accu", action="store_true")
    parser.addoption(
        "--report_nth_iteration",
        action="store",
        default=1,
        help="Run up to the specified iteration count and report metrics based on this iteration.",
    )


@pytest.fixture(scope="session")
def input_var_only_native(request):
    return request.config.getoption("--input_var_only_native")


@pytest.fixture(scope="session")
def input_var_check_accu(request):
    return request.config.getoption("--input_var_check_accu")


@pytest.fixture(scope="session")
def input_var_check_ttnn(request):
    return request.config.getoption("--input_var_check_ttnn")


@pytest.fixture(scope="session")
def device():
    # TODO(tt-metal#13746): Currently L1 small size needs to be manually determined
    device_id = 0
    l1_small_size = 16384
    dispatch_core_config = get_dispatch_core_config()

    device = ttnn.open_device(device_id=device_id, dispatch_core_config=dispatch_core_config, l1_small_size=16384)

    ttnn.SetDefaultDevice(device)

    yield device

    ttnn.synchronize_device(device)
    ttnn.close_device(device)


def get_dispatch_core_type():
    # Instead of conditionally returning WORKER or ETH, here we always return ETH
    # Without setting this property, we get less cores availble on N300 than on N150, which might lead to inconsistent and sub-sufficient results
    return ttnn.device.DispatchCoreType.ETH


def get_dispatch_core_axis():
    # Should be ttnn.DispatchCoreAxis.COL for Blackhole
    return ttnn.DispatchCoreAxis.ROW


def get_dispatch_core_config():
    dispatch_core_type = get_dispatch_core_type()
    dispatch_core_axis = get_dispatch_core_axis()
    dispatch_core_config = ttnn.DispatchCoreConfig(dispatch_core_type, dispatch_core_axis)
    return dispatch_core_config


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
    logging.info("Starting the compile_and_run fixture.")

    runtime_metrics = {"success": False}  # Initialize early to ensure it's defined
    comp_runtime_metrics = {
        "success": False,
        "fits_in_memory": "N/A",
        "peak_sram_usage": 0,
    }
    try:
        logging.debug("Initializing test run timing.")
        start = time.perf_counter() * 1000
        yield
        end = time.perf_counter() * 1000
        runtime_metrics = {"success": True, "run_time": round(end - start, 2)}
        logging.info(f"Test run completed successfully in {runtime_metrics['run_time']} ms.")
    except Exception as e:
        runtime_metrics = {"success": False}
        logging.error(f"Test run failed. Exception: {e}", exc_info=True)
        raise
    finally:
        logging.debug("Processing runtime metrics.")
        record = dict(request.node.user_properties)
        model_path = Path(request.node.location[0])
        runtime_metrics["model_path"] = str(model_path.parent)

        if "model_name" in record:
            model_name = record["model_name"]
            if "mode" in record and record["mode"] != "eval":
                model_name = f"{model_name}-{record['mode']}"
            p = Path(f"metrics/{model_name}")
            os.makedirs(p, exist_ok=True)

            original_metrics_path = p / "original-run_time_metrics.pickle"
            with open(original_metrics_path, "wb") as f:
                pickle.dump(runtime_metrics, f)
            logging.info(f"Runtime metrics saved to {original_metrics_path}.")

    if "torch_ttnn" in record:
        model_tester, outputs = record["torch_ttnn"]
        from tests.utils import ModelTester

        if not isinstance(model_tester, ModelTester):
            logging.error("model_tester must be an instance of ModelTester.")
            raise TypeError("model_tester must be instance of ModelTester")

        try:
            logging.debug("Compiling model with ttnn backend.")
            option = torch_ttnn.TorchTtnnOption(
                device=device,
                gen_graphviz=False,
                run_mem_analysis=False,
                metrics_path=model_name,
                verbose=True,
            )
            for idx in range(int(request.config.getoption("--report_nth_iteration"))):
                start = time.perf_counter() * 1000
                # Don't need to reset options if inputs don't change because of cache
                outputs_after = model_tester.test_model(as_ttnn=True, option=option)
                end = time.perf_counter() * 1000
                run_time = end - start
                if idx == 0:
                    first_iter_runtime = run_time

            comp_runtime_metrics = {
                "success": True,
                "run_time": round(run_time, 2),
                "run_time_first_iter": round(first_iter_runtime, 2),
            }
            logging.info(f"Compilation and run successful in {comp_runtime_metrics['run_time']} ms.")

            if len(option._out_fx_graphs) > 0:
                option._out_fx_graphs[0].print_tabular()

            if model_name not in ["speecht5-tts"]:
                accuracy = calculate_accuracy(outputs, outputs_after)
                if accuracy:
                    comp_runtime_metrics["accuracy"] = accuracy
                    logging.info(f"Accuracy calculated: {accuracy}.")

            metrics.save_pickle(
                [x.dict() for x in option.compiled_schema_list],
                option.metrics_path,
                "compiled-schema_list",
            )
        except Exception as e:
            logging.error("Compilation failed.", exc_info=True)
            comp_runtime_metrics = {
                "success": False,
                "fits_in_memory": "N/A",
                "peak_sram_usage": 0,
            }
            try:
                logging.debug("Attempting rerun with bypass option to collect aten op metrics.")
                torch._dynamo.reset()
                option.bypass_compile = True
                option.reset_containers()
                model_tester.test_model(as_ttnn=True, option=option)
            except Exception as e2:
                logging.critical(
                    "Rerun with bypass compilation failed. Please check model or model.generate.",
                    exc_info=True,
                )
                raise TypeError(
                    f"{model_name} - Torch run with bypass compilation failed. "
                    "Please check whether `model` or `model.generate` is passed to `record_property`."
                ) from e2
            else:
                if request.node.get_closest_marker("compilation_xfail"):
                    pytest.xfail()
                else:
                    raise TypeError(f"{model_name} compiled failed to run.") from e
        finally:
            logging.debug("Saving metrics.")
            metrics.save_pickle(
                [x.dict() for x in option.original_schema_list],
                option.metrics_path,
                "original-schema_list",
            )
            compiled_metrics_path = p / "compiled-run_time_metrics.pickle"
            with open(compiled_metrics_path, "wb") as f:
                pickle.dump(comp_runtime_metrics, f)
            logging.info(f"Compiled runtime metrics saved to {compiled_metrics_path}.")


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
