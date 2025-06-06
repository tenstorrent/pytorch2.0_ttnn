### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Done     | Done       | 0.999959 |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Removed  | Done       | 0.999965 |      0 |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 1024]> mat2 = ?   | Removed  | Done       | 0.999979 |      0 |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Removed  | Done       | 0.99993  |      0 |
|  4 | Tensor<[128]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 128]> mat2 = ?   | Removed  | Done       | 0.999963 |      0 |
|  5 | Tensor<[128]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 128]> mat2 = ?     | Removed  | Done       | 0.999968 |      0 |
|  6 | Tensor<[30000]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 30000]> mat2 = ? | Removed  | Done       | 0.999979 |      0 |
|  7 | Tensor<[3072]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?   | Removed  | Done       | 0.999968 |      0 |
|  8 | Tensor<[4096]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Removed  | Done       | 0.999964 |      0 |
|  9 | Tensor<[768]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?     | Removed  | Done       | 0.99998  |      0 |
| 10 | Tensor<[768]> self = ?,<br>Tensor<[9, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?   | Removed  | Done       | 0.999941 |      0 |
| 11 | Tensor<[768]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?     | Removed  | Done       | 0.999968 |      0 |

