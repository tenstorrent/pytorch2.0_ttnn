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
    save_pickle(metrics, "metrics-input-variations/model-tests-metrics-group-30/ssdlite320_mobilenet_v3_large eval", "aten._native_batch_norm_legit_no_training.default")


@pytest.mark.parametrize("input_strings", [['Tensor<[1, 16, 160, 160]> input = ?', 'Optional[Tensor]<[16]> weight = ?', 'Optional[Tensor]<[16]> bias = ?', 'Tensor<[16]> running_mean = ?', 'Tensor<[16]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 64, 160, 160]> input = ?', 'Optional[Tensor]<[64]> weight = ?', 'Optional[Tensor]<[64]> bias = ?', 'Tensor<[64]> running_mean = ?', 'Tensor<[64]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 64, 80, 80]> input = ?', 'Optional[Tensor]<[64]> weight = ?', 'Optional[Tensor]<[64]> bias = ?', 'Tensor<[64]> running_mean = ?', 'Tensor<[64]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 24, 80, 80]> input = ?', 'Optional[Tensor]<[24]> weight = ?', 'Optional[Tensor]<[24]> bias = ?', 'Tensor<[24]> running_mean = ?', 'Tensor<[24]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 72, 80, 80]> input = ?', 'Optional[Tensor]<[72]> weight = ?', 'Optional[Tensor]<[72]> bias = ?', 'Tensor<[72]> running_mean = ?', 'Tensor<[72]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 72, 40, 40]> input = ?', 'Optional[Tensor]<[72]> weight = ?', 'Optional[Tensor]<[72]> bias = ?', 'Tensor<[72]> running_mean = ?', 'Tensor<[72]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 40, 40, 40]> input = ?', 'Optional[Tensor]<[40]> weight = ?', 'Optional[Tensor]<[40]> bias = ?', 'Tensor<[40]> running_mean = ?', 'Tensor<[40]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 120, 40, 40]> input = ?', 'Optional[Tensor]<[120]> weight = ?', 'Optional[Tensor]<[120]> bias = ?', 'Tensor<[120]> running_mean = ?', 'Tensor<[120]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 240, 40, 40]> input = ?', 'Optional[Tensor]<[240]> weight = ?', 'Optional[Tensor]<[240]> bias = ?', 'Tensor<[240]> running_mean = ?', 'Tensor<[240]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 240, 20, 20]> input = ?', 'Optional[Tensor]<[240]> weight = ?', 'Optional[Tensor]<[240]> bias = ?', 'Tensor<[240]> running_mean = ?', 'Tensor<[240]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 80, 20, 20]> input = ?', 'Optional[Tensor]<[80]> weight = ?', 'Optional[Tensor]<[80]> bias = ?', 'Tensor<[80]> running_mean = ?', 'Tensor<[80]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 200, 20, 20]> input = ?', 'Optional[Tensor]<[200]> weight = ?', 'Optional[Tensor]<[200]> bias = ?', 'Tensor<[200]> running_mean = ?', 'Tensor<[200]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 184, 20, 20]> input = ?', 'Optional[Tensor]<[184]> weight = ?', 'Optional[Tensor]<[184]> bias = ?', 'Tensor<[184]> running_mean = ?', 'Tensor<[184]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 480, 20, 20]> input = ?', 'Optional[Tensor]<[480]> weight = ?', 'Optional[Tensor]<[480]> bias = ?', 'Tensor<[480]> running_mean = ?', 'Tensor<[480]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 112, 20, 20]> input = ?', 'Optional[Tensor]<[112]> weight = ?', 'Optional[Tensor]<[112]> bias = ?', 'Tensor<[112]> running_mean = ?', 'Tensor<[112]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 672, 20, 20]> input = ?', 'Optional[Tensor]<[672]> weight = ?', 'Optional[Tensor]<[672]> bias = ?', 'Tensor<[672]> running_mean = ?', 'Tensor<[672]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 672, 10, 10]> input = ?', 'Optional[Tensor]<[672]> weight = ?', 'Optional[Tensor]<[672]> bias = ?', 'Tensor<[672]> running_mean = ?', 'Tensor<[672]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 80, 10, 10]> input = ?', 'Optional[Tensor]<[80]> weight = ?', 'Optional[Tensor]<[80]> bias = ?', 'Tensor<[80]> running_mean = ?', 'Tensor<[80]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 480, 10, 10]> input = ?', 'Optional[Tensor]<[480]> weight = ?', 'Optional[Tensor]<[480]> bias = ?', 'Tensor<[480]> running_mean = ?', 'Tensor<[480]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 256, 10, 10]> input = ?', 'Optional[Tensor]<[256]> weight = ?', 'Optional[Tensor]<[256]> bias = ?', 'Tensor<[256]> running_mean = ?', 'Tensor<[256]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 256, 5, 5]> input = ?', 'Optional[Tensor]<[256]> weight = ?', 'Optional[Tensor]<[256]> bias = ?', 'Tensor<[256]> running_mean = ?', 'Tensor<[256]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 512, 5, 5]> input = ?', 'Optional[Tensor]<[512]> weight = ?', 'Optional[Tensor]<[512]> bias = ?', 'Tensor<[512]> running_mean = ?', 'Tensor<[512]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 128, 5, 5]> input = ?', 'Optional[Tensor]<[128]> weight = ?', 'Optional[Tensor]<[128]> bias = ?', 'Tensor<[128]> running_mean = ?', 'Tensor<[128]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 128, 3, 3]> input = ?', 'Optional[Tensor]<[128]> weight = ?', 'Optional[Tensor]<[128]> bias = ?', 'Tensor<[128]> running_mean = ?', 'Tensor<[128]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 256, 3, 3]> input = ?', 'Optional[Tensor]<[256]> weight = ?', 'Optional[Tensor]<[256]> bias = ?', 'Tensor<[256]> running_mean = ?', 'Tensor<[256]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 128, 2, 2]> input = ?', 'Optional[Tensor]<[128]> weight = ?', 'Optional[Tensor]<[128]> bias = ?', 'Tensor<[128]> running_mean = ?', 'Tensor<[128]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 256, 2, 2]> input = ?', 'Optional[Tensor]<[256]> weight = ?', 'Optional[Tensor]<[256]> bias = ?', 'Tensor<[256]> running_mean = ?', 'Tensor<[256]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 64, 2, 2]> input = ?', 'Optional[Tensor]<[64]> weight = ?', 'Optional[Tensor]<[64]> bias = ?', 'Tensor<[64]> running_mean = ?', 'Tensor<[64]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 64, 1, 1]> input = ?', 'Optional[Tensor]<[64]> weight = ?', 'Optional[Tensor]<[64]> bias = ?', 'Tensor<[64]> running_mean = ?', 'Tensor<[64]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001'], ['Tensor<[1, 128, 1, 1]> input = ?', 'Optional[Tensor]<[128]> weight = ?', 'Optional[Tensor]<[128]> bias = ?', 'Tensor<[128]> running_mean = ?', 'Tensor<[128]> running_var = ?', 'float momentum = 0.03', 'float eps = 0.001']])
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