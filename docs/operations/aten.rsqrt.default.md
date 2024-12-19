### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?       | Unknown  | Fallback   | 1        |     -1 |
|  1 | Tensor<[1, 10, 1]> self = ?      | Unknown  | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 1024, 1, 1]> self = ? | Done     | Done       | 0.999995 |      0 |
|  3 | Tensor<[1, 128, 1, 1]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  4 | Tensor<[1, 15, 1]> self = ?      | Unknown  | Done       | 1        |      0 |
|  5 | Tensor<[1, 2048, 1, 1]> self = ? | Done     | Done       | 0.999995 |      0 |
|  6 | Tensor<[1, 256, 1, 1]> self = ?  | Done     | Done       | 0.999996 |      0 |
|  7 | Tensor<[1, 512, 1, 1]> self = ?  | Done     | Done       | 0.999994 |      0 |
|  8 | Tensor<[1, 64, 1, 1]> self = ?   | Done     | Done       | 0.999991 |      0 |

