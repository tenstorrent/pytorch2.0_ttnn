### aten.repeat.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1]             | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Removed  | Fallback   | True  |
|  2 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]         | Removed  | Fallback   | True  |
|  3 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1, 1]                   | Unknown  | Fallback   | True  |
|  4 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1444, 1]                | Done     | Done       | True  |
|  5 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [9, 1]                   | Done     | Done       | True  |
|  6 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [1, 1]                   | Unknown  | Fallback   | True  |
|  7 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [100, 1]                 | Done     | Done       | True  |
|  8 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [25, 1]                  | Done     | Done       | True  |
|  9 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [361, 1]                 | Done     | Done       | True  |
| 10 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [4, 1]                   | Done     | Done       | True  |
| 11 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1]                 | Done     | Done       | True  |
| 12 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [9, 1]                   | Done     | Done       | True  |

