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
    save_pickle(metrics, "metrics-autogen-op/densenet161", "aten.relu.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 96, 112, 112]> self = ?"],
        ["Tensor<[1, 96, 56, 56]> self = ?"],
        ["Tensor<[1, 192, 56, 56]> self = ?"],
        ["Tensor<[1, 144, 56, 56]> self = ?"],
        ["Tensor<[1, 240, 56, 56]> self = ?"],
        ["Tensor<[1, 288, 56, 56]> self = ?"],
        ["Tensor<[1, 336, 56, 56]> self = ?"],
        ["Tensor<[1, 384, 56, 56]> self = ?"],
        ["Tensor<[1, 192, 28, 28]> self = ?"],
        ["Tensor<[1, 240, 28, 28]> self = ?"],
        ["Tensor<[1, 288, 28, 28]> self = ?"],
        ["Tensor<[1, 336, 28, 28]> self = ?"],
        ["Tensor<[1, 384, 28, 28]> self = ?"],
        ["Tensor<[1, 432, 28, 28]> self = ?"],
        ["Tensor<[1, 480, 28, 28]> self = ?"],
        ["Tensor<[1, 528, 28, 28]> self = ?"],
        ["Tensor<[1, 576, 28, 28]> self = ?"],
        ["Tensor<[1, 624, 28, 28]> self = ?"],
        ["Tensor<[1, 672, 28, 28]> self = ?"],
        ["Tensor<[1, 720, 28, 28]> self = ?"],
        ["Tensor<[1, 768, 28, 28]> self = ?"],
        ["Tensor<[1, 384, 14, 14]> self = ?"],
        ["Tensor<[1, 192, 14, 14]> self = ?"],
        ["Tensor<[1, 432, 14, 14]> self = ?"],
        ["Tensor<[1, 480, 14, 14]> self = ?"],
        ["Tensor<[1, 528, 14, 14]> self = ?"],
        ["Tensor<[1, 576, 14, 14]> self = ?"],
        ["Tensor<[1, 624, 14, 14]> self = ?"],
        ["Tensor<[1, 672, 14, 14]> self = ?"],
        ["Tensor<[1, 720, 14, 14]> self = ?"],
        ["Tensor<[1, 768, 14, 14]> self = ?"],
        ["Tensor<[1, 816, 14, 14]> self = ?"],
        ["Tensor<[1, 864, 14, 14]> self = ?"],
        ["Tensor<[1, 912, 14, 14]> self = ?"],
        ["Tensor<[1, 960, 14, 14]> self = ?"],
        ["Tensor<[1, 1008, 14, 14]> self = ?"],
        ["Tensor<[1, 1056, 14, 14]> self = ?"],
        ["Tensor<[1, 1104, 14, 14]> self = ?"],
        ["Tensor<[1, 1152, 14, 14]> self = ?"],
        ["Tensor<[1, 1200, 14, 14]> self = ?"],
        ["Tensor<[1, 1248, 14, 14]> self = ?"],
        ["Tensor<[1, 1296, 14, 14]> self = ?"],
        ["Tensor<[1, 1344, 14, 14]> self = ?"],
        ["Tensor<[1, 1392, 14, 14]> self = ?"],
        ["Tensor<[1, 1440, 14, 14]> self = ?"],
        ["Tensor<[1, 1488, 14, 14]> self = ?"],
        ["Tensor<[1, 1536, 14, 14]> self = ?"],
        ["Tensor<[1, 1584, 14, 14]> self = ?"],
        ["Tensor<[1, 1632, 14, 14]> self = ?"],
        ["Tensor<[1, 1680, 14, 14]> self = ?"],
        ["Tensor<[1, 1728, 14, 14]> self = ?"],
        ["Tensor<[1, 1776, 14, 14]> self = ?"],
        ["Tensor<[1, 1824, 14, 14]> self = ?"],
        ["Tensor<[1, 1872, 14, 14]> self = ?"],
        ["Tensor<[1, 1920, 14, 14]> self = ?"],
        ["Tensor<[1, 1968, 14, 14]> self = ?"],
        ["Tensor<[1, 2016, 14, 14]> self = ?"],
        ["Tensor<[1, 2064, 14, 14]> self = ?"],
        ["Tensor<[1, 2112, 14, 14]> self = ?"],
        ["Tensor<[1, 1056, 7, 7]> self = ?"],
        ["Tensor<[1, 192, 7, 7]> self = ?"],
        ["Tensor<[1, 1104, 7, 7]> self = ?"],
        ["Tensor<[1, 1152, 7, 7]> self = ?"],
        ["Tensor<[1, 1200, 7, 7]> self = ?"],
        ["Tensor<[1, 1248, 7, 7]> self = ?"],
        ["Tensor<[1, 1296, 7, 7]> self = ?"],
        ["Tensor<[1, 1344, 7, 7]> self = ?"],
        ["Tensor<[1, 1392, 7, 7]> self = ?"],
        ["Tensor<[1, 1440, 7, 7]> self = ?"],
        ["Tensor<[1, 1488, 7, 7]> self = ?"],
        ["Tensor<[1, 1536, 7, 7]> self = ?"],
        ["Tensor<[1, 1584, 7, 7]> self = ?"],
        ["Tensor<[1, 1632, 7, 7]> self = ?"],
        ["Tensor<[1, 1680, 7, 7]> self = ?"],
        ["Tensor<[1, 1728, 7, 7]> self = ?"],
        ["Tensor<[1, 1776, 7, 7]> self = ?"],
        ["Tensor<[1, 1824, 7, 7]> self = ?"],
        ["Tensor<[1, 1872, 7, 7]> self = ?"],
        ["Tensor<[1, 1920, 7, 7]> self = ?"],
        ["Tensor<[1, 1968, 7, 7]> self = ?"],
        ["Tensor<[1, 2016, 7, 7]> self = ?"],
        ["Tensor<[1, 2064, 7, 7]> self = ?"],
        ["Tensor<[1, 2112, 7, 7]> self = ?"],
        ["Tensor<[1, 2160, 7, 7]> self = ?"],
        ["Tensor<[1, 2208, 7, 7]> self = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.relu.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.relu.default", input_strings
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
                return

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
