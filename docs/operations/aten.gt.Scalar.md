### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 0   | None     | Done       |     1 |      0 |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[15, 15]> self = ?,<br>number other = 0 | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[]> self = ?,<br>number other = 0       | Unknown  | Fallback   |     1 |     -1 |

