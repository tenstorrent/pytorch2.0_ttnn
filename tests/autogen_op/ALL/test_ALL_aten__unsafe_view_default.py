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
        return torch.ops.aten._unsafe_view.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten._unsafe_view.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 32, 16, 96]> self = ?", "List[int] size = [1, 32, 1536]"],
        ["Tensor<[1, 50, 12, 64]> self = ?", "List[int] size = [1, 50, 768]"],
        ["Tensor<[2, 7, 8, 64]> self = ?", "List[int] size = [2, 7, 512]"],
        ["Tensor<[2, 8, 7, 64]> self = ?", "List[int] size = [16, 7, 64]"],
        ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [14, 512]"],
        ["Tensor<[1, 7, 71, 64]> self = ?", "List[int] size = [1, 7, 4544]"],
        ["Tensor<[1, 16, 16, 16, 16, 3]> self = ?", "List[int] size = [1, 256, 768]"],
        ["Tensor<[1, 3, 16, 16, 16, 16]> self = ?", "List[int] size = [1, 3, 256, 256]"],
        ["Tensor<[1, 20, 20, 6, 4]> self = ?", "List[int] size = [1, 2400, 4]"],
        ["Tensor<[1, 10, 10, 6, 4]> self = ?", "List[int] size = [1, 600, 4]"],
        ["Tensor<[1, 5, 5, 6, 4]> self = ?", "List[int] size = [1, 150, 4]"],
        ["Tensor<[1, 3, 3, 6, 4]> self = ?", "List[int] size = [1, 54, 4]"],
        ["Tensor<[1, 2, 2, 6, 4]> self = ?", "List[int] size = [1, 24, 4]"],
        ["Tensor<[1, 20, 20, 6, 91]> self = ?", "List[int] size = [1, 2400, 91]"],
        ["Tensor<[1, 10, 10, 6, 91]> self = ?", "List[int] size = [1, 600, 91]"],
        ["Tensor<[1, 5, 5, 6, 91]> self = ?", "List[int] size = [1, 150, 91]"],
        ["Tensor<[1, 3, 3, 6, 91]> self = ?", "List[int] size = [1, 54, 91]"],
        ["Tensor<[1, 2, 2, 6, 91]> self = ?", "List[int] size = [1, 24, 91]"],
        ["Tensor<[20, 20]> self = ?", "List[int] size = [400]"],
        ["Tensor<[10, 10]> self = ?", "List[int] size = [100]"],
        ["Tensor<[5, 5]> self = ?", "List[int] size = [25]"],
        ["Tensor<[3, 3]> self = ?", "List[int] size = [9]"],
        ["Tensor<[2, 2]> self = ?", "List[int] size = [4]"],
        ["Tensor<[1, 59, 16, 64]> self = ?", "List[int] size = [1, 59, 1024]"],
        ["Tensor<[1, 256, 8, 32]> self = ?", "List[int] size = [1, 256, 256]"],
        ["Tensor<[1, 256, 5, 32]> self = ?", "List[int] size = [1, 256, 160]"],
        ["Tensor<[1, 1024, 5, 32]> self = ?", "List[int] size = [1, 1024, 160]"],
        ["Tensor<[1, 256, 2, 32]> self = ?", "List[int] size = [1, 256, 64]"],
        ["Tensor<[1, 4096, 2, 32]> self = ?", "List[int] size = [1, 4096, 64]"],
        ["Tensor<[1, 19, 16, 64]> self = ?", "List[int] size = [1, 19, 1024]"],
        ["Tensor<[1, 9, 12, 64]> self = ?", "List[int] size = [1, 9, 768]"],
        ["Tensor<[1, 12, 12, 64]> self = ?", "List[int] size = [1, 12, 768]"],
        ["Tensor<[1, 9, 16, 64]> self = ?", "List[int] size = [1, 9, 1024]"],
        ["Tensor<[1, 9, 16, 128]> self = ?", "List[int] size = [1, 9, 2048]"],
        ["Tensor<[1, 9, 64, 64]> self = ?", "List[int] size = [1, 9, 4096]"],
        ["Tensor<[1, 5, 4, 4, 64]> self = ?", "List[int] size = [1, 5, 16, 64]"],
        ["Tensor<[1, 1, 4, 4, 64]> self = ?", "List[int] size = [1, 1, 16, 64]"],
        ["Tensor<[1, 197, 12, 64]> self = ?", "List[int] size = [1, 197, 768]"],
        ["Tensor<[1, 197, 16, 64]> self = ?", "List[int] size = [1, 197, 1024]"],
        ["Tensor<[1, 100, 136, 9, 91]> self = ?", "List[int] size = [1, 122400, 91]"],
        ["Tensor<[1, 50, 68, 9, 91]> self = ?", "List[int] size = [1, 30600, 91]"],
        ["Tensor<[1, 25, 34, 9, 91]> self = ?", "List[int] size = [1, 7650, 91]"],
        ["Tensor<[1, 13, 17, 9, 91]> self = ?", "List[int] size = [1, 1989, 91]"],
        ["Tensor<[1, 7, 9, 9, 91]> self = ?", "List[int] size = [1, 567, 91]"],
        ["Tensor<[1, 100, 136, 9, 4]> self = ?", "List[int] size = [1, 122400, 4]"],
        ["Tensor<[1, 50, 68, 9, 4]> self = ?", "List[int] size = [1, 30600, 4]"],
        ["Tensor<[1, 25, 34, 9, 4]> self = ?", "List[int] size = [1, 7650, 4]"],
        ["Tensor<[1, 13, 17, 9, 4]> self = ?", "List[int] size = [1, 1989, 4]"],
        ["Tensor<[1, 7, 9, 9, 4]> self = ?", "List[int] size = [1, 567, 4]"],
        ["Tensor<[100, 136]> self = ?", "List[int] size = [13600]"],
        ["Tensor<[50, 68]> self = ?", "List[int] size = [3400]"],
        ["Tensor<[25, 34]> self = ?", "List[int] size = [850]"],
        ["Tensor<[13, 17]> self = ?", "List[int] size = [221]"],
        ["Tensor<[7, 9]> self = ?", "List[int] size = [63]"],
        ["Tensor<[1, 24, 12, 64]> self = ?", "List[int] size = [1, 24, 768]"],
        ["Tensor<[1, 38, 38, 4, 4]> self = ?", "List[int] size = [1, 5776, 4]"],
        ["Tensor<[1, 19, 19, 6, 4]> self = ?", "List[int] size = [1, 2166, 4]"],
        ["Tensor<[1, 3, 3, 4, 4]> self = ?", "List[int] size = [1, 36, 4]"],
        ["Tensor<[1, 38, 38, 4, 91]> self = ?", "List[int] size = [1, 5776, 91]"],
        ["Tensor<[1, 19, 19, 6, 91]> self = ?", "List[int] size = [1, 2166, 91]"],
        ["Tensor<[1, 3, 3, 4, 91]> self = ?", "List[int] size = [1, 36, 91]"],
        ["Tensor<[38, 38]> self = ?", "List[int] size = [1444]"],
        ["Tensor<[19, 19]> self = ?", "List[int] size = [361]"],
        ["Tensor<[1, 8, 8, 7, 7, 128]> self = ?", "List[int] size = [64, 49, 128]"],
        ["Tensor<[64, 4, 49, 32]> self = ?", "List[int] size = [256, 49, 32]"],
        ["Tensor<[64, 4, 32, 49]> self = ?", "List[int] size = [256, 32, 49]"],
        ["Tensor<[64, 49, 4, 32]> self = ?", "List[int] size = [64, 49, 128]"],
        ["Tensor<[1, 8, 7, 8, 7, 128]> self = ?", "List[int] size = [1, 56, 56, 128]"],
        ["Tensor<[8, 8, 7, 7]> self = ?", "List[int] size = [64, 49]"],
        ["Tensor<[1, 4, 4, 7, 7, 256]> self = ?", "List[int] size = [16, 49, 256]"],
        ["Tensor<[16, 8, 49, 32]> self = ?", "List[int] size = [128, 49, 32]"],
        ["Tensor<[16, 8, 32, 49]> self = ?", "List[int] size = [128, 32, 49]"],
        ["Tensor<[16, 49, 8, 32]> self = ?", "List[int] size = [16, 49, 256]"],
        ["Tensor<[1, 4, 7, 4, 7, 256]> self = ?", "List[int] size = [1, 28, 28, 256]"],
        ["Tensor<[4, 4, 7, 7]> self = ?", "List[int] size = [16, 49]"],
        ["Tensor<[1, 2, 2, 7, 7, 512]> self = ?", "List[int] size = [4, 49, 512]"],
        ["Tensor<[4, 16, 49, 32]> self = ?", "List[int] size = [64, 49, 32]"],
        ["Tensor<[4, 16, 32, 49]> self = ?", "List[int] size = [64, 32, 49]"],
        ["Tensor<[4, 49, 16, 32]> self = ?", "List[int] size = [4, 49, 512]"],
        ["Tensor<[1, 2, 7, 2, 7, 512]> self = ?", "List[int] size = [1, 14, 14, 512]"],
        ["Tensor<[2, 2, 7, 7]> self = ?", "List[int] size = [4, 49]"],
        ["Tensor<[1, 49, 32, 32]> self = ?", "List[int] size = [1, 49, 1024]"],
        ["Tensor<[1, 8, 8, 7, 7, 96]> self = ?", "List[int] size = [64, 49, 96]"],
        ["Tensor<[64, 3, 49, 32]> self = ?", "List[int] size = [192, 49, 32]"],
        ["Tensor<[64, 3, 32, 49]> self = ?", "List[int] size = [192, 32, 49]"],
        ["Tensor<[64, 49, 3, 32]> self = ?", "List[int] size = [64, 49, 96]"],
        ["Tensor<[1, 8, 7, 8, 7, 96]> self = ?", "List[int] size = [1, 56, 56, 96]"],
        ["Tensor<[1, 4, 4, 7, 7, 192]> self = ?", "List[int] size = [16, 49, 192]"],
        ["Tensor<[16, 6, 49, 32]> self = ?", "List[int] size = [96, 49, 32]"],
        ["Tensor<[16, 6, 32, 49]> self = ?", "List[int] size = [96, 32, 49]"],
        ["Tensor<[16, 49, 6, 32]> self = ?", "List[int] size = [16, 49, 192]"],
        ["Tensor<[1, 4, 7, 4, 7, 192]> self = ?", "List[int] size = [1, 28, 28, 192]"],
        ["Tensor<[1, 2, 2, 7, 7, 384]> self = ?", "List[int] size = [4, 49, 384]"],
        ["Tensor<[4, 12, 49, 32]> self = ?", "List[int] size = [48, 49, 32]"],
        ["Tensor<[4, 12, 32, 49]> self = ?", "List[int] size = [48, 32, 49]"],
        ["Tensor<[4, 49, 12, 32]> self = ?", "List[int] size = [4, 49, 384]"],
        ["Tensor<[1, 2, 7, 2, 7, 384]> self = ?", "List[int] size = [1, 14, 14, 384]"],
        ["Tensor<[1, 49, 24, 32]> self = ?", "List[int] size = [1, 49, 768]"],
        ["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "List[int] size = [64, 64, 128]"],
        ["Tensor<[64, 4, 64, 32]> self = ?", "List[int] size = [256, 64, 32]"],
        ["Tensor<[64, 4, 32, 64]> self = ?", "List[int] size = [256, 32, 64]"],
        ["Tensor<[64, 64, 4, 32]> self = ?", "List[int] size = [64, 64, 128]"],
        ["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "List[int] size = [1, 64, 64, 128]"],
        ["Tensor<[8, 8, 8, 8]> self = ?", "List[int] size = [64, 64]"],
        ["Tensor<[1, 4, 4, 8, 8, 256]> self = ?", "List[int] size = [16, 64, 256]"],
        ["Tensor<[16, 8, 64, 32]> self = ?", "List[int] size = [128, 64, 32]"],
        ["Tensor<[16, 8, 32, 64]> self = ?", "List[int] size = [128, 32, 64]"],
        ["Tensor<[16, 64, 8, 32]> self = ?", "List[int] size = [16, 64, 256]"],
        ["Tensor<[1, 4, 8, 4, 8, 256]> self = ?", "List[int] size = [1, 32, 32, 256]"],
        ["Tensor<[4, 4, 8, 8]> self = ?", "List[int] size = [16, 64]"],
        ["Tensor<[1, 2, 2, 8, 8, 512]> self = ?", "List[int] size = [4, 64, 512]"],
        ["Tensor<[4, 16, 64, 32]> self = ?", "List[int] size = [64, 64, 32]"],
        ["Tensor<[4, 16, 32, 64]> self = ?", "List[int] size = [64, 32, 64]"],
        ["Tensor<[4, 64, 16, 32]> self = ?", "List[int] size = [4, 64, 512]"],
        ["Tensor<[1, 2, 8, 2, 8, 512]> self = ?", "List[int] size = [1, 16, 16, 512]"],
        ["Tensor<[2, 2, 8, 8]> self = ?", "List[int] size = [4, 64]"],
        ["Tensor<[1, 64, 32, 32]> self = ?", "List[int] size = [1, 64, 1024]"],
        ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] size = [64, 64, 96]"],
        ["Tensor<[64, 3, 64, 32]> self = ?", "List[int] size = [192, 64, 32]"],
        ["Tensor<[64, 3, 32, 64]> self = ?", "List[int] size = [192, 32, 64]"],
        ["Tensor<[64, 64, 3, 32]> self = ?", "List[int] size = [64, 64, 96]"],
        ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] size = [1, 64, 64, 96]"],
        ["Tensor<[1, 4, 4, 8, 8, 192]> self = ?", "List[int] size = [16, 64, 192]"],
        ["Tensor<[16, 6, 64, 32]> self = ?", "List[int] size = [96, 64, 32]"],
        ["Tensor<[16, 6, 32, 64]> self = ?", "List[int] size = [96, 32, 64]"],
        ["Tensor<[16, 64, 6, 32]> self = ?", "List[int] size = [16, 64, 192]"],
        ["Tensor<[1, 4, 8, 4, 8, 192]> self = ?", "List[int] size = [1, 32, 32, 192]"],
        ["Tensor<[1, 2, 2, 8, 8, 384]> self = ?", "List[int] size = [4, 64, 384]"],
        ["Tensor<[4, 12, 64, 32]> self = ?", "List[int] size = [48, 64, 32]"],
        ["Tensor<[4, 12, 32, 64]> self = ?", "List[int] size = [48, 32, 64]"],
        ["Tensor<[4, 64, 12, 32]> self = ?", "List[int] size = [4, 64, 384]"],
        ["Tensor<[1, 2, 8, 2, 8, 384]> self = ?", "List[int] size = [1, 16, 16, 384]"],
        ["Tensor<[1, 64, 24, 32]> self = ?", "List[int] size = [1, 64, 768]"],
        ["Tensor<[1, 14, 12, 64]> self = ?", "List[int] size = [1, 14, 768]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._unsafe_view.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._unsafe_view.default", input_strings
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
