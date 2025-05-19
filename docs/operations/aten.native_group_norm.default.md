### aten.native_group_norm.default
|    | ATen Input Variations                                                                                                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 320, 64, 64]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>int N = 1,<br>int C = 320,<br>int HxW = 4096,<br>int group = 32,<br>float eps = 1e-05 | None     | Fallback   |     1 |      0 |

