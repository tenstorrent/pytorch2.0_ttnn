### aten.squeeze.dim
|    | ATen Input Variations                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 25088]> self = ?,<br>int dim = 0    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1 | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 14, 1]> self = ?,<br>int dim = -1      | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 25, 1]> self = ?,<br>int dim = -1      | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[16384, 1]> self = ?,<br>int dim = 1       | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[8, 384, 1]> self = ?,<br>int dim = -1     | Done     | Unknown    | N/A   | N/A    |

