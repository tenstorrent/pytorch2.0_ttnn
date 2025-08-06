### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[12, 1, 1]> self = ? | Removed  | Done       | 0.9999940070362978 | 0      |
|  1 | Tensor<[16, 1, 1]> self = ? | Removed  | Done       | 0.9999704292850197 | 0      |
|  2 | Tensor<[160]> self = ?      | Unknown  | Done       | 0.9999535203227093 | 0      |
|  3 | Tensor<[16384, 3]> self = ? | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor<[24, 1, 1]> self = ? | Removed  | Done       | 0.9999977599032482 | 0      |
|  5 | Tensor<[3, 1, 1]> self = ?  | Removed  | Done       | 0.9999995024121492 | 0      |
|  6 | Tensor<[32, 1, 1]> self = ? | Removed  | Done       | 0.9999714226216067 | 0      |
|  7 | Tensor<[3234, 1]> self = ?  | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor<[4, 1, 1]> self = ?  | Removed  | Done       | 0.9999680814282008 | 0      |
|  9 | Tensor<[6, 1, 1]> self = ?  | Removed  | Done       | 0.9998698725623045 | 0      |
| 10 | Tensor<[8, 1, 1]> self = ?  | Removed  | Done       | 0.9999925367427515 | 0      |
| 11 | Tensor<[8732, 1]> self = ?  | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[]> self = ?         | Removed  | Done       | 1.0                | 0      |

