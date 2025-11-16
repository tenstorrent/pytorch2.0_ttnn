### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 10, 10]> self = ?,<br>Tensor<[1, 1, 10, 10]> mask = ?,<br>number value = -3.3895313892515355e+38       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 12, 12]> self = ?,<br>Tensor<[1, 1, 12, 12]> mask = ?,<br>number value = -3.3895313892515355e+38       | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 14, 14]> self = ?,<br>Tensor<[1, 1, 14, 14]> mask = ?,<br>number value = -3.3895313892515355e+38       | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 16, 16]> self = ?,<br>Tensor<[1, 1, 16, 16]> mask = ?,<br>number value = -3.3895313892515355e+38       | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> mask = ?,<br>number value = -3.3895313892515355e+38       | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 1, 25, 25]> self = ?,<br>Tensor<[1, 1, 25, 25]> mask = ?,<br>number value = -3.3895313892515355e+38       | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38       | Done     | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 1, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> mask = ?,<br>number value = -3.3895313892515355e+38       | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 1, 5, 5]> self = ?,<br>Tensor<[1, 1, 5, 5]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> mask = ?,<br>number value = -3.3895313892515355e+38       | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38           | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 1, 9, 9]> self = ?,<br>Tensor<[1, 1, 9, 9]> mask = ?,<br>number value = -3.3895313892515355e+38           | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 45]> self = ?,<br>Tensor<[1, 45]> mask = ?,<br>number value = 1                                           | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 50257]> mask = ?,<br>number value = -inf                                  | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> mask = ?,<br>number value = 1                                           | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 5]> self = ?,<br>Tensor<[1, 5]> mask = ?,<br>number value = 1                                             | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 920]> self = ?,<br>Tensor<[1, 920]> mask = ?,<br>number value = -inf                                      | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, s1]> self = ?,<br>Tensor<[1, s1]> mask = ?,<br>number value = 1                                           | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = -100.0                            | Done     | Done       | 1.0   | 0      |
| 24 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = 0.0                               | Done     | Done       | 1.0   | 0      |
| 25 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = -100.0                            | Done     | Done       | 1.0   | 0      |
| 26 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = 0.0                               | Done     | Done       | 1.0   | 0      |
| 27 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 1]> mask = ?,<br>number value = 0                                     | None     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38           | Done     | Done       | 1.0   | 0      |
| 29 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number value = -100.0                              | Done     | Done       | 1.0   | 0      |
| 30 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number value = 0.0                                 | Done     | Done       | 1.0   | 0      |
| 31 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = -100.0                              | Done     | Done       | 1.0   | 0      |
| 32 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = 0.0                                 | Done     | Done       | 1.0   | 0      |
| 33 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = -100.0                            | Done     | Done       | 1.0   | 0      |
| 34 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = 0.0                               | Done     | Done       | 1.0   | 0      |
| 35 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = -100.0                            | Done     | Done       | 1.0   | 0      |
| 36 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = 0.0                               | Done     | Done       | 1.0   | 0      |
| 37 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = 0                                             | None     | Unknown    | N/A   | N/A    |
| 38 | Tensor<[8, 1, 384, 384]> self = ?,<br>Tensor<[8, 1, 384, 384]> mask = ?,<br>number value = -3.3895313892515355e+38   | Done     | Unknown    | N/A   | N/A    |

