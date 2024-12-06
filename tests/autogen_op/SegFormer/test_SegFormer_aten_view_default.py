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
    save_pickle(metrics, "metrics-autogen-op/SegFormer", "aten.view.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 32, 128, 128]> self = ?", "List[int] size = [1, 32, 16384]"],
        ["Tensor<[1, 16384, 32]> self = ?", "List[int] size = [16384, 32]"],
        ["Tensor<[16384, 32]> self = ?", "List[int] size = [1, 16384, 32]"],
        ["Tensor<[1, 16384, 32]> self = ?", "List[int] size = [1, 16384, 1, 32]"],
        ["Tensor<[1, 32, 16384]> self = ?", "List[int] size = [1, 32, 128, 128]"],
        ["Tensor<[1, 32, 16, 16]> self = ?", "List[int] size = [1, 32, 256]"],
        ["Tensor<[1, 256, 32]> self = ?", "List[int] size = [256, 32]"],
        ["Tensor<[256, 32]> self = ?", "List[int] size = [1, 256, 32]"],
        ["Tensor<[1, 256, 32]> self = ?", "List[int] size = [1, 256, 1, 32]"],
        ["Tensor<[1, 1, 16384, 32]> self = ?", "List[int] size = [1, 16384, 32]"],
        ["Tensor<[1, 1, 32, 256]> self = ?", "List[int] size = [1, 32, 256]"],
        ["Tensor<[1, 16384, 256]> self = ?", "List[int] size = [1, 1, 16384, 256]"],
        ["Tensor<[1, 1, 16384, 256]> self = ?", "List[int] size = [1, 16384, 256]"],
        ["Tensor<[1, 1, 256, 32]> self = ?", "List[int] size = [1, 256, 32]"],
        ["Tensor<[1, 16384, 32]> self = ?", "List[int] size = [1, 1, 16384, 32]"],
        ["Tensor<[1, 16384, 1, 32]> self = ?", "List[int] size = [1, 16384, 32]"],
        ["Tensor<[16384, 128]> self = ?", "List[int] size = [1, 16384, 128]"],
        ["Tensor<[1, 128, 16384]> self = ?", "List[int] size = [1, 128, 128, 128]"],
        ["Tensor<[1, 128, 128, 128]> self = ?", "List[int] size = [1, 128, 16384]"],
        ["Tensor<[1, 16384, 128]> self = ?", "List[int] size = [16384, 128]"],
        ["Tensor<[1, 16384, 32]> self = ?", "List[int] size = [1, 128, 128, -1]"],
        ["Tensor<[1, 64, 64, 64]> self = ?", "List[int] size = [1, 64, 4096]"],
        ["Tensor<[1, 4096, 64]> self = ?", "List[int] size = [4096, 64]"],
        ["Tensor<[4096, 64]> self = ?", "List[int] size = [1, 4096, 64]"],
        ["Tensor<[1, 4096, 64]> self = ?", "List[int] size = [1, 4096, 2, 32]"],
        ["Tensor<[1, 64, 4096]> self = ?", "List[int] size = [1, 64, 64, 64]"],
        ["Tensor<[1, 64, 16, 16]> self = ?", "List[int] size = [1, 64, 256]"],
        ["Tensor<[1, 256, 64]> self = ?", "List[int] size = [256, 64]"],
        ["Tensor<[256, 64]> self = ?", "List[int] size = [1, 256, 64]"],
        ["Tensor<[1, 256, 64]> self = ?", "List[int] size = [1, 256, 2, 32]"],
        ["Tensor<[1, 2, 4096, 32]> self = ?", "List[int] size = [2, 4096, 32]"],
        ["Tensor<[1, 2, 32, 256]> self = ?", "List[int] size = [2, 32, 256]"],
        ["Tensor<[2, 4096, 256]> self = ?", "List[int] size = [1, 2, 4096, 256]"],
        ["Tensor<[1, 2, 4096, 256]> self = ?", "List[int] size = [2, 4096, 256]"],
        ["Tensor<[1, 2, 256, 32]> self = ?", "List[int] size = [2, 256, 32]"],
        ["Tensor<[2, 4096, 32]> self = ?", "List[int] size = [1, 2, 4096, 32]"],
        ["Tensor<[1, 4096, 2, 32]> self = ?", "List[int] size = [1, 4096, 64]"],
        ["Tensor<[4096, 256]> self = ?", "List[int] size = [1, 4096, 256]"],
        ["Tensor<[1, 256, 4096]> self = ?", "List[int] size = [1, 256, 64, 64]"],
        ["Tensor<[1, 256, 64, 64]> self = ?", "List[int] size = [1, 256, 4096]"],
        ["Tensor<[1, 4096, 256]> self = ?", "List[int] size = [4096, 256]"],
        ["Tensor<[1, 4096, 64]> self = ?", "List[int] size = [1, 64, 64, -1]"],
        ["Tensor<[1, 160, 32, 32]> self = ?", "List[int] size = [1, 160, 1024]"],
        ["Tensor<[1, 1024, 160]> self = ?", "List[int] size = [1024, 160]"],
        ["Tensor<[1024, 160]> self = ?", "List[int] size = [1, 1024, 160]"],
        ["Tensor<[1, 1024, 160]> self = ?", "List[int] size = [1, 1024, 5, 32]"],
        ["Tensor<[1, 160, 1024]> self = ?", "List[int] size = [1, 160, 32, 32]"],
        ["Tensor<[1, 160, 16, 16]> self = ?", "List[int] size = [1, 160, 256]"],
        ["Tensor<[1, 256, 160]> self = ?", "List[int] size = [256, 160]"],
        ["Tensor<[256, 160]> self = ?", "List[int] size = [1, 256, 160]"],
        ["Tensor<[1, 256, 160]> self = ?", "List[int] size = [1, 256, 5, 32]"],
        ["Tensor<[1, 5, 1024, 32]> self = ?", "List[int] size = [5, 1024, 32]"],
        ["Tensor<[1, 5, 32, 256]> self = ?", "List[int] size = [5, 32, 256]"],
        ["Tensor<[5, 1024, 256]> self = ?", "List[int] size = [1, 5, 1024, 256]"],
        ["Tensor<[1, 5, 1024, 256]> self = ?", "List[int] size = [5, 1024, 256]"],
        ["Tensor<[1, 5, 256, 32]> self = ?", "List[int] size = [5, 256, 32]"],
        ["Tensor<[5, 1024, 32]> self = ?", "List[int] size = [1, 5, 1024, 32]"],
        ["Tensor<[1, 1024, 5, 32]> self = ?", "List[int] size = [1, 1024, 160]"],
        ["Tensor<[1024, 640]> self = ?", "List[int] size = [1, 1024, 640]"],
        ["Tensor<[1, 640, 1024]> self = ?", "List[int] size = [1, 640, 32, 32]"],
        ["Tensor<[1, 640, 32, 32]> self = ?", "List[int] size = [1, 640, 1024]"],
        ["Tensor<[1, 1024, 640]> self = ?", "List[int] size = [1024, 640]"],
        ["Tensor<[1, 1024, 160]> self = ?", "List[int] size = [1, 32, 32, -1]"],
        ["Tensor<[1, 256, 16, 16]> self = ?", "List[int] size = [1, 256, 256]"],
        ["Tensor<[1, 256, 256]> self = ?", "List[int] size = [256, 256]"],
        ["Tensor<[256, 256]> self = ?", "List[int] size = [1, 256, 256]"],
        ["Tensor<[1, 256, 256]> self = ?", "List[int] size = [1, 256, 8, 32]"],
        ["Tensor<[1, 8, 256, 32]> self = ?", "List[int] size = [8, 256, 32]"],
        ["Tensor<[1, 8, 32, 256]> self = ?", "List[int] size = [8, 32, 256]"],
        ["Tensor<[8, 256, 256]> self = ?", "List[int] size = [1, 8, 256, 256]"],
        ["Tensor<[1, 8, 256, 256]> self = ?", "List[int] size = [8, 256, 256]"],
        ["Tensor<[8, 256, 32]> self = ?", "List[int] size = [1, 8, 256, 32]"],
        ["Tensor<[1, 256, 8, 32]> self = ?", "List[int] size = [1, 256, 256]"],
        ["Tensor<[256, 1024]> self = ?", "List[int] size = [1, 256, 1024]"],
        ["Tensor<[1, 1024, 256]> self = ?", "List[int] size = [1, 1024, 16, 16]"],
        ["Tensor<[1, 1024, 16, 16]> self = ?", "List[int] size = [1, 1024, 256]"],
        ["Tensor<[1, 256, 1024]> self = ?", "List[int] size = [256, 1024]"],
        ["Tensor<[1, 256, 256]> self = ?", "List[int] size = [1, 16, 16, -1]"],
        ["Tensor<[16384, 256]> self = ?", "List[int] size = [1, 16384, 256]"],
        ["Tensor<[1, 256, 16384]> self = ?", "List[int] size = [1, 256, 128, 128]"],
        ["Tensor<[1024, 256]> self = ?", "List[int] size = [1, 1024, 256]"],
        ["Tensor<[1, 256, 1024]> self = ?", "List[int] size = [1, 256, 32, 32]"],
        ["Tensor<[1, 256, 256]> self = ?", "List[int] size = [1, 256, 16, 16]"],
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
