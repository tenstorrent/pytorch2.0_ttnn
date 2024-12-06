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
        return torch.ops.aten.t.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.t.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[128, 784]> self = ?"],
        ["Tensor<[64, 128]> self = ?"],
        ["Tensor<[12, 64]> self = ?"],
        ["Tensor<[3, 12]> self = ?"],
        ["Tensor<[12, 3]> self = ?"],
        ["Tensor<[64, 12]> self = ?"],
        ["Tensor<[128, 64]> self = ?"],
        ["Tensor<[784, 128]> self = ?"],
        ["Tensor<[1, 784]> self = ?"],
        ["Tensor<[1, 128]> self = ?"],
        ["Tensor<[1, 64]> self = ?"],
        ["Tensor<[1, 12]> self = ?"],
        ["Tensor<[1, 3]> self = ?"],
        ["Tensor<[1024, 1024]> self = ?"],
        ["Tensor<[4096, 1024]> self = ?"],
        ["Tensor<[1024, 4096]> self = ?"],
        ["Tensor<[2, 1024]> self = ?"],
        ["Tensor<[4608, 1536]> self = ?"],
        ["Tensor<[1536, 1536]> self = ?"],
        ["Tensor<[6144, 1536]> self = ?"],
        ["Tensor<[1536, 6144]> self = ?"],
        ["Tensor<[250880, 1536]> self = ?"],
        ["Tensor<[768, 768]> self = ?"],
        ["Tensor<[3072, 768]> self = ?"],
        ["Tensor<[768, 3072]> self = ?"],
        ["Tensor<[512, 512]> self = ?"],
        ["Tensor<[2048, 512]> self = ?"],
        ["Tensor<[512, 2048]> self = ?"],
        ["Tensor<[512, 768]> self = ?"],
        ["Tensor<[1, 512]> self = ?"],
        ["Tensor<[2, 1]> self = ?"],
        ["Tensor<[512, 1]> self = ?"],
        ["Tensor<[2, 512]> self = ?"],
        ["Tensor<[768, 512]> self = ?"],
        ["Tensor<[14, 512]> self = ?"],
        ["Tensor<[14, 2048]> self = ?"],
        ["Tensor<[50, 768]> self = ?"],
        ["Tensor<[50, 3072]> self = ?"],
        ["Tensor<[256, 256]> self = ?"],
        ["Tensor<[2048, 256]> self = ?"],
        ["Tensor<[256, 2048]> self = ?"],
        ["Tensor<[92, 256]> self = ?"],
        ["Tensor<[4, 256]> self = ?"],
        ["Tensor<[2, 768]> self = ?"],
        ["Tensor<[1, 768]> self = ?"],
        ["Tensor<[384, 512]> self = ?"],
        ["Tensor<[512, 384]> self = ?"],
        ["Tensor<[1024, 512]> self = ?"],
        ["Tensor<[512, 1024]> self = ?"],
        ["Tensor<[32128, 512]> self = ?"],
        ["Tensor<[64, 64]> self = ?"],
        ["Tensor<[256, 64]> self = ?"],
        ["Tensor<[64, 256]> self = ?"],
        ["Tensor<[128, 128]> self = ?"],
        ["Tensor<[512, 128]> self = ?"],
        ["Tensor<[128, 512]> self = ?"],
        ["Tensor<[320, 320]> self = ?"],
        ["Tensor<[1280, 320]> self = ?"],
        ["Tensor<[320, 1280]> self = ?"],
        ["Tensor<[50257, 768]> self = ?"],
        ["Tensor<[1000, 1024]> self = ?"],
        ["Tensor<[1024, 1000]> self = ?"],
        ["Tensor<[1, 1000]> self = ?"],
        ["Tensor<[256, 512]> self = ?"],
        ["Tensor<[512, 256]> self = ?"],
        ["Tensor<[1000, 512]> self = ?"],
        ["Tensor<[512, 1000]> self = ?"],
        ["Tensor<[128, 9216]> self = ?"],
        ["Tensor<[10, 128]> self = ?"],
        ["Tensor<[128, 10]> self = ?"],
        ["Tensor<[1, 10]> self = ?"],
        ["Tensor<[9216, 128]> self = ?"],
        ["Tensor<[1000, 1280]> self = ?"],
        ["Tensor<[50272, 512]> self = ?"],
        ["Tensor<[256, 1280]> self = ?"],
        ["Tensor<[256, 768]> self = ?"],
        ["Tensor<[1280, 768]> self = ?"],
        ["Tensor<[1280, 1280]> self = ?"],
        ["Tensor<[768, 1280]> self = ?"],
        ["Tensor<[1000, 2048]> self = ?"],
        ["Tensor<[2048, 1000]> self = ?"],
        ["Tensor<[250002, 768]> self = ?"],
        ["Tensor<[32, 32]> self = ?"],
        ["Tensor<[128, 32]> self = ?"],
        ["Tensor<[32, 128]> self = ?"],
        ["Tensor<[160, 160]> self = ?"],
        ["Tensor<[640, 160]> self = ?"],
        ["Tensor<[160, 640]> self = ?"],
        ["Tensor<[1024, 256]> self = ?"],
        ["Tensor<[256, 1024]> self = ?"],
        ["Tensor<[256, 32]> self = ?"],
        ["Tensor<[256, 160]> self = ?"],
        ["Tensor<[160, 1024]> self = ?"],
        ["Tensor<[160, 256]> self = ?"],
        ["Tensor<[4096, 256]> self = ?"],
        ["Tensor<[64, 4096]> self = ?"],
        ["Tensor<[16384, 256]> self = ?"],
        ["Tensor<[32, 16384]> self = ?"],
        ["Tensor<[32, 256]> self = ?"],
        ["Tensor<[1024, 160]> self = ?"],
        ["Tensor<[1024, 640]> self = ?"],
        ["Tensor<[4096, 64]> self = ?"],
        ["Tensor<[16384, 32]> self = ?"],
        ["Tensor<[16384, 128]> self = ?"],
        ["Tensor<[320, 768]> self = ?"],
        ["Tensor<[2560, 320]> self = ?"],
        ["Tensor<[640, 1280]> self = ?"],
        ["Tensor<[640, 640]> self = ?"],
        ["Tensor<[640, 768]> self = ?"],
        ["Tensor<[5120, 640]> self = ?"],
        ["Tensor<[640, 2560]> self = ?"],
        ["Tensor<[10240, 1280]> self = ?"],
        ["Tensor<[1280, 5120]> self = ?"],
        ["Tensor<[51865, 768]> self = ?"],
        ["Tensor<[256008, 1024]> self = ?"],
        ["Tensor<[192, 192]> self = ?"],
        ["Tensor<[768, 192]> self = ?"],
        ["Tensor<[192, 768]> self = ?"],
        ["Tensor<[92, 192]> self = ?"],
        ["Tensor<[4, 192]> self = ?"],
        ["Tensor<[768, 128]> self = ?"],
        ["Tensor<[128, 768]> self = ?"],
        ["Tensor<[30000, 128]> self = ?"],
        ["Tensor<[1024, 128]> self = ?"],
        ["Tensor<[128, 1024]> self = ?"],
        ["Tensor<[2048, 128]> self = ?"],
        ["Tensor<[2048, 2048]> self = ?"],
        ["Tensor<[8192, 2048]> self = ?"],
        ["Tensor<[2048, 8192]> self = ?"],
        ["Tensor<[128, 2048]> self = ?"],
        ["Tensor<[4096, 128]> self = ?"],
        ["Tensor<[4096, 4096]> self = ?"],
        ["Tensor<[16384, 4096]> self = ?"],
        ["Tensor<[4096, 16384]> self = ?"],
        ["Tensor<[128, 4096]> self = ?"],
        ["Tensor<[3072, 1024]> self = ?"],
        ["Tensor<[51200, 1024]> self = ?"],
        ["Tensor<[1000, 2208]> self = ?"],
        ["Tensor<[1000, 1664]> self = ?"],
        ["Tensor<[1000, 1920]> self = ?"],
        ["Tensor<[1000, 768]> self = ?"],
        ["Tensor<[768, 1000]> self = ?"],
        ["Tensor<[197, 768]> self = ?"],
        ["Tensor<[197, 3072]> self = ?"],
        ["Tensor<[1280, 1000]> self = ?"],
        ["Tensor<[1000, 1536]> self = ?"],
        ["Tensor<[1536, 1000]> self = ?"],
        ["Tensor<[197, 1024]> self = ?"],
        ["Tensor<[197, 4096]> self = ?"],
        ["Tensor<[384, 196]> self = ?"],
        ["Tensor<[196, 384]> self = ?"],
        ["Tensor<[21843, 768]> self = ?"],
        ["Tensor<[768, 21843]> self = ?"],
        ["Tensor<[1, 21843]> self = ?"],
        ["Tensor<[196, 768]> self = ?"],
        ["Tensor<[196, 3072]> self = ?"],
        ["Tensor<[768, 196]> self = ?"],
        ["Tensor<[768, 384]> self = ?"],
        ["Tensor<[1280, 960]> self = ?"],
        ["Tensor<[1024, 576]> self = ?"],
        ["Tensor<[1000, 912]> self = ?"],
        ["Tensor<[1000, 2520]> self = ?"],
        ["Tensor<[1000, 1008]> self = ?"],
        ["Tensor<[1000, 400]> self = ?"],
        ["Tensor<[1000, 672]> self = ?"],
        ["Tensor<[1000, 7392]> self = ?"],
        ["Tensor<[1000, 3024]> self = ?"],
        ["Tensor<[1000, 888]> self = ?"],
        ["Tensor<[1000, 3712]> self = ?"],
        ["Tensor<[1000, 1512]> self = ?"],
        ["Tensor<[1000, 440]> self = ?"],
        ["Tensor<[1000, 784]> self = ?"],
        ["Tensor<[1000, 2016]> self = ?"],
        ["Tensor<[384, 128]> self = ?"],
        ["Tensor<[768, 256]> self = ?"],
        ["Tensor<[1536, 512]> self = ?"],
        ["Tensor<[1024, 2048]> self = ?"],
        ["Tensor<[288, 96]> self = ?"],
        ["Tensor<[96, 96]> self = ?"],
        ["Tensor<[384, 96]> self = ?"],
        ["Tensor<[96, 384]> self = ?"],
        ["Tensor<[192, 384]> self = ?"],
        ["Tensor<[576, 192]> self = ?"],
        ["Tensor<[384, 768]> self = ?"],
        ["Tensor<[1152, 384]> self = ?"],
        ["Tensor<[384, 384]> self = ?"],
        ["Tensor<[1536, 384]> self = ?"],
        ["Tensor<[384, 1536]> self = ?"],
        ["Tensor<[768, 1536]> self = ?"],
        ["Tensor<[2304, 768]> self = ?"],
        ["Tensor<[512, 2]> self = ?"],
        ["Tensor<[4, 512]> self = ?"],
        ["Tensor<[8, 512]> self = ?"],
        ["Tensor<[16, 512]> self = ?"],
        ["Tensor<[32, 512]> self = ?"],
        ["Tensor<[3, 512]> self = ?"],
        ["Tensor<[6, 512]> self = ?"],
        ["Tensor<[12, 512]> self = ?"],
        ["Tensor<[24, 512]> self = ?"],
        ["Tensor<[32128, 768]> self = ?"],
        ["Tensor<[32128, 1024]> self = ?"],
        ["Tensor<[4096, 25088]> self = ?"],
        ["Tensor<[1000, 4096]> self = ?"],
        ["Tensor<[3840, 1280]> self = ?"],
        ["Tensor<[5120, 1280]> self = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.t.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.t.default", input_strings)
    if status == False:
        pytest.skip("Invalid input strings")
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
        metric["native_run"] = False

    if metric["native_run"] == True:
        result_after = None
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            ttnn.graph.begin_graph_capture()
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {e}")
            metric["run"] = False
        finally:
            trace = ttnn.graph.end_graph_capture()
            call_stack = ttnn.graph.extract_calltrace(trace)
            if metric["run"] == True:
                print(call_stack)
                expected_to_host_count = 0
                if result_after is None:
                    expected_to_host_count = 0
                elif isinstance(result_after, torch.Tensor):
                    expected_to_host_count = 1
                elif isinstance(result_after, (list, dict)):
                    expected_to_host_count = len(result_after)
                else:
                    print(f"Unexpected result_after type: {type(result_after)}")

                to_host_count = sum(["Tensor::cpu" in str(node) for node in call_stack])
                fallbacks_to_host_count = to_host_count - expected_to_host_count
                print(f"expected_to_host_count: {expected_to_host_count}")
                print(f"to_host_count: {to_host_count}")
                print(f"fallbacks_to_host_count: {fallbacks_to_host_count}")
                metric["ttnn_fallbacks_to_host_count"] = fallbacks_to_host_count
                return

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
