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
        return torch.ops.aten.addmm.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/swin_v2_b", "aten.addmm.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[512]> self = ?", "Tensor<[225, 2]> mat1 = ?", "Tensor<[2, 512]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[4096, 128]> mat1 = ?", "Tensor<[128, 384]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[4096, 128]> mat1 = ?", "Tensor<[128, 128]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[4096, 128]> mat1 = ?", "Tensor<[128, 512]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[4096, 512]> mat1 = ?", "Tensor<[512, 128]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1024, 256]> mat1 = ?", "Tensor<[256, 768]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[1024, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[1024, 256]> mat1 = ?", "Tensor<[256, 1024]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[1024, 1024]> mat1 = ?", "Tensor<[1024, 256]> mat2 = ?"],
        ["Tensor<[1536]> self = ?", "Tensor<[256, 512]> mat1 = ?", "Tensor<[512, 1536]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[256, 512]> mat1 = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[256, 512]> mat1 = ?", "Tensor<[512, 2048]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[256, 2048]> mat1 = ?", "Tensor<[2048, 512]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[64, 1024]> mat1 = ?", "Tensor<[1024, 3072]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[64, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[64, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[64, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 1024]> mat1 = ?", "Tensor<[1024, 1000]> mat2 = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.addmm.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.addmm.default", input_strings
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
