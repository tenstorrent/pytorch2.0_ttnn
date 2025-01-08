### aten.silu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?   | Unknown  | Done       | 0.9999824795953417 | 0      |
|  1 | Tensor<[1, 1280, s0, s1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1280, s1, s2]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 1280]> self = ?         | Unknown  | Done       | 0.9999829731962186 | 0      |
|  4 | Tensor<[1, 1920, s1, s2]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 2560, 8, 8]> self = ?   | Unknown  | Done       | 0.9999824481315113 | 0      |
|  6 | Tensor<[1, 2560, s0, s1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 32, 256, 256]> self = ? | Done     | Done       | 0.9999824019041996 | 0      |
|  8 | Tensor<[1, 320, 64, 64]> self = ?  | Unknown  | Done       | 0.9999823273810333 | 0      |
|  9 | Tensor<[1, 320, s0, s1]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 320, s1, s2]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 640, s0, s1]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 640, s1, s2]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 960, s1, s2]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |

