### aten.cos.default
|    | ATen Input Variations            | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 160]> self = ?        | Done     | Done       | 0.9999882607646311 | 0      |
|  1 | Tensor<[1, 23, 40, 64]> self = ? | Done     | Done       | 0.9999924108688564 | 0      |
|  2 | Tensor<[1, 32, 128]> self = ?    | Unknown  | Done       | 0.9999926742802123 | 0      |
|  3 | Tensor<[1, 7, 64]> self = ?      | Unknown  | Unknown    | N/A                | N/A    |

