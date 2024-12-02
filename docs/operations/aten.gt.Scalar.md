### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Done     | Done       | True  |
|  1 | Tensor<[15, 15]> self = ?,<br>number other = 0 | Done     | Done       | True  |
|  2 | Tensor<[]> self = ?,<br>number other = 0       | None     | Fallback   | True  |

