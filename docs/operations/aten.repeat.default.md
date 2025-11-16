### aten.repeat.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>List[int] repeats = [1, 1]                   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]   | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1]> self = ?,<br>List[int] repeats = [1, 1]           | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 4]> self = ?,<br>List[int] repeats = [1, 1]           | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, s0, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]  | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1] | Removed  | Done       | 1.0   | -1     |
|  6 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1, 1]           | Removed  | Done       | 1.0   | -1     |
|  7 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1444, 1]        | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [9, 1]           | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [1, 1]           | Removed  | Done       | 1.0   | -1     |
| 10 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [100, 1]         | Done     | Done       | 1.0   | 0      |
| 11 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [25, 1]          | Done     | Done       | 1.0   | 0      |
| 12 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [361, 1]         | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [4, 1]           | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1]         | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [9, 1]           | Done     | Done       | 1.0   | 0      |

