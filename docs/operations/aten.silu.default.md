### aten.silu.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 128, (((s1 - 1)//2)) + 1, (((s2 - 1)//2)) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 128, s1, s2]> self = ?                                   | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1280, 16, 16]> self = ?                                  | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 1280, 32, 32]> self = ?                                  | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 1280, 8, 8]> self = ?                                    | Done     | Done       | 0.9999882925407249 | 0      |
|  5 | Tensor<[1, 1280]> self = ?                                          | Done     | Done       | 0.9999873068113269 | 0      |
|  6 | Tensor<[1, 1920, 16, 16]> self = ?                                  | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1920, 32, 32]> self = ?                                  | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 256, (((s1 - 1)//2)) + 1, (((s2 - 1)//2)) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 256, s0, s1]> self = ?                                   | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 256, s1, s2]> self = ?                                   | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 2560, 16, 16]> self = ?                                  | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 2560, 8, 8]> self = ?                                    | Done     | Done       | 0.9999880961698088 | 0      |
| 13 | Tensor<[1, 32, 11008]> self = ?                                     | Unknown  | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 32, 256, 256]> self = ?                                  | Unknown  | Done       | 0.9999882858915076 | 0      |
| 15 | Tensor<[1, 32, s0, s1]> self = ?                                    | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 320, 32, 32]> self = ?                                   | Done     | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, 320, 64, 64]> self = ?                                   | Done     | Done       | 0.9999882863664363 | 0      |
| 18 | Tensor<[1, 512, (((s1 - 1)//2)) + 1, (((s2 - 1)//2)) + 1]> self = ? | Unknown  | Unknown    | N/A                | N/A    |
| 19 | Tensor<[1, 512, s1, s2]> self = ?                                   | Unknown  | Unknown    | N/A                | N/A    |
| 20 | Tensor<[1, 64, (((s1 - 1)//2)) + 1, (((s2 - 1)//2)) + 1]> self = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 21 | Tensor<[1, 64, s0, s1]> self = ?                                    | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 64, s1, s2]> self = ?                                    | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 640, 16, 16]> self = ?                                   | Done     | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 640, 32, 32]> self = ?                                   | Done     | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 640, 64, 64]> self = ?                                   | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 960, 32, 32]> self = ?                                   | Done     | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 960, 64, 64]> self = ?                                   | Done     | Unknown    | N/A                | N/A    |

