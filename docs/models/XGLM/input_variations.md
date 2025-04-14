# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._log_softmax.default      |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  1 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  2 | aten._to_copy.default          |                  3 |           3 |         0 |          0 | ✅          |     1   |
|  3 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  4 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  5 | aten.addmm.default             |                  3 |           3 |         0 |          0 | ✅          |     1   |
|  6 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  7 | aten.clone.default             |                  6 |           0 |         6 |          0 | ✅          |     1   |
|  8 | aten.copy.default              |                  1 |           0 |         1 |          0 | ✅          |     1   |
|  9 | aten.detach.default            |                  1 |           0 |         1 |          0 | ✅          |     1   |
| 10 | aten.embedding.default         |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 11 | aten.expand.default            |                  2 |           1 |         1 |          0 | ✅          |     1   |
| 12 | aten.fill.Tensor               |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 13 | aten.full.default              |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 14 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 15 | aten.index_select.default      |                  1 |           0 |         1 |          0 | ✅          |     1   |
| 16 | aten.lt.Tensor                 |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 17 | aten.masked_fill.Scalar        |                  2 |           1 |         0 |          0 | 🚧          |     0.5 |
| 18 | aten.maximum.default           |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 19 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 20 | aten.mul.Tensor                |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 21 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 22 | aten.new_zeros.default         |                  1 |           0 |         1 |          0 | ✅          |     1   |
| 23 | aten.nll_loss_forward.default  |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 24 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 25 | aten.select.int                |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 26 | aten.select_scatter.default    |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 27 | aten.slice.Tensor              |                  6 |           1 |         5 |          0 | ✅          |     1   |
| 28 | aten.slice_scatter.default     |                  2 |           1 |         1 |          0 | ✅          |     1   |
| 29 | aten.squeeze.dim               |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 30 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |     1   |
| 31 | aten.transpose.int             |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 32 | aten.unsqueeze.default         |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 33 | aten.view.default              |                 14 |          14 |         0 |          0 | ✅          |     1   |
| 34 | aten.zeros.default             |                  1 |           1 |         0 |          0 | ✅          |     1   |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[19, 256008]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | None     | Fallback   |     1 |     -1 |
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[16, 19, 19]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999604 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1, 19, 19]> self = ?,<br>Optional[int] dtype = torch.bool     | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[19, 19]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Done     | Fallback   |     1 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 19, 16, 64]> self = ?,<br>List[int] size = [1, 19, 1024] | Done     | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ?    | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[19, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[19, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | 0.999931 |      0 |
|  2 | Tensor<[4096]> self = ?,<br>Tensor<[19, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[16, 19, 19]> self = ?,<br>Tensor<[16, 19, 64]> mat2 = ? | Done     | Done       | 0.999989 |      0 |
|  1 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ? | Done     | Done       | 0.999986 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 19, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 18]> self = ?                                                                   | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 19, 1024]> self = ?                                                             | Removed  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 19, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 19, 4096]> self = ?                                                             | Removed  | Done       | 1.0   | 0      |
|  5 | Tensor<[16, 19, 19]> self = ?                                                              | Removed  | Done       | 1.0   | 0      |
### aten.copy.default
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 18]> self = ?,<br>Tensor<[1, 18]> src = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.detach.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 19, 1024]> self = ? | Removed  | Done       |     1 |     -1 |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[19]> indices = ?                              | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1 | Done     | Done       | 1.0   | 0      |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19]  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 19, 19]> self = ?,<br>List[int] size = [1, 1, 19, 19] | Removed  | Done       |     1 |     -1 |
### aten.fill.Tensor
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>Tensor value = ? | None     | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [19, 19],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | Done       |     1 |      0 |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 19, 4096]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.index_select.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2050, 1024]> self = ?,<br>int dim = 0,<br>Tensor<[19]> index = ? | Removed  | Done       |     1 |      0 |
### aten.lt.Tensor
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ? | None     | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[19, 19]> self = ?,<br>Tensor<[19, 19]> mask = ?,<br>number value = 0                                   | None     | Unknown    | N/A   | N/A    |
### aten.maximum.default
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor other = ? | None     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                           | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[19, 1024]> self = ?,<br>Tensor<[1024, 256008]> mat2 = ? | Done     | Done       | 0.999966 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                   | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0  | Done     | Done       |     1 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   | PCC   |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 19, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      1 |
### aten.new_zeros.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 19]> self = ?,<br>List[int] size = [1, 19],<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |      0 |
### aten.nll_loss_forward.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[19, 256008]> self = ?,<br>Tensor<[19]> target = ?,<br>Optional[Tensor] weight = ?,<br>int reduction = 1,<br>int ignore_index = -100 | None     | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0 | Done     | Done       | 0.999995 |      0 |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 19]> self = ?,<br>int dim = 1,<br>int index = -1 | Done     | Unknown    | N/A   | N/A    |
### aten.select_scatter.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 19]> self = ?,<br>Tensor<[1]> src = ?,<br>int dim = 1,<br>int index = -1 | None     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 19, 19]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 19]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Removed  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 19]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                         | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 19]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807        | Done     | Unknown    | N/A   | N/A    |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 19]> self = ?,<br>Tensor<[1, 18]> src = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 19]> self = ?,<br>Tensor<[1, 19]> src = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
### aten.squeeze.dim
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0 | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 1024]> self = ?   | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1024, 4096]> self = ?   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[256008, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[4096, 1024]> self = ?   | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 19, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 19]> self = ?,<br>int dim = 2  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 19, 19]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 19]> self = ?,<br>int dim = 1     | Done     | Done       |     1 |      0 |
|  3 | Tensor<[19, 19]> self = ?,<br>int dim = 0    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[19]> self = ?,<br>int dim = 0        | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 19, 19]> self = ?,<br>List[int] size = [16, 19, 19]  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 19, 64]> self = ?,<br>List[int] size = [16, -1, 64]  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [1, 19, 16, 64] | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 19, 1024]> self = ?,<br>List[int] size = [19, 1024]      | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 19, 256008]> self = ?,<br>List[int] size = [-1, 256008]  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 19, 4096]> self = ?,<br>List[int] size = [19, 4096]      | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1, 19]              | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 19]> self = ?,<br>List[int] size = [-1]                  | Done     | Done       |     1 |      0 |
|  9 | Tensor<[16, 19, 19]> self = ?,<br>List[int] size = [1, 16, 19, 19]  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[16, 19, 64]> self = ?,<br>List[int] size = [1, 16, 19, 64]  | Done     | Done       |     1 |      0 |
| 11 | Tensor<[19, 1024]> self = ?,<br>List[int] size = [1, 19, 1024]      | Done     | Done       |     1 |      0 |
| 12 | Tensor<[19, 256008]> self = ?,<br>List[int] size = [1, 19, 256008]  | Done     | Done       |     1 |      0 |
| 13 | Tensor<[19, 4096]> self = ?,<br>List[int] size = [1, 19, 4096]      | Done     | Done       |     1 |      0 |
### aten.zeros.default
|    | ATen Input Variations                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 19],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.int64 | Done     | Unknown    | N/A   | N/A    |

