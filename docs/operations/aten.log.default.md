### aten.log.default
|    | ATen Input Variations        | Status   | Isolated   | PCC                  | Host   |
|---:|:-----------------------------|:---------|:-----------|:---------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?     | Done     | Unknown    | N/A                  | N/A    |
|  1 | Tensor<[1, 1]> self = ?      | Unknown  | Done       | 0.0                  | 0      |
|  2 | Tensor<[1, 2]> self = ?      | Unknown  | Unknown    | N/A                  | N/A    |
|  3 | Tensor<[1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A                  | N/A    |
|  4 | Tensor<[10, 10]> self = ?    | Unknown  | Done       | -0.18738580027428464 | 0      |
|  5 | Tensor<[15, 15]> self = ?    | Unknown  | Done       | -0.22294320093744074 | 0      |

