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
        return torch.ops.aten._scaled_dot_product_flash_attention.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten._scaled_dot_product_flash_attention.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 8, 4096, 40]> query = ?",
            "Tensor<[1, 8, 4096, 40]> key = ?",
            "Tensor<[1, 8, 4096, 40]> value = ?",
        ],
        ["Tensor<[1, 8, 4096, 40]> query = ?", "Tensor<[1, 8, 9, 40]> key = ?", "Tensor<[1, 8, 9, 40]> value = ?"],
        [
            "Tensor<[1, 8, s0*s1, 80]> query = ?",
            "Tensor<[1, 8, s0*s1, 80]> key = ?",
            "Tensor<[1, 8, s0*s1, 80]> value = ?",
        ],
        ["Tensor<[1, 8, s0*s1, 80]> query = ?", "Tensor<[1, 8, 9, 80]> key = ?", "Tensor<[1, 8, 9, 80]> value = ?"],
        [
            "Tensor<[1, 8, s1*s2, 160]> query = ?",
            "Tensor<[1, 8, s1*s2, 160]> key = ?",
            "Tensor<[1, 8, s1*s2, 160]> value = ?",
        ],
        ["Tensor<[1, 8, s1*s2, 160]> query = ?", "Tensor<[1, 8, 9, 160]> key = ?", "Tensor<[1, 8, 9, 160]> value = ?"],
        [
            "Tensor<[1, 8, s0*s1, 160]> query = ?",
            "Tensor<[1, 8, s0*s1, 160]> key = ?",
            "Tensor<[1, 8, s0*s1, 160]> value = ?",
        ],
        ["Tensor<[1, 8, s0*s1, 160]> query = ?", "Tensor<[1, 8, 9, 160]> key = ?", "Tensor<[1, 8, 9, 160]> value = ?"],
        [
            "Tensor<[1, 8, s1*s2, 80]> query = ?",
            "Tensor<[1, 8, s1*s2, 80]> key = ?",
            "Tensor<[1, 8, s1*s2, 80]> value = ?",
        ],
        ["Tensor<[1, 8, s1*s2, 80]> query = ?", "Tensor<[1, 8, 9, 80]> key = ?", "Tensor<[1, 8, 9, 80]> value = ?"],
        [
            "Tensor<[1, 8, s1*s2, 40]> query = ?",
            "Tensor<[1, 8, s1*s2, 40]> key = ?",
            "Tensor<[1, 8, s1*s2, 40]> value = ?",
        ],
        ["Tensor<[1, 8, s1*s2, 40]> query = ?", "Tensor<[1, 8, 9, 40]> key = ?", "Tensor<[1, 8, 9, 40]> value = ?"],
        [
            "Tensor<[1, 12, 1500, 64]> query = ?",
            "Tensor<[1, 12, 1500, 64]> key = ?",
            "Tensor<[1, 12, 1500, 64]> value = ?",
        ],
        ["Tensor<[1, 12, 1, 64]> query = ?", "Tensor<[1, 12, 1, 64]> key = ?", "Tensor<[1, 12, 1, 64]> value = ?"],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, 1500, 64]> key = ?",
            "Tensor<[1, 12, 1500, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 4, 64]> query = ?",
            "Tensor<[1, 12, 4, 64]> key = ?",
            "Tensor<[1, 12, 4, 64]> value = ?",
            "float dropout_p = 0.0",
            "bool is_causal = True",
        ],
        [
            "Tensor<[1, 12, 4, 64]> query = ?",
            "Tensor<[1, 12, 1500, 64]> key = ?",
            "Tensor<[1, 12, 1500, 64]> value = ?",
        ],
        ["Tensor<[1, 12, 1, 64]> query = ?", "Tensor<[1, 12, 5, 64]> key = ?", "Tensor<[1, 12, 5, 64]> value = ?"],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s2 + 1, 64]> key = ?",
            "Tensor<[1, 12, s3 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s4 + 1, 64]> key = ?",
            "Tensor<[1, 12, s5 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s6 + 1, 64]> key = ?",
            "Tensor<[1, 12, s7 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s8 + 1, 64]> key = ?",
            "Tensor<[1, 12, s9 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s10 + 1, 64]> key = ?",
            "Tensor<[1, 12, s11 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s12 + 1, 64]> key = ?",
            "Tensor<[1, 12, s13 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s14 + 1, 64]> key = ?",
            "Tensor<[1, 12, s15 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s16 + 1, 64]> key = ?",
            "Tensor<[1, 12, s17 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s18 + 1, 64]> key = ?",
            "Tensor<[1, 12, s19 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s20 + 1, 64]> key = ?",
            "Tensor<[1, 12, s21 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s22 + 1, 64]> key = ?",
            "Tensor<[1, 12, s23 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 1, 64]> query = ?",
            "Tensor<[1, 12, s24 + 1, 64]> key = ?",
            "Tensor<[1, 12, s25 + 1, 64]> value = ?",
        ],
        [
            "Tensor<[1, 12, 197, 64]> query = ?",
            "Tensor<[1, 12, 197, 64]> key = ?",
            "Tensor<[1, 12, 197, 64]> value = ?",
        ],
        ["Tensor<[1, 12, 50, 64]> query = ?", "Tensor<[1, 12, 50, 64]> key = ?", "Tensor<[1, 12, 50, 64]> value = ?"],
        [
            "Tensor<[1, 16, 1370, 80]> query = ?",
            "Tensor<[1, 16, 1370, 80]> key = ?",
            "Tensor<[1, 16, 1370, 80]> value = ?",
        ],
        [
            "Tensor<[1, 16, 197, 64]> query = ?",
            "Tensor<[1, 16, 197, 64]> key = ?",
            "Tensor<[1, 16, 197, 64]> value = ?",
        ],
        ["Tensor<[1, 16, 50, 64]> query = ?", "Tensor<[1, 16, 50, 64]> key = ?", "Tensor<[1, 16, 50, 64]> value = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._scaled_dot_product_flash_attention.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._scaled_dot_product_flash_attention.default", input_strings
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
