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
        return torch.ops.aten.slice.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ghostnetv2_100.in1k-train", "aten.slice.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 16, 112, 112]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 16, 112, 112]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 16, 112, 112]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 48, 112, 112]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 48, 112, 112]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 48, 112, 112]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 24, 56, 56]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 24, 56, 56]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 24, 56, 56]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 72, 56, 56]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 72, 56, 56]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 72, 56, 56]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 40, 28, 28]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 40, 28, 28]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 40, 28, 28]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 120, 28, 28]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 120, 28, 28]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 120, 28, 28]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 240, 28, 28]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 240, 28, 28]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 240, 28, 28]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 80, 14, 14]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 80, 14, 14]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 80, 14, 14]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 200, 14, 14]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 200, 14, 14]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 200, 14, 14]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 184, 14, 14]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 184, 14, 14]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 184, 14, 14]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 480, 14, 14]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 480, 14, 14]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 480, 14, 14]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 112, 14, 14]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 112, 14, 14]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 112, 14, 14]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 672, 14, 14]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 672, 14, 14]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 672, 14, 14]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 160, 7, 7]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 160, 7, 7]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 160, 7, 7]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 960, 7, 7]> self = ?",
            "int dim = 0",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 960, 7, 7]> self = ?",
            "int dim = 2",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        [
            "Tensor<[1, 960, 7, 7]> self = ?",
            "int dim = 3",
            "Optional[int] start = 0",
            "Optional[int] end = 9223372036854775807",
        ],
        ["Tensor<[1, 160, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 80", "Optional[int] end = 160"],
        ["Tensor<[1, 160, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 80"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 480"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 480", "Optional[int] end = 960"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 336"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 336", "Optional[int] end = 672"],
        ["Tensor<[1, 112, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 56", "Optional[int] end = 112"],
        ["Tensor<[1, 112, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 56"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 240"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 240", "Optional[int] end = 480"],
        ["Tensor<[1, 80, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 80"],
        ["Tensor<[1, 80, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 184, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 92"],
        ["Tensor<[1, 184, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 92", "Optional[int] end = 184"],
        ["Tensor<[1, 200, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 100"],
        ["Tensor<[1, 200, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 100", "Optional[int] end = 200"],
        ["Tensor<[1, 240, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 120"],
        ["Tensor<[1, 240, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 120", "Optional[int] end = 240"],
        ["Tensor<[1, 40, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 40"],
        ["Tensor<[1, 40, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 120, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 60"],
        ["Tensor<[1, 120, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 60", "Optional[int] end = 120"],
        ["Tensor<[1, 72, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 36"],
        ["Tensor<[1, 72, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 36", "Optional[int] end = 72"],
        ["Tensor<[1, 24, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 12", "Optional[int] end = 24"],
        ["Tensor<[1, 24, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 12"],
        ["Tensor<[1, 48, 112, 112]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 24"],
        ["Tensor<[1, 48, 112, 112]> self = ?", "int dim = 1", "Optional[int] start = 24", "Optional[int] end = 48"],
        ["Tensor<[1, 16, 112, 112]> self = ?", "int dim = 1", "Optional[int] start = 8", "Optional[int] end = 16"],
        ["Tensor<[1, 16, 112, 112]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 8"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.slice.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.slice.Tensor", input_strings
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