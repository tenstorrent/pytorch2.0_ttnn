### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 512]> mat1 = ?,<br>Tensor<[512, 1000]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[10]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 10]> mat2 = ?     | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[256]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 256]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[512]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 512]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[512]> self = ?,<br>Tensor<[256, 768]> mat1 = ?,<br>Tensor<[768, 512]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |

