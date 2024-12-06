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
        return torch.ops.aten._native_batch_norm_legit_functional.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/HardNet-train", "aten._native_batch_norm_legit_functional.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 32, 112, 112]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "Tensor<[32]> running_mean = ?",
            "Tensor<[32]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 64, 112, 112]> input = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "Tensor<[64]> running_mean = ?",
            "Tensor<[64]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 14, 56, 56]> input = ?",
            "Optional[Tensor]<[14]> weight = ?",
            "Optional[Tensor]<[14]> bias = ?",
            "Tensor<[14]> running_mean = ?",
            "Tensor<[14]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 24, 56, 56]> input = ?",
            "Optional[Tensor]<[24]> weight = ?",
            "Optional[Tensor]<[24]> bias = ?",
            "Tensor<[24]> running_mean = ?",
            "Tensor<[24]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 40, 56, 56]> input = ?",
            "Optional[Tensor]<[40]> weight = ?",
            "Optional[Tensor]<[40]> bias = ?",
            "Tensor<[40]> running_mean = ?",
            "Tensor<[40]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 68, 56, 56]> input = ?",
            "Optional[Tensor]<[68]> weight = ?",
            "Optional[Tensor]<[68]> bias = ?",
            "Tensor<[68]> running_mean = ?",
            "Tensor<[68]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 128, 56, 56]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "Tensor<[128]> running_mean = ?",
            "Tensor<[128]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 16, 28, 28]> input = ?",
            "Optional[Tensor]<[16]> weight = ?",
            "Optional[Tensor]<[16]> bias = ?",
            "Tensor<[16]> running_mean = ?",
            "Tensor<[16]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 28, 28, 28]> input = ?",
            "Optional[Tensor]<[28]> weight = ?",
            "Optional[Tensor]<[28]> bias = ?",
            "Tensor<[28]> running_mean = ?",
            "Tensor<[28]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 46, 28, 28]> input = ?",
            "Optional[Tensor]<[46]> weight = ?",
            "Optional[Tensor]<[46]> bias = ?",
            "Tensor<[46]> running_mean = ?",
            "Tensor<[46]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 78, 28, 28]> input = ?",
            "Optional[Tensor]<[78]> weight = ?",
            "Optional[Tensor]<[78]> bias = ?",
            "Tensor<[78]> running_mean = ?",
            "Tensor<[78]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 134, 28, 28]> input = ?",
            "Optional[Tensor]<[134]> weight = ?",
            "Optional[Tensor]<[134]> bias = ?",
            "Tensor<[134]> running_mean = ?",
            "Tensor<[134]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 28, 28]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "Tensor<[256]> running_mean = ?",
            "Tensor<[256]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 20, 28, 28]> input = ?",
            "Optional[Tensor]<[20]> weight = ?",
            "Optional[Tensor]<[20]> bias = ?",
            "Tensor<[20]> running_mean = ?",
            "Tensor<[20]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 34, 28, 28]> input = ?",
            "Optional[Tensor]<[34]> weight = ?",
            "Optional[Tensor]<[34]> bias = ?",
            "Tensor<[34]> running_mean = ?",
            "Tensor<[34]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 58, 28, 28]> input = ?",
            "Optional[Tensor]<[58]> weight = ?",
            "Optional[Tensor]<[58]> bias = ?",
            "Tensor<[58]> running_mean = ?",
            "Tensor<[58]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 98, 28, 28]> input = ?",
            "Optional[Tensor]<[98]> weight = ?",
            "Optional[Tensor]<[98]> bias = ?",
            "Tensor<[98]> running_mean = ?",
            "Tensor<[98]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 168, 28, 28]> input = ?",
            "Optional[Tensor]<[168]> weight = ?",
            "Optional[Tensor]<[168]> bias = ?",
            "Tensor<[168]> running_mean = ?",
            "Tensor<[168]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 320, 28, 28]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "Tensor<[320]> running_mean = ?",
            "Tensor<[320]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 40, 14, 14]> input = ?",
            "Optional[Tensor]<[40]> weight = ?",
            "Optional[Tensor]<[40]> bias = ?",
            "Tensor<[40]> running_mean = ?",
            "Tensor<[40]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 68, 14, 14]> input = ?",
            "Optional[Tensor]<[68]> weight = ?",
            "Optional[Tensor]<[68]> bias = ?",
            "Tensor<[68]> running_mean = ?",
            "Tensor<[68]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 116, 14, 14]> input = ?",
            "Optional[Tensor]<[116]> weight = ?",
            "Optional[Tensor]<[116]> bias = ?",
            "Tensor<[116]> running_mean = ?",
            "Tensor<[116]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 196, 14, 14]> input = ?",
            "Optional[Tensor]<[196]> weight = ?",
            "Optional[Tensor]<[196]> bias = ?",
            "Tensor<[196]> running_mean = ?",
            "Tensor<[196]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 334, 14, 14]> input = ?",
            "Optional[Tensor]<[334]> weight = ?",
            "Optional[Tensor]<[334]> bias = ?",
            "Tensor<[334]> running_mean = ?",
            "Tensor<[334]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 640, 14, 14]> input = ?",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> bias = ?",
            "Tensor<[640]> running_mean = ?",
            "Tensor<[640]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 160, 7, 7]> input = ?",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> bias = ?",
            "Tensor<[160]> running_mean = ?",
            "Tensor<[160]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 272, 7, 7]> input = ?",
            "Optional[Tensor]<[272]> weight = ?",
            "Optional[Tensor]<[272]> bias = ?",
            "Tensor<[272]> running_mean = ?",
            "Tensor<[272]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 462, 7, 7]> input = ?",
            "Optional[Tensor]<[462]> weight = ?",
            "Optional[Tensor]<[462]> bias = ?",
            "Tensor<[462]> running_mean = ?",
            "Tensor<[462]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1024, 7, 7]> input = ?",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "Tensor<[1024]> running_mean = ?",
            "Tensor<[1024]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._native_batch_norm_legit_functional.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._native_batch_norm_legit_functional.default", input_strings
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
