### aten.rsqrt.default
|    | ATen Input Variations            | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1]> self = ?       | Unknown  | Done       | 0.0                | 0      |
|  1 | Tensor<[1, 10, 1]> self = ?      | Unknown  | Done       | 0.9999827232557152 | 0      |
|  2 | Tensor<[1, 1024, 1, 1]> self = ? | Removed  | Done       | 0.9999941103453499 | 0      |
|  3 | Tensor<[1, 128, 1, 1]> self = ?  | Removed  | Done       | 0.9999960660672417 | 0      |
|  4 | Tensor<[1, 15, 1]> self = ?      | Unknown  | Done       | 0.9999948444170371 | 0      |
|  5 | Tensor<[1, 2048, 1, 1]> self = ? | Removed  | Done       | 0.999994460678461  | 0      |
|  6 | Tensor<[1, 256, 1, 1]> self = ?  | Removed  | Done       | 0.9999945612153546 | 0      |
|  7 | Tensor<[1, 32, 1]> self = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 512, 1, 1]> self = ?  | Removed  | Done       | 0.9999953362514562 | 0      |
|  9 | Tensor<[1, 64, 1, 1]> self = ?   | Removed  | Done       | 0.9999931513415758 | 0      |

