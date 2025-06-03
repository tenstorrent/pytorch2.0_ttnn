### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?      | Removed  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?      | Removed  | Done       | 0.9999978023281414 | 0      |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?   | Done     | Done       | 0.9999979687135953 | 0      |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ? | Done     | Done       | 0.9999979922127943 | 0      |
|  4 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ? | Done     | Done       | 0.9999979393027826 | 0      |
|  5 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ? | Done     | Done       | 0.9999980853593755 | 0      |
|  6 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?       | Done     | Done       | 0.9999980086694681 | 0      |
|  7 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                    | Done     | Done       | 0.9999953083943827 | 0      |
|  8 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?         | Done     | Done       | 0.9999981515660623 | 0      |
|  9 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                   | Done     | Done       | 0.9999949071381329 | 0      |
| 10 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?       | Done     | Done       | 0.9999979742285228 | 0      |
| 11 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                   | Done     | Done       | 0.9999946955492108 | 0      |
| 12 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?       | Done     | Done       | 0.9999980893785527 | 0      |
| 13 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?         | Done     | Done       | 0.9999981074787422 | 0      |
| 14 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ? | Done     | Done       | 0.9999980035899985 | 0      |

