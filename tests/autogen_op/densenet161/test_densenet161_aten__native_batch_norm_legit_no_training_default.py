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
    save_pickle(metrics, "metrics-autogen-op/densenet161", "aten._native_batch_norm_legit_no_training.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 96, 112, 112]> input = ?",
            "Optional[Tensor]<[96]> weight = ?",
            "Optional[Tensor]<[96]> bias = ?",
            "Tensor<[96]> running_mean = ?",
            "Tensor<[96]> running_var = ?",
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
            "Tensor<[1, 192, 56, 56]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "Tensor<[192]> running_mean = ?",
            "Tensor<[192]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 144, 56, 56]> input = ?",
            "Optional[Tensor]<[144]> weight = ?",
            "Optional[Tensor]<[144]> bias = ?",
            "Tensor<[144]> running_mean = ?",
            "Tensor<[144]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 240, 56, 56]> input = ?",
            "Optional[Tensor]<[240]> weight = ?",
            "Optional[Tensor]<[240]> bias = ?",
            "Tensor<[240]> running_mean = ?",
            "Tensor<[240]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 288, 56, 56]> input = ?",
            "Optional[Tensor]<[288]> weight = ?",
            "Optional[Tensor]<[288]> bias = ?",
            "Tensor<[288]> running_mean = ?",
            "Tensor<[288]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 336, 56, 56]> input = ?",
            "Optional[Tensor]<[336]> weight = ?",
            "Optional[Tensor]<[336]> bias = ?",
            "Tensor<[336]> running_mean = ?",
            "Tensor<[336]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 384, 56, 56]> input = ?",
            "Optional[Tensor]<[384]> weight = ?",
            "Optional[Tensor]<[384]> bias = ?",
            "Tensor<[384]> running_mean = ?",
            "Tensor<[384]> running_var = ?",
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
            "Tensor<[1, 240, 28, 28]> input = ?",
            "Optional[Tensor]<[240]> weight = ?",
            "Optional[Tensor]<[240]> bias = ?",
            "Tensor<[240]> running_mean = ?",
            "Tensor<[240]> running_var = ?",
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
            "Tensor<[1, 336, 28, 28]> input = ?",
            "Optional[Tensor]<[336]> weight = ?",
            "Optional[Tensor]<[336]> bias = ?",
            "Tensor<[336]> running_mean = ?",
            "Tensor<[336]> running_var = ?",
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
            "Tensor<[1, 432, 28, 28]> input = ?",
            "Optional[Tensor]<[432]> weight = ?",
            "Optional[Tensor]<[432]> bias = ?",
            "Tensor<[432]> running_mean = ?",
            "Tensor<[432]> running_var = ?",
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
            "Tensor<[1, 528, 28, 28]> input = ?",
            "Optional[Tensor]<[528]> weight = ?",
            "Optional[Tensor]<[528]> bias = ?",
            "Tensor<[528]> running_mean = ?",
            "Tensor<[528]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 576, 28, 28]> input = ?",
            "Optional[Tensor]<[576]> weight = ?",
            "Optional[Tensor]<[576]> bias = ?",
            "Tensor<[576]> running_mean = ?",
            "Tensor<[576]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 624, 28, 28]> input = ?",
            "Optional[Tensor]<[624]> weight = ?",
            "Optional[Tensor]<[624]> bias = ?",
            "Tensor<[624]> running_mean = ?",
            "Tensor<[624]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 672, 28, 28]> input = ?",
            "Optional[Tensor]<[672]> weight = ?",
            "Optional[Tensor]<[672]> bias = ?",
            "Tensor<[672]> running_mean = ?",
            "Tensor<[672]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 720, 28, 28]> input = ?",
            "Optional[Tensor]<[720]> weight = ?",
            "Optional[Tensor]<[720]> bias = ?",
            "Tensor<[720]> running_mean = ?",
            "Tensor<[720]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 768, 28, 28]> input = ?",
            "Optional[Tensor]<[768]> weight = ?",
            "Optional[Tensor]<[768]> bias = ?",
            "Tensor<[768]> running_mean = ?",
            "Tensor<[768]> running_var = ?",
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
            "Tensor<[1, 192, 14, 14]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "Tensor<[192]> running_mean = ?",
            "Tensor<[192]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 432, 14, 14]> input = ?",
            "Optional[Tensor]<[432]> weight = ?",
            "Optional[Tensor]<[432]> bias = ?",
            "Tensor<[432]> running_mean = ?",
            "Tensor<[432]> running_var = ?",
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
            "Tensor<[1, 528, 14, 14]> input = ?",
            "Optional[Tensor]<[528]> weight = ?",
            "Optional[Tensor]<[528]> bias = ?",
            "Tensor<[528]> running_mean = ?",
            "Tensor<[528]> running_var = ?",
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
            "Tensor<[1, 624, 14, 14]> input = ?",
            "Optional[Tensor]<[624]> weight = ?",
            "Optional[Tensor]<[624]> bias = ?",
            "Tensor<[624]> running_mean = ?",
            "Tensor<[624]> running_var = ?",
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
            "Tensor<[1, 720, 14, 14]> input = ?",
            "Optional[Tensor]<[720]> weight = ?",
            "Optional[Tensor]<[720]> bias = ?",
            "Tensor<[720]> running_mean = ?",
            "Tensor<[720]> running_var = ?",
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
            "Tensor<[1, 816, 14, 14]> input = ?",
            "Optional[Tensor]<[816]> weight = ?",
            "Optional[Tensor]<[816]> bias = ?",
            "Tensor<[816]> running_mean = ?",
            "Tensor<[816]> running_var = ?",
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
            "Tensor<[1, 912, 14, 14]> input = ?",
            "Optional[Tensor]<[912]> weight = ?",
            "Optional[Tensor]<[912]> bias = ?",
            "Tensor<[912]> running_mean = ?",
            "Tensor<[912]> running_var = ?",
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
            "Tensor<[1, 1008, 14, 14]> input = ?",
            "Optional[Tensor]<[1008]> weight = ?",
            "Optional[Tensor]<[1008]> bias = ?",
            "Tensor<[1008]> running_mean = ?",
            "Tensor<[1008]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1056, 14, 14]> input = ?",
            "Optional[Tensor]<[1056]> weight = ?",
            "Optional[Tensor]<[1056]> bias = ?",
            "Tensor<[1056]> running_mean = ?",
            "Tensor<[1056]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1104, 14, 14]> input = ?",
            "Optional[Tensor]<[1104]> weight = ?",
            "Optional[Tensor]<[1104]> bias = ?",
            "Tensor<[1104]> running_mean = ?",
            "Tensor<[1104]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1152, 14, 14]> input = ?",
            "Optional[Tensor]<[1152]> weight = ?",
            "Optional[Tensor]<[1152]> bias = ?",
            "Tensor<[1152]> running_mean = ?",
            "Tensor<[1152]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1200, 14, 14]> input = ?",
            "Optional[Tensor]<[1200]> weight = ?",
            "Optional[Tensor]<[1200]> bias = ?",
            "Tensor<[1200]> running_mean = ?",
            "Tensor<[1200]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1248, 14, 14]> input = ?",
            "Optional[Tensor]<[1248]> weight = ?",
            "Optional[Tensor]<[1248]> bias = ?",
            "Tensor<[1248]> running_mean = ?",
            "Tensor<[1248]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1296, 14, 14]> input = ?",
            "Optional[Tensor]<[1296]> weight = ?",
            "Optional[Tensor]<[1296]> bias = ?",
            "Tensor<[1296]> running_mean = ?",
            "Tensor<[1296]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1344, 14, 14]> input = ?",
            "Optional[Tensor]<[1344]> weight = ?",
            "Optional[Tensor]<[1344]> bias = ?",
            "Tensor<[1344]> running_mean = ?",
            "Tensor<[1344]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1392, 14, 14]> input = ?",
            "Optional[Tensor]<[1392]> weight = ?",
            "Optional[Tensor]<[1392]> bias = ?",
            "Tensor<[1392]> running_mean = ?",
            "Tensor<[1392]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1440, 14, 14]> input = ?",
            "Optional[Tensor]<[1440]> weight = ?",
            "Optional[Tensor]<[1440]> bias = ?",
            "Tensor<[1440]> running_mean = ?",
            "Tensor<[1440]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1488, 14, 14]> input = ?",
            "Optional[Tensor]<[1488]> weight = ?",
            "Optional[Tensor]<[1488]> bias = ?",
            "Tensor<[1488]> running_mean = ?",
            "Tensor<[1488]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1536, 14, 14]> input = ?",
            "Optional[Tensor]<[1536]> weight = ?",
            "Optional[Tensor]<[1536]> bias = ?",
            "Tensor<[1536]> running_mean = ?",
            "Tensor<[1536]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1584, 14, 14]> input = ?",
            "Optional[Tensor]<[1584]> weight = ?",
            "Optional[Tensor]<[1584]> bias = ?",
            "Tensor<[1584]> running_mean = ?",
            "Tensor<[1584]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1632, 14, 14]> input = ?",
            "Optional[Tensor]<[1632]> weight = ?",
            "Optional[Tensor]<[1632]> bias = ?",
            "Tensor<[1632]> running_mean = ?",
            "Tensor<[1632]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1680, 14, 14]> input = ?",
            "Optional[Tensor]<[1680]> weight = ?",
            "Optional[Tensor]<[1680]> bias = ?",
            "Tensor<[1680]> running_mean = ?",
            "Tensor<[1680]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1728, 14, 14]> input = ?",
            "Optional[Tensor]<[1728]> weight = ?",
            "Optional[Tensor]<[1728]> bias = ?",
            "Tensor<[1728]> running_mean = ?",
            "Tensor<[1728]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1776, 14, 14]> input = ?",
            "Optional[Tensor]<[1776]> weight = ?",
            "Optional[Tensor]<[1776]> bias = ?",
            "Tensor<[1776]> running_mean = ?",
            "Tensor<[1776]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1824, 14, 14]> input = ?",
            "Optional[Tensor]<[1824]> weight = ?",
            "Optional[Tensor]<[1824]> bias = ?",
            "Tensor<[1824]> running_mean = ?",
            "Tensor<[1824]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1872, 14, 14]> input = ?",
            "Optional[Tensor]<[1872]> weight = ?",
            "Optional[Tensor]<[1872]> bias = ?",
            "Tensor<[1872]> running_mean = ?",
            "Tensor<[1872]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1920, 14, 14]> input = ?",
            "Optional[Tensor]<[1920]> weight = ?",
            "Optional[Tensor]<[1920]> bias = ?",
            "Tensor<[1920]> running_mean = ?",
            "Tensor<[1920]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1968, 14, 14]> input = ?",
            "Optional[Tensor]<[1968]> weight = ?",
            "Optional[Tensor]<[1968]> bias = ?",
            "Tensor<[1968]> running_mean = ?",
            "Tensor<[1968]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2016, 14, 14]> input = ?",
            "Optional[Tensor]<[2016]> weight = ?",
            "Optional[Tensor]<[2016]> bias = ?",
            "Tensor<[2016]> running_mean = ?",
            "Tensor<[2016]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2064, 14, 14]> input = ?",
            "Optional[Tensor]<[2064]> weight = ?",
            "Optional[Tensor]<[2064]> bias = ?",
            "Tensor<[2064]> running_mean = ?",
            "Tensor<[2064]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2112, 14, 14]> input = ?",
            "Optional[Tensor]<[2112]> weight = ?",
            "Optional[Tensor]<[2112]> bias = ?",
            "Tensor<[2112]> running_mean = ?",
            "Tensor<[2112]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1056, 7, 7]> input = ?",
            "Optional[Tensor]<[1056]> weight = ?",
            "Optional[Tensor]<[1056]> bias = ?",
            "Tensor<[1056]> running_mean = ?",
            "Tensor<[1056]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 192, 7, 7]> input = ?",
            "Optional[Tensor]<[192]> weight = ?",
            "Optional[Tensor]<[192]> bias = ?",
            "Tensor<[192]> running_mean = ?",
            "Tensor<[192]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1104, 7, 7]> input = ?",
            "Optional[Tensor]<[1104]> weight = ?",
            "Optional[Tensor]<[1104]> bias = ?",
            "Tensor<[1104]> running_mean = ?",
            "Tensor<[1104]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1152, 7, 7]> input = ?",
            "Optional[Tensor]<[1152]> weight = ?",
            "Optional[Tensor]<[1152]> bias = ?",
            "Tensor<[1152]> running_mean = ?",
            "Tensor<[1152]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1200, 7, 7]> input = ?",
            "Optional[Tensor]<[1200]> weight = ?",
            "Optional[Tensor]<[1200]> bias = ?",
            "Tensor<[1200]> running_mean = ?",
            "Tensor<[1200]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1248, 7, 7]> input = ?",
            "Optional[Tensor]<[1248]> weight = ?",
            "Optional[Tensor]<[1248]> bias = ?",
            "Tensor<[1248]> running_mean = ?",
            "Tensor<[1248]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1296, 7, 7]> input = ?",
            "Optional[Tensor]<[1296]> weight = ?",
            "Optional[Tensor]<[1296]> bias = ?",
            "Tensor<[1296]> running_mean = ?",
            "Tensor<[1296]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1344, 7, 7]> input = ?",
            "Optional[Tensor]<[1344]> weight = ?",
            "Optional[Tensor]<[1344]> bias = ?",
            "Tensor<[1344]> running_mean = ?",
            "Tensor<[1344]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1392, 7, 7]> input = ?",
            "Optional[Tensor]<[1392]> weight = ?",
            "Optional[Tensor]<[1392]> bias = ?",
            "Tensor<[1392]> running_mean = ?",
            "Tensor<[1392]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1440, 7, 7]> input = ?",
            "Optional[Tensor]<[1440]> weight = ?",
            "Optional[Tensor]<[1440]> bias = ?",
            "Tensor<[1440]> running_mean = ?",
            "Tensor<[1440]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1488, 7, 7]> input = ?",
            "Optional[Tensor]<[1488]> weight = ?",
            "Optional[Tensor]<[1488]> bias = ?",
            "Tensor<[1488]> running_mean = ?",
            "Tensor<[1488]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1536, 7, 7]> input = ?",
            "Optional[Tensor]<[1536]> weight = ?",
            "Optional[Tensor]<[1536]> bias = ?",
            "Tensor<[1536]> running_mean = ?",
            "Tensor<[1536]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1584, 7, 7]> input = ?",
            "Optional[Tensor]<[1584]> weight = ?",
            "Optional[Tensor]<[1584]> bias = ?",
            "Tensor<[1584]> running_mean = ?",
            "Tensor<[1584]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1632, 7, 7]> input = ?",
            "Optional[Tensor]<[1632]> weight = ?",
            "Optional[Tensor]<[1632]> bias = ?",
            "Tensor<[1632]> running_mean = ?",
            "Tensor<[1632]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1680, 7, 7]> input = ?",
            "Optional[Tensor]<[1680]> weight = ?",
            "Optional[Tensor]<[1680]> bias = ?",
            "Tensor<[1680]> running_mean = ?",
            "Tensor<[1680]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1728, 7, 7]> input = ?",
            "Optional[Tensor]<[1728]> weight = ?",
            "Optional[Tensor]<[1728]> bias = ?",
            "Tensor<[1728]> running_mean = ?",
            "Tensor<[1728]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1776, 7, 7]> input = ?",
            "Optional[Tensor]<[1776]> weight = ?",
            "Optional[Tensor]<[1776]> bias = ?",
            "Tensor<[1776]> running_mean = ?",
            "Tensor<[1776]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1824, 7, 7]> input = ?",
            "Optional[Tensor]<[1824]> weight = ?",
            "Optional[Tensor]<[1824]> bias = ?",
            "Tensor<[1824]> running_mean = ?",
            "Tensor<[1824]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1872, 7, 7]> input = ?",
            "Optional[Tensor]<[1872]> weight = ?",
            "Optional[Tensor]<[1872]> bias = ?",
            "Tensor<[1872]> running_mean = ?",
            "Tensor<[1872]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1920, 7, 7]> input = ?",
            "Optional[Tensor]<[1920]> weight = ?",
            "Optional[Tensor]<[1920]> bias = ?",
            "Tensor<[1920]> running_mean = ?",
            "Tensor<[1920]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1968, 7, 7]> input = ?",
            "Optional[Tensor]<[1968]> weight = ?",
            "Optional[Tensor]<[1968]> bias = ?",
            "Tensor<[1968]> running_mean = ?",
            "Tensor<[1968]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2016, 7, 7]> input = ?",
            "Optional[Tensor]<[2016]> weight = ?",
            "Optional[Tensor]<[2016]> bias = ?",
            "Tensor<[2016]> running_mean = ?",
            "Tensor<[2016]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2064, 7, 7]> input = ?",
            "Optional[Tensor]<[2064]> weight = ?",
            "Optional[Tensor]<[2064]> bias = ?",
            "Tensor<[2064]> running_mean = ?",
            "Tensor<[2064]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2112, 7, 7]> input = ?",
            "Optional[Tensor]<[2112]> weight = ?",
            "Optional[Tensor]<[2112]> bias = ?",
            "Tensor<[2112]> running_mean = ?",
            "Tensor<[2112]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2160, 7, 7]> input = ?",
            "Optional[Tensor]<[2160]> weight = ?",
            "Optional[Tensor]<[2160]> bias = ?",
            "Tensor<[2160]> running_mean = ?",
            "Tensor<[2160]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 2208, 7, 7]> input = ?",
            "Optional[Tensor]<[2208]> weight = ?",
            "Optional[Tensor]<[2208]> bias = ?",
            "Tensor<[2208]> running_mean = ?",
            "Tensor<[2208]> running_var = ?",
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
