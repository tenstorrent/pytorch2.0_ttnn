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
        return torch.ops.aten.relu.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.relu.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 16, 28, 28]> self = ?"],
        ["Tensor<[1, 4, 14, 14]> self = ?"],
        ["Tensor<[1, 16, 14, 14]> self = ?"],
        ["Tensor<[1, 128]> self = ?"],
        ["Tensor<[1, 64]> self = ?"],
        ["Tensor<[1, 12]> self = ?"],
        ["Tensor<[1, 64, 360, 640]> self = ?"],
        ["Tensor<[1, 64, 180, 320]> self = ?"],
        ["Tensor<[1, 256, 180, 320]> self = ?"],
        ["Tensor<[1, 128, 180, 320]> self = ?"],
        ["Tensor<[1, 128, 90, 160]> self = ?"],
        ["Tensor<[1, 512, 90, 160]> self = ?"],
        ["Tensor<[1, 256, 90, 160]> self = ?"],
        ["Tensor<[1, 256, 45, 80]> self = ?"],
        ["Tensor<[1, 1024, 45, 80]> self = ?"],
        ["Tensor<[1, 512, 45, 80]> self = ?"],
        ["Tensor<[1, 512, 23, 40]> self = ?"],
        ["Tensor<[1, 2048, 23, 40]> self = ?"],
        ["Tensor<[920, 1, 2048]> self = ?"],
        ["Tensor<[100, 1, 2048]> self = ?"],
        ["Tensor<[6, 1, 100, 256]> self = ?"],
        ["Tensor<[1, 64, 30, 40]> self = ?"],
        ["Tensor<[1, 32, 30, 40]> self = ?"],
        ["Tensor<[1, 64, 60, 80]> self = ?"],
        ["Tensor<[1, 32, 60, 80]> self = ?"],
        ["Tensor<[1, 64, 120, 160]> self = ?"],
        ["Tensor<[1, 32, 120, 160]> self = ?"],
        ["Tensor<[1, 64, 480, 640]> self = ?"],
        ["Tensor<[1, 32, 26, 26]> self = ?"],
        ["Tensor<[1, 64, 24, 24]> self = ?"],
        ["Tensor<[1, 16, 160, 160]> self = ?"],
        ["Tensor<[1, 64, 160, 160]> self = ?"],
        ["Tensor<[1, 64, 80, 80]> self = ?"],
        ["Tensor<[1, 72, 80, 80]> self = ?"],
        ["Tensor<[1, 72, 40, 40]> self = ?"],
        ["Tensor<[1, 24, 1, 1]> self = ?"],
        ["Tensor<[1, 120, 40, 40]> self = ?"],
        ["Tensor<[1, 32, 1, 1]> self = ?"],
        ["Tensor<[1, 120, 1, 1]> self = ?"],
        ["Tensor<[1, 168, 1, 1]> self = ?"],
        ["Tensor<[59, 4096]> self = ?"],
        ["Tensor<[1, 4096]> self = ?"],
        ["Tensor<[1, 32, 112, 112]> self = ?"],
        ["Tensor<[1, 64, 112, 112]> self = ?"],
        ["Tensor<[1, 64, 56, 56]> self = ?"],
        ["Tensor<[1, 128, 56, 56]> self = ?"],
        ["Tensor<[1, 128, 28, 28]> self = ?"],
        ["Tensor<[1, 256, 28, 28]> self = ?"],
        ["Tensor<[1, 512, 28, 28]> self = ?"],
        ["Tensor<[1, 256, 14, 14]> self = ?"],
        ["Tensor<[1, 512, 7, 7]> self = ?"],
        ["Tensor<[1, 256, 56, 56]> self = ?"],
        ["Tensor<[1, 1024, 14, 14]> self = ?"],
        ["Tensor<[1, 512, 14, 14]> self = ?"],
        ["Tensor<[1, 2048, 7, 7]> self = ?"],
        ["Tensor<[1, 256, 128, 128]> self = ?"],
        ["Tensor<[1, 32, 256, 256]> self = ?"],
        ["Tensor<[1, 64, 128, 128]> self = ?"],
        ["Tensor<[1, 128, 64, 64]> self = ?"],
        ["Tensor<[1, 256, 32, 32]> self = ?"],
        ["Tensor<[1, 512, 16, 16]> self = ?"],
        ["Tensor<[1, 64, 224, 224]> self = ?"],
        ["Tensor<[1, 128, 112, 112]> self = ?"],
        ["Tensor<[1, 100, 192]> self = ?"],
        ["Tensor<[1, 96, 56, 56]> self = ?"],
        ["Tensor<[1, 160, 56, 56]> self = ?"],
        ["Tensor<[1, 192, 56, 56]> self = ?"],
        ["Tensor<[1, 224, 56, 56]> self = ?"],
        ["Tensor<[1, 160, 28, 28]> self = ?"],
        ["Tensor<[1, 192, 28, 28]> self = ?"],
        ["Tensor<[1, 224, 28, 28]> self = ?"],
        ["Tensor<[1, 288, 28, 28]> self = ?"],
        ["Tensor<[1, 320, 28, 28]> self = ?"],
        ["Tensor<[1, 352, 28, 28]> self = ?"],
        ["Tensor<[1, 384, 28, 28]> self = ?"],
        ["Tensor<[1, 416, 28, 28]> self = ?"],
        ["Tensor<[1, 448, 28, 28]> self = ?"],
        ["Tensor<[1, 480, 28, 28]> self = ?"],
        ["Tensor<[1, 128, 14, 14]> self = ?"],
        ["Tensor<[1, 288, 14, 14]> self = ?"],
        ["Tensor<[1, 320, 14, 14]> self = ?"],
        ["Tensor<[1, 352, 14, 14]> self = ?"],
        ["Tensor<[1, 384, 14, 14]> self = ?"],
        ["Tensor<[1, 416, 14, 14]> self = ?"],
        ["Tensor<[1, 448, 14, 14]> self = ?"],
        ["Tensor<[1, 480, 14, 14]> self = ?"],
        ["Tensor<[1, 544, 14, 14]> self = ?"],
        ["Tensor<[1, 576, 14, 14]> self = ?"],
        ["Tensor<[1, 608, 14, 14]> self = ?"],
        ["Tensor<[1, 640, 14, 14]> self = ?"],
        ["Tensor<[1, 672, 14, 14]> self = ?"],
        ["Tensor<[1, 704, 14, 14]> self = ?"],
        ["Tensor<[1, 736, 14, 14]> self = ?"],
        ["Tensor<[1, 768, 14, 14]> self = ?"],
        ["Tensor<[1, 800, 14, 14]> self = ?"],
        ["Tensor<[1, 832, 14, 14]> self = ?"],
        ["Tensor<[1, 864, 14, 14]> self = ?"],
        ["Tensor<[1, 896, 14, 14]> self = ?"],
        ["Tensor<[1, 928, 14, 14]> self = ?"],
        ["Tensor<[1, 960, 14, 14]> self = ?"],
        ["Tensor<[1, 992, 14, 14]> self = ?"],
        ["Tensor<[1, 128, 7, 7]> self = ?"],
        ["Tensor<[1, 544, 7, 7]> self = ?"],
        ["Tensor<[1, 576, 7, 7]> self = ?"],
        ["Tensor<[1, 608, 7, 7]> self = ?"],
        ["Tensor<[1, 640, 7, 7]> self = ?"],
        ["Tensor<[1, 672, 7, 7]> self = ?"],
        ["Tensor<[1, 704, 7, 7]> self = ?"],
        ["Tensor<[1, 736, 7, 7]> self = ?"],
        ["Tensor<[1, 768, 7, 7]> self = ?"],
        ["Tensor<[1, 800, 7, 7]> self = ?"],
        ["Tensor<[1, 832, 7, 7]> self = ?"],
        ["Tensor<[1, 864, 7, 7]> self = ?"],
        ["Tensor<[1, 896, 7, 7]> self = ?"],
        ["Tensor<[1, 928, 7, 7]> self = ?"],
        ["Tensor<[1, 960, 7, 7]> self = ?"],
        ["Tensor<[1, 992, 7, 7]> self = ?"],
        ["Tensor<[1, 1024, 7, 7]> self = ?"],
        ["Tensor<[1, 96, 112, 112]> self = ?"],
        ["Tensor<[1, 144, 56, 56]> self = ?"],
        ["Tensor<[1, 240, 56, 56]> self = ?"],
        ["Tensor<[1, 288, 56, 56]> self = ?"],
        ["Tensor<[1, 336, 56, 56]> self = ?"],
        ["Tensor<[1, 384, 56, 56]> self = ?"],
        ["Tensor<[1, 240, 28, 28]> self = ?"],
        ["Tensor<[1, 336, 28, 28]> self = ?"],
        ["Tensor<[1, 432, 28, 28]> self = ?"],
        ["Tensor<[1, 528, 28, 28]> self = ?"],
        ["Tensor<[1, 576, 28, 28]> self = ?"],
        ["Tensor<[1, 624, 28, 28]> self = ?"],
        ["Tensor<[1, 672, 28, 28]> self = ?"],
        ["Tensor<[1, 720, 28, 28]> self = ?"],
        ["Tensor<[1, 768, 28, 28]> self = ?"],
        ["Tensor<[1, 192, 14, 14]> self = ?"],
        ["Tensor<[1, 432, 14, 14]> self = ?"],
        ["Tensor<[1, 528, 14, 14]> self = ?"],
        ["Tensor<[1, 624, 14, 14]> self = ?"],
        ["Tensor<[1, 720, 14, 14]> self = ?"],
        ["Tensor<[1, 816, 14, 14]> self = ?"],
        ["Tensor<[1, 912, 14, 14]> self = ?"],
        ["Tensor<[1, 1008, 14, 14]> self = ?"],
        ["Tensor<[1, 1056, 14, 14]> self = ?"],
        ["Tensor<[1, 1104, 14, 14]> self = ?"],
        ["Tensor<[1, 1152, 14, 14]> self = ?"],
        ["Tensor<[1, 1200, 14, 14]> self = ?"],
        ["Tensor<[1, 1248, 14, 14]> self = ?"],
        ["Tensor<[1, 1296, 14, 14]> self = ?"],
        ["Tensor<[1, 1344, 14, 14]> self = ?"],
        ["Tensor<[1, 1392, 14, 14]> self = ?"],
        ["Tensor<[1, 1440, 14, 14]> self = ?"],
        ["Tensor<[1, 1488, 14, 14]> self = ?"],
        ["Tensor<[1, 1536, 14, 14]> self = ?"],
        ["Tensor<[1, 1584, 14, 14]> self = ?"],
        ["Tensor<[1, 1632, 14, 14]> self = ?"],
        ["Tensor<[1, 1680, 14, 14]> self = ?"],
        ["Tensor<[1, 1728, 14, 14]> self = ?"],
        ["Tensor<[1, 1776, 14, 14]> self = ?"],
        ["Tensor<[1, 1824, 14, 14]> self = ?"],
        ["Tensor<[1, 1872, 14, 14]> self = ?"],
        ["Tensor<[1, 1920, 14, 14]> self = ?"],
        ["Tensor<[1, 1968, 14, 14]> self = ?"],
        ["Tensor<[1, 2016, 14, 14]> self = ?"],
        ["Tensor<[1, 2064, 14, 14]> self = ?"],
        ["Tensor<[1, 2112, 14, 14]> self = ?"],
        ["Tensor<[1, 1056, 7, 7]> self = ?"],
        ["Tensor<[1, 192, 7, 7]> self = ?"],
        ["Tensor<[1, 1104, 7, 7]> self = ?"],
        ["Tensor<[1, 1152, 7, 7]> self = ?"],
        ["Tensor<[1, 1200, 7, 7]> self = ?"],
        ["Tensor<[1, 1248, 7, 7]> self = ?"],
        ["Tensor<[1, 1296, 7, 7]> self = ?"],
        ["Tensor<[1, 1344, 7, 7]> self = ?"],
        ["Tensor<[1, 1392, 7, 7]> self = ?"],
        ["Tensor<[1, 1440, 7, 7]> self = ?"],
        ["Tensor<[1, 1488, 7, 7]> self = ?"],
        ["Tensor<[1, 1536, 7, 7]> self = ?"],
        ["Tensor<[1, 1584, 7, 7]> self = ?"],
        ["Tensor<[1, 1632, 7, 7]> self = ?"],
        ["Tensor<[1, 1680, 7, 7]> self = ?"],
        ["Tensor<[1, 1728, 7, 7]> self = ?"],
        ["Tensor<[1, 1776, 7, 7]> self = ?"],
        ["Tensor<[1, 1824, 7, 7]> self = ?"],
        ["Tensor<[1, 1872, 7, 7]> self = ?"],
        ["Tensor<[1, 1920, 7, 7]> self = ?"],
        ["Tensor<[1, 1968, 7, 7]> self = ?"],
        ["Tensor<[1, 2016, 7, 7]> self = ?"],
        ["Tensor<[1, 2064, 7, 7]> self = ?"],
        ["Tensor<[1, 2112, 7, 7]> self = ?"],
        ["Tensor<[1, 2160, 7, 7]> self = ?"],
        ["Tensor<[1, 2208, 7, 7]> self = ?"],
        ["Tensor<[1, 1088, 14, 14]> self = ?"],
        ["Tensor<[1, 1120, 14, 14]> self = ?"],
        ["Tensor<[1, 1184, 14, 14]> self = ?"],
        ["Tensor<[1, 1216, 14, 14]> self = ?"],
        ["Tensor<[1, 1280, 14, 14]> self = ?"],
        ["Tensor<[1, 1088, 7, 7]> self = ?"],
        ["Tensor<[1, 1120, 7, 7]> self = ?"],
        ["Tensor<[1, 1184, 7, 7]> self = ?"],
        ["Tensor<[1, 1216, 7, 7]> self = ?"],
        ["Tensor<[1, 1280, 7, 7]> self = ?"],
        ["Tensor<[1, 1312, 7, 7]> self = ?"],
        ["Tensor<[1, 1376, 7, 7]> self = ?"],
        ["Tensor<[1, 1408, 7, 7]> self = ?"],
        ["Tensor<[1, 1472, 7, 7]> self = ?"],
        ["Tensor<[1, 1504, 7, 7]> self = ?"],
        ["Tensor<[1, 1568, 7, 7]> self = ?"],
        ["Tensor<[1, 1600, 7, 7]> self = ?"],
        ["Tensor<[1, 1664, 7, 7]> self = ?"],
        ["Tensor<[1, 1312, 14, 14]> self = ?"],
        ["Tensor<[1, 1376, 14, 14]> self = ?"],
        ["Tensor<[1, 1408, 14, 14]> self = ?"],
        ["Tensor<[1, 1472, 14, 14]> self = ?"],
        ["Tensor<[1, 1504, 14, 14]> self = ?"],
        ["Tensor<[1, 1568, 14, 14]> self = ?"],
        ["Tensor<[1, 1600, 14, 14]> self = ?"],
        ["Tensor<[1, 1664, 14, 14]> self = ?"],
        ["Tensor<[1, 1696, 14, 14]> self = ?"],
        ["Tensor<[1, 1760, 14, 14]> self = ?"],
        ["Tensor<[1, 1792, 14, 14]> self = ?"],
        ["Tensor<[1, 1696, 7, 7]> self = ?"],
        ["Tensor<[1, 1760, 7, 7]> self = ?"],
        ["Tensor<[1, 1792, 7, 7]> self = ?"],
        ["Tensor<[1, 1856, 7, 7]> self = ?"],
        ["Tensor<[1, 1888, 7, 7]> self = ?"],
        ["Tensor<[1, 16, 224, 224]> self = ?"],
        ["Tensor<[1, 224, 7, 7]> self = ?"],
        ["Tensor<[1, 16, 112, 112]> self = ?"],
        ["Tensor<[1, 8, 112, 112]> self = ?"],
        ["Tensor<[1, 24, 112, 112]> self = ?"],
        ["Tensor<[1, 36, 56, 56]> self = ?"],
        ["Tensor<[1, 20, 1, 1]> self = ?"],
        ["Tensor<[1, 60, 28, 28]> self = ?"],
        ["Tensor<[1, 120, 28, 28]> self = ?"],
        ["Tensor<[1, 100, 14, 14]> self = ?"],
        ["Tensor<[1, 92, 14, 14]> self = ?"],
        ["Tensor<[1, 240, 14, 14]> self = ?"],
        ["Tensor<[1, 336, 14, 14]> self = ?"],
        ["Tensor<[1, 480, 7, 7]> self = ?"],
        ["Tensor<[1, 240, 1, 1]> self = ?"],
        ["Tensor<[1, 1280, 1, 1]> self = ?"],
        ["Tensor<[1, 64, 28, 28]> self = ?"],
        ["Tensor<[1, 96, 28, 28]> self = ?"],
        ["Tensor<[1, 32, 28, 28]> self = ?"],
        ["Tensor<[1, 96, 14, 14]> self = ?"],
        ["Tensor<[1, 208, 14, 14]> self = ?"],
        ["Tensor<[1, 48, 14, 14]> self = ?"],
        ["Tensor<[1, 64, 14, 14]> self = ?"],
        ["Tensor<[1, 160, 14, 14]> self = ?"],
        ["Tensor<[1, 112, 14, 14]> self = ?"],
        ["Tensor<[1, 224, 14, 14]> self = ?"],
        ["Tensor<[1, 24, 14, 14]> self = ?"],
        ["Tensor<[1, 144, 14, 14]> self = ?"],
        ["Tensor<[1, 32, 14, 14]> self = ?"],
        ["Tensor<[1, 256, 7, 7]> self = ?"],
        ["Tensor<[1, 160, 7, 7]> self = ?"],
        ["Tensor<[1, 320, 7, 7]> self = ?"],
        ["Tensor<[1, 32, 7, 7]> self = ?"],
        ["Tensor<[1, 384, 7, 7]> self = ?"],
        ["Tensor<[1, 48, 7, 7]> self = ?"],
        ["Tensor<[1, 18, 56, 56]> self = ?"],
        ["Tensor<[1, 36, 28, 28]> self = ?"],
        ["Tensor<[1, 72, 14, 14]> self = ?"],
        ["Tensor<[1, 18, 28, 28]> self = ?"],
        ["Tensor<[1, 144, 7, 7]> self = ?"],
        ["Tensor<[1, 18, 14, 14]> self = ?"],
        ["Tensor<[1, 36, 14, 14]> self = ?"],
        ["Tensor<[1, 32, 56, 56]> self = ?"],
        ["Tensor<[1, 32, 149, 149]> self = ?"],
        ["Tensor<[1, 32, 147, 147]> self = ?"],
        ["Tensor<[1, 64, 147, 147]> self = ?"],
        ["Tensor<[1, 96, 73, 73]> self = ?"],
        ["Tensor<[1, 64, 73, 73]> self = ?"],
        ["Tensor<[1, 96, 71, 71]> self = ?"],
        ["Tensor<[1, 192, 35, 35]> self = ?"],
        ["Tensor<[1, 96, 35, 35]> self = ?"],
        ["Tensor<[1, 64, 35, 35]> self = ?"],
        ["Tensor<[1, 384, 17, 17]> self = ?"],
        ["Tensor<[1, 224, 35, 35]> self = ?"],
        ["Tensor<[1, 256, 17, 17]> self = ?"],
        ["Tensor<[1, 192, 17, 17]> self = ?"],
        ["Tensor<[1, 224, 17, 17]> self = ?"],
        ["Tensor<[1, 128, 17, 17]> self = ?"],
        ["Tensor<[1, 192, 8, 8]> self = ?"],
        ["Tensor<[1, 320, 17, 17]> self = ?"],
        ["Tensor<[1, 320, 8, 8]> self = ?"],
        ["Tensor<[1, 256, 8, 8]> self = ?"],
        ["Tensor<[1, 384, 8, 8]> self = ?"],
        ["Tensor<[1, 448, 8, 8]> self = ?"],
        ["Tensor<[1, 512, 8, 8]> self = ?"],
        ["Tensor<[1, 72, 56, 56]> self = ?"],
        ["Tensor<[1, 72, 28, 28]> self = ?"],
        ["Tensor<[1, 16, 56, 56]> self = ?"],
        ["Tensor<[1, 8, 1, 1]> self = ?"],
        ["Tensor<[1, 88, 28, 28]> self = ?"],
        ["Tensor<[1, 64, 1, 1]> self = ?"],
        ["Tensor<[1, 40, 1, 1]> self = ?"],
        ["Tensor<[1, 72, 1, 1]> self = ?"],
        ["Tensor<[1, 144, 1, 1]> self = ?"],
        ["Tensor<[1, 256, 112, 112]> self = ?"],
        ["Tensor<[1, 512, 56, 56]> self = ?"],
        ["Tensor<[1, 896, 28, 28]> self = ?"],
        ["Tensor<[1, 2048, 14, 14]> self = ?"],
        ["Tensor<[1, 72, 112, 112]> self = ?"],
        ["Tensor<[1, 168, 56, 56]> self = ?"],
        ["Tensor<[1, 168, 28, 28]> self = ?"],
        ["Tensor<[1, 408, 28, 28]> self = ?"],
        ["Tensor<[1, 408, 14, 14]> self = ?"],
        ["Tensor<[1, 912, 7, 7]> self = ?"],
        ["Tensor<[1, 336, 112, 112]> self = ?"],
        ["Tensor<[1, 672, 56, 56]> self = ?"],
        ["Tensor<[1, 1344, 28, 28]> self = ?"],
        ["Tensor<[1, 2520, 14, 14]> self = ?"],
        ["Tensor<[1, 2520, 7, 7]> self = ?"],
        ["Tensor<[1, 1008, 7, 7]> self = ?"],
        ["Tensor<[1, 400, 14, 14]> self = ?"],
        ["Tensor<[1, 400, 7, 7]> self = ?"],
        ["Tensor<[1, 80, 112, 112]> self = ?"],
        ["Tensor<[1, 80, 56, 56]> self = ?"],
        ["Tensor<[1, 32, 192, 192]> self = ?"],
        ["Tensor<[1, 528, 192, 192]> self = ?"],
        ["Tensor<[1, 528, 96, 96]> self = ?"],
        ["Tensor<[1, 132, 1, 1]> self = ?"],
        ["Tensor<[1, 1056, 96, 96]> self = ?"],
        ["Tensor<[1, 1056, 48, 48]> self = ?"],
        ["Tensor<[1, 264, 1, 1]> self = ?"],
        ["Tensor<[1, 2904, 48, 48]> self = ?"],
        ["Tensor<[1, 2904, 24, 24]> self = ?"],
        ["Tensor<[1, 726, 1, 1]> self = ?"],
        ["Tensor<[1, 7392, 24, 24]> self = ?"],
        ["Tensor<[1, 7392, 12, 12]> self = ?"],
        ["Tensor<[1, 224, 112, 112]> self = ?"],
        ["Tensor<[1, 56, 1, 1]> self = ?"],
        ["Tensor<[1, 448, 56, 56]> self = ?"],
        ["Tensor<[1, 112, 1, 1]> self = ?"],
        ["Tensor<[1, 1232, 28, 28]> self = ?"],
        ["Tensor<[1, 1232, 14, 14]> self = ?"],
        ["Tensor<[1, 308, 1, 1]> self = ?"],
        ["Tensor<[1, 3024, 14, 14]> self = ?"],
        ["Tensor<[1, 3024, 7, 7]> self = ?"],
        ["Tensor<[1, 48, 112, 112]> self = ?"],
        ["Tensor<[1, 48, 56, 56]> self = ?"],
        ["Tensor<[1, 12, 1, 1]> self = ?"],
        ["Tensor<[1, 120, 56, 56]> self = ?"],
        ["Tensor<[1, 30, 1, 1]> self = ?"],
        ["Tensor<[1, 84, 1, 1]> self = ?"],
        ["Tensor<[1, 888, 14, 14]> self = ?"],
        ["Tensor<[1, 888, 7, 7]> self = ?"],
        ["Tensor<[1, 222, 1, 1]> self = ?"],
        ["Tensor<[1, 232, 112, 112]> self = ?"],
        ["Tensor<[1, 232, 56, 56]> self = ?"],
        ["Tensor<[1, 58, 1, 1]> self = ?"],
        ["Tensor<[1, 696, 56, 56]> self = ?"],
        ["Tensor<[1, 696, 28, 28]> self = ?"],
        ["Tensor<[1, 174, 1, 1]> self = ?"],
        ["Tensor<[1, 1392, 28, 28]> self = ?"],
        ["Tensor<[1, 348, 1, 1]> self = ?"],
        ["Tensor<[1, 3712, 14, 14]> self = ?"],
        ["Tensor<[1, 3712, 7, 7]> self = ?"],
        ["Tensor<[1, 18, 1, 1]> self = ?"],
        ["Tensor<[1, 216, 56, 56]> self = ?"],
        ["Tensor<[1, 216, 28, 28]> self = ?"],
        ["Tensor<[1, 54, 1, 1]> self = ?"],
        ["Tensor<[1, 1512, 14, 14]> self = ?"],
        ["Tensor<[1, 1512, 7, 7]> self = ?"],
        ["Tensor<[1, 104, 56, 56]> self = ?"],
        ["Tensor<[1, 104, 28, 28]> self = ?"],
        ["Tensor<[1, 26, 1, 1]> self = ?"],
        ["Tensor<[1, 208, 28, 28]> self = ?"],
        ["Tensor<[1, 52, 1, 1]> self = ?"],
        ["Tensor<[1, 440, 14, 14]> self = ?"],
        ["Tensor<[1, 440, 7, 7]> self = ?"],
        ["Tensor<[1, 110, 1, 1]> self = ?"],
        ["Tensor<[1, 144, 28, 28]> self = ?"],
        ["Tensor<[1, 16, 1, 1]> self = ?"],
        ["Tensor<[1, 36, 1, 1]> self = ?"],
        ["Tensor<[1, 80, 1, 1]> self = ?"],
        ["Tensor<[1, 784, 14, 14]> self = ?"],
        ["Tensor<[1, 784, 7, 7]> self = ?"],
        ["Tensor<[1, 196, 1, 1]> self = ?"],
        ["Tensor<[1, 224, 1, 1]> self = ?"],
        ["Tensor<[1, 1024, 28, 28]> self = ?"],
        ["Tensor<[1, 64, 400, 544]> self = ?"],
        ["Tensor<[1, 64, 200, 272]> self = ?"],
        ["Tensor<[1, 256, 200, 272]> self = ?"],
        ["Tensor<[1, 128, 200, 272]> self = ?"],
        ["Tensor<[1, 128, 100, 136]> self = ?"],
        ["Tensor<[1, 512, 100, 136]> self = ?"],
        ["Tensor<[1, 256, 100, 136]> self = ?"],
        ["Tensor<[1, 256, 50, 68]> self = ?"],
        ["Tensor<[1, 1024, 50, 68]> self = ?"],
        ["Tensor<[1, 512, 50, 68]> self = ?"],
        ["Tensor<[1, 512, 25, 34]> self = ?"],
        ["Tensor<[1, 2048, 25, 34]> self = ?"],
        ["Tensor<[1, 256, 13, 17]> self = ?"],
        ["Tensor<[1, 256, 25, 34]> self = ?"],
        ["Tensor<[1, 256, 7, 9]> self = ?"],
        ["Tensor<[1, 64, 300, 300]> self = ?"],
        ["Tensor<[1, 128, 150, 150]> self = ?"],
        ["Tensor<[1, 256, 75, 75]> self = ?"],
        ["Tensor<[1, 512, 38, 38]> self = ?"],
        ["Tensor<[1, 512, 19, 19]> self = ?"],
        ["Tensor<[1, 1024, 19, 19]> self = ?"],
        ["Tensor<[1, 256, 19, 19]> self = ?"],
        ["Tensor<[1, 512, 10, 10]> self = ?"],
        ["Tensor<[1, 128, 10, 10]> self = ?"],
        ["Tensor<[1, 256, 5, 5]> self = ?"],
        ["Tensor<[1, 128, 5, 5]> self = ?"],
        ["Tensor<[1, 256, 3, 3]> self = ?"],
        ["Tensor<[1, 128, 3, 3]> self = ?"],
        ["Tensor<[1, 256, 1, 1]> self = ?"],
        ["Tensor<[1, 15, 15, 512]> self = ?"],
        ["Tensor<[1, 10, 3072]> self = ?"],
        ["Tensor<[1, 1, 3072]> self = ?"],
        ["Tensor<[1, 10, 4096]> self = ?"],
        ["Tensor<[1, 1, 4096]> self = ?"],
        ["Tensor<[1, 10, 2048]> self = ?"],
        ["Tensor<[1, 1, 2048]> self = ?"],
        ["Tensor<[1, 32, 150, 150]> self = ?"],
        ["Tensor<[1, 64, 150, 150]> self = ?"],
        ["Tensor<[1, 128, 75, 75]> self = ?"],
        ["Tensor<[1, 256, 38, 38]> self = ?"],
        ["Tensor<[1, 728, 38, 38]> self = ?"],
        ["Tensor<[1, 728, 19, 19]> self = ?"],
        ["Tensor<[1, 1024, 10, 10]> self = ?"],
        ["Tensor<[1, 1536, 10, 10]> self = ?"],
        ["Tensor<[1, 2048, 10, 10]> self = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.relu.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.relu.default", input_strings
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
