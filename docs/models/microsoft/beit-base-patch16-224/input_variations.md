# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  3 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  4 | aten.cat.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.clone.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  6 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.expand.default            |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.index.Tensor              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.mean.dim                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.mul.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 14 | aten.native_layer_norm.default |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 15 | aten.permute.default           |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 16 | aten.slice.Tensor              |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
| 17 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 18 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 19 | aten.unsqueeze.default         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 20 | aten.view.default              |                 14 |           6 |         0 |          8 | 🚧          |    0.43 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ? | Done     |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?         | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Done     |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[197, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ? | Done     |
|  1 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?  | Done     |
### aten.cat.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 196, 768]>],<br>int dim = 1 | None     |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?                                                          | Done     |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  2 | Tensor<[1, 197, 768]> self = ?                                                              | Done     |
|  3 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0 | None     |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Unknown  |
|  1 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Unknown  |
|  2 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Unknown  |
|  3 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 197, 3072]> self = ? | Done     |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[732, 12]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>] | None     |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1] | Done     |
### aten.mm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ? | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12      | Done     |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     |
|  2 | Tensor<[197, 197, 12]> self = ?,<br>List[int] dims = [2, 0, 1]      | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
|  2 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807 | Done     |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1000, 768]> self = ? | Done     |
|  1 | Tensor<[3072, 768]> self = ? | Done     |
|  2 | Tensor<[768, 3072]> self = ? | Done     |
|  3 | Tensor<[768, 768]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     |
|  1 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[12, 197, 197]> self = ?,<br>int dim = 0 | Done     |
### aten.view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197] | Fallback |
|  1 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]   | Done     |
|  2 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]   | Fallback |
|  3 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]   | Fallback |
|  4 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]       | Done     |
|  5 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]   | Fallback |
|  6 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]         | Done     |
|  7 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]   | Fallback |
|  8 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Fallback |
|  9 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Done     |
| 10 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                  | Fallback |
| 11 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]       | Done     |
| 12 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]         | Done     |
| 13 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [197, 197, -1]       | Fallback |

