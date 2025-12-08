### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1, 32, 32]> self = ?,<br>Tensor<[32, 1, 1, 32]> other = ?      | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 32, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 32, 32, 128]> self = ?,<br>Tensor<[32, 32, 32, 128]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 32, 4096]> self = ?,<br>Tensor<[32, 32, 4096]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 8, 32, 128]> self = ?,<br>Tensor<[32, 8, 32, 128]> other = ?   | Done     | Unknown    | N/A   | N/A    |

