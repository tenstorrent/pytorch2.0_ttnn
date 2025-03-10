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
        return torch.ops.aten._unsafe_index.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten._unsafe_index.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 64, 15, 20]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_3]",
        ],
        [
            "Tensor<[1, 64, 15, 20]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_3]",
        ],
        [
            "Tensor<[1, 64, 15, 20]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_4]",
        ],
        [
            "Tensor<[1, 64, 15, 20]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_4]",
        ],
        [
            "Tensor<[1, 64, 30, 40]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_9]",
        ],
        [
            "Tensor<[1, 64, 30, 40]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_9]",
        ],
        [
            "Tensor<[1, 64, 30, 40]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_10]",
        ],
        [
            "Tensor<[1, 64, 30, 40]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_10]",
        ],
        [
            "Tensor<[1, 64, 60, 80]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_15]",
        ],
        [
            "Tensor<[1, 64, 60, 80]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_15]",
        ],
        [
            "Tensor<[1, 64, 60, 80]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_16]",
        ],
        [
            "Tensor<[1, 64, 60, 80]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_16]",
        ],
        [
            "Tensor<[1, 64, 120, 160]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_21]",
        ],
        [
            "Tensor<[1, 64, 120, 160]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_21]",
        ],
        [
            "Tensor<[1, 64, 120, 160]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_22]",
        ],
        [
            "Tensor<[1, 64, 120, 160]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_22]",
        ],
        [
            "Tensor<[1, 64, 240, 320]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_27]",
        ],
        [
            "Tensor<[1, 64, 240, 320]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_27]",
        ],
        [
            "Tensor<[1, 64, 240, 320]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_28]",
        ],
        [
            "Tensor<[1, 64, 240, 320]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_28]",
        ],
        [
            "Tensor<[1, 3, 320, 320]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_2]",
        ],
        [
            "Tensor<[1, 3, 320, 320]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_2]",
        ],
        [
            "Tensor<[1, 3, 320, 320]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_3]",
        ],
        [
            "Tensor<[1, 3, 320, 320]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_3]",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_3]",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_3]",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_4]",
        ],
        [
            "Tensor<[1, 256, 128, 128]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_4]",
        ],
        [
            "Tensor<[1, 256, 64, 64]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_9]",
        ],
        [
            "Tensor<[1, 256, 64, 64]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_9]",
        ],
        [
            "Tensor<[1, 256, 64, 64]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_10]",
        ],
        [
            "Tensor<[1, 256, 64, 64]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_10]",
        ],
        [
            "Tensor<[1, 256, 32, 32]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_15]",
        ],
        [
            "Tensor<[1, 256, 32, 32]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_15]",
        ],
        [
            "Tensor<[1, 256, 32, 32]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_16]",
        ],
        [
            "Tensor<[1, 256, 32, 32]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_16]",
        ],
        [
            "Tensor<[1, 256, 16, 16]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_21]",
        ],
        [
            "Tensor<[1, 256, 16, 16]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_21]",
        ],
        [
            "Tensor<[1, 256, 16, 16]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_22]",
        ],
        [
            "Tensor<[1, 256, 16, 16]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_22]",
        ],
        [
            "Tensor<[1, 1280, 8, 8]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_2]",
        ],
        ["Tensor<[1, 1280, s0, s1]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[2*s0, 1]>, <[2*s1]>]"],
        ["Tensor<[1, s0, s1, s2]> self = ?", "List[Optional[Tensor]] indices = [None, None, <[2*s1, 1]>, <[2*s2]>]"],
        [
            "Tensor<[1, 1, 384, 512]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_2]",
        ],
        [
            "Tensor<[1, 192, 50, 83]> self = ?",
            "List[Optional[Tensor]] indices = [_folded_view_2, _folded_view_3, <[1, 1, 32, 1]>, <[1, 1, 1, 42]>]",
        ],
        [
            "Tensor<[1, 256, 16, 16]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_2]",
        ],
        [
            "Tensor<[1, 128, 32, 32]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_6]",
        ],
        [
            "Tensor<[1, 72, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_2]",
        ],
        [
            "Tensor<[1, 72, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_6]",
        ],
        [
            "Tensor<[1, 120, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_10]",
        ],
        [
            "Tensor<[1, 240, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_3, _folded__to_copy_14]",
        ],
        [
            "Tensor<[1, 200, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_18]",
        ],
        [
            "Tensor<[1, 184, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_22]",
        ],
        [
            "Tensor<[1, 184, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_26]",
        ],
        [
            "Tensor<[1, 480, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_30]",
        ],
        [
            "Tensor<[1, 672, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_34]",
        ],
        [
            "Tensor<[1, 672, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_38]",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_42]",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_46]",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_50]",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_13, _folded__to_copy_54]",
        ],
        [
            "Tensor<[1, 72, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_36]",
        ],
        [
            "Tensor<[1, 72, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_54]",
        ],
        [
            "Tensor<[1, 120, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_78]",
        ],
        [
            "Tensor<[1, 240, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_3, _folded__to_copy_96]",
        ],
        [
            "Tensor<[1, 200, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_120]",
        ],
        [
            "Tensor<[1, 184, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_138]",
        ],
        [
            "Tensor<[1, 184, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_156]",
        ],
        [
            "Tensor<[1, 480, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_174]",
        ],
        [
            "Tensor<[1, 672, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_196]",
        ],
        [
            "Tensor<[1, 672, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_214]",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_238]",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_256]",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_274]",
        ],
        [
            "Tensor<[1, 960, 3, 3]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_13, _folded__to_copy_292]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_2]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_6]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_10]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_3, _folded__to_copy_14]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_18]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_22]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_26]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_30]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_34]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_38]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_42]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_46]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_50]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_13, _folded__to_copy_54]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_14, _folded__to_copy_58]",
        ],
        [
            "Tensor<[1, 18, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_15, _folded__to_copy_62]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_66]",
        ],
        [
            "Tensor<[1, 36, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_70]",
        ],
        [
            "Tensor<[1, 72, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_18, _folded__to_copy_74]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_78]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_82]",
        ],
        [
            "Tensor<[1, 18, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_21, _folded__to_copy_86]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_22, _folded__to_copy_90]",
        ],
        [
            "Tensor<[1, 36, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_23, _folded__to_copy_94]",
        ],
        [
            "Tensor<[1, 72, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_24, _folded__to_copy_98]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_25, _folded__to_copy_102]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_26, _folded__to_copy_106]",
        ],
        [
            "Tensor<[1, 18, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_27, _folded__to_copy_110]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_28, _folded__to_copy_114]",
        ],
        [
            "Tensor<[1, 36, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_29, _folded__to_copy_118]",
        ],
        [
            "Tensor<[1, 72, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_30, _folded__to_copy_122]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze, _folded__to_copy_70]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_128]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_2, _folded__to_copy_134]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_3, _folded__to_copy_142]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_4, _folded__to_copy_202]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_5, _folded__to_copy_208]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_216]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_276]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_282]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_290]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_10, _folded__to_copy_350]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_11, _folded__to_copy_356]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_12, _folded__to_copy_364]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_13, _folded__to_copy_442]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_14, _folded__to_copy_448]",
        ],
        [
            "Tensor<[1, 18, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_15, _folded__to_copy_454]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_16, _folded__to_copy_462]",
        ],
        [
            "Tensor<[1, 36, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_17, _folded__to_copy_468]",
        ],
        [
            "Tensor<[1, 72, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_18, _folded__to_copy_480]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_19, _folded__to_copy_562]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_20, _folded__to_copy_568]",
        ],
        [
            "Tensor<[1, 18, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_21, _folded__to_copy_574]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_22, _folded__to_copy_582]",
        ],
        [
            "Tensor<[1, 36, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_23, _folded__to_copy_588]",
        ],
        [
            "Tensor<[1, 72, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_24, _folded__to_copy_600]",
        ],
        [
            "Tensor<[1, 18, 28, 28]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_25, _folded__to_copy_682]",
        ],
        [
            "Tensor<[1, 18, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_26, _folded__to_copy_688]",
        ],
        [
            "Tensor<[1, 18, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_27, _folded__to_copy_694]",
        ],
        [
            "Tensor<[1, 36, 14, 14]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_28, _folded__to_copy_702]",
        ],
        [
            "Tensor<[1, 36, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_29, _folded__to_copy_708]",
        ],
        [
            "Tensor<[1, 72, 7, 7]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_30, _folded__to_copy_720]",
        ],
        [
            "Tensor<[1, 3, 480, 640]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_2]",
        ],
        [
            "Tensor<[1, 3, 480, 640]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_2]",
        ],
        [
            "Tensor<[1, 3, 480, 640]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_6, _folded__to_copy_3]",
        ],
        [
            "Tensor<[1, 3, 480, 640]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_7, _folded__to_copy_3]",
        ],
        [
            "Tensor<[1, 256, 25, 34]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_8, _folded__to_copy_5]",
        ],
        [
            "Tensor<[1, 256, 50, 68]> self = ?",
            "List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_9, _folded__to_copy_7]",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten._unsafe_index.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten._unsafe_index.Tensor", input_strings
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
