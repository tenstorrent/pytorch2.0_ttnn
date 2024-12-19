### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.998428 |      0 |
|  1 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.998475 |      0 |
|  2 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       | 0.998468 |      0 |
|  3 | Tensor<[1, 12, 3072]> self = ? | Done     | Done       | 0.998432 |      0 |
|  4 | Tensor<[1, 14, 3072]> self = ? | Done     | Done       | 0.998455 |      0 |
|  5 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.99844  |      0 |
|  6 | Tensor<[1, 32, 6144]> self = ? | Done     | Done       | 0.998432 |      0 |
|  7 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.998438 |      0 |
|  8 | Tensor<[1, 5, 4096]> self = ?  | Unknown  | Done       | 0.998449 |      0 |
|  9 | Tensor<[1, 7, 3072]> self = ?  | Done     | Done       | 0.998436 |      0 |
| 10 | Tensor<[1, 768]> self = ?      | Done     | Done       | 0.998426 |      0 |
| 11 | Tensor<[1, 9, 128]> self = ?   | Done     | Done       | 0.998499 |      0 |
| 12 | Tensor<[1, 9, 16384]> self = ? | Done     | Done       | 0.998439 |      0 |
| 13 | Tensor<[1, 9, 3072]> self = ?  | Done     | Done       | 0.998457 |      0 |
| 14 | Tensor<[1, 9, 4096]> self = ?  | Done     | Done       | 0.998442 |      0 |
| 15 | Tensor<[1, 9, 8192]> self = ?  | Done     | Done       | 0.998436 |      0 |

