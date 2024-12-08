### aten.repeat.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1]             | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]         | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1, 1]                   | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1444, 1]                | Done     | Done       |     1 |      1 |
|  5 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [9, 1]                   | Done     | Done       |     1 |      1 |
|  6 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [1, 1]                   | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [100, 1]                 | Done     | Done       |     1 |      1 |
|  8 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [25, 1]                  | Done     | Done       |     1 |      1 |
|  9 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [361, 1]                 | Done     | Done       |     1 |      1 |
| 10 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [4, 1]                   | Done     | Done       |     1 |      1 |
| 11 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1]                 | Done     | Done       |     1 |      1 |
| 12 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [9, 1]                   | Done     | Done       |     1 |      1 |

