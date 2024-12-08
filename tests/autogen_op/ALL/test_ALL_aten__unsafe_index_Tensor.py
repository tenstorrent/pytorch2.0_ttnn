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
        return torch.ops.aten._unsafe_index.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten._unsafe_index.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 1, 720, 1280]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[23, 1]>, <[40]>]"],
        ["Tensor<[1, 64, 15, 20]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[30, 1]>, <[40]>]"],
        ["Tensor<[1, 64, 30, 40]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[60, 1]>, <[80]>]"],
        ["Tensor<[1, 64, 60, 80]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[120, 1]>, <[160]>]"],
        ["Tensor<[1, 64, 120, 160]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[240, 1]>, <[320]>]"],
        ["Tensor<[1, 64, 240, 320]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[480, 1]>, <[640]>]"],
        ["Tensor<[1, 3, 320, 320]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[320, 1]>, <[320]>]"],
        ["Tensor<[1, 256, 128, 128]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]"],
        ["Tensor<[1, 256, 64, 64]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]"],
        ["Tensor<[1, 256, 32, 32]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]"],
        ["Tensor<[1, 256, 16, 16]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[128, 1]>, <[128]>]"],
        ["Tensor<[1, 1280, 8, 8]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[16, 1]>, <[16]>]"],
        ["Tensor<[1, 1280, s0, s1]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[2*s0, 1]>, <[2*s1]>]"],
        ["Tensor<[1, s0, s1, s2]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[2*s1, 1]>, <[2*s2]>]"],
        ["Tensor<[1, 1, 384, 512]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[12, 1]>, <[16]>]"],
        [
            "Tensor<[1, 192, 50, 83]> self = ?",
            "List[Optional[Tensor]] indices = [<[1, 1, 1, 1]>, <[1, 192, 1, 1]>, <[1, 1, 32, 1]>, <[1, 1, 1, 42]>]",
        ],
        ["Tensor<[1, 256, 16, 16]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[32, 1]>, <[32]>]"],
        ["Tensor<[1, 128, 32, 32]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[64, 1]>, <[64]>]"],
        ["Tensor<[1, 72, 28, 28]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>]"],
        ["Tensor<[1, 120, 14, 14]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>]"],
        ["Tensor<[1, 240, 14, 14]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>]"],
        ["Tensor<[1, 200, 7, 7]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]"],
        ["Tensor<[1, 184, 7, 7]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]"],
        ["Tensor<[1, 480, 7, 7]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]"],
        ["Tensor<[1, 672, 7, 7]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]"],
        ["Tensor<[1, 960, 3, 3]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[7, 1]>, <[7]>]"],
        ["Tensor<[1, 18, 28, 28]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>]"],
        ["Tensor<[1, 18, 14, 14]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>]"],
        ["Tensor<[1, 36, 14, 14]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>]"],
        ["Tensor<[1, 18, 7, 7]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[56, 1]>, <[56]>]"],
        ["Tensor<[1, 36, 7, 7]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[28, 1]>, <[28]>]"],
        ["Tensor<[1, 72, 7, 7]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[14, 1]>, <[14]>]"],
        ["Tensor<[1, 3, 480, 640]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[800, 1]>, <[1066]>]"],
        ["Tensor<[1, 256, 25, 34]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[50, 1]>, <[68]>]"],
        ["Tensor<[1, 256, 50, 68]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[100, 1]>, <[136]>]"],
        ["Tensor<[1, 3, 480, 640]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[300, 1]>, <[300]>]"],
        ["Tensor<[1, 3, 480, 640]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[320, 1]>, <[320]>]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._unsafe_index.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._unsafe_index.Tensor", input_strings
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
