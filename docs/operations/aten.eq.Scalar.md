### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16]> self = ?,<br>number other = 0      | Done     | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1]> self = ?,<br>number other = 0       | Done     | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 45]> self = ?,<br>number other = 0      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 5]> self = ?,<br>number other = 0       | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 7]> self = ?,<br>number other = 1       | Done     | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 7]> self = ?,<br>number other = 50256   | Done     | Done       | 1.0   | -1     |
|  6 | Tensor<[1, s0]> self = ?,<br>number other = 0      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[16, 49, 49]> self = ?,<br>number other = 0 | Done     | Done       | 1.0   | -1     |
|  8 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | 1.0   | -1     |
|  9 | Tensor<[1]> self = ?,<br>number other = 1          | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1]> self = ?,<br>number other = 50256      | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[2, 1]> self = ?,<br>number other = 0       | Done     | Done       | 1.0   | -1     |
| 12 | Tensor<[4, 49, 49]> self = ?,<br>number other = 0  | Done     | Done       | 1.0   | -1     |
| 13 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | Done       | 1.0   | -1     |
| 14 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Done     | Done       | 1.0   | -1     |
| 15 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | 1.0   | -1     |

