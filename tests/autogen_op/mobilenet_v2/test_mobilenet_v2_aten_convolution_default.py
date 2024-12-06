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
        return torch.ops.aten.convolution.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/mobilenet_v2", "aten.convolution.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 3, 224, 224]> input = ?",
            "Tensor<[32, 3, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 32, 112, 112]> input = ?",
            "Tensor<[32, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 32",
        ],
        [
            "Tensor<[1, 32, 112, 112]> input = ?",
            "Tensor<[16, 32, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 16, 112, 112]> input = ?",
            "Tensor<[96, 16, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 96, 112, 112]> input = ?",
            "Tensor<[96, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 96",
        ],
        [
            "Tensor<[1, 96, 56, 56]> input = ?",
            "Tensor<[24, 96, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 24, 56, 56]> input = ?",
            "Tensor<[144, 24, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 144, 56, 56]> input = ?",
            "Tensor<[144, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 144",
        ],
        [
            "Tensor<[1, 144, 56, 56]> input = ?",
            "Tensor<[24, 144, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 144, 56, 56]> input = ?",
            "Tensor<[144, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 144",
        ],
        [
            "Tensor<[1, 144, 28, 28]> input = ?",
            "Tensor<[32, 144, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 32, 28, 28]> input = ?",
            "Tensor<[192, 32, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 192, 28, 28]> input = ?",
            "Tensor<[192, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 192",
        ],
        [
            "Tensor<[1, 192, 28, 28]> input = ?",
            "Tensor<[32, 192, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 192, 28, 28]> input = ?",
            "Tensor<[192, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 192",
        ],
        [
            "Tensor<[1, 192, 14, 14]> input = ?",
            "Tensor<[64, 192, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 64, 14, 14]> input = ?",
            "Tensor<[384, 64, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 384, 14, 14]> input = ?",
            "Tensor<[384, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 384",
        ],
        [
            "Tensor<[1, 384, 14, 14]> input = ?",
            "Tensor<[64, 384, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 384, 14, 14]> input = ?",
            "Tensor<[96, 384, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 96, 14, 14]> input = ?",
            "Tensor<[576, 96, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 576, 14, 14]> input = ?",
            "Tensor<[576, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 576",
        ],
        [
            "Tensor<[1, 576, 14, 14]> input = ?",
            "Tensor<[96, 576, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 576, 14, 14]> input = ?",
            "Tensor<[576, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 576",
        ],
        [
            "Tensor<[1, 576, 7, 7]> input = ?",
            "Tensor<[160, 576, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 160, 7, 7]> input = ?",
            "Tensor<[960, 160, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 960, 7, 7]> input = ?",
            "Tensor<[960, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 960",
        ],
        [
            "Tensor<[1, 960, 7, 7]> input = ?",
            "Tensor<[160, 960, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 960, 7, 7]> input = ?",
            "Tensor<[320, 960, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 320, 7, 7]> input = ?",
            "Tensor<[1280, 320, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.convolution.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.convolution.default", input_strings
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
