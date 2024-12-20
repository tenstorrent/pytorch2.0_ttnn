### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.998458 |      0 |
|  1 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.99847  |      0 |
|  2 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       | 0.998446 |      0 |
|  3 | Tensor<[1, 12, 3072]> self = ? | Done     | Done       | 0.99845  |      0 |
|  4 | Tensor<[1, 14, 3072]> self = ? | Done     | Done       | 0.998448 |      0 |
|  5 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.998462 |      0 |
|  6 | Tensor<[1, 32, 6144]> self = ? | Done     | Done       | 0.998435 |      0 |
|  7 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.99844  |      0 |
|  8 | Tensor<[1, 5, 4096]> self = ?  | Unknown  | Done       | 0.998447 |      0 |
|  9 | Tensor<[1, 7, 3072]> self = ?  | Done     | Done       | 0.998452 |      0 |
| 10 | Tensor<[1, 768]> self = ?      | Done     | Done       | 0.9985   |      0 |
| 11 | Tensor<[1, 9, 128]> self = ?   | Done     | Done       | 0.998499 |      0 |
| 12 | Tensor<[1, 9, 16384]> self = ? | Done     | Done       | 0.998443 |      0 |
| 13 | Tensor<[1, 9, 3072]> self = ?  | Done     | Done       | 0.998446 |      0 |
| 14 | Tensor<[1, 9, 4096]> self = ?  | Done     | Done       | 0.998419 |      0 |
| 15 | Tensor<[1, 9, 8192]> self = ?  | Done     | Done       | 0.998436 |      0 |

