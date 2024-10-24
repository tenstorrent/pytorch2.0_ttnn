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
        return torch.ops.aten.native_layer_norm_backward.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.native_layer_norm_backward.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[2, 7, 512]> grad_out = ?",
            "Tensor<[2, 7, 512]> input = ?",
            "List[int] normalized_shape = [512]",
            "Tensor<[2, 7, 1]> mean = ?",
            "Tensor<[2, 7, 1]> rstd = ?",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 768]> grad_out = ?",
            "Tensor<[1, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Tensor<[1, 1]> mean = ?",
            "Tensor<[1, 1]> rstd = ?",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 50, 768]> grad_out = ?",
            "Tensor<[1, 50, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Tensor<[1, 50, 1]> mean = ?",
            "Tensor<[1, 50, 1]> rstd = ?",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 256, 512]> grad_out = ?",
            "Tensor<[1, 256, 512]> input = ?",
            "List[int] normalized_shape = [512]",
            "Tensor<[1, 256, 1]> mean = ?",
            "Tensor<[1, 256, 1]> rstd = ?",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 256, 256]> grad_out = ?",
            "Tensor<[1, 256, 256]> input = ?",
            "List[int] normalized_shape = [256]",
            "Tensor<[1, 256, 1]> mean = ?",
            "Tensor<[1, 256, 1]> rstd = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 1024, 160]> grad_out = ?",
            "Tensor<[1, 1024, 160]> input = ?",
            "List[int] normalized_shape = [160]",
            "Tensor<[1, 1024, 1]> mean = ?",
            "Tensor<[1, 1024, 1]> rstd = ?",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 256, 160]> grad_out = ?",
            "Tensor<[1, 256, 160]> input = ?",
            "List[int] normalized_shape = [160]",
            "Tensor<[1, 256, 1]> mean = ?",
            "Tensor<[1, 256, 1]> rstd = ?",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 4096, 64]> grad_out = ?",
            "Tensor<[1, 4096, 64]> input = ?",
            "List[int] normalized_shape = [64]",
            "Tensor<[1, 4096, 1]> mean = ?",
            "Tensor<[1, 4096, 1]> rstd = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 256, 64]> grad_out = ?",
            "Tensor<[1, 256, 64]> input = ?",
            "List[int] normalized_shape = [64]",
            "Tensor<[1, 256, 1]> mean = ?",
            "Tensor<[1, 256, 1]> rstd = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 16384, 32]> grad_out = ?",
            "Tensor<[1, 16384, 32]> input = ?",
            "List[int] normalized_shape = [32]",
            "Tensor<[1, 16384, 1]> mean = ?",
            "Tensor<[1, 16384, 1]> rstd = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 256, 32]> grad_out = ?",
            "Tensor<[1, 256, 32]> input = ?",
            "List[int] normalized_shape = [32]",
            "Tensor<[1, 256, 1]> mean = ?",
            "Tensor<[1, 256, 1]> rstd = ?",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 197, 768]> grad_out = ?",
            "Tensor<[1, 197, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Tensor<[1, 197, 1]> mean = ?",
            "Tensor<[1, 197, 1]> rstd = ?",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 1024]> grad_out = ?",
            "Tensor<[1, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Tensor<[1, 1]> mean = ?",
            "Tensor<[1, 1]> rstd = ?",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 197, 1024]> grad_out = ?",
            "Tensor<[1, 197, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Tensor<[1, 197, 1]> mean = ?",
            "Tensor<[1, 197, 1]> rstd = ?",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
        [
            "Tensor<[1, 196, 768]> grad_out = ?",
            "Tensor<[1, 196, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Tensor<[1, 196, 1]> mean = ?",
            "Tensor<[1, 196, 1]> rstd = ?",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "List[bool] output_mask = [True, True, True]",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.native_layer_norm_backward.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.native_layer_norm_backward.default", input_strings
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