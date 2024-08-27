# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._to_copy.default          |                  1 |
|  2 | aten.add.Tensor                |                  1 |
|  3 | aten.addmm.default             |                  1 |
|  4 | aten.bmm.default               |                  1 |
|  5 | aten.clone.default             |                  2 |
|  6 | aten.div.Tensor                |                  1 |
|  7 | aten.embedding.default         |                  2 |
|  8 | aten.expand.default            |                  3 |
|  9 | aten.gelu.default              |                  1 |
| 10 | aten.mul.Tensor                |                  1 |
| 11 | aten.native_layer_norm.default |                  1 |
| 12 | aten.permute.default           |                  1 |
| 13 | aten.rsub.Scalar               |                  1 |
| 14 | aten.slice.Tensor              |                  3 |
| 15 | aten.split.Tensor              |                  1 |
| 16 | aten.squeeze.dim               |                  1 |
| 17 | aten.t.default                 |                  1 |
| 18 | aten.transpose.int             |                  1 |
| 19 | aten.unsqueeze.default         |                  2 |
| 20 | aten.view.default              |                 10 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 256, 1024]> self = ?                                                             | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                             | Unknown  |
|  1 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]   | Unknown  |
|  1 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256] | Unknown  |
|  2 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [1, 16, 64, 256]   | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 256, 4096]> self = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256      | Unknown  |
|  2 | Tensor<[1, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1       | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 1]> self = ?,<br>int dim = -1 | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1024, 1024]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 2 | Unknown  |
|  1 | Tensor<[1, 256]> self = ?,<br>int dim = 1    | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[256, 4096]> self = ?,<br>List[int] size = [1, 256, 4096]       | Unknown  |
|  1 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [16, 256, 256] | Unknown  |
|  2 | Tensor<[16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256] | Unknown  |
|  3 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [16, 256, 64]   | Unknown  |
|  4 | Tensor<[16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]   | Unknown  |
|  5 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [16, 64, 256]   | Unknown  |
|  6 | Tensor<[256, 2]> self = ?,<br>List[int] size = [1, 256, 2]             | Unknown  |
|  7 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]       | Unknown  |
|  8 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [256, 4096]       | Unknown  |
|  9 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]       | Unknown  |

