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
        return torch.ops.aten._to_copy.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten._to_copy.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 1, 1, 256]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[16, 1, 32]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[32, 32]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 32, 32]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 32, 32]> self = ?", "Optional[int] dtype = torch.bool"],
        [
            "Tensor<[1, 16, 32, 32]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 16, 32, 32]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[2, 1, 7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[2, 1, 7, 7]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[2, 7]> self = ?", "Optional[int] dtype = torch.int32", "Optional[Device] device = cpu"],
        ["Tensor<[1, 256, 23, 40]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 25]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 15]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 15, 512]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 15, 512]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[15, 15]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[15, 15]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 6, 15, 15]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 6, 15, 15]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 1, 1]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1, 1, 1]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 512]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1, 512]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 6, 1, 1]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 6, 1, 1]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 6, 1, 15]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 6, 1, 15]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 1, 1, 2]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[2, 2]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[2, 2]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 6, 1, 2]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 6, 1, 2]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 1, 1, s0 + 1]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[s0 + 1, s0 + 1]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[s0 + 1, s0 + 1]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 6, 1, s0 + 1]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 6, 1, s0 + 1]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 1, 1, 17]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[17, 17]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[17, 17]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 6, 1, 17]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 6, 1, 17]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 64, 15, 20]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 64, 30, 40]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 64, 30, 40]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 64, 60, 80]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 64, 60, 80]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 64, 120, 160]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 64, 120, 160]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 64, 240, 320]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 64, 240, 320]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 64, 480, 640]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 7]> self = ?", "Optional[int] dtype = torch.int32"],
        ["Tensor<[45, 45]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 45, 45]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 45, 45]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[1, 12, 45, 64]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 12, 45, 45]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 46]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 46]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[1, 12, 1, 64]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 12, 46, 64]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 12, 1, 46]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, s10 + 1]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, s10 + 1]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[1, 12, s10 + 1, 64]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 12, 1, s10 + 1]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[32]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[64]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[14]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[24]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[40]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[68]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[128]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[16]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[28]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[46]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[78]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[134]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[256]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[20]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[34]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[58]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[98]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[168]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[320]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[116]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[196]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[334]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[640]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[160]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[272]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[462]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1024]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 1, 32]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[59, 59]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 59, 59]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 59, 59]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[1, 1, 1, 60]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 60]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[512]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 1, 1, 2048]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[2048]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 1, 1, 10]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 10]> self = ?", "Optional[int] dtype = torch.int32"],
        [
            "Tensor<[1, 10]> self = ?",
            "Optional[int] dtype = torch.int32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 10]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 256, 128, 128]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 256, 128, 128]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 256, 64, 64]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 256, 32, 32]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 256, 16, 16]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 256, 16, 16]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 256, 32, 32]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 256, 64, 64]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 1, 1, 8]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 320]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1280, 8, 8]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1280, 16, 16]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1280, s0, s1]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[2*s0]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[2*s1]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 1280, 2*s0, 2*s1]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, s0, s1, s2]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[2*s2]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, s0, 2*s1, 2*s2]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 384, 512]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1, 12, 16]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[19, 19]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 19, 19]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 19, 19]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[1, 192, 50, 83]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[1, 192, 32, 42]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 256, 32, 32]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 128, 32, 32]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 128, 64, 64]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 9]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 12]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 5]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 16, 5, 64]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 16, 5, 5]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 5, 51200]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1, 1, 6]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 16, 6, 64]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 16, 1, 6]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 51200]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 16, s10 + 1, 64]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 16, 1, s10 + 1]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[192]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[768]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[224]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[8]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[48]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[12]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[36]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[72]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[60]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[120]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[240]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[80]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[100]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[92]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[56]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[112]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[336]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[672]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[480]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[960]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 72, 28, 28]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 72, 56, 56]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 120, 14, 14]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 120, 28, 28]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 240, 14, 14]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 240, 28, 28]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 200, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 200, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 184, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 184, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 480, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 672, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 960, 3, 3]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[200]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[184]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        [
            "Tensor<[1, 960, 7, 7]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 672, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 672, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 480, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 480, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 184, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 184, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 200, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 200, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 240, 28, 28]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 240, 14, 14]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 120, 28, 28]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 120, 14, 14]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 72, 56, 56]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 72, 28, 28]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 18, 28, 28]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 18, 56, 56]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 18, 14, 14]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 36, 14, 14]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 36, 28, 28]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 18, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 36, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 72, 7, 7]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 72, 14, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[18]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[144]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        [
            "Tensor<[1, 72, 14, 14]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 72, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 36, 28, 28]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 36, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 18, 56, 56]> self = ?",
            "Optional[int] dtype = torch.float32",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 18, 7, 7]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[96]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[384]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[448]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 1, 24, 24]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 24, 24]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[1, 1, 1, 24]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 1, 1, 24]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[1, 10, 768]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 10, 768]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[10, 10]> self = ?", "Optional[int] dtype = torch.int64"],
        ["Tensor<[10, 10]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 12, 10, 10]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 12, 10, 10]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 1, 768]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1, 768]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 12, 1, 1]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 12, 1, 1]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 12, 1, 10]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 12, 1, 10]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 12, 1, 2]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 12, 1, 2]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 12, 1, s0 + 1]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 12, 1, s0 + 1]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 10, 1024]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 10, 1024]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 16, 10, 10]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 16, 10, 10]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 1, 1024]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 1, 1024]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 16, 1, 1]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 16, 1, 1]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 16, 1, 10]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 16, 1, 10]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 16, 1, 2]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 16, 1, 2]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 16, 1, s0 + 1]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 16, 1, s0 + 1]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 10, 512]> self = ?", "Optional[int] dtype = torch.float32"],
        ["Tensor<[1, 10, 512]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[1, 8, 10, 10]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 8, 10, 10]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 8, 1, 1]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 8, 1, 1]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 8, 1, 10]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 8, 1, 10]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 8, 1, 2]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 8, 1, 2]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1, 8, 1, s0 + 1]> self = ?", "Optional[int] dtype = torch.float32"],
        [
            "Tensor<[1, 8, 1, s0 + 1]> self = ?",
            "Optional[int] dtype = torch.bfloat16",
            "Optional[int] layout = torch.strided",
            "Optional[Device] device = cpu",
        ],
        ["Tensor<[1152]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1280]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[288]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[88]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[528]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[720]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[208]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1248]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[352]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[576]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[136]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[816]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[232]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1392]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1632]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1, 1, 1, 14]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[728]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
        ["Tensor<[1536]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[int] layout = torch.strided"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._to_copy.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._to_copy.default", input_strings
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
