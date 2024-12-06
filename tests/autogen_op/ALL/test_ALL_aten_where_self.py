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
        return torch.ops.aten.where.self(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.where.self")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[15, 15]> condition = ?", "Tensor<[15, 15]> self = ?", "Tensor<[15, 15]> other = ?"],
        ["Tensor<[1, 1]> condition = ?", "Tensor<[1, 1]> self = ?", "Tensor<[1, 1]> other = ?"],
        ["Tensor<[2, 2]> condition = ?", "Tensor<[2, 2]> self = ?", "Tensor<[2, 2]> other = ?"],
        [
            "Tensor<[s0 + 1, s0 + 1]> condition = ?",
            "Tensor<[s0 + 1, s0 + 1]> self = ?",
            "Tensor<[s0 + 1, s0 + 1]> other = ?",
        ],
        ["Tensor<[17, 17]> condition = ?", "Tensor<[17, 17]> self = ?", "Tensor<[17, 17]> other = ?"],
        ["Tensor<[1, 1, 7, 7]> condition = ?", "Tensor<[1, 12, 7, 7]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 1, 45, 45]> condition = ?", "Tensor<[1, 12, 45, 45]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 1, 1, 46]> condition = ?", "Tensor<[1, 12, 1, 46]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 1, 1, s10 + 1]> condition = ?", "Tensor<[1, 12, 1, s10 + 1]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 1, 5, 5]> condition = ?", "Tensor<[1, 16, 5, 5]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 1, 1, 6]> condition = ?", "Tensor<[1, 16, 1, 6]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 1, 1, s10 + 1]> condition = ?", "Tensor<[1, 16, 1, s10 + 1]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[10, 10]> condition = ?", "Tensor<[10, 10]> self = ?", "Tensor<[10, 10]> other = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.where.self",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.where.self", input_strings)
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
