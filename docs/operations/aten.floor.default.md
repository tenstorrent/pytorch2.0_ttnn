### aten.floor.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?                | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 42]> self = ? | Removed  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 32, 1]> self = ? | Removed  | Done       | 1.0   | 0      |

