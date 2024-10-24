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
        return torch.ops.aten.add.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/microsoft/beit-large-patch16-224-train", "aten.add.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 16, 197, 197]> self = ?", "Tensor<[1, 16, 197, 197]> other = ?"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor<[1, 197, 1024]> other = ?"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9956521736457944"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9913043472915888"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9869565209373832"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9826086945831776"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9782608672976494"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9739130418747663"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9695652164518833"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9652173891663551"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.960869561880827"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9565217345952988"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9521739110350609"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.947826087474823"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9434782639145851"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9391304366290569"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9347826093435287"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9304347857832909"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9260869547724724"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9217391312122345"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.917391300201416"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9130434766411781"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9086956530809402"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.9043478220701218"],
        ["Tensor<[1, 1, 1]> self = ?", "Tensor other = 0.8999999985098839"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.add.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.add.Tensor", input_strings)
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
