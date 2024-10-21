import torch
import torch_ttnn.metrics as metrics
from functools import partial

aten_permute_default_blocklist = [
    ["Tensor<[1, 3, 16, 16, 16, 16]> self = ?", "List[int] dims = [0, 2, 4, 3, 5, 1]"],
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
    ["Tensor<[64, 64, 3]> self = ?", "List[int] dims = [2, 0, 1]"],
    ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[64, 64, 3, 3, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 4, 8, 4, 8, 192]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[16, 64, 3, 6, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 4, 4, 8, 8, 192]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 2, 8, 2, 8, 384]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[4, 64, 3, 12, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 2, 2, 8, 8, 384]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 1, 8, 1, 8, 768]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 64, 3, 24, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 1, 1, 8, 8, 768]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
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
    ["Tensor<[49, 49, 3]> self = ?", "List[int] dims = [2, 0, 1]"],
    ["Tensor<[1, 8, 7, 8, 7, 96]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[64, 49, 3, 3, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 8, 8, 7, 7, 96]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[8, 7, 8, 7]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
    ["Tensor<[1, 4, 7, 4, 7, 192]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[16, 49, 3, 6, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 4, 4, 7, 7, 192]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[4, 7, 4, 7]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
    ["Tensor<[1, 2, 7, 2, 7, 384]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[4, 49, 3, 12, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 2, 2, 7, 7, 384]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[2, 7, 2, 7]> self = ?", "List[int] dims = [0, 2, 1, 3]"],
    ["Tensor<[1, 1, 7, 1, 7, 768]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 49, 3, 24, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 1, 1, 7, 7, 768]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[12, 197, 197]> self = ?", "List[int] dims = [1, 2, 0]"],
    ["Tensor<[1, 3, 85, 64, 64]> self = ?", "List[int] dims = [0, 1, 3, 4, 2]"],
    ["Tensor<[1, 3, 85, 32, 32]> self = ?", "List[int] dims = [0, 1, 3, 4, 2]"],
    ["Tensor<[1, 3, 85, 16, 16]> self = ?", "List[int] dims = [0, 1, 3, 4, 2]"],
    ["Tensor<[1, 4, 4, 38, 38]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
    ["Tensor<[1, 6, 4, 19, 19]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
    ["Tensor<[1, 4, 4, 3, 3]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
    ["Tensor<[1, 4, 4, 1, 1]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
    ["Tensor<[1, 4, 91, 38, 38]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
    ["Tensor<[1, 6, 91, 19, 19]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
    ["Tensor<[1, 4, 91, 3, 3]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
    ["Tensor<[1, 4, 91, 1, 1]> self = ?", "List[int] dims = [0, 3, 4, 1, 2]"],
    ["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[64, 64, 3, 4, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 4, 8, 4, 8, 256]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[16, 64, 3, 8, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 4, 4, 8, 8, 256]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 2, 8, 2, 8, 512]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[4, 64, 3, 16, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 2, 2, 8, 8, 512]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 1, 8, 1, 8, 1024]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 64, 3, 32, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 1, 1, 8, 8, 1024]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 8, 7, 8, 7, 128]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[64, 49, 3, 4, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 8, 8, 7, 7, 128]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 4, 7, 4, 7, 256]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[16, 49, 3, 8, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 4, 4, 7, 7, 256]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 2, 7, 2, 7, 512]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[4, 49, 3, 16, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 2, 2, 7, 7, 512]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 1, 7, 1, 7, 1024]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 49, 3, 32, 32]> self = ?", "List[int] dims = [2, 0, 3, 1, 4]"],
    ["Tensor<[1, 1, 1, 7, 7, 1024]> self = ?", "List[int] dims = [0, 1, 3, 2, 4, 5]"],
    ["Tensor<[1, 1024, 49]> self = ?", "List[int] dims = [0, 2, 1]"],
    ["Tensor<[1, 768, 49]> self = ?", "List[int] dims = [0, 2, 1]"],
    ["Tensor<[1, 1280, 1369]> self = ?", "List[int] dims = [0, 2, 1]"],
    ["Tensor<[16, 197, 197]> self = ?", "List[int] dims = [1, 2, 0]"],
]
aten_view_default_blocklist = [
    ["Tensor<[1, 3, 256, 256]> self = ?", "List[int] size = [1, 3, 16, 16, 16, 16]"],
    ["Tensor<[1, 256, 768]> self = ?", "List[int] size = [1, 16, 16, 16, 16, 3]"],
    ["Tensor<[1, 32, 16, 16]> self = ?", "List[int] size = [1, 32, 256]"],
    ["Tensor<[1, 16384, 1, 32]> self = ?", "List[int] size = [1, 16384, 32]"],
    ["Tensor<[1, 64, 16, 16]> self = ?", "List[int] size = [1, 64, 256]"],
    ["Tensor<[1, 160, 16, 16]> self = ?", "List[int] size = [1, 160, 256]"],
    ["Tensor<[1, 256, 16, 16]> self = ?", "List[int] size = [1, 256, 256]"],
    ["Tensor<[1, 1024, 16, 16]> self = ?", "List[int] size = [1, 1024, 256]"],
    ["Tensor<[1, 16, 16, 256]> self = ?", "List[int] size = [1, 256, 256]"],
    ["Tensor<[1, 256, 1, 32]> self = ?", "List[int] size = [1, 256, 32]"],
    ["Tensor<[1, 192, 32, 42]> self = ?", "List[int] size = [1, 192, 1344]"],
    ["Tensor<[1, 19200, 1, 64]> self = ?", "List[int] size = [1, 19200, 64]"],
    ["Tensor<[1, 128, 60, 80]> self = ?", "List[int] size = [1, 128, 4800]"],
    ["Tensor<[1, 512, 60, 80]> self = ?", "List[int] size = [1, 512, 4800]"],
    ["Tensor<[64, 64, 288]> self = ?", "List[int] size = [64, 64, 3, 3, 32]"],
    ["Tensor<[16, 64, 576]> self = ?", "List[int] size = [16, 64, 3, 6, 32]"],
    ["Tensor<[1, 16, 16, 768]> self = ?", "List[int] size = [256, 768]"],
    ["Tensor<[4, 64, 1152]> self = ?", "List[int] size = [4, 64, 3, 12, 32]"],
    ["Tensor<[1, 16, 16, 384]> self = ?", "List[int] size = [256, 384]"],
    ["Tensor<[1, 16, 16, 1536]> self = ?", "List[int] size = [256, 1536]"],
    ["Tensor<[1, 8, 8, 1536]> self = ?", "List[int] size = [64, 1536]"],
    ["Tensor<[1, 1, 1, 8, 8, 768]> self = ?", "List[int] size = [1, 64, 768]"],
    ["Tensor<[1, 64, 2304]> self = ?", "List[int] size = [1, 64, 3, 24, 32]"],
    ["Tensor<[1, 8, 8, 768]> self = ?", "List[int] size = [64, 768]"],
    ["Tensor<[1, 8, 8, 3072]> self = ?", "List[int] size = [64, 3072]"],
    ["Tensor<[0, 1, 4]> self = ?", "List[int] size = [0, 4]"],
    ["Tensor<[0, 2, 2]> self = ?", "List[int] size = [0, 4]"],
    ["Tensor<[1, 2048]> self = ?", "List[int] size = [1, 2048, 1, 1]"],
    ["Tensor<[64, 49, 96]> self = ?", "List[int] size = [3136, 96]"],
    ["Tensor<[64, 49, 288]> self = ?", "List[int] size = [64, 49, 3, 3, 32]"],
    ["Tensor<[1, 56, 56, 96]> self = ?", "List[int] size = [3136, 96]"],
    ["Tensor<[1, 56, 56, 384]> self = ?", "List[int] size = [3136, 384]"],
    ["Tensor<[16, 49, 576]> self = ?", "List[int] size = [16, 49, 3, 6, 32]"],
    ["Tensor<[4, 49, 1152]> self = ?", "List[int] size = [4, 49, 3, 12, 32]"],
    ["Tensor<[1, 49, 2304]> self = ?", "List[int] size = [1, 49, 3, 24, 32]"],
    ["Tensor<[1, 1024]> self = ?", "List[int] size = [1, 1024, 1, 1]"],
    ["Tensor<[1, 32, 4608]> self = ?", "List[int] size = [1, 32, 16, 3, 96]"],
    ["Tensor<[1, 768, 12, 16]> self = ?", "List[int] size = [1, 768, 192]"],
    ["Tensor<[64, 64, 384]> self = ?", "List[int] size = [64, 64, 3, 4, 32]"],
    ["Tensor<[16, 64, 768]> self = ?", "List[int] size = [16, 64, 3, 8, 32]"],
    ["Tensor<[1, 16, 16, 1024]> self = ?", "List[int] size = [256, 1024]"],
    ["Tensor<[4, 64, 1536]> self = ?", "List[int] size = [4, 64, 3, 16, 32]"],
    ["Tensor<[1, 16, 16, 512]> self = ?", "List[int] size = [256, 512]"],
    ["Tensor<[1, 16, 16, 2048]> self = ?", "List[int] size = [256, 2048]"],
    ["Tensor<[1, 8, 8, 2048]> self = ?", "List[int] size = [64, 2048]"],
    ["Tensor<[1, 1, 1, 8, 8, 1024]> self = ?", "List[int] size = [1, 64, 1024]"],
    ["Tensor<[1, 64, 3072]> self = ?", "List[int] size = [1, 64, 3, 32, 32]"],
    ["Tensor<[1, 8, 8, 1024]> self = ?", "List[int] size = [64, 1024]"],
    ["Tensor<[1, 8, 8, 4096]> self = ?", "List[int] size = [64, 4096]"],
    ["Tensor<[64, 49, 128]> self = ?", "List[int] size = [3136, 128]"],
    ["Tensor<[64, 49, 384]> self = ?", "List[int] size = [64, 49, 3, 4, 32]"],
    ["Tensor<[1, 56, 56, 128]> self = ?", "List[int] size = [3136, 128]"],
    ["Tensor<[1, 56, 56, 512]> self = ?", "List[int] size = [3136, 512]"],
    ["Tensor<[16, 49, 768]> self = ?", "List[int] size = [16, 49, 3, 8, 32]"],
    ["Tensor<[4, 49, 1536]> self = ?", "List[int] size = [4, 49, 3, 16, 32]"],
    ["Tensor<[1, 49, 3072]> self = ?", "List[int] size = [1, 49, 3, 32, 32]"],
    ["Tensor<[1, 512]> self = ?", "List[int] size = [1, 512, 1, 1]"],
]
aten__unsafe_view_default_blocklist = [
    ["Tensor<[1, 16, 16, 16, 16, 3]> self = ?", "List[int] size = [1, 256, 768]"],
    ["Tensor<[1, 3, 16, 16, 16, 16]> self = ?", "List[int] size = [1, 3, 256, 256]"],
    ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] size = [64, 64, 96]"],
    ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] size = [1, 64, 64, 96]"],
    ["Tensor<[8, 8, 8, 8]> self = ?", "List[int] size = [64, 64]"],
    ["Tensor<[1, 4, 4, 8, 8, 192]> self = ?", "List[int] size = [16, 64, 192]"],
    ["Tensor<[1, 4, 8, 4, 8, 192]> self = ?", "List[int] size = [1, 32, 32, 192]"],
    ["Tensor<[1, 2, 2, 8, 8, 384]> self = ?", "List[int] size = [4, 64, 384]"],
    ["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "List[int] size = [64, 64, 128]"],
    ["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "List[int] size = [1, 64, 64, 128]"],
    ["Tensor<[1, 4, 4, 8, 8, 256]> self = ?", "List[int] size = [16, 64, 256]"],
    ["Tensor<[1, 4, 8, 4, 8, 256]> self = ?", "List[int] size = [1, 32, 32, 256]"],
    ["Tensor<[1, 2, 2, 8, 8, 512]> self = ?", "List[int] size = [4, 64, 512]"],
]
aten_add_Tensor_blocklist = [
    ["Tensor<[]> self = ?", "Tensor other = 1"],
    ["Tensor<[1, 16, 19, 19]> self = ?", "Tensor<[1, 1, 19, 19]> other = ?"],
    ["Tensor<[1, 64, 3, 64, 64]> self = ?", "Tensor<[1, 64, 1, 64, 64]> other = ?"],
    ["Tensor<[1, 16, 6, 64, 64]> self = ?", "Tensor<[1, 16, 1, 64, 64]> other = ?"],
    ["Tensor<[1, 4, 12, 64, 64]> self = ?", "Tensor<[1, 4, 1, 64, 64]> other = ?"],
    ["Tensor<[13600, 1, 4]> self = ?", "Tensor<[1, 9, 4]> other = ?"],
    ["Tensor<[3400, 1, 4]> self = ?", "Tensor<[1, 9, 4]> other = ?"],
    ["Tensor<[850, 1, 4]> self = ?", "Tensor<[1, 9, 4]> other = ?"],
    ["Tensor<[221, 1, 4]> self = ?", "Tensor<[1, 9, 4]> other = ?"],
    ["Tensor<[63, 1, 4]> self = ?", "Tensor<[1, 9, 4]> other = ?"],
    ["Tensor<[0]> self = ?", "Tensor<[0]> other = ?"],
    ["Tensor<[0, 1]> self = ?", "Tensor<[0, 1]> other = ?"],
    ["Tensor<[1, 64, 1, 1]> self = ?", "Tensor other = 1e-05"],
    ["Tensor<[1, 256, 1, 1]> self = ?", "Tensor other = 1e-05"],
    ["Tensor<[1, 128, 1, 1]> self = ?", "Tensor other = 1e-05"],
    ["Tensor<[1, 512, 1, 1]> self = ?", "Tensor other = 1e-05"],
    ["Tensor<[1, 1024, 1, 1]> self = ?", "Tensor other = 1e-05"],
    ["Tensor<[1, 2048, 1, 1]> self = ?", "Tensor other = 1e-05"],
    ["Tensor<[920, 1, 256]> self = ?", "Tensor<[256]> other = ?"],
    ["Tensor<[1, 64, 3, 49, 49]> self = ?", "Tensor<[1, 64, 1, 49, 49]> other = ?"],
    ["Tensor<[1, 16, 6, 49, 49]> self = ?", "Tensor<[1, 16, 1, 49, 49]> other = ?"],
    ["Tensor<[1, 4, 12, 49, 49]> self = ?", "Tensor<[1, 4, 1, 49, 49]> other = ?"],
    ["Tensor<[2, 7, 512]> self = ?", "Tensor<[1, 7, 512]> other = ?"],
    ["Tensor<[2, 8, 7, 7]> self = ?", "Tensor<[2, 1, 7, 7]> other = ?"],
    ["Tensor<[1, 71, 7, 7]> self = ?", "Tensor<[7, 7]> other = ?"],
    ["Tensor<[]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 64, 4, 64, 64]> self = ?", "Tensor<[1, 64, 1, 64, 64]> other = ?"],
    ["Tensor<[1, 16, 8, 64, 64]> self = ?", "Tensor<[1, 16, 1, 64, 64]> other = ?"],
    ["Tensor<[1, 4, 16, 64, 64]> self = ?", "Tensor<[1, 4, 1, 64, 64]> other = ?"],
    ["Tensor<[1, 64, 4, 49, 49]> self = ?", "Tensor<[1, 64, 1, 49, 49]> other = ?"],
    ["Tensor<[1, 16, 8, 49, 49]> self = ?", "Tensor<[1, 16, 1, 49, 49]> other = ?"],
    ["Tensor<[1, 4, 16, 49, 49]> self = ?", "Tensor<[1, 4, 1, 49, 49]> other = ?"],
    ["Tensor<[1, 64, 1, 1]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[1, 256, 1, 1]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[1, 128, 1, 1]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[1, 512, 1, 1]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[1, 1024, 1, 1]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[1, 2048, 1, 1]> self = ?", "Tensor other = 0.0"],
]
aten_clamp_default_blocklist = [
    ["Tensor<[128]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 127"],
    ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 63"],
    ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 31"],
    ["Tensor<[128]> self = ?", "Optional[number] min = ?", "Optional[number] max = 15"],
    ["Tensor<[320]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
    ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
    ["Tensor<[3234, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
    ["Tensor<[30]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[40]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[30]> self = ?", "Optional[number] min = ?", "Optional[number] max = 14"],
    ["Tensor<[40]> self = ?", "Optional[number] min = ?", "Optional[number] max = 19"],
    ["Tensor<[60]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[80]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[60]> self = ?", "Optional[number] min = ?", "Optional[number] max = 29"],
    ["Tensor<[80]> self = ?", "Optional[number] min = ?", "Optional[number] max = 39"],
    ["Tensor<[120]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[160]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[120]> self = ?", "Optional[number] min = ?", "Optional[number] max = 59"],
    ["Tensor<[160]> self = ?", "Optional[number] min = ?", "Optional[number] max = 79"],
    ["Tensor<[240]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[240]> self = ?", "Optional[number] min = ?", "Optional[number] max = 119"],
    ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 159"],
    ["Tensor<[480]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[640]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[480]> self = ?", "Optional[number] min = ?", "Optional[number] max = 239"],
    ["Tensor<[640]> self = ?", "Optional[number] min = ?", "Optional[number] max = 319"],
    ["Tensor<[3, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[6, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[12, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[24, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[800]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[1066]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[800]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
    ["Tensor<[1066]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
    ["Tensor<[0, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
    ["Tensor<[0, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 1066"],
    ["Tensor<[0, 2]> self = ?", "Optional[number] min = 0", "Optional[number] max = 800"],
    ["Tensor<[320]> self = ?", "Optional[number] min = ?", "Optional[number] max = 319"],
    ["Tensor<[300]> self = ?", "Optional[number] min = 0.0"],
    ["Tensor<[300]> self = ?", "Optional[number] min = ?", "Optional[number] max = 479"],
    ["Tensor<[300]> self = ?", "Optional[number] min = ?", "Optional[number] max = 639"],
    ["Tensor<[8732, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.135166556742356"],
    ["Tensor<[4, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[8, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[16, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
    ["Tensor<[32, 1, 1]> self = ?", "Optional[number] min = ?", "Optional[number] max = 4.605170185988092"],
]
aten_maximum_default_blocklist = [["Tensor<[1, 16, 19, 19]> self = ?", "Tensor<[]> other = ?"]]
aten__log_softmax_default_blocklist = [["Tensor<[19, 256008]> self = ?", "int dim = 1", "bool half_to_float = False"]]
aten_expand_default_blocklist = [
    ["Tensor<[1, 1, 1, 19]> self = ?", "List[int] size = [1, 1, 19, 19]"],
    ["Tensor<[256, 1280]> self = ?", "List[int] size = [1, -1, -1]"],
    ["Tensor<[2048, 768]> self = ?", "List[int] size = [1, -1, -1]"],
    ["Tensor<[1, 5]> self = ?", "List[int] size = [5, 5]"],
    ["Tensor<[1, 3]> self = ?", "List[int] size = [3, 3]"],
    ["Tensor<[1, 17]> self = ?", "List[int] size = [13, 17]"],
    ["Tensor<[1, 9]> self = ?", "List[int] size = [7, 9]"],
    ["Tensor<[768]> self = ?", "List[int] size = [1, 1, -1]"],
    ["Tensor<[1, 1, 7, 7]> self = ?", "List[int] size = [2, 1, 7, 7]"],
    ["Tensor<[2, 1, 1, 7]> self = ?", "List[int] size = [2, 1, 7, 7]"],
    ["Tensor<[1, 1, 64, 7]> self = ?", "List[int] size = [1, 71, 64, 7]"],
    ["Tensor<[1, 19]> self = ?", "List[int] size = [19, 19]"],
]
aten_full_default_blocklist = [
    [
        "List[int] size = [19, 19]",
        "number fill_value = -3.4028234663852886e+38",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
    [
        "List[int] size = [7, 7]",
        "number fill_value = -3.3895313892515355e+38",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ],
]
aten_rsub_Scalar_blocklist = [
    ["Tensor<[1, 1, 19, 19]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 9]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 25]> self = ?", "number other = 1.0"],
    ["Tensor<[2, 1, 7, 7]> self = ?", "number other = 1.0"],
    ["Tensor<[1, 1, 1, 7]> self = ?", "number other = 1.0"],
]
aten_addmm_default_blocklist = [
    ["Tensor<[4096]> self = ?", "Tensor<[1, 25088]> mat1 = ?", "Tensor<[25088, 4096]> mat2 = ?"]
]
aten__scaled_dot_product_flash_attention_default_blocklist = [
    ["Tensor<[1, 16, 197, 64]> query = ?", "Tensor<[1, 16, 197, 64]> key = ?", "Tensor<[1, 16, 197, 64]> value = ?"],
    ["Tensor<[1, 12, 197, 64]> query = ?", "Tensor<[1, 12, 197, 64]> key = ?", "Tensor<[1, 12, 197, 64]> value = ?"],
    ["Tensor<[1, 16, 50, 64]> query = ?", "Tensor<[1, 16, 50, 64]> key = ?", "Tensor<[1, 16, 50, 64]> value = ?"],
    ["Tensor<[1, 8, 4096, 40]> query = ?", "Tensor<[1, 8, 4096, 40]> key = ?", "Tensor<[1, 8, 4096, 40]> value = ?"],
    ["Tensor<[1, 8, 1024, 80]> query = ?", "Tensor<[1, 8, 9, 80]> key = ?", "Tensor<[1, 8, 9, 80]> value = ?"],
    ["Tensor<[1, 8, 256, 160]> query = ?", "Tensor<[1, 8, 256, 160]> key = ?", "Tensor<[1, 8, 256, 160]> value = ?"],
    ["Tensor<[1, 8, 64, 160]> query = ?", "Tensor<[1, 8, 64, 160]> key = ?", "Tensor<[1, 8, 64, 160]> value = ?"],
]
aten_transpose_int_blocklist = [
    ["Tensor<[1, 197, 1, 3, 1024]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[12, 197, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[12, 64, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[1, 12, 64, 197]> self = ?", "int dim0 = -1", "int dim1 = -2"],
    ["Tensor<[1, 197, 1, 3, 768]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[1, 768, 49]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[16, 7, 7]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[16, 64, 7]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[1, 50, 1, 3, 1024]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[1, 50, 1, 3, 768]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[1, 1370, 1, 3, 1280]> self = ?", "int dim0 = 0", "int dim1 = -2"],
    ["Tensor<[16, 197, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[16, 64, 197]> self = ?", "int dim0 = 1", "int dim1 = 2"],
    ["Tensor<[1, 16, 64, 197]> self = ?", "int dim0 = -1", "int dim1 = -2"],
]
aten_embedding_default_blocklist = [["Tensor<[2048, 768]> weight = ?", "Tensor<[2048]> indices = ?"]]
aten_zeros_like_default_blocklist = [
    ["Tensor<[13685]> self = ?", "Optional[int] dtype = torch.bool", "Optional[bool] pin_memory = False"],
    ["Tensor<[7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
]
aten_div_Tensor_blocklist = [
    ["Tensor<[]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 12, 9, 9]> self = ?", "Tensor other = 8.0"],
    ["Tensor<[1, 64, 9, 9]> self = ?", "Tensor other = 8.0"],
    ["Tensor<[1, 23, 40, 1]> self = ?", "Tensor<[128]> other = ?"],
    ["Tensor<[1, 12, 25, 25]> self = ?", "Tensor other = 8.0"],
    ["Tensor<[1, 16, 9, 9]> self = ?", "Tensor other = 11.313708498984761"],
    ["Tensor<[1, 16, 9, 9]> self = ?", "Tensor other = 8.0"],
    ["Tensor<[1, 12, 7, 7]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 1280, 8, 8]> self = ?", "Tensor other = 1"],
]
aten_mul_Tensor_blocklist = [
    ["Tensor<[]> self = ?", "Tensor<[3234, 1]> other = ?"],
    ["Tensor<[300]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 64, 30, 40]> self = ?", "Tensor<[1, 1, 30, 40]> other = ?"],
    ["Tensor<[1, 64, 60, 80]> self = ?", "Tensor<[1, 1, 60, 80]> other = ?"],
    ["Tensor<[1, 64, 120, 160]> self = ?", "Tensor<[1, 1, 120, 160]> other = ?"],
    ["Tensor<[64, 3, 64, 64]> self = ?", "Tensor<[3, 1, 1]> other = ?"],
    ["Tensor<[16, 6, 64, 64]> self = ?", "Tensor<[6, 1, 1]> other = ?"],
    ["Tensor<[4, 12, 64, 64]> self = ?", "Tensor<[12, 1, 1]> other = ?"],
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
    ["Tensor<[16, 1]> self = ?", "Tensor<[1, 1, 32]> other = ?"],
    ["Tensor<[2, 1]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 71, 7, 64]> self = ?", "Tensor<[1, 1, 7, 64]> other = ?"],
    ["Tensor<[1, 3, 64, 64, 2]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 3, 32, 32, 2]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[1, 3, 16, 16, 2]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[]> self = ?", "Tensor<[8732, 1]> other = ?"],
    ["Tensor<[12]> self = ?", "Tensor<[]> other = ?"],
    ["Tensor<[64, 4, 64, 64]> self = ?", "Tensor<[4, 1, 1]> other = ?"],
    ["Tensor<[16, 8, 64, 64]> self = ?", "Tensor<[8, 1, 1]> other = ?"],
    ["Tensor<[4, 16, 64, 64]> self = ?", "Tensor<[16, 1, 1]> other = ?"],
]
aten_slice_Tensor_blocklist = [
    ["Tensor<[1, 512]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 9"],
    ["Tensor<[1, 512]> self = ?", "int dim = 1", "Optional[int] start = 0", "Optional[int] end = 25"],
    ["Tensor<[1, 1, 7, 1024]> self = ?", "int dim = 3", "Optional[int] start = 0", "Optional[int] end = 7"],
]
aten_native_layer_norm_default_blocklist = [
    [
        "Tensor<[1, 9, 4096]> input = ?",
        "List[int] normalized_shape = [4096]",
        "Optional[Tensor]<[4096]> weight = ?",
        "Optional[Tensor]<[4096]> bias = ?",
        "float eps = 1e-12",
    ],
    [
        "Tensor<[1, 7, 4544]> input = ?",
        "List[int] normalized_shape = [4544]",
        "Optional[Tensor]<[4544]> weight = ?",
        "Optional[Tensor]<[4544]> bias = ?",
        "float eps = 1e-05",
    ],
]
aten_sub_Tensor_blocklist = [
    ["Tensor<[64, 1, 64]> self = ?", "Tensor<[64, 64, 1]> other = ?"],
    ["Tensor<[16, 1, 64]> self = ?", "Tensor<[16, 64, 1]> other = ?"],
    ["Tensor<[4, 1, 64]> self = ?", "Tensor<[4, 64, 1]> other = ?"],
    ["Tensor<[0]> self = ?", "Tensor<[0]> other = ?"],
    ["Tensor<[0, 1]> self = ?", "Tensor<[0, 1]> other = ?"],
    ["Tensor<[64, 1, 49]> self = ?", "Tensor<[64, 49, 1]> other = ?"],
    ["Tensor<[16, 1, 49]> self = ?", "Tensor<[16, 49, 1]> other = ?"],
    ["Tensor<[4, 1, 49]> self = ?", "Tensor<[4, 49, 1]> other = ?"],
]
aten_exp_default_blocklist = [["Tensor<[0, 1]> self = ?"], ["Tensor<[]> self = ?"]]
aten_split_Tensor_blocklist = [
    ["Tensor<[768, 256]> self = ?", "int split_size = 256"],
    ["Tensor<[768]> self = ?", "int split_size = 256"],
    ["Tensor<[1, 7, 2304]> self = ?", "int split_size = 768", "int dim = 2"],
]
aten_t_default_blocklist = [
    ["Tensor<[12, 3]> self = ?"],
    ["Tensor<[1, 3]> self = ?"],
    ["Tensor<[2, 1]> self = ?"],
    ["Tensor<[512, 1]> self = ?"],
]
aten_ones_default_blocklist = [
    [
        "List[int] size = [7, 7]",
        "Optional[int] dtype = torch.bool",
        "Optional[int] layout = torch.strided",
        "Optional[Device] device = cpu",
    ]
]
aten_where_self_blocklist = [
    ["Tensor<[1, 1, 7, 7]> condition = ?", "Tensor<[1, 12, 7, 7]> self = ?", "Tensor<[]> other = ?"]
]
aten_empty_memory_format_blocklist = [
    [
        "List[int] size = []",
        "Optional[int] dtype = torch.int64",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ]
]

# Add for pass CLIP eval
aten_mul_Tensor_blocklist += [
    ["Tensor<[1, 50, 768]> self = ?", "Tensor other = 0.125"],
    ["Tensor<[1, 50, 3072]> self = ?", "Tensor other = 1.702"],
    ["Tensor<[1, 50, 3072]> self = ?", "Tensor<[1, 50, 3072]> other = ?"],
    ["Tensor<[2, 7, 512]> self = ?", "Tensor other = 0.125"],
    ["Tensor<[2, 7, 2048]> self = ?", "Tensor other = 1.702"],
    ["Tensor<[2, 7, 2048]> self = ?", "Tensor<[2, 7, 2048]> other = ?"],
    ["Tensor<[2, 1]> self = ?", "Tensor<[]> other = ?"],
]

aten_view_default_blocklist += [
    ["Tensor<[1, 768, 7, 7]> self = ?", "List[int] size = [1, 768, 49]"],
    ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [50, 768]"],
    ["Tensor<[50, 768]> self = ?", "List[int] size = [1, 50, 768]"],
    ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [1, -1, 12, 64]"],
    ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [1, 50, 12, 64]"],
    ["Tensor<[1, 12, 50, 64]> self = ?", "List[int] size = [12, -1, 64]"],
    ["Tensor<[12, 50, 64]> self = ?", "List[int] size = [1, 12, 50, 64]"],
    ["Tensor<[50, 3072]> self = ?", "List[int] size = [1, 50, 3072]"],
    ["Tensor<[1, 50, 3072]> self = ?", "List[int] size = [50, 3072]"],
    ["Tensor<[2, 7]> self = ?", "List[int] size = [-1, 7]"],
    ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [14, 512]"],
    ["Tensor<[14, 512]> self = ?", "List[int] size = [2, 7, 512]"],
    ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [2, -1, 8, 64]"],
    ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [2, 7, 8, 64]"],
    ["Tensor<[2, 8, 7, 64]> self = ?", "List[int] size = [16, -1, 64]"],
    ["Tensor<[16, 7, 7]> self = ?", "List[int] size = [2, 8, 7, 7]"],
    ["Tensor<[2, 8, 7, 7]> self = ?", "List[int] size = [16, 7, 7]"],
    ["Tensor<[16, 7, 64]> self = ?", "List[int] size = [2, 8, 7, 64]"],
    ["Tensor<[14, 2048]> self = ?", "List[int] size = [2, 7, 2048]"],
    ["Tensor<[2, 7, 2048]> self = ?", "List[int] size = [14, 2048]"],
]

aten__to_copy_default_blocklist = [
    ["Tensor<[1, 3, 224, 224]> self = ?", "Optional[int] dtype = torch.bfloat16"],
    ["Tensor<[7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
    ["Tensor<[2, 1, 7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
    ["Tensor<[2, 1, 7, 7]> self = ?", "Optional[int] dtype = torch.bool"],
    ["Tensor<[2, 7]> self = ?", "Optional[int] dtype = torch.int32", "Optional[Device] device = cpu"],
]

aten_native_layer_norm_default_blocklist += [
    [
        "Tensor<[1, 50, 768]> input = ?",
        "List[int] normalized_shape = [768]",
        "Optional[Tensor]<[768]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "float eps = 1e-05",
    ],
    [
        "Tensor<[1, 768]> input = ?",
        "List[int] normalized_shape = [768]",
        "Optional[Tensor]<[768]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "float eps = 1e-05",
    ],
    [
        "Tensor<[2, 7, 512]> input = ?",
        "List[int] normalized_shape = [512]",
        "Optional[Tensor]<[512]> weight = ?",
        "Optional[Tensor]<[512]> bias = ?",
        "float eps = 1e-05",
    ],
]

# Need to remove this from the blocklist so that yolos can pass
aten_view_default_blocklist.remove(["Tensor<[1, 192, 32, 42]> self = ?", "List[int] size = [1, 192, 1344]"])


def get_inputs(node):
    node_inputs = metrics.collect_input_variation_from_node(node)
    if type(node_inputs) == metrics.InputVariation:
        return node_inputs.inputs
    elif type(node_inputs) == metrics.ConvertedInput:
        return node_inputs.original_input_variation.inputs
    else:
        return None


def guard_aten(blocklist, node):
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blocklist:
        return False
    return True


GUARD = {
    torch.ops.aten.permute.default: partial(guard_aten, aten_permute_default_blocklist),
    torch.ops.aten.view.default: partial(guard_aten, aten_view_default_blocklist),
    torch.ops.aten._unsafe_view.default: partial(guard_aten, aten__unsafe_view_default_blocklist),
    torch.ops.aten.add.Tensor: partial(guard_aten, aten_add_Tensor_blocklist),
    torch.ops.aten.clamp.default: partial(guard_aten, aten_clamp_default_blocklist),
    torch.ops.aten.maximum.default: partial(guard_aten, aten_maximum_default_blocklist),
    torch.ops.aten._log_softmax.default: partial(guard_aten, aten__log_softmax_default_blocklist),
    torch.ops.aten.expand.default: partial(guard_aten, aten_expand_default_blocklist),
    torch.ops.aten.full.default: partial(guard_aten, aten_full_default_blocklist),
    torch.ops.aten.rsub.Scalar: partial(guard_aten, aten_rsub_Scalar_blocklist),
    torch.ops.aten.addmm.default: partial(guard_aten, aten_addmm_default_blocklist),
    torch.ops.aten._scaled_dot_product_flash_attention.default: partial(
        guard_aten, aten__scaled_dot_product_flash_attention_default_blocklist
    ),
    torch.ops.aten.transpose.int: partial(guard_aten, aten_transpose_int_blocklist),
    torch.ops.aten.embedding.default: partial(guard_aten, aten_embedding_default_blocklist),
    torch.ops.aten.zeros_like.default: partial(guard_aten, aten_zeros_like_default_blocklist),
    torch.ops.aten.div.Tensor: partial(guard_aten, aten_div_Tensor_blocklist),
    torch.ops.aten.mul.Tensor: partial(guard_aten, aten_mul_Tensor_blocklist),
    torch.ops.aten.slice.Tensor: partial(guard_aten, aten_slice_Tensor_blocklist),
    torch.ops.aten.native_layer_norm.default: partial(guard_aten, aten_native_layer_norm_default_blocklist),
    torch.ops.aten.sub.Tensor: partial(guard_aten, aten_sub_Tensor_blocklist),
    torch.ops.aten.exp.default: partial(guard_aten, aten_exp_default_blocklist),
    torch.ops.aten.split.Tensor: partial(guard_aten, aten_split_Tensor_blocklist),
    torch.ops.aten.t.default: partial(guard_aten, aten_t_default_blocklist),
    torch.ops.aten.ones.default: partial(guard_aten, aten_ones_default_blocklist),
    torch.ops.aten.where.self: partial(guard_aten, aten_where_self_blocklist),
    torch.ops.aten.empty.memory_format: partial(guard_aten, aten_empty_memory_format_blocklist),
    # Add for pass CLIP eval
    torch.ops.aten._to_copy.default: partial(guard_aten, aten__to_copy_default_blocklist),
}


GROUP1 = [
    torch.ops.aten.eq.Scalar,
    torch.ops.aten.lt.Scalar,
    torch.ops.aten.le.Scalar,
    torch.ops.aten.gt.Scalar,
    torch.ops.aten.ge.Scalar,
    torch.ops.aten.ne.Scalar,
    torch.ops.aten.argmax.default,
    torch.ops.aten.argmin.default,
    torch.ops.aten.floor.default,
    torch.ops.aten.zeros_like.default,
]
GROUP2 = [
    torch.ops.aten.addmm.default,
    torch.ops.aten.bmm.default,
    torch.ops.aten.linear.default,
    torch.ops.aten.mm.default,
]
GROUP3 = [
    torch.ops.aten.abs.default,
    torch.ops.aten.acos.default,
    torch.ops.aten.acosh.default,
    torch.ops.aten.asin.default,
    torch.ops.aten.asinh.default,
    torch.ops.aten.atan.default,
    torch.ops.aten.atanh.default,
    torch.ops.aten.clamp.default,
    torch.ops.aten.cos.default,
    torch.ops.aten.cosh.default,
]
GROUP4 = [
    torch.ops.aten.erf.default,
    torch.ops.aten.exp.default,
    torch.ops.aten.expm1.default,
    torch.ops.aten.floor.default,
    torch.ops.aten.gelu.default,
    torch.ops.aten.hardtanh.default,
    torch.ops.aten.isinf.default,
    torch.ops.aten.isnan.default,
    torch.ops.aten.log.default,
    torch.ops.aten.log10.default,
]
GROUP5 = [
    torch.ops.aten.log1p.default,
    torch.ops.aten.log2.default,
    torch.ops.aten.logical_not.default,
    torch.ops.aten.neg.default,
    torch.ops.aten.reciprocal.default,
    torch.ops.aten.relu.default,
    torch.ops.aten.remainder.Scalar,
    torch.ops.aten.rsqrt.default,
    torch.ops.aten.sigmoid.default,
    torch.ops.aten.sign.default,
]
GROUP6 = [
    torch.ops.aten.sin.default,
    torch.ops.aten.sinh.default,
    torch.ops.aten.silu.default,
    torch.ops.aten._softmax.default,
    torch.ops.aten.sqrt.default,
    torch.ops.aten.tan.default,
    torch.ops.aten.tanh.default,
    torch.ops.aten.tril.default,
]
GROUP7 = [
    torch.ops.aten.add.Tensor,
    torch.ops.aten.atan2.default,
    torch.ops.aten.leaky_relu.default,
    torch.ops.aten.maximum.default,
    torch.ops.aten.minimum.default,
    torch.ops.aten.mul.Tensor,
    torch.ops.aten.pow.Tensor_Scalar,
    torch.ops.aten.rsub.Tensor,
    torch.ops.aten.sub.Tensor,
    torch.ops.aten.xlogy.Tensor,
]
GROUP8 = [
    torch.ops.aten.addcdiv.default,
    torch.ops.aten.addcmul.default,
    torch.ops.aten.where.self,
]
GROUP9 = [
    torch.ops.aten.mean.dim,
    torch.ops.aten.min.default,
    torch.ops.aten._adaptive_avg_pool2d.default,
    torch.ops.aten._log_softmax.default,
    torch.ops.aten.rsub.Scalar,
    torch.ops.aten.div.Tensor,
]
GROUP10 = [
    torch.ops.aten.native_layer_norm.default,
    torch.ops.aten.baddbmm.default,
    torch.ops.aten.embedding.default,
    torch.ops.aten.expand.default,
    torch.ops.aten.slice.Tensor,
    torch.ops.aten.repeat.default,
    torch.ops.aten.split.Tensor,
]
GROUP11 = [
    torch.ops.aten.clone.default,
    torch.ops.aten.ones.default,
    torch.ops.aten.full.default,
    torch.ops.aten._to_copy.default,
    torch.ops.aten.eq.Tensor,
    torch.ops.aten.arange.start,
    torch.ops.aten.arange.start_step,
    torch.ops.aten.constant_pad_nd.default,
]
GROUP12 = [
    torch.ops.aten.squeeze.dim,
    torch.ops.aten.squeeze.default,
    torch.ops.aten.unsqueeze.default,
    torch.ops.aten.transpose.int,
    torch.ops.aten.t.default,
    torch.ops.aten.permute.default,
    torch.ops.aten.view.default,
    torch.ops.aten._unsafe_view.default,
]

LOWERING_WHITE_LIST = []


def can_lowering_to_ttnn(node):
    if node.target not in LOWERING_WHITE_LIST:
        return False
    if node.target in GUARD:
        return GUARD[node.target](node)

    return True
