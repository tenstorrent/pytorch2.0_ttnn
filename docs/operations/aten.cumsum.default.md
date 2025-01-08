### aten.cumsum.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1      | Done     | Done       | 0.9999905685526331 | 1      |
|  1 | Tensor<[1, 32]> self = ?,<br>int dim = -1     | Done     | Done       | 0.9997682891909632 | 1      |
|  2 | Tensor<[1, 45]> self = ?,<br>int dim = -1     | Unknown  | Done       | 0.9999800769020748 | 1      |
|  3 | Tensor<[1, 59]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9996639500912012 | 1      |
|  4 | Tensor<[1, 5]> self = ?,<br>int dim = -1      | Unknown  | Done       | 0.999992019634762  | 1      |
|  5 | Tensor<[1, 60]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999480634116437 | 1      |
|  6 | Tensor<[1, s0]> self = ?,<br>int dim = -1     | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A                | N/A    |

