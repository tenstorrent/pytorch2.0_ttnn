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
        return torch.ops.aten.sub.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.sub.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 32]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, 64, 1, 1]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 1, 1]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 1, 1]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 1, 1]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 1, 1]> self = ?", "Tensor<[1, 1024, 1, 1]> other = ?"],
        ["Tensor<[1, 2048, 1, 1]> self = ?", "Tensor<[1, 2048, 1, 1]> other = ?"],
        ["Tensor<[1, 15]> self = ?", "Tensor<[15, 1]> other = ?"],
        ["Tensor<[1, 1]> self = ?", "Tensor<[1, 1]> other = ?"],
        ["Tensor<[1, 2]> self = ?", "Tensor<[2, 1]> other = ?"],
        ["Tensor<[1, s0 + 1]> self = ?", "Tensor<[s0 + 1, 1]> other = ?"],
        ["Tensor<[1, 17]> self = ?", "Tensor<[17, 1]> other = ?"],
        ["Tensor<[30]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[40]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[30, 1]> self = ?", "Tensor<[30, 1]> other = ?"],
        ["Tensor<[40]> self = ?", "Tensor<[40]> other = ?"],
        ["Tensor<[60]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[80]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[60, 1]> self = ?", "Tensor<[60, 1]> other = ?"],
        ["Tensor<[80]> self = ?", "Tensor<[80]> other = ?"],
        ["Tensor<[120]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[160]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[120, 1]> self = ?", "Tensor<[120, 1]> other = ?"],
        ["Tensor<[160]> self = ?", "Tensor<[160]> other = ?"],
        ["Tensor<[240]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[320]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[240, 1]> self = ?", "Tensor<[240, 1]> other = ?"],
        ["Tensor<[320]> self = ?", "Tensor<[320]> other = ?"],
        ["Tensor<[480]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[640]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[480, 1]> self = ?", "Tensor<[480, 1]> other = ?"],
        ["Tensor<[640]> self = ?", "Tensor<[640]> other = ?"],
        ["Tensor<[1]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, 45]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, s0]> self = ?", "Tensor other = 1"],
        ["Tensor<[3, 320, 320]> self = ?", "Tensor<[3, 1, 1]> other = ?"],
        ["Tensor<[320, 1]> self = ?", "Tensor<[320, 1]> other = ?"],
        ["Tensor<[3234, 2]> self = ?", "Tensor<[3234, 2]> other = ?"],
        ["Tensor<[3234]> self = ?", "Tensor<[3234]> other = ?"],
        ["Tensor<[3234, 1]> self = ?", "Tensor<[3234, 1]> other = ?"],
        ["Tensor<[1, 59]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, 60]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, s10 + 1]> self = ?", "Tensor other = 1"],
        ["Tensor<[128]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[128, 1]> self = ?", "Tensor<[128, 1]> other = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[128]> other = ?"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor<[1, 1, 1, 42]> other = ?"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor<[1, 1, 32, 1]> other = ?"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor other = -3.75"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor other = -3.0"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor other = 2.25"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor other = -3.75"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor other = -3.0"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor other = 2.25"],
        ["Tensor<[1, 5]> self = ?", "Tensor other = 1"],
        ["Tensor<[3, 480, 640]> self = ?", "Tensor<[3, 1, 1]> other = ?"],
        ["Tensor<[800]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1066]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[800, 1]> self = ?", "Tensor<[800, 1]> other = ?"],
        ["Tensor<[1066]> self = ?", "Tensor<[1066]> other = ?"],
        ["Tensor<[0]> self = ?", "Tensor<[0]> other = ?"],
        ["Tensor<[0, 1]> self = ?", "Tensor<[0, 1]> other = ?"],
        ["Tensor<[24, 1]> self = ?", "Tensor<[1, 24]> other = ?"],
        ["Tensor<[300]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[300, 1]> self = ?", "Tensor<[300, 1]> other = ?"],
        ["Tensor<[300]> self = ?", "Tensor<[300]> other = ?"],
        ["Tensor<[8732, 2]> self = ?", "Tensor<[8732, 2]> other = ?"],
        ["Tensor<[8732]> self = ?", "Tensor<[8732]> other = ?"],
        ["Tensor<[8732, 1]> self = ?", "Tensor<[8732, 1]> other = ?"],
        ["Tensor<[64, 1, 49]> self = ?", "Tensor<[64, 49, 1]> other = ?"],
        ["Tensor<[16, 1, 49]> self = ?", "Tensor<[16, 49, 1]> other = ?"],
        ["Tensor<[4, 1, 49]> self = ?", "Tensor<[4, 49, 1]> other = ?"],
        ["Tensor<[64, 1, 64]> self = ?", "Tensor<[64, 64, 1]> other = ?"],
        ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, 1]> other = ?"],
        ["Tensor<[4, 1, 64]> self = ?", "Tensor<[4, 64, 1]> other = ?"],
        ["Tensor<[1, 10]> self = ?", "Tensor<[10, 1]> other = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.sub.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.sub.Tensor", input_strings)
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
