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
        return torch.ops.aten.addmm.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.addmm.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[128]> self = ?", "Tensor<[1, 784]> mat1 = ?", "Tensor<[784, 128]> mat2 = ?"],
        ["Tensor<[64]> self = ?", "Tensor<[1, 128]> mat1 = ?", "Tensor<[128, 64]> mat2 = ?"],
        ["Tensor<[12]> self = ?", "Tensor<[1, 64]> mat1 = ?", "Tensor<[64, 12]> mat2 = ?"],
        ["Tensor<[3]> self = ?", "Tensor<[1, 12]> mat1 = ?", "Tensor<[12, 3]> mat2 = ?"],
        ["Tensor<[12]> self = ?", "Tensor<[1, 3]> mat1 = ?", "Tensor<[3, 12]> mat2 = ?"],
        ["Tensor<[64]> self = ?", "Tensor<[1, 12]> mat1 = ?", "Tensor<[12, 64]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[1, 64]> mat1 = ?", "Tensor<[64, 128]> mat2 = ?"],
        ["Tensor<[784]> self = ?", "Tensor<[1, 128]> mat1 = ?", "Tensor<[128, 784]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[256, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[256, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[256, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[2]> self = ?", "Tensor<[256, 1024]> mat1 = ?", "Tensor<[1024, 2]> mat2 = ?"],
        ["Tensor<[4608]> self = ?", "Tensor<[32, 1536]> mat1 = ?", "Tensor<[1536, 4608]> mat2 = ?"],
        ["Tensor<[1536]> self = ?", "Tensor<[32, 1536]> mat1 = ?", "Tensor<[1536, 1536]> mat2 = ?"],
        ["Tensor<[6144]> self = ?", "Tensor<[32, 1536]> mat1 = ?", "Tensor<[1536, 6144]> mat2 = ?"],
        ["Tensor<[1536]> self = ?", "Tensor<[32, 6144]> mat1 = ?", "Tensor<[6144, 1536]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[50, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[50, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[50, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[14, 512]> mat1 = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[14, 512]> mat1 = ?", "Tensor<[512, 2048]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[14, 2048]> mat1 = ?", "Tensor<[2048, 512]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[920, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[920, 256]> mat1 = ?", "Tensor<[256, 2048]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[920, 2048]> mat1 = ?", "Tensor<[2048, 256]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[100, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[100, 256]> mat1 = ?", "Tensor<[256, 2048]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[100, 2048]> mat1 = ?", "Tensor<[2048, 256]> mat2 = ?"],
        ["Tensor<[92]> self = ?", "Tensor<[600, 256]> mat1 = ?", "Tensor<[256, 92]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[600, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[4]> self = ?", "Tensor<[600, 256]> mat1 = ?", "Tensor<[256, 4]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[25, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[25, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[25, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[2]> self = ?", "Tensor<[25, 768]> mat1 = ?", "Tensor<[768, 2]> mat2 = ?"],
        ["Tensor<[1]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 1]> mat2 = ?"],
        ["Tensor<[64]> self = ?", "Tensor<[19200, 64]> mat1 = ?", "Tensor<[64, 64]> mat2 = ?"],
        ["Tensor<[64]> self = ?", "Tensor<[300, 64]> mat1 = ?", "Tensor<[64, 64]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[19200, 64]> mat1 = ?", "Tensor<[64, 256]> mat2 = ?"],
        ["Tensor<[64]> self = ?", "Tensor<[19200, 256]> mat1 = ?", "Tensor<[256, 64]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[4800, 128]> mat1 = ?", "Tensor<[128, 128]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[300, 128]> mat1 = ?", "Tensor<[128, 128]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[4800, 128]> mat1 = ?", "Tensor<[128, 512]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[4800, 512]> mat1 = ?", "Tensor<[512, 128]> mat2 = ?"],
        ["Tensor<[320]> self = ?", "Tensor<[1200, 320]> mat1 = ?", "Tensor<[320, 320]> mat2 = ?"],
        ["Tensor<[320]> self = ?", "Tensor<[300, 320]> mat1 = ?", "Tensor<[320, 320]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[1200, 320]> mat1 = ?", "Tensor<[320, 1280]> mat2 = ?"],
        ["Tensor<[320]> self = ?", "Tensor<[1200, 1280]> mat1 = ?", "Tensor<[1280, 320]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[300, 512]> mat1 = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[300, 512]> mat1 = ?", "Tensor<[512, 2048]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[300, 2048]> mat1 = ?", "Tensor<[2048, 512]> mat2 = ?"],
        ["Tensor<[2304]> self = ?", "Tensor<[7, 768]> mat1 = ?", "Tensor<[768, 2304]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[7, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[7, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[7, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[45, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[45, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[45, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 1024]> mat1 = ?", "Tensor<[1024, 1000]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[256, 768]> mat1 = ?", "Tensor<[768, 512]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[256, 512]> mat1 = ?", "Tensor<[512, 256]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[256, 256]> mat1 = ?", "Tensor<[256, 512]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 512]> mat1 = ?", "Tensor<[512, 1000]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[1, 9216]> mat1 = ?", "Tensor<[9216, 128]> mat2 = ?"],
        ["Tensor<[10]> self = ?", "Tensor<[1, 128]> mat1 = ?", "Tensor<[128, 10]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 1280]> mat1 = ?", "Tensor<[1280, 1000]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[59, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[59, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[59, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[1, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[1, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[1, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[256, 1280]> mat1 = ?", "Tensor<[1280, 256]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[2048, 768]> mat1 = ?", "Tensor<[768, 256]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[2048, 768]> mat1 = ?", "Tensor<[768, 1280]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[256, 1280]> mat1 = ?", "Tensor<[1280, 1280]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[256, 1280]> mat1 = ?", "Tensor<[1280, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[2048, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 2048]> mat1 = ?", "Tensor<[2048, 1000]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[10, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[10, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[10, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[250002]> self = ?", "Tensor<[10, 768]> mat1 = ?", "Tensor<[768, 250002]> mat2 = ?"],
        ["Tensor<[32]> self = ?", "Tensor<[16384, 32]> mat1 = ?", "Tensor<[32, 32]> mat2 = ?"],
        ["Tensor<[32]> self = ?", "Tensor<[256, 32]> mat1 = ?", "Tensor<[32, 32]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[16384, 32]> mat1 = ?", "Tensor<[32, 128]> mat2 = ?"],
        ["Tensor<[32]> self = ?", "Tensor<[16384, 128]> mat1 = ?", "Tensor<[128, 32]> mat2 = ?"],
        ["Tensor<[64]> self = ?", "Tensor<[4096, 64]> mat1 = ?", "Tensor<[64, 64]> mat2 = ?"],
        ["Tensor<[64]> self = ?", "Tensor<[256, 64]> mat1 = ?", "Tensor<[64, 64]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[4096, 64]> mat1 = ?", "Tensor<[64, 256]> mat2 = ?"],
        ["Tensor<[64]> self = ?", "Tensor<[4096, 256]> mat1 = ?", "Tensor<[256, 64]> mat2 = ?"],
        ["Tensor<[160]> self = ?", "Tensor<[1024, 160]> mat1 = ?", "Tensor<[160, 160]> mat2 = ?"],
        ["Tensor<[160]> self = ?", "Tensor<[256, 160]> mat1 = ?", "Tensor<[160, 160]> mat2 = ?"],
        ["Tensor<[640]> self = ?", "Tensor<[1024, 160]> mat1 = ?", "Tensor<[160, 640]> mat2 = ?"],
        ["Tensor<[160]> self = ?", "Tensor<[1024, 640]> mat1 = ?", "Tensor<[640, 160]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[256, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[256, 256]> mat1 = ?", "Tensor<[256, 1024]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[256, 1024]> mat1 = ?", "Tensor<[1024, 256]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[1, 320]> mat1 = ?", "Tensor<[320, 1280]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[1, 1280]> mat1 = ?", "Tensor<[1280, 1280]> mat2 = ?"],
        ["Tensor<[320]> self = ?", "Tensor<[1, 1280]> mat1 = ?", "Tensor<[1280, 320]> mat2 = ?"],
        ["Tensor<[320]> self = ?", "Tensor<[4096, 320]> mat1 = ?", "Tensor<[320, 320]> mat2 = ?"],
        ["Tensor<[2560]> self = ?", "Tensor<[4096, 320]> mat1 = ?", "Tensor<[320, 2560]> mat2 = ?"],
        ["Tensor<[320]> self = ?", "Tensor<[4096, 1280]> mat1 = ?", "Tensor<[1280, 320]> mat2 = ?"],
        ["Tensor<[640]> self = ?", "Tensor<[1, 1280]> mat1 = ?", "Tensor<[1280, 640]> mat2 = ?"],
        ["Tensor<[640]> self = ?", "Tensor<[1024, 640]> mat1 = ?", "Tensor<[640, 640]> mat2 = ?"],
        ["Tensor<[5120]> self = ?", "Tensor<[1024, 640]> mat1 = ?", "Tensor<[640, 5120]> mat2 = ?"],
        ["Tensor<[640]> self = ?", "Tensor<[1024, 2560]> mat1 = ?", "Tensor<[2560, 640]> mat2 = ?"],
        ["Tensor<[10240]> self = ?", "Tensor<[256, 1280]> mat1 = ?", "Tensor<[1280, 10240]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[256, 5120]> mat1 = ?", "Tensor<[5120, 1280]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[64, 1280]> mat1 = ?", "Tensor<[1280, 1280]> mat2 = ?"],
        ["Tensor<[10240]> self = ?", "Tensor<[64, 1280]> mat1 = ?", "Tensor<[1280, 10240]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[64, 5120]> mat1 = ?", "Tensor<[5120, 1280]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[201, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[201, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[201, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[1536]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 1536]> mat2 = ?"],
        ["Tensor<[3129]> self = ?", "Tensor<[1, 1536]> mat1 = ?", "Tensor<[1536, 3129]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1500, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[1500, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1500, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[4, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[4, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[4, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[19, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[19, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[19, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[192]> self = ?", "Tensor<[1445, 192]> mat1 = ?", "Tensor<[192, 192]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1445, 192]> mat1 = ?", "Tensor<[192, 768]> mat2 = ?"],
        ["Tensor<[192]> self = ?", "Tensor<[1445, 768]> mat1 = ?", "Tensor<[768, 192]> mat2 = ?"],
        ["Tensor<[192]> self = ?", "Tensor<[100, 192]> mat1 = ?", "Tensor<[192, 192]> mat2 = ?"],
        ["Tensor<[92]> self = ?", "Tensor<[100, 192]> mat1 = ?", "Tensor<[192, 92]> mat2 = ?"],
        ["Tensor<[4]> self = ?", "Tensor<[100, 192]> mat1 = ?", "Tensor<[192, 4]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[9, 128]> mat1 = ?", "Tensor<[128, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[9, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[9, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[9, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[9, 768]> mat1 = ?", "Tensor<[768, 128]> mat2 = ?"],
        ["Tensor<[30000]> self = ?", "Tensor<[9, 128]> mat1 = ?", "Tensor<[128, 30000]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[12, 128]> mat1 = ?", "Tensor<[128, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[12, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[12, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[12, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[2]> self = ?", "Tensor<[12, 768]> mat1 = ?", "Tensor<[768, 2]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[9, 128]> mat1 = ?", "Tensor<[128, 1024]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[9, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[9, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[9, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[9, 1024]> mat1 = ?", "Tensor<[1024, 128]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[9, 128]> mat1 = ?", "Tensor<[128, 2048]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[9, 2048]> mat1 = ?", "Tensor<[2048, 2048]> mat2 = ?"],
        ["Tensor<[8192]> self = ?", "Tensor<[9, 2048]> mat1 = ?", "Tensor<[2048, 8192]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[9, 8192]> mat1 = ?", "Tensor<[8192, 2048]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[9, 2048]> mat1 = ?", "Tensor<[2048, 128]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[9, 128]> mat1 = ?", "Tensor<[128, 4096]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[9, 4096]> mat1 = ?", "Tensor<[4096, 4096]> mat2 = ?"],
        ["Tensor<[16384]> self = ?", "Tensor<[9, 4096]> mat1 = ?", "Tensor<[4096, 16384]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[9, 16384]> mat1 = ?", "Tensor<[16384, 4096]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[9, 4096]> mat1 = ?", "Tensor<[4096, 128]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[5, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[5, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[51200]> self = ?", "Tensor<[5, 1024]> mat1 = ?", "Tensor<[1024, 51200]> mat2 = ?"],
        ["Tensor<[51200]> self = ?", "Tensor<[1, 1024]> mat1 = ?", "Tensor<[1024, 51200]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 2208]> mat1 = ?", "Tensor<[2208, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 1664]> mat1 = ?", "Tensor<[1664, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 1920]> mat1 = ?", "Tensor<[1920, 1000]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[16, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[16, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[16, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[197, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[197, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[197, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 1536]> mat1 = ?", "Tensor<[1536, 1000]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[197, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[197, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[197, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[196]> self = ?", "Tensor<[768, 384]> mat1 = ?", "Tensor<[384, 196]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[196, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[196, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[21843]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 21843]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[1, 960]> mat1 = ?", "Tensor<[960, 1280]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[1, 576]> mat1 = ?", "Tensor<[576, 1024]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 912]> mat1 = ?", "Tensor<[912, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 2520]> mat1 = ?", "Tensor<[2520, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 1008]> mat1 = ?", "Tensor<[1008, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 400]> mat1 = ?", "Tensor<[400, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 672]> mat1 = ?", "Tensor<[672, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 7392]> mat1 = ?", "Tensor<[7392, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 3024]> mat1 = ?", "Tensor<[3024, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 888]> mat1 = ?", "Tensor<[888, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 3712]> mat1 = ?", "Tensor<[3712, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 1512]> mat1 = ?", "Tensor<[1512, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 440]> mat1 = ?", "Tensor<[440, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 784]> mat1 = ?", "Tensor<[784, 1000]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 2016]> mat1 = ?", "Tensor<[2016, 1000]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[24, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[24, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[24, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[1, 80]> mat1 = ?", "Tensor<[80, 256]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[1, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1, 256]> mat1 = ?", "Tensor<[256, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1, 1280]> mat1 = ?", "Tensor<[1280, 768]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[s0, 80]> mat1 = ?", "Tensor<[80, 256]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[s0, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[s0, 256]> mat1 = ?", "Tensor<[256, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[s0, 1280]> mat1 = ?", "Tensor<[1280, 768]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[3136, 128]> mat1 = ?", "Tensor<[128, 384]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[3136, 128]> mat1 = ?", "Tensor<[128, 128]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[3136, 128]> mat1 = ?", "Tensor<[128, 512]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[3136, 512]> mat1 = ?", "Tensor<[512, 128]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[784, 256]> mat1 = ?", "Tensor<[256, 768]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[784, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[784, 256]> mat1 = ?", "Tensor<[256, 1024]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[784, 1024]> mat1 = ?", "Tensor<[1024, 256]> mat2 = ?"],
        ["Tensor<[1536]> self = ?", "Tensor<[196, 512]> mat1 = ?", "Tensor<[512, 1536]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[196, 512]> mat1 = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[196, 512]> mat1 = ?", "Tensor<[512, 2048]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[196, 2048]> mat1 = ?", "Tensor<[2048, 512]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[49, 1024]> mat1 = ?", "Tensor<[1024, 3072]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[49, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[49, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[49, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[288]> self = ?", "Tensor<[3136, 96]> mat1 = ?", "Tensor<[96, 288]> mat2 = ?"],
        ["Tensor<[96]> self = ?", "Tensor<[3136, 96]> mat1 = ?", "Tensor<[96, 96]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[3136, 96]> mat1 = ?", "Tensor<[96, 384]> mat2 = ?"],
        ["Tensor<[96]> self = ?", "Tensor<[3136, 384]> mat1 = ?", "Tensor<[384, 96]> mat2 = ?"],
        ["Tensor<[576]> self = ?", "Tensor<[784, 192]> mat1 = ?", "Tensor<[192, 576]> mat2 = ?"],
        ["Tensor<[192]> self = ?", "Tensor<[784, 192]> mat1 = ?", "Tensor<[192, 192]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[784, 192]> mat1 = ?", "Tensor<[192, 768]> mat2 = ?"],
        ["Tensor<[192]> self = ?", "Tensor<[784, 768]> mat1 = ?", "Tensor<[768, 192]> mat2 = ?"],
        ["Tensor<[1152]> self = ?", "Tensor<[196, 384]> mat1 = ?", "Tensor<[384, 1152]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[196, 384]> mat1 = ?", "Tensor<[384, 384]> mat2 = ?"],
        ["Tensor<[1536]> self = ?", "Tensor<[196, 384]> mat1 = ?", "Tensor<[384, 1536]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[196, 1536]> mat1 = ?", "Tensor<[1536, 384]> mat2 = ?"],
        ["Tensor<[2304]> self = ?", "Tensor<[49, 768]> mat1 = ?", "Tensor<[768, 2304]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[49, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[49, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[49, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[225, 2]> mat1 = ?", "Tensor<[2, 512]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[4096, 128]> mat1 = ?", "Tensor<[128, 384]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[4096, 128]> mat1 = ?", "Tensor<[128, 128]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[4096, 128]> mat1 = ?", "Tensor<[128, 512]> mat2 = ?"],
        ["Tensor<[128]> self = ?", "Tensor<[4096, 512]> mat1 = ?", "Tensor<[512, 128]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1024, 256]> mat1 = ?", "Tensor<[256, 768]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[1024, 256]> mat1 = ?", "Tensor<[256, 256]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[1024, 256]> mat1 = ?", "Tensor<[256, 1024]> mat2 = ?"],
        ["Tensor<[256]> self = ?", "Tensor<[1024, 1024]> mat1 = ?", "Tensor<[1024, 256]> mat2 = ?"],
        ["Tensor<[1536]> self = ?", "Tensor<[256, 512]> mat1 = ?", "Tensor<[512, 1536]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[256, 512]> mat1 = ?", "Tensor<[512, 512]> mat2 = ?"],
        ["Tensor<[2048]> self = ?", "Tensor<[256, 512]> mat1 = ?", "Tensor<[512, 2048]> mat2 = ?"],
        ["Tensor<[512]> self = ?", "Tensor<[256, 2048]> mat1 = ?", "Tensor<[2048, 512]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[64, 1024]> mat1 = ?", "Tensor<[1024, 3072]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[64, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[64, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[64, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
        ["Tensor<[288]> self = ?", "Tensor<[4096, 96]> mat1 = ?", "Tensor<[96, 288]> mat2 = ?"],
        ["Tensor<[96]> self = ?", "Tensor<[4096, 96]> mat1 = ?", "Tensor<[96, 96]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[4096, 96]> mat1 = ?", "Tensor<[96, 384]> mat2 = ?"],
        ["Tensor<[96]> self = ?", "Tensor<[4096, 384]> mat1 = ?", "Tensor<[384, 96]> mat2 = ?"],
        ["Tensor<[576]> self = ?", "Tensor<[1024, 192]> mat1 = ?", "Tensor<[192, 576]> mat2 = ?"],
        ["Tensor<[192]> self = ?", "Tensor<[1024, 192]> mat1 = ?", "Tensor<[192, 192]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[1024, 192]> mat1 = ?", "Tensor<[192, 768]> mat2 = ?"],
        ["Tensor<[192]> self = ?", "Tensor<[1024, 768]> mat1 = ?", "Tensor<[768, 192]> mat2 = ?"],
        ["Tensor<[1152]> self = ?", "Tensor<[256, 384]> mat1 = ?", "Tensor<[384, 1152]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[256, 384]> mat1 = ?", "Tensor<[384, 384]> mat2 = ?"],
        ["Tensor<[1536]> self = ?", "Tensor<[256, 384]> mat1 = ?", "Tensor<[384, 1536]> mat2 = ?"],
        ["Tensor<[384]> self = ?", "Tensor<[256, 1536]> mat1 = ?", "Tensor<[1536, 384]> mat2 = ?"],
        ["Tensor<[2304]> self = ?", "Tensor<[64, 768]> mat1 = ?", "Tensor<[768, 2304]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[64, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[64, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[64, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[2]> self = ?", "Tensor<[1, 768]> mat1 = ?", "Tensor<[768, 2]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[14, 128]> mat1 = ?", "Tensor<[128, 768]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[14, 768]> mat1 = ?", "Tensor<[768, 768]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[14, 768]> mat1 = ?", "Tensor<[768, 3072]> mat2 = ?"],
        ["Tensor<[768]> self = ?", "Tensor<[14, 3072]> mat1 = ?", "Tensor<[3072, 768]> mat2 = ?"],
        ["Tensor<[2]> self = ?", "Tensor<[14, 768]> mat1 = ?", "Tensor<[768, 2]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[1, 25088]> mat1 = ?", "Tensor<[25088, 4096]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[1, 4096]> mat1 = ?", "Tensor<[4096, 4096]> mat2 = ?"],
        ["Tensor<[1000]> self = ?", "Tensor<[1, 4096]> mat1 = ?", "Tensor<[4096, 1000]> mat2 = ?"],
        ["Tensor<[2304]> self = ?", "Tensor<[197, 768]> mat1 = ?", "Tensor<[768, 2304]> mat2 = ?"],
        ["Tensor<[2304]> self = ?", "Tensor<[50, 768]> mat1 = ?", "Tensor<[768, 2304]> mat2 = ?"],
        ["Tensor<[3840]> self = ?", "Tensor<[1370, 1280]> mat1 = ?", "Tensor<[1280, 3840]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[1370, 1280]> mat1 = ?", "Tensor<[1280, 1280]> mat2 = ?"],
        ["Tensor<[5120]> self = ?", "Tensor<[1370, 1280]> mat1 = ?", "Tensor<[1280, 5120]> mat2 = ?"],
        ["Tensor<[1280]> self = ?", "Tensor<[1370, 5120]> mat1 = ?", "Tensor<[5120, 1280]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[197, 1024]> mat1 = ?", "Tensor<[1024, 3072]> mat2 = ?"],
        ["Tensor<[3072]> self = ?", "Tensor<[50, 1024]> mat1 = ?", "Tensor<[1024, 3072]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[50, 1024]> mat1 = ?", "Tensor<[1024, 1024]> mat2 = ?"],
        ["Tensor<[4096]> self = ?", "Tensor<[50, 1024]> mat1 = ?", "Tensor<[1024, 4096]> mat2 = ?"],
        ["Tensor<[1024]> self = ?", "Tensor<[50, 4096]> mat1 = ?", "Tensor<[4096, 1024]> mat2 = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.addmm.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.addmm.default", input_strings
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
