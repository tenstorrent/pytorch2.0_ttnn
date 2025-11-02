### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[12, 1, 1]> self = ? | Removed  | Done       | 0.9999897229384956 | 0      |
|  1 | Tensor<[16, 1, 1]> self = ? | Removed  | Done       | 0.9999981388156887 | 0      |
|  2 | Tensor<[160]> self = ?      | Unknown  | Done       | 0.9999946255473999 | 0      |
|  3 | Tensor<[16384, 3]> self = ? | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor<[24, 1, 1]> self = ? | Removed  | Done       | 0.9999947431166959 | 0      |
|  5 | Tensor<[3, 1, 1]> self = ?  | Removed  | Done       | 1.0                | 0      |
|  6 | Tensor<[32, 1, 1]> self = ? | Removed  | Done       | 0.9999996523027741 | 0      |
|  7 | Tensor<[3234, 1]> self = ?  | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor<[4, 1, 1]> self = ?  | Removed  | Done       | 1.0                | 0      |
|  9 | Tensor<[6, 1, 1]> self = ?  | Removed  | Done       | 0.9999996523121443 | 0      |
| 10 | Tensor<[8, 1, 1]> self = ?  | Removed  | Done       | 0.9999998062016302 | 0      |
| 11 | Tensor<[8732, 1]> self = ?  | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[]> self = ?         | Removed  | Done       | 1.0                | 0      |

