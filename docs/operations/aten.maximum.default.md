### aten.maximum.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[]> other = ?     | Removed  | Failed     | N/A   |
|  3 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor other = ?         | Done     | Unknown    | N/A   |
|  4 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[]> other = ?     | Unknown  | Fallback   | True  |

