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
|    | ATen Input Variations                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 50, 64]> query = ?,<br>Tensor<[1, 12, 50, 64]> key = ?,<br>Tensor<[1, 12, 50, 64]> value = ? | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2304]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [expand, permute],<br>int dim = 1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> self = ?                                                              | Unknown  |
|  1 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 50, 3072]> self = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3] | Unknown  |
|  1 | Tensor<[1, 768, 49]> self = ?,<br>List[int] dims = [0, 2, 1]       | Unknown  |
### aten.select.int
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0    | Unknown  |
|  1 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                | Status   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[3, 50, 1, 1, 768]> self = ?,<br>int dim = -2 | Unknown  |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[2304, 768]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | Unknown  |
|  1 | Tensor<[1, 50, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Unknown  |
|  2 | Tensor<[50, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1        | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[50, 1, 3, 768]> self = ?,<br>int dim = 0 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]      | Unknown  |
|  1 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]   | Unknown  |
|  2 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64]  | Unknown  |
|  3 | Tensor<[50, 1, 2304]> self = ?,<br>List[int] size = [50, 1, 3, 768] | Unknown  |
|  4 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 768]        | Unknown  |
|  5 | Tensor<[50, 2304]> self = ?,<br>List[int] size = [50, 1, 2304]      | Unknown  |
|  6 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]      | Unknown  |
|  7 | Tensor<[50, 768]> self = ?,<br>List[int] size = [50, 1, 768]        | Unknown  |
