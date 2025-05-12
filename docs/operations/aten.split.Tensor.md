### aten.split.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  | Done       | 1.0   | -2     |
|  1 | Tensor<[1, 1, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  | Done       | 1.0   | -3     |
|  2 | Tensor<[1, 14, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1       | Done     | Done       | 1.0   | -2     |
|  3 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1       | Done     | Done       | 1.0   | -2     |
|  4 | Tensor<[1, 384, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1      | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  | Done       | 1.0   | -2     |
|  6 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  | Done       | 1.0   | -3     |
|  7 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2    | Done     | Done       | 1.0   | -3     |
|  8 | Tensor<[768, 256]> self = ?,<br>int split_size = 256                      | Unknown  | Done       | 1.0   | -3     |
|  9 | Tensor<[768]> self = ?,<br>int split_size = 256                           | Unknown  | Fallback   | 1.0   | -3     |

