### aten.split.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1          | Unknown  | Done       | 1.0   | 1      |
|  1 | Tensor<[1, 1, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1     | Unknown  | Done       | 1.0   | 1      |
|  2 | Tensor<[1, 14, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1           | Done     | Done       | 1.0   | 1      |
|  3 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1           | Done     | Done       | 1.0   | 1      |
|  4 | Tensor<[1, 256, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1          | Done     | Done       | 1.0   | 1      |
|  5 | Tensor<[1, 4096, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1   | Unknown  | Done       | 1.0   | 1      |
|  6 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1          | Unknown  | Done       | 1.0   | 1      |
|  7 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1     | Unknown  | Done       | 1.0   | 1      |
|  8 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2        | None     | Fallback   | 1.0   | -3     |
|  9 | Tensor<[1, s0*s1, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s0*s1, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1  | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s1*s2, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, s1*s2, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, s1*s2, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1  | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[768, 256]> self = ?,<br>int split_size = 256                          | None     | Fallback   | 1.0   | -3     |
| 15 | Tensor<[768]> self = ?,<br>int split_size = 256                               | None     | Fallback   | 1.0   | -3     |

