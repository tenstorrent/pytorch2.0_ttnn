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
    save_pickle(
        metrics, "metrics-autogen-op/tf_efficientnet_lite4.in1k", "aten._native_batch_norm_legit_no_training.default"
    )


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 32, 190, 190]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "Tensor<[32]> running_mean = ?",
            "Tensor<[32]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 24, 190, 190]> input = ?",
            "Optional[Tensor]<[24]> weight = ?",
            "Optional[Tensor]<[24]> bias = ?",
            "Tensor<[24]> running_mean = ?",
            "Tensor<[24]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 144, 190, 190]> input = ?",
            "Optional[Tensor]<[144]> weight = ?",
            "Optional[Tensor]<[144]> bias = ?",
            "Tensor<[144]> running_mean = ?",
            "Tensor<[144]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 144, 95, 95]> input = ?",
            "Optional[Tensor]<[144]> weight = ?",
            "Optional[Tensor]<[144]> bias = ?",
            "Tensor<[144]> running_mean = ?",
            "Tensor<[144]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 32, 95, 95]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "Tensor<[32]> running_mean = ?",
            "Tensor<[32]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 192, 95, 95]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "Tensor<[192]> running_mean = ?",
            "Tensor<[192]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 192, 48, 48]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "Tensor<[192]> running_mean = ?",
            "Tensor<[192]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 56, 48, 48]> input = ?",
            "Optional[Tensor]<[56]> weight = ?",
            "Optional[Tensor]<[56]> bias = ?",
            "Tensor<[56]> running_mean = ?",
            "Tensor<[56]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 336, 48, 48]> input = ?",
            "Optional[Tensor]<[336]> weight = ?",
            "Optional[Tensor]<[336]> bias = ?",
            "Tensor<[336]> running_mean = ?",
            "Tensor<[336]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 336, 24, 24]> input = ?",
            "Optional[Tensor]<[336]> weight = ?",
            "Optional[Tensor]<[336]> bias = ?",
            "Tensor<[336]> running_mean = ?",
            "Tensor<[336]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 112, 24, 24]> input = ?",
            "Optional[Tensor]<[112]> weight = ?",
            "Optional[Tensor]<[112]> bias = ?",
            "Tensor<[112]> running_mean = ?",
            "Tensor<[112]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 672, 24, 24]> input = ?",
            "Optional[Tensor]<[672]> weight = ?",
            "Optional[Tensor]<[672]> bias = ?",
            "Tensor<[672]> running_mean = ?",
            "Tensor<[672]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 160, 24, 24]> input = ?",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> bias = ?",
            "Tensor<[160]> running_mean = ?",
            "Tensor<[160]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 960, 24, 24]> input = ?",
            "Optional[Tensor]<[960]> weight = ?",
            "Optional[Tensor]<[960]> bias = ?",
            "Tensor<[960]> running_mean = ?",
            "Tensor<[960]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 960, 12, 12]> input = ?",
            "Optional[Tensor]<[960]> weight = ?",
            "Optional[Tensor]<[960]> bias = ?",
            "Tensor<[960]> running_mean = ?",
            "Tensor<[960]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 272, 12, 12]> input = ?",
            "Optional[Tensor]<[272]> weight = ?",
            "Optional[Tensor]<[272]> bias = ?",
            "Tensor<[272]> running_mean = ?",
            "Tensor<[272]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 1632, 12, 12]> input = ?",
            "Optional[Tensor]<[1632]> weight = ?",
            "Optional[Tensor]<[1632]> bias = ?",
            "Tensor<[1632]> running_mean = ?",
            "Tensor<[1632]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 448, 12, 12]> input = ?",
            "Optional[Tensor]<[448]> weight = ?",
            "Optional[Tensor]<[448]> bias = ?",
            "Tensor<[448]> running_mean = ?",
            "Tensor<[448]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 1280, 12, 12]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "Tensor<[1280]> running_mean = ?",
            "Tensor<[1280]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._native_batch_norm_legit_no_training.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._native_batch_norm_legit_no_training.default", input_strings
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
