# High Level Operations Status
|    | Operations                      |   Input Variations |
|---:|:--------------------------------|-------------------:|
|  0 | aten._softmax.default           |                  1 |
|  1 | aten._to_copy.default           |                  3 |
|  2 | aten._unsafe_view.default       |                  2 |
|  3 | aten.add.Tensor                 |                  1 |
|  4 | aten.addmm.default              |                  1 |
|  5 | aten.arange.default             |                  1 |
|  6 | aten.argmax.default             |                  1 |
|  7 | aten.bmm.default                |                  1 |
|  8 | aten.cat.default                |                  1 |
|  9 | aten.clone.default              |                  2 |
| 10 | aten.convolution.default        |                  1 |
| 11 | aten.div.Tensor                 |                  1 |
| 12 | aten.embedding.default          |                  1 |
| 13 | aten.exp.default                |                  1 |
| 14 | aten.expand.default             |                  2 |
| 15 | aten.full.default               |                  1 |
| 16 | aten.index.Tensor               |                  1 |
| 17 | aten.linalg_vector_norm.default |                  1 |
| 18 | aten.masked_fill.Scalar         |                  1 |
| 19 | aten.mm.default                 |                  1 |
| 20 | aten.mul.Tensor                 |                  3 |
| 21 | aten.native_layer_norm.default  |                  2 |
| 22 | aten.rsub.Scalar                |                  1 |
| 23 | aten.select.int                 |                  1 |
| 24 | aten.sigmoid.default            |                  1 |
| 25 | aten.slice.Tensor               |                  5 |
| 26 | aten.t.default                  |                  1 |
| 27 | aten.transpose.int              |                  1 |
| 28 | aten.unsqueeze.default          |                  3 |
| 29 | aten.view.default               |                 16 |
***
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> self = ?,<br>Optional[int] dtype = torch.bfloat16                      | Unknown  |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                              | Unknown  |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Unknown  |
|  1 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | number end = 2,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.argmax.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1 | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [expand, transpose],<br>int dim = 1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[12, 50, 50]> self = ?                                                              | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ? | Unknown  |
### aten.exp.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[]> self = ?     | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Unknown  |
|  1 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]          | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [arange, argmax] | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702            | Unknown  |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Unknown  |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125             | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  |
|  1 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 50, 3072]> self = ? | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                | Status   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  2 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
|  3 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7       | Unknown  |
|  4 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[768, 768]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   |
|---:|:-------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1 | Unknown  |
|  1 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2 | Unknown  |
|  2 | Tensor<[7, 7]> self = ?,<br>int dim = 0    | Unknown  |
### aten.view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64] | Unknown  |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]     | Unknown  |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]       | Unknown  |
|  3 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]  | Unknown  |
|  4 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64] | Unknown  |
|  5 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]      | Unknown  |
|  6 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]        | Unknown  |
|  7 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]    | Unknown  |
|  8 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]      | Unknown  |
|  9 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]      | Unknown  |
| 10 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Unknown  |
| 11 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]               | Unknown  |
| 12 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]   | Unknown  |
| 13 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]      | Unknown  |
| 14 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]     | Unknown  |
| 15 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]       | Unknown  |

