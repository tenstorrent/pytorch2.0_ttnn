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
        return torch.ops.aten.expand.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.expand.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 16, 256, 64]> self = ?", "List[int] size = [1, 16, 256, 64]"],
        ["Tensor<[1, 16, 64, 256]> self = ?", "List[int] size = [1, 16, 64, 256]"],
        ["Tensor<[1, 16, 256, 256]> self = ?", "List[int] size = [1, 16, 256, 256]"],
        ["Tensor<[1, 1, 32, 32]> self = ?", "List[int] size = [1, 1, 32, 32]"],
        ["Tensor<[1, 1, 1, 32]> self = ?", "List[int] size = [1, 1, 32, 32]"],
        ["Tensor<[768]> self = ?", "List[int] size = [1, 1, -1]"],
        ["Tensor<[1, 1, 7, 7]> self = ?", "List[int] size = [2, 1, 7, 7]"],
        ["Tensor<[2, 1, 1, 7]> self = ?", "List[int] size = [2, 1, 7, 7]"],
        ["Tensor<[1, 1, 1, 920]> self = ?", "List[int] size = [-1, 8, -1, -1]"],
        ["Tensor<[1, 25]> self = ?", "List[int] size = [1, 25]"],
        ["Tensor<[1, 12, 25, 64]> self = ?", "List[int] size = [1, 12, 25, 64]"],
        ["Tensor<[1, 12, 64, 25]> self = ?", "List[int] size = [1, 12, 64, 25]"],
        ["Tensor<[1, 12, 25, 25]> self = ?", "List[int] size = [1, 12, 25, 25]"],
        ["Tensor<[1, 6, 15, 64]> self = ?", "List[int] size = [1, 6, 15, 64]"],
        ["Tensor<[1, 6, 64, 15]> self = ?", "List[int] size = [1, 6, 64, 15]"],
        ["Tensor<[1, 6, 15, 15]> self = ?", "List[int] size = [1, 6, 15, 15]"],
        ["Tensor<[1, 6, 1, 64]> self = ?", "List[int] size = [1, 6, 1, 64]"],
        ["Tensor<[1, 6, 64, 1]> self = ?", "List[int] size = [1, 6, 64, 1]"],
        ["Tensor<[1, 6, 1, 1]> self = ?", "List[int] size = [1, 6, 1, 1]"],
        ["Tensor<[1, 6, 1, 15]> self = ?", "List[int] size = [1, 6, 1, 15]"],
        ["Tensor<[1, 6, 64, 2]> self = ?", "List[int] size = [1, 6, 64, 2]"],
        ["Tensor<[1, 6, 1, 2]> self = ?", "List[int] size = [1, 6, 1, 2]"],
        ["Tensor<[1, 6, 2, 64]> self = ?", "List[int] size = [1, 6, 2, 64]"],
        ["Tensor<[1, 6, 64, s0 + 1]> self = ?", "List[int] size = [1, 6, 64, <s0 + 1>]"],
        ["Tensor<[1, 6, 1, s0 + 1]> self = ?", "List[int] size = [1, 6, 1, <s0 + 1>]"],
        ["Tensor<[1, 6, s0 + 1, 64]> self = ?", "List[int] size = [1, 6, <s0 + 1>, 64]"],
        ["Tensor<[1, 6, 64, 17]> self = ?", "List[int] size = [1, 6, 64, 17]"],
        ["Tensor<[1, 6, 1, 17]> self = ?", "List[int] size = [1, 6, 1, 17]"],
        ["Tensor<[1, 6, 17, 64]> self = ?", "List[int] size = [1, 6, 17, 64]"],
        ["Tensor<[1, 1, 19200, 64]> self = ?", "List[int] size = [1, 1, 19200, 64]"],
        ["Tensor<[1, 1, 64, 300]> self = ?", "List[int] size = [1, 1, 64, 300]"],
        ["Tensor<[1, 1, 19200, 300]> self = ?", "List[int] size = [1, 1, 19200, 300]"],
        ["Tensor<[1, 1, 300, 64]> self = ?", "List[int] size = [1, 1, 300, 64]"],
        ["Tensor<[1, 2, 4800, 64]> self = ?", "List[int] size = [1, 2, 4800, 64]"],
        ["Tensor<[1, 2, 64, 300]> self = ?", "List[int] size = [1, 2, 64, 300]"],
        ["Tensor<[1, 2, 4800, 300]> self = ?", "List[int] size = [1, 2, 4800, 300]"],
        ["Tensor<[1, 2, 300, 64]> self = ?", "List[int] size = [1, 2, 300, 64]"],
        ["Tensor<[1, 5, 1200, 64]> self = ?", "List[int] size = [1, 5, 1200, 64]"],
        ["Tensor<[1, 5, 64, 300]> self = ?", "List[int] size = [1, 5, 64, 300]"],
        ["Tensor<[1, 5, 1200, 300]> self = ?", "List[int] size = [1, 5, 1200, 300]"],
        ["Tensor<[1, 5, 300, 64]> self = ?", "List[int] size = [1, 5, 300, 64]"],
        ["Tensor<[1, 8, 300, 64]> self = ?", "List[int] size = [1, 8, 300, 64]"],
        ["Tensor<[1, 8, 64, 300]> self = ?", "List[int] size = [1, 8, 64, 300]"],
        ["Tensor<[1, 8, 300, 300]> self = ?", "List[int] size = [1, 8, 300, 300]"],
        ["Tensor<[1, 12, 7, 64]> self = ?", "List[int] size = [1, 12, 7, 64]"],
        ["Tensor<[1, 12, 64, 7]> self = ?", "List[int] size = [1, 12, 64, 7]"],
        ["Tensor<[1, 12, 7, 7]> self = ?", "List[int] size = [1, 12, 7, 7]"],
        ["Tensor<[1, 1, 45]> self = ?", "List[int] size = [1, 1, 45]"],
        ["Tensor<[1, 1, 45, 45]> self = ?", "List[int] size = [1, 1, 45, 45]"],
        ["Tensor<[1, 1, 1, 45]> self = ?", "List[int] size = [1, 1, 45, 45]"],
        ["Tensor<[1, 12, 45, 64]> self = ?", "List[int] size = [1, 12, 45, 64]"],
        ["Tensor<[1, 12, 64, 45]> self = ?", "List[int] size = [1, 12, 64, 45]"],
        ["Tensor<[1, 12, 45, 45]> self = ?", "List[int] size = [1, 12, 45, 45]"],
        ["Tensor<[1, 1, 1, 46]> self = ?", "List[int] size = [1, 1, 1, 46]"],
        ["Tensor<[1, 12, 1, 64]> self = ?", "List[int] size = [1, 12, 1, 64]"],
        ["Tensor<[1, 12, 64, 46]> self = ?", "List[int] size = [1, 12, 64, 46]"],
        ["Tensor<[1, 12, 1, 46]> self = ?", "List[int] size = [1, 12, 1, 46]"],
        ["Tensor<[1, 12, 46, 64]> self = ?", "List[int] size = [1, 12, 46, 64]"],
        ["Tensor<[1, 1, 1, s10 + 1]> self = ?", "List[int] size = [1, 1, 1, <s10 + 1>]"],
        ["Tensor<[1, 12, 64, s10 + 1]> self = ?", "List[int] size = [1, 12, 64, <s10 + 1>]"],
        ["Tensor<[1, 12, 1, s10 + 1]> self = ?", "List[int] size = [1, 12, 1, <s10 + 1>]"],
        ["Tensor<[1, 12, s10 + 1, 64]> self = ?", "List[int] size = [1, 12, <s10 + 1>, 64]"],
        ["Tensor<[1, 1024, 1, 1]> self = ?", "List[int] size = [1, 1024, 7, 7]"],
        ["Tensor<[1, 64, 1]> self = ?", "List[int] size = [1, -1, 1]"],
        ["Tensor<[1, 64, 1]> self = ?", "List[int] size = [1, 64, 1]"],
        ["Tensor<[1, 1, 32]> self = ?", "List[int] size = [1, 1, 32]"],
        ["Tensor<[1, 512, 1]> self = ?", "List[int] size = [1, 512, 256]"],
        ["Tensor<[20, 1]> self = ?", "List[int] size = [20, 20]"],
        ["Tensor<[1, 20]> self = ?", "List[int] size = [20, 20]"],
        ["Tensor<[10, 1]> self = ?", "List[int] size = [10, 10]"],
        ["Tensor<[1, 10]> self = ?", "List[int] size = [10, 10]"],
        ["Tensor<[5, 1]> self = ?", "List[int] size = [5, 5]"],
        ["Tensor<[1, 5]> self = ?", "List[int] size = [5, 5]"],
        ["Tensor<[3, 1]> self = ?", "List[int] size = [3, 3]"],
        ["Tensor<[1, 3]> self = ?", "List[int] size = [3, 3]"],
        ["Tensor<[2, 1]> self = ?", "List[int] size = [2, 2]"],
        ["Tensor<[1, 2]> self = ?", "List[int] size = [2, 2]"],
        ["Tensor<[1, 1]> self = ?", "List[int] size = [1, 1]"],
        ["Tensor<[1, 1, 59, 59]> self = ?", "List[int] size = [1, 1, 59, 59]"],
        ["Tensor<[1, 1, 1, 59]> self = ?", "List[int] size = [1, 1, 59, 59]"],
        ["Tensor<[1, 1, 1, 60]> self = ?", "List[int] size = [1, 1, 1, 60]"],
        ["Tensor<[256, 1280]> self = ?", "List[int] size = [1, -1, -1]"],
        ["Tensor<[1, 8, 256, 32]> self = ?", "List[int] size = [1, 8, 256, 32]"],
        ["Tensor<[1, 8, 32, 2048]> self = ?", "List[int] size = [1, 8, 32, 2048]"],
        ["Tensor<[1, 8, 256, 2048]> self = ?", "List[int] size = [1, 8, 256, 2048]"],
        ["Tensor<[1, 8, 2048, 160]> self = ?", "List[int] size = [1, 8, 2048, 160]"],
        ["Tensor<[1, 8, 32, 256]> self = ?", "List[int] size = [1, 8, 32, 256]"],
        ["Tensor<[1, 8, 256, 256]> self = ?", "List[int] size = [1, 8, 256, 256]"],
        ["Tensor<[1, 8, 256, 160]> self = ?", "List[int] size = [1, 8, 256, 160]"],
        ["Tensor<[2048, 768]> self = ?", "List[int] size = [1, -1, -1]"],
        ["Tensor<[1, 8, 2048, 32]> self = ?", "List[int] size = [1, 8, 2048, 32]"],
        ["Tensor<[1, 8, 2048, 256]> self = ?", "List[int] size = [1, 8, 2048, 256]"],
        ["Tensor<[1, 8, 256, 96]> self = ?", "List[int] size = [1, 8, 256, 96]"],
        ["Tensor<[1, 512, 1, 1]> self = ?", "List[int] size = [1, 512, 7, 7]"],
        ["Tensor<[1, 2048, 1, 1]> self = ?", "List[int] size = [1, 2048, 7, 7]"],
        ["Tensor<[1, 10]> self = ?", "List[int] size = [1, 10]"],
        ["Tensor<[1, 12, 10, 64]> self = ?", "List[int] size = [1, 12, 10, 64]"],
        ["Tensor<[1, 12, 64, 10]> self = ?", "List[int] size = [1, 12, 64, 10]"],
        ["Tensor<[1, 12, 10, 10]> self = ?", "List[int] size = [1, 12, 10, 10]"],
        ["Tensor<[1, 1, 16384, 32]> self = ?", "List[int] size = [1, 1, 16384, 32]"],
        ["Tensor<[1, 1, 32, 256]> self = ?", "List[int] size = [1, 1, 32, 256]"],
        ["Tensor<[1, 1, 16384, 256]> self = ?", "List[int] size = [1, 1, 16384, 256]"],
        ["Tensor<[1, 1, 256, 32]> self = ?", "List[int] size = [1, 1, 256, 32]"],
        ["Tensor<[1, 2, 4096, 32]> self = ?", "List[int] size = [1, 2, 4096, 32]"],
        ["Tensor<[1, 2, 32, 256]> self = ?", "List[int] size = [1, 2, 32, 256]"],
        ["Tensor<[1, 2, 4096, 256]> self = ?", "List[int] size = [1, 2, 4096, 256]"],
        ["Tensor<[1, 2, 256, 32]> self = ?", "List[int] size = [1, 2, 256, 32]"],
        ["Tensor<[1, 5, 1024, 32]> self = ?", "List[int] size = [1, 5, 1024, 32]"],
        ["Tensor<[1, 5, 32, 256]> self = ?", "List[int] size = [1, 5, 32, 256]"],
        ["Tensor<[1, 5, 1024, 256]> self = ?", "List[int] size = [1, 5, 1024, 256]"],
        ["Tensor<[1, 5, 256, 32]> self = ?", "List[int] size = [1, 5, 256, 32]"],
        ["Tensor<[1]> self = ?", "List[int] size = [1]"],
        ["Tensor<[12, 1]> self = ?", "List[int] size = [12, 16]"],
        ["Tensor<[1, 16]> self = ?", "List[int] size = [12, 16]"],
        ["Tensor<[1, 1, 19, 19]> self = ?", "List[int] size = [1, 1, 19, 19]"],
        ["Tensor<[1, 1, 1, 19]> self = ?", "List[int] size = [1, 1, 19, 19]"],
        ["Tensor<[1, 1, 192]> self = ?", "List[int] size = [1, -1, -1]"],
        ["Tensor<[1, 100, 192]> self = ?", "List[int] size = [1, -1, -1]"],
        ["Tensor<[1, 3, 1445, 64]> self = ?", "List[int] size = [1, 3, 1445, 64]"],
        ["Tensor<[1, 3, 64, 1445]> self = ?", "List[int] size = [1, 3, 64, 1445]"],
        ["Tensor<[1, 3, 1445, 1445]> self = ?", "List[int] size = [1, 3, 1445, 1445]"],
        ["Tensor<[1, 12, 9, 64]> self = ?", "List[int] size = [1, 12, 9, 64]"],
        ["Tensor<[1, 12, 64, 9]> self = ?", "List[int] size = [1, 12, 64, 9]"],
        ["Tensor<[1, 12, 9, 9]> self = ?", "List[int] size = [1, 12, 9, 9]"],
        ["Tensor<[1, 12, 12, 64]> self = ?", "List[int] size = [1, 12, 12, 64]"],
        ["Tensor<[1, 12, 64, 12]> self = ?", "List[int] size = [1, 12, 64, 12]"],
        ["Tensor<[1, 12, 12, 12]> self = ?", "List[int] size = [1, 12, 12, 12]"],
        ["Tensor<[1, 16, 9, 64]> self = ?", "List[int] size = [1, 16, 9, 64]"],
        ["Tensor<[1, 16, 64, 9]> self = ?", "List[int] size = [1, 16, 64, 9]"],
        ["Tensor<[1, 16, 9, 9]> self = ?", "List[int] size = [1, 16, 9, 9]"],
        ["Tensor<[1, 16, 9, 128]> self = ?", "List[int] size = [1, 16, 9, 128]"],
        ["Tensor<[1, 16, 128, 9]> self = ?", "List[int] size = [1, 16, 128, 9]"],
        ["Tensor<[1, 64, 9, 64]> self = ?", "List[int] size = [1, 64, 9, 64]"],
        ["Tensor<[1, 64, 64, 9]> self = ?", "List[int] size = [1, 64, 64, 9]"],
        ["Tensor<[1, 64, 9, 9]> self = ?", "List[int] size = [1, 64, 9, 9]"],
        ["Tensor<[1, 5, 1, 16, 1]> self = ?", "List[int] size = [1, 5, 1, 16, 2]"],
        ["Tensor<[1, 16, 5, 64]> self = ?", "List[int] size = [1, 16, 5, 64]"],
        ["Tensor<[1, 16, 64, 5]> self = ?", "List[int] size = [1, 16, 64, 5]"],
        ["Tensor<[1, 16, 5, 5]> self = ?", "List[int] size = [1, 16, 5, 5]"],
        ["Tensor<[1, 1, 1, 16, 1]> self = ?", "List[int] size = [1, 1, 1, 16, 2]"],
        ["Tensor<[1, 16, 1, 64]> self = ?", "List[int] size = [1, 16, 1, 64]"],
        ["Tensor<[1, 16, 64, 6]> self = ?", "List[int] size = [1, 16, 64, 6]"],
        ["Tensor<[1, 16, 1, 6]> self = ?", "List[int] size = [1, 16, 1, 6]"],
        ["Tensor<[1, 16, 6, 64]> self = ?", "List[int] size = [1, 16, 6, 64]"],
        ["Tensor<[1, 16, 64, s10 + 1]> self = ?", "List[int] size = [1, 16, 64, <s10 + 1>]"],
        ["Tensor<[1, 16, 1, s10 + 1]> self = ?", "List[int] size = [1, 16, 1, <s10 + 1>]"],
        ["Tensor<[1, 16, s10 + 1, 64]> self = ?", "List[int] size = [1, 16, <s10 + 1>, 64]"],
        ["Tensor<[1, 12, 16, 64]> self = ?", "List[int] size = [1, 12, 16, 64]"],
        ["Tensor<[1, 12, 64, 16]> self = ?", "List[int] size = [1, 12, 64, 16]"],
        ["Tensor<[1, 1, 1, 16]> self = ?", "List[int] size = [1, 12, 16, 16]"],
        ["Tensor<[1, 12, 16, 16]> self = ?", "List[int] size = [1, 12, 16, 16]"],
        ["Tensor<[1, 768, 1, 1]> self = ?", "List[int] size = [1, 768, 14, 14]"],
        ["Tensor<[1, 512, 1, 1]> self = ?", "List[int] size = [1, 512, 28, 28]"],
        ["Tensor<[1, 256, 1, 1]> self = ?", "List[int] size = [1, 256, 56, 56]"],
        ["Tensor<[1, 1, 768]> self = ?", "List[int] size = [1, -1, -1]"],
        ["Tensor<[1, 12, 197, 64]> self = ?", "List[int] size = [1, 12, 197, 64]"],
        ["Tensor<[1, 12, 64, 197]> self = ?", "List[int] size = [1, 12, 64, 197]"],
        ["Tensor<[1, 12, 197, 197]> self = ?", "List[int] size = [1, 12, 197, 197]"],
        ["Tensor<[1, 960, 1, 1]> self = ?", "List[int] size = [1, 960, 7, 7]"],
        ["Tensor<[1, 672, 1, 1]> self = ?", "List[int] size = [1, 672, 7, 7]"],
        ["Tensor<[1, 672, 1, 1]> self = ?", "List[int] size = [1, 672, 14, 14]"],
        ["Tensor<[1, 480, 1, 1]> self = ?", "List[int] size = [1, 480, 14, 14]"],
        ["Tensor<[1, 120, 1, 1]> self = ?", "List[int] size = [1, 120, 28, 28]"],
        ["Tensor<[1, 72, 1, 1]> self = ?", "List[int] size = [1, 72, 28, 28]"],
        ["Tensor<[1, 1536, 1, 1]> self = ?", "List[int] size = [1, 1536, 8, 8]"],
        ["Tensor<[1, 1, 768]> self = ?", "List[int] size = [1, 196, 768]"],
        ["Tensor<[1, 1, 1024]> self = ?", "List[int] size = [1, -1, -1]"],
        ["Tensor<[1, 16, 197, 64]> self = ?", "List[int] size = [1, 16, 197, 64]"],
        ["Tensor<[1, 16, 64, 197]> self = ?", "List[int] size = [1, 16, 64, 197]"],
        ["Tensor<[1, 16, 197, 197]> self = ?", "List[int] size = [1, 16, 197, 197]"],
        ["Tensor<[1, 1, 1024]> self = ?", "List[int] size = [1, 196, 1024]"],
        ["Tensor<[100, 1]> self = ?", "List[int] size = [100, 136]"],
        ["Tensor<[1, 136]> self = ?", "List[int] size = [100, 136]"],
        ["Tensor<[50, 1]> self = ?", "List[int] size = [50, 68]"],
        ["Tensor<[1, 68]> self = ?", "List[int] size = [50, 68]"],
        ["Tensor<[25, 1]> self = ?", "List[int] size = [25, 34]"],
        ["Tensor<[1, 34]> self = ?", "List[int] size = [25, 34]"],
        ["Tensor<[13, 1]> self = ?", "List[int] size = [13, 17]"],
        ["Tensor<[1, 17]> self = ?", "List[int] size = [13, 17]"],
        ["Tensor<[7, 1]> self = ?", "List[int] size = [7, 9]"],
        ["Tensor<[1, 9]> self = ?", "List[int] size = [7, 9]"],
        ["Tensor<[1, 1, 1, 24]> self = ?", "List[int] size = [1, 1, 24, 24]"],
        ["Tensor<[24, 12, 64]> self = ?", "List[int] size = [24, 12, 64]"],
        ["Tensor<[24, 64, 24]> self = ?", "List[int] size = [24, 64, 24]"],
        ["Tensor<[1, 1, 1, 24]> self = ?", "List[int] size = [1, 1, 1, 24]"],
        ["Tensor<[1, 1, 38, 38]> self = ?", "List[int] size = [1, 512, 38, 38]"],
        ["Tensor<[38, 1]> self = ?", "List[int] size = [38, 38]"],
        ["Tensor<[1, 38]> self = ?", "List[int] size = [38, 38]"],
        ["Tensor<[19, 1]> self = ?", "List[int] size = [19, 19]"],
        ["Tensor<[1, 19]> self = ?", "List[int] size = [19, 19]"],
        ["Tensor<[64, 4, 49, 32]> self = ?", "List[int] size = [64, 4, 49, 32]"],
        ["Tensor<[64, 4, 32, 49]> self = ?", "List[int] size = [64, 4, 32, 49]"],
        ["Tensor<[64, 4, 49, 49]> self = ?", "List[int] size = [64, 4, 49, 49]"],
        ["Tensor<[16, 8, 49, 32]> self = ?", "List[int] size = [16, 8, 49, 32]"],
        ["Tensor<[16, 8, 32, 49]> self = ?", "List[int] size = [16, 8, 32, 49]"],
        ["Tensor<[16, 8, 49, 49]> self = ?", "List[int] size = [16, 8, 49, 49]"],
        ["Tensor<[4, 16, 49, 32]> self = ?", "List[int] size = [4, 16, 49, 32]"],
        ["Tensor<[4, 16, 32, 49]> self = ?", "List[int] size = [4, 16, 32, 49]"],
        ["Tensor<[4, 16, 49, 49]> self = ?", "List[int] size = [4, 16, 49, 49]"],
        ["Tensor<[1, 32, 49, 32]> self = ?", "List[int] size = [1, 32, 49, 32]"],
        ["Tensor<[1, 32, 32, 49]> self = ?", "List[int] size = [1, 32, 32, 49]"],
        ["Tensor<[1, 32, 49, 49]> self = ?", "List[int] size = [1, 32, 49, 49]"],
        ["Tensor<[64, 3, 49, 32]> self = ?", "List[int] size = [64, 3, 49, 32]"],
        ["Tensor<[64, 3, 32, 49]> self = ?", "List[int] size = [64, 3, 32, 49]"],
        ["Tensor<[64, 3, 49, 49]> self = ?", "List[int] size = [64, 3, 49, 49]"],
        ["Tensor<[16, 6, 49, 32]> self = ?", "List[int] size = [16, 6, 49, 32]"],
        ["Tensor<[16, 6, 32, 49]> self = ?", "List[int] size = [16, 6, 32, 49]"],
        ["Tensor<[16, 6, 49, 49]> self = ?", "List[int] size = [16, 6, 49, 49]"],
        ["Tensor<[4, 12, 49, 32]> self = ?", "List[int] size = [4, 12, 49, 32]"],
        ["Tensor<[4, 12, 32, 49]> self = ?", "List[int] size = [4, 12, 32, 49]"],
        ["Tensor<[4, 12, 49, 49]> self = ?", "List[int] size = [4, 12, 49, 49]"],
        ["Tensor<[1, 24, 49, 32]> self = ?", "List[int] size = [1, 24, 49, 32]"],
        ["Tensor<[1, 24, 32, 49]> self = ?", "List[int] size = [1, 24, 32, 49]"],
        ["Tensor<[1, 24, 49, 49]> self = ?", "List[int] size = [1, 24, 49, 49]"],
        ["Tensor<[64, 4, 64, 1]> self = ?", "List[int] size = [64, 4, 64, 32]"],
        ["Tensor<[64, 4, 64, 32]> self = ?", "List[int] size = [64, 4, 64, 32]"],
        ["Tensor<[64, 4, 32, 64]> self = ?", "List[int] size = [64, 4, 32, 64]"],
        ["Tensor<[64, 4, 64, 64]> self = ?", "List[int] size = [64, 4, 64, 64]"],
        ["Tensor<[16, 8, 64, 1]> self = ?", "List[int] size = [16, 8, 64, 32]"],
        ["Tensor<[16, 8, 64, 32]> self = ?", "List[int] size = [16, 8, 64, 32]"],
        ["Tensor<[16, 8, 32, 64]> self = ?", "List[int] size = [16, 8, 32, 64]"],
        ["Tensor<[16, 8, 64, 64]> self = ?", "List[int] size = [16, 8, 64, 64]"],
        ["Tensor<[4, 16, 64, 1]> self = ?", "List[int] size = [4, 16, 64, 32]"],
        ["Tensor<[4, 16, 64, 32]> self = ?", "List[int] size = [4, 16, 64, 32]"],
        ["Tensor<[4, 16, 32, 64]> self = ?", "List[int] size = [4, 16, 32, 64]"],
        ["Tensor<[4, 16, 64, 64]> self = ?", "List[int] size = [4, 16, 64, 64]"],
        ["Tensor<[1, 32, 64, 1]> self = ?", "List[int] size = [1, 32, 64, 32]"],
        ["Tensor<[1, 32, 64, 32]> self = ?", "List[int] size = [1, 32, 64, 32]"],
        ["Tensor<[1, 32, 32, 64]> self = ?", "List[int] size = [1, 32, 32, 64]"],
        ["Tensor<[1, 32, 64, 64]> self = ?", "List[int] size = [1, 32, 64, 64]"],
        ["Tensor<[64, 3, 64, 1]> self = ?", "List[int] size = [64, 3, 64, 32]"],
        ["Tensor<[64, 3, 64, 32]> self = ?", "List[int] size = [64, 3, 64, 32]"],
        ["Tensor<[64, 3, 32, 64]> self = ?", "List[int] size = [64, 3, 32, 64]"],
        ["Tensor<[64, 3, 64, 64]> self = ?", "List[int] size = [64, 3, 64, 64]"],
        ["Tensor<[16, 6, 64, 1]> self = ?", "List[int] size = [16, 6, 64, 32]"],
        ["Tensor<[16, 6, 64, 32]> self = ?", "List[int] size = [16, 6, 64, 32]"],
        ["Tensor<[16, 6, 32, 64]> self = ?", "List[int] size = [16, 6, 32, 64]"],
        ["Tensor<[16, 6, 64, 64]> self = ?", "List[int] size = [16, 6, 64, 64]"],
        ["Tensor<[4, 12, 64, 1]> self = ?", "List[int] size = [4, 12, 64, 32]"],
        ["Tensor<[4, 12, 64, 32]> self = ?", "List[int] size = [4, 12, 64, 32]"],
        ["Tensor<[4, 12, 32, 64]> self = ?", "List[int] size = [4, 12, 32, 64]"],
        ["Tensor<[4, 12, 64, 64]> self = ?", "List[int] size = [4, 12, 64, 64]"],
        ["Tensor<[1, 24, 64, 1]> self = ?", "List[int] size = [1, 24, 64, 32]"],
        ["Tensor<[1, 24, 64, 32]> self = ?", "List[int] size = [1, 24, 64, 32]"],
        ["Tensor<[1, 24, 32, 64]> self = ?", "List[int] size = [1, 24, 32, 64]"],
        ["Tensor<[1, 24, 64, 64]> self = ?", "List[int] size = [1, 24, 64, 64]"],
        ["Tensor<[1, 12, 64, 1]> self = ?", "List[int] size = [1, 12, 64, 1]"],
        ["Tensor<[1, 12, 1, 1]> self = ?", "List[int] size = [1, 12, 1, 1]"],
        ["Tensor<[1, 12, 1, 10]> self = ?", "List[int] size = [1, 12, 1, 10]"],
        ["Tensor<[1, 12, 64, 2]> self = ?", "List[int] size = [1, 12, 64, 2]"],
        ["Tensor<[1, 12, 1, 2]> self = ?", "List[int] size = [1, 12, 1, 2]"],
        ["Tensor<[1, 12, 2, 64]> self = ?", "List[int] size = [1, 12, 2, 64]"],
        ["Tensor<[1, 12, 64, s0 + 1]> self = ?", "List[int] size = [1, 12, 64, <s0 + 1>]"],
        ["Tensor<[1, 12, 1, s0 + 1]> self = ?", "List[int] size = [1, 12, 1, <s0 + 1>]"],
        ["Tensor<[1, 12, s0 + 1, 64]> self = ?", "List[int] size = [1, 12, <s0 + 1>, 64]"],
        ["Tensor<[1, 16, 10, 64]> self = ?", "List[int] size = [1, 16, 10, 64]"],
        ["Tensor<[1, 16, 64, 10]> self = ?", "List[int] size = [1, 16, 64, 10]"],
        ["Tensor<[1, 16, 10, 10]> self = ?", "List[int] size = [1, 16, 10, 10]"],
        ["Tensor<[1, 16, 64, 1]> self = ?", "List[int] size = [1, 16, 64, 1]"],
        ["Tensor<[1, 16, 1, 1]> self = ?", "List[int] size = [1, 16, 1, 1]"],
        ["Tensor<[1, 16, 1, 10]> self = ?", "List[int] size = [1, 16, 1, 10]"],
        ["Tensor<[1, 16, 64, 2]> self = ?", "List[int] size = [1, 16, 64, 2]"],
        ["Tensor<[1, 16, 1, 2]> self = ?", "List[int] size = [1, 16, 1, 2]"],
        ["Tensor<[1, 16, 2, 64]> self = ?", "List[int] size = [1, 16, 2, 64]"],
        ["Tensor<[1, 16, 64, s0 + 1]> self = ?", "List[int] size = [1, 16, 64, <s0 + 1>]"],
        ["Tensor<[1, 16, 1, s0 + 1]> self = ?", "List[int] size = [1, 16, 1, <s0 + 1>]"],
        ["Tensor<[1, 16, s0 + 1, 64]> self = ?", "List[int] size = [1, 16, <s0 + 1>, 64]"],
        ["Tensor<[1, 8, 10, 64]> self = ?", "List[int] size = [1, 8, 10, 64]"],
        ["Tensor<[1, 8, 64, 10]> self = ?", "List[int] size = [1, 8, 64, 10]"],
        ["Tensor<[1, 8, 10, 10]> self = ?", "List[int] size = [1, 8, 10, 10]"],
        ["Tensor<[1, 8, 1, 64]> self = ?", "List[int] size = [1, 8, 1, 64]"],
        ["Tensor<[1, 8, 64, 1]> self = ?", "List[int] size = [1, 8, 64, 1]"],
        ["Tensor<[1, 8, 1, 1]> self = ?", "List[int] size = [1, 8, 1, 1]"],
        ["Tensor<[1, 8, 1, 10]> self = ?", "List[int] size = [1, 8, 1, 10]"],
        ["Tensor<[1, 8, 64, 2]> self = ?", "List[int] size = [1, 8, 64, 2]"],
        ["Tensor<[1, 8, 1, 2]> self = ?", "List[int] size = [1, 8, 1, 2]"],
        ["Tensor<[1, 8, 2, 64]> self = ?", "List[int] size = [1, 8, 2, 64]"],
        ["Tensor<[1, 8, 64, s0 + 1]> self = ?", "List[int] size = [1, 8, 64, <s0 + 1>]"],
        ["Tensor<[1, 8, 1, s0 + 1]> self = ?", "List[int] size = [1, 8, 1, <s0 + 1>]"],
        ["Tensor<[1, 8, s0 + 1, 64]> self = ?", "List[int] size = [1, 8, <s0 + 1>, 64]"],
        ["Tensor<[1, 1280, 1, 1]> self = ?", "List[int] size = [1, 1280, 7, 7]"],
        ["Tensor<[1, 1280, 1, 1]> self = ?", "List[int] size = [1, 1280, 8, 8]"],
        ["Tensor<[1, 1280, 1, 1]> self = ?", "List[int] size = [1, 1280, 9, 9]"],
        ["Tensor<[1, 1280, 1, 1]> self = ?", "List[int] size = [1, 1280, 10, 10]"],
        ["Tensor<[1, 1280, 1, 1]> self = ?", "List[int] size = [1, 1280, 12, 12]"],
        ["Tensor<[1, 12, 14, 64]> self = ?", "List[int] size = [1, 12, 14, 64]"],
        ["Tensor<[1, 12, 64, 14]> self = ?", "List[int] size = [1, 12, 64, 14]"],
        ["Tensor<[1, 12, 14, 14]> self = ?", "List[int] size = [1, 12, 14, 14]"],
        ["Tensor<[1, 1, 1280]> self = ?", "List[int] size = [1, -1, -1]"],
        ["Tensor<[1, 2048, 1, 1]> self = ?", "List[int] size = [1, 2048, 10, 10]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.expand.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.expand.default", input_strings
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
