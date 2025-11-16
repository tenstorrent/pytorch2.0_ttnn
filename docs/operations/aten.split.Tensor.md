### aten.split.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1        | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1   | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1024, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 14, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1         | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1         | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 256, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 4096, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1 | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1        | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1   | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 64, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1  | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2      | Done     | Done       | 1.0   | 0      |
| 11 | Tensor<[768, 256]> self = ?,<br>int split_size = 256                        | Removed  | Done       | 1.0   | 0      |
| 12 | Tensor<[768]> self = ?,<br>int split_size = 256                             | Removed  | Fallback   | 1.0   | -3     |
| 13 | Tensor<[8, 384, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1        | Done     | Unknown    | N/A   | N/A    |

