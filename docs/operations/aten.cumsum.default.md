### aten.cumsum.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1                                             | Done     | Done       | 0.9999624632886693 | 1      |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] dtype = torch.float32 | None     | Fallback   | 1.0                | -1     |
|  2 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] dtype = torch.float32 | None     | Fallback   | 1.0                | -1     |
|  3 | Tensor<[1, 32]> self = ?,<br>int dim = -1                                            | Done     | Done       | 0.9999794101067873 | 1      |
|  4 | Tensor<[1, 45]> self = ?,<br>int dim = -1                                            | Unknown  | Done       | 0.9999903732725718 | 1      |
|  5 | Tensor<[1, 59]> self = ?,<br>int dim = 1                                             | Unknown  | Done       | 0.999983370800759  | 1      |
|  6 | Tensor<[1, 5]> self = ?,<br>int dim = -1                                             | Unknown  | Done       | 0.9999952014831228 | 1      |
|  7 | Tensor<[1, 60]> self = ?,<br>int dim = 1                                             | Unknown  | Done       | 0.9998882945246725 | 1      |
|  8 | Tensor<[1, s0]> self = ?,<br>int dim = -1                                            | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1                                        | Unknown  | Unknown    | N/A                | N/A    |

