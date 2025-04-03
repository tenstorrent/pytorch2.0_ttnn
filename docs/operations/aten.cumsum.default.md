### aten.cumsum.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1      | Done     | Done       | 0.9999941343604419 | 0      |
|  1 | Tensor<[1, 32]> self = ?,<br>int dim = -1     | Unknown  | Done       | 0.9999842828531169 | 0      |
|  2 | Tensor<[1, 45]> self = ?,<br>int dim = -1     | Unknown  | Done       | 0.9997900751841682 | 0      |
|  3 | Tensor<[1, 59]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999635158900884 | 0      |
|  4 | Tensor<[1, 5]> self = ?,<br>int dim = -1      | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 60]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999744398410074 | 0      |
|  6 | Tensor<[1, s0]> self = ?,<br>int dim = -1     | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A                | N/A    |

