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
        return torch.ops.aten.clone.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/swin_b", "aten.clone.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[4, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 8, 7, 7, 128]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 49, 49]> self = ?"],
        ["Tensor<[64, 49, 4, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 49, 128]> self = ?"],
        ["Tensor<[1, 8, 7, 8, 7, 128]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 56, 56, 512]> self = ?"],
        ["Tensor<[1, 56, 56, 128]> self = ?"],
        ["Tensor<[8, 8, 7, 7]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[8, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4, 4, 7, 7, 256]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 49, 49]> self = ?"],
        ["Tensor<[16, 49, 8, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 49, 256]> self = ?"],
        ["Tensor<[1, 4, 7, 4, 7, 256]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 28, 28, 1024]> self = ?"],
        ["Tensor<[1, 28, 28, 256]> self = ?"],
        ["Tensor<[4, 4, 7, 7]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 2, 7, 7, 512]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 49, 49]> self = ?"],
        ["Tensor<[4, 49, 16, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 49, 512]> self = ?"],
        ["Tensor<[1, 2, 7, 2, 7, 512]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 14, 14, 2048]> self = ?"],
        ["Tensor<[1, 14, 14, 512]> self = ?"],
        ["Tensor<[2, 2, 7, 7]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[32, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 32, 49, 49]> self = ?"],
        ["Tensor<[1, 49, 32, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 49, 1024]> self = ?"],
        ["Tensor<[1, 7, 7, 4096]> self = ?"],
        ["Tensor<[1, 7, 7, 1024]> self = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.clone.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.clone.default", input_strings
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
