### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> mask = ?,<br>number value = -3.3895313892515355e+38           | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> mask = ?,<br>number value = -3.3895313892515355e+38         | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> mask = ?,<br>number value = -3.3895313892515355e+38         | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 1, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 16, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38        | Unknown  | Done       | 1.0   | 1      |
| 10 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 50257]> mask = ?,<br>number value = -inf                                    | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> mask = ?,<br>number value = 0                                             | Unknown  | Fallback   | 1.0   | -1     |
| 12 | Tensor<[1, 920]> self = ?,<br>Tensor mask = ?,<br>number value = -inf                                                  | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = -100.0                              | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[16, 49, 49]> self = ?,<br>Tensor<[16, 49, 49]> mask = ?,<br>number value = 0.0                                 | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = -100.0                              | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[16, 64, 64]> self = ?,<br>Tensor<[16, 64, 64]> mask = ?,<br>number value = 0.0                                 | Done     | Done       | 1.0   | 0      |
| 17 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38             | Done     | Done       | 1.0   | 0      |
| 18 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> mask = ?,<br>number value = 0                                             | Unknown  | Fallback   | 1.0   | -1     |
| 19 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number value = -100.0                                | Done     | Done       | 1.0   | 0      |
| 20 | Tensor<[4, 49, 49]> self = ?,<br>Tensor<[4, 49, 49]> mask = ?,<br>number value = 0.0                                   | Done     | Done       | 1.0   | 0      |
| 21 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = -100.0                                | Done     | Done       | 1.0   | 0      |
| 22 | Tensor<[4, 64, 64]> self = ?,<br>Tensor<[4, 64, 64]> mask = ?,<br>number value = 0.0                                   | Done     | Done       | 1.0   | 0      |
| 23 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = -100.0                              | Done     | Done       | 1.0   | 0      |
| 24 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 49]> mask = ?,<br>number value = 0.0                                 | Done     | Done       | 1.0   | 0      |
| 25 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = -100.0                              | Done     | Done       | 1.0   | 0      |
| 26 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 64]> mask = ?,<br>number value = 0.0                                 | Done     | Done       | 1.0   | 0      |

