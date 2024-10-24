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
        return torch.ops.aten.convolution_backward.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/Unet-brain-train", "aten.convolution_backward.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 1, 256, 256]> grad_output = ?",
            "Tensor<[1, 32, 256, 256]> input = ?",
            "Tensor<[1, 32, 1, 1]> weight = ?",
            "Optional[List[int]] bias_sizes = [1]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 32, 256, 256]> grad_output = ?",
            "Tensor<[1, 32, 256, 256]> input = ?",
            "Tensor<[32, 32, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 32, 256, 256]> grad_output = ?",
            "Tensor<[1, 64, 256, 256]> input = ?",
            "Tensor<[32, 64, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 32, 256, 256]> grad_output = ?",
            "Tensor<[1, 64, 128, 128]> input = ?",
            "Tensor<[64, 32, 2, 2]> weight = ?",
            "Optional[List[int]] bias_sizes = [32]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = True",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 64, 128, 128]> grad_output = ?",
            "Tensor<[1, 64, 128, 128]> input = ?",
            "Tensor<[64, 64, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 64, 128, 128]> grad_output = ?",
            "Tensor<[1, 128, 128, 128]> input = ?",
            "Tensor<[64, 128, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 64, 128, 128]> grad_output = ?",
            "Tensor<[1, 128, 64, 64]> input = ?",
            "Tensor<[128, 64, 2, 2]> weight = ?",
            "Optional[List[int]] bias_sizes = [64]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = True",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 128, 64, 64]> grad_output = ?",
            "Tensor<[1, 128, 64, 64]> input = ?",
            "Tensor<[128, 128, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 128, 64, 64]> grad_output = ?",
            "Tensor<[1, 256, 64, 64]> input = ?",
            "Tensor<[128, 256, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 128, 64, 64]> grad_output = ?",
            "Tensor<[1, 256, 32, 32]> input = ?",
            "Tensor<[256, 128, 2, 2]> weight = ?",
            "Optional[List[int]] bias_sizes = [128]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = True",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 256, 32, 32]> grad_output = ?",
            "Tensor<[1, 256, 32, 32]> input = ?",
            "Tensor<[256, 256, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 256, 32, 32]> grad_output = ?",
            "Tensor<[1, 512, 32, 32]> input = ?",
            "Tensor<[256, 512, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 256, 32, 32]> grad_output = ?",
            "Tensor<[1, 512, 16, 16]> input = ?",
            "Tensor<[512, 256, 2, 2]> weight = ?",
            "Optional[List[int]] bias_sizes = [256]",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = True",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 512, 16, 16]> grad_output = ?",
            "Tensor<[1, 512, 16, 16]> input = ?",
            "Tensor<[512, 512, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 512, 16, 16]> grad_output = ?",
            "Tensor<[1, 256, 16, 16]> input = ?",
            "Tensor<[512, 256, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 256, 32, 32]> grad_output = ?",
            "Tensor<[1, 128, 32, 32]> input = ?",
            "Tensor<[256, 128, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 128, 64, 64]> grad_output = ?",
            "Tensor<[1, 64, 64, 64]> input = ?",
            "Tensor<[128, 64, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 64, 128, 128]> grad_output = ?",
            "Tensor<[1, 32, 128, 128]> input = ?",
            "Tensor<[64, 32, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
        [
            "Tensor<[1, 32, 256, 256]> grad_output = ?",
            "Tensor<[1, 3, 256, 256]> input = ?",
            "Tensor<[32, 3, 3, 3]> weight = ?",
            "Optional[List[int]] bias_sizes = [0]",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
            "List[bool] output_mask = [True, True, False]",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.convolution_backward.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.convolution_backward.default", input_strings
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
