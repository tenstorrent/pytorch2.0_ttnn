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
        return torch.ops.aten.view.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/swin_s", "aten.view.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[2401, 3]> self = ?", "List[int] size = [49, 49, -1]"],
        ["Tensor<[1, 56, 56, 96]> self = ?", "List[int] size = [1, 8, 7, 8, 7, 96]"],
        ["Tensor<[64, 49, 96]> self = ?", "List[int] size = [3136, 96]"],
        ["Tensor<[3136, 288]> self = ?", "List[int] size = [64, 49, 288]"],
        ["Tensor<[64, 49, 288]> self = ?", "List[int] size = [64, 49, 3, 3, 32]"],
        ["Tensor<[192, 49, 49]> self = ?", "List[int] size = [64, 3, 49, 49]"],
        ["Tensor<[64, 3, 49, 49]> self = ?", "List[int] size = [192, 49, 49]"],
        ["Tensor<[192, 49, 32]> self = ?", "List[int] size = [64, 3, 49, 32]"],
        ["Tensor<[3136, 96]> self = ?", "List[int] size = [64, 49, 96]"],
        ["Tensor<[64, 49, 96]> self = ?", "List[int] size = [1, 8, 8, 7, 7, 96]"],
        ["Tensor<[1, 56, 56, 96]> self = ?", "List[int] size = [3136, 96]"],
        ["Tensor<[3136, 384]> self = ?", "List[int] size = [1, 56, 56, 384]"],
        ["Tensor<[1, 56, 56, 384]> self = ?", "List[int] size = [3136, 384]"],
        ["Tensor<[3136, 96]> self = ?", "List[int] size = [1, 56, 56, 96]"],
        ["Tensor<[56, 56]> self = ?", "List[int] size = [8, 7, 8, 7]"],
        ["Tensor<[64, 3, 49, 49]> self = ?", "List[int] size = [1, 64, 3, 49, 49]"],
        ["Tensor<[1, 64, 3, 49, 49]> self = ?", "List[int] size = [-1, 3, 49, 49]"],
        ["Tensor<[1, 28, 28, 384]> self = ?", "List[int] size = [784, 384]"],
        ["Tensor<[784, 192]> self = ?", "List[int] size = [1, 28, 28, 192]"],
        ["Tensor<[2401, 6]> self = ?", "List[int] size = [49, 49, -1]"],
        ["Tensor<[1, 28, 28, 192]> self = ?", "List[int] size = [1, 4, 7, 4, 7, 192]"],
        ["Tensor<[16, 49, 192]> self = ?", "List[int] size = [784, 192]"],
        ["Tensor<[784, 576]> self = ?", "List[int] size = [16, 49, 576]"],
        ["Tensor<[16, 49, 576]> self = ?", "List[int] size = [16, 49, 3, 6, 32]"],
        ["Tensor<[96, 49, 49]> self = ?", "List[int] size = [16, 6, 49, 49]"],
        ["Tensor<[16, 6, 49, 49]> self = ?", "List[int] size = [96, 49, 49]"],
        ["Tensor<[96, 49, 32]> self = ?", "List[int] size = [16, 6, 49, 32]"],
        ["Tensor<[784, 192]> self = ?", "List[int] size = [16, 49, 192]"],
        ["Tensor<[16, 49, 192]> self = ?", "List[int] size = [1, 4, 4, 7, 7, 192]"],
        ["Tensor<[1, 28, 28, 192]> self = ?", "List[int] size = [784, 192]"],
        ["Tensor<[784, 768]> self = ?", "List[int] size = [1, 28, 28, 768]"],
        ["Tensor<[1, 28, 28, 768]> self = ?", "List[int] size = [784, 768]"],
        ["Tensor<[28, 28]> self = ?", "List[int] size = [4, 7, 4, 7]"],
        ["Tensor<[16, 6, 49, 49]> self = ?", "List[int] size = [1, 16, 6, 49, 49]"],
        ["Tensor<[1, 16, 6, 49, 49]> self = ?", "List[int] size = [-1, 6, 49, 49]"],
        ["Tensor<[1, 14, 14, 768]> self = ?", "List[int] size = [196, 768]"],
        ["Tensor<[196, 384]> self = ?", "List[int] size = [1, 14, 14, 384]"],
        ["Tensor<[2401, 12]> self = ?", "List[int] size = [49, 49, -1]"],
        ["Tensor<[1, 14, 14, 384]> self = ?", "List[int] size = [1, 2, 7, 2, 7, 384]"],
        ["Tensor<[4, 49, 384]> self = ?", "List[int] size = [196, 384]"],
        ["Tensor<[196, 1152]> self = ?", "List[int] size = [4, 49, 1152]"],
        ["Tensor<[4, 49, 1152]> self = ?", "List[int] size = [4, 49, 3, 12, 32]"],
        ["Tensor<[48, 49, 49]> self = ?", "List[int] size = [4, 12, 49, 49]"],
        ["Tensor<[4, 12, 49, 49]> self = ?", "List[int] size = [48, 49, 49]"],
        ["Tensor<[48, 49, 32]> self = ?", "List[int] size = [4, 12, 49, 32]"],
        ["Tensor<[196, 384]> self = ?", "List[int] size = [4, 49, 384]"],
        ["Tensor<[4, 49, 384]> self = ?", "List[int] size = [1, 2, 2, 7, 7, 384]"],
        ["Tensor<[1, 14, 14, 384]> self = ?", "List[int] size = [196, 384]"],
        ["Tensor<[196, 1536]> self = ?", "List[int] size = [1, 14, 14, 1536]"],
        ["Tensor<[1, 14, 14, 1536]> self = ?", "List[int] size = [196, 1536]"],
        ["Tensor<[14, 14]> self = ?", "List[int] size = [2, 7, 2, 7]"],
        ["Tensor<[4, 12, 49, 49]> self = ?", "List[int] size = [1, 4, 12, 49, 49]"],
        ["Tensor<[1, 4, 12, 49, 49]> self = ?", "List[int] size = [-1, 12, 49, 49]"],
        ["Tensor<[1, 7, 7, 1536]> self = ?", "List[int] size = [49, 1536]"],
        ["Tensor<[49, 768]> self = ?", "List[int] size = [1, 7, 7, 768]"],
        ["Tensor<[2401, 24]> self = ?", "List[int] size = [49, 49, -1]"],
        ["Tensor<[1, 7, 7, 768]> self = ?", "List[int] size = [1, 1, 7, 1, 7, 768]"],
        ["Tensor<[1, 1, 1, 7, 7, 768]> self = ?", "List[int] size = [1, 49, 768]"],
        ["Tensor<[1, 49, 768]> self = ?", "List[int] size = [49, 768]"],
        ["Tensor<[49, 2304]> self = ?", "List[int] size = [1, 49, 2304]"],
        ["Tensor<[1, 49, 2304]> self = ?", "List[int] size = [1, 49, 3, 24, 32]"],
        ["Tensor<[1, 24, 49, 32]> self = ?", "List[int] size = [24, 49, 32]"],
        ["Tensor<[1, 24, 32, 49]> self = ?", "List[int] size = [24, 32, 49]"],
        ["Tensor<[24, 49, 49]> self = ?", "List[int] size = [1, 24, 49, 49]"],
        ["Tensor<[1, 24, 49, 49]> self = ?", "List[int] size = [24, 49, 49]"],
        ["Tensor<[24, 49, 32]> self = ?", "List[int] size = [1, 24, 49, 32]"],
        ["Tensor<[49, 768]> self = ?", "List[int] size = [1, 49, 768]"],
        ["Tensor<[1, 49, 768]> self = ?", "List[int] size = [1, 1, 1, 7, 7, 768]"],
        ["Tensor<[1, 1, 7, 1, 7, 768]> self = ?", "List[int] size = [1, 7, 7, 768]"],
        ["Tensor<[1, 7, 7, 768]> self = ?", "List[int] size = [49, 768]"],
        ["Tensor<[49, 3072]> self = ?", "List[int] size = [1, 7, 7, 3072]"],
        ["Tensor<[1, 7, 7, 3072]> self = ?", "List[int] size = [49, 3072]"],
        ["Tensor<[1, 768, 1, 1]> self = ?", "List[int] size = [1, 768]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.view.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.view.default", input_strings
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
