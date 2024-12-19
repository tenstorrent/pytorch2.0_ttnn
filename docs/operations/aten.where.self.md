### aten.where.self
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 46]> condition = ?,<br>Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor other = ?                        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 6]> condition = ?,<br>Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor other = ?                          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, s10 + 1]> condition = ?,<br>Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor other = ?              | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, s10 + 1]> condition = ?,<br>Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor other = ?              | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 45, 45]> condition = ?,<br>Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor other = ?                      | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 5, 5]> condition = ?,<br>Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor other = ?                          | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 7, 7]> condition = ?,<br>Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                      | None     | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                               | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                         | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[15, 15]> condition = ?,<br>Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                         | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[17, 17]> condition = ?,<br>Tensor<[17, 17]> self = ?,<br>Tensor<[17, 17]> other = ?                         | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[2, 2]> condition = ?,<br>Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                               | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[s0 + 1, s0 + 1]> condition = ?,<br>Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |

