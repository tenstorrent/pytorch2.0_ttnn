### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [32, 1, -1, -1]          | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]                   | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]                   | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]                   | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 8, 1, 32, 128]> self = ?,<br>List[int] size = [32, 8, 4, 32, 128] | Done     | Unknown    | N/A   | N/A    |

