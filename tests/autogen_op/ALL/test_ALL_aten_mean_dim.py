# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
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
        return torch.ops.aten.mean.dim(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.mean.dim")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 15, 512]> self = ?", "Optional[List[int]] dim = [-1]", "bool keepdim = True"],
        ["Tensor<[1, 1, 512]> self = ?", "Optional[List[int]] dim = [-1]", "bool keepdim = True"],
        ["Tensor<[1, 1024, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 512, 256]> self = ?", "Optional[List[int]] dim = [2]"],
        ["Tensor<[1, 72, 40, 40]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 120, 40, 40]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 480, 20, 20]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 672, 20, 20]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 672, 10, 10]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 480, 10, 10]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1280, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 512, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 2048, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 2208, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1664, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1920, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 256, 56, 56]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 512, 28, 28]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 768, 14, 14]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 1024, 7, 7]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 72, 28, 28]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 120, 28, 28]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 672, 7, 7]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "Optional[List[int]] dim = [2, 3]", "bool keepdim = True"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1536, 8, 8]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 196, 768]> self = ?", "Optional[List[int]] dim = [1]"],
        ["Tensor<[1, 196, 1024]> self = ?", "Optional[List[int]] dim = [1]"],
        ["Tensor<[1, 72, 28, 28]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 120, 28, 28]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 672, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 16, 56, 56]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 96, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 240, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 120, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 144, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 288, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 576, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 912, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 2520, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1008, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 400, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 528, 96, 96]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1056, 48, 48]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 2904, 24, 24]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 7392, 12, 12]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 224, 56, 56]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 448, 28, 28]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1232, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 3024, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 48, 56, 56]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 336, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 888, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 232, 56, 56]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 696, 28, 28]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1392, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 3712, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 72, 56, 56]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 216, 28, 28]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 576, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1512, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 104, 28, 28]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 208, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 440, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 64, 56, 56]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 144, 28, 28]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 320, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 784, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 896, 14, 14]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 2016, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 768, 7, 7]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1024, 8, 8]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 768, 8, 8]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 10, 768]> self = ?", "Optional[List[int]] dim = [-1]", "bool keepdim = True"],
        ["Tensor<[1, 1, 768]> self = ?", "Optional[List[int]] dim = [-1]", "bool keepdim = True"],
        ["Tensor<[1, 10, 1024]> self = ?", "Optional[List[int]] dim = [-1]", "bool keepdim = True"],
        ["Tensor<[1, 1, 1024]> self = ?", "Optional[List[int]] dim = [-1]", "bool keepdim = True"],
        ["Tensor<[1, 10, 512]> self = ?", "Optional[List[int]] dim = [-1]", "bool keepdim = True"],
        ["Tensor<[1, 1280, 8, 8]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1280, 9, 9]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1280, 10, 10]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 1280, 12, 12]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
        ["Tensor<[1, 2048, 10, 10]> self = ?", "Optional[List[int]] dim = [-1, -2]", "bool keepdim = True"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.mean.dim",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.mean.dim", input_strings)
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
