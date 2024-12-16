### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16]> self = ?,<br>number other = 0      | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1]> self = ?,<br>number other = 0       | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 7]> self = ?,<br>number other = 1       | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 7]> self = ?,<br>number other = 50256   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[16, 49, 49]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
|  5 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1]> self = ?,<br>number other = 1          | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1]> self = ?,<br>number other = 50256      | Done     | Done       |     1 |      0 |
|  8 | Tensor<[2, 1]> self = ?,<br>number other = 0       | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[4, 49, 49]> self = ?,<br>number other = 0  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | Done       |     1 |      0 |
| 11 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
| 12 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |

