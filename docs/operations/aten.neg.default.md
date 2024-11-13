### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   |
|---:|:----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 16, 16]> self = ?   | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1]> self = ?           | Fallback | Done       | True  |
|  2 | Tensor<[1, 5, 16, 16]> self = ?   | Unknown  | Done       | True  |
|  3 | Tensor<[1, 512]> self = ?         | Done     | Done       | True  |
|  4 | Tensor<[17, 17]> self = ?         | Unknown  | Done       | True  |
|  5 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | True  |
|  6 | Tensor<[2, 512]> self = ?         | Done     | Done       | True  |
|  7 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   |

