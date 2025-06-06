### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?      | Removed  | Done       | 0.9999978672306958 | 0      |
|  1 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?      | Removed  | Done       | 0.9999971930119512 | 0      |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?   | Done     | Done       | 0.9999980318998538 | 0      |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ? | Done     | Done       | 0.9999980308316793 | 0      |
|  4 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ? | Done     | Done       | 0.9999979628636693 | 0      |
|  5 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ? | Done     | Done       | 0.9999980148342027 | 0      |
|  6 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?       | Done     | Done       | 0.9999978534184917 | 0      |
|  7 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                    | Done     | Done       | 0.9999949505618564 | 0      |
|  8 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?         | Done     | Done       | 0.9999980609785831 | 0      |
|  9 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                   | Done     | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?       | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                   | Done     | Done       | 0.9999947540383407 | 0      |
| 12 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?       | Done     | Done       | 0.9999980008841669 | 0      |
| 13 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?         | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ? | Done     | Done       | 0.999998058019936  | 0      |

