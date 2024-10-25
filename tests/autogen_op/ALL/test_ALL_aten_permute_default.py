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
        return torch.ops.aten.permute.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.permute.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 256, 16, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 16, 256, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 32, 16, 96]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 16, 32, 96]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 23, 40, 256]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 256, 920]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 25, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 12, 25, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[15, 15, 6]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 1, 6]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[2, 2, 6]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[s0 + 1, s0 + 1, 6]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[17, 17, 6]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[4672, 4544]> self = ?", "List[int] dims = [1, 0]"],
        ["Tensor<[1, 71, 7, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[4544, 4544]> self = ?", "List[int] dims = [1, 0]"],
        ["Tensor<[18176, 4544]> self = ?", "List[int] dims = [1, 0]"],
        ["Tensor<[4544, 18176]> self = ?", "List[int] dims = [1, 0]"],
        ["Tensor<[1, 19200, 1, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 19200, 64]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 64, 300]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 300, 1, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 1, 19200, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 120, 160, 64]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 4800, 2, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 4800, 128]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 128, 300]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 300, 2, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 2, 4800, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 60, 80, 128]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 1200, 5, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 1200, 320]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 320, 300]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 300, 5, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 5, 1200, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 30, 40, 320]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 300, 8, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 8, 300, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 15, 20, 512]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 7, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 12, 7, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 45, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 12, 45, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 1, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 12, 1, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 3, 16, 16, 16, 16]> self = ?", "List[int] dims = [0, 2, 4, 3, 5, 1]"],
        ["Tensor<[1, 256, 512]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 512, 256]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 16, 16, 16, 16, 3]> self = ?", "List[int] dims = [0, 5, 1, 3, 2, 4]"],
        ["Tensor<[1, 6, 4, 20, 20]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 4, 10, 10]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 4, 5, 5]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 4, 3, 3]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 4, 2, 2]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 4, 1, 1]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 91, 20, 20]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 91, 10, 10]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 91, 5, 5]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 91, 3, 3]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 91, 2, 2]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 91, 1, 1]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 256, 8, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 2048, 8, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 2048, 8, 160]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 8, 256, 160]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 256, 8, 160]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 256, 8, 96]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 8, 2048, 96]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 10, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 12, 10, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 16384, 1, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 16384, 32]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 32, 256]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 256, 1, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 1, 16384, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 128, 128, 32]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 4096, 2, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 4096, 64]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 64, 256]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 256, 2, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 2, 4096, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 64, 64, 64]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 1024, 5, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 1024, 160]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 160, 256]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 256, 5, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 5, 1024, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 32, 32, 160]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 8, 256, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 16, 16, 256]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 16384, 256]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 4096, 256]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 1024, 256]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 256, 256]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 256, 1024]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 256, 4096]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 256, 16384]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 256, 16, 16]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 160, 32, 32]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 5, 256, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 256, 160]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 160, 1024]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 64, 64, 64]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 2, 256, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 256, 64]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 64, 4096]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 32, 128, 128]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 1, 256, 32]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 256, 32]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 32, 16384]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 320, 64, 64]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 64, 64, 320]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 640, 32, 32]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 32, 32, 640]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 1280, 16, 16]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 16, 16, 1280]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 1280, 8, 8]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[1, 8, 8, 1280]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 201, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 12, 201, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 768, 1500]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 1445, 3, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 3, 1445, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 9, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 12, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 9, 16, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 9, 16, 128]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 9, 64, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 5, 16, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 16, 5, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 1, 16, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 16, 1, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 197, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 12, 197, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[197, 197, 12]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[12, 197, 197]> self = ?", "List[int] dims = [1, 2, 0]"],
        ["Tensor<[1, 197, 16, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[197, 197, 16]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 16, 197, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[16, 197, 197]> self = ?", "List[int] dims = [1, 2, 0]"],
        ["Tensor<[1, 9, 91, 100, 136]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 91, 50, 68]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 91, 25, 34]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 91, 13, 17]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 91, 7, 9]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 4, 100, 136]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 4, 50, 68]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 4, 25, 34]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 4, 13, 17]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 9, 4, 7, 9]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 4, 4, 38, 38]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 4, 19, 19]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 4, 4, 3, 3]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 4, 4, 1, 1]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 4, 91, 38, 38]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 6, 91, 19, 19]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 4, 91, 3, 3]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 4, 91, 1, 1]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
        ["Tensor<[1, 128, 56, 56]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[49, 49, 4]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 8, 7, 8, 7, 128]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[64, 49, 3, 4, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 8, 8, 7, 7, 128]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[8, 7, 8, 7]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[49, 49, 8]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 4, 7, 4, 7, 256]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[16, 49, 3, 8, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 4, 4, 7, 7, 256]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[4, 7, 4, 7]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[49, 49, 16]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 2, 7, 2, 7, 512]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[4, 49, 3, 16, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 2, 2, 7, 7, 512]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[2, 7, 2, 7]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[49, 49, 32]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 1, 7, 1, 7, 1024]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[1, 49, 3, 32, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 1, 1, 7, 7, 1024]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[1, 7, 7, 1024]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 96, 56, 56]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[49, 49, 3]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 8, 7, 8, 7, 96]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[64, 49, 3, 3, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 8, 8, 7, 7, 96]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[49, 49, 6]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 4, 7, 4, 7, 192]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[16, 49, 3, 6, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 4, 4, 7, 7, 192]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[49, 49, 12]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 2, 7, 2, 7, 384]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[4, 49, 3, 12, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 2, 2, 7, 7, 384]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[49, 49, 24]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 1, 7, 1, 7, 768]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[1, 49, 3, 24, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 1, 1, 7, 7, 768]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[1, 7, 7, 768]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 128, 64, 64]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[64, 64, 4]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[64, 64, 3, 4, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[8, 8, 8, 8]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[64, 64, 8]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 4, 8, 4, 8, 256]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[16, 64, 3, 8, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 4, 4, 8, 8, 256]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[4, 8, 4, 8]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[64, 64, 16]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 2, 8, 2, 8, 512]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[4, 64, 3, 16, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 2, 2, 8, 8, 512]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[2, 8, 2, 8]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[64, 64, 32]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 1, 8, 1, 8, 1024]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[1, 64, 3, 32, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 1, 1, 8, 8, 1024]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[1, 8, 8, 1024]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[1, 96, 64, 64]> self = ?", "List[int] dims = [0, 2, 3, 1]"],
        ["Tensor<[64, 64, 3]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[64, 64, 3, 3, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[64, 64, 6]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 4, 8, 4, 8, 192]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[16, 64, 3, 6, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 4, 4, 8, 8, 192]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[64, 64, 12]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 2, 8, 2, 8, 384]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[4, 64, 3, 12, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 2, 2, 8, 8, 384]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[64, 64, 24]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 1, 8, 1, 8, 768]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[1, 64, 3, 24, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
        ["Tensor<[1, 1, 1, 8, 8, 768]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
        ["Tensor<[1, 8, 8, 768]> self = ?", "List[int] dims = [0, 3, 1, 2]"],
        ["Tensor<[10, 10, 12]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 1, 12]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[2, 2, 12]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[s0 + 1, s0 + 1, 12]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[10, 10, 16]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 1, 16]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[2, 2, 16]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[s0 + 1, s0 + 1, 16]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[10, 10, 8]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 1, 8]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[2, 2, 8]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[s0 + 1, s0 + 1, 8]> self = ?", "List[int] dims = [2, 0, 1]"],
        ["Tensor<[1, 14, 12, 64]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
        ["Tensor<[1, 768, 196]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 12, 197, 64]> self = ?", "List[int] dims = [2, 0, 1, 3]"],
        ["Tensor<[1, 768, 49]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 12, 50, 64]> self = ?", "List[int] dims = [2, 0, 1, 3]"],
        ["Tensor<[1, 1280, 1369]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 16, 1370, 80]> self = ?", "List[int] dims = [2, 0, 1, 3]"],
        ["Tensor<[1, 1024, 196]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 16, 197, 64]> self = ?", "List[int] dims = [2, 0, 1, 3]"],
        ["Tensor<[1, 1024, 49]> self = ?", "List[int] dims = [0, 2, 1]"],
        ["Tensor<[1, 16, 50, 64]> self = ?", "List[int] dims = [2, 0, 1, 3]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.permute.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.permute.default", input_strings
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
