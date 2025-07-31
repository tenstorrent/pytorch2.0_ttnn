### aten.bmm.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 5120, 16]> self = ?,<br>Tensor<[1, 16, 1]> mat2 = ?   | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0, s1]> self = ?,<br>Tensor<[1, s1, 1]> mat2 = ?     | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 5120, 16]> self = ?,<br>Tensor<[32, 16, 1]> mat2 = ? | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, s0, s1]> self = ?,<br>Tensor<[32, s1, 1]> mat2 = ?   | Removed  | Unknown    | N/A   | N/A    |

