### aten.split_with_sizes.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 33, 10240]> self = ?,<br>List[int] split_sizes = [5120, 5120],<br>int dim = -1  | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 33, 192]> self = ?,<br>List[int] split_sizes = [160, 16, 16],<br>int dim = -1   | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 33, 10240]> self = ?,<br>List[int] split_sizes = [5120, 5120],<br>int dim = -1 | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 33, 192]> self = ?,<br>List[int] split_sizes = [160, 16, 16],<br>int dim = -1  | Removed  | Unknown    | N/A   | N/A    |

