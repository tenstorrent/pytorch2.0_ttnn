### aten.silu.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 128, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 128, s1, s2]> self = ?                               | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 256, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 256, s0, s1]> self = ?                               | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 256, s1, s2]> self = ?                               | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 32, 256, 256]> self = ?                              | Unknown  | Done       | 0.9999823979497721 | 0      |
|  6 | Tensor<[1, 32, s0, s1]> self = ?                                | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 320, 64, 64]> self = ?                               | Done     | Done       | 0.9999823906612312 | 0      |
|  8 | Tensor<[1, 512, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 512, s1, s2]> self = ?                               | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 64, ((s1 - 1)//2) + 1, ((s2 - 1)//2) + 1]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 64, s0, s1]> self = ?                                | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 64, s1, s2]> self = ?                                | Unknown  | Unknown    | N/A                | N/A    |

