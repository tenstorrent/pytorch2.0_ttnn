# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._to_copy.default          |                  3 |
|  2 | aten._unsafe_view.default      |                  1 |
|  3 | aten.add.Tensor                |                  2 |
|  4 | aten.addmm.default             |                  1 |
|  5 | aten.arange.start              |                  1 |
|  6 | aten.baddbmm.default           |                  1 |
|  7 | aten.bmm.default               |                  1 |
|  8 | aten.clone.default             |                  2 |
|  9 | aten.cumsum.default            |                  1 |
| 10 | aten.embedding.default         |                  1 |
| 11 | aten.expand.default            |                  1 |
| 12 | aten.full.default              |                  1 |
| 13 | aten.lift_fresh_copy.default   |                  1 |
| 14 | aten.masked_fill.Scalar        |                  1 |
| 15 | aten.mm.default                |                  1 |
| 16 | aten.mul.Tensor                |                  2 |
| 17 | aten.native_layer_norm.default |                  1 |
| 18 | aten.permute.default           |                  2 |
| 19 | aten.pow.Tensor_Tensor         |                  1 |
| 20 | aten.rsub.Scalar               |                  1 |
| 21 | aten.select.int                |                  1 |
| 22 | aten.slice.Tensor              |                  3 |
| 23 | aten.sub.Tensor                |                  1 |
| 24 | aten.t.default                 |                  1 |
| 25 | aten.tanh.default              |                  1 |
| 26 | aten.transpose.int             |                  1 |
| 27 | aten.unsqueeze.default         |                  3 |
| 28 | aten.view.default              |                 13 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                | Unknown  |
|  2 | Tensor<[16, 1, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                               | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] size = [1, 32, 1536] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ? | Unknown  |
|  1 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[4608]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 4608]> mat2 = ? | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 1,<br>number end = 17,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 32]> self = ?,<br>Tensor<[16, 32, 96]> batch1 = ?,<br>Tensor<[16, 96, 32]> batch2 = ?,<br>number beta = 1.0,<br>number alpha = 0.10206207261596577 | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 32, 32]> self = ?                                                           | Unknown  |
|  1 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>int dim = -1 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32] | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5  | Unknown  |
|  1 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Unknown  |
|  1 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.pow.Tensor_Tensor
|    | ATen Input Variations                             | Status   |
|---:|:--------------------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>Tensor<[16]> exponent = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1        | Unknown  |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
|  2 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1 | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[4608, 1536]> self = ? | Unknown  |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 32, 6144]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[32, 32]> self = ?,<br>int dim = 0   | Unknown  |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2 | Unknown  |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = 1    | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]          | Unknown  |
|  1 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]         | Unknown  |
|  2 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96] | Unknown  |
|  3 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]         | Unknown  |
|  4 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]     | Unknown  |
|  5 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]     | Unknown  |
|  6 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]     | Unknown  |
|  7 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]     | Unknown  |
|  8 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]     | Unknown  |
|  9 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]     | Unknown  |
| 10 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]         | Unknown  |
| 11 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]         | Unknown  |
| 12 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]         | Unknown  |

