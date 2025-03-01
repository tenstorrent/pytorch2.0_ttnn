### aten.cumsum.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1      | Done     | Done       | 0.9999860259032941 | 1      |
|  1 | Tensor<[1, 32]> self = ?,<br>int dim = -1     | Unknown  | Done       | 0.9999624991517904 | 1      |
|  2 | Tensor<[1, 45]> self = ?,<br>int dim = -1     | Unknown  | Done       | 0.9999634136792082 | 1      |
|  3 | Tensor<[1, 59]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999803239459782 | 1      |
|  4 | Tensor<[1, 5]> self = ?,<br>int dim = -1      | Unknown  | Done       | 0.9999996606616214 | 1      |
|  5 | Tensor<[1, 60]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999897092792507 | 1      |
|  6 | Tensor<[1, s0]> self = ?,<br>int dim = -1     | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A                | N/A    |

