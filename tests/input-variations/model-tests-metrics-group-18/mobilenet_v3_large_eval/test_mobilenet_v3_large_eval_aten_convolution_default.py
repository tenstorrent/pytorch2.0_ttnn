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
    save_pickle(metrics, "metrics-input-variations/model-tests-metrics-group-18/mobilenet_v3_large eval", "aten.convolution.default")


@pytest.mark.parametrize("input_strings", [['Tensor<[1, 3, 224, 224]> input = ?', 'Tensor<[16, 3, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 16, 112, 112]> input = ?', 'Tensor<[16, 1, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 16'], ['Tensor<[1, 16, 112, 112]> input = ?', 'Tensor<[16, 16, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 16, 112, 112]> input = ?', 'Tensor<[64, 16, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 64, 112, 112]> input = ?', 'Tensor<[64, 1, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 64'], ['Tensor<[1, 64, 56, 56]> input = ?', 'Tensor<[24, 64, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 24, 56, 56]> input = ?', 'Tensor<[72, 24, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 72, 56, 56]> input = ?', 'Tensor<[72, 1, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 72'], ['Tensor<[1, 72, 56, 56]> input = ?', 'Tensor<[24, 72, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 72, 56, 56]> input = ?', 'Tensor<[72, 1, 5, 5]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [2, 2]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 72'], ['Tensor<[1, 72, 1, 1]> input = ?', 'Tensor<[24, 72, 1, 1]> weight = ?', 'Optional[Tensor]<[24]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 24, 1, 1]> input = ?', 'Tensor<[72, 24, 1, 1]> weight = ?', 'Optional[Tensor]<[72]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 72, 28, 28]> input = ?', 'Tensor<[40, 72, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 40, 28, 28]> input = ?', 'Tensor<[120, 40, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 120, 28, 28]> input = ?', 'Tensor<[120, 1, 5, 5]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [2, 2]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 120'], ['Tensor<[1, 120, 1, 1]> input = ?', 'Tensor<[32, 120, 1, 1]> weight = ?', 'Optional[Tensor]<[32]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 32, 1, 1]> input = ?', 'Tensor<[120, 32, 1, 1]> weight = ?', 'Optional[Tensor]<[120]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 120, 28, 28]> input = ?', 'Tensor<[40, 120, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 40, 28, 28]> input = ?', 'Tensor<[240, 40, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 240, 28, 28]> input = ?', 'Tensor<[240, 1, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 240'], ['Tensor<[1, 240, 14, 14]> input = ?', 'Tensor<[80, 240, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 80, 14, 14]> input = ?', 'Tensor<[200, 80, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 200, 14, 14]> input = ?', 'Tensor<[200, 1, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 200'], ['Tensor<[1, 200, 14, 14]> input = ?', 'Tensor<[80, 200, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 80, 14, 14]> input = ?', 'Tensor<[184, 80, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 184, 14, 14]> input = ?', 'Tensor<[184, 1, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 184'], ['Tensor<[1, 184, 14, 14]> input = ?', 'Tensor<[80, 184, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 80, 14, 14]> input = ?', 'Tensor<[480, 80, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 480, 14, 14]> input = ?', 'Tensor<[480, 1, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 480'], ['Tensor<[1, 480, 1, 1]> input = ?', 'Tensor<[120, 480, 1, 1]> weight = ?', 'Optional[Tensor]<[120]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 120, 1, 1]> input = ?', 'Tensor<[480, 120, 1, 1]> weight = ?', 'Optional[Tensor]<[480]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 480, 14, 14]> input = ?', 'Tensor<[112, 480, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 112, 14, 14]> input = ?', 'Tensor<[672, 112, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 672, 14, 14]> input = ?', 'Tensor<[672, 1, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 672'], ['Tensor<[1, 672, 1, 1]> input = ?', 'Tensor<[168, 672, 1, 1]> weight = ?', 'Optional[Tensor]<[168]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 168, 1, 1]> input = ?', 'Tensor<[672, 168, 1, 1]> weight = ?', 'Optional[Tensor]<[672]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 672, 14, 14]> input = ?', 'Tensor<[112, 672, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 672, 14, 14]> input = ?', 'Tensor<[672, 1, 5, 5]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [2, 2]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 672'], ['Tensor<[1, 672, 7, 7]> input = ?', 'Tensor<[160, 672, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 160, 7, 7]> input = ?', 'Tensor<[960, 160, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 960, 7, 7]> input = ?', 'Tensor<[960, 1, 5, 5]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [2, 2]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 960'], ['Tensor<[1, 960, 1, 1]> input = ?', 'Tensor<[240, 960, 1, 1]> weight = ?', 'Optional[Tensor]<[240]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 240, 1, 1]> input = ?', 'Tensor<[960, 240, 1, 1]> weight = ?', 'Optional[Tensor]<[960]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 960, 7, 7]> input = ?', 'Tensor<[160, 960, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1']])
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
            "opname": "aten.convolution.default",
            "input_strings": input_strings,
            "native_run": False,
            "run": False,
            "accuracy": False,
            "convert_to_ttnn": False,
        }
    m = AtenModule()
    input_args, input_kwargs = get_input_vals_from_metric_str("aten.convolution.default", input_strings)
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