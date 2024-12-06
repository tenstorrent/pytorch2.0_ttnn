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
        return torch.ops.aten.add.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/t5-base", "aten.add.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 10, 1]> self = ?", "Tensor other = 1e-06"],
        ["Tensor<[10, 10]> self = ?", "Tensor other = 0"],
        ["Tensor<[10, 10]> self = ?", "Tensor other = 8"],
        ["Tensor<[10, 10]> self = ?", "Tensor<[10, 10]> other = ?"],
        ["Tensor<[1, 12, 10, 10]> self = ?", "Tensor<[1, 1, 1, 10]> other = ?"],
        ["Tensor<[1, 12, 10, 10]> self = ?", "Tensor<[1, 12, 10, 10]> other = ?"],
        ["Tensor<[1, 10, 768]> self = ?", "Tensor<[1, 10, 768]> other = ?"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 1e-06"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 16"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 0"],
        ["Tensor<[1, 12, 1, 1]> self = ?", "Tensor<[1, 1, 1, 1]> other = ?"],
        ["Tensor<[1, 12, 1, 1]> self = ?", "Tensor<[1, 12, 1, 1]> other = ?"],
        ["Tensor<[1, 1, 768]> self = ?", "Tensor<[1, 1, 768]> other = ?"],
        ["Tensor<[1, 12, 1, 10]> self = ?", "Tensor<[1, 1, 1, 10]> other = ?"],
        ["Tensor<[1, 12, 1, 10]> self = ?", "Tensor<[1, 12, 1, 10]> other = ?"],
        ["Tensor<[2, 2]> self = ?", "Tensor other = 16"],
        ["Tensor<[2, 2]> self = ?", "Tensor other = 0"],
        ["Tensor<[1, 12, 1, 2]> self = ?", "Tensor<[1, 1, 1, 2]> other = ?"],
        ["Tensor<[1, 12, 1, 2]> self = ?", "Tensor<[1, 12, 1, 2]> other = ?"],
        ["Tensor<[s0 + 1, s0 + 1]> self = ?", "Tensor other = 16"],
        ["Tensor<[s0 + 1, s0 + 1]> self = ?", "Tensor other = 0"],
        ["Tensor<[1, 12, 1, s0 + 1]> self = ?", "Tensor<[1, 1, 1, s0 + 1]> other = ?"],
        ["Tensor<[1, 12, 1, s0 + 1]> self = ?", "Tensor<[1, 12, 1, s0 + 1]> other = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.add.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.add.Tensor", input_strings)
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
