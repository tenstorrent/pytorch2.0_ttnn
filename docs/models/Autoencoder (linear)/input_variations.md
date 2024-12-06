# High Level Operations Status
|    | Operations         |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.addmm.default |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  1 | aten.relu.default  |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  2 | aten.t.default     |                  8 |           8 |         0 |          0 | ✅          |       1 |
***
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[128]> self = ?,<br>Tensor<[1, 64]> mat1 = ?,<br>Tensor<[64, 128]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[1, 784]> mat1 = ?,<br>Tensor<[784, 128]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[12]> self = ?,<br>Tensor<[1, 3]> mat1 = ?,<br>Tensor<[3, 12]> mat2 = ?       | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[12]> self = ?,<br>Tensor<[1, 64]> mat1 = ?,<br>Tensor<[64, 12]> mat2 = ?     | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[3]> self = ?,<br>Tensor<[1, 12]> mat1 = ?,<br>Tensor<[12, 3]> mat2 = ?       | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[64]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 64]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[64]> self = ?,<br>Tensor<[1, 12]> mat1 = ?,<br>Tensor<[12, 64]> mat2 = ?     | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[784]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 784]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 128]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64]> self = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[12, 3]> self = ?    | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[12, 64]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[128, 64]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[128, 784]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[3, 12]> self = ?    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[64, 128]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[64, 12]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[784, 128]> self = ? | Done     | Unknown    | N/A   | N/A    |

