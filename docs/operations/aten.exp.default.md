### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 1, 1]> self = ? | Done     | Done       | 0.99999  |      0 |
|  1 | Tensor<[16, 1, 1]> self = ? | Done     | Done       | 0.999974 |      0 |
|  2 | Tensor<[160]> self = ?      | Done     | Done       | 0.999983 |      0 |
|  3 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | 0.999972 |      0 |
|  4 | Tensor<[3, 1, 1]> self = ?  | Done     | Done       | 0.999982 |      0 |
|  5 | Tensor<[32, 1, 1]> self = ? | Done     | Done       | 0.999983 |      0 |
|  6 | Tensor<[4, 1, 1]> self = ?  | Done     | Done       | 0.999977 |      0 |
|  7 | Tensor<[6, 1, 1]> self = ?  | Done     | Done       | 0.999992 |      0 |
|  8 | Tensor<[8, 1, 1]> self = ?  | Done     | Done       | 0.999988 |      0 |
|  9 | Tensor<[]> self = ?         | None     | Fallback   | 1        |     -1 |

