### aten.mm.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1024, 14336]> self = ?,<br>Tensor<[14336, 4096]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1024, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1024, 4096]> self = ?,<br>Tensor<[4096, 14336]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1024, 4096]> self = ?,<br>Tensor<[4096, 32768]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1024, 4096]> self = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |

