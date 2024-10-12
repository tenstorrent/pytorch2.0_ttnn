import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, get_input_vals_from_metric_str


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
    save_pickle(metrics, "metrics-input-variations/model-tests-metrics-group-17/googlenet eval", "aten.relu.default")


@pytest.mark.parametrize("input_strings", [['Tensor<[1, 64, 112, 112]> self = ?'], ['Tensor<[1, 64, 56, 56]> self = ?'], ['Tensor<[1, 192, 56, 56]> self = ?'], ['Tensor<[1, 64, 28, 28]> self = ?'], ['Tensor<[1, 96, 28, 28]> self = ?'], ['Tensor<[1, 128, 28, 28]> self = ?'], ['Tensor<[1, 16, 28, 28]> self = ?'], ['Tensor<[1, 32, 28, 28]> self = ?'], ['Tensor<[1, 192, 28, 28]> self = ?'], ['Tensor<[1, 192, 14, 14]> self = ?'], ['Tensor<[1, 96, 14, 14]> self = ?'], ['Tensor<[1, 208, 14, 14]> self = ?'], ['Tensor<[1, 16, 14, 14]> self = ?'], ['Tensor<[1, 48, 14, 14]> self = ?'], ['Tensor<[1, 64, 14, 14]> self = ?'], ['Tensor<[1, 160, 14, 14]> self = ?'], ['Tensor<[1, 112, 14, 14]> self = ?'], ['Tensor<[1, 224, 14, 14]> self = ?'], ['Tensor<[1, 24, 14, 14]> self = ?'], ['Tensor<[1, 128, 14, 14]> self = ?'], ['Tensor<[1, 256, 14, 14]> self = ?'], ['Tensor<[1, 144, 14, 14]> self = ?'], ['Tensor<[1, 288, 14, 14]> self = ?'], ['Tensor<[1, 32, 14, 14]> self = ?'], ['Tensor<[1, 320, 14, 14]> self = ?'], ['Tensor<[1, 256, 7, 7]> self = ?'], ['Tensor<[1, 160, 7, 7]> self = ?'], ['Tensor<[1, 320, 7, 7]> self = ?'], ['Tensor<[1, 32, 7, 7]> self = ?'], ['Tensor<[1, 128, 7, 7]> self = ?'], ['Tensor<[1, 384, 7, 7]> self = ?'], ['Tensor<[1, 192, 7, 7]> self = ?'], ['Tensor<[1, 48, 7, 7]> self = ?']])
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
            "opname": "aten.relu.default",
            "input_strings": input_strings,
            "native_run": False,
            "run": False,
            "accuracy": False,
            "convert_to_ttnn": False,
        }
    m = AtenModule()
    input_args, input_kwargs = get_input_vals_from_metric_str("aten.relu.default", input_strings)
    if input_args is None and input_kwargs is None:
        pytest.skip("Invalid input strings:" + str(input_strings))
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
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

    if metric["run"] == True:
        # Check inference result
        accuracy = calculate_accuracy(result_before, result_after)
        if accuracy >= 0.99:
            metric["accuracy"] = True

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        if any(["ttnn" in str(node) for node in nodes]):
            metric["convert_to_ttnn"] = True

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] == True
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True