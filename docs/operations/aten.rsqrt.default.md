### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1]> self = ?       | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 10, 1]> self = ?      | Done     | Done       | True  |
|  2 | Tensor<[1, 1024, 1, 1]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 128, 1, 1]> self = ?  | Done     | Done       | True  |
|  4 | Tensor<[1, 15, 1]> self = ?      | Done     | Done       | True  |
|  5 | Tensor<[1, 2048, 1, 1]> self = ? | Done     | Done       | True  |
|  6 | Tensor<[1, 256, 1, 1]> self = ?  | Done     | Done       | True  |
|  7 | Tensor<[1, 512, 1, 1]> self = ?  | Done     | Done       | True  |
|  8 | Tensor<[1, 64, 1, 1]> self = ?   | Done     | Done       | True  |

