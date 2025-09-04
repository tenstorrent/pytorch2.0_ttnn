import torch
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, render_metric_string_list_to_input_args_kwargs
from torch_ttnn.cpp_extension import ttnn_module


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.aten.bmm.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/BERT", "aten.bmm.default")


@pytest.mark.parametrize(
    "input_strings", [
        ["Tensor<[12, 512, 64]> self = ?", "Tensor<[12, 64, 512]> mat2 = ?"],
        ["Tensor<[12, 512, 512]> self = ?", "Tensor<[12, 512, 64]> mat2 = ?"],
        ["Tensor<[16, 256, 64]> self = ?", "Tensor<[16, 64, 256]> mat2 = ?"],
        ["Tensor<[16, 256, 256]> self = ?", "Tensor<[16, 256, 64]> mat2 = ?"],
    ]
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.bmm.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.bmm.default", input_strings
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
        ttnn_torch_device = ttnn_module.as_torch_device(device)
        m = m.to(ttnn_torch_device)
        input_args = [a.to(ttnn_torch_device) if isinstance(a, torch.Tensor) else a for a in input_args]
        input_kwargs = {k: (v.to(ttnn_torch_device) if isinstance(v, torch.Tensor) else v) for k, v in input_kwargs.items()}
        try:
            with torch.no_grad():
                result_after = m.forward(*input_args, **input_kwargs)
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run on TTNN device. Raised exception: {e}")
            metric["run"] = False

    if metric["run"] == True:
        try:
            metric["accuracy"] = calculate_accuracy(result_before, result_after)
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        metric["convert_to_ttnn"] = "N/A"
        metric["ttnn_fallbacks_to_host_count"] = "N/A"

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] >= 0.99
