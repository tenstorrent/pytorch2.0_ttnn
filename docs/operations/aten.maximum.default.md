### aten.maximum.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[]> other = ?     | Removed  | Failed     | N/A   | N/A    |
|  3 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[]> other = ?     | Unknown  | Fallback   | 1.0   | -1     |

