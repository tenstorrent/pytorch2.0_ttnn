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
        return torch.ops.aten.select.int(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.select.int")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 32, 16, 3, 96]> self = ?", "int dim = 3", "int index = 0"],
        ["Tensor<[1, 32, 16, 3, 96]> self = ?", "int dim = 3", "int index = 1"],
        ["Tensor<[1, 32, 16, 3, 96]> self = ?", "int dim = 3", "int index = 2"],
        ["Tensor<[1, 50, 768]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 1, 23, 40]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[6, 1, 100, 92]> self = ?", "int dim = 0", "int index = -1"],
        ["Tensor<[6, 1, 100, 4]> self = ?", "int dim = 0", "int index = -1"],
        ["Tensor<[1, 25, 768]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 2, 30, 40]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 2, 30, 40]> self = ?", "int dim = 1", "int index = 1"],
        ["Tensor<[1, 2, 60, 80]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 2, 60, 80]> self = ?", "int dim = 1", "int index = 1"],
        ["Tensor<[1, 2, 120, 160]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 2, 120, 160]> self = ?", "int dim = 1", "int index = 1"],
        ["Tensor<[1, 45]> self = ?", "int dim = 1", "int index = -1"],
        ["Tensor<[1, 50]> self = ?", "int dim = 1", "int index = -1"],
        ["Tensor<[1, 3, 320, 320]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3234, 4]> self = ?", "int dim = 1", "int index = 2"],
        ["Tensor<[3234, 4]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[3234, 4]> self = ?", "int dim = 1", "int index = 3"],
        ["Tensor<[3234, 4]> self = ?", "int dim = 1", "int index = 1"],
        ["Tensor<[1, 59]> self = ?", "int dim = 1", "int index = -1"],
        ["Tensor<[1, 1, 12, 16]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 16]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 12]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[1, 1, 51865]> self = ?", "int dim = 1", "int index = -1"],
        ["Tensor<[1, 4251, 192]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 5]> self = ?", "int dim = 1", "int index = -1"],
        ["Tensor<[1, 197, 768]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 3, 224, 224]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[1, 3, 224, 224]> self = ?", "int dim = 1", "int index = 1"],
        ["Tensor<[1, 3, 224, 224]> self = ?", "int dim = 1", "int index = 2"],
        ["Tensor<[1, 3, 480, 640]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[1, 3, 800, 1066]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[0, 4]> self = ?", "int dim = 1", "int index = 2"],
        ["Tensor<[0, 4]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[0, 4]> self = ?", "int dim = 1", "int index = 3"],
        ["Tensor<[0, 4]> self = ?", "int dim = 1", "int index = 1"],
        ["Tensor<[1, 3, 300, 300]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[8732, 4]> self = ?", "int dim = 1", "int index = 2"],
        ["Tensor<[8732, 4]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[8732, 4]> self = ?", "int dim = 1", "int index = 3"],
        ["Tensor<[8732, 4]> self = ?", "int dim = 1", "int index = 1"],
        ["Tensor<[3, 64, 4, 49, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 64, 4, 49, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 64, 4, 49, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 16, 8, 49, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 16, 8, 49, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 16, 8, 49, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 4, 16, 49, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 4, 16, 49, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 4, 16, 49, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 1, 32, 49, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 1, 32, 49, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 1, 32, 49, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 64, 3, 49, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 64, 3, 49, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 64, 3, 49, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 16, 6, 49, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 16, 6, 49, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 16, 6, 49, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 4, 12, 49, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 4, 12, 49, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 4, 12, 49, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 1, 24, 49, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 1, 24, 49, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 1, 24, 49, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 64, 4, 64, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 64, 4, 64, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 64, 4, 64, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 16, 8, 64, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 16, 8, 64, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 16, 8, 64, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 4, 16, 64, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 4, 16, 64, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 4, 16, 64, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 1, 32, 64, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 1, 32, 64, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 1, 32, 64, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 64, 3, 64, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 64, 3, 64, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 64, 3, 64, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 16, 6, 64, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 16, 6, 64, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 16, 6, 64, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 4, 12, 64, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 4, 12, 64, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 4, 12, 64, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 1, 24, 64, 32]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 1, 24, 64, 32]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 1, 24, 64, 32]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[1, 9, 768]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[3, 197, 1, 768]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 197, 1, 768]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 197, 1, 768]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 50, 1, 768]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 50, 1, 768]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 50, 1, 768]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[3, 1370, 1, 1280]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 1370, 1, 1280]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 1370, 1, 1280]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[1, 1370, 1280]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[3, 197, 1, 1024]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 197, 1, 1024]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 197, 1, 1024]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[1, 197, 1024]> self = ?", "int dim = 1", "int index = 0"],
        ["Tensor<[3, 50, 1, 1024]> self = ?", "int dim = 0", "int index = 0"],
        ["Tensor<[3, 50, 1, 1024]> self = ?", "int dim = 0", "int index = 1"],
        ["Tensor<[3, 50, 1, 1024]> self = ?", "int dim = 0", "int index = 2"],
        ["Tensor<[1, 50, 1024]> self = ?", "int dim = 1", "int index = 0"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.select.int",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.select.int", input_strings)
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
            assert metric["accuracy"] >= 0.99
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
