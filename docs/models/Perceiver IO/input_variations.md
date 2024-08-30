# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._to_copy.default          |                  1 |
|  2 | aten.add.Tensor                |                  1 |
|  3 | aten.addmm.default             |                  1 |
|  4 | aten.arange.start              |                  1 |
|  5 | aten.bmm.default               |                  1 |
|  6 | aten.clone.default             |                  2 |
|  7 | aten.div.Tensor                |                  1 |
|  8 | aten.embedding.default         |                  1 |
|  9 | aten.expand.default            |                 11 |
| 10 | aten.gelu.default              |                  1 |
| 11 | aten.mm.default                |                  1 |
| 12 | aten.mul.Tensor                |                  1 |
| 13 | aten.native_layer_norm.default |                  2 |
| 14 | aten.permute.default           |                  1 |
| 15 | aten.rsub.Scalar               |                  1 |
| 16 | aten.slice.Tensor              |                  2 |
| 17 | aten.t.default                 |                  1 |
| 18 | aten.transpose.int             |                  2 |
| 19 | aten.unsqueeze.default         |                  2 |
| 20 | aten.view.default              |                 28 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[256]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 256]> mat2 = ? | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 2048,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 8, 256, 2048]> self = ?                                                          | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [1, 8, 2048, 160] | Unknown  |
|  1 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256] | Unknown  |
|  2 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [1, 8, 2048, 32]   | Unknown  |
|  3 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]   | Unknown  |
|  4 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048] | Unknown  |
|  5 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]   | Unknown  |
|  6 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]     | Unknown  |
|  7 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [1, 8, 256, 96]     | Unknown  |
|  8 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [1, 8, 32, 2048]   | Unknown  |
|  9 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]     | Unknown  |
| 10 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, -1, -1]             | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 256, 1280]> self = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[2048, 768]> self = ?,<br>Tensor<[768, 262]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.4028234663852886e+38 | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Unknown  |
|  1 | Tensor<[1, 256, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1       | Unknown  |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[256, 1280]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 2048, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
|  1 | Tensor<[262, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 2 | Unknown  |
|  1 | Tensor<[1, 2048]> self = ?,<br>int dim = 1    | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 8, 160] | Unknown  |
|  1 | Tensor<[1, 2048, 256]> self = ?,<br>List[int] size = [1, 2048, 8, 32]   | Unknown  |
|  2 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [2048, 768]        | Unknown  |
|  3 | Tensor<[1, 2048, 8, 96]> self = ?,<br>List[int] size = [1, 2048, 768]   | Unknown  |
|  4 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]        | Unknown  |
|  5 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]     | Unknown  |
|  6 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 256, 8, 96]     | Unknown  |
|  7 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, 256, 1280]   | Unknown  |
|  8 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [8, 2048, 160]  | Unknown  |
|  9 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [8, 2048, 256]  | Unknown  |
| 10 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [8, 2048, 32]    | Unknown  |
| 11 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [8, 256, 160]    | Unknown  |
| 12 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [8, 256, 2048]  | Unknown  |
| 13 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]    | Unknown  |
| 14 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]      | Unknown  |
| 15 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [8, 256, 96]      | Unknown  |
| 16 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [8, 32, 2048]    | Unknown  |
| 17 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]      | Unknown  |
| 18 | Tensor<[2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 1280]      | Unknown  |
| 19 | Tensor<[2048, 256]> self = ?,<br>List[int] size = [1, 2048, 256]        | Unknown  |
| 20 | Tensor<[2048, 262]> self = ?,<br>List[int] size = [1, 2048, 262]        | Unknown  |
| 21 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]          | Unknown  |
| 22 | Tensor<[256, 768]> self = ?,<br>List[int] size = [1, 256, 768]          | Unknown  |
| 23 | Tensor<[8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]  | Unknown  |
| 24 | Tensor<[8, 2048, 96]> self = ?,<br>List[int] size = [1, 8, 2048, 96]    | Unknown  |
| 25 | Tensor<[8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]    | Unknown  |
| 26 | Tensor<[8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]  | Unknown  |
| 27 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]    | Unknown  |

