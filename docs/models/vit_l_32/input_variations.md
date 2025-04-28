# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten.add.Tensor                                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                               |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  3 | aten.cat.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  4 | aten.clone.default                               |                  3 |           0 |         3 |          0 | ✅          |       1 |
|  5 | aten.convolution.default                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.expand.default                              |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  7 | aten.gelu.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.native_layer_norm.default                   |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.permute.default                             |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 10 | aten.select.int                                  |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 11 | aten.slice.Tensor                                |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 12 | aten.squeeze.dim                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 13 | aten.t.default                                   |                  5 |           5 |         0 |          0 | ✅          |       1 |
| 14 | aten.transpose.int                               |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 15 | aten.unsqueeze.default                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.view.default                                |                 12 |          12 |         0 |          0 | ✅          |       1 |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                       | Status   | Isolated   | PCC   |   Host |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 16, 50, 64]> query = ?,<br>Tensor<[1, 16, 50, 64]> key = ?,<br>Tensor<[1, 16, 50, 64]> value = ? | None     | Fallback   | N/A   |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ? | Done     | Done       | 0.999998 |     -1 |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?  | Done     | Done       | 0.999965 |     -1 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[50, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999964 |     -1 |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[50, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | 0.999931 |     -1 |
|  3 | Tensor<[3072]> self = ?,<br>Tensor<[50, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Done     | Done       | 0.999964 |     -1 |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[50, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | 0.999964 |     -1 |
### aten.cat.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 1024]>, <[1, 49, 1024]>],<br>int dim = 1 | Done     | Done       |     1 |     -1 |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 1024]> self = ?                                                              | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 50, 4096]> self = ?                                                              | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |     -1 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1] | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 4096]> self = ? | Done     | Done       | 0.999991 |     -1 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   | PCC   |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 50, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-06 | Done     | Done       | N/A   |      0 |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 49]> self = ?,<br>List[int] dims = [0, 2, 1]      | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 16, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3] | Done     | Done       |     1 |     -1 |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 1,<br>int index = 0    | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
### aten.squeeze.dim
|    | ATen Input Variations                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 50, 1, 1, 1024]> self = ?,<br>int dim = -2 | Done     | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1024]> self = ? | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1024, 1024]> self = ? | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1024, 4096]> self = ? | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[3072, 1024]> self = ? | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[4096, 1024]> self = ? | Done     | Done       |     1 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 50, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[50, 1, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[50, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Done     | Done       |     1 |     -1 |
### aten.unsqueeze.default
|    | ATen Input Variations                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[50, 1, 3, 1024]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>List[int] size = [1, 1024, 49]  | Done     | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 50, 1024]> self = ?,<br>List[int] size = [50, 1024]       | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 50, 4096]> self = ?,<br>List[int] size = [50, 4096]       | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16, 50, 64]> self = ?,<br>List[int] size = [1, 16, 50, 64]   | Done     | Done       | 1.0   | -1     |
|  4 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 1024]       | Done     | Done       | 1.0   | -1     |
|  5 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 16, 64]     | Done     | Done       | 1.0   | -1     |
|  6 | Tensor<[50, 1, 16, 64]> self = ?,<br>List[int] size = [50, 1024]     | Done     | Done       | 1.0   | -1     |
|  7 | Tensor<[50, 1, 3072]> self = ?,<br>List[int] size = [50, 1, 3, 1024] | Done     | Done       | 1.0   | -1     |
|  8 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [1, 50, 1024]       | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [50, 1, 1024]       | Done     | Done       | 1.0   | -1     |
| 10 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [50, 1, 3072]       | Done     | Done       | 1.0   | -1     |
| 11 | Tensor<[50, 4096]> self = ?,<br>List[int] size = [1, 50, 4096]       | Done     | Unknown    | N/A   | N/A    |

