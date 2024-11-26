### aten.gelu_backward.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 512]> grad_output = ?,<br>Tensor<[1, 1024, 512]> self = ?   | None     | Fallback   | True  |
|  1 | Tensor<[1, 1024, 640]> grad_output = ?,<br>Tensor<[1, 1024, 640]> self = ?   | None     | Fallback   | True  |
|  2 | Tensor<[1, 16384, 128]> grad_output = ?,<br>Tensor<[1, 16384, 128]> self = ? | None     | Fallback   | True  |
|  3 | Tensor<[1, 196, 3072]> grad_output = ?,<br>Tensor<[1, 196, 3072]> self = ?   | None     | Fallback   | True  |
|  4 | Tensor<[1, 197, 3072]> grad_output = ?,<br>Tensor<[1, 197, 3072]> self = ?   | None     | Fallback   | True  |
|  5 | Tensor<[1, 197, 4096]> grad_output = ?,<br>Tensor<[1, 197, 4096]> self = ?   | None     | Fallback   | True  |
|  6 | Tensor<[1, 256, 1024]> grad_output = ?,<br>Tensor<[1, 256, 1024]> self = ?   | None     | Fallback   | True  |
|  7 | Tensor<[1, 256, 256]> grad_output = ?,<br>Tensor<[1, 256, 256]> self = ?     | None     | Fallback   | True  |
|  8 | Tensor<[1, 4096, 256]> grad_output = ?,<br>Tensor<[1, 4096, 256]> self = ?   | None     | Fallback   | True  |
|  9 | Tensor<[1, 768, 384]> grad_output = ?,<br>Tensor<[1, 768, 384]> self = ?     | None     | Fallback   | True  |

