### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16]> self = ?,<br>int dim = 2        | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 16]> self = ?,<br>int dim = 3    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 5120]> self = ?,<br>int dim = 3  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, s1]> self = ?,<br>int dim = 3    | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, s1]> self = ?,<br>int dim = 2        | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 16]> self = ?,<br>int dim = 2       | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[32, 33, 16]> self = ?,<br>int dim = 3   | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[32, 33, 5120]> self = ?,<br>int dim = 3 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[32, 33, s2]> self = ?,<br>int dim = 3   | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, s1]> self = ?,<br>int dim = 2       | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[5120, 16, 1]> self = ?,<br>int dim = 3  | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[5120, 16]> self = ?,<br>int dim = 2     | Done     | Unknown    | N/A   | N/A    |

