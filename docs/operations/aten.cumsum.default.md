### aten.cumsum.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1                                             | Done     | Done       | 0.9999999123019047 | 0      |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] dtype = torch.float32 | None     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] dtype = torch.float32 | None     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 32]> self = ?,<br>int dim = -1                                            | Done     | Done       | 0.9999868886818619 | 0      |
|  4 | Tensor<[1, 45]> self = ?,<br>int dim = -1                                            | Unknown  | Done       | 0.9998849214396636 | 0      |
|  5 | Tensor<[1, 59]> self = ?,<br>int dim = 1                                             | Unknown  | Done       | 0.9999699782185184 | 0      |
|  6 | Tensor<[1, 5]> self = ?,<br>int dim = -1                                             | Unknown  | Done       | 0.9999992758433656 | 0      |
|  7 | Tensor<[1, 60]> self = ?,<br>int dim = 1                                             | Unknown  | Done       | 0.9999873449611172 | 0      |
|  8 | Tensor<[1, s0]> self = ?,<br>int dim = -1                                            | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1                                        | Unknown  | Unknown    | N/A                | N/A    |

