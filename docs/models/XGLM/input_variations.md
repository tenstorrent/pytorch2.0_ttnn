# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._log_softmax.default      |                  1 |           1 |         0 |          0 | ✅          |                1   |
|  1 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |                1   |
|  2 | aten._to_copy.default          |                  2 |           0 |         0 |          0 | ✘           |                0   |
|  3 | aten._unsafe_view.default      |                  1 |           0 |         0 |          0 | ✘           |                0   |
|  4 | aten.add.Tensor                |                  3 |           3 |         0 |          0 | ✅          |                1   |
|  5 | aten.addmm.default             |                  3 |           3 |         0 |          0 | ✅          |                1   |
|  6 | aten.arange.start              |                  1 |           0 |         0 |          0 | ✘           |                0   |
|  7 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |                1   |
|  8 | aten.clone.default             |                  5 |           5 |         0 |          0 | ✅          |                1   |
|  9 | aten.detach.default            |                  1 |           0 |         0 |          0 | ✘           |                0   |
| 10 | aten.embedding.default         |                  1 |           0 |         0 |          0 | ✘           |                0   |
| 11 | aten.expand.default            |                  2 |           1 |         0 |          0 | 🚧          |                0.5 |
| 12 | aten.full.default              |                  1 |           1 |         0 |          0 | ✅          |                1   |
| 13 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |                1   |
| 14 | aten.index_select.default      |                  1 |           0 |         0 |          0 | ✘           |                0   |
| 15 | aten.lift_fresh_copy.default   |                  1 |           0 |         0 |          0 | ✘           |                0   |
| 16 | aten.masked_fill.Scalar        |                  1 |           0 |         0 |          0 | ✘           |                0   |
| 17 | aten.maximum.default           |                  1 |           1 |         0 |          0 | ✅          |                1   |
| 18 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |                1   |
| 19 | aten.mul.Tensor                |                  2 |           2 |         0 |          0 | ✅          |                1   |
| 20 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |                1   |
| 21 | aten.new_zeros.default         |                  1 |           0 |         0 |          0 | ✘           |                0   |
| 22 | aten.nll_loss_forward.default  |                  1 |           0 |         0 |          0 | ✘           |                0   |
| 23 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |                1   |
| 24 | aten.slice.Tensor              |                  4 |           0 |         0 |          0 | ✘           |                0   |
| 25 | aten.squeeze.dim               |                  1 |           1 |         0 |          0 | ✅          |                1   |
| 26 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |                1   |
| 27 | aten.transpose.int             |                  3 |           3 |         0 |          0 | ✅          |                1   |
| 28 | aten.unsqueeze.default         |                  5 |           5 |         0 |          0 | ✅          |                1   |
| 29 | aten.view.default              |                 14 |           7 |         0 |          7 | 🚧          |                0.5 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[19, 256008]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Done     |
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 19, 19]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>Optional[int] dtype = torch.bool    | None     |
|  1 | Tensor<[1, 1, 19, 19]> self = ?,<br>Optional[int] dtype = torch.float32 | None     |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19, 16, 64]> self = ?,<br>List[int] size = [1, 19, 1024] | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> other = ? | Done     |
|  1 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ?    | Done     |
|  2 | Tensor<[1, 19]> self = ?,<br>Tensor other = 2                         | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[19, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[19, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     |
|  2 | Tensor<[4096]> self = ?,<br>Tensor<[19, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     |
### aten.arange.start
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 19,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 19, 19]> self = ?,<br>Tensor<[16, 19, 64]> mat2 = ? | Done     |
|  1 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ? | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  1 | Tensor<[1, 19, 1024]> self = ?                                                             | Done     |
|  2 | Tensor<[1, 19, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[1, 19, 4096]> self = ?                                                             | Done     |
|  4 | Tensor<[16, 19, 19]> self = ?                                                              | Done     |
### aten.detach.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 19, 1024]> self = ? | None     |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1 | None     |
### aten.expand.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19]  | Done     |
|  1 | Tensor<[1, 1, 19, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19] | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [19, 19],<br>number fill_value = -3.4028234663852886e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 19, 4096]> self = ? | Done     |
### aten.index_select.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2050, 1024]> self = ?,<br>int dim = 0,<br>Tensor<[19]> index = ? | None     |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | None     |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> mask = ?,<br>number value = -3.4028234663852886e+38 | None     |
### aten.maximum.default
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[]> other = ? | Done     |
### aten.mm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[19, 1024]> self = ?,<br>Tensor<[1024, 256008]> mat2 = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125 | Done     |
|  1 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0  | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Done     |
### aten.new_zeros.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 19]> self = ?,<br>List[int] size = [1, 19],<br>Optional[bool] pin_memory = False | None     |
### aten.nll_loss_forward.default
|    | ATen Input Variations                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[19, 256008]> self = ?,<br>Tensor<[19]> target = ?,<br>Optional[Tensor] weight = ?,<br>int reduction = 1,<br>int ignore_index = -100 | None     |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0 | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  |
|  1 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
|  2 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  |
|  3 | Tensor<[1, 19]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[1, 19]> self = ?,<br>int dim = 0 | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1024, 1024]> self = ?   | Done     |
|  1 | Tensor<[1024, 4096]> self = ?   | Done     |
|  2 | Tensor<[256008, 1024]> self = ? | Done     |
|  3 | Tensor<[4096, 1024]> self = ?   | Done     |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  1 | Tensor<[1, 19, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  2 | Tensor<[16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 19]> self = ?,<br>int dim = 2  | Done     |
|  1 | Tensor<[1, 19, 19]> self = ?,<br>int dim = 1 | Done     |
|  2 | Tensor<[1, 19]> self = ?,<br>int dim = 1     | Done     |
|  3 | Tensor<[19, 19]> self = ?,<br>int dim = 0    | Done     |
|  4 | Tensor<[19]> self = ?,<br>int dim = 0        | Done     |
### aten.view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>List[int] size = [16, 19, 19]  | Done     |
|  1 | Tensor<[1, 16, 19, 64]> self = ?,<br>List[int] size = [16, -1, 64]  | Fallback |
|  2 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64] | Fallback |
|  3 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [1, 19, 16, 64] | Fallback |
|  4 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [19, 1024]      | Done     |
|  5 | Tensor<[1, 19, 256008]> self = ?,<br>List[int] size = [-1, 256008]  | Fallback |
|  6 | Tensor<[1, 19, 4096]> self = ?,<br>List[int] size = [19, 4096]      | Done     |
|  7 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1, 19]              | Fallback |
|  8 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1]                  | Fallback |
|  9 | Tensor<[16, 19, 19]> self = ?,<br>List[int] size = [1, 16, 19, 19]  | Done     |
| 10 | Tensor<[16, 19, 64]> self = ?,<br>List[int] size = [1, 16, 19, 64]  | Done     |
| 11 | Tensor<[19, 1024]> self = ?,<br>List[int] size = [1, 19, 1024]      | Done     |
| 12 | Tensor<[19, 256008]> self = ?,<br>List[int] size = [1, 19, 256008]  | Fallback |
| 13 | Tensor<[19, 4096]> self = ?,<br>List[int] size = [1, 19, 4096]      | Done     |

