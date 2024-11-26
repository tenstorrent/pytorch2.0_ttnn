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
        return torch.ops.aten._native_batch_norm_legit_no_training.default(*args, **kwargs)[0]


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/densenet121", "aten._native_batch_norm_legit_no_training.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 64, 112, 112]> input = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "Tensor<[64]> running_mean = ?",
            "Tensor<[64]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 64, 56, 56]> input = ?",
            "Optional[Tensor]<[64]> weight = ?",
            "Optional[Tensor]<[64]> bias = ?",
            "Tensor<[64]> running_mean = ?",
            "Tensor<[64]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 128, 56, 56]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "Tensor<[128]> running_mean = ?",
            "Tensor<[128]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 96, 56, 56]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> bias = ?",
            "Tensor<[96]> running_mean = ?",
            "Tensor<[96]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 160, 56, 56]> input = ?",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> bias = ?",
            "Tensor<[160]> running_mean = ?",
            "Tensor<[160]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 192, 56, 56]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "Tensor<[192]> running_mean = ?",
            "Tensor<[192]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 224, 56, 56]> input = ?",
            "Optional[Tensor]<[224]> weight = ?",
            "Optional[Tensor]<[224]> bias = ?",
            "Tensor<[224]> running_mean = ?",
            "Tensor<[224]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 56, 56]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "Tensor<[256]> running_mean = ?",
            "Tensor<[256]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 128, 28, 28]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "Tensor<[128]> running_mean = ?",
            "Tensor<[128]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 160, 28, 28]> input = ?",
            "Optional[Tensor]<[160]> weight = ?",
            "Optional[Tensor]<[160]> bias = ?",
            "Tensor<[160]> running_mean = ?",
            "Tensor<[160]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 192, 28, 28]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "Tensor<[192]> running_mean = ?",
            "Tensor<[192]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 224, 28, 28]> input = ?",
            "Optional[Tensor]<[224]> weight = ?",
            "Optional[Tensor]<[224]> bias = ?",
            "Tensor<[224]> running_mean = ?",
            "Tensor<[224]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 28, 28]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "Tensor<[256]> running_mean = ?",
            "Tensor<[256]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 288, 28, 28]> input = ?",
            "Optional[Tensor]<[288]> weight = ?",
            "Optional[Tensor]<[288]> bias = ?",
            "Tensor<[288]> running_mean = ?",
            "Tensor<[288]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 320, 28, 28]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "Tensor<[320]> running_mean = ?",
            "Tensor<[320]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 352, 28, 28]> input = ?",
            "Optional[Tensor]<[352]> weight = ?",
            "Optional[Tensor]<[352]> bias = ?",
            "Tensor<[352]> running_mean = ?",
            "Tensor<[352]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 384, 28, 28]> input = ?",
            "Optional[Tensor]<[384]> weight = ?",
            "Optional[Tensor]<[384]> bias = ?",
            "Tensor<[384]> running_mean = ?",
            "Tensor<[384]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 416, 28, 28]> input = ?",
            "Optional[Tensor]<[416]> weight = ?",
            "Optional[Tensor]<[416]> bias = ?",
            "Tensor<[416]> running_mean = ?",
            "Tensor<[416]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 448, 28, 28]> input = ?",
            "Optional[Tensor]<[448]> weight = ?",
            "Optional[Tensor]<[448]> bias = ?",
            "Tensor<[448]> running_mean = ?",
            "Tensor<[448]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 480, 28, 28]> input = ?",
            "Optional[Tensor]<[480]> weight = ?",
            "Optional[Tensor]<[480]> bias = ?",
            "Tensor<[480]> running_mean = ?",
            "Tensor<[480]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 512, 28, 28]> input = ?",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "Tensor<[512]> running_mean = ?",
            "Tensor<[512]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 256, 14, 14]> input = ?",
            "Optional[Tensor]<[256]> weight = ?",
            "Optional[Tensor]<[256]> bias = ?",
            "Tensor<[256]> running_mean = ?",
            "Tensor<[256]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 128, 14, 14]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "Tensor<[128]> running_mean = ?",
            "Tensor<[128]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 288, 14, 14]> input = ?",
            "Optional[Tensor]<[288]> weight = ?",
            "Optional[Tensor]<[288]> bias = ?",
            "Tensor<[288]> running_mean = ?",
            "Tensor<[288]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 320, 14, 14]> input = ?",
            "Optional[Tensor]<[320]> weight = ?",
            "Optional[Tensor]<[320]> bias = ?",
            "Tensor<[320]> running_mean = ?",
            "Tensor<[320]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 352, 14, 14]> input = ?",
            "Optional[Tensor]<[352]> weight = ?",
            "Optional[Tensor]<[352]> bias = ?",
            "Tensor<[352]> running_mean = ?",
            "Tensor<[352]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 384, 14, 14]> input = ?",
            "Optional[Tensor]<[384]> weight = ?",
            "Optional[Tensor]<[384]> bias = ?",
            "Tensor<[384]> running_mean = ?",
            "Tensor<[384]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 416, 14, 14]> input = ?",
            "Optional[Tensor]<[416]> weight = ?",
            "Optional[Tensor]<[416]> bias = ?",
            "Tensor<[416]> running_mean = ?",
            "Tensor<[416]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 448, 14, 14]> input = ?",
            "Optional[Tensor]<[448]> weight = ?",
            "Optional[Tensor]<[448]> bias = ?",
            "Tensor<[448]> running_mean = ?",
            "Tensor<[448]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 480, 14, 14]> input = ?",
            "Optional[Tensor]<[480]> weight = ?",
            "Optional[Tensor]<[480]> bias = ?",
            "Tensor<[480]> running_mean = ?",
            "Tensor<[480]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 512, 14, 14]> input = ?",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "Tensor<[512]> running_mean = ?",
            "Tensor<[512]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 544, 14, 14]> input = ?",
            "Optional[Tensor]<[544]> weight = ?",
            "Optional[Tensor]<[544]> bias = ?",
            "Tensor<[544]> running_mean = ?",
            "Tensor<[544]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 576, 14, 14]> input = ?",
            "Optional[Tensor]<[576]> weight = ?",
            "Optional[Tensor]<[576]> bias = ?",
            "Tensor<[576]> running_mean = ?",
            "Tensor<[576]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 608, 14, 14]> input = ?",
            "Optional[Tensor]<[608]> weight = ?",
            "Optional[Tensor]<[608]> bias = ?",
            "Tensor<[608]> running_mean = ?",
            "Tensor<[608]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 640, 14, 14]> input = ?",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> bias = ?",
            "Tensor<[640]> running_mean = ?",
            "Tensor<[640]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 672, 14, 14]> input = ?",
            "Optional[Tensor]<[672]> weight = ?",
            "Optional[Tensor]<[672]> bias = ?",
            "Tensor<[672]> running_mean = ?",
            "Tensor<[672]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 704, 14, 14]> input = ?",
            "Optional[Tensor]<[704]> weight = ?",
            "Optional[Tensor]<[704]> bias = ?",
            "Tensor<[704]> running_mean = ?",
            "Tensor<[704]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 736, 14, 14]> input = ?",
            "Optional[Tensor]<[736]> weight = ?",
            "Optional[Tensor]<[736]> bias = ?",
            "Tensor<[736]> running_mean = ?",
            "Tensor<[736]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 768, 14, 14]> input = ?",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "Tensor<[768]> running_mean = ?",
            "Tensor<[768]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 800, 14, 14]> input = ?",
            "Optional[Tensor]<[800]> weight = ?",
            "Optional[Tensor]<[800]> bias = ?",
            "Tensor<[800]> running_mean = ?",
            "Tensor<[800]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 832, 14, 14]> input = ?",
            "Optional[Tensor]<[832]> weight = ?",
            "Optional[Tensor]<[832]> bias = ?",
            "Tensor<[832]> running_mean = ?",
            "Tensor<[832]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 864, 14, 14]> input = ?",
            "Optional[Tensor]<[864]> weight = ?",
            "Optional[Tensor]<[864]> bias = ?",
            "Tensor<[864]> running_mean = ?",
            "Tensor<[864]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 896, 14, 14]> input = ?",
            "Optional[Tensor]<[896]> weight = ?",
            "Optional[Tensor]<[896]> bias = ?",
            "Tensor<[896]> running_mean = ?",
            "Tensor<[896]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 928, 14, 14]> input = ?",
            "Optional[Tensor]<[928]> weight = ?",
            "Optional[Tensor]<[928]> bias = ?",
            "Tensor<[928]> running_mean = ?",
            "Tensor<[928]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 960, 14, 14]> input = ?",
            "Optional[Tensor]<[960]> weight = ?",
            "Optional[Tensor]<[960]> bias = ?",
            "Tensor<[960]> running_mean = ?",
            "Tensor<[960]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 992, 14, 14]> input = ?",
            "Optional[Tensor]<[992]> weight = ?",
            "Optional[Tensor]<[992]> bias = ?",
            "Tensor<[992]> running_mean = ?",
            "Tensor<[992]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1024, 14, 14]> input = ?",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "Tensor<[1024]> running_mean = ?",
            "Tensor<[1024]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 512, 7, 7]> input = ?",
            "Optional[Tensor]<[512]> weight = ?",
            "Optional[Tensor]<[512]> bias = ?",
            "Tensor<[512]> running_mean = ?",
            "Tensor<[512]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 128, 7, 7]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "Tensor<[128]> running_mean = ?",
            "Tensor<[128]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 544, 7, 7]> input = ?",
            "Optional[Tensor]<[544]> weight = ?",
            "Optional[Tensor]<[544]> bias = ?",
            "Tensor<[544]> running_mean = ?",
            "Tensor<[544]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 576, 7, 7]> input = ?",
            "Optional[Tensor]<[576]> weight = ?",
            "Optional[Tensor]<[576]> bias = ?",
            "Tensor<[576]> running_mean = ?",
            "Tensor<[576]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 608, 7, 7]> input = ?",
            "Optional[Tensor]<[608]> weight = ?",
            "Optional[Tensor]<[608]> bias = ?",
            "Tensor<[608]> running_mean = ?",
            "Tensor<[608]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 640, 7, 7]> input = ?",
            "Optional[Tensor]<[640]> weight = ?",
            "Optional[Tensor]<[640]> bias = ?",
            "Tensor<[640]> running_mean = ?",
            "Tensor<[640]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 672, 7, 7]> input = ?",
            "Optional[Tensor]<[672]> weight = ?",
            "Optional[Tensor]<[672]> bias = ?",
            "Tensor<[672]> running_mean = ?",
            "Tensor<[672]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 704, 7, 7]> input = ?",
            "Optional[Tensor]<[704]> weight = ?",
            "Optional[Tensor]<[704]> bias = ?",
            "Tensor<[704]> running_mean = ?",
            "Tensor<[704]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 736, 7, 7]> input = ?",
            "Optional[Tensor]<[736]> weight = ?",
            "Optional[Tensor]<[736]> bias = ?",
            "Tensor<[736]> running_mean = ?",
            "Tensor<[736]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 768, 7, 7]> input = ?",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "Tensor<[768]> running_mean = ?",
            "Tensor<[768]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 800, 7, 7]> input = ?",
            "Optional[Tensor]<[800]> weight = ?",
            "Optional[Tensor]<[800]> bias = ?",
            "Tensor<[800]> running_mean = ?",
            "Tensor<[800]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 832, 7, 7]> input = ?",
            "Optional[Tensor]<[832]> weight = ?",
            "Optional[Tensor]<[832]> bias = ?",
            "Tensor<[832]> running_mean = ?",
            "Tensor<[832]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 864, 7, 7]> input = ?",
            "Optional[Tensor]<[864]> weight = ?",
            "Optional[Tensor]<[864]> bias = ?",
            "Tensor<[864]> running_mean = ?",
            "Tensor<[864]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 896, 7, 7]> input = ?",
            "Optional[Tensor]<[896]> weight = ?",
            "Optional[Tensor]<[896]> bias = ?",
            "Tensor<[896]> running_mean = ?",
            "Tensor<[896]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 928, 7, 7]> input = ?",
            "Optional[Tensor]<[928]> weight = ?",
            "Optional[Tensor]<[928]> bias = ?",
            "Tensor<[928]> running_mean = ?",
            "Tensor<[928]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 960, 7, 7]> input = ?",
            "Optional[Tensor]<[960]> weight = ?",
            "Optional[Tensor]<[960]> bias = ?",
            "Tensor<[960]> running_mean = ?",
            "Tensor<[960]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 992, 7, 7]> input = ?",
            "Optional[Tensor]<[992]> weight = ?",
            "Optional[Tensor]<[992]> bias = ?",
            "Tensor<[992]> running_mean = ?",
            "Tensor<[992]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1024, 7, 7]> input = ?",
            "Optional[Tensor]<[1024]> weight = ?",
            "Optional[Tensor]<[1024]> bias = ?",
            "Tensor<[1024]> running_mean = ?",
            "Tensor<[1024]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._native_batch_norm_legit_no_training.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._native_batch_norm_legit_no_training.default", input_strings
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
