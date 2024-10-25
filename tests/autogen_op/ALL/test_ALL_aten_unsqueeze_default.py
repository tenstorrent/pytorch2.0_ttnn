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
        return torch.ops.aten.unsqueeze.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.unsqueeze.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 256]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 256]> self = ?", "int dim = 2"],
        ["Tensor<[1, 32]> self = ?", "int dim = 1"],
        ["Tensor<[16]> self = ?", "int dim = 1"],
        ["Tensor<[32, 32]> self = ?", "int dim = 0"],
        ["Tensor<[1, 32, 32]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 32]> self = ?", "int dim = 2"],
        ["Tensor<[7, 7]> self = ?", "int dim = 0"],
        ["Tensor<[1, 7, 7]> self = ?", "int dim = 1"],
        ["Tensor<[2, 7]> self = ?", "int dim = 1"],
        ["Tensor<[2, 1, 7]> self = ?", "int dim = 2"],
        ["Tensor<[1, 720, 1280]> self = ?", "int dim = 0"],
        ["Tensor<[23]> self = ?", "int dim = -1"],
        ["Tensor<[1, 23, 40]> self = ?", "int dim = 3"],
        ["Tensor<[100, 256]> self = ?", "int dim = 1"],
        ["Tensor<[1, 25]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 25]> self = ?", "int dim = 2"],
        ["Tensor<[1, 15]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 15]> self = ?", "int dim = 2"],
        ["Tensor<[15]> self = ?", "int dim = 1"],
        ["Tensor<[15]> self = ?", "int dim = 0"],
        ["Tensor<[6, 15, 15]> self = ?", "int dim = 0"],
        ["Tensor<[1]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1]> self = ?", "int dim = 2"],
        ["Tensor<[1, 1, 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 1]> self = ?", "int dim = 2"],
        ["Tensor<[1]> self = ?", "int dim = 1"],
        ["Tensor<[6, 1, 1]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1, 2]> self = ?", "int dim = 1"],
        ["Tensor<[1, 2]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 2]> self = ?", "int dim = 2"],
        ["Tensor<[2]> self = ?", "int dim = 1"],
        ["Tensor<[2]> self = ?", "int dim = 0"],
        ["Tensor<[6, 2, 2]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1, s0 + 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, s0 + 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, s0 + 1]> self = ?", "int dim = 2"],
        ["Tensor<[s0 + 1]> self = ?", "int dim = 1"],
        ["Tensor<[s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[6, s0 + 1, s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1, 17]> self = ?", "int dim = 1"],
        ["Tensor<[1, 17]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 17]> self = ?", "int dim = 2"],
        ["Tensor<[17]> self = ?", "int dim = 1"],
        ["Tensor<[17]> self = ?", "int dim = 0"],
        ["Tensor<[6, 17, 17]> self = ?", "int dim = 0"],
        ["Tensor<[7]> self = ?", "int dim = 0"],
        ["Tensor<[1, 7, 64]> self = ?", "int dim = 1"],
        ["Tensor<[30]> self = ?", "int dim = 1"],
        ["Tensor<[1, 30, 40]> self = ?", "int dim = 1"],
        ["Tensor<[60]> self = ?", "int dim = 1"],
        ["Tensor<[1, 60, 80]> self = ?", "int dim = 1"],
        ["Tensor<[120]> self = ?", "int dim = 1"],
        ["Tensor<[1, 120, 160]> self = ?", "int dim = 1"],
        ["Tensor<[240]> self = ?", "int dim = 1"],
        ["Tensor<[480]> self = ?", "int dim = 1"],
        ["Tensor<[1, 7]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 7]> self = ?", "int dim = 2"],
        ["Tensor<[1, 45]> self = ?", "int dim = 1"],
        ["Tensor<[45, 45]> self = ?", "int dim = 0"],
        ["Tensor<[1, 45, 45]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 45]> self = ?", "int dim = 2"],
        ["Tensor<[1, 46]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 46]> self = ?", "int dim = 2"],
        ["Tensor<[1, s10 + 1]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, s10 + 1]> self = ?", "int dim = 2"],
        ["Tensor<[32]> self = ?", "int dim = 0"],
        ["Tensor<[2048, 2048]> self = ?", "int dim = 0"],
        ["Tensor<[1, 2048, 2048]> self = ?", "int dim = 1"],
        ["Tensor<[64]> self = ?", "int dim = 0"],
        ["Tensor<[1, 64]> self = ?", "int dim = 2"],
        ["Tensor<[1, 512]> self = ?", "int dim = 2"],
        ["Tensor<[3]> self = ?", "int dim = 1"],
        ["Tensor<[3, 1]> self = ?", "int dim = 2"],
        ["Tensor<[3, 320, 320]> self = ?", "int dim = 0"],
        ["Tensor<[320]> self = ?", "int dim = 1"],
        ["Tensor<[3234]> self = ?", "int dim = 1"],
        ["Tensor<[59, 59]> self = ?", "int dim = 0"],
        ["Tensor<[1, 59, 59]> self = ?", "int dim = 1"],
        ["Tensor<[1, 59]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 59]> self = ?", "int dim = 2"],
        ["Tensor<[1, 60]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 60]> self = ?", "int dim = 2"],
        ["Tensor<[1, 2048]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 2048]> self = ?", "int dim = 2"],
        ["Tensor<[1, 10]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 10]> self = ?", "int dim = 2"],
        ["Tensor<[128]> self = ?", "int dim = 1"],
        ["Tensor<[1, 8]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 8]> self = ?", "int dim = 2"],
        ["Tensor<[160]> self = ?", "int dim = 0"],
        ["Tensor<[1, 320]> self = ?", "int dim = 2"],
        ["Tensor<[1, 320, 1]> self = ?", "int dim = 3"],
        ["Tensor<[1, 640]> self = ?", "int dim = 2"],
        ["Tensor<[1, 640, 1]> self = ?", "int dim = 3"],
        ["Tensor<[1, 1280]> self = ?", "int dim = 2"],
        ["Tensor<[1, 1280, 1]> self = ?", "int dim = 3"],
        ["Tensor<[16]> self = ?", "int dim = -1"],
        ["Tensor<[32]> self = ?", "int dim = -1"],
        ["Tensor<[64]> self = ?", "int dim = -1"],
        ["Tensor<[1, 384, 512]> self = ?", "int dim = 1"],
        ["Tensor<[12]> self = ?", "int dim = -1"],
        ["Tensor<[12, 16, 2]> self = ?", "int dim = 0"],
        ["Tensor<[1, 12, 16, 2]> self = ?", "int dim = 1"],
        ["Tensor<[1, 201]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 201]> self = ?", "int dim = 2"],
        ["Tensor<[19]> self = ?", "int dim = 0"],
        ["Tensor<[19, 19]> self = ?", "int dim = 0"],
        ["Tensor<[1, 19, 19]> self = ?", "int dim = 1"],
        ["Tensor<[1, 19]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 19]> self = ?", "int dim = 2"],
        ["Tensor<[1, 192]> self = ?", "int dim = 1"],
        ["Tensor<[1, 9]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 9]> self = ?", "int dim = 2"],
        ["Tensor<[1, 12]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 12]> self = ?", "int dim = 2"],
        ["Tensor<[1, 5]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 5]> self = ?", "int dim = 2"],
        ["Tensor<[1, 5, 16]> self = ?", "int dim = 2"],
        ["Tensor<[1, 5, 1, 16]> self = ?", "int dim = 4"],
        ["Tensor<[1, 6]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 6]> self = ?", "int dim = 2"],
        ["Tensor<[1, 1, 16]> self = ?", "int dim = 2"],
        ["Tensor<[1, 1, 1, 16]> self = ?", "int dim = 4"],
        ["Tensor<[56]> self = ?", "int dim = -1"],
        ["Tensor<[28]> self = ?", "int dim = -1"],
        ["Tensor<[14]> self = ?", "int dim = -1"],
        ["Tensor<[7]> self = ?", "int dim = -1"],
        ["Tensor<[1, 224, 224]> self = ?", "int dim = 1"],
        ["Tensor<[12, 197, 197]> self = ?", "int dim = 0"],
        ["Tensor<[1, 768]> self = ?", "int dim = 1"],
        ["Tensor<[16, 197, 197]> self = ?", "int dim = 0"],
        ["Tensor<[1, 1024]> self = ?", "int dim = 1"],
        ["Tensor<[3, 480, 640]> self = ?", "int dim = 0"],
        ["Tensor<[800]> self = ?", "int dim = 1"],
        ["Tensor<[50]> self = ?", "int dim = -1"],
        ["Tensor<[100]> self = ?", "int dim = -1"],
        ["Tensor<[0]> self = ?", "int dim = 1"],
        ["Tensor<[1, 24]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 24]> self = ?", "int dim = 2"],
        ["Tensor<[24]> self = ?", "int dim = 1"],
        ["Tensor<[24]> self = ?", "int dim = 0"],
        ["Tensor<[1, 256]> self = ?", "int dim = 0"],
        ["Tensor<[1, 512]> self = ?", "int dim = 1"],
        ["Tensor<[s0, 256]> self = ?", "int dim = 0"],
        ["Tensor<[98, 80]> self = ?", "int dim = 0"],
        ["Tensor<[300]> self = ?", "int dim = 1"],
        ["Tensor<[8732]> self = ?", "int dim = 1"],
        ["Tensor<[25]> self = ?", "int dim = 1"],
        ["Tensor<[4, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[64, 49]> self = ?", "int dim = 1"],
        ["Tensor<[64, 49]> self = ?", "int dim = 2"],
        ["Tensor<[64, 49, 49]> self = ?", "int dim = 1"],
        ["Tensor<[64, 1, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[8, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[16, 49]> self = ?", "int dim = 1"],
        ["Tensor<[16, 49]> self = ?", "int dim = 2"],
        ["Tensor<[16, 49, 49]> self = ?", "int dim = 1"],
        ["Tensor<[16, 1, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[16, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[4, 49]> self = ?", "int dim = 1"],
        ["Tensor<[4, 49]> self = ?", "int dim = 2"],
        ["Tensor<[4, 49, 49]> self = ?", "int dim = 1"],
        ["Tensor<[4, 1, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[32, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[3, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[6, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[12, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[24, 49, 49]> self = ?", "int dim = 0"],
        ["Tensor<[4, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[64, 64]> self = ?", "int dim = 1"],
        ["Tensor<[64, 64]> self = ?", "int dim = 2"],
        ["Tensor<[64, 64, 64]> self = ?", "int dim = 1"],
        ["Tensor<[64, 1, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[8, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[16, 64]> self = ?", "int dim = 1"],
        ["Tensor<[16, 64]> self = ?", "int dim = 2"],
        ["Tensor<[16, 64, 64]> self = ?", "int dim = 1"],
        ["Tensor<[16, 1, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[16, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[4, 64]> self = ?", "int dim = 1"],
        ["Tensor<[4, 64]> self = ?", "int dim = 2"],
        ["Tensor<[4, 64, 64]> self = ?", "int dim = 1"],
        ["Tensor<[4, 1, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[32, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[3, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[6, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[12, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[24, 64, 64]> self = ?", "int dim = 0"],
        ["Tensor<[10]> self = ?", "int dim = 1"],
        ["Tensor<[10]> self = ?", "int dim = 0"],
        ["Tensor<[12, 10, 10]> self = ?", "int dim = 0"],
        ["Tensor<[12, 1, 1]> self = ?", "int dim = 0"],
        ["Tensor<[12, 2, 2]> self = ?", "int dim = 0"],
        ["Tensor<[12, s0 + 1, s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[16, 10, 10]> self = ?", "int dim = 0"],
        ["Tensor<[16, 1, 1]> self = ?", "int dim = 0"],
        ["Tensor<[16, 2, 2]> self = ?", "int dim = 0"],
        ["Tensor<[16, s0 + 1, s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[8, 10, 10]> self = ?", "int dim = 0"],
        ["Tensor<[8, 1, 1]> self = ?", "int dim = 0"],
        ["Tensor<[8, 2, 2]> self = ?", "int dim = 0"],
        ["Tensor<[8, s0 + 1, s0 + 1]> self = ?", "int dim = 0"],
        ["Tensor<[1, 14]> self = ?", "int dim = 1"],
        ["Tensor<[1, 1, 14]> self = ?", "int dim = 2"],
        ["Tensor<[197, 1, 3, 768]> self = ?", "int dim = 0"],
        ["Tensor<[50, 1, 3, 768]> self = ?", "int dim = 0"],
        ["Tensor<[1370, 1, 3, 1280]> self = ?", "int dim = 0"],
        ["Tensor<[197, 1, 3, 1024]> self = ?", "int dim = 0"],
        ["Tensor<[50, 1, 3, 1024]> self = ?", "int dim = 0"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.unsqueeze.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.unsqueeze.default", input_strings
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
