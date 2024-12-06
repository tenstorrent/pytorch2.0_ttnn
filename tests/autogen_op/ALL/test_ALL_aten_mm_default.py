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
        return torch.ops.aten.mm.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.mm.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 784]> self = ?", "Tensor<[784, 128]> mat2 = ?"],
        ["Tensor<[784, 1]> self = ?", "Tensor<[1, 128]> mat2 = ?"],
        ["Tensor<[1, 128]> self = ?", "Tensor<[128, 64]> mat2 = ?"],
        ["Tensor<[128, 1]> self = ?", "Tensor<[1, 64]> mat2 = ?"],
        ["Tensor<[1, 64]> self = ?", "Tensor<[64, 12]> mat2 = ?"],
        ["Tensor<[64, 1]> self = ?", "Tensor<[1, 12]> mat2 = ?"],
        ["Tensor<[1, 12]> self = ?", "Tensor<[12, 3]> mat2 = ?"],
        ["Tensor<[12, 1]> self = ?", "Tensor<[1, 3]> mat2 = ?"],
        ["Tensor<[1, 3]> self = ?", "Tensor<[3, 12]> mat2 = ?"],
        ["Tensor<[3, 1]> self = ?", "Tensor<[1, 12]> mat2 = ?"],
        ["Tensor<[1, 12]> self = ?", "Tensor<[12, 64]> mat2 = ?"],
        ["Tensor<[12, 1]> self = ?", "Tensor<[1, 64]> mat2 = ?"],
        ["Tensor<[1, 64]> self = ?", "Tensor<[64, 128]> mat2 = ?"],
        ["Tensor<[64, 1]> self = ?", "Tensor<[1, 128]> mat2 = ?"],
        ["Tensor<[1, 128]> self = ?", "Tensor<[128, 784]> mat2 = ?"],
        ["Tensor<[128, 1]> self = ?", "Tensor<[1, 784]> mat2 = ?"],
        ["Tensor<[32, 1536]> self = ?", "Tensor<[1536, 250880]> mat2 = ?"],
        ["Tensor<[1, 768]> self = ?", "Tensor<[768, 512]> mat2 = ?"],
        ["Tensor<[2, 512]> self = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[2, 512]> self = ?", "Tensor<[512, 1]> mat2 = ?"],
        ["Tensor<[1, 2]> self = ?", "Tensor<[2, 512]> mat2 = ?"],
        ["Tensor<[2, 1]> self = ?", "Tensor<[1, 512]> mat2 = ?"],
        ["Tensor<[512, 2]> self = ?", "Tensor<[2, 512]> mat2 = ?"],
        ["Tensor<[512, 1]> self = ?", "Tensor<[1, 768]> mat2 = ?"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[512, 768]> mat2 = ?"],
        ["Tensor<[14, 512]> self = ?", "Tensor<[512, 2048]> mat2 = ?"],
        ["Tensor<[512, 14]> self = ?", "Tensor<[14, 2048]> mat2 = ?"],
        ["Tensor<[14, 2048]> self = ?", "Tensor<[2048, 512]> mat2 = ?"],
        ["Tensor<[2048, 14]> self = ?", "Tensor<[14, 512]> mat2 = ?"],
        ["Tensor<[14, 512]> self = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[512, 14]> self = ?", "Tensor<[14, 512]> mat2 = ?"],
        ["Tensor<[50, 768]> self = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768, 50]> self = ?", "Tensor<[50, 3072]> mat2 = ?"],
        ["Tensor<[50, 3072]> self = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[3072, 50]> self = ?", "Tensor<[50, 768]> mat2 = ?"],
        ["Tensor<[50, 768]> self = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[768, 50]> self = ?", "Tensor<[50, 768]> mat2 = ?"],
        ["Tensor<[920, 256]> self = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[15, 512]> self = ?", "Tensor<[512, 384]> mat2 = ?"],
        ["Tensor<[15, 384]> self = ?", "Tensor<[384, 512]> mat2 = ?"],
        ["Tensor<[15, 512]> self = ?", "Tensor<[512, 1024]> mat2 = ?"],
        ["Tensor<[15, 1024]> self = ?", "Tensor<[1024, 512]> mat2 = ?"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[512, 384]> mat2 = ?"],
        ["Tensor<[1, 384]> self = ?", "Tensor<[384, 512]> mat2 = ?"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[512, 1024]> mat2 = ?"],
        ["Tensor<[1, 1024]> self = ?", "Tensor<[1024, 512]> mat2 = ?"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[512, 32128]> mat2 = ?"],
        ["Tensor<[7, 768]> self = ?", "Tensor<[768, 2]> mat2 = ?"],
        ["Tensor<[45, 768]> self = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[45, 768]> self = ?", "Tensor<[768, 50257]> mat2 = ?"],
        ["Tensor<[1, 768]> self = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[1, 768]> self = ?", "Tensor<[768, 50257]> mat2 = ?"],
        ["Tensor<[1, 1000]> self = ?", "Tensor<[1000, 1024]> mat2 = ?"],
        ["Tensor<[1000, 1]> self = ?", "Tensor<[1, 1024]> mat2 = ?"],
        ["Tensor<[1, 1000]> self = ?", "Tensor<[1000, 512]> mat2 = ?"],
        ["Tensor<[1000, 1]> self = ?", "Tensor<[1, 512]> mat2 = ?"],
        ["Tensor<[256, 512]> self = ?", "Tensor<[512, 256]> mat2 = ?"],
        ["Tensor<[512, 256]> self = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[256, 256]> self = ?", "Tensor<[256, 512]> mat2 = ?"],
        ["Tensor<[256, 512]> self = ?", "Tensor<[512, 768]> mat2 = ?"],
        ["Tensor<[512, 256]> self = ?", "Tensor<[256, 768]> mat2 = ?"],
        ["Tensor<[1, 10]> self = ?", "Tensor<[10, 128]> mat2 = ?"],
        ["Tensor<[10, 1]> self = ?", "Tensor<[1, 128]> mat2 = ?"],
        ["Tensor<[1, 128]> self = ?", "Tensor<[128, 9216]> mat2 = ?"],
        ["Tensor<[128, 1]> self = ?", "Tensor<[1, 9216]> mat2 = ?"],
        ["Tensor<[59, 512]> self = ?", "Tensor<[512, 1024]> mat2 = ?"],
        ["Tensor<[59, 1024]> self = ?", "Tensor<[1024, 512]> mat2 = ?"],
        ["Tensor<[59, 512]> self = ?", "Tensor<[512, 50272]> mat2 = ?"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[512, 50272]> mat2 = ?"],
        ["Tensor<[2048, 768]> self = ?", "Tensor<[768, 262]> mat2 = ?"],
        ["Tensor<[1, 1000]> self = ?", "Tensor<[1000, 2048]> mat2 = ?"],
        ["Tensor<[1000, 1]> self = ?", "Tensor<[1, 2048]> mat2 = ?"],
        ["Tensor<[16384, 32]> self = ?", "Tensor<[32, 256]> mat2 = ?"],
        ["Tensor<[4096, 64]> self = ?", "Tensor<[64, 256]> mat2 = ?"],
        ["Tensor<[1024, 160]> self = ?", "Tensor<[160, 256]> mat2 = ?"],
        ["Tensor<[256, 256]> self = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[256, 1024]> self = ?", "Tensor<[1024, 160]> mat2 = ?"],
        ["Tensor<[160, 256]> self = ?", "Tensor<[256, 1024]> mat2 = ?"],
        ["Tensor<[256, 4096]> self = ?", "Tensor<[4096, 64]> mat2 = ?"],
        ["Tensor<[64, 256]> self = ?", "Tensor<[256, 4096]> mat2 = ?"],
        ["Tensor<[256, 16384]> self = ?", "Tensor<[16384, 32]> mat2 = ?"],
        ["Tensor<[32, 256]> self = ?", "Tensor<[256, 16384]> mat2 = ?"],
        ["Tensor<[256, 256]> self = ?", "Tensor<[256, 1024]> mat2 = ?"],
        ["Tensor<[256, 1024]> self = ?", "Tensor<[1024, 256]> mat2 = ?"],
        ["Tensor<[1024, 256]> self = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[1024, 160]> self = ?", "Tensor<[160, 640]> mat2 = ?"],
        ["Tensor<[160, 1024]> self = ?", "Tensor<[1024, 640]> mat2 = ?"],
        ["Tensor<[1024, 640]> self = ?", "Tensor<[640, 160]> mat2 = ?"],
        ["Tensor<[640, 1024]> self = ?", "Tensor<[1024, 160]> mat2 = ?"],
        ["Tensor<[1024, 160]> self = ?", "Tensor<[160, 160]> mat2 = ?"],
        ["Tensor<[160, 1024]> self = ?", "Tensor<[1024, 160]> mat2 = ?"],
        ["Tensor<[256, 160]> self = ?", "Tensor<[160, 160]> mat2 = ?"],
        ["Tensor<[160, 256]> self = ?", "Tensor<[256, 160]> mat2 = ?"],
        ["Tensor<[64, 4096]> self = ?", "Tensor<[4096, 256]> mat2 = ?"],
        ["Tensor<[4096, 256]> self = ?", "Tensor<[256, 64]> mat2 = ?"],
        ["Tensor<[4096, 64]> self = ?", "Tensor<[64, 64]> mat2 = ?"],
        ["Tensor<[64, 4096]> self = ?", "Tensor<[4096, 64]> mat2 = ?"],
        ["Tensor<[256, 64]> self = ?", "Tensor<[64, 64]> mat2 = ?"],
        ["Tensor<[64, 256]> self = ?", "Tensor<[256, 64]> mat2 = ?"],
        ["Tensor<[16384, 32]> self = ?", "Tensor<[32, 128]> mat2 = ?"],
        ["Tensor<[32, 16384]> self = ?", "Tensor<[16384, 128]> mat2 = ?"],
        ["Tensor<[16384, 128]> self = ?", "Tensor<[128, 32]> mat2 = ?"],
        ["Tensor<[128, 16384]> self = ?", "Tensor<[16384, 32]> mat2 = ?"],
        ["Tensor<[16384, 32]> self = ?", "Tensor<[32, 32]> mat2 = ?"],
        ["Tensor<[32, 16384]> self = ?", "Tensor<[16384, 32]> mat2 = ?"],
        ["Tensor<[256, 32]> self = ?", "Tensor<[32, 32]> mat2 = ?"],
        ["Tensor<[32, 256]> self = ?", "Tensor<[256, 32]> mat2 = ?"],
        ["Tensor<[4096, 320]> self = ?", "Tensor<[320, 320]> mat2 = ?"],
        ["Tensor<[9, 768]> self = ?", "Tensor<[768, 320]> mat2 = ?"],
        ["Tensor<[s0*s1, 640]> self = ?", "Tensor<[640, 640]> mat2 = ?"],
        ["Tensor<[9, 768]> self = ?", "Tensor<[768, 640]> mat2 = ?"],
        ["Tensor<[s1*s2, 1280]> self = ?", "Tensor<[1280, 1280]> mat2 = ?"],
        ["Tensor<[9, 768]> self = ?", "Tensor<[768, 1280]> mat2 = ?"],
        ["Tensor<[s0*s1, 1280]> self = ?", "Tensor<[1280, 1280]> mat2 = ?"],
        ["Tensor<[s1*s2, 640]> self = ?", "Tensor<[640, 640]> mat2 = ?"],
        ["Tensor<[s1*s2, 320]> self = ?", "Tensor<[320, 320]> mat2 = ?"],
        ["Tensor<[1500, 768]> self = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[1, 768]> self = ?", "Tensor<[768, 51865]> mat2 = ?"],
        ["Tensor<[4, 768]> self = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[4, 768]> self = ?", "Tensor<[768, 51865]> mat2 = ?"],
        ["Tensor<[19, 1024]> self = ?", "Tensor<[1024, 256008]> mat2 = ?"],
        ["Tensor<[5, 1024]> self = ?", "Tensor<[1024, 3072]> mat2 = ?"],
        ["Tensor<[5, 1024]> self = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[1, 1024]> self = ?", "Tensor<[1024, 3072]> mat2 = ?"],
        ["Tensor<[1, 1024]> self = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[1, 1000]> self = ?", "Tensor<[1000, 768]> mat2 = ?"],
        ["Tensor<[1000, 1]> self = ?", "Tensor<[1, 768]> mat2 = ?"],
        ["Tensor<[197, 768]> self = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768, 197]> self = ?", "Tensor<[197, 3072]> mat2 = ?"],
        ["Tensor<[197, 3072]> self = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[3072, 197]> self = ?", "Tensor<[197, 768]> mat2 = ?"],
        ["Tensor<[197, 768]> self = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[768, 197]> self = ?", "Tensor<[197, 768]> mat2 = ?"],
        ["Tensor<[1, 1000]> self = ?", "Tensor<[1000, 1280]> mat2 = ?"],
        ["Tensor<[1000, 1]> self = ?", "Tensor<[1, 1280]> mat2 = ?"],
        ["Tensor<[1, 1000]> self = ?", "Tensor<[1000, 1536]> mat2 = ?"],
        ["Tensor<[1000, 1]> self = ?", "Tensor<[1, 1536]> mat2 = ?"],
        ["Tensor<[197, 1024]> self = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[197, 1024]> self = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024, 197]> self = ?", "Tensor<[197, 4096]> mat2 = ?"],
        ["Tensor<[197, 4096]> self = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[4096, 197]> self = ?", "Tensor<[197, 1024]> mat2 = ?"],
        ["Tensor<[1024, 197]> self = ?", "Tensor<[197, 1024]> mat2 = ?"],
        ["Tensor<[768, 196]> self = ?", "Tensor<[196, 384]> mat2 = ?"],
        ["Tensor<[1, 21843]> self = ?", "Tensor<[21843, 768]> mat2 = ?"],
        ["Tensor<[21843, 1]> self = ?", "Tensor<[1, 768]> mat2 = ?"],
        ["Tensor<[196, 768]> self = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768, 196]> self = ?", "Tensor<[196, 3072]> mat2 = ?"],
        ["Tensor<[196, 3072]> self = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[3072, 196]> self = ?", "Tensor<[196, 768]> mat2 = ?"],
        ["Tensor<[196, 768]> self = ?", "Tensor<[768, 384]> mat2 = ?"],
        ["Tensor<[384, 768]> self = ?", "Tensor<[768, 196]> mat2 = ?"],
        ["Tensor<[196, 384]> self = ?", "Tensor<[384, 768]> mat2 = ?"],
        ["Tensor<[784, 512]> self = ?", "Tensor<[512, 256]> mat2 = ?"],
        ["Tensor<[196, 1024]> self = ?", "Tensor<[1024, 512]> mat2 = ?"],
        ["Tensor<[49, 2048]> self = ?", "Tensor<[2048, 1024]> mat2 = ?"],
        ["Tensor<[784, 384]> self = ?", "Tensor<[384, 192]> mat2 = ?"],
        ["Tensor<[49, 1536]> self = ?", "Tensor<[1536, 768]> mat2 = ?"],
        ["Tensor<[225, 512]> self = ?", "Tensor<[512, 4]> mat2 = ?"],
        ["Tensor<[1024, 512]> self = ?", "Tensor<[512, 256]> mat2 = ?"],
        ["Tensor<[225, 512]> self = ?", "Tensor<[512, 8]> mat2 = ?"],
        ["Tensor<[256, 1024]> self = ?", "Tensor<[1024, 512]> mat2 = ?"],
        ["Tensor<[225, 512]> self = ?", "Tensor<[512, 16]> mat2 = ?"],
        ["Tensor<[64, 2048]> self = ?", "Tensor<[2048, 1024]> mat2 = ?"],
        ["Tensor<[225, 512]> self = ?", "Tensor<[512, 32]> mat2 = ?"],
        ["Tensor<[225, 512]> self = ?", "Tensor<[512, 3]> mat2 = ?"],
        ["Tensor<[1024, 384]> self = ?", "Tensor<[384, 192]> mat2 = ?"],
        ["Tensor<[225, 512]> self = ?", "Tensor<[512, 6]> mat2 = ?"],
        ["Tensor<[256, 768]> self = ?", "Tensor<[768, 384]> mat2 = ?"],
        ["Tensor<[225, 512]> self = ?", "Tensor<[512, 12]> mat2 = ?"],
        ["Tensor<[64, 1536]> self = ?", "Tensor<[1536, 768]> mat2 = ?"],
        ["Tensor<[225, 512]> self = ?", "Tensor<[512, 24]> mat2 = ?"],
        ["Tensor<[10, 768]> self = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[10, 768]> self = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[10, 3072]> self = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[1, 768]> self = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[1, 3072]> self = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[1, 768]> self = ?", "Tensor<[768, 32128]> mat2 = ?"],
        ["Tensor<[10, 1024]> self = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[10, 1024]> self = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[10, 4096]> self = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[1, 1024]> self = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1, 4096]> self = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[1, 1024]> self = ?", "Tensor<[1024, 32128]> mat2 = ?"],
        ["Tensor<[10, 512]> self = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[10, 512]> self = ?", "Tensor<[512, 2048]> mat2 = ?"],
        ["Tensor<[10, 2048]> self = ?", "Tensor<[2048, 512]> mat2 = ?"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[512, 2048]> mat2 = ?"],
        ["Tensor<[1, 2048]> self = ?", "Tensor<[2048, 512]> mat2 = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.mm.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.mm.default", input_strings)
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
