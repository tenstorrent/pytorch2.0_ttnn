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
    save_pickle(metrics, "metrics-autogen-op/inception_v4.tf_in1k-train", "aten.convolution.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 3, 299, 299]> input = ?",
            "Tensor<[32, 3, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 32, 149, 149]> input = ?",
            "Tensor<[32, 32, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 32, 147, 147]> input = ?",
            "Tensor<[64, 32, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 64, 147, 147]> input = ?",
            "Tensor<[96, 64, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 160, 73, 73]> input = ?",
            "Tensor<[64, 160, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 64, 73, 73]> input = ?",
            "Tensor<[96, 64, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 64, 73, 73]> input = ?",
            "Tensor<[64, 64, 1, 7]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 3]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 64, 73, 73]> input = ?",
            "Tensor<[64, 64, 7, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [3, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 192, 71, 71]> input = ?",
            "Tensor<[192, 192, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 384, 35, 35]> input = ?",
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
            "Tensor<[1, 384, 35, 35]> input = ?",
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
            "Tensor<[1, 64, 35, 35]> input = ?",
            "Tensor<[96, 64, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 96, 35, 35]> input = ?",
            "Tensor<[96, 96, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 384, 35, 35]> input = ?",
            "Tensor<[384, 384, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 384, 35, 35]> input = ?",
            "Tensor<[192, 384, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 192, 35, 35]> input = ?",
            "Tensor<[224, 192, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 224, 35, 35]> input = ?",
            "Tensor<[256, 224, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 1024, 17, 17]> input = ?",
            "Tensor<[384, 1024, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 1024, 17, 17]> input = ?",
            "Tensor<[192, 1024, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 192, 17, 17]> input = ?",
            "Tensor<[224, 192, 1, 7]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 3]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 224, 17, 17]> input = ?",
            "Tensor<[256, 224, 7, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [3, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 192, 17, 17]> input = ?",
            "Tensor<[192, 192, 7, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [3, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 224, 17, 17]> input = ?",
            "Tensor<[224, 224, 7, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [3, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 224, 17, 17]> input = ?",
            "Tensor<[256, 224, 1, 7]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 3]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 1024, 17, 17]> input = ?",
            "Tensor<[128, 1024, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 192, 17, 17]> input = ?",
            "Tensor<[192, 192, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 1024, 17, 17]> input = ?",
            "Tensor<[256, 1024, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 256, 17, 17]> input = ?",
            "Tensor<[256, 256, 1, 7]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 3]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 256, 17, 17]> input = ?",
            "Tensor<[320, 256, 7, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [3, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 320, 17, 17]> input = ?",
            "Tensor<[320, 320, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 1536, 8, 8]> input = ?",
            "Tensor<[256, 1536, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 1536, 8, 8]> input = ?",
            "Tensor<[384, 1536, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 384, 8, 8]> input = ?",
            "Tensor<[256, 384, 1, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 384, 8, 8]> input = ?",
            "Tensor<[256, 384, 3, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 384, 8, 8]> input = ?",
            "Tensor<[448, 384, 3, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 448, 8, 8]> input = ?",
            "Tensor<[512, 448, 1, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 512, 8, 8]> input = ?",
            "Tensor<[256, 512, 1, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 512, 8, 8]> input = ?",
            "Tensor<[256, 512, 3, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 0]",
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
        "ttnn_fallbacks_to_host_count": "N/A",
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
        result_after = None
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            ttnn.graph.begin_graph_capture()
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {e}")
            metric["run"] = False
        finally:
            trace = ttnn.graph.end_graph_capture()
            call_stack = ttnn.graph.extract_calltrace(trace)
            if metric["run"] == True:
                print(call_stack)
                expected_to_host_count = 0
                if result_after is None:
                    expected_to_host_count = 0
                elif isinstance(result_after, torch.Tensor):
                    expected_to_host_count = 1
                elif isinstance(result_after, (list, dict)):
                    expected_to_host_count = len(result_after)
                else:
                    print(f"Unexpected result_after type: {type(result_after)}")

                to_host_count = sum(["Tensor::cpu" in str(node) for node in call_stack])
                fallbacks_to_host_count = to_host_count - expected_to_host_count
                print(f"expected_to_host_count: {expected_to_host_count}")
                print(f"to_host_count: {to_host_count}")
                print(f"fallbacks_to_host_count: {fallbacks_to_host_count}")
                metric["ttnn_fallbacks_to_host_count"] = fallbacks_to_host_count

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
