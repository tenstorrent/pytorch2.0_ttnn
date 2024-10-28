### aten.maximum.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[]> other = ?     | None     | Fallback   | True  |
|  3 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[]> other = ?     | None     | Fallback   | True  |

