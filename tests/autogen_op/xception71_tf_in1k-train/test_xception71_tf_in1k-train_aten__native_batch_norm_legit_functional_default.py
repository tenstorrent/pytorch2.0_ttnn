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
        return torch.ops.aten._native_batch_norm_legit_functional.default(*args, **kwargs)


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
        metrics, "metrics-autogen-op/xception71.tf_in1k-train", "aten._native_batch_norm_legit_functional.default"
    )


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 32, 150, 150]> input = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "Tensor<[32]> running_mean = ?",
            "Tensor<[32]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 64, 150, 150]> input = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "Tensor<[64]> running_mean = ?",
            "Tensor<[64]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 128, 150, 150]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "Tensor<[128]> running_mean = ?",
            "Tensor<[128]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 128, 75, 75]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "Tensor<[128]> running_mean = ?",
            "Tensor<[128]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 256, 75, 75]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "Tensor<[256]> running_mean = ?",
            "Tensor<[256]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 256, 38, 38]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "Tensor<[256]> running_mean = ?",
            "Tensor<[256]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 728, 38, 38]> input = ?",
            "Optional[Tensor]<[728]> weight = ?",
            "Optional[Tensor]<[728]> bias = ?",
            "Tensor<[728]> running_mean = ?",
            "Tensor<[728]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 728, 19, 19]> input = ?",
            "Optional[Tensor]<[728]> weight = ?",
            "Optional[Tensor]<[728]> bias = ?",
            "Tensor<[728]> running_mean = ?",
            "Tensor<[728]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 1024, 19, 19]> input = ?",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "Tensor<[1024]> running_mean = ?",
            "Tensor<[1024]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 1024, 10, 10]> input = ?",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "Tensor<[1024]> running_mean = ?",
            "Tensor<[1024]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 1536, 10, 10]> input = ?",
            "Optional[Tensor]<[1536]> weight = ?",
            "Optional[Tensor]<[1536]> bias = ?",
            "Tensor<[1536]> running_mean = ?",
            "Tensor<[1536]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
        [
            "Tensor<[1, 2048, 10, 10]> input = ?",
            "Optional[Tensor]<[2048]> weight = ?",
            "Optional[Tensor]<[2048]> bias = ?",
            "Tensor<[2048]> running_mean = ?",
            "Tensor<[2048]> running_var = ?",
            "bool training = True",
            "float momentum = 0.1",
            "float eps = 0.001",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._native_batch_norm_legit_functional.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._native_batch_norm_legit_functional.default", input_strings
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
