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
        return torch.ops.aten.native_group_norm.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.native_group_norm.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 320, 64, 64]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "int N = 1",
            "int C = 320",
            "int HxW = 4096",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 320, 64, 64]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "int N = 1",
            "int C = 320",
            "int HxW = 4096",
            "int group = 32",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 320, s0, s1]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "int N = 1",
            "int C = 320",
            "int<s0*s1> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 640, s0, s1]> input = ?",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> bias = ?",
            "int N = 1",
            "int C = 640",
            "int<s0*s1> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 640, s0, s1]> input = ?",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> bias = ?",
            "int N = 1",
            "int C = 640",
            "int<s0*s1> HxW = ?",
            "int group = 32",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 640, s1, s2]> input = ?",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> bias = ?",
            "int N = 1",
            "int C = 640",
            "int<s1*s2> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1280, s1, s2]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "int N = 1",
            "int C = 1280",
            "int<s1*s2> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1280, s1, s2]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "int N = 1",
            "int C = 1280",
            "int<s1*s2> HxW = ?",
            "int group = 32",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 1280, s0, s1]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "int N = 1",
            "int C = 1280",
            "int<s0*s1> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1280, s0, s1]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "int N = 1",
            "int C = 1280",
            "int<s0*s1> HxW = ?",
            "int group = 32",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 2560, 8, 8]> input = ?",
            "Optional[Tensor]<[2560]> weight = ?",
            "Optional[Tensor]<[2560]> bias = ?",
            "int N = 1",
            "int C = 2560",
            "int HxW = 64",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1280, 8, 8]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "int N = 1",
            "int C = 1280",
            "int HxW = 64",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2560, s0, s1]> input = ?",
            "Optional[Tensor]<[2560]> weight = ?",
            "Optional[Tensor]<[2560]> bias = ?",
            "int N = 1",
            "int C = 2560",
            "int<s0*s1> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1920, s1, s2]> input = ?",
            "Optional[Tensor]<[1920]> weight = ?",
            "Optional[Tensor]<[1920]> bias = ?",
            "int N = 1",
            "int C = 1920",
            "int<s1*s2> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 640, s1, s2]> input = ?",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> bias = ?",
            "int N = 1",
            "int C = 640",
            "int<s1*s2> HxW = ?",
            "int group = 32",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 960, s1, s2]> input = ?",
            "Optional[Tensor]<[960]> weight = ?",
            "Optional[Tensor]<[960]> bias = ?",
            "int N = 1",
            "int C = 960",
            "int<s1*s2> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 320, s1, s2]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "int N = 1",
            "int C = 320",
            "int<s1*s2> HxW = ?",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 320, s1, s2]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "int N = 1",
            "int C = 320",
            "int<s1*s2> HxW = ?",
            "int group = 32",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 256, 100, 136]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "int N = 1",
            "int C = 256",
            "int HxW = 13600",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 50, 68]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "int N = 1",
            "int C = 256",
            "int HxW = 3400",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 25, 34]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "int N = 1",
            "int C = 256",
            "int HxW = 850",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 13, 17]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "int N = 1",
            "int C = 256",
            "int HxW = 221",
            "int group = 32",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 7, 9]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "int N = 1",
            "int C = 256",
            "int HxW = 63",
            "int group = 32",
            "float eps = 1e-05",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.native_group_norm.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.native_group_norm.default", input_strings
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
            metric["accuracy"] = calculate_accuracy(result_before, result_after)
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        try:
            # Check the graph has be rewritten and contain ttnn ops
            nodes = list(option._out_fx_graphs[0].nodes)
            if not any(["aten." in str(node.target) for node in nodes]):
                metric["convert_to_ttnn"] = True
            else:
                metric["convert_to_ttnn"] = False
        except Exception as e:
            print(f"Failed to check the graph has ttnn op. Raised exception: {e}")

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] >= 0.99
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
