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
        return torch.ops.aten.div.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.div.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 16, 256, 256]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[1, 1]> other = ?"],
        ["Tensor<[2, 512]> self = ?", "Tensor<[2, 1]> other = ?"],
        ["Tensor<[1, 23, 40]> self = ?", "Tensor<[1, 1, 40]> other = ?"],
        ["Tensor<[1, 23, 40]> self = ?", "Tensor<[1, 23, 1]> other = ?"],
        ["Tensor<[128]> self = ?", "Tensor other = 128"],
        ["Tensor<[1, 23, 40, 1]> self = ?", "Tensor<[128]> other = ?"],
        ["Tensor<[8, 920, 32]> self = ?", "Tensor other = 5.656854249492381"],
        ["Tensor<[8, 100, 32]> self = ?", "Tensor other = 5.656854249492381"],
        ["Tensor<[1, 12, 25, 25]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[15, 15]> self = ?", "Tensor other = 8"],
        ["Tensor<[15, 15]> self = ?", "Tensor other = 2.772588722239781"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 16"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 2.0794415416798357"],
        ["Tensor<[2, 2]> self = ?", "Tensor other = 16"],
        ["Tensor<[2, 2]> self = ?", "Tensor other = 2.0794415416798357"],
        ["Tensor<[s0 + 1, s0 + 1]> self = ?", "Tensor other = 16"],
        ["Tensor<[s0 + 1, s0 + 1]> self = ?", "Tensor other = 2.0794415416798357"],
        ["Tensor<[17, 17]> self = ?", "Tensor other = 16"],
        ["Tensor<[17, 17]> self = ?", "Tensor other = 2.0794415416798357"],
        ["Tensor<[1, 1, 19200, 300]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 2, 4800, 300]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 5, 1200, 300]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 8, 300, 300]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 12, 7, 7]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 50257]> self = ?", "Tensor other = 0.9"],
        ["Tensor<[3, 320, 320]> self = ?", "Tensor<[3, 1, 1]> other = ?"],
        ["Tensor<[20]> self = ?", "Tensor other = 20"],
        ["Tensor<[10]> self = ?", "Tensor other = 10"],
        ["Tensor<[5]> self = ?", "Tensor other = 5"],
        ["Tensor<[3]> self = ?", "Tensor other = 3"],
        ["Tensor<[2]> self = ?", "Tensor other = 2"],
        ["Tensor<[1]> self = ?", "Tensor other = 1"],
        ["Tensor<[3234, 1]> self = ?", "Tensor other = 10.0"],
        ["Tensor<[3234, 1]> self = ?", "Tensor other = 5.0"],
        ["Tensor<[]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 8, 256, 2048]> self = ?", "Tensor other = 5.656854249492381"],
        ["Tensor<[1, 8, 256, 256]> self = ?", "Tensor other = 5.656854249492381"],
        ["Tensor<[1, 8, 2048, 256]> self = ?", "Tensor other = 5.656854249492381"],
        ["Tensor<[1, 12, 10, 10]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 1, 16384, 256]> self = ?", "Tensor other = 5.656854249492381"],
        ["Tensor<[1, 2, 4096, 256]> self = ?", "Tensor other = 5.656854249492381"],
        ["Tensor<[1, 5, 1024, 256]> self = ?", "Tensor other = 5.656854249492381"],
        ["Tensor<[1, 16384, 32]> self = ?", "Tensor other = 0.9857142856344581"],
        ["Tensor<[1, 4096, 64]> self = ?", "Tensor other = 0.9714285712689161"],
        ["Tensor<[1, 4096, 64]> self = ?", "Tensor other = 0.9571428559720516"],
        ["Tensor<[1, 1024, 160]> self = ?", "Tensor other = 0.9428571425378323"],
        ["Tensor<[1, 1024, 160]> self = ?", "Tensor other = 0.9285714253783226"],
        ["Tensor<[1, 256, 256]> self = ?", "Tensor other = 0.9142857119441032"],
        ["Tensor<[1, 256, 256]> self = ?", "Tensor other = 0.8999999985098839"],
        ["Tensor<[160]> self = ?", "Tensor other = 160"],
        ["Tensor<[1, 320, 64, 64]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 4096, 320]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 640, s0, s1]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, s0*s1, 640]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 1280, s1, s2]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, s1*s2, 1280]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 1280, s0, s1]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 1280, s0, s1]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, s0*s1, 1280]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 1280, 8, 8]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 640, s1, s2]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, s1*s2, 640]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 320, s1, s2]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, s1*s2, 320]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 3, 1445, 1445]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 12, 9, 9]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 12, 12, 12]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 16, 9, 9]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 16, 9, 9]> self = ?", "Tensor other = 11.313708498984761"],
        ["Tensor<[1, 64, 9, 9]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 16, 5, 5]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 16, 1, 6]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 16, 1, s10 + 1]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 12, 16, 64]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 12, 197, 197]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.9909090911969543"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.9818181823939085"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.9727272726595402"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.963636364787817"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.9545454569160938"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.94545454159379"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.9363636374473572"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.9272727221250534"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.9181818142533302"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.9090909063816071"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor other = 0.8999999985098839"],
        ["Tensor<[1, 16, 197, 197]> self = ?", "Tensor other = 8.0"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9956521736457944"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9913043472915888"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9869565209373832"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9826086945831776"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9782608672976494"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9739130418747663"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9695652164518833"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9652173891663551"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.960869561880827"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9565217345952988"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9521739110350609"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.947826087474823"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9434782639145851"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9391304366290569"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9347826093435287"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9304347857832909"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9260869547724724"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9217391312122345"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.917391300201416"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9130434766411781"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9086956530809402"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.9043478220701218"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor other = 0.8999999985098839"],
        ["Tensor<[3, 480, 640]> self = ?", "Tensor<[3, 1, 1]> other = ?"],
        ["Tensor<[0, 1]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 512, 38, 38]> self = ?", "Tensor<[1, 512, 38, 38]> other = ?"],
        ["Tensor<[38]> self = ?", "Tensor other = 37.5"],
        ["Tensor<[19]> self = ?", "Tensor other = 18.75"],
        ["Tensor<[10]> self = ?", "Tensor other = 9.375"],
        ["Tensor<[5]> self = ?", "Tensor other = 4.6875"],
        ["Tensor<[3]> self = ?", "Tensor other = 3.0"],
        ["Tensor<[1]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[8732, 1]> self = ?", "Tensor other = 10.0"],
        ["Tensor<[8732, 1]> self = ?", "Tensor other = 5.0"],
        ["Tensor<[64, 4, 64, 32]> self = ?", "Tensor<[64, 4, 64, 32]> other = ?"],
        ["Tensor<[16, 8, 64, 32]> self = ?", "Tensor<[16, 8, 64, 32]> other = ?"],
        ["Tensor<[4, 16, 64, 32]> self = ?", "Tensor<[4, 16, 64, 32]> other = ?"],
        ["Tensor<[1, 32, 64, 32]> self = ?", "Tensor<[1, 32, 64, 32]> other = ?"],
        ["Tensor<[64, 3, 64, 32]> self = ?", "Tensor<[64, 3, 64, 32]> other = ?"],
        ["Tensor<[16, 6, 64, 32]> self = ?", "Tensor<[16, 6, 64, 32]> other = ?"],
        ["Tensor<[4, 12, 64, 32]> self = ?", "Tensor<[4, 12, 64, 32]> other = ?"],
        ["Tensor<[1, 24, 64, 32]> self = ?", "Tensor<[1, 24, 64, 32]> other = ?"],
        ["Tensor<[10, 10]> self = ?", "Tensor other = 8"],
        ["Tensor<[10, 10]> self = ?", "Tensor other = 2.772588722239781"],
        ["Tensor<[1, 12, 14, 14]> self = ?", "Tensor other = 8.0"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.div.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.div.Tensor", input_strings)
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
