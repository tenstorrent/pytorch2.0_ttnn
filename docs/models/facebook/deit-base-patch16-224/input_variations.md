# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  1 |           1 |
|  1 | aten.add.Tensor                |                  1 |           1 |
|  2 | aten.addmm.default             |                  4 |           4 |
|  3 | aten.bmm.default               |                  2 |           2 |
|  4 | aten.cat.default               |                  1 |           0 |
|  5 | aten.clone.default             |                  3 |           3 |
|  6 | aten.convolution.default       |                  1 |           0 |
|  7 | aten.div.Tensor                |                  1 |           0 |
|  8 | aten.expand.default            |                  4 |           0 |
|  9 | aten.gelu.default              |                  1 |           1 |
| 10 | aten.native_layer_norm.default |                  1 |           1 |
| 11 | aten.permute.default           |                  2 |           2 |
| 12 | aten.select.int                |                  1 |           0 |
| 13 | aten.slice.Tensor              |                  2 |           0 |
| 14 | aten.t.default                 |                  4 |           4 |
| 15 | aten.transpose.int             |                  2 |           2 |
| 16 | aten.view.default              |                 12 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ? | Done     |
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
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = ['torch.Size([1, 1, 768])', 'torch.Size([1, 196, 768])'],<br>int dim = 1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?                                                          | Done     |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  2 | Tensor<[1, 197, 768]> self = ?                                                              | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0 | Unknown  |
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
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     |
### aten.select.int
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1      | Unknown  |
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
### aten.view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197] | Unknown  |
|  1 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]   | Unknown  |
|  2 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]   | Unknown  |
|  3 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]   | Unknown  |
|  4 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]       | Unknown  |
|  5 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]   | Unknown  |
|  6 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]         | Unknown  |
|  7 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]   | Unknown  |
|  8 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Unknown  |
|  9 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Unknown  |
| 10 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]       | Unknown  |
| 11 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]         | Unknown  |

