### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC                 | Host   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor<[1, 14, 14, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
|  1 | Tensor<[1, 14, 14, 512]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
|  2 | Tensor<[1, 144, 150, 150]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0     | Done     | Done       | 0.38457661473518895 | 0      |
|  3 | Tensor<[1, 144, 151, 151]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                          | None     | Fallback   | 1.0                 | -1     |
|  4 | Tensor<[1, 144, 190, 190]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0     | Unknown  | Done       | 1.0                 | 0      |
|  5 | Tensor<[1, 144, 191, 191]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                          | Unknown  | Unknown    | N/A                 | N/A    |
|  6 | Tensor<[1, 144, 56, 56]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
|  7 | Tensor<[1, 144, 59, 59]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Fallback   | 1.0                 | -1     |
|  8 | Tensor<[1, 144, 60, 60]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
|  9 | Tensor<[1, 144, 63, 63]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Fallback   | 1.0                 | -1     |
| 10 | Tensor<[1, 144, 65, 65]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 11 | Tensor<[1, 144, 69, 69]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | 1.0                 | -1     |
| 12 | Tensor<[1, 16, 16, 384]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
| 13 | Tensor<[1, 16, 16, 512]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
| 14 | Tensor<[1, 192, 75, 75]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 15 | Tensor<[1, 192, 79, 79]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | 1.0                 | -1     |
| 16 | Tensor<[1, 192, 95, 95]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Unknown  | Done       | 1.0                 | 0      |
| 17 | Tensor<[1, 192, 99, 99]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | Unknown  | Unknown    | N/A                 | N/A    |
| 18 | Tensor<[1, 240, 28, 28]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 19 | Tensor<[1, 240, 29, 29]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | 1.0                 | -1     |
| 20 | Tensor<[1, 240, 30, 30]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 21 | Tensor<[1, 240, 31, 31]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | 1.0                 | -1     |
| 22 | Tensor<[1, 28, 28, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
| 23 | Tensor<[1, 28, 28, 256]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
| 24 | Tensor<[1, 288, 33, 33]> self = ?,<br>List[int] pad = [1, 1, 1, 1],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 25 | Tensor<[1, 288, 35, 35]> self = ?,<br>List[int] pad = [-1, -1, -1, -1]                          | None     | Fallback   | 1.0                 | -1     |
| 26 | Tensor<[1, 288, 38, 38]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Done     | Done       | 0.5110147545680122  | 0      |
| 27 | Tensor<[1, 288, 39, 39]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | 1.0                 | -1     |
| 28 | Tensor<[1, 3, 224, 224]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Done     | Done       | 0.5354638392250529  | 0      |
| 29 | Tensor<[1, 3, 225, 225]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | 1.0                 | -1     |
| 30 | Tensor<[1, 3, 240, 240]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Done     | Done       | 0.5367176177872001  | 0      |
| 31 | Tensor<[1, 3, 241, 241]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | 1.0                 | -1     |
| 32 | Tensor<[1, 3, 260, 260]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Done     | Done       | 0.5120941661887938  | 0      |
| 33 | Tensor<[1, 3, 261, 261]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | 1.0                 | -1     |
| 34 | Tensor<[1, 3, 300, 300]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 35 | Tensor<[1, 3, 301, 301]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | None     | Fallback   | 1.0                 | -1     |
| 36 | Tensor<[1, 3, 380, 380]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Unknown  | Done       | 1.0                 | 0      |
| 37 | Tensor<[1, 3, 381, 381]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | Unknown  | Unknown    | N/A                 | N/A    |
| 38 | Tensor<[1, 32, 32, 192]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
| 39 | Tensor<[1, 32, 32, 256]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
| 40 | Tensor<[1, 336, 48, 48]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0       | Unknown  | Done       | 0.5502020825054155  | 0      |
| 41 | Tensor<[1, 336, 49, 49]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                            | Unknown  | Unknown    | N/A                 | N/A    |
| 42 | Tensor<[1, 56, 56, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
| 43 | Tensor<[1, 56, 56, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       | 1.0                 | 0      |
| 44 | Tensor<[1, 64, 64, 128]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0 | Done     | Done       | 1.0                 | 0      |
| 45 | Tensor<[1, 64, 64, 96]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       | 1.0                 | 0      |
| 46 | Tensor<[1, 672, 14, 14]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 47 | Tensor<[1, 672, 15, 15]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 48 | Tensor<[1, 672, 17, 17]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | None     | Fallback   | 1.0                 | -1     |
| 49 | Tensor<[1, 672, 19, 19]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | 1.0                 | -1     |
| 50 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       | 1.0                 | 0      |
| 51 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Done       | 1.0                 | 0      |
| 52 | Tensor<[1, 720, 17, 17]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 53 | Tensor<[1, 720, 21, 21]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | 1.0                 | -1     |
| 54 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0  | Done     | Done       | 1.0                 | 0      |
| 55 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] pad = [0, 0, 0, 0, 0, 0],<br>number value = 0.0   | Done     | Done       | 1.0                 | 0      |
| 56 | Tensor<[1, 816, 19, 19]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0       | Done     | Done       | 1.0                 | 0      |
| 57 | Tensor<[1, 816, 23, 23]> self = ?,<br>List[int] pad = [-2, -2, -2, -2]                          | None     | Fallback   | 1.0                 | -1     |
| 58 | Tensor<[1, 96, 112, 112]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | Done     | Done       | 0.5194925689748708  | 0      |
| 59 | Tensor<[1, 96, 113, 113]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Fallback   | 1.0                 | -1     |
| 60 | Tensor<[1, 96, 120, 120]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | Done     | Done       | 1.0                 | 0      |
| 61 | Tensor<[1, 96, 121, 121]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Fallback   | 1.0                 | -1     |
| 62 | Tensor<[1, 96, 130, 130]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0      | Done     | Done       | 0.3540476721730103  | 0      |
| 63 | Tensor<[1, 96, 131, 131]> self = ?,<br>List[int] pad = [0, -1, 0, -1]                           | None     | Fallback   | 1.0                 | -1     |
| 64 | Tensor<[1, 960, 24, 24]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0       | Unknown  | Done       | 1.0                 | 0      |
| 65 | Tensor<[1, 960, 27, 27]> self = ?,<br>List[int] pad = [-1, -2, -1, -2]                          | Unknown  | Unknown    | N/A                 | N/A    |

