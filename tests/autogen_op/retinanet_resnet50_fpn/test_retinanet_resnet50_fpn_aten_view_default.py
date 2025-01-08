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
    save_pickle(metrics, "metrics-autogen-op/retinanet_resnet50_fpn", "aten.view.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[64]> self = ?", "List[int] size = [1, -1, 1, 1]"],
        ["Tensor<[256]> self = ?", "List[int] size = [1, -1, 1, 1]"],
        ["Tensor<[128]> self = ?", "List[int] size = [1, -1, 1, 1]"],
        ["Tensor<[512]> self = ?", "List[int] size = [1, -1, 1, 1]"],
        ["Tensor<[1024]> self = ?", "List[int] size = [1, -1, 1, 1]"],
        ["Tensor<[2048]> self = ?", "List[int] size = [1, -1, 1, 1]"],
        ["Tensor<[1, 819, 100, 136]> self = ?", "List[int] size = [1, -1, 91, 100, 136]"],
        ["Tensor<[1, 819, 50, 68]> self = ?", "List[int] size = [1, -1, 91, 50, 68]"],
        ["Tensor<[1, 819, 25, 34]> self = ?", "List[int] size = [1, -1, 91, 25, 34]"],
        ["Tensor<[1, 819, 13, 17]> self = ?", "List[int] size = [1, -1, 91, 13, 17]"],
        ["Tensor<[1, 819, 7, 9]> self = ?", "List[int] size = [1, -1, 91, 7, 9]"],
        ["Tensor<[1, 36, 100, 136]> self = ?", "List[int] size = [1, -1, 4, 100, 136]"],
        ["Tensor<[1, 36, 50, 68]> self = ?", "List[int] size = [1, -1, 4, 50, 68]"],
        ["Tensor<[1, 36, 25, 34]> self = ?", "List[int] size = [1, -1, 4, 25, 34]"],
        ["Tensor<[1, 36, 13, 17]> self = ?", "List[int] size = [1, -1, 4, 13, 17]"],
        ["Tensor<[1, 36, 7, 9]> self = ?", "List[int] size = [1, -1, 4, 7, 9]"],
        ["Tensor<[100]> self = ?", "List[int] size = [-1, 1]"],
        ["Tensor<[136]> self = ?", "List[int] size = [1, -1]"],
        ["Tensor<[13600, 4]> self = ?", "List[int] size = [-1, 1, 4]"],
        ["Tensor<[9, 4]> self = ?", "List[int] size = [1, -1, 4]"],
        ["Tensor<[13600, 9, 4]> self = ?", "List[int] size = [-1, 4]"],
        ["Tensor<[50]> self = ?", "List[int] size = [-1, 1]"],
        ["Tensor<[68]> self = ?", "List[int] size = [1, -1]"],
        ["Tensor<[3400, 4]> self = ?", "List[int] size = [-1, 1, 4]"],
        ["Tensor<[3400, 9, 4]> self = ?", "List[int] size = [-1, 4]"],
        ["Tensor<[25]> self = ?", "List[int] size = [-1, 1]"],
        ["Tensor<[34]> self = ?", "List[int] size = [1, -1]"],
        ["Tensor<[850, 4]> self = ?", "List[int] size = [-1, 1, 4]"],
        ["Tensor<[850, 9, 4]> self = ?", "List[int] size = [-1, 4]"],
        ["Tensor<[13]> self = ?", "List[int] size = [-1, 1]"],
        ["Tensor<[17]> self = ?", "List[int] size = [1, -1]"],
        ["Tensor<[221, 4]> self = ?", "List[int] size = [-1, 1, 4]"],
        ["Tensor<[221, 9, 4]> self = ?", "List[int] size = [-1, 4]"],
        ["Tensor<[7]> self = ?", "List[int] size = [-1, 1]"],
        ["Tensor<[9]> self = ?", "List[int] size = [1, -1]"],
        ["Tensor<[63, 4]> self = ?", "List[int] size = [-1, 1, 4]"],
        ["Tensor<[63, 9, 4]> self = ?", "List[int] size = [-1, 4]"],
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
        "ttnn_fallbacks_to_host_count": "N/A",
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
