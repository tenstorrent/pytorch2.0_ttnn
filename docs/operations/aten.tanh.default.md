### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.998399 |      0 |
|  1 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | 0.998432 |      0 |
|  2 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       | 0.998456 |      0 |
|  3 | Tensor<[1, 12, 3072]> self = ? | Done     | Done       | 0.998432 |      0 |
|  4 | Tensor<[1, 14, 3072]> self = ? | Done     | Done       | 0.998438 |      0 |
|  5 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.998422 |      0 |
|  6 | Tensor<[1, 32, 6144]> self = ? | Unknown  | Done       | 0.998429 |      0 |
|  7 | Tensor<[1, 45, 3072]> self = ? | Unknown  | Done       | 0.998431 |      0 |
|  8 | Tensor<[1, 5, 4096]> self = ?  | Unknown  | Done       | 0.998457 |      0 |
|  9 | Tensor<[1, 7, 3072]> self = ?  | Done     | Done       | 0.998457 |      0 |
| 10 | Tensor<[1, 768]> self = ?      | Done     | Done       | 0.998321 |      0 |
| 11 | Tensor<[1, 9, 128]> self = ?   | Done     | Done       | 0.99855  |      0 |
| 12 | Tensor<[1, 9, 16384]> self = ? | Done     | Done       | 0.998434 |      0 |
| 13 | Tensor<[1, 9, 3072]> self = ?  | Done     | Done       | 0.998434 |      0 |
| 14 | Tensor<[1, 9, 4096]> self = ?  | Done     | Done       | 0.998433 |      0 |
| 15 | Tensor<[1, 9, 8192]> self = ?  | Done     | Done       | 0.998438 |      0 |

