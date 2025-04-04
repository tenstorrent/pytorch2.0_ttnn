### aten.mm.default
|    | ATen Input Variations                                     | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 64]> mat2 = ?  | Done     | Done       | 0.999984 |      0 |
|  1 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 784]> mat2 = ? | Done     | Done       | 0.99998  |      0 |
|  2 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 3]> mat2 = ?     | Done     | Done       | 1        |      0 |
|  3 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 64]> mat2 = ?    | Done     | Done       | 0.999993 |      0 |
|  4 | Tensor<[1, 3]> self = ?,<br>Tensor<[3, 12]> mat2 = ?      | Done     | Done       | 0.999995 |      0 |
|  5 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 128]> mat2 = ?   | Done     | Done       | 0.999984 |      0 |
|  6 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 12]> mat2 = ?    | Done     | Done       | 0.999987 |      0 |
|  7 | Tensor<[1, 784]> self = ?,<br>Tensor<[784, 128]> mat2 = ? | Done     | Done       | 0.999965 |      0 |
|  8 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 3]> mat2 = ?      | Done     | Done       | 0.999995 |      0 |
|  9 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?     | Done     | Done       | 0.999995 |      0 |
| 10 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?    | Done     | Done       | 0.999992 |      0 |
| 11 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 784]> mat2 = ?   | Done     | Done       | 0.999993 |      0 |
| 12 | Tensor<[3, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?      | Done     | Done       | 0.999993 |      0 |
| 13 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?    | Done     | Done       | 0.999991 |      0 |
| 14 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?     | Done     | Done       | 0.999992 |      0 |
| 15 | Tensor<[784, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?   | Done     | Done       | 0.999992 |      0 |

