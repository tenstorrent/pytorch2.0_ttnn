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
        return torch.ops.aten.embedding.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.embedding.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[30522, 1024]> weight = ?", "Tensor<[1, 256]> indices = ?", "int padding_idx = 0"],
        ["Tensor<[2, 1024]> weight = ?", "Tensor<[1, 256]> indices = ?"],
        ["Tensor<[512, 1024]> weight = ?", "Tensor<[1, 256]> indices = ?"],
        ["Tensor<[250880, 1536]> weight = ?", "Tensor<[1, 32]> indices = ?"],
        ["Tensor<[50, 768]> weight = ?", "Tensor<[1, 50]> indices = ?"],
        ["Tensor<[49408, 512]> weight = ?", "Tensor<[2, 7]> indices = ?"],
        ["Tensor<[77, 512]> weight = ?", "Tensor<[1, 7]> indices = ?"],
        ["Tensor<[30522, 768]> weight = ?", "Tensor<[1, 25]> indices = ?", "int padding_idx = 0"],
        ["Tensor<[2, 768]> weight = ?", "Tensor<[1, 25]> indices = ?"],
        ["Tensor<[512, 768]> weight = ?", "Tensor<[1, 25]> indices = ?"],
        ["Tensor<[32128, 512]> weight = ?", "Tensor<[1, 15]> indices = ?"],
        ["Tensor<[32, 6]> weight = ?", "Tensor<[15, 15]> indices = ?"],
        ["Tensor<[32128, 512]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[32, 6]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[32, 6]> weight = ?", "Tensor<[2, 2]> indices = ?"],
        ["Tensor<[32, 6]> weight = ?", "Tensor<[s0 + 1, s0 + 1]> indices = ?"],
        ["Tensor<[32, 6]> weight = ?", "Tensor<[17, 17]> indices = ?"],
        ["Tensor<[65024, 4544]> weight = ?", "Tensor<[1, 7]> indices = ?"],
        ["Tensor<[50257, 768]> weight = ?", "Tensor<[1, 7]> indices = ?"],
        ["Tensor<[1024, 768]> weight = ?", "Tensor<[1, 7]> indices = ?"],
        ["Tensor<[50257, 768]> weight = ?", "Tensor<[1, 45]> indices = ?"],
        ["Tensor<[2048, 768]> weight = ?", "Tensor<[1, 45]> indices = ?"],
        ["Tensor<[50257, 768]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[2048, 768]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[32000, 4096]> weight = ?", "Tensor<[1, 32]> indices = ?", "int padding_idx = 0"],
        ["Tensor<[50272, 512]> weight = ?", "Tensor<[1, 59]> indices = ?", "int padding_idx = 1"],
        ["Tensor<[2050, 1024]> weight = ?", "Tensor<[1, 59]> indices = ?"],
        ["Tensor<[50272, 512]> weight = ?", "Tensor<[1, 1]> indices = ?", "int padding_idx = 1"],
        ["Tensor<[2050, 1024]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[262, 768]> weight = ?", "Tensor<[1, 2048]> indices = ?"],
        ["Tensor<[2048, 768]> weight = ?", "Tensor<[2048]> indices = ?"],
        ["Tensor<[250002, 768]> weight = ?", "Tensor<[1, 10]> indices = ?", "int padding_idx = 1"],
        ["Tensor<[1, 768]> weight = ?", "Tensor<[1, 10]> indices = ?"],
        ["Tensor<[514, 768]> weight = ?", "Tensor<[1, 10]> indices = ?", "int padding_idx = 1"],
        ["Tensor<[30528, 768]> weight = ?", "Tensor<[1, 8]> indices = ?", "int padding_idx = 0"],
        ["Tensor<[512, 768]> weight = ?", "Tensor<[1, 8]> indices = ?"],
        ["Tensor<[2, 768]> weight = ?", "Tensor<[1, 8]> indices = ?"],
        ["Tensor<[30522, 768]> weight = ?", "Tensor<[1, 8]> indices = ?"],
        ["Tensor<[40, 768]> weight = ?", "Tensor<[1, 8]> indices = ?"],
        ["Tensor<[51865, 768]> weight = ?", "Tensor<[1, 1]> indices = ?", "int padding_idx = 50257"],
        ["Tensor<[51865, 768]> weight = ?", "Tensor<[1, 4]> indices = ?", "int padding_idx = 50257"],
        ["Tensor<[256008, 1024]> weight = ?", "Tensor<[1, 19]> indices = ?", "int padding_idx = 1"],
        ["Tensor<[30000, 128]> weight = ?", "Tensor<[1, 9]> indices = ?", "int padding_idx = 0"],
        ["Tensor<[2, 128]> weight = ?", "Tensor<[1, 9]> indices = ?"],
        ["Tensor<[512, 128]> weight = ?", "Tensor<[1, 9]> indices = ?"],
        ["Tensor<[30000, 128]> weight = ?", "Tensor<[1, 12]> indices = ?", "int padding_idx = 0"],
        ["Tensor<[2, 128]> weight = ?", "Tensor<[1, 12]> indices = ?"],
        ["Tensor<[512, 128]> weight = ?", "Tensor<[1, 12]> indices = ?"],
        ["Tensor<[51200, 1024]> weight = ?", "Tensor<[1, 5]> indices = ?"],
        ["Tensor<[51200, 1024]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[30522, 768]> weight = ?", "Tensor<[1, 16]> indices = ?", "int padding_idx = 0"],
        ["Tensor<[512, 768]> weight = ?", "Tensor<[1, 16]> indices = ?"],
        ["Tensor<[81, 768]> weight = ?", "Tensor<[1, 24]> indices = ?", "int padding_idx = 1"],
        ["Tensor<[320, 64]> weight = ?", "Tensor<[24, 24]> indices = ?"],
        ["Tensor<[32128, 768]> weight = ?", "Tensor<[1, 10]> indices = ?"],
        ["Tensor<[32, 12]> weight = ?", "Tensor<[10, 10]> indices = ?"],
        ["Tensor<[32128, 768]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[32, 12]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[32, 12]> weight = ?", "Tensor<[2, 2]> indices = ?"],
        ["Tensor<[32, 12]> weight = ?", "Tensor<[s0 + 1, s0 + 1]> indices = ?"],
        ["Tensor<[32128, 1024]> weight = ?", "Tensor<[1, 10]> indices = ?"],
        ["Tensor<[32, 16]> weight = ?", "Tensor<[10, 10]> indices = ?"],
        ["Tensor<[32128, 1024]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[32, 16]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[32, 16]> weight = ?", "Tensor<[2, 2]> indices = ?"],
        ["Tensor<[32, 16]> weight = ?", "Tensor<[s0 + 1, s0 + 1]> indices = ?"],
        ["Tensor<[32128, 512]> weight = ?", "Tensor<[1, 10]> indices = ?"],
        ["Tensor<[32, 8]> weight = ?", "Tensor<[10, 10]> indices = ?"],
        ["Tensor<[32, 8]> weight = ?", "Tensor<[1, 1]> indices = ?"],
        ["Tensor<[32, 8]> weight = ?", "Tensor<[2, 2]> indices = ?"],
        ["Tensor<[32, 8]> weight = ?", "Tensor<[s0 + 1, s0 + 1]> indices = ?"],
        ["Tensor<[30000, 128]> weight = ?", "Tensor<[1, 14]> indices = ?", "int padding_idx = 0"],
        ["Tensor<[2, 128]> weight = ?", "Tensor<[1, 14]> indices = ?"],
        ["Tensor<[512, 128]> weight = ?", "Tensor<[1, 14]> indices = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.embedding.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.embedding.default", input_strings
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
