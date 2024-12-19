### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[0, 1]> self = ?     | Unknown  | Fallback   | 1        |     -1 |
|  1 | Tensor<[12, 1, 1]> self = ? | Done     | Done       | 0.999964 |      0 |
|  2 | Tensor<[16, 1, 1]> self = ? | Done     | Done       | 0.999991 |      0 |
|  3 | Tensor<[160]> self = ?      | Unknown  | Done       | 0.99997  |      0 |
|  4 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | 0.999979 |      0 |
|  5 | Tensor<[3, 1, 1]> self = ?  | Done     | Done       | 0.99993  |      0 |
|  6 | Tensor<[32, 1, 1]> self = ? | Done     | Done       | 0.999962 |      0 |
|  7 | Tensor<[3234, 1]> self = ?  | Unknown  | Done       | 0.999969 |      0 |
|  8 | Tensor<[4, 1, 1]> self = ?  | Done     | Done       | 0.99985  |      0 |
|  9 | Tensor<[6, 1, 1]> self = ?  | Done     | Done       | 0.99997  |      0 |
| 10 | Tensor<[8, 1, 1]> self = ?  | Done     | Done       | 0.999973 |      0 |
| 11 | Tensor<[8732, 1]> self = ?  | Unknown  | Done       | 0.99997  |      0 |
| 12 | Tensor<[]> self = ?         | None     | Fallback   | 1        |     -1 |

