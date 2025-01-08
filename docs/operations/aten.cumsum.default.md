### aten.cumsum.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1      | Done     | Done       | 0.9999932686711521 | 1      |
|  1 | Tensor<[1, 32]> self = ?,<br>int dim = -1     | Done     | Done       | 0.9998666428361949 | 1      |
|  2 | Tensor<[1, 45]> self = ?,<br>int dim = -1     | Unknown  | Done       | 0.999976535335596  | 1      |
|  3 | Tensor<[1, 59]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999732633016813 | 1      |
|  4 | Tensor<[1, 5]> self = ?,<br>int dim = -1      | Unknown  | Done       | 1.0                | 1      |
|  5 | Tensor<[1, 60]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.999893271638613  | 1      |
|  6 | Tensor<[1, s0]> self = ?,<br>int dim = -1     | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A                | N/A    |

