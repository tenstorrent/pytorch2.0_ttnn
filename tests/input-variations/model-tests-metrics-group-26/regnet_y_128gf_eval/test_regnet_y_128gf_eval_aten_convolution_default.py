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
    save_pickle(metrics, "metrics-input-variations/model-tests-metrics-group-26/regnet_y_128gf eval", "aten.convolution.default")


@pytest.mark.parametrize("input_strings", [['Tensor<[1, 3, 384, 384]> input = ?', 'Tensor<[32, 3, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 32, 192, 192]> input = ?', 'Tensor<[528, 32, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 32, 192, 192]> input = ?', 'Tensor<[528, 32, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 528, 192, 192]> input = ?', 'Tensor<[528, 264, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 2'], ['Tensor<[1, 528, 1, 1]> input = ?', 'Tensor<[8, 528, 1, 1]> weight = ?', 'Optional[Tensor]<[8]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 8, 1, 1]> input = ?', 'Tensor<[528, 8, 1, 1]> weight = ?', 'Optional[Tensor]<[528]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 528, 96, 96]> input = ?', 'Tensor<[528, 528, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 528, 96, 96]> input = ?', 'Tensor<[528, 264, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 2'], ['Tensor<[1, 528, 1, 1]> input = ?', 'Tensor<[132, 528, 1, 1]> weight = ?', 'Optional[Tensor]<[132]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 132, 1, 1]> input = ?', 'Tensor<[528, 132, 1, 1]> weight = ?', 'Optional[Tensor]<[528]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 528, 96, 96]> input = ?', 'Tensor<[1056, 528, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 528, 96, 96]> input = ?', 'Tensor<[1056, 528, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 1056, 96, 96]> input = ?', 'Tensor<[1056, 264, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 4'], ['Tensor<[1, 1056, 1, 1]> input = ?', 'Tensor<[132, 1056, 1, 1]> weight = ?', 'Optional[Tensor]<[132]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 132, 1, 1]> input = ?', 'Tensor<[1056, 132, 1, 1]> weight = ?', 'Optional[Tensor]<[1056]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 1056, 48, 48]> input = ?', 'Tensor<[1056, 1056, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 1056, 48, 48]> input = ?', 'Tensor<[1056, 264, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 4'], ['Tensor<[1, 1056, 1, 1]> input = ?', 'Tensor<[264, 1056, 1, 1]> weight = ?', 'Optional[Tensor]<[264]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 264, 1, 1]> input = ?', 'Tensor<[1056, 264, 1, 1]> weight = ?', 'Optional[Tensor]<[1056]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 1056, 48, 48]> input = ?', 'Tensor<[2904, 1056, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 1056, 48, 48]> input = ?', 'Tensor<[2904, 1056, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 2904, 48, 48]> input = ?', 'Tensor<[2904, 264, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 11'], ['Tensor<[1, 2904, 1, 1]> input = ?', 'Tensor<[264, 2904, 1, 1]> weight = ?', 'Optional[Tensor]<[264]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 264, 1, 1]> input = ?', 'Tensor<[2904, 264, 1, 1]> weight = ?', 'Optional[Tensor]<[2904]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 2904, 24, 24]> input = ?', 'Tensor<[2904, 2904, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 2904, 24, 24]> input = ?', 'Tensor<[2904, 264, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 11'], ['Tensor<[1, 2904, 1, 1]> input = ?', 'Tensor<[726, 2904, 1, 1]> weight = ?', 'Optional[Tensor]<[726]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 726, 1, 1]> input = ?', 'Tensor<[2904, 726, 1, 1]> weight = ?', 'Optional[Tensor]<[2904]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 2904, 24, 24]> input = ?', 'Tensor<[7392, 2904, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 2904, 24, 24]> input = ?', 'Tensor<[7392, 2904, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 7392, 24, 24]> input = ?', 'Tensor<[7392, 264, 3, 3]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [2, 2]', 'List[int] padding = [1, 1]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 28'], ['Tensor<[1, 7392, 1, 1]> input = ?', 'Tensor<[726, 7392, 1, 1]> weight = ?', 'Optional[Tensor]<[726]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 726, 1, 1]> input = ?', 'Tensor<[7392, 726, 1, 1]> weight = ?', 'Optional[Tensor]<[7392]> bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1'], ['Tensor<[1, 7392, 12, 12]> input = ?', 'Tensor<[7392, 7392, 1, 1]> weight = ?', 'Optional[Tensor] bias = ?', 'List[int] stride = [1, 1]', 'List[int] padding = [0, 0]', 'List[int] dilation = [1, 1]', 'bool transposed = False', 'List[int] output_padding = [0, 0]', 'int groups = 1']])
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