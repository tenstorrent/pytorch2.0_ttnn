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
        return torch.ops.aten.threshold_backward.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.threshold_backward.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 16, 14, 14]> grad_output = ?", "Tensor<[1, 16, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 4, 14, 14]> grad_output = ?", "Tensor<[1, 4, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 16, 28, 28]> grad_output = ?", "Tensor<[1, 16, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128]> grad_output = ?", "Tensor<[1, 128]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64]> grad_output = ?", "Tensor<[1, 64]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 12]> grad_output = ?", "Tensor<[1, 12]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 24, 24]> grad_output = ?", "Tensor<[1, 64, 24, 24]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 32, 26, 26]> grad_output = ?", "Tensor<[1, 32, 26, 26]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128, 28, 28]> grad_output = ?", "Tensor<[1, 128, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 512, 28, 28]> grad_output = ?", "Tensor<[1, 512, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 28, 28]> grad_output = ?", "Tensor<[1, 256, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128, 56, 56]> grad_output = ?", "Tensor<[1, 128, 56, 56]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 56, 56]> grad_output = ?", "Tensor<[1, 64, 56, 56]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 112, 112]> grad_output = ?", "Tensor<[1, 64, 112, 112]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 32, 112, 112]> grad_output = ?", "Tensor<[1, 32, 112, 112]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 512, 7, 7]> grad_output = ?", "Tensor<[1, 512, 7, 7]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 14, 14]> grad_output = ?", "Tensor<[1, 256, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 2048, 7, 7]> grad_output = ?", "Tensor<[1, 2048, 7, 7]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 512, 14, 14]> grad_output = ?", "Tensor<[1, 512, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 1024, 14, 14]> grad_output = ?", "Tensor<[1, 1024, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 56, 56]> grad_output = ?", "Tensor<[1, 256, 56, 56]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 128, 128]> grad_output = ?", "Tensor<[1, 256, 128, 128]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 32, 256, 256]> grad_output = ?", "Tensor<[1, 32, 256, 256]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 128, 128]> grad_output = ?", "Tensor<[1, 64, 128, 128]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128, 64, 64]> grad_output = ?", "Tensor<[1, 128, 64, 64]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 32, 32]> grad_output = ?", "Tensor<[1, 256, 32, 32]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 512, 16, 16]> grad_output = ?", "Tensor<[1, 512, 16, 16]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 224, 224]> grad_output = ?", "Tensor<[1, 64, 224, 224]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128, 112, 112]> grad_output = ?", "Tensor<[1, 128, 112, 112]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 16, 224, 224]> grad_output = ?", "Tensor<[1, 16, 224, 224]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 1024, 7, 7]> grad_output = ?", "Tensor<[1, 1024, 7, 7]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 224, 7, 7]> grad_output = ?", "Tensor<[1, 224, 7, 7]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 768, 14, 14]> grad_output = ?", "Tensor<[1, 768, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 192, 14, 14]> grad_output = ?", "Tensor<[1, 192, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 160, 28, 28]> grad_output = ?", "Tensor<[1, 160, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 1280, 1, 1]> grad_output = ?", "Tensor<[1, 1280, 1, 1]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 960, 7, 7]> grad_output = ?", "Tensor<[1, 960, 7, 7]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 240, 1, 1]> grad_output = ?", "Tensor<[1, 240, 1, 1]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 480, 7, 7]> grad_output = ?", "Tensor<[1, 480, 7, 7]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 168, 1, 1]> grad_output = ?", "Tensor<[1, 168, 1, 1]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 336, 14, 14]> grad_output = ?", "Tensor<[1, 336, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 120, 1, 1]> grad_output = ?", "Tensor<[1, 120, 1, 1]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 240, 14, 14]> grad_output = ?", "Tensor<[1, 240, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 92, 14, 14]> grad_output = ?", "Tensor<[1, 92, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 100, 14, 14]> grad_output = ?", "Tensor<[1, 100, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 120, 28, 28]> grad_output = ?", "Tensor<[1, 120, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 32, 1, 1]> grad_output = ?", "Tensor<[1, 32, 1, 1]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 60, 28, 28]> grad_output = ?", "Tensor<[1, 60, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 20, 1, 1]> grad_output = ?", "Tensor<[1, 20, 1, 1]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 36, 56, 56]> grad_output = ?", "Tensor<[1, 36, 56, 56]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 24, 112, 112]> grad_output = ?", "Tensor<[1, 24, 112, 112]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 8, 112, 112]> grad_output = ?", "Tensor<[1, 8, 112, 112]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 16, 112, 112]> grad_output = ?", "Tensor<[1, 16, 112, 112]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 7, 7]> grad_output = ?", "Tensor<[1, 256, 7, 7]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128, 14, 14]> grad_output = ?", "Tensor<[1, 128, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 28, 28]> grad_output = ?", "Tensor<[1, 64, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 32, 56, 56]> grad_output = ?", "Tensor<[1, 32, 56, 56]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 144, 7, 7]> grad_output = ?", "Tensor<[1, 144, 7, 7]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 36, 14, 14]> grad_output = ?", "Tensor<[1, 36, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 18, 14, 14]> grad_output = ?", "Tensor<[1, 18, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 18, 28, 28]> grad_output = ?", "Tensor<[1, 18, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 72, 14, 14]> grad_output = ?", "Tensor<[1, 72, 14, 14]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 36, 28, 28]> grad_output = ?", "Tensor<[1, 36, 28, 28]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 18, 56, 56]> grad_output = ?", "Tensor<[1, 18, 56, 56]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 8, 8]> grad_output = ?", "Tensor<[1, 256, 8, 8]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 512, 8, 8]> grad_output = ?", "Tensor<[1, 512, 8, 8]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 448, 8, 8]> grad_output = ?", "Tensor<[1, 448, 8, 8]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 384, 8, 8]> grad_output = ?", "Tensor<[1, 384, 8, 8]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 320, 8, 8]> grad_output = ?", "Tensor<[1, 320, 8, 8]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 320, 17, 17]> grad_output = ?", "Tensor<[1, 320, 17, 17]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 17, 17]> grad_output = ?", "Tensor<[1, 256, 17, 17]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 192, 8, 8]> grad_output = ?", "Tensor<[1, 192, 8, 8]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 192, 17, 17]> grad_output = ?", "Tensor<[1, 192, 17, 17]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128, 17, 17]> grad_output = ?", "Tensor<[1, 128, 17, 17]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 224, 17, 17]> grad_output = ?", "Tensor<[1, 224, 17, 17]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 384, 17, 17]> grad_output = ?", "Tensor<[1, 384, 17, 17]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 224, 35, 35]> grad_output = ?", "Tensor<[1, 224, 35, 35]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 192, 35, 35]> grad_output = ?", "Tensor<[1, 192, 35, 35]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 96, 35, 35]> grad_output = ?", "Tensor<[1, 96, 35, 35]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 35, 35]> grad_output = ?", "Tensor<[1, 64, 35, 35]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 96, 71, 71]> grad_output = ?", "Tensor<[1, 96, 71, 71]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 73, 73]> grad_output = ?", "Tensor<[1, 64, 73, 73]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 96, 73, 73]> grad_output = ?", "Tensor<[1, 96, 73, 73]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 147, 147]> grad_output = ?", "Tensor<[1, 64, 147, 147]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 32, 147, 147]> grad_output = ?", "Tensor<[1, 32, 147, 147]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 32, 149, 149]> grad_output = ?", "Tensor<[1, 32, 149, 149]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 2048, 10, 10]> grad_output = ?", "Tensor<[1, 2048, 10, 10]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 1536, 10, 10]> grad_output = ?", "Tensor<[1, 1536, 10, 10]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 1024, 10, 10]> grad_output = ?", "Tensor<[1, 1024, 10, 10]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 1024, 19, 19]> grad_output = ?", "Tensor<[1, 1024, 19, 19]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 728, 19, 19]> grad_output = ?", "Tensor<[1, 728, 19, 19]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 728, 38, 38]> grad_output = ?", "Tensor<[1, 728, 38, 38]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 38, 38]> grad_output = ?", "Tensor<[1, 256, 38, 38]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 256, 75, 75]> grad_output = ?", "Tensor<[1, 256, 75, 75]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128, 75, 75]> grad_output = ?", "Tensor<[1, 128, 75, 75]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 128, 150, 150]> grad_output = ?", "Tensor<[1, 128, 150, 150]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 64, 150, 150]> grad_output = ?", "Tensor<[1, 64, 150, 150]> self = ?", "number threshold = 0"],
        ["Tensor<[1, 32, 150, 150]> grad_output = ?", "Tensor<[1, 32, 150, 150]> self = ?", "number threshold = 0"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.threshold_backward.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.threshold_backward.default", input_strings
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
