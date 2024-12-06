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
    save_pickle(metrics, "metrics-autogen-op/ghostnet_100.in1k-train", "aten.native_batch_norm_backward.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 960, 7, 7]> grad_out = ?",
            "Tensor<[1, 960, 7, 7]> input = ?",
            "Optional[Tensor]<[960]> weight = ?",
            "Optional[Tensor]<[960]> running_mean = ?",
            "Optional[Tensor]<[960]> running_var = ?",
            "Optional[Tensor]<[960]> save_mean = ?",
            "Optional[Tensor]<[960]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 80, 7, 7]> grad_out = ?",
            "Tensor<[1, 80, 7, 7]> input = ?",
            "Optional[Tensor]<[80]> weight = ?",
            "Optional[Tensor]<[80]> running_mean = ?",
            "Optional[Tensor]<[80]> running_var = ?",
            "Optional[Tensor]<[80]> save_mean = ?",
            "Optional[Tensor]<[80]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 480, 7, 7]> grad_out = ?",
            "Tensor<[1, 480, 7, 7]> input = ?",
            "Optional[Tensor]<[480]> weight = ?",
            "Optional[Tensor]<[480]> running_mean = ?",
            "Optional[Tensor]<[480]> running_var = ?",
            "Optional[Tensor]<[480]> save_mean = ?",
            "Optional[Tensor]<[480]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 160, 7, 7]> grad_out = ?",
            "Tensor<[1, 160, 7, 7]> input = ?",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> running_mean = ?",
            "Optional[Tensor]<[160]> running_var = ?",
            "Optional[Tensor]<[160]> save_mean = ?",
            "Optional[Tensor]<[160]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 112, 7, 7]> grad_out = ?",
            "Tensor<[1, 112, 7, 7]> input = ?",
            "Optional[Tensor]<[112]> weight = ?",
            "Optional[Tensor]<[112]> running_mean = ?",
            "Optional[Tensor]<[112]> running_var = ?",
            "Optional[Tensor]<[112]> save_mean = ?",
            "Optional[Tensor]<[112]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 672, 7, 7]> grad_out = ?",
            "Tensor<[1, 672, 7, 7]> input = ?",
            "Optional[Tensor]<[672]> weight = ?",
            "Optional[Tensor]<[672]> running_mean = ?",
            "Optional[Tensor]<[672]> running_var = ?",
            "Optional[Tensor]<[672]> save_mean = ?",
            "Optional[Tensor]<[672]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 336, 14, 14]> grad_out = ?",
            "Tensor<[1, 336, 14, 14]> input = ?",
            "Optional[Tensor]<[336]> weight = ?",
            "Optional[Tensor]<[336]> running_mean = ?",
            "Optional[Tensor]<[336]> running_var = ?",
            "Optional[Tensor]<[336]> save_mean = ?",
            "Optional[Tensor]<[336]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 56, 14, 14]> grad_out = ?",
            "Tensor<[1, 56, 14, 14]> input = ?",
            "Optional[Tensor]<[56]> weight = ?",
            "Optional[Tensor]<[56]> running_mean = ?",
            "Optional[Tensor]<[56]> running_var = ?",
            "Optional[Tensor]<[56]> save_mean = ?",
            "Optional[Tensor]<[56]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 112, 14, 14]> grad_out = ?",
            "Tensor<[1, 112, 14, 14]> input = ?",
            "Optional[Tensor]<[112]> weight = ?",
            "Optional[Tensor]<[112]> running_mean = ?",
            "Optional[Tensor]<[112]> running_var = ?",
            "Optional[Tensor]<[112]> save_mean = ?",
            "Optional[Tensor]<[112]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 80, 14, 14]> grad_out = ?",
            "Tensor<[1, 80, 14, 14]> input = ?",
            "Optional[Tensor]<[80]> weight = ?",
            "Optional[Tensor]<[80]> running_mean = ?",
            "Optional[Tensor]<[80]> running_var = ?",
            "Optional[Tensor]<[80]> save_mean = ?",
            "Optional[Tensor]<[80]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 240, 14, 14]> grad_out = ?",
            "Tensor<[1, 240, 14, 14]> input = ?",
            "Optional[Tensor]<[240]> weight = ?",
            "Optional[Tensor]<[240]> running_mean = ?",
            "Optional[Tensor]<[240]> running_var = ?",
            "Optional[Tensor]<[240]> save_mean = ?",
            "Optional[Tensor]<[240]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 40, 14, 14]> grad_out = ?",
            "Tensor<[1, 40, 14, 14]> input = ?",
            "Optional[Tensor]<[40]> weight = ?",
            "Optional[Tensor]<[40]> running_mean = ?",
            "Optional[Tensor]<[40]> running_var = ?",
            "Optional[Tensor]<[40]> save_mean = ?",
            "Optional[Tensor]<[40]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 92, 14, 14]> grad_out = ?",
            "Tensor<[1, 92, 14, 14]> input = ?",
            "Optional[Tensor]<[92]> weight = ?",
            "Optional[Tensor]<[92]> running_mean = ?",
            "Optional[Tensor]<[92]> running_var = ?",
            "Optional[Tensor]<[92]> save_mean = ?",
            "Optional[Tensor]<[92]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 100, 14, 14]> grad_out = ?",
            "Tensor<[1, 100, 14, 14]> input = ?",
            "Optional[Tensor]<[100]> weight = ?",
            "Optional[Tensor]<[100]> running_mean = ?",
            "Optional[Tensor]<[100]> running_var = ?",
            "Optional[Tensor]<[100]> save_mean = ?",
            "Optional[Tensor]<[100]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 120, 28, 28]> grad_out = ?",
            "Tensor<[1, 120, 28, 28]> input = ?",
            "Optional[Tensor]<[120]> weight = ?",
            "Optional[Tensor]<[120]> running_mean = ?",
            "Optional[Tensor]<[120]> running_var = ?",
            "Optional[Tensor]<[120]> save_mean = ?",
            "Optional[Tensor]<[120]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 20, 28, 28]> grad_out = ?",
            "Tensor<[1, 20, 28, 28]> input = ?",
            "Optional[Tensor]<[20]> weight = ?",
            "Optional[Tensor]<[20]> running_mean = ?",
            "Optional[Tensor]<[20]> running_var = ?",
            "Optional[Tensor]<[20]> save_mean = ?",
            "Optional[Tensor]<[20]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 60, 28, 28]> grad_out = ?",
            "Tensor<[1, 60, 28, 28]> input = ?",
            "Optional[Tensor]<[60]> weight = ?",
            "Optional[Tensor]<[60]> running_mean = ?",
            "Optional[Tensor]<[60]> running_var = ?",
            "Optional[Tensor]<[60]> save_mean = ?",
            "Optional[Tensor]<[60]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 40, 28, 28]> grad_out = ?",
            "Tensor<[1, 40, 28, 28]> input = ?",
            "Optional[Tensor]<[40]> weight = ?",
            "Optional[Tensor]<[40]> running_mean = ?",
            "Optional[Tensor]<[40]> running_var = ?",
            "Optional[Tensor]<[40]> save_mean = ?",
            "Optional[Tensor]<[40]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 24, 28, 28]> grad_out = ?",
            "Tensor<[1, 24, 28, 28]> input = ?",
            "Optional[Tensor]<[24]> weight = ?",
            "Optional[Tensor]<[24]> running_mean = ?",
            "Optional[Tensor]<[24]> running_var = ?",
            "Optional[Tensor]<[24]> save_mean = ?",
            "Optional[Tensor]<[24]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 72, 28, 28]> grad_out = ?",
            "Tensor<[1, 72, 28, 28]> input = ?",
            "Optional[Tensor]<[72]> weight = ?",
            "Optional[Tensor]<[72]> running_mean = ?",
            "Optional[Tensor]<[72]> running_var = ?",
            "Optional[Tensor]<[72]> save_mean = ?",
            "Optional[Tensor]<[72]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 36, 56, 56]> grad_out = ?",
            "Tensor<[1, 36, 56, 56]> input = ?",
            "Optional[Tensor]<[36]> weight = ?",
            "Optional[Tensor]<[36]> running_mean = ?",
            "Optional[Tensor]<[36]> running_var = ?",
            "Optional[Tensor]<[36]> save_mean = ?",
            "Optional[Tensor]<[36]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 12, 56, 56]> grad_out = ?",
            "Tensor<[1, 12, 56, 56]> input = ?",
            "Optional[Tensor]<[12]> weight = ?",
            "Optional[Tensor]<[12]> running_mean = ?",
            "Optional[Tensor]<[12]> running_var = ?",
            "Optional[Tensor]<[12]> save_mean = ?",
            "Optional[Tensor]<[12]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 24, 56, 56]> grad_out = ?",
            "Tensor<[1, 24, 56, 56]> input = ?",
            "Optional[Tensor]<[24]> weight = ?",
            "Optional[Tensor]<[24]> running_mean = ?",
            "Optional[Tensor]<[24]> running_var = ?",
            "Optional[Tensor]<[24]> save_mean = ?",
            "Optional[Tensor]<[24]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 16, 56, 56]> grad_out = ?",
            "Tensor<[1, 16, 56, 56]> input = ?",
            "Optional[Tensor]<[16]> weight = ?",
            "Optional[Tensor]<[16]> running_mean = ?",
            "Optional[Tensor]<[16]> running_var = ?",
            "Optional[Tensor]<[16]> save_mean = ?",
            "Optional[Tensor]<[16]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 48, 56, 56]> grad_out = ?",
            "Tensor<[1, 48, 56, 56]> input = ?",
            "Optional[Tensor]<[48]> weight = ?",
            "Optional[Tensor]<[48]> running_mean = ?",
            "Optional[Tensor]<[48]> running_var = ?",
            "Optional[Tensor]<[48]> save_mean = ?",
            "Optional[Tensor]<[48]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 24, 112, 112]> grad_out = ?",
            "Tensor<[1, 24, 112, 112]> input = ?",
            "Optional[Tensor]<[24]> weight = ?",
            "Optional[Tensor]<[24]> running_mean = ?",
            "Optional[Tensor]<[24]> running_var = ?",
            "Optional[Tensor]<[24]> save_mean = ?",
            "Optional[Tensor]<[24]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 8, 112, 112]> grad_out = ?",
            "Tensor<[1, 8, 112, 112]> input = ?",
            "Optional[Tensor]<[8]> weight = ?",
            "Optional[Tensor]<[8]> running_mean = ?",
            "Optional[Tensor]<[8]> running_var = ?",
            "Optional[Tensor]<[8]> save_mean = ?",
            "Optional[Tensor]<[8]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 16, 112, 112]> grad_out = ?",
            "Tensor<[1, 16, 112, 112]> input = ?",
            "Optional[Tensor]<[16]> weight = ?",
            "Optional[Tensor]<[16]> running_mean = ?",
            "Optional[Tensor]<[16]> running_var = ?",
            "Optional[Tensor]<[16]> save_mean = ?",
            "Optional[Tensor]<[16]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
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
