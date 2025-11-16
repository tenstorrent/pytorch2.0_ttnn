### aten.minimum.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2]> self = ?,<br>Tensor<[1, 2]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?       | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?       | Unknown  | Done       | 1.0   | 0      |

