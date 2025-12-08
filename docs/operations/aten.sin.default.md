### aten.sin.default
|    | ATen Input Variations            | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 160]> self = ?        | Done     | Done       | 0.9999971329324768 | 0      |
|  1 | Tensor<[1, 23, 40, 64]> self = ? | Done     | Done       | 0.9999970885684333 | 0      |
|  2 | Tensor<[1, 32, 128]> self = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 7, 64]> self = ?      | Unknown  | Unknown    | N/A                | N/A    |

