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
        return torch.ops.aten.view.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/swin_v2_t", "aten.view.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 15, 15, 2]> self = ?", "List[int] size = [225, 2]"],
        ["Tensor<[225, 512]> self = ?", "List[int] size = [1, 15, 15, 512]"],
        ["Tensor<[1, 15, 15, 512]> self = ?", "List[int] size = [225, 512]"],
        ["Tensor<[225, 3]> self = ?", "List[int] size = [1, 15, 15, 3]"],
        ["Tensor<[1, 15, 15, 3]> self = ?", "List[int] size = [-1, 3]"],
        ["Tensor<[4096, 3]> self = ?", "List[int] size = [64, 64, -1]"],
        ["Tensor<[1, 64, 64, 96]> self = ?", "List[int] size = [1, 8, 8, 8, 8, 96]"],
        ["Tensor<[64, 64, 96]> self = ?", "List[int] size = [4096, 96]"],
        ["Tensor<[4096, 288]> self = ?", "List[int] size = [64, 64, 288]"],
        ["Tensor<[64, 64, 288]> self = ?", "List[int] size = [64, 64, 3, 3, 32]"],
        ["Tensor<[192, 64, 64]> self = ?", "List[int] size = [64, 3, 64, 64]"],
        ["Tensor<[64, 3, 64, 64]> self = ?", "List[int] size = [192, 64, 64]"],
        ["Tensor<[192, 64, 32]> self = ?", "List[int] size = [64, 3, 64, 32]"],
        ["Tensor<[4096, 96]> self = ?", "List[int] size = [64, 64, 96]"],
        ["Tensor<[64, 64, 96]> self = ?", "List[int] size = [1, 8, 8, 8, 8, 96]"],
        ["Tensor<[1, 64, 64, 96]> self = ?", "List[int] size = [4096, 96]"],
        ["Tensor<[4096, 384]> self = ?", "List[int] size = [1, 64, 64, 384]"],
        ["Tensor<[1, 64, 64, 384]> self = ?", "List[int] size = [4096, 384]"],
        ["Tensor<[4096, 96]> self = ?", "List[int] size = [1, 64, 64, 96]"],
        ["Tensor<[64, 64]> self = ?", "List[int] size = [8, 8, 8, 8]"],
        ["Tensor<[64, 3, 64, 64]> self = ?", "List[int] size = [1, 64, 3, 64, 64]"],
        ["Tensor<[1, 64, 3, 64, 64]> self = ?", "List[int] size = [-1, 3, 64, 64]"],
        ["Tensor<[1, 32, 32, 384]> self = ?", "List[int] size = [1024, 384]"],
        ["Tensor<[1024, 192]> self = ?", "List[int] size = [1, 32, 32, 192]"],
        ["Tensor<[225, 6]> self = ?", "List[int] size = [1, 15, 15, 6]"],
        ["Tensor<[1, 15, 15, 6]> self = ?", "List[int] size = [-1, 6]"],
        ["Tensor<[4096, 6]> self = ?", "List[int] size = [64, 64, -1]"],
        ["Tensor<[1, 32, 32, 192]> self = ?", "List[int] size = [1, 4, 8, 4, 8, 192]"],
        ["Tensor<[16, 64, 192]> self = ?", "List[int] size = [1024, 192]"],
        ["Tensor<[1024, 576]> self = ?", "List[int] size = [16, 64, 576]"],
        ["Tensor<[16, 64, 576]> self = ?", "List[int] size = [16, 64, 3, 6, 32]"],
        ["Tensor<[96, 64, 64]> self = ?", "List[int] size = [16, 6, 64, 64]"],
        ["Tensor<[16, 6, 64, 64]> self = ?", "List[int] size = [96, 64, 64]"],
        ["Tensor<[96, 64, 32]> self = ?", "List[int] size = [16, 6, 64, 32]"],
        ["Tensor<[1024, 192]> self = ?", "List[int] size = [16, 64, 192]"],
        ["Tensor<[16, 64, 192]> self = ?", "List[int] size = [1, 4, 4, 8, 8, 192]"],
        ["Tensor<[1, 32, 32, 192]> self = ?", "List[int] size = [1024, 192]"],
        ["Tensor<[1024, 768]> self = ?", "List[int] size = [1, 32, 32, 768]"],
        ["Tensor<[1, 32, 32, 768]> self = ?", "List[int] size = [1024, 768]"],
        ["Tensor<[32, 32]> self = ?", "List[int] size = [4, 8, 4, 8]"],
        ["Tensor<[16, 6, 64, 64]> self = ?", "List[int] size = [1, 16, 6, 64, 64]"],
        ["Tensor<[1, 16, 6, 64, 64]> self = ?", "List[int] size = [-1, 6, 64, 64]"],
        ["Tensor<[1, 16, 16, 768]> self = ?", "List[int] size = [256, 768]"],
        ["Tensor<[256, 384]> self = ?", "List[int] size = [1, 16, 16, 384]"],
        ["Tensor<[225, 12]> self = ?", "List[int] size = [1, 15, 15, 12]"],
        ["Tensor<[1, 15, 15, 12]> self = ?", "List[int] size = [-1, 12]"],
        ["Tensor<[4096, 12]> self = ?", "List[int] size = [64, 64, -1]"],
        ["Tensor<[1, 16, 16, 384]> self = ?", "List[int] size = [1, 2, 8, 2, 8, 384]"],
        ["Tensor<[4, 64, 384]> self = ?", "List[int] size = [256, 384]"],
        ["Tensor<[256, 1152]> self = ?", "List[int] size = [4, 64, 1152]"],
        ["Tensor<[4, 64, 1152]> self = ?", "List[int] size = [4, 64, 3, 12, 32]"],
        ["Tensor<[48, 64, 64]> self = ?", "List[int] size = [4, 12, 64, 64]"],
        ["Tensor<[4, 12, 64, 64]> self = ?", "List[int] size = [48, 64, 64]"],
        ["Tensor<[48, 64, 32]> self = ?", "List[int] size = [4, 12, 64, 32]"],
        ["Tensor<[256, 384]> self = ?", "List[int] size = [4, 64, 384]"],
        ["Tensor<[4, 64, 384]> self = ?", "List[int] size = [1, 2, 2, 8, 8, 384]"],
        ["Tensor<[1, 16, 16, 384]> self = ?", "List[int] size = [256, 384]"],
        ["Tensor<[256, 1536]> self = ?", "List[int] size = [1, 16, 16, 1536]"],
        ["Tensor<[1, 16, 16, 1536]> self = ?", "List[int] size = [256, 1536]"],
        ["Tensor<[16, 16]> self = ?", "List[int] size = [2, 8, 2, 8]"],
        ["Tensor<[4, 12, 64, 64]> self = ?", "List[int] size = [1, 4, 12, 64, 64]"],
        ["Tensor<[1, 4, 12, 64, 64]> self = ?", "List[int] size = [-1, 12, 64, 64]"],
        ["Tensor<[1, 8, 8, 1536]> self = ?", "List[int] size = [64, 1536]"],
        ["Tensor<[64, 768]> self = ?", "List[int] size = [1, 8, 8, 768]"],
        ["Tensor<[225, 24]> self = ?", "List[int] size = [1, 15, 15, 24]"],
        ["Tensor<[1, 15, 15, 24]> self = ?", "List[int] size = [-1, 24]"],
        ["Tensor<[4096, 24]> self = ?", "List[int] size = [64, 64, -1]"],
        ["Tensor<[1, 8, 8, 768]> self = ?", "List[int] size = [1, 1, 8, 1, 8, 768]"],
        ["Tensor<[1, 1, 1, 8, 8, 768]> self = ?", "List[int] size = [1, 64, 768]"],
        ["Tensor<[1, 64, 768]> self = ?", "List[int] size = [64, 768]"],
        ["Tensor<[64, 2304]> self = ?", "List[int] size = [1, 64, 2304]"],
        ["Tensor<[1, 64, 2304]> self = ?", "List[int] size = [1, 64, 3, 24, 32]"],
        ["Tensor<[1, 24, 64, 32]> self = ?", "List[int] size = [24, 64, 32]"],
        ["Tensor<[1, 24, 32, 64]> self = ?", "List[int] size = [24, 32, 64]"],
        ["Tensor<[24, 64, 64]> self = ?", "List[int] size = [1, 24, 64, 64]"],
        ["Tensor<[1, 24, 64, 64]> self = ?", "List[int] size = [24, 64, 64]"],
        ["Tensor<[24, 64, 32]> self = ?", "List[int] size = [1, 24, 64, 32]"],
        ["Tensor<[64, 768]> self = ?", "List[int] size = [1, 64, 768]"],
        ["Tensor<[1, 64, 768]> self = ?", "List[int] size = [1, 1, 1, 8, 8, 768]"],
        ["Tensor<[1, 1, 8, 1, 8, 768]> self = ?", "List[int] size = [1, 8, 8, 768]"],
        ["Tensor<[1, 8, 8, 768]> self = ?", "List[int] size = [64, 768]"],
        ["Tensor<[64, 3072]> self = ?", "List[int] size = [1, 8, 8, 3072]"],
        ["Tensor<[1, 8, 8, 3072]> self = ?", "List[int] size = [64, 3072]"],
        ["Tensor<[1, 768, 1, 1]> self = ?", "List[int] size = [1, 768]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.view.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.view.default", input_strings
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
