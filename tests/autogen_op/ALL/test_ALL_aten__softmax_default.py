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
        return torch.ops.aten._softmax.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten._softmax.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 16, 256, 256]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 32, 32]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[12, 50, 50]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 7, 7]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[8, 920, 920]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[8, 100, 100]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[8, 100, 920]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 25, 25]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 6, 15, 15]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 6, 1, 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 6, 1, 15]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 6, 1, 2]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 6, 1, s0 + 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 6, 1, 17]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 1, 19200, 300]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 2, 4800, 300]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 5, 1200, 300]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 300, 300]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 7, 7]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 45, 45]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 1, 46]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 1, s10 + 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 59, 59]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 1, 60]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 1, s10 + 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 256, 2048]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 256, 256]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 2048, 256]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 10, 10]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 1, 16384, 256]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 2, 4096, 256]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 5, 1024, 256]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 19, 19]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 3, 1445, 1445]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 9, 9]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 12, 12]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 9, 9]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 64, 9, 9]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 5, 5]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 1, 6]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 1, s10 + 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 16, 16]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 197, 197]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 197, 197]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[12, 24, 24]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[64, 4, 49, 49]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 8, 49, 49]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[4, 16, 49, 49]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 32, 49, 49]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[64, 3, 49, 49]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 6, 49, 49]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[4, 12, 49, 49]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 24, 49, 49]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[64, 4, 64, 64]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 8, 64, 64]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[4, 16, 64, 64]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 32, 64, 64]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[64, 3, 64, 64]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 6, 64, 64]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[4, 12, 64, 64]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 24, 64, 64]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 1, 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 1, 10]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 1, 2]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 1, s0 + 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 10, 10]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 1, 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 1, 10]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 1, 2]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 16, 1, s0 + 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 10, 10]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 1, 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 1, 10]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 1, 2]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 8, 1, s0 + 1]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[1, 12, 14, 14]> self = ?", "int dim = -1", "bool half_to_float = False"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._softmax.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._softmax.default", input_strings
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
