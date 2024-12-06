### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 144, 150, 150]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0     | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 144, 151, 151]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                          | None     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 144, 190, 190]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0     | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 144, 191, 191]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                          | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 144, 56, 56]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 144, 59, 59]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 144, 60, 60]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 144, 63, 63]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 144, 65, 65]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 144, 69, 69]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 192, 75, 75]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 192, 79, 79]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 192, 95, 95]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 192, 99, 99]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 240, 28, 28]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 240, 29, 29]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 240, 30, 30]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 240, 31, 31]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 288, 33, 33]> self = ?,<br>List[int] pad = [1, 1, 1, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 288, 35, 35]> self = ?,<br>List[int] pad = [-1, -1, -1, -1]                          | None     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 288, 38, 38]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 288, 39, 39]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 3, 224, 224]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 3, 225, 225]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 3, 240, 240]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 3, 241, 241]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 3, 260, 260]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 3, 261, 261]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 3, 300, 300]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 3, 301, 301]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 3, 380, 380]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 3, 381, 381]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 336, 48, 48]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 336, 49, 49]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Unknown    | N/A   | N/A    |
| 44 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Unknown    | N/A   | N/A    |
| 45 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Unknown    | N/A   | N/A    |
| 46 | Tensor<[1, 672, 14, 14]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 47 | Tensor<[1, 672, 15, 15]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 48 | Tensor<[1, 672, 17, 17]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Unknown    | N/A   | N/A    |
| 49 | Tensor<[1, 672, 19, 19]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Unknown    | N/A   | N/A    |
| 50 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Unknown    | N/A   | N/A    |
| 51 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Unknown    | N/A   | N/A    |
| 52 | Tensor<[1, 720, 17, 17]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 53 | Tensor<[1, 720, 21, 21]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Unknown    | N/A   | N/A    |
| 54 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Unknown    | N/A   | N/A    |
| 55 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Unknown    | N/A   | N/A    |
| 56 | Tensor<[1, 816, 19, 19]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 57 | Tensor<[1, 816, 23, 23]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Unknown    | N/A   | N/A    |
| 58 | Tensor<[1, 96, 112, 112]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | None     | Unknown    | N/A   | N/A    |
| 59 | Tensor<[1, 96, 113, 113]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Unknown    | N/A   | N/A    |
| 60 | Tensor<[1, 96, 120, 120]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | None     | Unknown    | N/A   | N/A    |
| 61 | Tensor<[1, 96, 121, 121]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Unknown    | N/A   | N/A    |
| 62 | Tensor<[1, 96, 130, 130]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | None     | Unknown    | N/A   | N/A    |
| 63 | Tensor<[1, 96, 131, 131]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Unknown    | N/A   | N/A    |
| 64 | Tensor<[1, 960, 24, 24]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | None     | Unknown    | N/A   | N/A    |
| 65 | Tensor<[1, 960, 27, 27]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | Unknown  | Unknown    | N/A   | N/A    |

