### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 1]> self = ?,<br>Tensor other = 1e-05               | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 2560]> self = ?,<br>Tensor<[1, 33, 2560]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 33, 5120]> self = ?,<br>Tensor<[1, 33, 5120]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, 5120]> self = ?,<br>Tensor<[5120]> other = ?        | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 5120, 16]> self = ?,<br>Tensor<[1, 5120, 16]> other = ? | Done     | Unknown    | N/A   | N/A    |

