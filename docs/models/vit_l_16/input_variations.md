# High Level Operations Status
|    | Operations                                       |   Input Variations |
|---:|:-------------------------------------------------|-------------------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                  1 |
|  1 | aten.add.Tensor                                  |                  1 |
|  2 | aten.addmm.default                               |                  1 |
|  3 | aten.cat.default                                 |                  1 |
|  4 | aten.clone.default                               |                  2 |
|  5 | aten.convolution.default                         |                  1 |
|  6 | aten.expand.default                              |                  1 |
|  7 | aten.gelu.default                                |                  1 |
|  8 | aten.native_layer_norm.default                   |                  1 |
|  9 | aten.permute.default                             |                  2 |
| 10 | aten.select.int                                  |                  2 |
| 11 | aten.slice.Tensor                                |                  1 |
| 12 | aten.squeeze.dim                                 |                  1 |
| 13 | aten.t.default                                   |                  1 |
| 14 | aten.transpose.int                               |                  3 |
| 15 | aten.unsqueeze.default                           |                  1 |
| 16 | aten.view.default                                |                  8 |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 197, 64]> query = ?,<br>Tensor<[1, 16, 197, 64]> key = ?,<br>Tensor<[1, 16, 197, 64]> value = ? | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [expand, permute],<br>int dim = 1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 1024]> self = ?                                                              | Unknown  |
|  1 | Tensor<[3, 197, 1, 1024]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 197, 4096]> self = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-06 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] dims = [0, 2, 1]      | Unknown  |
|  1 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3] | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>int index = 0    | Unknown  |
|  1 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[3, 197, 1, 1, 1024]> self = ?,<br>int dim = -2 | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[3072, 1024]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 197, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | Unknown  |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Unknown  |
|  2 | Tensor<[197, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[197, 1, 3, 1024]> self = ?,<br>int dim = 0 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196] | Unknown  |
|  1 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]       | Unknown  |
|  2 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | Unknown  |
|  3 | Tensor<[197, 1, 1024]> self = ?,<br>List[int] size = [197, 1024]       | Unknown  |
|  4 | Tensor<[197, 1, 3072]> self = ?,<br>List[int] size = [197, 1, 3, 1024] | Unknown  |
|  5 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [197, 1, 1024]       | Unknown  |
|  6 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [197, 1, 3072]       | Unknown  |
|  7 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]       | Unknown  |

