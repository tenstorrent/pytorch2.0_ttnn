### aten.cumsum.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1                                             | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 1,<br>Optional[int] dtype = torch.float32 | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 2,<br>Optional[int] dtype = torch.float32 | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32]> self = ?,<br>int dim = -1                                            | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 45]> self = ?,<br>int dim = -1                                            | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 59]> self = ?,<br>int dim = 1                                             | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 5]> self = ?,<br>int dim = -1                                             | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 60]> self = ?,<br>int dim = 1                                             | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, s0]> self = ?,<br>int dim = -1                                            | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1                                        | Unknown  | Unknown    | N/A   | N/A    |

