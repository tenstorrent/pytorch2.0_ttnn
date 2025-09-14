### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1]> self = ?       | Unknown  | Done       | 0.0                | 0      |
|  1 | Tensor<[1, 10, 1]> self = ?      | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1024, 1, 1]> self = ? | Removed  | Done       | 0.9999998682927774 | 0      |
|  3 | Tensor<[1, 128, 1, 1]> self = ?  | Removed  | Done       | 0.9999966314301005 | 0      |
|  4 | Tensor<[1, 15, 1]> self = ?      | Unknown  | Done       | 0.9999920698136395 | 0      |
|  5 | Tensor<[1, 2048, 1, 1]> self = ? | Removed  | Done       | 0.9999949132882158 | 0      |
|  6 | Tensor<[1, 256, 1, 1]> self = ?  | Removed  | Done       | 0.9999950737362349 | 0      |
|  7 | Tensor<[1, 32, 1]> self = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 512, 1, 1]> self = ?  | Removed  | Done       | 0.9999957145236434 | 0      |
|  9 | Tensor<[1, 64, 1, 1]> self = ?   | Removed  | Done       | 0.9999947771618419 | 0      |

