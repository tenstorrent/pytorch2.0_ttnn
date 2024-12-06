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
    save_pickle(metrics, "metrics-autogen-op/HardNet-train", "aten.slice.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 782, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 160"],
        ["Tensor<[1, 782, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 160", "Optional[int] end = 320"],
        ["Tensor<[1, 782, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 320", "Optional[int] end = 782"],
        ["Tensor<[1, 1072, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 160"],
        ["Tensor<[1, 1072, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 160", "Optional[int] end = 432"],
        ["Tensor<[1, 1072, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 432", "Optional[int] end = 1072"],
        ["Tensor<[1, 800, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 160"],
        ["Tensor<[1, 800, 7, 7]> self = ?", "int dim = 1", "Optional[int] start = 160", "Optional[int] end = 800"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 80"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 80", "Optional[int] end = 120"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 120", "Optional[int] end = 160"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 160", "Optional[int] end = 200"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 200", "Optional[int] end = 240"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 240", "Optional[int] end = 280"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 280", "Optional[int] end = 320"],
        ["Tensor<[1, 654, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 320", "Optional[int] end = 654"],
        ["Tensor<[1, 740, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 740, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 108"],
        ["Tensor<[1, 740, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 108", "Optional[int] end = 224"],
        ["Tensor<[1, 740, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 224", "Optional[int] end = 420"],
        ["Tensor<[1, 740, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 420", "Optional[int] end = 740"],
        ["Tensor<[1, 156, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 156, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 156"],
        ["Tensor<[1, 304, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 304, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 108"],
        ["Tensor<[1, 304, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 108", "Optional[int] end = 304"],
        ["Tensor<[1, 236, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 236, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 236"],
        ["Tensor<[1, 544, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 544, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 108"],
        ["Tensor<[1, 544, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 108", "Optional[int] end = 224"],
        ["Tensor<[1, 544, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 224", "Optional[int] end = 544"],
        ["Tensor<[1, 428, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 428, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 108"],
        ["Tensor<[1, 428, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 108", "Optional[int] end = 428"],
        ["Tensor<[1, 360, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 40"],
        ["Tensor<[1, 360, 14, 14]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 360"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 40"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 40", "Optional[int] end = 60"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 60", "Optional[int] end = 80"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 80", "Optional[int] end = 100"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 100", "Optional[int] end = 120"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 120", "Optional[int] end = 140"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 140", "Optional[int] end = 160"],
        ["Tensor<[1, 328, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 160", "Optional[int] end = 328"],
        ["Tensor<[1, 466, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 466, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 54"],
        ["Tensor<[1, 466, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 54", "Optional[int] end = 112"],
        ["Tensor<[1, 466, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 112", "Optional[int] end = 210"],
        ["Tensor<[1, 466, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 210", "Optional[int] end = 466"],
        ["Tensor<[1, 78, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 78, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 78"],
        ["Tensor<[1, 152, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 152, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 54"],
        ["Tensor<[1, 152, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 54", "Optional[int] end = 152"],
        ["Tensor<[1, 118, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 118, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 118"],
        ["Tensor<[1, 368, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 368, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 54"],
        ["Tensor<[1, 368, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 54", "Optional[int] end = 112"],
        ["Tensor<[1, 368, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 112", "Optional[int] end = 368"],
        ["Tensor<[1, 310, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 310, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 54"],
        ["Tensor<[1, 310, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 54", "Optional[int] end = 310"],
        ["Tensor<[1, 276, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 20"],
        ["Tensor<[1, 276, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 20", "Optional[int] end = 276"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 16"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 16", "Optional[int] end = 32"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 32", "Optional[int] end = 48"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 48", "Optional[int] end = 64"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 64", "Optional[int] end = 80"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 80", "Optional[int] end = 96"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 96", "Optional[int] end = 112"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 112", "Optional[int] end = 128"],
        ["Tensor<[1, 262, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 128", "Optional[int] end = 262"],
        ["Tensor<[1, 296, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 16"],
        ["Tensor<[1, 296, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 16", "Optional[int] end = 44"],
        ["Tensor<[1, 296, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 44", "Optional[int] end = 90"],
        ["Tensor<[1, 296, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 90", "Optional[int] end = 168"],
        ["Tensor<[1, 296, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 168", "Optional[int] end = 296"],
        ["Tensor<[1, 62, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 16"],
        ["Tensor<[1, 62, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 16", "Optional[int] end = 62"],
        ["Tensor<[1, 122, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 16"],
        ["Tensor<[1, 122, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 16", "Optional[int] end = 44"],
        ["Tensor<[1, 122, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 44", "Optional[int] end = 122"],
        ["Tensor<[1, 94, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 16"],
        ["Tensor<[1, 94, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 16", "Optional[int] end = 94"],
        ["Tensor<[1, 218, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 16"],
        ["Tensor<[1, 218, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 16", "Optional[int] end = 44"],
        ["Tensor<[1, 218, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 44", "Optional[int] end = 90"],
        ["Tensor<[1, 218, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 90", "Optional[int] end = 218"],
        ["Tensor<[1, 172, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 16"],
        ["Tensor<[1, 172, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 16", "Optional[int] end = 44"],
        ["Tensor<[1, 172, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 44", "Optional[int] end = 172"],
        ["Tensor<[1, 144, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 16"],
        ["Tensor<[1, 144, 28, 28]> self = ?", "int dim = 1", "Optional[int] start = 16", "Optional[int] end = 144"],
        ["Tensor<[1, 124, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 14"],
        ["Tensor<[1, 124, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 14", "Optional[int] end = 28"],
        ["Tensor<[1, 124, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 28", "Optional[int] end = 42"],
        ["Tensor<[1, 124, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 42", "Optional[int] end = 56"],
        ["Tensor<[1, 124, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 56", "Optional[int] end = 124"],
        ["Tensor<[1, 142, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 14"],
        ["Tensor<[1, 142, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 14", "Optional[int] end = 38"],
        ["Tensor<[1, 142, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 38", "Optional[int] end = 78"],
        ["Tensor<[1, 142, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 78", "Optional[int] end = 142"],
        ["Tensor<[1, 54, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 14"],
        ["Tensor<[1, 54, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 14", "Optional[int] end = 54"],
        ["Tensor<[1, 102, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 14"],
        ["Tensor<[1, 102, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 14", "Optional[int] end = 38"],
        ["Tensor<[1, 102, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 38", "Optional[int] end = 102"],
        ["Tensor<[1, 78, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 14"],
        ["Tensor<[1, 78, 56, 56]> self = ?", "int dim = 1", "Optional[int] start = 14", "Optional[int] end = 78"],
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
