### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 38, 38]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 0.9999999999999989 | 0      |
|  1 | Tensor<[1, 1]> self = ?,<br>number min = 1e-12         | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 24, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 32, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 1.0                | 0      |
|  4 | Tensor<[16, 6, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 1.0                | 0      |
|  5 | Tensor<[16, 8, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 1.0                | 0      |
|  6 | Tensor<[4, 12, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 1.0                | 0      |
|  7 | Tensor<[4, 16, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 1.0                | 0      |
|  8 | Tensor<[64, 3, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 1.0                | 0      |
|  9 | Tensor<[64, 4, 64, 1]> self = ?,<br>number min = 1e-12 | Removed  | Done       | 0.9999999999999982 | 0      |

