import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, get_input_vals_from_metric_str


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.aten._native_batch_norm_legit_no_training.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-input-variations/model-tests-metrics-group-18/mobilenet_v2 eval", "aten._native_batch_norm_legit_no_training.default")


@pytest.mark.parametrize("input_strings", [['Tensor<[1, 32, 112, 112]> input = ?', 'Optional[Tensor]<[32]> weight = ?', 'Optional[Tensor]<[32]> bias = ?', 'Tensor<[32]> running_mean = ?', 'Tensor<[32]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 16, 112, 112]> input = ?', 'Optional[Tensor]<[16]> weight = ?', 'Optional[Tensor]<[16]> bias = ?', 'Tensor<[16]> running_mean = ?', 'Tensor<[16]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 96, 112, 112]> input = ?', 'Optional[Tensor]<[96]> weight = ?', 'Optional[Tensor]<[96]> bias = ?', 'Tensor<[96]> running_mean = ?', 'Tensor<[96]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 96, 56, 56]> input = ?', 'Optional[Tensor]<[96]> weight = ?', 'Optional[Tensor]<[96]> bias = ?', 'Tensor<[96]> running_mean = ?', 'Tensor<[96]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 24, 56, 56]> input = ?', 'Optional[Tensor]<[24]> weight = ?', 'Optional[Tensor]<[24]> bias = ?', 'Tensor<[24]> running_mean = ?', 'Tensor<[24]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 144, 56, 56]> input = ?', 'Optional[Tensor]<[144]> weight = ?', 'Optional[Tensor]<[144]> bias = ?', 'Tensor<[144]> running_mean = ?', 'Tensor<[144]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 144, 28, 28]> input = ?', 'Optional[Tensor]<[144]> weight = ?', 'Optional[Tensor]<[144]> bias = ?', 'Tensor<[144]> running_mean = ?', 'Tensor<[144]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 32, 28, 28]> input = ?', 'Optional[Tensor]<[32]> weight = ?', 'Optional[Tensor]<[32]> bias = ?', 'Tensor<[32]> running_mean = ?', 'Tensor<[32]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 192, 28, 28]> input = ?', 'Optional[Tensor]<[192]> weight = ?', 'Optional[Tensor]<[192]> bias = ?', 'Tensor<[192]> running_mean = ?', 'Tensor<[192]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 192, 14, 14]> input = ?', 'Optional[Tensor]<[192]> weight = ?', 'Optional[Tensor]<[192]> bias = ?', 'Tensor<[192]> running_mean = ?', 'Tensor<[192]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 64, 14, 14]> input = ?', 'Optional[Tensor]<[64]> weight = ?', 'Optional[Tensor]<[64]> bias = ?', 'Tensor<[64]> running_mean = ?', 'Tensor<[64]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 384, 14, 14]> input = ?', 'Optional[Tensor]<[384]> weight = ?', 'Optional[Tensor]<[384]> bias = ?', 'Tensor<[384]> running_mean = ?', 'Tensor<[384]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 96, 14, 14]> input = ?', 'Optional[Tensor]<[96]> weight = ?', 'Optional[Tensor]<[96]> bias = ?', 'Tensor<[96]> running_mean = ?', 'Tensor<[96]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 576, 14, 14]> input = ?', 'Optional[Tensor]<[576]> weight = ?', 'Optional[Tensor]<[576]> bias = ?', 'Tensor<[576]> running_mean = ?', 'Tensor<[576]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 576, 7, 7]> input = ?', 'Optional[Tensor]<[576]> weight = ?', 'Optional[Tensor]<[576]> bias = ?', 'Tensor<[576]> running_mean = ?', 'Tensor<[576]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 160, 7, 7]> input = ?', 'Optional[Tensor]<[160]> weight = ?', 'Optional[Tensor]<[160]> bias = ?', 'Tensor<[160]> running_mean = ?', 'Tensor<[160]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 960, 7, 7]> input = ?', 'Optional[Tensor]<[960]> weight = ?', 'Optional[Tensor]<[960]> bias = ?', 'Tensor<[960]> running_mean = ?', 'Tensor<[960]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 320, 7, 7]> input = ?', 'Optional[Tensor]<[320]> weight = ?', 'Optional[Tensor]<[320]> bias = ?', 'Tensor<[320]> running_mean = ?', 'Tensor<[320]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05'], ['Tensor<[1, 1280, 7, 7]> input = ?', 'Optional[Tensor]<[1280]> weight = ?', 'Optional[Tensor]<[1280]> bias = ?', 'Tensor<[1280]> running_mean = ?', 'Tensor<[1280]> running_var = ?', 'float momentum = 0.1', 'float eps = 1e-05']])
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
            "opname": "aten._native_batch_norm_legit_no_training.default",
            "input_strings": input_strings,
            "native_run": False,
            "run": False,
            "accuracy": False,
            "convert_to_ttnn": False,
        }
    m = AtenModule()
    input_args, input_kwargs = get_input_vals_from_metric_str("aten._native_batch_norm_legit_no_training.default", input_strings)
    if input_args is None and input_kwargs is None:
        pytest.skip("Invalid input strings:" + str(input_strings))
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
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

    if metric["run"] == True:
        # Check inference result
        accuracy = calculate_accuracy(result_before, result_after)
        if accuracy >= 0.99:
            metric["accuracy"] = True

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        if any(["ttnn" in str(node) for node in nodes]):
            metric["convert_to_ttnn"] = True

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] == True
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True