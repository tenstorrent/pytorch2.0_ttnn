### aten.lt.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16           | Done     | Fallback   | 1.0   | 0      |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8          | Done     | Fallback   | 1.0   | 0      |
|  2 | Tensor<[15, 15]> self = ?,<br>number other = 8          | Done     | Fallback   | 1.0   | 0      |
|  3 | Tensor<[17, 17]> self = ?,<br>number other = 16         | Unknown  | Fallback   | 1.0   | 0      |
|  4 | Tensor<[2, 2]> self = ?,<br>number other = 16           | Unknown  | Fallback   | 1.0   | 0      |
|  5 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | Unknown    | N/A   | N/A    |

