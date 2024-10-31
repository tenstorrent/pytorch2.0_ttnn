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
        return torch.ops.aten.avg_pool2d_backward.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.avg_pool2d_backward.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 160, 3, 3]> grad_output = ?",
            "Tensor<[1, 160, 7, 7]> self = ?",
            "List[int] kernel_size = [2, 2]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "bool ceil_mode = False",
            "bool count_include_pad = True",
            "Optional[int] divisor_override = ?",
        ],
        [
            "Tensor<[1, 112, 7, 7]> grad_output = ?",
            "Tensor<[1, 112, 14, 14]> self = ?",
            "List[int] kernel_size = [2, 2]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "bool ceil_mode = False",
            "bool count_include_pad = True",
            "Optional[int] divisor_override = ?",
        ],
        [
            "Tensor<[1, 80, 7, 7]> grad_output = ?",
            "Tensor<[1, 80, 14, 14]> self = ?",
            "List[int] kernel_size = [2, 2]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "bool ceil_mode = False",
            "bool count_include_pad = True",
            "Optional[int] divisor_override = ?",
        ],
        [
            "Tensor<[1, 40, 14, 14]> grad_output = ?",
            "Tensor<[1, 40, 28, 28]> self = ?",
            "List[int] kernel_size = [2, 2]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "bool ceil_mode = False",
            "bool count_include_pad = True",
            "Optional[int] divisor_override = ?",
        ],
        [
            "Tensor<[1, 24, 28, 28]> grad_output = ?",
            "Tensor<[1, 24, 56, 56]> self = ?",
            "List[int] kernel_size = [2, 2]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "bool ceil_mode = False",
            "bool count_include_pad = True",
            "Optional[int] divisor_override = ?",
        ],
        [
            "Tensor<[1, 1536, 8, 8]> grad_output = ?",
            "Tensor<[1, 1536, 8, 8]> self = ?",
            "List[int] kernel_size = [3, 3]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "bool ceil_mode = False",
            "bool count_include_pad = False",
            "Optional[int] divisor_override = ?",
        ],
        [
            "Tensor<[1, 1024, 17, 17]> grad_output = ?",
            "Tensor<[1, 1024, 17, 17]> self = ?",
            "List[int] kernel_size = [3, 3]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "bool ceil_mode = False",
            "bool count_include_pad = False",
            "Optional[int] divisor_override = ?",
        ],
        [
            "Tensor<[1, 384, 35, 35]> grad_output = ?",
            "Tensor<[1, 384, 35, 35]> self = ?",
            "List[int] kernel_size = [3, 3]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "bool ceil_mode = False",
            "bool count_include_pad = False",
            "Optional[int] divisor_override = ?",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.avg_pool2d_backward.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.avg_pool2d_backward.default", input_strings
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
