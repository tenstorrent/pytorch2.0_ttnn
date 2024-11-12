### aten.unbind.int
|    | ATen Input Variations                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1   | Unknown  | Unknown    | N/A   |
|  1 | Tensor<[12, 4]> self = ?,<br>int dim = 1  | Unknown  | Fallback   | True  |
|  2 | Tensor<[300, 4]> self = ?,<br>int dim = 1 | Unknown  | Fallback   | True  |

