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
        metrics, "metrics-autogen-op/tf_efficientnet_lite2.in1k-train", "aten.native_batch_norm_backward.default"
    )


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 1280, 9, 9]> grad_out = ?",
            "Tensor<[1, 1280, 9, 9]> input = ?",
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
            "Tensor<[1, 352, 9, 9]> grad_out = ?",
            "Tensor<[1, 352, 9, 9]> input = ?",
            "Optional[Tensor]<[352]> weight = ?",
            "Optional[Tensor]<[352]> running_mean = ?",
            "Optional[Tensor]<[352]> running_var = ?",
            "Optional[Tensor]<[352]> save_mean = ?",
            "Optional[Tensor]<[352]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 1248, 9, 9]> grad_out = ?",
            "Tensor<[1, 1248, 9, 9]> input = ?",
            "Optional[Tensor]<[1248]> weight = ?",
            "Optional[Tensor]<[1248]> running_mean = ?",
            "Optional[Tensor]<[1248]> running_var = ?",
            "Optional[Tensor]<[1248]> save_mean = ?",
            "Optional[Tensor]<[1248]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 208, 9, 9]> grad_out = ?",
            "Tensor<[1, 208, 9, 9]> input = ?",
            "Optional[Tensor]<[208]> weight = ?",
            "Optional[Tensor]<[208]> running_mean = ?",
            "Optional[Tensor]<[208]> running_var = ?",
            "Optional[Tensor]<[208]> save_mean = ?",
            "Optional[Tensor]<[208]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 720, 9, 9]> grad_out = ?",
            "Tensor<[1, 720, 9, 9]> input = ?",
            "Optional[Tensor]<[720]> weight = ?",
            "Optional[Tensor]<[720]> running_mean = ?",
            "Optional[Tensor]<[720]> running_var = ?",
            "Optional[Tensor]<[720]> save_mean = ?",
            "Optional[Tensor]<[720]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 720, 17, 17]> grad_out = ?",
            "Tensor<[1, 720, 17, 17]> input = ?",
            "Optional[Tensor]<[720]> weight = ?",
            "Optional[Tensor]<[720]> running_mean = ?",
            "Optional[Tensor]<[720]> running_var = ?",
            "Optional[Tensor]<[720]> save_mean = ?",
            "Optional[Tensor]<[720]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 120, 17, 17]> grad_out = ?",
            "Tensor<[1, 120, 17, 17]> input = ?",
            "Optional[Tensor]<[120]> weight = ?",
            "Optional[Tensor]<[120]> running_mean = ?",
            "Optional[Tensor]<[120]> running_var = ?",
            "Optional[Tensor]<[120]> save_mean = ?",
            "Optional[Tensor]<[120]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 528, 17, 17]> grad_out = ?",
            "Tensor<[1, 528, 17, 17]> input = ?",
            "Optional[Tensor]<[528]> weight = ?",
            "Optional[Tensor]<[528]> running_mean = ?",
            "Optional[Tensor]<[528]> running_var = ?",
            "Optional[Tensor]<[528]> save_mean = ?",
            "Optional[Tensor]<[528]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 88, 17, 17]> grad_out = ?",
            "Tensor<[1, 88, 17, 17]> input = ?",
            "Optional[Tensor]<[88]> weight = ?",
            "Optional[Tensor]<[88]> running_mean = ?",
            "Optional[Tensor]<[88]> running_var = ?",
            "Optional[Tensor]<[88]> save_mean = ?",
            "Optional[Tensor]<[88]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 288, 17, 17]> grad_out = ?",
            "Tensor<[1, 288, 17, 17]> input = ?",
            "Optional[Tensor]<[288]> weight = ?",
            "Optional[Tensor]<[288]> running_mean = ?",
            "Optional[Tensor]<[288]> running_var = ?",
            "Optional[Tensor]<[288]> save_mean = ?",
            "Optional[Tensor]<[288]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 288, 33, 33]> grad_out = ?",
            "Tensor<[1, 288, 33, 33]> input = ?",
            "Optional[Tensor]<[288]> weight = ?",
            "Optional[Tensor]<[288]> running_mean = ?",
            "Optional[Tensor]<[288]> running_var = ?",
            "Optional[Tensor]<[288]> save_mean = ?",
            "Optional[Tensor]<[288]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 48, 33, 33]> grad_out = ?",
            "Tensor<[1, 48, 33, 33]> input = ?",
            "Optional[Tensor]<[48]> weight = ?",
            "Optional[Tensor]<[48]> running_mean = ?",
            "Optional[Tensor]<[48]> running_var = ?",
            "Optional[Tensor]<[48]> save_mean = ?",
            "Optional[Tensor]<[48]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 144, 33, 33]> grad_out = ?",
            "Tensor<[1, 144, 33, 33]> input = ?",
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
            "Tensor<[1, 144, 65, 65]> grad_out = ?",
            "Tensor<[1, 144, 65, 65]> input = ?",
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
            "Tensor<[1, 24, 65, 65]> grad_out = ?",
            "Tensor<[1, 24, 65, 65]> input = ?",
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
            "Tensor<[1, 96, 65, 65]> grad_out = ?",
            "Tensor<[1, 96, 65, 65]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> running_mean = ?",
            "Optional[Tensor]<[96]> running_var = ?",
            "Optional[Tensor]<[96]> save_mean = ?",
            "Optional[Tensor]<[96]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 96, 130, 130]> grad_out = ?",
            "Tensor<[1, 96, 130, 130]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> running_mean = ?",
            "Optional[Tensor]<[96]> running_var = ?",
            "Optional[Tensor]<[96]> save_mean = ?",
            "Optional[Tensor]<[96]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 16, 130, 130]> grad_out = ?",
            "Tensor<[1, 16, 130, 130]> input = ?",
            "Optional[Tensor]<[16]> weight = ?",
            "Optional[Tensor]<[16]> running_mean = ?",
            "Optional[Tensor]<[16]> running_var = ?",
            "Optional[Tensor]<[16]> save_mean = ?",
            "Optional[Tensor]<[16]> save_invstd = ?",
            "bool train = True",
            "float eps = 0.001",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 32, 130, 130]> grad_out = ?",
            "Tensor<[1, 32, 130, 130]> input = ?",
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
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {e}")
            metric["run"] = False

    if metric["run"] == True:
        try:
            # Check inference result
            accuracy = calculate_accuracy(result_before, result_after)
            if accuracy >= 0.99:
                metric["accuracy"] = True
            else:
                metric["accuracy"] = False
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        try:
            # Check the graph has be rewritten and contain ttnn ops
            nodes = list(option._out_fx_graphs[0].nodes)
            if any(["ttnn" in str(node) for node in nodes]):
                metric["convert_to_ttnn"] = True
            else:
                metric["convert_to_ttnn"] = False
        except Exception as e:
            print(f"Failed to check the graph has ttnn op. Raised exception: {e}")

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] == True
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
