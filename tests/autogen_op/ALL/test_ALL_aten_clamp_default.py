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
        return torch.ops.aten.clamp.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.clamp.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[30]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[40]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[30]> self = ?", "Optional[number] min = ?", "Optional[number] max = 14"],
        ["Tensor<[40]> self = ?", "Optional[number] min = ?", "Optional[number] max = 19"],
        ["Tensor<[60]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[80]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[60]> self = ?", "Optional[number] min = ?", "Optional[number] max = 29"],
        ["Tensor<[80]> self = ?", "Optional[number] min = ?", "Optional[number] max = 39"],
        ["Tensor<[120]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[160]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[120]> self = ?", "Optional[number] min = ?", "Optional[number] max = 59"],
        ["Tensor<[160]> self = ?", "Optional[number] min = ?", "Optional[number] max = 79"],
        ["Tensor<[240]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[320]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[240]> self = ?", "Optional[number] min = ?", "Optional[number] max = 119"],
        ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 159"],
        ["Tensor<[480]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[640]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[480]> self = ?", "Optional[number] min = ?", "Optional[number] max = 239"],
        ["Tensor<[640]> self = ?", "Optional[number] min = ?", "Optional[number] max = 319"],
        ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 319"],
        ["Tensor<[6, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 1"],
        ["Tensor<[3234, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
        ["Tensor<[3234, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 320"],
        ["Tensor<[128]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 127"],
        ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 63"],
        ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 31"],
        ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 15"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Optional[number] min = 0", "Optional[number] max = 49"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Optional[number] min = 0", "Optional[number] max = 82"],
        ["Tensor<[800]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[1066]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[800]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
        ["Tensor<[1066]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
        ["Tensor<[0, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
        ["Tensor<[0, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 1066"],
        ["Tensor<[0, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 800"],
        ["Tensor<[300]> self = ?", "Optional[number] min = 0.0"],
        ["Tensor<[300]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
        ["Tensor<[300]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
        ["Tensor<[4, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 1"],
        ["Tensor<[8732, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
        ["Tensor<[8732, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 300"],
        ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
        ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
        ["Tensor<[4, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
        ["Tensor<[8, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
        ["Tensor<[16, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
        ["Tensor<[32, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
        ["Tensor<[3, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
        ["Tensor<[6, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
        ["Tensor<[12, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
        ["Tensor<[24, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.clamp.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.clamp.default", input_strings
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