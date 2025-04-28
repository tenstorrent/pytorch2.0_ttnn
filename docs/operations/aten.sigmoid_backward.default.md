### aten.sigmoid_backward.default
|    | ATen Input Variations                                                            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 256, 256]> grad_output = ?,<br>Tensor<[1, 1, 256, 256]> output = ? | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 120, 14, 14]> grad_output = ?,<br>Tensor<[1, 120, 14, 14]> output = ? | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 184, 7, 7]> grad_output = ?,<br>Tensor<[1, 184, 7, 7]> output = ?     | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 200, 7, 7]> grad_output = ?,<br>Tensor<[1, 200, 7, 7]> output = ?     | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 240, 14, 14]> grad_output = ?,<br>Tensor<[1, 240, 14, 14]> output = ? | None     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 480, 7, 7]> grad_output = ?,<br>Tensor<[1, 480, 7, 7]> output = ?     | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 50, 3072]> grad_output = ?,<br>Tensor<[1, 50, 3072]> output = ?       | None     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 672, 7, 7]> grad_output = ?,<br>Tensor<[1, 672, 7, 7]> output = ?     | None     | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 72, 28, 28]> grad_output = ?,<br>Tensor<[1, 72, 28, 28]> output = ?   | None     | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 960, 3, 3]> grad_output = ?,<br>Tensor<[1, 960, 3, 3]> output = ?     | None     | Fallback   |     1 |     -1 |
| 10 | Tensor<[2, 7, 2048]> grad_output = ?,<br>Tensor<[2, 7, 2048]> output = ?         | None     | Fallback   |     1 |     -1 |

