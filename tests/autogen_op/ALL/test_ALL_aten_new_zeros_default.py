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
        return torch.ops.aten.new_zeros.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.new_zeros.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[2, 512]> self = ?",
            "List[int] size = [2, 7, 512]",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "List[int] size = [1, 256, 16, 16]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "List[int] size = [1, 256, 32, 32]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "List[int] size = [1, 256, 64, 64]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "List[int] size = [1, 256, 128, 128]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 19]> self = ?", "List[int] size = [1, 19]", "Optional[bool] pin_memory = False"],
        ["Tensor<[160, 7, 7]> self = ?", "List[int] size = [7840]"],
        ["Tensor<[112, 14, 14]> self = ?", "List[int] size = [21952]"],
        ["Tensor<[80, 14, 14]> self = ?", "List[int] size = [15680]"],
        ["Tensor<[40, 28, 28]> self = ?", "List[int] size = [31360]"],
        ["Tensor<[24, 56, 56]> self = ?", "List[int] size = [75264]"],
        ["Tensor<[16, 112, 112]> self = ?", "List[int] size = [200704]"],
        [
            "Tensor<[1, 960, 7, 7]> self = ?",
            "List[int] size = [1, 960, 3, 3]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 672, 14, 14]> self = ?",
            "List[int] size = [1, 672, 7, 7]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 480, 14, 14]> self = ?",
            "List[int] size = [1, 480, 7, 7]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 184, 14, 14]> self = ?",
            "List[int] size = [1, 184, 7, 7]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 200, 14, 14]> self = ?",
            "List[int] size = [1, 200, 7, 7]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 240, 28, 28]> self = ?",
            "List[int] size = [1, 240, 14, 14]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 120, 28, 28]> self = ?",
            "List[int] size = [1, 120, 14, 14]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 72, 56, 56]> self = ?",
            "List[int] size = [1, 72, 28, 28]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 72, 14, 14]> self = ?",
            "List[int] size = [1, 72, 7, 7]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 36, 28, 28]> self = ?",
            "List[int] size = [1, 36, 7, 7]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 36, 28, 28]> self = ?",
            "List[int] size = [1, 36, 14, 14]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 18, 56, 56]> self = ?",
            "List[int] size = [1, 18, 7, 7]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 18, 56, 56]> self = ?",
            "List[int] size = [1, 18, 14, 14]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 18, 56, 56]> self = ?",
            "List[int] size = [1, 18, 28, 28]",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[38809, 12]> self = ?",
            "List[int] size = [732, 12]",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[38809, 16]> self = ?",
            "List[int] size = [732, 16]",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[64, 49, 128]> self = ?", "List[int] size = [56, 56]", "Optional[bool] pin_memory = False"],
        ["Tensor<[16, 49, 256]> self = ?", "List[int] size = [28, 28]", "Optional[bool] pin_memory = False"],
        ["Tensor<[4, 49, 512]> self = ?", "List[int] size = [14, 14]", "Optional[bool] pin_memory = False"],
        ["Tensor<[64, 49, 96]> self = ?", "List[int] size = [56, 56]", "Optional[bool] pin_memory = False"],
        ["Tensor<[16, 49, 192]> self = ?", "List[int] size = [28, 28]", "Optional[bool] pin_memory = False"],
        ["Tensor<[4, 49, 384]> self = ?", "List[int] size = [14, 14]", "Optional[bool] pin_memory = False"],
        ["Tensor<[64, 64, 128]> self = ?", "List[int] size = [64, 64]", "Optional[bool] pin_memory = False"],
        ["Tensor<[16, 64, 256]> self = ?", "List[int] size = [32, 32]", "Optional[bool] pin_memory = False"],
        ["Tensor<[4, 64, 512]> self = ?", "List[int] size = [16, 16]", "Optional[bool] pin_memory = False"],
        ["Tensor<[64, 64, 96]> self = ?", "List[int] size = [64, 64]", "Optional[bool] pin_memory = False"],
        ["Tensor<[16, 64, 192]> self = ?", "List[int] size = [32, 32]", "Optional[bool] pin_memory = False"],
        ["Tensor<[4, 64, 384]> self = ?", "List[int] size = [16, 16]", "Optional[bool] pin_memory = False"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.new_zeros.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.new_zeros.default", input_strings
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