### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
|  1 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
|  2 | Tensor<[1, 144, 150, 150]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0     | None     | Fallback   | True  |
|  3 | Tensor<[1, 144, 151, 151]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                          | None     | Fallback   | True  |
|  4 | Tensor<[1, 144, 190, 190]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0     | None     | Fallback   | True  |
|  5 | Tensor<[1, 144, 191, 191]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                          | None     | Fallback   | True  |
|  6 | Tensor<[1, 144, 56, 56]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | None     | Fallback   | True  |
|  7 | Tensor<[1, 144, 59, 59]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Fallback   | True  |
|  8 | Tensor<[1, 144, 60, 60]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | None     | Fallback   | True  |
|  9 | Tensor<[1, 144, 63, 63]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Fallback   | True  |
| 10 | Tensor<[1, 144, 65, 65]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Fallback   | True  |
| 11 | Tensor<[1, 144, 69, 69]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | True  |
| 12 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
| 13 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
| 14 | Tensor<[1, 192, 75, 75]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Fallback   | True  |
| 15 | Tensor<[1, 192, 79, 79]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | True  |
| 16 | Tensor<[1, 192, 95, 95]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Fallback   | True  |
| 17 | Tensor<[1, 192, 99, 99]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | True  |
| 18 | Tensor<[1, 240, 28, 28]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 19 | Tensor<[1, 240, 29, 29]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 20 | Tensor<[1, 240, 30, 30]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 21 | Tensor<[1, 240, 31, 31]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 22 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
| 23 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
| 24 | Tensor<[1, 288, 33, 33]> self = ?,<br>List[int] pad = [1, 1, 1, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 25 | Tensor<[1, 288, 35, 35]> self = ?,<br>List[int] pad = [-1, -1, -1, -1]                          | None     | Fallback   | True  |
| 26 | Tensor<[1, 288, 38, 38]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 27 | Tensor<[1, 288, 39, 39]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 28 | Tensor<[1, 3, 224, 224]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 29 | Tensor<[1, 3, 225, 225]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 30 | Tensor<[1, 3, 240, 240]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 31 | Tensor<[1, 3, 241, 241]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 32 | Tensor<[1, 3, 260, 260]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 33 | Tensor<[1, 3, 261, 261]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 34 | Tensor<[1, 3, 300, 300]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 35 | Tensor<[1, 3, 301, 301]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 36 | Tensor<[1, 3, 380, 380]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 37 | Tensor<[1, 3, 381, 381]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 38 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
| 39 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
| 40 | Tensor<[1, 336, 48, 48]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Fallback   | True  |
| 41 | Tensor<[1, 336, 49, 49]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | True  |
| 42 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
| 43 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Fallback | Done       | True  |
| 44 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Fallback | Done       | True  |
| 45 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Fallback | Done       | True  |
| 46 | Tensor<[1, 672, 14, 14]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | None     | Fallback   | True  |
| 47 | Tensor<[1, 672, 15, 15]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Fallback   | True  |
| 48 | Tensor<[1, 672, 17, 17]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Fallback   | True  |
| 49 | Tensor<[1, 672, 19, 19]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | True  |
| 50 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       | True  |
| 51 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Done       | True  |
| 52 | Tensor<[1, 720, 17, 17]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Fallback   | True  |
| 53 | Tensor<[1, 720, 21, 21]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | True  |
| 54 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       | True  |
| 55 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Done       | True  |
| 56 | Tensor<[1, 816, 19, 19]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Fallback   | True  |
| 57 | Tensor<[1, 816, 23, 23]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | True  |
| 58 | Tensor<[1, 96, 112, 112]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | None     | Fallback   | True  |
| 59 | Tensor<[1, 96, 113, 113]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Fallback   | True  |
| 60 | Tensor<[1, 96, 120, 120]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | None     | Fallback   | True  |
| 61 | Tensor<[1, 96, 121, 121]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Fallback   | True  |
| 62 | Tensor<[1, 96, 130, 130]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | None     | Fallback   | True  |
| 63 | Tensor<[1, 96, 131, 131]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Fallback   | True  |
| 64 | Tensor<[1, 960, 24, 24]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | None     | Fallback   | True  |
| 65 | Tensor<[1, 960, 27, 27]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Fallback   | True  |

