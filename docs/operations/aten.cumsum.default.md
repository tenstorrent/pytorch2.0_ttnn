### aten.cumsum.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1                                             | Done     | Done       | 0.9999902339446957 | 0      |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] dtype = torch.float32 | None     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] dtype = torch.float32 | None     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 32]> self = ?,<br>int dim = -1                                            | Done     | Done       | 0.999992901881656  | 0      |
|  4 | Tensor<[1, 45]> self = ?,<br>int dim = -1                                            | Unknown  | Done       | 0.9997705502216899 | 0      |
|  5 | Tensor<[1, 59]> self = ?,<br>int dim = 1                                             | Unknown  | Done       | 0.9998689572783247 | 0      |
|  6 | Tensor<[1, 5]> self = ?,<br>int dim = -1                                             | Unknown  | Done       | 0.9999969202123631 | 0      |
|  7 | Tensor<[1, 60]> self = ?,<br>int dim = 1                                             | Unknown  | Done       | 0.9994877347798705 | 0      |
|  8 | Tensor<[1, s0]> self = ?,<br>int dim = -1                                            | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1                                        | Unknown  | Unknown    | N/A                | N/A    |

