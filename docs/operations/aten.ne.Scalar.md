### aten.ne.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?,<br>number other = 1      | None     | Fallback   | True  |
|  1 | Tensor<[16, 49, 49]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
|  2 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | True  |
|  3 | Tensor<[4, 49, 49]> self = ?,<br>number other = 0  | None     | Fallback   | True  |
|  4 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | Done       | True  |
|  5 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
|  6 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | True  |

