### aten.bmm.default
|    | ATen Input Variations                                         | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ? | Done     | Done       | 0.999985 |      0 |
|  1 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?  | Done     | Done       | 0.999992 |      0 |
|  2 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ? | Done     | Done       | 0.999986 |      0 |
|  3 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?  | Done     | Done       | 0.999992 |      0 |

