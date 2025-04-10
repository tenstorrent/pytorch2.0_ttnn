### aten.mm.default
|    | ATen Input Variations                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 128]> mat2 = ?    | Done     | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 9216]> mat2 = ? | Done     | Done       | 0.999979 |      0 |
|  2 | Tensor<[10, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?     | Done     | Done       | 0.999992 |      0 |
|  3 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 9216]> mat2 = ?   | Done     | Done       | 0.999992 |      0 |

