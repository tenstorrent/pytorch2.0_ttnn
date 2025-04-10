### aten.clone.default
|    | ATen Input Variations                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 512]> self = ?                                                                   | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 128]> self = ?                                                                         | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1, 256, 256]> self = ?                                                                    | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 512]> self = ?                                                                    | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[1, 64, 12, 12]> self = ?                                                                  | Removed  | Done       |     1 |      0 |

