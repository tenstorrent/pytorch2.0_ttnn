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
        return torch.ops.aten._to_copy.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ghostnetv2_100.in1k-train", "aten._to_copy.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[16]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[8]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[24]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[48]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[12]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[72]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[36]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 72, 28, 28]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[56]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 72, 56, 56]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[20]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[40]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[120]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[60]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 120, 14, 14]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[28]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 120, 28, 28]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[240]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 240, 14, 14]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 240, 28, 28]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[80]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[200]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[100]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 200, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[14]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 200, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[184]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[92]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 184, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 184, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[480]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 480, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[56]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[112]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[672]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[336]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 672, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[160]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[960]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 960, 3, 3]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[7]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        [
            "Tensor<[1, 960, 7, 7]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 672, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 672, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 480, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 480, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 184, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 184, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 200, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 200, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 240, 28, 28]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 240, 14, 14]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 120, 28, 28]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 120, 14, 14]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 72, 56, 56]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 72, 28, 28]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._to_copy.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._to_copy.default", input_strings
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
