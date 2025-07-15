### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]          | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, s1]> self = ?,<br>List[int] dims = [2, 0, 1]          | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 33, 16, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 33, 5120, 1]> self = ?,<br>List[int] dims = [0, 1, 2, 3] | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 33, 5120]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 33, s1, 1]> self = ?,<br>List[int] dims = [0, 1, 3, 2]   | Removed  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 5120, 16]> self = ?,<br>List[int] dims = [0, 1, 2]       | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 5120, 16]> self = ?,<br>List[int] dims = [1, 2, 0]       | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 5120, 33]> self = ?,<br>List[int] dims = [0, 2, 1]       | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s0, s1]> self = ?,<br>List[int] dims = [0, 1, 2]         | Removed  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, s0, s1]> self = ?,<br>List[int] dims = [1, 2, 0]         | Removed  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, s1, 1]> self = ?,<br>List[int] dims = [0, 2, 1]          | Removed  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[5120, 1, 1]> self = ?,<br>List[int] dims = [2, 0, 1]        | Removed  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[5120, 16, 1, 1]> self = ?,<br>List[int] dims = [2, 3, 0, 1] | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[s0, 1, 1]> self = ?,<br>List[int] dims = [2, 0, 1]          | Removed  | Unknown    | N/A   | N/A    |

