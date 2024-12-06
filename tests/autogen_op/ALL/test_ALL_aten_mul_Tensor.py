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
        return torch.ops.aten.mul.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.mul.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 1, 1, 256]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 32]> self = ?", "Tensor<[1, 32]> other = ?"],
        ["Tensor<[16, 1]> self = ?", "Tensor<[1, 1, 32]> other = ?"],
        ["Tensor<[1, 32, 6144]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 32, 6144]> self = ?", "Tensor other = 0.79788456"],
        ["Tensor<[1, 32, 6144]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 32, 6144]> self = ?", "Tensor<[1, 32, 6144]> other = ?"],
        ["Tensor<[1, 50, 768]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[1, 50, 3072]> self = ?", "Tensor other = 1.702"],
        ["Tensor<[1, 50, 3072]> self = ?", "Tensor<[1, 50, 3072]> other = ?"],
        ["Tensor<[2, 7, 512]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[2, 7, 2048]> self = ?", "Tensor other = 1.702"],
        ["Tensor<[2, 7, 2048]> self = ?", "Tensor<[2, 7, 2048]> other = ?"],
        ["Tensor<[2, 1]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[2, 1]> self = ?", "Tensor<[2, 1]> other = ?"],
        ["Tensor<[]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[2, 512]> self = ?", "Tensor<[2, 512]> other = ?"],
        ["Tensor<[2, 1]> self = ?", "Tensor<[2, 512]> other = ?"],
        ["Tensor<[1, 512]> self = ?", "Tensor<[1, 512]> other = ?"],
        ["Tensor<[1, 1]> self = ?", "Tensor<[1, 512]> other = ?"],
        ["Tensor<[1, 64, 1, 1]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 64, 360, 640]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 64, 180, 320]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 1, 1]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 180, 320]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 1, 1]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 180, 320]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 90, 160]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 1, 1]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 90, 160]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 90, 160]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 45, 80]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 1, 1]> self = ?", "Tensor<[1, 1024, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 45, 80]> self = ?", "Tensor<[1, 1024, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 45, 80]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 23, 40]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 2048, 1, 1]> self = ?", "Tensor<[1, 2048, 1, 1]> other = ?"],
        ["Tensor<[1, 2048, 23, 40]> self = ?", "Tensor<[1, 2048, 1, 1]> other = ?"],
        ["Tensor<[23]> self = ?", "Tensor other = 31.304347826086957"],
        ["Tensor<[40]> self = ?", "Tensor other = 32.0"],
        ["Tensor<[1, 23, 40]> self = ?", "Tensor other = 6.283185307179586"],
        ["Tensor<[128]> self = ?", "Tensor other = 2"],
        ["Tensor<[1, 1, 1, 25]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 1, 1, 15]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 15, 512]> self = ?", "Tensor<[1, 15, 1]> other = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[1, 15, 512]> other = ?"],
        ["Tensor<[15, 15]> self = ?", "Tensor other = 16"],
        ["Tensor<[15, 15]> self = ?", "Tensor other = 8"],
        ["Tensor<[1, 15, 1024]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 15, 1024]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 15, 1024]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 15, 1024]> self = ?", "Tensor<[1, 15, 1024]> other = ?"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 0"],
        ["Tensor<[1, 1, 1, 1]> self = ?", "Tensor<[1, 1, 1, 1]> other = ?"],
        ["Tensor<[1, 1, 1, 1]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 1, 512]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[1, 1, 512]> other = ?"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 16"],
        ["Tensor<[1, 1, 1024]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 1, 1024]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 1, 1024]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 1, 1024]> self = ?", "Tensor<[1, 1, 1024]> other = ?"],
        ["Tensor<[1, 1, 1, 2]> self = ?", "Tensor<[1, 1, 1, 2]> other = ?"],
        ["Tensor<[1, 1, 1, 2]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[2, 2]> self = ?", "Tensor other = 16"],
        ["Tensor<[1, 1, 1, s0 + 1]> self = ?", "Tensor<[1, 1, 1, s0 + 1]> other = ?"],
        ["Tensor<[1, 1, 1, s0 + 1]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[s0 + 1, s0 + 1]> self = ?", "Tensor other = 16"],
        ["Tensor<[1, 1, 1, 17]> self = ?", "Tensor<[1, 1, 1, 17]> other = ?"],
        ["Tensor<[1, 1, 1, 17]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[17, 17]> self = ?", "Tensor other = 16"],
        ["Tensor<[30]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[40]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 64, 30, 40]> self = ?", "Tensor<[30, 1]> other = ?"],
        ["Tensor<[1, 64, 30, 40]> self = ?", "Tensor<[40]> other = ?"],
        ["Tensor<[1, 64, 30, 40]> self = ?", "Tensor<[1, 1, 30, 40]> other = ?"],
        ["Tensor<[60]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[80]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 64, 60, 80]> self = ?", "Tensor<[60, 1]> other = ?"],
        ["Tensor<[1, 64, 60, 80]> self = ?", "Tensor<[80]> other = ?"],
        ["Tensor<[1, 64, 60, 80]> self = ?", "Tensor<[1, 1, 60, 80]> other = ?"],
        ["Tensor<[120]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[160]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 64, 120, 160]> self = ?", "Tensor<[120, 1]> other = ?"],
        ["Tensor<[1, 64, 120, 160]> self = ?", "Tensor<[160]> other = ?"],
        ["Tensor<[1, 64, 120, 160]> self = ?", "Tensor<[1, 1, 120, 160]> other = ?"],
        ["Tensor<[240]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[320]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 64, 240, 320]> self = ?", "Tensor<[240, 1]> other = ?"],
        ["Tensor<[1, 64, 240, 320]> self = ?", "Tensor<[320]> other = ?"],
        ["Tensor<[480]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[640]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 64, 480, 640]> self = ?", "Tensor<[480, 1]> other = ?"],
        ["Tensor<[1, 64, 480, 640]> self = ?", "Tensor<[640]> other = ?"],
        ["Tensor<[1, 1, 480, 640]> self = ?", "Tensor other = 10"],
        ["Tensor<[1, 1, 1, 7]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 7, 3072]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 7, 3072]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 7, 3072]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 7, 3072]> self = ?", "Tensor<[1, 7, 3072]> other = ?"],
        ["Tensor<[1, 45, 3072]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 45, 3072]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 45, 3072]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 45, 3072]> self = ?", "Tensor<[1, 45, 3072]> other = ?"],
        ["Tensor<[1, 1, 3072]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 1, 3072]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 1, 3072]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 1, 3072]> self = ?", "Tensor<[1, 1, 3072]> other = ?"],
        ["Tensor<[320]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 3, 320, 320]> self = ?", "Tensor<[320, 1]> other = ?"],
        ["Tensor<[1, 3, 320, 320]> self = ?", "Tensor<[320]> other = ?"],
        ["Tensor<[1, 72, 1, 1]> self = ?", "Tensor<[1, 72, 40, 40]> other = ?"],
        ["Tensor<[1, 120, 1, 1]> self = ?", "Tensor<[1, 120, 40, 40]> other = ?"],
        ["Tensor<[1, 480, 1, 1]> self = ?", "Tensor<[1, 480, 20, 20]> other = ?"],
        ["Tensor<[1, 672, 1, 1]> self = ?", "Tensor<[1, 672, 20, 20]> other = ?"],
        ["Tensor<[1, 672, 1, 1]> self = ?", "Tensor<[1, 672, 10, 10]> other = ?"],
        ["Tensor<[1, 480, 1, 1]> self = ?", "Tensor<[1, 480, 10, 10]> other = ?"],
        ["Tensor<[3234, 2]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[3234, 2]> self = ?", "Tensor<[2]> other = ?"],
        ["Tensor<[3234]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[3234, 1]> self = ?", "Tensor<[3234, 1]> other = ?"],
        ["Tensor<[]> self = ?", "Tensor<[3234, 1]> other = ?"],
        ["Tensor<[300]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[1, 59]> self = ?", "Tensor<[1, 59]> other = ?"],
        ["Tensor<[1, 59, 1024]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[1, 60]> self = ?", "Tensor<[1, 60]> other = ?"],
        ["Tensor<[1, 1, 1024]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[1, s10 + 1]> self = ?", "Tensor<[1, s10 + 1]> other = ?"],
        ["Tensor<[1, 1, 1, 2048]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 1, 1, 10]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 10]> self = ?", "Tensor<[1, 10]> other = ?"],
        ["Tensor<[128]> self = ?", "Tensor other = 1.0"],
        ["Tensor<[1, 256, 128, 128]> self = ?", "Tensor<[128, 1]> other = ?"],
        ["Tensor<[1, 256, 128, 128]> self = ?", "Tensor<[128]> other = ?"],
        ["Tensor<[128]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[128]> self = ?", "Tensor other = 0.25"],
        ["Tensor<[128]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[1, 16384, 32]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[1, 4096, 64]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 160]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 256]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[1, 1, 1, 8]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[160]> self = ?", "Tensor other = -9.210340371976184"],
        ["Tensor<[1, 1]> self = ?", "Tensor<[1, 160]> other = ?"],
        ["Tensor<[1, 160]> self = ?", "Tensor other = 1"],
        ["Tensor<[1, 4096, 1280]> self = ?", "Tensor<[1, 4096, 1280]> other = ?"],
        ["Tensor<[1, s0*s1, 2560]> self = ?", "Tensor<[1, s0*s1, 2560]> other = ?"],
        ["Tensor<[1, s1*s2, 5120]> self = ?", "Tensor<[1, s1*s2, 5120]> other = ?"],
        ["Tensor<[1, s0*s1, 5120]> self = ?", "Tensor<[1, s0*s1, 5120]> other = ?"],
        ["Tensor<[16]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[2*s0]> self = ?", "Tensor<0.500000000000000> other = ?"],
        ["Tensor<[2*s1]> self = ?", "Tensor<0.500000000000000> other = ?"],
        ["Tensor<[1, s1*s2, 2560]> self = ?", "Tensor<[1, s1*s2, 2560]> other = ?"],
        ["Tensor<[2*s2]> self = ?", "Tensor<0.500000000000000> other = ?"],
        ["Tensor<[1, s1*s2, 1280]> self = ?", "Tensor<[1, s1*s2, 1280]> other = ?"],
        ["Tensor<[12]> self = ?", "Tensor other = 32.0"],
        ["Tensor<[16]> self = ?", "Tensor other = 32.0"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 50258"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 50259"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 50359"],
        ["Tensor<[1, 1]> self = ?", "Tensor other = 50363"],
        ["Tensor<[1, 19, 1024]> self = ?", "Tensor other = 32.0"],
        ["Tensor<[1, 19, 1024]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor other = 1.9761904761904763"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor other = 1.5625"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor other = -0.75"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor<[1, 1, 1, 42]> other = ?"],
        ["Tensor<[1, 1, 1, 42]> self = ?", "Tensor other = 1.25"],
        ["Tensor<[1, 192, 32, 42]> self = ?", "Tensor<[1, 1, 1, 42]> other = ?"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor other = -0.75"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor<[1, 1, 32, 1]> other = ?"],
        ["Tensor<[1, 1, 32, 1]> self = ?", "Tensor other = 1.25"],
        ["Tensor<[1, 192, 32, 42]> self = ?", "Tensor<[1, 1, 32, 1]> other = ?"],
        ["Tensor<[32]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[64]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 1, 1, 9]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 9, 3072]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 9, 3072]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 9, 3072]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 9, 3072]> self = ?", "Tensor<[1, 9, 3072]> other = ?"],
        ["Tensor<[1, 9, 128]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 9, 128]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 9, 128]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 9, 128]> self = ?", "Tensor<[1, 9, 128]> other = ?"],
        ["Tensor<[1, 1, 1, 12]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 12, 3072]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 12, 3072]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 12, 3072]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 12, 3072]> self = ?", "Tensor<[1, 12, 3072]> other = ?"],
        ["Tensor<[1, 9, 4096]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 9, 4096]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 9, 4096]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 9, 4096]> self = ?", "Tensor<[1, 9, 4096]> other = ?"],
        ["Tensor<[1, 9, 8192]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 9, 8192]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 9, 8192]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 9, 8192]> self = ?", "Tensor<[1, 9, 8192]> other = ?"],
        ["Tensor<[1, 9, 16384]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 9, 16384]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 9, 16384]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 9, 16384]> self = ?", "Tensor<[1, 9, 16384]> other = ?"],
        ["Tensor<[1, 1, 1, 5]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 5, 16, 32]> self = ?", "Tensor<[1, 5, 1, 32]> other = ?"],
        ["Tensor<[1, 5, 4096]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 5, 4096]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 5, 4096]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 5, 4096]> self = ?", "Tensor<[1, 5, 4096]> other = ?"],
        ["Tensor<[1, 1, 1, 6]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 1, 16, 32]> self = ?", "Tensor<[1, 1, 1, 32]> other = ?"],
        ["Tensor<[1, 1, 4096]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 1, 4096]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 1, 4096]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 1, 4096]> self = ?", "Tensor<[1, 1, 4096]> other = ?"],
        ["Tensor<[1, 1, 1, s10 + 1]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 256, 56, 56]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 28, 28]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 768, 14, 14]> self = ?", "Tensor<[1, 768, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 7, 7]> self = ?", "Tensor<[1, 1024, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 7, 7]> self = ?", "Tensor<[1, 1024, 7, 7]> other = ?"],
        ["Tensor<[1, 768, 14, 14]> self = ?", "Tensor<[1, 768, 14, 14]> other = ?"],
        ["Tensor<[1, 512, 28, 28]> self = ?", "Tensor<[1, 512, 28, 28]> other = ?"],
        ["Tensor<[1, 256, 56, 56]> self = ?", "Tensor<[1, 256, 56, 56]> other = ?"],
        ["Tensor<[1, 72, 28, 28]> self = ?", "Tensor<[1, 72, 1, 1]> other = ?"],
        ["Tensor<[1, 120, 28, 28]> self = ?", "Tensor<[1, 120, 1, 1]> other = ?"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "Tensor<[1, 480, 1, 1]> other = ?"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "Tensor<[1, 672, 1, 1]> other = ?"],
        ["Tensor<[1, 672, 7, 7]> self = ?", "Tensor<[1, 672, 1, 1]> other = ?"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "Tensor<[1, 960, 1, 1]> other = ?"],
        ["Tensor<[1, 960, 7, 7]> self = ?", "Tensor<[1, 960, 7, 7]> other = ?"],
        ["Tensor<[1, 672, 7, 7]> self = ?", "Tensor<[1, 672, 7, 7]> other = ?"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "Tensor<[1, 672, 14, 14]> other = ?"],
        ["Tensor<[1, 480, 14, 14]> self = ?", "Tensor<[1, 480, 14, 14]> other = ?"],
        ["Tensor<[1, 120, 28, 28]> self = ?", "Tensor<[1, 120, 28, 28]> other = ?"],
        ["Tensor<[1, 72, 28, 28]> self = ?", "Tensor<[1, 72, 28, 28]> other = ?"],
        ["Tensor<[56]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 72, 56, 56]> self = ?", "Tensor<[1, 72, 56, 56]> other = ?"],
        ["Tensor<[28]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 240, 28, 28]> self = ?", "Tensor<[1, 240, 28, 28]> other = ?"],
        ["Tensor<[14]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 200, 14, 14]> self = ?", "Tensor<[1, 200, 14, 14]> other = ?"],
        ["Tensor<[1, 184, 14, 14]> self = ?", "Tensor<[1, 184, 14, 14]> other = ?"],
        ["Tensor<[7]> self = ?", "Tensor other = 0.42857142857142855"],
        ["Tensor<[1, 1, 224, 224]> self = ?", "Tensor other = 0.458"],
        ["Tensor<[1, 1, 224, 224]> self = ?", "Tensor other = 0.448"],
        ["Tensor<[1, 1, 224, 224]> self = ?", "Tensor other = 0.45"],
        ["Tensor<[56]> self = ?", "Tensor other = 0.25"],
        ["Tensor<[56]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[28]> self = ?", "Tensor other = 0.25"],
        ["Tensor<[768]> self = ?", "Tensor<[1, 197, 768]> other = ?"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor<[768]> other = ?"],
        ["Tensor<[1, 197, 768]> self = ?", "Tensor<[1, 197, 768]> other = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[1, 197, 1024]> other = ?"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor<[1024]> other = ?"],
        ["Tensor<[1, 197, 1024]> self = ?", "Tensor<[1, 197, 1024]> other = ?"],
        ["Tensor<[1, 72, 1, 1]> self = ?", "Tensor<[1, 72, 28, 28]> other = ?"],
        ["Tensor<[1, 120, 1, 1]> self = ?", "Tensor<[1, 120, 28, 28]> other = ?"],
        ["Tensor<[1, 480, 1, 1]> self = ?", "Tensor<[1, 480, 14, 14]> other = ?"],
        ["Tensor<[1, 672, 1, 1]> self = ?", "Tensor<[1, 672, 14, 14]> other = ?"],
        ["Tensor<[1, 672, 1, 1]> self = ?", "Tensor<[1, 672, 7, 7]> other = ?"],
        ["Tensor<[1, 960, 1, 1]> self = ?", "Tensor<[1, 960, 7, 7]> other = ?"],
        ["Tensor<[1, 16, 1, 1]> self = ?", "Tensor<[1, 16, 56, 56]> other = ?"],
        ["Tensor<[1, 96, 1, 1]> self = ?", "Tensor<[1, 96, 14, 14]> other = ?"],
        ["Tensor<[1, 240, 1, 1]> self = ?", "Tensor<[1, 240, 14, 14]> other = ?"],
        ["Tensor<[1, 120, 1, 1]> self = ?", "Tensor<[1, 120, 14, 14]> other = ?"],
        ["Tensor<[1, 144, 1, 1]> self = ?", "Tensor<[1, 144, 14, 14]> other = ?"],
        ["Tensor<[1, 288, 1, 1]> self = ?", "Tensor<[1, 288, 7, 7]> other = ?"],
        ["Tensor<[1, 576, 1, 1]> self = ?", "Tensor<[1, 576, 7, 7]> other = ?"],
        ["Tensor<[1, 528, 1, 1]> self = ?", "Tensor<[1, 528, 96, 96]> other = ?"],
        ["Tensor<[1, 1056, 1, 1]> self = ?", "Tensor<[1, 1056, 48, 48]> other = ?"],
        ["Tensor<[1, 2904, 1, 1]> self = ?", "Tensor<[1, 2904, 24, 24]> other = ?"],
        ["Tensor<[1, 7392, 1, 1]> self = ?", "Tensor<[1, 7392, 12, 12]> other = ?"],
        ["Tensor<[1, 224, 1, 1]> self = ?", "Tensor<[1, 224, 56, 56]> other = ?"],
        ["Tensor<[1, 448, 1, 1]> self = ?", "Tensor<[1, 448, 28, 28]> other = ?"],
        ["Tensor<[1, 1232, 1, 1]> self = ?", "Tensor<[1, 1232, 14, 14]> other = ?"],
        ["Tensor<[1, 3024, 1, 1]> self = ?", "Tensor<[1, 3024, 7, 7]> other = ?"],
        ["Tensor<[1, 48, 1, 1]> self = ?", "Tensor<[1, 48, 56, 56]> other = ?"],
        ["Tensor<[1, 336, 1, 1]> self = ?", "Tensor<[1, 336, 14, 14]> other = ?"],
        ["Tensor<[1, 888, 1, 1]> self = ?", "Tensor<[1, 888, 7, 7]> other = ?"],
        ["Tensor<[1, 232, 1, 1]> self = ?", "Tensor<[1, 232, 56, 56]> other = ?"],
        ["Tensor<[1, 696, 1, 1]> self = ?", "Tensor<[1, 696, 28, 28]> other = ?"],
        ["Tensor<[1, 1392, 1, 1]> self = ?", "Tensor<[1, 1392, 14, 14]> other = ?"],
        ["Tensor<[1, 3712, 1, 1]> self = ?", "Tensor<[1, 3712, 7, 7]> other = ?"],
        ["Tensor<[1, 72, 1, 1]> self = ?", "Tensor<[1, 72, 56, 56]> other = ?"],
        ["Tensor<[1, 216, 1, 1]> self = ?", "Tensor<[1, 216, 28, 28]> other = ?"],
        ["Tensor<[1, 576, 1, 1]> self = ?", "Tensor<[1, 576, 14, 14]> other = ?"],
        ["Tensor<[1, 1512, 1, 1]> self = ?", "Tensor<[1, 1512, 7, 7]> other = ?"],
        ["Tensor<[1, 104, 1, 1]> self = ?", "Tensor<[1, 104, 28, 28]> other = ?"],
        ["Tensor<[1, 208, 1, 1]> self = ?", "Tensor<[1, 208, 14, 14]> other = ?"],
        ["Tensor<[1, 440, 1, 1]> self = ?", "Tensor<[1, 440, 7, 7]> other = ?"],
        ["Tensor<[1, 64, 1, 1]> self = ?", "Tensor<[1, 64, 56, 56]> other = ?"],
        ["Tensor<[1, 144, 1, 1]> self = ?", "Tensor<[1, 144, 28, 28]> other = ?"],
        ["Tensor<[1, 320, 1, 1]> self = ?", "Tensor<[1, 320, 14, 14]> other = ?"],
        ["Tensor<[1, 784, 1, 1]> self = ?", "Tensor<[1, 784, 7, 7]> other = ?"],
        ["Tensor<[1, 896, 1, 1]> self = ?", "Tensor<[1, 896, 14, 14]> other = ?"],
        ["Tensor<[1, 2016, 1, 1]> self = ?", "Tensor<[1, 2016, 7, 7]> other = ?"],
        ["Tensor<[800]> self = ?", "Tensor other = 0.6"],
        ["Tensor<[1066]> self = ?", "Tensor other = 0.600375234521576"],
        ["Tensor<[1, 3, 800, 1066]> self = ?", "Tensor<[800, 1]> other = ?"],
        ["Tensor<[1, 3, 800, 1066]> self = ?", "Tensor<[1066]> other = ?"],
        ["Tensor<[1, 64, 400, 544]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 64, 200, 272]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 200, 272]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 200, 272]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 100, 136]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 100, 136]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 100, 136]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 50, 68]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 50, 68]> self = ?", "Tensor<[1, 1024, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 50, 68]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 25, 34]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 2048, 25, 34]> self = ?", "Tensor<[1, 2048, 1, 1]> other = ?"],
        ["Tensor<[50]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[68]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[100]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[136]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[136]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[100]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[68]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[50]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[34]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[25]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[17]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[13]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[9]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[7]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[0]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[0, 1]> self = ?", "Tensor<[0, 1]> other = ?"],
        ["Tensor<[]> self = ?", "Tensor<[0, 1]> other = ?"],
        ["Tensor<[0]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[]> self = ?", "Tensor<[1, 24, 768]> other = ?"],
        ["Tensor<[1, 24, 768]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[300]> self = ?", "Tensor other = 1.6"],
        ["Tensor<[300]> self = ?", "Tensor other = 2.1333333333333333"],
        ["Tensor<[1, 3, 300, 300]> self = ?", "Tensor<[300, 1]> other = ?"],
        ["Tensor<[1, 3, 300, 300]> self = ?", "Tensor<[300]> other = ?"],
        ["Tensor<[1, 512, 1, 1]> self = ?", "Tensor<[1, 512, 38, 38]> other = ?"],
        ["Tensor<[8732, 2]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[8732, 2]> self = ?", "Tensor<[2]> other = ?"],
        ["Tensor<[8732]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[8732, 1]> self = ?", "Tensor<[8732, 1]> other = ?"],
        ["Tensor<[]> self = ?", "Tensor<[8732, 1]> other = ?"],
        ["Tensor<[12]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[320]> self = ?", "Tensor other = 1.5"],
        ["Tensor<[320]> self = ?", "Tensor other = 2.0"],
        ["Tensor<[64, 4, 49, 32]> self = ?", "Tensor other = 0.1767766952966369"],
        ["Tensor<[16, 8, 49, 32]> self = ?", "Tensor other = 0.1767766952966369"],
        ["Tensor<[4, 16, 49, 32]> self = ?", "Tensor other = 0.1767766952966369"],
        ["Tensor<[1, 32, 49, 32]> self = ?", "Tensor other = 0.1767766952966369"],
        ["Tensor<[64, 3, 49, 32]> self = ?", "Tensor other = 0.1767766952966369"],
        ["Tensor<[16, 6, 49, 32]> self = ?", "Tensor other = 0.1767766952966369"],
        ["Tensor<[4, 12, 49, 32]> self = ?", "Tensor other = 0.1767766952966369"],
        ["Tensor<[1, 24, 49, 32]> self = ?", "Tensor other = 0.1767766952966369"],
        ["Tensor<[1, 4, 64, 64]> self = ?", "Tensor other = 16"],
        ["Tensor<[64, 4, 64, 64]> self = ?", "Tensor<[4, 1, 1]> other = ?"],
        ["Tensor<[1, 8, 64, 64]> self = ?", "Tensor other = 16"],
        ["Tensor<[16, 8, 64, 64]> self = ?", "Tensor<[8, 1, 1]> other = ?"],
        ["Tensor<[1, 16, 64, 64]> self = ?", "Tensor other = 16"],
        ["Tensor<[4, 16, 64, 64]> self = ?", "Tensor<[16, 1, 1]> other = ?"],
        ["Tensor<[1, 32, 64, 64]> self = ?", "Tensor other = 16"],
        ["Tensor<[1, 32, 64, 64]> self = ?", "Tensor<[32, 1, 1]> other = ?"],
        ["Tensor<[1, 3, 64, 64]> self = ?", "Tensor other = 16"],
        ["Tensor<[64, 3, 64, 64]> self = ?", "Tensor<[3, 1, 1]> other = ?"],
        ["Tensor<[1, 6, 64, 64]> self = ?", "Tensor other = 16"],
        ["Tensor<[16, 6, 64, 64]> self = ?", "Tensor<[6, 1, 1]> other = ?"],
        ["Tensor<[1, 12, 64, 64]> self = ?", "Tensor other = 16"],
        ["Tensor<[4, 12, 64, 64]> self = ?", "Tensor<[12, 1, 1]> other = ?"],
        ["Tensor<[1, 24, 64, 64]> self = ?", "Tensor other = 16"],
        ["Tensor<[1, 24, 64, 64]> self = ?", "Tensor<[24, 1, 1]> other = ?"],
        ["Tensor<[1, 10, 768]> self = ?", "Tensor<[1, 10, 1]> other = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1, 10, 768]> other = ?"],
        ["Tensor<[10, 10]> self = ?", "Tensor other = 16"],
        ["Tensor<[10, 10]> self = ?", "Tensor other = 8"],
        ["Tensor<[1, 1, 768]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1, 1, 768]> other = ?"],
        ["Tensor<[1, 1, 768]> self = ?", "Tensor other = 0.03608439182435161"],
        ["Tensor<[1, 10, 1024]> self = ?", "Tensor<[1, 10, 1]> other = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[1, 10, 1024]> other = ?"],
        ["Tensor<[1, 1, 1024]> self = ?", "Tensor<[1, 1, 1]> other = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[1, 1, 1024]> other = ?"],
        ["Tensor<[1, 1, 1024]> self = ?", "Tensor other = 0.03125"],
        ["Tensor<[1, 10, 512]> self = ?", "Tensor<[1, 10, 1]> other = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[1, 10, 512]> other = ?"],
        ["Tensor<[1, 1, 512]> self = ?", "Tensor other = 0.04419417382415922"],
        ["Tensor<[1, 1, 1, 14]> self = ?", "Tensor other = -3.3895313892515355e+38"],
        ["Tensor<[1, 14, 3072]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[1, 14, 3072]> self = ?", "Tensor other = 0.044715"],
        ["Tensor<[1, 14, 3072]> self = ?", "Tensor other = 0.7978845608028654"],
        ["Tensor<[1, 14, 3072]> self = ?", "Tensor<[1, 14, 3072]> other = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.mul.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.mul.Tensor", input_strings)
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
