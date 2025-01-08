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
        return torch.ops.aten.unsqueeze.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.unsqueeze.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 256]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 256]> self = ?", "int dim = 2"],
        ["Tensor<[1, 32]> self = ?", "int dim = 1"],
        ["Tensor<[32, 32]> self = ?", "int dim = 0"],
        ["Tensor<[1, 32, 32]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 32]> self = ?", "int dim = 2"],
        ["Tensor<[7, 7]> self = ?", "int dim = 0"],
        ["Tensor<[1, 7, 7]> self = ?", "int dim = 1"],
        ["Tensor<[2, 7]> self = ?", "int dim = 1"],
        ["Tensor<[2, 1, 7]> self = ?", "int dim = 2"],
        ["Tensor<[1, 23, 40]> self = ?", "int dim = 3"],
        ["Tensor<[100, 256]> self = ?", "int dim = 1"],
        ["Tensor<[1, 25]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 25]> self = ?", "int dim = 2"],
        ["Tensor<[1, 15]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 15]> self = ?", "int dim = 2"],
        ["Tensor<[15]> self = ?", "int dim = 1"],
        ["Tensor<[6, 15, 15]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1]> self = ?", "int dim = 2"],
        ["Tensor<[1, 1, 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 1]> self = ?", "int dim = 2"],
        ["Tensor<[1]> self = ?", "int dim = 1"],
        ["Tensor<[6, 1, 1]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1, 2]> self = ?", "int dim = 1"],
        ["Tensor<[1, 2]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 2]> self = ?", "int dim = 2"],
        ["Tensor<[2]> self = ?", "int dim = 1"],
        ["Tensor<[6, 2, 2]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1, s0 + 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, s0 + 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, s0 + 1]> self = ?", "int dim = 2"],
        ["Tensor<[s0 + 1]> self = ?", "int dim = 1"],
        ["Tensor<[s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[6, s0 + 1, s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1, 17]> self = ?", "int dim = 1"],
        ["Tensor<[1, 17]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 17]> self = ?", "int dim = 2"],
        ["Tensor<[17]> self = ?", "int dim = 1"],
        ["Tensor<[6, 17, 17]> self = ?", "int dim = 0"],
        ["Tensor<[1, 7, 64]> self = ?", "int dim = 1"],
        ["Tensor<[1, 30, 40]> self = ?", "int dim = 1"],
        ["Tensor<[1, 60, 80]> self = ?", "int dim = 1"],
        ["Tensor<[1, 120, 160]> self = ?", "int dim = 1"],
        ["Tensor<[1, 7]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 7]> self = ?", "int dim = 2"],
        ["Tensor<[1, 45]> self = ?", "int dim = 1"],
        ["Tensor<[45, 45]> self = ?", "int dim = 0"],
        ["Tensor<[1, 45, 45]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 45]> self = ?", "int dim = 2"],
        ["Tensor<[1, 46]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 46]> self = ?", "int dim = 2"],
        ["Tensor<[1, s10 + 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, s10 + 1]> self = ?", "int dim = 2"],
        ["Tensor<[2048, 2048]> self = ?", "int dim = 0"],
        ["Tensor<[1, 2048, 2048]> self = ?", "int dim = 1"],
        ["Tensor<[64]> self = ?", "int dim = 0"],
        ["Tensor<[1, 64]> self = ?", "int dim = 2"],
        ["Tensor<[1, 512]> self = ?", "int dim = 2"],
        ["Tensor<[3]> self = ?", "int dim = 1"],
        ["Tensor<[3, 1]> self = ?", "int dim = 2"],
        ["Tensor<[3, 320, 320]> self = ?", "int dim = 0"],
        ["Tensor<[59, 59]> self = ?", "int dim = 0"],
        ["Tensor<[1, 59, 59]> self = ?", "int dim = 1"],
        ["Tensor<[1, 59]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 59]> self = ?", "int dim = 2"],
        ["Tensor<[1, 60]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 60]> self = ?", "int dim = 2"],
        ["Tensor<[1, 2048]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 2048]> self = ?", "int dim = 2"],
        ["Tensor<[1, 10]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 10]> self = ?", "int dim = 2"],
        ["Tensor<[1, 8]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 8]> self = ?", "int dim = 2"],
        ["Tensor<[160]> self = ?", "int dim = 0"],
        ["Tensor<[1, 320]> self = ?", "int dim = 2"],
        ["Tensor<[1, 320, 1]> self = ?", "int dim = 3"],
        ["Tensor<[1, 640]> self = ?", "int dim = 2"],
        ["Tensor<[1, 640, 1]> self = ?", "int dim = 3"],
        ["Tensor<[1, 1280]> self = ?", "int dim = 2"],
        ["Tensor<[1, 1280, 1]> self = ?", "int dim = 3"],
        ["Tensor<[2*s0]> self = ?", "int dim = -1"],
        ["Tensor<[2*s1]> self = ?", "int dim = -1"],
        ["Tensor<[1, 384, 512]> self = ?", "int dim = 1"],
        ["Tensor<[19, 19]> self = ?", "int dim = 0"],
        ["Tensor<[1, 19, 19]> self = ?", "int dim = 1"],
        ["Tensor<[1, 19]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 19]> self = ?", "int dim = 2"],
        ["Tensor<[19]> self = ?", "int dim = 0"],
        ["Tensor<[1, 192]> self = ?", "int dim = 1"],
        ["Tensor<[1, 9]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 9]> self = ?", "int dim = 2"],
        ["Tensor<[1, 12]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 12]> self = ?", "int dim = 2"],
        ["Tensor<[1, 5]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 5]> self = ?", "int dim = 2"],
        ["Tensor<[1, 5, 16]> self = ?", "int dim = 2"],
        ["Tensor<[1, 5, 1, 16]> self = ?", "int dim = 4"],
        ["Tensor<[1, 6]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 6]> self = ?", "int dim = 2"],
        ["Tensor<[1, 1, 16]> self = ?", "int dim = 2"],
        ["Tensor<[1, 1, 1, 16]> self = ?", "int dim = 4"],
        ["Tensor<[1, 224, 224]> self = ?", "int dim = 1"],
        ["Tensor<[12, 197, 197]> self = ?", "int dim = 0"],
        ["Tensor<[1, 768]> self = ?", "int dim = 1"],
        ["Tensor<[16, 197, 197]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1024]> self = ?", "int dim = 1"],
        ["Tensor<[3, 480, 640]> self = ?", "int dim = 0"],
        ["Tensor<[1, 24]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 24]> self = ?", "int dim = 2"],
        ["Tensor<[24]> self = ?", "int dim = 1"],
        ["Tensor<[4, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[64, 49]> self = ?", "int dim = 1"],
        ["Tensor<[64, 49]> self = ?", "int dim = 2"],
        ["Tensor<[64, 49, 49]> self = ?", "int dim = 1"],
        ["Tensor<[64, 1, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[8, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[16, 49]> self = ?", "int dim = 1"],
        ["Tensor<[16, 49]> self = ?", "int dim = 2"],
        ["Tensor<[16, 49, 49]> self = ?", "int dim = 1"],
        ["Tensor<[16, 1, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[16, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[4, 49]> self = ?", "int dim = 1"],
        ["Tensor<[4, 49]> self = ?", "int dim = 2"],
        ["Tensor<[4, 49, 49]> self = ?", "int dim = 1"],
        ["Tensor<[4, 1, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[32, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[3, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[6, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[12, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[24, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[4, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[64, 64]> self = ?", "int dim = 1"],
        ["Tensor<[64, 64]> self = ?", "int dim = 2"],
        ["Tensor<[64, 64, 64]> self = ?", "int dim = 1"],
        ["Tensor<[64, 1, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[8, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[16, 64]> self = ?", "int dim = 1"],
        ["Tensor<[16, 64]> self = ?", "int dim = 2"],
        ["Tensor<[16, 64, 64]> self = ?", "int dim = 1"],
        ["Tensor<[16, 1, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[16, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[4, 64]> self = ?", "int dim = 1"],
        ["Tensor<[4, 64]> self = ?", "int dim = 2"],
        ["Tensor<[4, 64, 64]> self = ?", "int dim = 1"],
        ["Tensor<[4, 1, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[32, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[3, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[6, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[12, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[24, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[10]> self = ?", "int dim = 1"],
        ["Tensor<[12, 10, 10]> self = ?", "int dim = 0"],
        ["Tensor<[12, 1, 1]> self = ?", "int dim = 0"],
        ["Tensor<[12, 2, 2]> self = ?", "int dim = 0"],
        ["Tensor<[12, s0 + 1, s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[16, 10, 10]> self = ?", "int dim = 0"],
        ["Tensor<[16, 1, 1]> self = ?", "int dim = 0"],
        ["Tensor<[16, 2, 2]> self = ?", "int dim = 0"],
        ["Tensor<[16, s0 + 1, s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[8, 10, 10]> self = ?", "int dim = 0"],
        ["Tensor<[8, 1, 1]> self = ?", "int dim = 0"],
        ["Tensor<[8, 2, 2]> self = ?", "int dim = 0"],
        ["Tensor<[8, s0 + 1, s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[1, 14]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 14]> self = ?", "int dim = 2"],
        ["Tensor<[197, 1, 3, 768]> self = ?", "int dim = 0"],
        ["Tensor<[50, 1, 3, 768]> self = ?", "int dim = 0"],
        ["Tensor<[1370, 1, 3, 1280]> self = ?", "int dim = 0"],
        ["Tensor<[197, 1, 3, 1024]> self = ?", "int dim = 0"],
        ["Tensor<[50, 1, 3, 1024]> self = ?", "int dim = 0"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.unsqueeze.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.unsqueeze.default", input_strings
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
