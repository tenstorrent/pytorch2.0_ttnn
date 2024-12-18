### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[15, 15]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[]> self = ?,<br>number other = 0       | None     | Fallback   |     1 |     -1 |

