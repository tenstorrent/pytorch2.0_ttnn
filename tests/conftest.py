# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import datetime

import pytest
import ttnn
import torch
import torch_ttnn
import collections
from tests.utils import calculate_accuracy, get_absolute_cache_path
import time
from pathlib import Path
import os
import pickle
from torch._subclasses import FakeTensor
from torch_ttnn import mem_utils
import torch_ttnn.metrics as metrics
import subprocess
import sys
import logging

import tools.export_code as export_code

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
    parser.addoption(
        "--export_code",
        action="store",
        help=f"Export standalone Python code. Supported options: {export_code.export_code_options}",
    )
    parser.addoption("--data_parallel", action="store_true")
    parser.addoption(
        "--native_integration",
        action="store_true",
        help="Use native device integration for ttnn. Note: this is not supported with data parallel.",
    )
    parser.addoption(
        "--disable_load_params_once",
        action="store_true",
        help="Disable LoadParamsOnce optimization.",
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
def device(request):
    # TODO(tt-metal#13746): Currently L1 small size needs to be manually determined
    l1_small_size = 65536
    dispatch_core_config = get_dispatch_core_config()

    if request.config.getoption("--data_parallel"):
        # TODO: allow user to specify how to split model (data parallel vs tensor parallel)
        device = ttnn.open_mesh_device(
            ttnn.MeshShape(1, 2), dispatch_core_config=dispatch_core_config, l1_small_size=l1_small_size
        )

        device.enable_program_cache()

        yield device

        ttnn.synchronize_device(device)
        ttnn.close_mesh_device(device)
    else:
        device_id = 0

        device = ttnn.open_device(
            device_id=device_id, dispatch_core_config=dispatch_core_config, l1_small_size=l1_small_size
        )

        device.enable_program_cache()

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


@pytest.fixture
def disable_load_params_once():
    """Fixture to disable load_params_once optimization in TorchTtnnOption.

    When this fixture is requested in a test function, it disables the
    load_params_once optimization. This can also be controlled via the
    --disable_load_params_once command line option.

    Example:
        def test_my_model(device, disable_load_params_once):
            # load_params_once will be disabled for this test
            ...
    """
    logging.info("load_params_once optimization disabled via disable_load_params_once fixture")
    return True


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
def check_native_integration_flag(request):
    # This acts as an allowlist where if `--native_integration` is passed, only run the model
    # if `e2e_with_native_integration` marker is also present. Otherwise skip.
    native_integration = request.config.getoption("--native_integration")
    if native_integration and not request.node.get_closest_marker("e2e_with_native_integration"):
        pytest.skip(f"Test not compatible with native integration. Skipping...")
    # else continue with test


@pytest.fixture(autouse=True)
def reset_program_cache(device):
    # TODO: delete this fixture when program cache can be left on between tests
    device.disable_and_clear_program_cache()
    device.enable_program_cache()


def get_cache_for_model_test(request):
    cache_path = get_absolute_cache_path(f"pytorch_eager_results/{request.node.name}.pkl")

    if not os.path.exists(cache_path):
        return None

    try:
        full_results = pickle.load(open(cache_path, "rb"))
        return full_results
    except:
        return None


def cache_model_test(request, results, runtime_metrics):
    parent_cache_path = get_absolute_cache_path("pytorch_eager_results/")

    os.makedirs(parent_cache_path, exist_ok=True)

    cache_path = parent_cache_path + f"{request.node.name}.pkl"

    cache_dict = {"results": results, "runtime_metrics": runtime_metrics}
    pickle.dump(cache_dict, open(cache_path, "wb"))


@pytest.fixture
def cached_results(request):
    """Get previously cached results and path where results are stored.

    returns: Tuple[results, cache_path]
    """
    full_results = get_cache_for_model_test(request)

    if full_results is None:
        return None

    return full_results.get("results")


def cached_runtime_metrics(request):
    full_results = get_cache_for_model_test(request)

    if full_results is None:
        return None

    return full_results.get("runtime_metrics")


@pytest.fixture(autouse=True)
def compile_and_run(device, reset_torch_dynamo, request):
    start_ts = datetime.datetime.now(datetime.timezone.utc)
    logging.info("Starting the compile_and_run fixture.")

    test_file_path = Path(request.node.location[0])
    print(f"Running tests in {test_file_path}")
    model_name = test_file_path.parent.name.lower()

    runtime_metrics = {
        "success": False,
        "start_ts": start_ts,
        "test_name": request.node.name,
        "test_filepath": str(test_file_path),
        "model_name": model_name,
        "model_path": str(test_file_path.parent),
    }

    comp_runtime_metrics = {
        "success": False,
        "start_ts": start_ts,
        "fits_in_memory": "N/A",
        "peak_sram_usage": 0,
    }

    try:
        logging.debug("Initializing test run timing.")
        start = time.perf_counter() * 1000
        yield
        end = time.perf_counter() * 1000
        end_ts = datetime.datetime.now(datetime.timezone.utc)

        runtime_metrics["end_time"] = end_ts
        runtime_metrics["success"] = True
        runtime_metrics["run_time"] = round(end - start, 2)

        logging.info(f"Test run completed successfully in {runtime_metrics['run_time']} ms.")
    except Exception as e:
        runtime_metrics["success"] = False
        logging.error(f"Test run failed. Exception: {e}", exc_info=True)
        raise
    finally:
        end_ts = datetime.datetime.now(datetime.timezone.utc)
        logging.debug("Processing runtime metrics.")
        record = dict(request.node.user_properties)

        if "model_name" in record:
            model_name = record["model_name"]
            if "mode" in record and record["mode"] != "eval":
                model_name = f"{model_name}-{record['mode']}"
            p = Path(f"metrics/{model_name}")
            os.makedirs(p, exist_ok=True)

            original_metrics_path = p / "original-run_time_metrics.pickle"
            runtime_metrics["end_ts"] = end_ts

            if request.session.testsfailed > 0:
                # Get error message from `sys.last_value` when we can.
                try:
                    error_message = str(sys.last_value)
                except AttributeError:
                    error_message = ""

                runtime_metrics["success"] = False
                runtime_metrics["error_message"] = error_message

            # use cached_value if exists
            cached_metrics = cached_runtime_metrics(request)
            if cached_metrics is not None:
                runtime_metrics = cached_metrics

            with open(original_metrics_path, "wb") as f:
                pickle.dump(runtime_metrics, f)
            logging.info(f"Runtime metrics saved to {original_metrics_path}.")

    if "torch_ttnn" in record:
        model_tester, outputs = record["torch_ttnn"]
        from tests.utils import ModelTester

        cache_model_test(request, outputs, runtime_metrics)

        if not isinstance(model_tester, ModelTester):
            logging.error("model_tester must be an instance of ModelTester.")
            raise TypeError("model_tester must be instance of ModelTester")

        try:
            logging.debug("Compiling model with ttnn backend.")
            # verify --export_code has valid option
            export_code_opt = request.config.getoption("--export_code")
            if export_code_opt is not None:
                assert export_code_opt in export_code.export_code_options

            total_num_iterations = int(request.config.getoption("--report_nth_iteration"))
            native_integration = request.config.getoption("--native_integration")

            # load_params_once conflicts with native integration
            # It can be disabled via command line option or fixture
            load_params_once_default = not native_integration
            disable_via_cli = request.config.getoption("--disable_load_params_once")
            disable_via_fixture = "disable_load_params_once" in request.fixturenames
            load_params_once = load_params_once_default and not (disable_via_cli or disable_via_fixture)

            option = torch_ttnn.TorchTtnnOption(
                device=device,
                gen_graphviz=False,
                run_mem_analysis=False,
                metrics_path=model_name,
                verbose=True,
                export_code=export_code_opt,
                total_num_iterations=total_num_iterations,
                data_parallel=request.config.getoption("--data_parallel"),
                load_params_once=load_params_once,
                native_integration=native_integration,
            )

            if option.native_integration and option.data_parallel:
                logging.error("Native integration is not supported with data parallel.")
                raise ValueError("Native integration is not supported with data parallel.")

            # Move model and inputs to ttnn device
            if option.native_integration:
                from torch_ttnn.cpp_extension import ttnn_module

                torch_device = ttnn_module.as_torch_device(option.device)
                start = time.perf_counter() * 1000
                model_tester.model = model_tester.model.to(torch_device)
                model_tester.inputs = model_tester.inputs.to(torch_device)
                end = time.perf_counter() * 1000
                logging.info(f"Model and inputs moved to ttnn device in {end - start} ms.")

            warm_run_times = []
            for idx in range(total_num_iterations):
                start = time.perf_counter() * 1000
                # Don't need to reset options if inputs don't change because of cache
                outputs_after = model_tester.test_model(as_ttnn=True, option=option)
                end = time.perf_counter() * 1000
                run_time = end - start
                if idx == 0:
                    first_iter_runtime = run_time
                if idx > 1:
                    warm_run_times.append(run_time)
                logging.info(f"Iteration {idx}: {run_time} ms")

            # set avg_run_time to average, or last run_time if we only ran once or twice
            if len(warm_run_times) > 0:
                avg_run_time = sum(warm_run_times) / len(warm_run_times)
            else:
                avg_run_time = run_time

            # Move model and inputs back to CPU
            if option.native_integration:
                model_tester.model = model_tester.model.to("cpu")
                model_tester.inputs = model_tester.inputs.to("cpu")

            comp_runtime_metrics["success"] = True
            comp_runtime_metrics["avg_run_time"] = round(avg_run_time, 2)
            comp_runtime_metrics["run_time"] = round(run_time, 2)
            comp_runtime_metrics["run_time_first_iter"] = round(first_iter_runtime, 2)
            comp_runtime_metrics["has_aten"] = None
            comp_runtime_metrics["batch_size"] = model_tester.batch_size

            logging.info(f"Compilation and run successful in {comp_runtime_metrics['run_time']} ms.")

            if export_code_opt:
                export_code.export_code(option)

            if model_name not in ["speecht5-tts", "ssd300_vgg16", "retinanet_resnet50_fpn_v2"]:
                accuracy = calculate_accuracy(outputs, outputs_after)
                if accuracy:
                    comp_runtime_metrics["accuracy"] = accuracy
                    logging.info(f"Accuracy calculated: {accuracy}.")

            metrics.save_pickle(
                [x.dict() for x in option.compiled_schema_list],
                option.metrics_path,
                "compiled-schema_list",
            )
            comp_runtime_metrics["has_aten"] = False
            for g in option._out_fx_graphs:
                nodes = list(g.nodes)
                if any(["aten." in str(node.target) for node in nodes]):
                    comp_runtime_metrics["has_aten"] = True
                    break
        except Exception as e:
            logging.error("Compilation failed.", exc_info=True)

            comp_runtime_metrics["success"] = False
            comp_runtime_metrics["fits_in_memory"] = "N/A"
            comp_runtime_metrics["peak_sram_usage"] = 0

            try:
                logging.debug("Attempting rerun with bypass option to collect aten op metrics.")
                torch._dynamo.reset()
                option.bypass_compile = True
                option.reset_containers()
                model_tester.test_model(as_ttnn=True, option=option)
                end_ts = datetime.datetime.now(datetime.timezone.utc)
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
                [x.dict_for_pickle() for x in option.original_schema_list],
                option.metrics_path,
                "original-schema_list",
            )
            compiled_metrics_path = p / "compiled-run_time_metrics.pickle"
            comp_runtime_metrics["end_ts"] = end_ts
            with open(compiled_metrics_path, "wb") as f:
                pickle.dump(comp_runtime_metrics, f)
            logging.info(f"Compiled runtime metrics saved to {compiled_metrics_path}.")

        if request.node.get_closest_marker("converted_end_to_end") and comp_runtime_metrics.get("has_aten"):
            raise TypeError(f"{model_name} - Marked as converted end-to-end but still contains aten ops.")


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
