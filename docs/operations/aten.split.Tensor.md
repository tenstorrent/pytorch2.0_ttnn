### aten.split.Tensor
|    | ATen Input Variations                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1024, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 14, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 256, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 4096, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 64, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2      | None     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[768, 256]> self = ?,<br>int split_size = 256                        | None     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[768]> self = ?,<br>int split_size = 256                             | None     | N/A                 | N/A          | N/A               | N/A                |

