### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 38, 38]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |
|  1 | Tensor<[1, 24, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 32, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |
|  3 | Tensor<[16, 6, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Unknown    | N/A   |
|  4 | Tensor<[16, 8, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |
|  5 | Tensor<[4, 12, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Unknown    | N/A   |
|  6 | Tensor<[4, 16, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |
|  7 | Tensor<[64, 3, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Unknown    | N/A   |
|  8 | Tensor<[64, 4, 64, 1]> self = ?,<br>number min = 1e-12 | None     | Fallback   | True  |

