### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 9, 9]> self = ?                                                            | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1280]> self = ?                                                                | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 9, 9]> self = ?                                                            | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1, 9, 1024]> self = ?                                                             | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[1, 9, 128]> self = ?                                                              | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  7 | Tensor<[1, 9, 768]> self = ?                                                              | Removed  | Done       |     1 |      0 |

