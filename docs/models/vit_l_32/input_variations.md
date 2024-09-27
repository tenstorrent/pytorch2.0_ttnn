# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten.add.Tensor                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                               |                  5 |           5 |         0 |          0 | ✅          |    1    |
|  3 | aten.cat.default                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.clone.default                               |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  5 | aten.convolution.default                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.expand.default                              |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.gelu.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  8 | aten.native_layer_norm.default                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.permute.default                             |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 10 | aten.select.int                                  |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.slice.Tensor                                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.squeeze.dim                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.t.default                                   |                  5 |           5 |         0 |          0 | ✅          |    1    |
| 14 | aten.transpose.int                               |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 15 | aten.unsqueeze.default                           |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 16 | aten.view.default                                |                 12 |           5 |         0 |          7 | 🚧          |    0.42 |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 50, 64]> query = ?,<br>Tensor<[1, 16, 50, 64]> key = ?,<br>Tensor<[1, 16, 50, 64]> value = ? | None     |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ? | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?  | Done     |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[50, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[50, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     |
|  3 | Tensor<[3072]> self = ?,<br>Tensor<[50, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Done     |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[50, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     |
### aten.cat.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [<[1, 1, 1024]>, <[1, 49, 1024]>],<br>int dim = 1 | None     |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 1024]> self = ?                                                              | Done     |
|  1 | Tensor<[1, 50, 4096]> self = ?                                                              | Done     |
|  2 | Tensor<[3, 50, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     |
### aten.expand.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 50, 4096]> self = ? | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-06 | Done     |
### aten.permute.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 49]> self = ?,<br>List[int] dims = [0, 2, 1]      | Done     |
|  1 | Tensor<[1, 16, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3] | Done     |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 1,<br>int index = 0    | None     |
|  1 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0 | None     |
|  2 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 1 | None     |
|  3 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 2 | None     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[3, 50, 1, 1, 1024]> self = ?,<br>int dim = -2 | None     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1024]> self = ? | Done     |
|  1 | Tensor<[1024, 1024]> self = ? | Done     |
|  2 | Tensor<[1024, 4096]> self = ? | Done     |
|  3 | Tensor<[3072, 1024]> self = ? | Done     |
|  4 | Tensor<[4096, 1024]> self = ? | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | Done     |
|  1 | Tensor<[1, 50, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     |
|  2 | Tensor<[50, 1, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     |
|  3 | Tensor<[50, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[50, 1, 3, 1024]> self = ?,<br>int dim = 0 | Done     |
### aten.view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>List[int] size = [1, 1024, 49]  | Fallback |
|  1 | Tensor<[1, 50, 1024]> self = ?,<br>List[int] size = [50, 1024]       | Done     |
|  2 | Tensor<[1, 50, 4096]> self = ?,<br>List[int] size = [50, 4096]       | Done     |
|  3 | Tensor<[16, 50, 64]> self = ?,<br>List[int] size = [1, 16, 50, 64]   | Done     |
|  4 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 1024]       | Fallback |
|  5 | Tensor<[50, 1, 1024]> self = ?,<br>List[int] size = [50, 16, 64]     | Fallback |
|  6 | Tensor<[50, 1, 16, 64]> self = ?,<br>List[int] size = [50, 1024]     | Fallback |
|  7 | Tensor<[50, 1, 3072]> self = ?,<br>List[int] size = [50, 1, 3, 1024] | Fallback |
|  8 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [1, 50, 1024]       | Done     |
|  9 | Tensor<[50, 1024]> self = ?,<br>List[int] size = [50, 1, 1024]       | Fallback |
| 10 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [50, 1, 3072]       | Fallback |
| 11 | Tensor<[50, 4096]> self = ?,<br>List[int] size = [1, 50, 4096]       | Done     |

