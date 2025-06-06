### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                 | Done     | Done       | 0.999995 |      0 |
|  2 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                      | Done     | Done       | 1        |      0 |
|  3 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654       | Done     | Done       | 0.999997 |      0 |
|  4 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?           | Done     | Done       | 0.999996 |      0 |
|  5 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                | Done     | Done       | 0.999995 |      0 |
|  6 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                     | Done     | Done       | 1        |      0 |
|  7 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654      | Done     | Done       | 0.999997 |      0 |
|  8 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?         | Done     | Done       | 0.999996 |      0 |
|  9 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                | Done     | Done       | 0.999995 |      0 |
| 10 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                     | Done     | Done       | 1        |      0 |
| 11 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654      | Done     | Done       | 0.999997 |      0 |
| 12 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?         | Done     | Done       | 0.999996 |      0 |

