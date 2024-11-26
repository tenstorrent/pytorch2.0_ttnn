### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   |
|---:|:----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[0, 1]> self = ?     | Unknown  | Fallback   | True  |
|  1 | Tensor<[12, 1, 1]> self = ? | Removed  | Done       | True  |
|  2 | Tensor<[16, 1, 1]> self = ? | Removed  | Done       | True  |
|  3 | Tensor<[160]> self = ?      | Unknown  | Done       | True  |
|  4 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | True  |
|  5 | Tensor<[3, 1, 1]> self = ?  | Removed  | Done       | True  |
|  6 | Tensor<[32, 1, 1]> self = ? | Done     | Done       | True  |
|  7 | Tensor<[3234, 1]> self = ?  | Unknown  | Done       | True  |
|  8 | Tensor<[4, 1, 1]> self = ?  | Removed  | Done       | True  |
|  9 | Tensor<[6, 1, 1]> self = ?  | Removed  | Done       | True  |
| 10 | Tensor<[8, 1, 1]> self = ?  | Removed  | Done       | True  |
| 11 | Tensor<[8732, 1]> self = ?  | Unknown  | Done       | True  |
| 12 | Tensor<[]> self = ?         | None     | Fallback   | True  |

