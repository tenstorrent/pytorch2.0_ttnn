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
        return torch.ops.aten._unsafe_view.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/swin_v2_t", "aten._unsafe_view.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] size = [64, 64, 96]"],
        ["Tensor<[64, 3, 64, 32]> self = ?", "List[int] size = [192, 64, 32]"],
        ["Tensor<[64, 3, 32, 64]> self = ?", "List[int] size = [192, 32, 64]"],
        ["Tensor<[64, 64, 3, 32]> self = ?", "List[int] size = [64, 64, 96]"],
        ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] size = [1, 64, 64, 96]"],
        ["Tensor<[8, 8, 8, 8]> self = ?", "List[int] size = [64, 64]"],
        ["Tensor<[1, 4, 4, 8, 8, 192]> self = ?", "List[int] size = [16, 64, 192]"],
        ["Tensor<[16, 6, 64, 32]> self = ?", "List[int] size = [96, 64, 32]"],
        ["Tensor<[16, 6, 32, 64]> self = ?", "List[int] size = [96, 32, 64]"],
        ["Tensor<[16, 64, 6, 32]> self = ?", "List[int] size = [16, 64, 192]"],
        ["Tensor<[1, 4, 8, 4, 8, 192]> self = ?", "List[int] size = [1, 32, 32, 192]"],
        ["Tensor<[4, 4, 8, 8]> self = ?", "List[int] size = [16, 64]"],
        ["Tensor<[1, 2, 2, 8, 8, 384]> self = ?", "List[int] size = [4, 64, 384]"],
        ["Tensor<[4, 12, 64, 32]> self = ?", "List[int] size = [48, 64, 32]"],
        ["Tensor<[4, 12, 32, 64]> self = ?", "List[int] size = [48, 32, 64]"],
        ["Tensor<[4, 64, 12, 32]> self = ?", "List[int] size = [4, 64, 384]"],
        ["Tensor<[1, 2, 8, 2, 8, 384]> self = ?", "List[int] size = [1, 16, 16, 384]"],
        ["Tensor<[2, 2, 8, 8]> self = ?", "List[int] size = [4, 64]"],
        ["Tensor<[1, 64, 24, 32]> self = ?", "List[int] size = [1, 64, 768]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._unsafe_view.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._unsafe_view.default", input_strings
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
