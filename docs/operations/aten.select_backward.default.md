### aten.select_backward.default
|    | ATen Input Variations                                                                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 768],<br>int dim = 1,<br>int index = 0 | None     | Fallback   | True  |
|  1 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 50, 768],<br>int dim = 1,<br>int index = 0  | None     | Fallback   | True  |

