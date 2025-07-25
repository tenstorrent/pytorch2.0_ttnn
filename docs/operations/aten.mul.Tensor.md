### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 2560]> self = ?,<br>Tensor<[1, 33, 1]> other = ?           | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 2560]> self = ?,<br>Tensor<[2560]> other = ?               | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 5120, 16]> self = ?,<br>Tensor<[1, 33, 5120, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, 5120, 1]> self = ?,<br>Tensor<[1, 1, 5120, 16]> other = ?  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 33, 5120, 1]> self = ?,<br>Tensor<[1, 33, 1, 16]> other = ?    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 33, 5120, 1]> self = ?,<br>Tensor<[1, 33, 1, s1]> other = ?    | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 33, 5120, s1]> self = ?,<br>Tensor<[1, 33, 5120, 1]> other = ? | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 33, 5120]> self = ?,<br>Tensor<[1, 33, 5120]> other = ?        | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 33, 5120]> self = ?,<br>Tensor<[5120]> other = ?               | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 5120, 16]> self = ?,<br>Tensor<[1, 5120, 16]> other = ?        | Removed  | Unknown    | N/A   | N/A    |

