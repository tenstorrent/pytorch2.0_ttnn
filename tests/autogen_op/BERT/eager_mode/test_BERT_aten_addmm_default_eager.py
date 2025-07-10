# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
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
        return torch.ops.aten.addmm.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/BERT", "aten.addmm.default")


@pytest.mark.parametrize(
    "input_strings", [
        ["Tensor<[768]> self = ?", "Tensor<[1, 512]> mat1 = ?", "Tensor<[512, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[30522]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 30522]> mat2 = ?"],
    ]
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.addmm.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.addmm.default", input_strings
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
        # Move module and input to TTNN device using cpp extension
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
            # Check inference result
            metric["accuracy"] = calculate_accuracy(result_before, result_after)
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        # In eager mode, we do not check graph rewriting
        metric["convert_to_ttnn"] = "N/A"
        metric["ttnn_fallbacks_to_host_count"] = "N/A"

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] >= 0.99
