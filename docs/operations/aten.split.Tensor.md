### aten.split.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 14, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1       | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1       | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 384, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1      | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  | Done       | 1.0   | 0      |

