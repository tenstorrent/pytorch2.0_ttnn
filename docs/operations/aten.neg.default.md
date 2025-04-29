### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16, 16]> self = ?   | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1]> self = ?           | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 5, 16, 16]> self = ?   | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 512]> self = ?         | Done     | Done       | 1.0   | -1     |
|  4 | Tensor<[17, 17]> self = ?         | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[2, 512]> self = ?         | Done     | Done       | 1.0   | -1     |
|  7 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |

