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
    save_pickle(metrics, "metrics-autogen-op/HardNet-train", "aten.native_batch_norm_backward.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 1024, 7, 7]> grad_out = ?",
            "Tensor<[1, 1024, 7, 7]> input = ?",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> running_mean = ?",
            "Optional[Tensor]<[1024]> running_var = ?",
            "Optional[Tensor]<[1024]> save_mean = ?",
            "Optional[Tensor]<[1024]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 462, 7, 7]> grad_out = ?",
            "Tensor<[1, 462, 7, 7]> input = ?",
            "Optional[Tensor]<[462]> weight = ?",
            "Optional[Tensor]<[462]> running_mean = ?",
            "Optional[Tensor]<[462]> running_var = ?",
            "Optional[Tensor]<[462]> save_mean = ?",
            "Optional[Tensor]<[462]> save_invstd = ?",
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
            "Tensor<[1, 272, 7, 7]> grad_out = ?",
            "Tensor<[1, 272, 7, 7]> input = ?",
            "Optional[Tensor]<[272]> weight = ?",
            "Optional[Tensor]<[272]> running_mean = ?",
            "Optional[Tensor]<[272]> running_var = ?",
            "Optional[Tensor]<[272]> save_mean = ?",
            "Optional[Tensor]<[272]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 640, 14, 14]> grad_out = ?",
            "Tensor<[1, 640, 14, 14]> input = ?",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> running_mean = ?",
            "Optional[Tensor]<[640]> running_var = ?",
            "Optional[Tensor]<[640]> save_mean = ?",
            "Optional[Tensor]<[640]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 334, 14, 14]> grad_out = ?",
            "Tensor<[1, 334, 14, 14]> input = ?",
            "Optional[Tensor]<[334]> weight = ?",
            "Optional[Tensor]<[334]> running_mean = ?",
            "Optional[Tensor]<[334]> running_var = ?",
            "Optional[Tensor]<[334]> save_mean = ?",
            "Optional[Tensor]<[334]> save_invstd = ?",
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
            "Tensor<[1, 68, 14, 14]> grad_out = ?",
            "Tensor<[1, 68, 14, 14]> input = ?",
            "Optional[Tensor]<[68]> weight = ?",
            "Optional[Tensor]<[68]> running_mean = ?",
            "Optional[Tensor]<[68]> running_var = ?",
            "Optional[Tensor]<[68]> save_mean = ?",
            "Optional[Tensor]<[68]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 116, 14, 14]> grad_out = ?",
            "Tensor<[1, 116, 14, 14]> input = ?",
            "Optional[Tensor]<[116]> weight = ?",
            "Optional[Tensor]<[116]> running_mean = ?",
            "Optional[Tensor]<[116]> running_var = ?",
            "Optional[Tensor]<[116]> save_mean = ?",
            "Optional[Tensor]<[116]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 196, 14, 14]> grad_out = ?",
            "Tensor<[1, 196, 14, 14]> input = ?",
            "Optional[Tensor]<[196]> weight = ?",
            "Optional[Tensor]<[196]> running_mean = ?",
            "Optional[Tensor]<[196]> running_var = ?",
            "Optional[Tensor]<[196]> save_mean = ?",
            "Optional[Tensor]<[196]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 320, 28, 28]> grad_out = ?",
            "Tensor<[1, 320, 28, 28]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> running_mean = ?",
            "Optional[Tensor]<[320]> running_var = ?",
            "Optional[Tensor]<[320]> save_mean = ?",
            "Optional[Tensor]<[320]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 168, 28, 28]> grad_out = ?",
            "Tensor<[1, 168, 28, 28]> input = ?",
            "Optional[Tensor]<[168]> weight = ?",
            "Optional[Tensor]<[168]> running_mean = ?",
            "Optional[Tensor]<[168]> running_var = ?",
            "Optional[Tensor]<[168]> save_mean = ?",
            "Optional[Tensor]<[168]> save_invstd = ?",
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
            "Tensor<[1, 34, 28, 28]> grad_out = ?",
            "Tensor<[1, 34, 28, 28]> input = ?",
            "Optional[Tensor]<[34]> weight = ?",
            "Optional[Tensor]<[34]> running_mean = ?",
            "Optional[Tensor]<[34]> running_var = ?",
            "Optional[Tensor]<[34]> save_mean = ?",
            "Optional[Tensor]<[34]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 58, 28, 28]> grad_out = ?",
            "Tensor<[1, 58, 28, 28]> input = ?",
            "Optional[Tensor]<[58]> weight = ?",
            "Optional[Tensor]<[58]> running_mean = ?",
            "Optional[Tensor]<[58]> running_var = ?",
            "Optional[Tensor]<[58]> save_mean = ?",
            "Optional[Tensor]<[58]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 98, 28, 28]> grad_out = ?",
            "Tensor<[1, 98, 28, 28]> input = ?",
            "Optional[Tensor]<[98]> weight = ?",
            "Optional[Tensor]<[98]> running_mean = ?",
            "Optional[Tensor]<[98]> running_var = ?",
            "Optional[Tensor]<[98]> save_mean = ?",
            "Optional[Tensor]<[98]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 256, 28, 28]> grad_out = ?",
            "Tensor<[1, 256, 28, 28]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> running_mean = ?",
            "Optional[Tensor]<[256]> running_var = ?",
            "Optional[Tensor]<[256]> save_mean = ?",
            "Optional[Tensor]<[256]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 134, 28, 28]> grad_out = ?",
            "Tensor<[1, 134, 28, 28]> input = ?",
            "Optional[Tensor]<[134]> weight = ?",
            "Optional[Tensor]<[134]> running_mean = ?",
            "Optional[Tensor]<[134]> running_var = ?",
            "Optional[Tensor]<[134]> save_mean = ?",
            "Optional[Tensor]<[134]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 16, 28, 28]> grad_out = ?",
            "Tensor<[1, 16, 28, 28]> input = ?",
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
            "Tensor<[1, 28, 28, 28]> grad_out = ?",
            "Tensor<[1, 28, 28, 28]> input = ?",
            "Optional[Tensor]<[28]> weight = ?",
            "Optional[Tensor]<[28]> running_mean = ?",
            "Optional[Tensor]<[28]> running_var = ?",
            "Optional[Tensor]<[28]> save_mean = ?",
            "Optional[Tensor]<[28]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 46, 28, 28]> grad_out = ?",
            "Tensor<[1, 46, 28, 28]> input = ?",
            "Optional[Tensor]<[46]> weight = ?",
            "Optional[Tensor]<[46]> running_mean = ?",
            "Optional[Tensor]<[46]> running_var = ?",
            "Optional[Tensor]<[46]> save_mean = ?",
            "Optional[Tensor]<[46]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 78, 28, 28]> grad_out = ?",
            "Tensor<[1, 78, 28, 28]> input = ?",
            "Optional[Tensor]<[78]> weight = ?",
            "Optional[Tensor]<[78]> running_mean = ?",
            "Optional[Tensor]<[78]> running_var = ?",
            "Optional[Tensor]<[78]> save_mean = ?",
            "Optional[Tensor]<[78]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 128, 56, 56]> grad_out = ?",
            "Tensor<[1, 128, 56, 56]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> running_mean = ?",
            "Optional[Tensor]<[128]> running_var = ?",
            "Optional[Tensor]<[128]> save_mean = ?",
            "Optional[Tensor]<[128]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 68, 56, 56]> grad_out = ?",
            "Tensor<[1, 68, 56, 56]> input = ?",
            "Optional[Tensor]<[68]> weight = ?",
            "Optional[Tensor]<[68]> running_mean = ?",
            "Optional[Tensor]<[68]> running_var = ?",
            "Optional[Tensor]<[68]> save_mean = ?",
            "Optional[Tensor]<[68]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 14, 56, 56]> grad_out = ?",
            "Tensor<[1, 14, 56, 56]> input = ?",
            "Optional[Tensor]<[14]> weight = ?",
            "Optional[Tensor]<[14]> running_mean = ?",
            "Optional[Tensor]<[14]> running_var = ?",
            "Optional[Tensor]<[14]> save_mean = ?",
            "Optional[Tensor]<[14]> save_invstd = ?",
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
            "Tensor<[1, 40, 56, 56]> grad_out = ?",
            "Tensor<[1, 40, 56, 56]> input = ?",
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
            "Tensor<[1, 64, 112, 112]> grad_out = ?",
            "Tensor<[1, 64, 112, 112]> input = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> running_mean = ?",
            "Optional[Tensor]<[64]> running_var = ?",
            "Optional[Tensor]<[64]> save_mean = ?",
            "Optional[Tensor]<[64]> save_invstd = ?",
            "bool train = True",
            "float eps = 1e-05",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 32, 112, 112]> grad_out = ?",
            "Tensor<[1, 32, 112, 112]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> running_mean = ?",
            "Optional[Tensor]<[32]> running_var = ?",
            "Optional[Tensor]<[32]> save_mean = ?",
            "Optional[Tensor]<[32]> save_invstd = ?",
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
