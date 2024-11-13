### aten.silu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1280, 8, 8]> self = ?   | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1280, s0, s1]> self = ? | Unknown  | Unknown    | N/A   |
|  2 | Tensor<[1, 1280, s1, s2]> self = ? | Unknown  | Unknown    | N/A   |
|  3 | Tensor<[1, 1280]> self = ?         | Unknown  | Done       | True  |
|  4 | Tensor<[1, 1920, s1, s2]> self = ? | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 2560, 8, 8]> self = ?   | Unknown  | Done       | True  |
|  6 | Tensor<[1, 2560, s0, s1]> self = ? | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 32, 256, 256]> self = ? | Fallback | Done       | True  |
|  8 | Tensor<[1, 320, 64, 64]> self = ?  | Unknown  | Done       | True  |
|  9 | Tensor<[1, 320, s0, s1]> self = ?  | Unknown  | Unknown    | N/A   |
| 10 | Tensor<[1, 320, s1, s2]> self = ?  | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, 640, s0, s1]> self = ?  | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 640, s1, s2]> self = ?  | Unknown  | Unknown    | N/A   |
| 13 | Tensor<[1, 960, s1, s2]> self = ?  | Unknown  | Unknown    | N/A   |

