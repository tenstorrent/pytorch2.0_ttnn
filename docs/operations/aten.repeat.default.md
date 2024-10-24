### aten.repeat.default
|    | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Removed  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, s0, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[100, 1, 256]> self = ?,<br>List[int] repeats = [1, 1, 1]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1, 1]                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1444, 1]                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [9, 1]                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [1, 1]                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [100, 1]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [25, 1]                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [361, 1]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [4, 1]                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [9, 1]                   | Done     | N/A                 | N/A          | N/A               | N/A                |

