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
        return torch.ops.aten.transpose.int(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.transpose.int")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 16, 256, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 32, 16, 96]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 768, 49]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 50, 12, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[12, 50, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 50, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[2, 7, 8, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 7, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[2, 8, 7, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 7, 7]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 64, 7]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[12, 50, 50]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[12, 64, 50]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 49, 768]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[920, 8, 32]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[8, 920, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[8, 920, 32]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[100, 8, 32]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[8, 100, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[8, 100, 32]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[6, 100, 1, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 25, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 15, 6, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 6, 15, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 6, 15, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1, 6, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 6, 1, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 6, 1, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 6, 2, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 6, s0 + 1, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 6, 17, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 64, 19200]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1, 300, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 19200, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 256, 19200]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 128, 4800]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 2, 300, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 4800, 512]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 512, 4800]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 320, 1200]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 5, 300, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 1200, 1280]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1280, 1200]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 512, 300]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, 300, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 300, 2048]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 2048, 300]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 7, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 12, 45, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 12, 46, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 12, s10 + 1, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 59, 16, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 59, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 16, 59, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1, 16, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 60, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 16, 1, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, s10 + 1, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, 2048, 32]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 8, 256, 32]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[262, 768]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[1, 12, 10, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 32, 16384]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1, 256, 32]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 16384, 128]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 128, 16384]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 64, 4096]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 2, 256, 32]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 4096, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 256, 4096]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 160, 1024]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 5, 256, 32]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 1024, 640]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 640, 1024]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 256, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 256, 1024]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1024, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1024, 160]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 4096, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 16384, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[8, 256, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[8, 256, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[8, 32, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, 32, 256]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[5, 1024, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[5, 256, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[5, 1024, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[5, 32, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 5, 32, 256]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[2, 4096, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[2, 256, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[2, 4096, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[2, 32, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 2, 32, 256]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 16384, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 256, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 32, 256]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1, 32, 256]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 4096, 8, 40]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, 4096, 40]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 9, 8, 40]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, s0*s1, 8, 80]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, s0*s1, 80]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 9, 8, 80]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, s1*s2, 8, 160]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, s1*s2, 160]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 9, 8, 160]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, s0*s1, 8, 160]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, s0*s1, 160]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, s1*s2, 8, 80]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, s1*s2, 80]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, s1*s2, 8, 40]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, s1*s2, 40]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 144, 768]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 768, 192]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1500, 12, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 1500, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1, 12, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 1, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 4, 12, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 4, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 19, 16, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 19, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 16, 19, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 192, 1344]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 4150, 192]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 3, 1445, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 12, 9, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 12, 9, 64]> self = ?", "int dim0 = 2", "int dim1 = 1"],
        ["Tensor<[1, 12, 12, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 12, 12, 64]> self = ?", "int dim0 = 2", "int dim1 = 1"],
        ["Tensor<[1, 16, 9, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 16, 9, 64]> self = ?", "int dim0 = 2", "int dim1 = 1"],
        ["Tensor<[1, 16, 9, 128]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 16, 9, 128]> self = ?", "int dim0 = 2", "int dim1 = 1"],
        ["Tensor<[1, 64, 9, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 64, 9, 64]> self = ?", "int dim0 = 2", "int dim1 = 1"],
        ["Tensor<[1, 16, 5, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 16, 6, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 16, s10 + 1, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 16, 12, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 16, 64]> self = ?", "int dim0 = 2", "int dim1 = 3"],
        ["Tensor<[1, 12, 16, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 768, 196]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 197, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[12, 197, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[12, 197, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[12, 64, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 64, 197]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 196, 768]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1024, 196]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 16, 197, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[16, 197, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 197, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 64, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 16, 64, 197]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 196, 1024]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 24, 12, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[12, 24, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[12, 24, 64]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[24, 24, 64]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[24, 12, 24]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[1, 12, 24, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[64, 4, 49, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[64, 4, 49, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 8, 49, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[16, 8, 49, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[4, 16, 49, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[4, 16, 49, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 32, 49, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[1, 32, 49, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[64, 3, 49, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[64, 3, 49, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 6, 49, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[16, 6, 49, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[4, 12, 49, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[4, 12, 49, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 24, 49, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[1, 24, 49, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[64, 4, 64, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[64, 4, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 8, 64, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[16, 8, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[4, 16, 64, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[4, 16, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 32, 64, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[1, 32, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[64, 3, 64, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[64, 3, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[16, 6, 64, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[16, 6, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[4, 12, 64, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[4, 12, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 24, 64, 32]> self = ?", "int dim0 = -2", "int dim1 = -1"],
        ["Tensor<[1, 24, 64, 32]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 10, 12, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 10, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 12, 10, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 12, 1, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 12, 2, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 12, s0 + 1, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 10, 16, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 16, 10, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 16, 10, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 16, 1, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 16, 2, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 16, s0 + 1, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 10, 8, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, 10, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 8, 10, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 1, 8, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, 1, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 8, 1, 64]> self = ?", "int dim0 = 1", "int dim1 = 2"],
        ["Tensor<[1, 8, 2, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 8, s0 + 1, 64]> self = ?", "int dim0 = 3", "int dim1 = 2"],
        ["Tensor<[1, 12, 14, 64]> self = ?", "int dim0 = -1", "int dim1 = -2"],
        ["Tensor<[1, 12, 14, 64]> self = ?", "int dim0 = 2", "int dim1 = 1"],
        ["Tensor<[1, 197, 768]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 197, 1, 3, 768]> self = ?", "int dim0 = 0", "int dim1 = -2"],
        ["Tensor<[197, 12, 64]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[197, 1, 768]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 50, 768]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 50, 1, 3, 768]> self = ?", "int dim0 = 0", "int dim1 = -2"],
        ["Tensor<[50, 12, 64]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[50, 1, 768]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 1370, 1280]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 1370, 1, 3, 1280]> self = ?", "int dim0 = 0", "int dim1 = -2"],
        ["Tensor<[1370, 16, 80]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[1370, 1, 1280]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 197, 1024]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 197, 1, 3, 1024]> self = ?", "int dim0 = 0", "int dim1 = -2"],
        ["Tensor<[197, 16, 64]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[197, 1, 1024]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 50, 1024]> self = ?", "int dim0 = 1", "int dim1 = 0"],
        ["Tensor<[1, 50, 1, 3, 1024]> self = ?", "int dim0 = 0", "int dim1 = -2"],
        ["Tensor<[50, 16, 64]> self = ?", "int dim0 = 0", "int dim1 = 1"],
        ["Tensor<[50, 1, 1024]> self = ?", "int dim0 = 1", "int dim1 = 0"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.transpose.int",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.transpose.int", input_strings
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
