### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1]> self = ?       | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 10, 1]> self = ?      | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1024, 1, 1]> self = ? | Removed  | Done       | 0.9999991030870395 | 0      |
|  3 | Tensor<[1, 128, 1, 1]> self = ?  | Removed  | Done       | 0.9999950235240824 | 0      |
|  4 | Tensor<[1, 15, 1]> self = ?      | Unknown  | Done       | 0.9999943865148672 | 0      |
|  5 | Tensor<[1, 2048, 1, 1]> self = ? | Removed  | Done       | 0.9999943648628117 | 0      |
|  6 | Tensor<[1, 256, 1, 1]> self = ?  | Removed  | Done       | 0.9999961671953982 | 0      |
|  7 | Tensor<[1, 32, 1]> self = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 512, 1, 1]> self = ?  | Removed  | Done       | 0.9999945654038421 | 0      |
|  9 | Tensor<[1, 64, 1, 1]> self = ?   | Removed  | Done       | 0.9999959738361062 | 0      |

