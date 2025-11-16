### aten.where.self
|    | ATen Input Variations                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 1]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 46]> condition = ?,<br>Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor other = ?         | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 5]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, s0 + 1]> condition = ?,<br>Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, s0 + 1]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ?             | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 256]> condition = ?,<br>Tensor<[1, 1, 256]> self = ?,<br>Tensor<[]> other = ?          | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 32, 32]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ?                | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 4, 4]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 45, 45]> condition = ?,<br>Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor other = ?       | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 2]> condition = ?,<br>Tensor<[1, 2]> self = ?,<br>Tensor<[1, 2]> other = ?                | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s0 + 1]> condition = ?,<br>Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, s0, 256]> condition = ?,<br>Tensor<[1, s0, 256]> self = ?,<br>Tensor<[]> other = ?        | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?          | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[15, 15]> condition = ?,<br>Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?          | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[16384, 1]> condition = ?,<br>Tensor<[16384, 1]> self = ?,<br>Tensor<[]> other = ?            | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[16384, 3]> condition = ?,<br>Tensor<[16384, 3]> self = ?,<br>Tensor<[]> other = ?            | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[16384]> condition = ?,<br>Tensor<[16384]> self = ?,<br>Tensor<[]> other = ?                  | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[51865]> condition = ?,<br>Tensor<[]> self = ?,<br>Tensor<[1, 51865]> other = ?               | Unknown  | Unknown    | N/A   | N/A    |

