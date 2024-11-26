import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, render_metric_string_list_to_input_args_kwargs


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.aten._native_batch_norm_legit_no_training.default(*args, **kwargs)[0]


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(
        metrics, "metrics-autogen-op/tf_efficientnet_lite1.in1k", "aten._native_batch_norm_legit_no_training.default"
    )


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 32, 120, 120]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "Tensor<[32]> running_mean = ?",
            "Tensor<[32]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 16, 120, 120]> input = ?",
            "Optional[Tensor]<[16]> weight = ?",
            "Optional[Tensor]<[16]> bias = ?",
            "Tensor<[16]> running_mean = ?",
            "Tensor<[16]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 96, 120, 120]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> bias = ?",
            "Tensor<[96]> running_mean = ?",
            "Tensor<[96]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 96, 60, 60]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> bias = ?",
            "Tensor<[96]> running_mean = ?",
            "Tensor<[96]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 24, 60, 60]> input = ?",
            "Optional[Tensor]<[24]> weight = ?",
            "Optional[Tensor]<[24]> bias = ?",
            "Tensor<[24]> running_mean = ?",
            "Tensor<[24]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 144, 60, 60]> input = ?",
            "Optional[Tensor]<[144]> weight = ?",
            "Optional[Tensor]<[144]> bias = ?",
            "Tensor<[144]> running_mean = ?",
            "Tensor<[144]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 144, 30, 30]> input = ?",
            "Optional[Tensor]<[144]> weight = ?",
            "Optional[Tensor]<[144]> bias = ?",
            "Tensor<[144]> running_mean = ?",
            "Tensor<[144]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 40, 30, 30]> input = ?",
            "Optional[Tensor]<[40]> weight = ?",
            "Optional[Tensor]<[40]> bias = ?",
            "Tensor<[40]> running_mean = ?",
            "Tensor<[40]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 240, 30, 30]> input = ?",
            "Optional[Tensor]<[240]> weight = ?",
            "Optional[Tensor]<[240]> bias = ?",
            "Tensor<[240]> running_mean = ?",
            "Tensor<[240]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 240, 15, 15]> input = ?",
            "Optional[Tensor]<[240]> weight = ?",
            "Optional[Tensor]<[240]> bias = ?",
            "Tensor<[240]> running_mean = ?",
            "Tensor<[240]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 80, 15, 15]> input = ?",
            "Optional[Tensor]<[80]> weight = ?",
            "Optional[Tensor]<[80]> bias = ?",
            "Tensor<[80]> running_mean = ?",
            "Tensor<[80]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 480, 15, 15]> input = ?",
            "Optional[Tensor]<[480]> weight = ?",
            "Optional[Tensor]<[480]> bias = ?",
            "Tensor<[480]> running_mean = ?",
            "Tensor<[480]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 112, 15, 15]> input = ?",
            "Optional[Tensor]<[112]> weight = ?",
            "Optional[Tensor]<[112]> bias = ?",
            "Tensor<[112]> running_mean = ?",
            "Tensor<[112]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 672, 15, 15]> input = ?",
            "Optional[Tensor]<[672]> weight = ?",
            "Optional[Tensor]<[672]> bias = ?",
            "Tensor<[672]> running_mean = ?",
            "Tensor<[672]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 672, 8, 8]> input = ?",
            "Optional[Tensor]<[672]> weight = ?",
            "Optional[Tensor]<[672]> bias = ?",
            "Tensor<[672]> running_mean = ?",
            "Tensor<[672]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 192, 8, 8]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "Tensor<[192]> running_mean = ?",
            "Tensor<[192]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 1152, 8, 8]> input = ?",
            "Optional[Tensor]<[1152]> weight = ?",
            "Optional[Tensor]<[1152]> bias = ?",
            "Tensor<[1152]> running_mean = ?",
            "Tensor<[1152]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 320, 8, 8]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "Tensor<[320]> running_mean = ?",
            "Tensor<[320]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 1280, 8, 8]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "Tensor<[1280]> running_mean = ?",
            "Tensor<[1280]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._native_batch_norm_legit_no_training.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._native_batch_norm_legit_no_training.default", input_strings
    )
    if status == False:
        pytest.skip("Invalid input strings")
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
        metric["native_run"] = False
    if metric["native_run"] == True:
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {e}")
            metric["run"] = False

    if metric["run"] == True:
        try:
            # Check inference result
            accuracy = calculate_accuracy(result_before, result_after)
            if accuracy >= 0.99:
                metric["accuracy"] = True
            else:
                metric["accuracy"] = False
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        try:
            # Check the graph has be rewritten and contain ttnn ops
            nodes = list(option._out_fx_graphs[0].nodes)
            if any(["ttnn" in str(node) for node in nodes]):
                metric["convert_to_ttnn"] = True
            else:
                metric["convert_to_ttnn"] = False
        except Exception as e:
            print(f"Failed to check the graph has ttnn op. Raised exception: {e}")

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] == True
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
