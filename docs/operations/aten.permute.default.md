### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]           | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, s1]> self = ?,<br>List[int] dims = [2, 0, 1]           | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 1]> self = ?,<br>List[int] dims = [0, 2, 1]           | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, 16, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]    | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 33, 5120, 1]> self = ?,<br>List[int] dims = [0, 1, 2, 3]  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 33, 5120]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 33, s1, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]    | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 5120, 16]> self = ?,<br>List[int] dims = [0, 1, 2]        | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 5120, 16]> self = ?,<br>List[int] dims = [1, 2, 0]        | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 5120, 33]> self = ?,<br>List[int] dims = [0, 2, 1]        | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s0, s1]> self = ?,<br>List[int] dims = [0, 1, 2]          | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, s0, s1]> self = ?,<br>List[int] dims = [1, 2, 0]          | Removed  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, s1, 1]> self = ?,<br>List[int] dims = [0, 2, 1]           | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[32, 1, 16]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[32, 1, s1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[32, 16, 1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[32, 33, 16, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]   | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[32, 33, 5120, 1]> self = ?,<br>List[int] dims = [0, 1, 2, 3] | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[32, 33, 5120]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[32, 33, s2, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]   | Removed  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[32, 5120, 16]> self = ?,<br>List[int] dims = [0, 1, 2]       | Removed  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[32, 5120, 1]> self = ?,<br>List[int] dims = [0, 1, 2]        | Removed  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[32, 5120, 33]> self = ?,<br>List[int] dims = [0, 2, 1]       | Removed  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[32, s0, 1]> self = ?,<br>List[int] dims = [0, 1, 2]          | Removed  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[32, s0, s1]> self = ?,<br>List[int] dims = [0, 1, 2]         | Removed  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[32, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[32, s1, 1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[5120, 1, 1]> self = ?,<br>List[int] dims = [2, 0, 1]         | Removed  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[5120, 16, 1, 1]> self = ?,<br>List[int] dims = [2, 3, 0, 1]  | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[s0, 1, 1]> self = ?,<br>List[int] dims = [2, 0, 1]           | Removed  | Unknown    | N/A   | N/A    |

