### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1]> self = ?       | Unknown  | Done       | 0.0                | 0      |
|  1 | Tensor<[1, 10, 1]> self = ?      | Unknown  | Done       | 0.9999977351508837 | 0      |
|  2 | Tensor<[1, 1024, 1, 1]> self = ? | Removed  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 128, 1, 1]> self = ?  | Removed  | Done       | 0.9999936873114142 | 0      |
|  4 | Tensor<[1, 15, 1]> self = ?      | Unknown  | Done       | 0.9999927020838906 | 0      |
|  5 | Tensor<[1, 2048, 1, 1]> self = ? | Removed  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 256, 1, 1]> self = ?  | Removed  | Done       | 0.9999939988520293 | 0      |
|  7 | Tensor<[1, 32, 1]> self = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 512, 1, 1]> self = ?  | Removed  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 64, 1, 1]> self = ?   | Removed  | Done       | 0.99999656724654   | 0      |

