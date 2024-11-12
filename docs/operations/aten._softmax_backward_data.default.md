### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 16384, 256]> grad_output = ?,<br>Tensor<[1, 1, 16384, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[1, 12, 197, 197]> grad_output = ?,<br>Tensor<[1, 12, 197, 197]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 197, 197]> grad_output = ?,<br>Tensor<[1, 16, 197, 197]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 2, 4096, 256]> grad_output = ?,<br>Tensor<[1, 2, 4096, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 5, 1024, 256]> grad_output = ?,<br>Tensor<[1, 5, 1024, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16   | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 8, 256, 256]> grad_output = ?,<br>Tensor<[1, 8, 256, 256]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16     | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[12, 50, 50]> grad_output = ?,<br>Tensor<[12, 50, 50]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16             | None     | Fallback   | True  |
|  7 | Tensor<[16, 7, 7]> grad_output = ?,<br>Tensor<[16, 7, 7]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16                 | None     | Fallback   | True  |

