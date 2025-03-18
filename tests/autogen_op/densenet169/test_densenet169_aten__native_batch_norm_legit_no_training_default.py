# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
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
    save_pickle(metrics, "metrics-autogen-op/densenet169", "aten._native_batch_norm_legit_no_training.default")


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
            "Tensor<[1, 1056, 14, 14]> input = ?",
            "Optional[Tensor]<[1056]> weight = ?",
            "Optional[Tensor]<[1056]> bias = ?",
            "Tensor<[1056]> running_mean = ?",
            "Tensor<[1056]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1088, 14, 14]> input = ?",
            "Optional[Tensor]<[1088]> weight = ?",
            "Optional[Tensor]<[1088]> bias = ?",
            "Tensor<[1088]> running_mean = ?",
            "Tensor<[1088]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1120, 14, 14]> input = ?",
            "Optional[Tensor]<[1120]> weight = ?",
            "Optional[Tensor]<[1120]> bias = ?",
            "Tensor<[1120]> running_mean = ?",
            "Tensor<[1120]> running_var = ?",
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
            "Tensor<[1, 1184, 14, 14]> input = ?",
            "Optional[Tensor]<[1184]> weight = ?",
            "Optional[Tensor]<[1184]> bias = ?",
            "Tensor<[1184]> running_mean = ?",
            "Tensor<[1184]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1216, 14, 14]> input = ?",
            "Optional[Tensor]<[1216]> weight = ?",
            "Optional[Tensor]<[1216]> bias = ?",
            "Tensor<[1216]> running_mean = ?",
            "Tensor<[1216]> running_var = ?",
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
            "Tensor<[1, 1280, 14, 14]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "Tensor<[1280]> running_mean = ?",
            "Tensor<[1280]> running_var = ?",
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
            "Tensor<[1, 128, 7, 7]> input = ?",
            "Optional[Tensor]<[128]> weight = ?",
            "Optional[Tensor]<[128]> bias = ?",
            "Tensor<[128]> running_mean = ?",
            "Tensor<[128]> running_var = ?",
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
            "Tensor<[1, 1088, 7, 7]> input = ?",
            "Optional[Tensor]<[1088]> weight = ?",
            "Optional[Tensor]<[1088]> bias = ?",
            "Tensor<[1088]> running_mean = ?",
            "Tensor<[1088]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1120, 7, 7]> input = ?",
            "Optional[Tensor]<[1120]> weight = ?",
            "Optional[Tensor]<[1120]> bias = ?",
            "Tensor<[1120]> running_mean = ?",
            "Tensor<[1120]> running_var = ?",
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
            "Tensor<[1, 1184, 7, 7]> input = ?",
            "Optional[Tensor]<[1184]> weight = ?",
            "Optional[Tensor]<[1184]> bias = ?",
            "Tensor<[1184]> running_mean = ?",
            "Tensor<[1184]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1216, 7, 7]> input = ?",
            "Optional[Tensor]<[1216]> weight = ?",
            "Optional[Tensor]<[1216]> bias = ?",
            "Tensor<[1216]> running_mean = ?",
            "Tensor<[1216]> running_var = ?",
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
            "Tensor<[1, 1280, 7, 7]> input = ?",
            "Optional[Tensor]<[1280]> weight = ?",
            "Optional[Tensor]<[1280]> bias = ?",
            "Tensor<[1280]> running_mean = ?",
            "Tensor<[1280]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1312, 7, 7]> input = ?",
            "Optional[Tensor]<[1312]> weight = ?",
            "Optional[Tensor]<[1312]> bias = ?",
            "Tensor<[1312]> running_mean = ?",
            "Tensor<[1312]> running_var = ?",
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
            "Tensor<[1, 1376, 7, 7]> input = ?",
            "Optional[Tensor]<[1376]> weight = ?",
            "Optional[Tensor]<[1376]> bias = ?",
            "Tensor<[1376]> running_mean = ?",
            "Tensor<[1376]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1408, 7, 7]> input = ?",
            "Optional[Tensor]<[1408]> weight = ?",
            "Optional[Tensor]<[1408]> bias = ?",
            "Tensor<[1408]> running_mean = ?",
            "Tensor<[1408]> running_var = ?",
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
            "Tensor<[1, 1472, 7, 7]> input = ?",
            "Optional[Tensor]<[1472]> weight = ?",
            "Optional[Tensor]<[1472]> bias = ?",
            "Tensor<[1472]> running_mean = ?",
            "Tensor<[1472]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1504, 7, 7]> input = ?",
            "Optional[Tensor]<[1504]> weight = ?",
            "Optional[Tensor]<[1504]> bias = ?",
            "Tensor<[1504]> running_mean = ?",
            "Tensor<[1504]> running_var = ?",
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
            "Tensor<[1, 1568, 7, 7]> input = ?",
            "Optional[Tensor]<[1568]> weight = ?",
            "Optional[Tensor]<[1568]> bias = ?",
            "Tensor<[1568]> running_mean = ?",
            "Tensor<[1568]> running_var = ?",
            "float momentum = 0.1",
            "float eps = 1e-05",
        ],
        [
            "Tensor<[1, 1600, 7, 7]> input = ?",
            "Optional[Tensor]<[1600]> weight = ?",
            "Optional[Tensor]<[1600]> bias = ?",
            "Tensor<[1600]> running_mean = ?",
            "Tensor<[1600]> running_var = ?",
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
            "Tensor<[1, 1664, 7, 7]> input = ?",
            "Optional[Tensor]<[1664]> weight = ?",
            "Optional[Tensor]<[1664]> bias = ?",
            "Tensor<[1664]> running_mean = ?",
            "Tensor<[1664]> running_var = ?",
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
        "ttnn_fallbacks_to_host_count": "N/A",
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
