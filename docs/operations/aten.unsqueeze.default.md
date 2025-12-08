### aten.unsqueeze.default
|    | ATen Input Variations                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 128]> self = ?,<br>int dim = 1     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 32]> self = ?,<br>int dim = 1      | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = 1          | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64]> self = ?,<br>int dim = 2          | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 1, 32]> self = ?,<br>int dim = 2      | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 32]> self = ?,<br>int dim = 0         | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 32]> self = ?,<br>int dim = 1         | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 8, 32, 128]> self = ?,<br>int dim = 2 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[64]> self = ?,<br>int dim = 0             | Done     | Unknown    | N/A   | N/A    |

