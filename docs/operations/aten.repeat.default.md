### aten.repeat.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int]<> repeats = [1, 1, 1]             | Unknown  |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int]<> repeats = [1, 1, 1, 1] | Removed  |
|  2 | Tensor<[1, 1, 256]> self = ?,<br>List[int]<> repeats = [1, 1, 1]           | Unknown  |
|  3 | Tensor<[1, s0, 256]> self = ?,<br>List[int]<> repeats = [1, 1, 1]          | Unknown  |
|  4 | Tensor<[100, 1, 256]> self = ?,<br>List[int]<> repeats = [1, 1, 1]         | Unknown  |
|  5 | Tensor<[4, 2]> self = ?,<br>List[int]<> repeats = [1, 1]                   | Unknown  |
|  6 | Tensor<[4, 2]> self = ?,<br>List[int]<> repeats = [1444, 1]                | Done     |
|  7 | Tensor<[4, 2]> self = ?,<br>List[int]<> repeats = [9, 1]                   | Done     |
|  8 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [1, 1]                   | Unknown  |
|  9 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [100, 1]                 | Done     |
| 10 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [25, 1]                  | Done     |
| 11 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [361, 1]                 | Done     |
| 12 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [4, 1]                   | Done     |
| 13 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [400, 1]                 | Done     |
| 14 | Tensor<[6, 2]> self = ?,<br>List[int]<> repeats = [9, 1]                   | Done     |

