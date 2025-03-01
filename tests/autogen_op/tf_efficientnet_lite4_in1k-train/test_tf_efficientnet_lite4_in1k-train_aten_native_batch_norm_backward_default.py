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
        return torch.ops.aten.native_batch_norm_backward.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(
        metrics, "metrics-autogen-op/tf_efficientnet_lite4.in1k-train", "aten.native_batch_norm_backward.default"
    )


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 1280, 12, 12]> grad_out = ?",
            "Tensor<[1, 1280, 12, 12]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> running_mean = ?",
            "Optional[Tensor]<[1280]> running_var = ?",
            "Optional[Tensor]<[1280]> save_mean = ?",
            "Optional[Tensor]<[1280]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 448, 12, 12]> grad_out = ?",
            "Tensor<[1, 448, 12, 12]> input = ?",
            "Optional[Tensor]<[448]> weight = ?",
            "Optional[Tensor]<[448]> running_mean = ?",
            "Optional[Tensor]<[448]> running_var = ?",
            "Optional[Tensor]<[448]> save_mean = ?",
            "Optional[Tensor]<[448]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 1632, 12, 12]> grad_out = ?",
            "Tensor<[1, 1632, 12, 12]> input = ?",
            "Optional[Tensor]<[1632]> weight = ?",
            "Optional[Tensor]<[1632]> running_mean = ?",
            "Optional[Tensor]<[1632]> running_var = ?",
            "Optional[Tensor]<[1632]> save_mean = ?",
            "Optional[Tensor]<[1632]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 272, 12, 12]> grad_out = ?",
            "Tensor<[1, 272, 12, 12]> input = ?",
            "Optional[Tensor]<[272]> weight = ?",
            "Optional[Tensor]<[272]> running_mean = ?",
            "Optional[Tensor]<[272]> running_var = ?",
            "Optional[Tensor]<[272]> save_mean = ?",
            "Optional[Tensor]<[272]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 960, 12, 12]> grad_out = ?",
            "Tensor<[1, 960, 12, 12]> input = ?",
            "Optional[Tensor]<[960]> weight = ?",
            "Optional[Tensor]<[960]> running_mean = ?",
            "Optional[Tensor]<[960]> running_var = ?",
            "Optional[Tensor]<[960]> save_mean = ?",
            "Optional[Tensor]<[960]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 960, 24, 24]> grad_out = ?",
            "Tensor<[1, 960, 24, 24]> input = ?",
            "Optional[Tensor]<[960]> weight = ?",
            "Optional[Tensor]<[960]> running_mean = ?",
            "Optional[Tensor]<[960]> running_var = ?",
            "Optional[Tensor]<[960]> save_mean = ?",
            "Optional[Tensor]<[960]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 160, 24, 24]> grad_out = ?",
            "Tensor<[1, 160, 24, 24]> input = ?",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> running_mean = ?",
            "Optional[Tensor]<[160]> running_var = ?",
            "Optional[Tensor]<[160]> save_mean = ?",
            "Optional[Tensor]<[160]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 672, 24, 24]> grad_out = ?",
            "Tensor<[1, 672, 24, 24]> input = ?",
            "Optional[Tensor]<[672]> weight = ?",
            "Optional[Tensor]<[672]> running_mean = ?",
            "Optional[Tensor]<[672]> running_var = ?",
            "Optional[Tensor]<[672]> save_mean = ?",
            "Optional[Tensor]<[672]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 112, 24, 24]> grad_out = ?",
            "Tensor<[1, 112, 24, 24]> input = ?",
            "Optional[Tensor]<[112]> weight = ?",
            "Optional[Tensor]<[112]> running_mean = ?",
            "Optional[Tensor]<[112]> running_var = ?",
            "Optional[Tensor]<[112]> save_mean = ?",
            "Optional[Tensor]<[112]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 336, 24, 24]> grad_out = ?",
            "Tensor<[1, 336, 24, 24]> input = ?",
            "Optional[Tensor]<[336]> weight = ?",
            "Optional[Tensor]<[336]> running_mean = ?",
            "Optional[Tensor]<[336]> running_var = ?",
            "Optional[Tensor]<[336]> save_mean = ?",
            "Optional[Tensor]<[336]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 336, 48, 48]> grad_out = ?",
            "Tensor<[1, 336, 48, 48]> input = ?",
            "Optional[Tensor]<[336]> weight = ?",
            "Optional[Tensor]<[336]> running_mean = ?",
            "Optional[Tensor]<[336]> running_var = ?",
            "Optional[Tensor]<[336]> save_mean = ?",
            "Optional[Tensor]<[336]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 56, 48, 48]> grad_out = ?",
            "Tensor<[1, 56, 48, 48]> input = ?",
            "Optional[Tensor]<[56]> weight = ?",
            "Optional[Tensor]<[56]> running_mean = ?",
            "Optional[Tensor]<[56]> running_var = ?",
            "Optional[Tensor]<[56]> save_mean = ?",
            "Optional[Tensor]<[56]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 192, 48, 48]> grad_out = ?",
            "Tensor<[1, 192, 48, 48]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> running_mean = ?",
            "Optional[Tensor]<[192]> running_var = ?",
            "Optional[Tensor]<[192]> save_mean = ?",
            "Optional[Tensor]<[192]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 192, 95, 95]> grad_out = ?",
            "Tensor<[1, 192, 95, 95]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> running_mean = ?",
            "Optional[Tensor]<[192]> running_var = ?",
            "Optional[Tensor]<[192]> save_mean = ?",
            "Optional[Tensor]<[192]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 32, 95, 95]> grad_out = ?",
            "Tensor<[1, 32, 95, 95]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> running_mean = ?",
            "Optional[Tensor]<[32]> running_var = ?",
            "Optional[Tensor]<[32]> save_mean = ?",
            "Optional[Tensor]<[32]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 144, 95, 95]> grad_out = ?",
            "Tensor<[1, 144, 95, 95]> input = ?",
            "Optional[Tensor]<[144]> weight = ?",
            "Optional[Tensor]<[144]> running_mean = ?",
            "Optional[Tensor]<[144]> running_var = ?",
            "Optional[Tensor]<[144]> save_mean = ?",
            "Optional[Tensor]<[144]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 144, 190, 190]> grad_out = ?",
            "Tensor<[1, 144, 190, 190]> input = ?",
            "Optional[Tensor]<[144]> weight = ?",
            "Optional[Tensor]<[144]> running_mean = ?",
            "Optional[Tensor]<[144]> running_var = ?",
            "Optional[Tensor]<[144]> save_mean = ?",
            "Optional[Tensor]<[144]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 24, 190, 190]> grad_out = ?",
            "Tensor<[1, 24, 190, 190]> input = ?",
            "Optional[Tensor]<[24]> weight = ?",
            "Optional[Tensor]<[24]> running_mean = ?",
            "Optional[Tensor]<[24]> running_var = ?",
            "Optional[Tensor]<[24]> save_mean = ?",
            "Optional[Tensor]<[24]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 32, 190, 190]> grad_out = ?",
            "Tensor<[1, 32, 190, 190]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> running_mean = ?",
            "Optional[Tensor]<[32]> running_var = ?",
            "Optional[Tensor]<[32]> save_mean = ?",
            "Optional[Tensor]<[32]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.native_batch_norm_backward.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.native_batch_norm_backward.default", input_strings
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
