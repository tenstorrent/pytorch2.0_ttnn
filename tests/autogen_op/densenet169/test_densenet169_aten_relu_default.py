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
        return torch.ops.aten.relu.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/densenet169", "aten.relu.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 64, 112, 112]> self = ?"],
        ["Tensor<[1, 64, 56, 56]> self = ?"],
        ["Tensor<[1, 128, 56, 56]> self = ?"],
        ["Tensor<[1, 96, 56, 56]> self = ?"],
        ["Tensor<[1, 160, 56, 56]> self = ?"],
        ["Tensor<[1, 192, 56, 56]> self = ?"],
        ["Tensor<[1, 224, 56, 56]> self = ?"],
        ["Tensor<[1, 256, 56, 56]> self = ?"],
        ["Tensor<[1, 128, 28, 28]> self = ?"],
        ["Tensor<[1, 160, 28, 28]> self = ?"],
        ["Tensor<[1, 192, 28, 28]> self = ?"],
        ["Tensor<[1, 224, 28, 28]> self = ?"],
        ["Tensor<[1, 256, 28, 28]> self = ?"],
        ["Tensor<[1, 288, 28, 28]> self = ?"],
        ["Tensor<[1, 320, 28, 28]> self = ?"],
        ["Tensor<[1, 352, 28, 28]> self = ?"],
        ["Tensor<[1, 384, 28, 28]> self = ?"],
        ["Tensor<[1, 416, 28, 28]> self = ?"],
        ["Tensor<[1, 448, 28, 28]> self = ?"],
        ["Tensor<[1, 480, 28, 28]> self = ?"],
        ["Tensor<[1, 512, 28, 28]> self = ?"],
        ["Tensor<[1, 256, 14, 14]> self = ?"],
        ["Tensor<[1, 128, 14, 14]> self = ?"],
        ["Tensor<[1, 288, 14, 14]> self = ?"],
        ["Tensor<[1, 320, 14, 14]> self = ?"],
        ["Tensor<[1, 352, 14, 14]> self = ?"],
        ["Tensor<[1, 384, 14, 14]> self = ?"],
        ["Tensor<[1, 416, 14, 14]> self = ?"],
        ["Tensor<[1, 448, 14, 14]> self = ?"],
        ["Tensor<[1, 480, 14, 14]> self = ?"],
        ["Tensor<[1, 512, 14, 14]> self = ?"],
        ["Tensor<[1, 544, 14, 14]> self = ?"],
        ["Tensor<[1, 576, 14, 14]> self = ?"],
        ["Tensor<[1, 608, 14, 14]> self = ?"],
        ["Tensor<[1, 640, 14, 14]> self = ?"],
        ["Tensor<[1, 672, 14, 14]> self = ?"],
        ["Tensor<[1, 704, 14, 14]> self = ?"],
        ["Tensor<[1, 736, 14, 14]> self = ?"],
        ["Tensor<[1, 768, 14, 14]> self = ?"],
        ["Tensor<[1, 800, 14, 14]> self = ?"],
        ["Tensor<[1, 832, 14, 14]> self = ?"],
        ["Tensor<[1, 864, 14, 14]> self = ?"],
        ["Tensor<[1, 896, 14, 14]> self = ?"],
        ["Tensor<[1, 928, 14, 14]> self = ?"],
        ["Tensor<[1, 960, 14, 14]> self = ?"],
        ["Tensor<[1, 992, 14, 14]> self = ?"],
        ["Tensor<[1, 1024, 14, 14]> self = ?"],
        ["Tensor<[1, 1056, 14, 14]> self = ?"],
        ["Tensor<[1, 1088, 14, 14]> self = ?"],
        ["Tensor<[1, 1120, 14, 14]> self = ?"],
        ["Tensor<[1, 1152, 14, 14]> self = ?"],
        ["Tensor<[1, 1184, 14, 14]> self = ?"],
        ["Tensor<[1, 1216, 14, 14]> self = ?"],
        ["Tensor<[1, 1248, 14, 14]> self = ?"],
        ["Tensor<[1, 1280, 14, 14]> self = ?"],
        ["Tensor<[1, 640, 7, 7]> self = ?"],
        ["Tensor<[1, 128, 7, 7]> self = ?"],
        ["Tensor<[1, 672, 7, 7]> self = ?"],
        ["Tensor<[1, 704, 7, 7]> self = ?"],
        ["Tensor<[1, 736, 7, 7]> self = ?"],
        ["Tensor<[1, 768, 7, 7]> self = ?"],
        ["Tensor<[1, 800, 7, 7]> self = ?"],
        ["Tensor<[1, 832, 7, 7]> self = ?"],
        ["Tensor<[1, 864, 7, 7]> self = ?"],
        ["Tensor<[1, 896, 7, 7]> self = ?"],
        ["Tensor<[1, 928, 7, 7]> self = ?"],
        ["Tensor<[1, 960, 7, 7]> self = ?"],
        ["Tensor<[1, 992, 7, 7]> self = ?"],
        ["Tensor<[1, 1024, 7, 7]> self = ?"],
        ["Tensor<[1, 1056, 7, 7]> self = ?"],
        ["Tensor<[1, 1088, 7, 7]> self = ?"],
        ["Tensor<[1, 1120, 7, 7]> self = ?"],
        ["Tensor<[1, 1152, 7, 7]> self = ?"],
        ["Tensor<[1, 1184, 7, 7]> self = ?"],
        ["Tensor<[1, 1216, 7, 7]> self = ?"],
        ["Tensor<[1, 1248, 7, 7]> self = ?"],
        ["Tensor<[1, 1280, 7, 7]> self = ?"],
        ["Tensor<[1, 1312, 7, 7]> self = ?"],
        ["Tensor<[1, 1344, 7, 7]> self = ?"],
        ["Tensor<[1, 1376, 7, 7]> self = ?"],
        ["Tensor<[1, 1408, 7, 7]> self = ?"],
        ["Tensor<[1, 1440, 7, 7]> self = ?"],
        ["Tensor<[1, 1472, 7, 7]> self = ?"],
        ["Tensor<[1, 1504, 7, 7]> self = ?"],
        ["Tensor<[1, 1536, 7, 7]> self = ?"],
        ["Tensor<[1, 1568, 7, 7]> self = ?"],
        ["Tensor<[1, 1600, 7, 7]> self = ?"],
        ["Tensor<[1, 1632, 7, 7]> self = ?"],
        ["Tensor<[1, 1664, 7, 7]> self = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.relu.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.relu.default", input_strings
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
            assert metric["accuracy"] >= 0.99
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
