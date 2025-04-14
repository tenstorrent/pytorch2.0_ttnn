### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 1, 1]> self = ? | Done     | Done       | 0.999974 |      0 |
|  1 | Tensor<[16, 1, 1]> self = ? | Done     | Done       | 0.999991 |      0 |
|  2 | Tensor<[160]> self = ?      | Done     | Done       | 0.99996  |      0 |
|  3 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | 0.999985 |      0 |
|  4 | Tensor<[3, 1, 1]> self = ?  | Done     | Done       | 1        |      0 |
|  5 | Tensor<[32, 1, 1]> self = ? | Done     | Done       | 0.999967 |      0 |
|  6 | Tensor<[4, 1, 1]> self = ?  | Done     | Done       | 1        |      0 |
|  7 | Tensor<[6, 1, 1]> self = ?  | Done     | Done       | 0.999962 |      0 |
|  8 | Tensor<[8, 1, 1]> self = ?  | Done     | Done       | 0.999996 |      0 |
|  9 | Tensor<[]> self = ?         | None     | Fallback   | 1        |     -1 |

