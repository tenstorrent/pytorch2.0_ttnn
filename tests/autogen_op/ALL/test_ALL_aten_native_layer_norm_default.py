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
        return torch.ops.aten.native_layer_norm.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.native_layer_norm.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 256, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 32, 1536]> input = ?",
            "List[int] normalized_shape = [1536]",
            "Optional[Tensor]<[1536]> weight = ?",
            "Optional[Tensor]<[1536]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 50, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[2, 7, 512]> input = ?",
            "List[int] normalized_shape = [512]",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[920, 1, 256]> input = ?",
            "List[int] normalized_shape = [256]",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[100, 1, 256]> input = ?",
            "List[int] normalized_shape = [256]",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 25, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 7, 4544]> input = ?",
            "List[int] normalized_shape = [4544]",
            "Optional[Tensor]<[4544]> weight = ?",
            "Optional[Tensor]<[4544]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 19200, 64]> input = ?",
            "List[int] normalized_shape = [64]",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 300, 64]> input = ?",
            "List[int] normalized_shape = [64]",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 4800, 128]> input = ?",
            "List[int] normalized_shape = [128]",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 300, 128]> input = ?",
            "List[int] normalized_shape = [128]",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1200, 320]> input = ?",
            "List[int] normalized_shape = [320]",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 300, 320]> input = ?",
            "List[int] normalized_shape = [320]",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 300, 512]> input = ?",
            "List[int] normalized_shape = [512]",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 7, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 45, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 512]> input = ?",
            "List[int] normalized_shape = [512]",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 59, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 1280]> input = ?",
            "List[int] normalized_shape = [1280]",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2048, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 10, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 16384, 32]> input = ?",
            "List[int] normalized_shape = [32]",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 32]> input = ?",
            "List[int] normalized_shape = [32]",
            "Optional[Tensor]<[32]> weight = ?",
            "Optional[Tensor]<[32]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 4096, 64]> input = ?",
            "List[int] normalized_shape = [64]",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 64]> input = ?",
            "List[int] normalized_shape = [64]",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1024, 160]> input = ?",
            "List[int] normalized_shape = [160]",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 160]> input = ?",
            "List[int] normalized_shape = [160]",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 256]> input = ?",
            "List[int] normalized_shape = [256]",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 8, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 4096, 320]> input = ?",
            "List[int] normalized_shape = [320]",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1024, 640]> input = ?",
            "List[int] normalized_shape = [640]",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 64, 1280]> input = ?",
            "List[int] normalized_shape = [1280]",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 201, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 1536]> input = ?",
            "List[int] normalized_shape = [1536]",
            "Optional[Tensor]<[1536]> weight = ?",
            "Optional[Tensor]<[1536]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1500, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 4, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 19, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1445, 192]> input = ?",
            "List[int] normalized_shape = [192]",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 9, 128]> input = ?",
            "List[int] normalized_shape = [128]",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 9, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 12, 128]> input = ?",
            "List[int] normalized_shape = [128]",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 12, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 9, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 9, 2048]> input = ?",
            "List[int] normalized_shape = [2048]",
            "Optional[Tensor]<[2048]> weight = ?",
            "Optional[Tensor]<[2048]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 9, 4096]> input = ?",
            "List[int] normalized_shape = [4096]",
            "Optional[Tensor]<[4096]> weight = ?",
            "Optional[Tensor]<[4096]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 5, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 16, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 197, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 197, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 196, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 24, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 56, 56, 128]> input = ?",
            "List[int] normalized_shape = [128]",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 28, 28, 512]> input = ?",
            "List[int] normalized_shape = [512]",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 28, 28, 256]> input = ?",
            "List[int] normalized_shape = [256]",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 14, 14, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 14, 14, 512]> input = ?",
            "List[int] normalized_shape = [512]",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 7, 7, 2048]> input = ?",
            "List[int] normalized_shape = [2048]",
            "Optional[Tensor]<[2048]> weight = ?",
            "Optional[Tensor]<[2048]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 7, 7, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 56, 56, 96]> input = ?",
            "List[int] normalized_shape = [96]",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 28, 28, 384]> input = ?",
            "List[int] normalized_shape = [384]",
            "Optional[Tensor]<[384]> weight = ?",
            "Optional[Tensor]<[384]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 28, 28, 192]> input = ?",
            "List[int] normalized_shape = [192]",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 14, 14, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 14, 14, 384]> input = ?",
            "List[int] normalized_shape = [384]",
            "Optional[Tensor]<[384]> weight = ?",
            "Optional[Tensor]<[384]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 7, 7, 1536]> input = ?",
            "List[int] normalized_shape = [1536]",
            "Optional[Tensor]<[1536]> weight = ?",
            "Optional[Tensor]<[1536]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 7, 7, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 64, 64, 128]> input = ?",
            "List[int] normalized_shape = [128]",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 32, 32, 256]> input = ?",
            "List[int] normalized_shape = [256]",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 16, 16, 512]> input = ?",
            "List[int] normalized_shape = [512]",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 8, 8, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 64, 64, 96]> input = ?",
            "List[int] normalized_shape = [96]",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 32, 32, 192]> input = ?",
            "List[int] normalized_shape = [192]",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 16, 16, 384]> input = ?",
            "List[int] normalized_shape = [384]",
            "Optional[Tensor]<[384]> weight = ?",
            "Optional[Tensor]<[384]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 8, 8, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 14, 128]> input = ?",
            "List[int] normalized_shape = [128]",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 14, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-12",
        ],
        [
            "Tensor<[1, 197, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 50, 768]> input = ?",
            "List[int] normalized_shape = [768]",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 1370, 1280]> input = ?",
            "List[int] normalized_shape = [1280]",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 197, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-06",
        ],
        [
            "Tensor<[1, 50, 1024]> input = ?",
            "List[int] normalized_shape = [1024]",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "float eps = 1e-06",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.native_layer_norm.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.native_layer_norm.default", input_strings
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
