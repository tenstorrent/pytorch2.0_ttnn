### aten.embedding_dense_backward.default
|    | ATen Input Variations                                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> grad_output = ?,<br>Tensor<[1, 50]> indices = ?,<br>int num_weights = 50,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False  | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 7, 512]> grad_output = ?,<br>Tensor<[1, 7]> indices = ?,<br>int num_weights = 77,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False    | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[2, 7, 512]> grad_output = ?,<br>Tensor<[2, 7]> indices = ?,<br>int num_weights = 49408,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False | None     | Fallback   |     1 |     -1 |

