# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._log_softmax.default      |                  1 |
|  1 | aten._softmax.default          |                  1 |
|  2 | aten._to_copy.default          |                  1 |
|  3 | aten._unsafe_view.default      |                  1 |
|  4 | aten.add.Tensor                |                  2 |
|  5 | aten.addmm.default             |                  1 |
|  6 | aten.arange.start              |                  1 |
|  7 | aten.bmm.default               |                  1 |
|  8 | aten.clone.default             |                  2 |
|  9 | aten.detach.default            |                  1 |
| 10 | aten.embedding.default         |                  1 |
| 11 | aten.expand.default            |                  1 |
| 12 | aten.full.default              |                  1 |
| 13 | aten.gelu.default              |                  1 |
| 14 | aten.index_select.default      |                  1 |
| 15 | aten.lift_fresh_copy.default   |                  1 |
| 16 | aten.masked_fill.Scalar        |                  1 |
| 17 | aten.maximum.default           |                  1 |
| 18 | aten.mm.default                |                  1 |
| 19 | aten.mul.Tensor                |                  1 |
| 20 | aten.native_layer_norm.default |                  1 |
| 21 | aten.new_zeros.default         |                  1 |
| 22 | aten.nll_loss_forward.default  |                  1 |
| 23 | aten.rsub.Scalar               |                  1 |
| 24 | aten.slice.Tensor              |                  3 |
| 25 | aten.squeeze.dim               |                  1 |
| 26 | aten.t.default                 |                  1 |
| 27 | aten.transpose.int             |                  1 |
| 28 | aten.unsqueeze.default         |                  3 |
| 29 | aten.view.default              |                 11 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[19, 256008]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Unknown  |
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 19, 19]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19, 16, 64]> self = ?,<br>List[int] size = [1, 19, 1024] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ? | Unknown  |
|  1 | Tensor<[1, 19]> self = ?,<br>Tensor other = 2                      | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[19, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 19,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 19, 1024]> self = ?                                                             | Unknown  |
### aten.detach.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 19, 1024]> self = ? | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19] | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [19, 19],<br>number fill_value = -3.4028234663852886e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 19, 4096]> self = ? | Unknown  |
### aten.index_select.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2050, 1024]> self = ?,<br>int dim = 0,<br>Tensor<[19]> index = ? | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> mask = ?,<br>number value = -3.4028234663852886e+38 | Unknown  |
### aten.maximum.default
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[19, 1024]> self = ?,<br>Tensor<[1024, 256008]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0 | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19]> self = ?,<br>List[int] size = [1, 19],<br>Optional[bool] pin_memory = False | Unknown  |
### aten.nll_loss_forward.default
|    | ATen Input Variations                                                                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[19, 256008]> self = ?,<br>Tensor<[19]> target = ?,<br>Optional[Tensor] weight = None,<br>int reduction = 1,<br>int ignore_index = -100 | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1  | Unknown  |
|  1 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  2 | Tensor<[1, 19]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1        | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[1, 19]> self = ?,<br>int dim = 0 | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1024, 1024]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19]> self = ?,<br>int dim = 2  | Unknown  |
|  1 | Tensor<[1, 19, 19]> self = ?,<br>int dim = 1 | Unknown  |
|  2 | Tensor<[19]> self = ?,<br>int dim = 0        | Unknown  |
### aten.view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>List[int] size = [16, 19, 19] | Unknown  |
|  1 | Tensor<[1, 16, 19, 64]> self = ?,<br>List[int] size = [16, -1, 64] | Unknown  |
|  2 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [19, 1024]     | Unknown  |
|  3 | Tensor<[1, 19, 256008]> self = ?,<br>List[int] size = [-1, 256008] | Unknown  |
|  4 | Tensor<[1, 19, 4096]> self = ?,<br>List[int] size = [19, 4096]     | Unknown  |
|  5 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1, 19]             | Unknown  |
|  6 | Tensor<[16, 19, 19]> self = ?,<br>List[int] size = [1, 16, 19, 19] | Unknown  |
|  7 | Tensor<[16, 19, 64]> self = ?,<br>List[int] size = [1, 16, 19, 64] | Unknown  |
|  8 | Tensor<[19, 1024]> self = ?,<br>List[int] size = [1, 19, 1024]     | Unknown  |
|  9 | Tensor<[19, 256008]> self = ?,<br>List[int] size = [1, 19, 256008] | Unknown  |
| 10 | Tensor<[19, 4096]> self = ?,<br>List[int] size = [1, 19, 4096]     | Unknown  |

