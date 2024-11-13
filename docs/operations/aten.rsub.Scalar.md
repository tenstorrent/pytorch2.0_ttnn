### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | True  |
|  2 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | True  |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | None     | Fallback   | True  |
|  4 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | None     | Fallback   | True  |
|  6 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | True  |
|  7 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Fallback | Done       | True  |
|  8 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0     | Done     | Done       | True  |
|  9 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | None     | Fallback   | True  |
| 10 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | True  |
| 11 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | None     | Fallback   | True  |
| 12 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | None     | Fallback   | True  |
| 13 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Fallback   | True  |
| 14 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Fallback   | True  |
| 15 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Fallback   | True  |
| 16 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | True  |
| 17 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Unknown  | Fallback   | True  |
| 18 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0       | Done     | Done       | True  |
| 19 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | None     | Fallback   | True  |
| 20 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A   |
| 21 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A   |
| 22 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0     | None     | Fallback   | True  |
| 23 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Fallback | Done       | True  |
| 24 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | None     | Fallback   | True  |
| 25 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | None     | Fallback   | True  |
| 26 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Fallback | Done       | True  |
| 27 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Fallback   | True  |
| 28 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | None     | Fallback   | True  |
| 29 | Tensor<[1066]> self = ?,<br>number other = 1.0             | None     | Fallback   | True  |
| 30 | Tensor<[120, 1]> self = ?,<br>number other = 1.0           | None     | Fallback   | True  |
| 31 | Tensor<[128, 1]> self = ?,<br>number other = 1.0           | None     | Fallback   | True  |
| 32 | Tensor<[128]> self = ?,<br>number other = 1.0              | None     | Fallback   | True  |
| 33 | Tensor<[160]> self = ?,<br>number other = 1.0              | None     | Fallback   | True  |
| 34 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | None     | Fallback   | True  |
| 35 | Tensor<[240, 1]> self = ?,<br>number other = 1.0           | None     | Fallback   | True  |
| 36 | Tensor<[30, 1]> self = ?,<br>number other = 1.0            | None     | Fallback   | True  |
| 37 | Tensor<[300, 1]> self = ?,<br>number other = 1.0           | None     | Fallback   | True  |
| 38 | Tensor<[300]> self = ?,<br>number other = 1.0              | None     | Fallback   | True  |
| 39 | Tensor<[320, 1]> self = ?,<br>number other = 1.0           | None     | Fallback   | True  |
| 40 | Tensor<[320]> self = ?,<br>number other = 1.0              | None     | Fallback   | True  |
| 41 | Tensor<[40]> self = ?,<br>number other = 1.0               | None     | Fallback   | True  |
| 42 | Tensor<[480, 1]> self = ?,<br>number other = 1.0           | None     | Fallback   | True  |
| 43 | Tensor<[60, 1]> self = ?,<br>number other = 1.0            | None     | Fallback   | True  |
| 44 | Tensor<[640]> self = ?,<br>number other = 1.0              | None     | Fallback   | True  |
| 45 | Tensor<[800, 1]> self = ?,<br>number other = 1.0           | None     | Fallback   | True  |
| 46 | Tensor<[80]> self = ?,<br>number other = 1.0               | None     | Fallback   | True  |

