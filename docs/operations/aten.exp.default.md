### aten.exp.default
|    | ATen Input Variations       | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[12, 1, 1]> self = ? | Done     | Done       | 0.9999887143752888 | -1     |
|  1 | Tensor<[16, 1, 1]> self = ? | Done     | Done       | 0.9999554061246013 | -1     |
|  2 | Tensor<[160]> self = ?      | Done     | Done       | 0.9999749659786294 | -1     |
|  3 | Tensor<[24, 1, 1]> self = ? | Done     | Done       | 0.9999896472402007 | -1     |
|  4 | Tensor<[3, 1, 1]> self = ?  | Done     | Done       | 0.9999996178972633 | -1     |
|  5 | Tensor<[32, 1, 1]> self = ? | Done     | Done       | 0.9999964605471738 | -1     |
|  6 | Tensor<[4, 1, 1]> self = ?  | Done     | Done       | 0.9999980663368915 | -1     |
|  7 | Tensor<[6, 1, 1]> self = ?  | Done     | Done       | 0.9999727896263988 | -1     |
|  8 | Tensor<[8, 1, 1]> self = ?  | Done     | Done       | 0.999973290467564  | -1     |
|  9 | Tensor<[8732, 1]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[]> self = ?         | None     | Fallback   | 1.0                | -1     |

