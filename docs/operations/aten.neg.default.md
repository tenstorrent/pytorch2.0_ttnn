### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16, 16]> self = ?   | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 7, 32]> self = ?    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1]> self = ?           | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 32, 32, 64]> self = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 5, 16, 16]> self = ?   | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 512]> self = ?         | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 71, 7, 32]> self = ?   | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[17, 17]> self = ?         | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[2, 512]> self = ?         | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |

