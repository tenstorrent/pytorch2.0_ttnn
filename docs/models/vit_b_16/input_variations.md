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
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 64]> query = ?,<br>Tensor<[1, 12, 197, 64]> key = ?,<br>Tensor<[1, 12, 197, 64]> value = ? | None     |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ? | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Done     |
|  1 | Tensor<[2304]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ? | Done     |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[197, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     |
### aten.cat.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 196, 768]>],<br>int dim = 1 | None     |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 3072]> self = ?                                                             | Done     |
|  1 | Tensor<[1, 197, 768]> self = ?                                                              | Done     |
|  2 | Tensor<[3, 197, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     |
### aten.expand.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 197, 3072]> self = ? | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Done     |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3] | Done     |
|  1 | Tensor<[1, 768, 196]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0    | None     |
|  1 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0 | None     |
|  2 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 1 | None     |
|  3 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 2 | None     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[3, 197, 1, 1, 768]> self = ?,<br>int dim = -2 | None     |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1000, 768]> self = ? | Done     |
|  1 | Tensor<[2304, 768]> self = ? | Done     |
|  2 | Tensor<[3072, 768]> self = ? | Done     |
|  3 | Tensor<[768, 3072]> self = ? | Done     |
|  4 | Tensor<[768, 768]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | Done     |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     |
|  2 | Tensor<[197, 1, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     |
|  3 | Tensor<[197, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1        | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[197, 1, 3, 768]> self = ?,<br>int dim = 0 | Done     |
### aten.view.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]      | Done     |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]        | Done     |
|  2 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]  | Fallback |
|  3 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]  | Done     |
|  4 | Tensor<[197, 1, 12, 64]> self = ?,<br>List[int] size = [197, 768]     | Fallback |
|  5 | Tensor<[197, 1, 2304]> self = ?,<br>List[int] size = [197, 1, 3, 768] | Fallback |
|  6 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 12, 64]     | Fallback |
|  7 | Tensor<[197, 1, 768]> self = ?,<br>List[int] size = [197, 768]        | Fallback |
|  8 | Tensor<[197, 2304]> self = ?,<br>List[int] size = [197, 1, 2304]      | Fallback |
|  9 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]      | Done     |
| 10 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]        | Done     |
| 11 | Tensor<[197, 768]> self = ?,<br>List[int] size = [197, 1, 768]        | Fallback |

