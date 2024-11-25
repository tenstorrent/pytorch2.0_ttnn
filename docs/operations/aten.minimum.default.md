### aten.minimum.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                     | Done     | Done       | True  |
|  1 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                 | Done     | Done       | True  |
|  2 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                 | Done     | Done       | True  |
|  3 | Tensor<[17, 17]> self = ?,<br>Tensor<[17, 17]> other = ?                 | Unknown  | Done       | True  |
|  4 | Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                     | Unknown  | Done       | True  |
|  5 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   |

