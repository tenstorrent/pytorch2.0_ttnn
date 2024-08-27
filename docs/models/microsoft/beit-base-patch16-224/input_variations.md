# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten.add.Tensor                |                  1 |
|  2 | aten.addmm.default             |                  1 |
|  3 | aten.bmm.default               |                  1 |
|  4 | aten.cat.default               |                  1 |
|  5 | aten.clone.default             |                  2 |
|  6 | aten.convolution.default       |                  1 |
|  7 | aten.div.Tensor                |                  1 |
|  8 | aten.expand.default            |                  4 |
|  9 | aten.gelu.default              |                  1 |
| 10 | aten.index.Tensor              |                  1 |
| 11 | aten.mean.dim                  |                  1 |
| 12 | aten.mm.default                |                  1 |
| 13 | aten.mul.Tensor                |                  1 |
| 14 | aten.native_layer_norm.default |                  1 |
| 15 | aten.permute.default           |                  2 |
| 16 | aten.slice.Tensor              |                  2 |
| 17 | aten.t.default                 |                  1 |
| 18 | aten.transpose.int             |                  2 |
| 19 | aten.unsqueeze.default         |                  1 |
| 20 | aten.view.default              |                 12 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [expand, transpose],<br>int dim = 1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 197, 768]> self = ?                                                            | Unknown  |
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
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Unknown  |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Unknown  |
|  2 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Unknown  |
|  3 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 197, 3072]> self = ? | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[732, 12]> self = ?,<br>List[Optional[Tensor]] indices = [view_13] | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1] | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[197, 197, 12]> self = ?,<br>List[int] dims = [2, 0, 1]      | Unknown  |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[768, 768]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
|  1 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[12, 197, 197]> self = ?,<br>int dim = 0 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]   | Unknown  |
|  1 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Unknown  |
|  2 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]   | Unknown  |
|  3 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                  | Unknown  |
|  4 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]   | Unknown  |
|  5 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197] | Unknown  |
|  6 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]       | Unknown  |
|  7 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]         | Unknown  |
|  8 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Unknown  |
|  9 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]         | Unknown  |
| 10 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]       | Unknown  |
| 11 | Tensor<[38809, 12]> self = ?,<br>List[int] size = [197, 197, -1]       | Unknown  |

