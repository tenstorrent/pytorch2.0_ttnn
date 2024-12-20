### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[0, 1]> self = ?     | Unknown  | Fallback   | 1        |     -1 |
|  1 | Tensor<[12, 1, 1]> self = ? | Done     | Done       | 0.999921 |      0 |
|  2 | Tensor<[16, 1, 1]> self = ? | Done     | Done       | 0.999978 |      0 |
|  3 | Tensor<[160]> self = ?      | Unknown  | Done       | 0.999955 |      0 |
|  4 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | 0.999968 |      0 |
|  5 | Tensor<[3, 1, 1]> self = ?  | Done     | Done       | 0.999747 |      0 |
|  6 | Tensor<[32, 1, 1]> self = ? | Done     | Done       | 0.999963 |      0 |
|  7 | Tensor<[3234, 1]> self = ?  | Unknown  | Done       | 0.999972 |      0 |
|  8 | Tensor<[4, 1, 1]> self = ?  | Done     | Done       | 0.999854 |      0 |
|  9 | Tensor<[6, 1, 1]> self = ?  | Done     | Done       | 0.999985 |      0 |
| 10 | Tensor<[8, 1, 1]> self = ?  | Done     | Done       | 0.999916 |      0 |
| 11 | Tensor<[8732, 1]> self = ?  | Unknown  | Done       | 0.999885 |      0 |
| 12 | Tensor<[]> self = ?         | None     | Fallback   | 1        |     -1 |

