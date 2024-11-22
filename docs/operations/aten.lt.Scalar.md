### aten.lt.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16           | None     | Fallback   | True  |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8          | None     | Fallback   | True  |
|  2 | Tensor<[15, 15]> self = ?,<br>number other = 8          | None     | Fallback   | True  |
|  3 | Tensor<[17, 17]> self = ?,<br>number other = 16         | Unknown  | Fallback   | True  |
|  4 | Tensor<[2, 2]> self = ?,<br>number other = 16           | Unknown  | Fallback   | True  |
|  5 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | Unknown    | N/A   |

