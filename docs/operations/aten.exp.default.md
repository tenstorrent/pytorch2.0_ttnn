### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 1, 1]> self = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[16, 1, 1]> self = ? | Done     | Done       | 0.999991 |      0 |
|  2 | Tensor<[160]> self = ?      | Unknown  | Done       | 0.999969 |      0 |
|  3 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[3, 1, 1]> self = ?  | Done     | Done       | 0.999997 |      0 |
|  5 | Tensor<[32, 1, 1]> self = ? | Done     | Done       | 0.999963 |      0 |
|  6 | Tensor<[4, 1, 1]> self = ?  | Done     | Done       | 0.999998 |      0 |
|  7 | Tensor<[6, 1, 1]> self = ?  | Done     | Done       | 0.999981 |      0 |
|  8 | Tensor<[8, 1, 1]> self = ?  | Done     | Done       | 0.999982 |      0 |
|  9 | Tensor<[]> self = ?         | None     | Fallback   | 1        |     -1 |

