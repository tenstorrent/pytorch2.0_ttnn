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
        return torch.ops.aten.bmm.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.bmm.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[16, 256, 64]> self = ?", "Tensor<[16, 64, 256]> mat2 = ?"],
        ["Tensor<[16, 256, 256]> self = ?", "Tensor<[16, 256, 64]> mat2 = ?"],
        ["Tensor<[16, 32, 32]> self = ?", "Tensor<[16, 32, 96]> mat2 = ?"],
        ["Tensor<[12, 50, 64]> self = ?", "Tensor<[12, 64, 50]> mat2 = ?"],
        ["Tensor<[12, 50, 50]> self = ?", "Tensor<[12, 50, 64]> mat2 = ?"],
        ["Tensor<[16, 7, 64]> self = ?", "Tensor<[16, 64, 7]> mat2 = ?"],
        ["Tensor<[16, 7, 7]> self = ?", "Tensor<[16, 7, 64]> mat2 = ?"],
        ["Tensor<[16, 64, 7]> self = ?", "Tensor<[16, 7, 7]> mat2 = ?"],
        ["Tensor<[12, 64, 50]> self = ?", "Tensor<[12, 50, 50]> mat2 = ?"],
        ["Tensor<[8, 920, 920]> self = ?", "Tensor<[8, 920, 32]> mat2 = ?"],
        ["Tensor<[8, 100, 32]> self = ?", "Tensor<[8, 32, 100]> mat2 = ?"],
        ["Tensor<[8, 100, 100]> self = ?", "Tensor<[8, 100, 32]> mat2 = ?"],
        ["Tensor<[8, 100, 920]> self = ?", "Tensor<[8, 920, 32]> mat2 = ?"],
        ["Tensor<[12, 25, 64]> self = ?", "Tensor<[12, 64, 25]> mat2 = ?"],
        ["Tensor<[12, 25, 25]> self = ?", "Tensor<[12, 25, 64]> mat2 = ?"],
        ["Tensor<[6, 15, 64]> self = ?", "Tensor<[6, 64, 15]> mat2 = ?"],
        ["Tensor<[6, 15, 15]> self = ?", "Tensor<[6, 15, 64]> mat2 = ?"],
        ["Tensor<[6, 1, 64]> self = ?", "Tensor<[6, 64, 1]> mat2 = ?"],
        ["Tensor<[6, 1, 1]> self = ?", "Tensor<[6, 1, 64]> mat2 = ?"],
        ["Tensor<[6, 1, 64]> self = ?", "Tensor<[6, 64, 15]> mat2 = ?"],
        ["Tensor<[6, 1, 15]> self = ?", "Tensor<[6, 15, 64]> mat2 = ?"],
        ["Tensor<[6, 1, 64]> self = ?", "Tensor<[6, 64, 2]> mat2 = ?"],
        ["Tensor<[6, 1, 2]> self = ?", "Tensor<[6, 2, 64]> mat2 = ?"],
        ["Tensor<[6, 1, 64]> self = ?", "Tensor<[6, 64, s0 + 1]> mat2 = ?"],
        ["Tensor<[6, 1, s0 + 1]> self = ?", "Tensor<[6, s0 + 1, 64]> mat2 = ?"],
        ["Tensor<[6, 1, 64]> self = ?", "Tensor<[6, 64, 17]> mat2 = ?"],
        ["Tensor<[6, 1, 17]> self = ?", "Tensor<[6, 17, 64]> mat2 = ?"],
        ["Tensor<[1, 19200, 64]> self = ?", "Tensor<[1, 64, 300]> mat2 = ?"],
        ["Tensor<[1, 19200, 300]> self = ?", "Tensor<[1, 300, 64]> mat2 = ?"],
        ["Tensor<[2, 4800, 64]> self = ?", "Tensor<[2, 64, 300]> mat2 = ?"],
        ["Tensor<[2, 4800, 300]> self = ?", "Tensor<[2, 300, 64]> mat2 = ?"],
        ["Tensor<[5, 1200, 64]> self = ?", "Tensor<[5, 64, 300]> mat2 = ?"],
        ["Tensor<[5, 1200, 300]> self = ?", "Tensor<[5, 300, 64]> mat2 = ?"],
        ["Tensor<[8, 300, 64]> self = ?", "Tensor<[8, 64, 300]> mat2 = ?"],
        ["Tensor<[8, 300, 300]> self = ?", "Tensor<[8, 300, 64]> mat2 = ?"],
        ["Tensor<[12, 7, 64]> self = ?", "Tensor<[12, 64, 7]> mat2 = ?"],
        ["Tensor<[12, 7, 7]> self = ?", "Tensor<[12, 7, 64]> mat2 = ?"],
        ["Tensor<[12, 45, 64]> self = ?", "Tensor<[12, 64, 45]> mat2 = ?"],
        ["Tensor<[12, 45, 45]> self = ?", "Tensor<[12, 45, 64]> mat2 = ?"],
        ["Tensor<[12, 1, 64]> self = ?", "Tensor<[12, 64, 46]> mat2 = ?"],
        ["Tensor<[12, 1, 46]> self = ?", "Tensor<[12, 46, 64]> mat2 = ?"],
        ["Tensor<[12, 1, 64]> self = ?", "Tensor<[12, 64, s10 + 1]> mat2 = ?"],
        ["Tensor<[12, 1, s10 + 1]> self = ?", "Tensor<[12, s10 + 1, 64]> mat2 = ?"],
        ["Tensor<[1, 64, 1]> self = ?", "Tensor<[1, 1, 32]> mat2 = ?"],
        ["Tensor<[16, 59, 64]> self = ?", "Tensor<[16, 64, 59]> mat2 = ?"],
        ["Tensor<[16, 59, 59]> self = ?", "Tensor<[16, 59, 64]> mat2 = ?"],
        ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, 60]> mat2 = ?"],
        ["Tensor<[16, 1, 60]> self = ?", "Tensor<[16, 60, 64]> mat2 = ?"],
        ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, s10 + 1]> mat2 = ?"],
        ["Tensor<[16, 1, s10 + 1]> self = ?", "Tensor<[16, s10 + 1, 64]> mat2 = ?"],
        ["Tensor<[8, 256, 32]> self = ?", "Tensor<[8, 32, 2048]> mat2 = ?"],
        ["Tensor<[8, 256, 2048]> self = ?", "Tensor<[8, 2048, 160]> mat2 = ?"],
        ["Tensor<[8, 256, 32]> self = ?", "Tensor<[8, 32, 256]> mat2 = ?"],
        ["Tensor<[8, 256, 256]> self = ?", "Tensor<[8, 256, 160]> mat2 = ?"],
        ["Tensor<[8, 2048, 32]> self = ?", "Tensor<[8, 32, 256]> mat2 = ?"],
        ["Tensor<[8, 2048, 256]> self = ?", "Tensor<[8, 256, 96]> mat2 = ?"],
        ["Tensor<[12, 10, 64]> self = ?", "Tensor<[12, 64, 10]> mat2 = ?"],
        ["Tensor<[12, 10, 10]> self = ?", "Tensor<[12, 10, 64]> mat2 = ?"],
        ["Tensor<[1, 16384, 32]> self = ?", "Tensor<[1, 32, 256]> mat2 = ?"],
        ["Tensor<[1, 16384, 256]> self = ?", "Tensor<[1, 256, 32]> mat2 = ?"],
        ["Tensor<[2, 4096, 32]> self = ?", "Tensor<[2, 32, 256]> mat2 = ?"],
        ["Tensor<[2, 4096, 256]> self = ?", "Tensor<[2, 256, 32]> mat2 = ?"],
        ["Tensor<[5, 1024, 32]> self = ?", "Tensor<[5, 32, 256]> mat2 = ?"],
        ["Tensor<[5, 1024, 256]> self = ?", "Tensor<[5, 256, 32]> mat2 = ?"],
        ["Tensor<[8, 256, 256]> self = ?", "Tensor<[8, 256, 32]> mat2 = ?"],
        ["Tensor<[8, 32, 256]> self = ?", "Tensor<[8, 256, 256]> mat2 = ?"],
        ["Tensor<[5, 256, 1024]> self = ?", "Tensor<[5, 1024, 32]> mat2 = ?"],
        ["Tensor<[5, 32, 1024]> self = ?", "Tensor<[5, 1024, 256]> mat2 = ?"],
        ["Tensor<[2, 256, 4096]> self = ?", "Tensor<[2, 4096, 32]> mat2 = ?"],
        ["Tensor<[2, 32, 4096]> self = ?", "Tensor<[2, 4096, 256]> mat2 = ?"],
        ["Tensor<[1, 256, 16384]> self = ?", "Tensor<[1, 16384, 32]> mat2 = ?"],
        ["Tensor<[1, 32, 16384]> self = ?", "Tensor<[1, 16384, 256]> mat2 = ?"],
        ["Tensor<[16, 19, 64]> self = ?", "Tensor<[16, 64, 19]> mat2 = ?"],
        ["Tensor<[16, 19, 19]> self = ?", "Tensor<[16, 19, 64]> mat2 = ?"],
        ["Tensor<[3, 1445, 64]> self = ?", "Tensor<[3, 64, 1445]> mat2 = ?"],
        ["Tensor<[3, 1445, 1445]> self = ?", "Tensor<[3, 1445, 64]> mat2 = ?"],
        ["Tensor<[12, 9, 64]> self = ?", "Tensor<[12, 64, 9]> mat2 = ?"],
        ["Tensor<[12, 9, 9]> self = ?", "Tensor<[12, 9, 64]> mat2 = ?"],
        ["Tensor<[12, 12, 64]> self = ?", "Tensor<[12, 64, 12]> mat2 = ?"],
        ["Tensor<[12, 12, 12]> self = ?", "Tensor<[12, 12, 64]> mat2 = ?"],
        ["Tensor<[16, 9, 64]> self = ?", "Tensor<[16, 64, 9]> mat2 = ?"],
        ["Tensor<[16, 9, 9]> self = ?", "Tensor<[16, 9, 64]> mat2 = ?"],
        ["Tensor<[16, 9, 128]> self = ?", "Tensor<[16, 128, 9]> mat2 = ?"],
        ["Tensor<[16, 9, 9]> self = ?", "Tensor<[16, 9, 128]> mat2 = ?"],
        ["Tensor<[64, 9, 64]> self = ?", "Tensor<[64, 64, 9]> mat2 = ?"],
        ["Tensor<[64, 9, 9]> self = ?", "Tensor<[64, 9, 64]> mat2 = ?"],
        ["Tensor<[16, 5, 64]> self = ?", "Tensor<[16, 64, 5]> mat2 = ?"],
        ["Tensor<[16, 5, 5]> self = ?", "Tensor<[16, 5, 64]> mat2 = ?"],
        ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, 6]> mat2 = ?"],
        ["Tensor<[16, 1, 6]> self = ?", "Tensor<[16, 6, 64]> mat2 = ?"],
        ["Tensor<[12, 16, 64]> self = ?", "Tensor<[12, 64, 16]> mat2 = ?"],
        ["Tensor<[12, 16, 16]> self = ?", "Tensor<[12, 16, 64]> mat2 = ?"],
        ["Tensor<[12, 197, 64]> self = ?", "Tensor<[12, 64, 197]> mat2 = ?"],
        ["Tensor<[12, 197, 197]> self = ?", "Tensor<[12, 197, 64]> mat2 = ?"],
        ["Tensor<[12, 64, 197]> self = ?", "Tensor<[12, 197, 197]> mat2 = ?"],
        ["Tensor<[16, 197, 64]> self = ?", "Tensor<[16, 64, 197]> mat2 = ?"],
        ["Tensor<[16, 197, 197]> self = ?", "Tensor<[16, 197, 64]> mat2 = ?"],
        ["Tensor<[16, 64, 197]> self = ?", "Tensor<[16, 197, 197]> mat2 = ?"],
        ["Tensor<[12, 24, 64]> self = ?", "Tensor<[12, 64, 24]> mat2 = ?"],
        ["Tensor<[24, 12, 64]> self = ?", "Tensor<[24, 64, 24]> mat2 = ?"],
        ["Tensor<[12, 24, 24]> self = ?", "Tensor<[12, 24, 64]> mat2 = ?"],
        ["Tensor<[256, 49, 32]> self = ?", "Tensor<[256, 32, 49]> mat2 = ?"],
        ["Tensor<[256, 49, 49]> self = ?", "Tensor<[256, 49, 32]> mat2 = ?"],
        ["Tensor<[128, 49, 32]> self = ?", "Tensor<[128, 32, 49]> mat2 = ?"],
        ["Tensor<[128, 49, 49]> self = ?", "Tensor<[128, 49, 32]> mat2 = ?"],
        ["Tensor<[64, 49, 32]> self = ?", "Tensor<[64, 32, 49]> mat2 = ?"],
        ["Tensor<[64, 49, 49]> self = ?", "Tensor<[64, 49, 32]> mat2 = ?"],
        ["Tensor<[32, 49, 32]> self = ?", "Tensor<[32, 32, 49]> mat2 = ?"],
        ["Tensor<[32, 49, 49]> self = ?", "Tensor<[32, 49, 32]> mat2 = ?"],
        ["Tensor<[192, 49, 32]> self = ?", "Tensor<[192, 32, 49]> mat2 = ?"],
        ["Tensor<[192, 49, 49]> self = ?", "Tensor<[192, 49, 32]> mat2 = ?"],
        ["Tensor<[96, 49, 32]> self = ?", "Tensor<[96, 32, 49]> mat2 = ?"],
        ["Tensor<[96, 49, 49]> self = ?", "Tensor<[96, 49, 32]> mat2 = ?"],
        ["Tensor<[48, 49, 32]> self = ?", "Tensor<[48, 32, 49]> mat2 = ?"],
        ["Tensor<[48, 49, 49]> self = ?", "Tensor<[48, 49, 32]> mat2 = ?"],
        ["Tensor<[24, 49, 32]> self = ?", "Tensor<[24, 32, 49]> mat2 = ?"],
        ["Tensor<[24, 49, 49]> self = ?", "Tensor<[24, 49, 32]> mat2 = ?"],
        ["Tensor<[256, 64, 32]> self = ?", "Tensor<[256, 32, 64]> mat2 = ?"],
        ["Tensor<[256, 64, 64]> self = ?", "Tensor<[256, 64, 32]> mat2 = ?"],
        ["Tensor<[128, 64, 32]> self = ?", "Tensor<[128, 32, 64]> mat2 = ?"],
        ["Tensor<[128, 64, 64]> self = ?", "Tensor<[128, 64, 32]> mat2 = ?"],
        ["Tensor<[64, 64, 32]> self = ?", "Tensor<[64, 32, 64]> mat2 = ?"],
        ["Tensor<[64, 64, 64]> self = ?", "Tensor<[64, 64, 32]> mat2 = ?"],
        ["Tensor<[32, 64, 32]> self = ?", "Tensor<[32, 32, 64]> mat2 = ?"],
        ["Tensor<[32, 64, 64]> self = ?", "Tensor<[32, 64, 32]> mat2 = ?"],
        ["Tensor<[192, 64, 32]> self = ?", "Tensor<[192, 32, 64]> mat2 = ?"],
        ["Tensor<[192, 64, 64]> self = ?", "Tensor<[192, 64, 32]> mat2 = ?"],
        ["Tensor<[96, 64, 32]> self = ?", "Tensor<[96, 32, 64]> mat2 = ?"],
        ["Tensor<[96, 64, 64]> self = ?", "Tensor<[96, 64, 32]> mat2 = ?"],
        ["Tensor<[48, 64, 32]> self = ?", "Tensor<[48, 32, 64]> mat2 = ?"],
        ["Tensor<[48, 64, 64]> self = ?", "Tensor<[48, 64, 32]> mat2 = ?"],
        ["Tensor<[24, 64, 32]> self = ?", "Tensor<[24, 32, 64]> mat2 = ?"],
        ["Tensor<[24, 64, 64]> self = ?", "Tensor<[24, 64, 32]> mat2 = ?"],
        ["Tensor<[12, 1, 64]> self = ?", "Tensor<[12, 64, 1]> mat2 = ?"],
        ["Tensor<[12, 1, 1]> self = ?", "Tensor<[12, 1, 64]> mat2 = ?"],
        ["Tensor<[12, 1, 64]> self = ?", "Tensor<[12, 64, 10]> mat2 = ?"],
        ["Tensor<[12, 1, 10]> self = ?", "Tensor<[12, 10, 64]> mat2 = ?"],
        ["Tensor<[12, 1, 64]> self = ?", "Tensor<[12, 64, 2]> mat2 = ?"],
        ["Tensor<[12, 1, 2]> self = ?", "Tensor<[12, 2, 64]> mat2 = ?"],
        ["Tensor<[12, 1, 64]> self = ?", "Tensor<[12, 64, s0 + 1]> mat2 = ?"],
        ["Tensor<[12, 1, s0 + 1]> self = ?", "Tensor<[12, s0 + 1, 64]> mat2 = ?"],
        ["Tensor<[16, 10, 64]> self = ?", "Tensor<[16, 64, 10]> mat2 = ?"],
        ["Tensor<[16, 10, 10]> self = ?", "Tensor<[16, 10, 64]> mat2 = ?"],
        ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, 1]> mat2 = ?"],
        ["Tensor<[16, 1, 1]> self = ?", "Tensor<[16, 1, 64]> mat2 = ?"],
        ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, 10]> mat2 = ?"],
        ["Tensor<[16, 1, 10]> self = ?", "Tensor<[16, 10, 64]> mat2 = ?"],
        ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, 2]> mat2 = ?"],
        ["Tensor<[16, 1, 2]> self = ?", "Tensor<[16, 2, 64]> mat2 = ?"],
        ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, s0 + 1]> mat2 = ?"],
        ["Tensor<[16, 1, s0 + 1]> self = ?", "Tensor<[16, s0 + 1, 64]> mat2 = ?"],
        ["Tensor<[8, 10, 64]> self = ?", "Tensor<[8, 64, 10]> mat2 = ?"],
        ["Tensor<[8, 10, 10]> self = ?", "Tensor<[8, 10, 64]> mat2 = ?"],
        ["Tensor<[8, 1, 64]> self = ?", "Tensor<[8, 64, 1]> mat2 = ?"],
        ["Tensor<[8, 1, 1]> self = ?", "Tensor<[8, 1, 64]> mat2 = ?"],
        ["Tensor<[8, 1, 64]> self = ?", "Tensor<[8, 64, 10]> mat2 = ?"],
        ["Tensor<[8, 1, 10]> self = ?", "Tensor<[8, 10, 64]> mat2 = ?"],
        ["Tensor<[8, 1, 64]> self = ?", "Tensor<[8, 64, 2]> mat2 = ?"],
        ["Tensor<[8, 1, 2]> self = ?", "Tensor<[8, 2, 64]> mat2 = ?"],
        ["Tensor<[8, 1, 64]> self = ?", "Tensor<[8, 64, s0 + 1]> mat2 = ?"],
        ["Tensor<[8, 1, s0 + 1]> self = ?", "Tensor<[8, s0 + 1, 64]> mat2 = ?"],
        ["Tensor<[12, 14, 64]> self = ?", "Tensor<[12, 64, 14]> mat2 = ?"],
        ["Tensor<[12, 14, 14]> self = ?", "Tensor<[12, 14, 64]> mat2 = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.bmm.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.bmm.default", input_strings)
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
