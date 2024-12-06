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
        return torch.ops.aten.hardtanh.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.hardtanh.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 32, 112, 112]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 64, 112, 112]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 14, 56, 56]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 24, 56, 56]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 40, 56, 56]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 68, 56, 56]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 128, 56, 56]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 16, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 28, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 46, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 78, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 134, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 256, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 20, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 34, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 58, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 98, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 168, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 320, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 40, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 68, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 116, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 196, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 334, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 640, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 160, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 272, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 462, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1024, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 256, 10, 10]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 256, 5, 5]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 512, 5, 5]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 128, 5, 5]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 128, 3, 3]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 256, 3, 3]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 128, 2, 2]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 256, 2, 2]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 64, 2, 2]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 64, 1, 1]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 128, 1, 1]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 672, 20, 20]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 480, 10, 10]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 96, 112, 112]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 96, 56, 56]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 56, 56]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 192, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 192, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 384, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 576, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 576, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1280, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 64, 56, 56]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 128, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 256, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 512, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 512, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 240, 28, 28]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 240, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 672, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1152, 7, 7]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 32, 120, 120]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 96, 120, 120]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 96, 60, 60]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 60, 60]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 30, 30]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 240, 30, 30]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 240, 15, 15]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 480, 15, 15]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 672, 15, 15]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 672, 8, 8]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1152, 8, 8]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1280, 8, 8]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 32, 130, 130]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 96, 130, 130]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 96, 65, 65]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 65, 65]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 33, 33]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 288, 33, 33]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 288, 17, 17]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 528, 17, 17]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 720, 17, 17]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 720, 9, 9]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1248, 9, 9]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1280, 9, 9]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 32, 150, 150]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 150, 150]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 75, 75]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 192, 75, 75]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 192, 38, 38]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 288, 38, 38]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 288, 19, 19]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 576, 19, 19]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 816, 19, 19]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 816, 10, 10]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1392, 10, 10]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1280, 10, 10]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 32, 190, 190]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 190, 190]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 144, 95, 95]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 192, 95, 95]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 192, 48, 48]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 336, 48, 48]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 336, 24, 24]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 672, 24, 24]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 960, 24, 24]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 960, 12, 12]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1632, 12, 12]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
        ["Tensor<[1, 1280, 12, 12]> self = ?", "number min_val = 0.0", "number max_val = 6.0"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.hardtanh.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.hardtanh.default", input_strings
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
