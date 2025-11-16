### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 16384, 256]> grad_output = ?,<br>Tensor<[1, 1, 16384, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 2, 4096, 256]> grad_output = ?,<br>Tensor<[1, 2, 4096, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 5, 1024, 256]> grad_output = ?,<br>Tensor<[1, 5, 1024, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 8, 256, 256]> grad_output = ?,<br>Tensor<[1, 8, 256, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16     | None     | Fallback   |     1 |     -1 |

