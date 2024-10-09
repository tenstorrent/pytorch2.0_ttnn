# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._to_copy.default   |                  3 |           0 |         2 |          0 | 🚧          |    0.67 |
|  1 | aten.all.default        |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.arange.start       |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.arange.start_step  |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  4 | aten.argmax.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.embedding.default  |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  6 | aten.eq.Scalar          |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.expand.default     |                  2 |           1 |         1 |          0 | ✅          |    1    |
|  8 | aten.full.default       |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.gt.Scalar          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.masked_fill.Scalar |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.mul.Tensor         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.rsub.Scalar        |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.slice.Tensor       |                  5 |           1 |         4 |          0 | ✅          |    1    |
| 14 | aten.unsqueeze.default  |                  5 |           5 |         0 |          0 | ✅          |    1    |
***
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Removed  |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bool     | None     |
|  2 | Tensor<[32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Removed  |
### aten.all.default
|    | ATen Input Variations    | Status   |
|---:|:-------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ? | None     |
### aten.arange.start
|    | ATen Input Variations                                                                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 32,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     |
### aten.arange.start_step
|    | ATen Input Variations                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 32,<br>number end = 0,<br>number step = -1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     |
### aten.argmax.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>Optional[int] dim = 1,<br>bool keepdim = True | None     |
### aten.embedding.default
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[65024, 2272]> weight = ?,<br>Tensor<[1, 32]> indices = ? | Done     |
### aten.eq.Scalar
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>number other = 1 | None     |
### aten.expand.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]  | Done     |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32] | Removed  |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     |
### aten.gt.Scalar
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 0 | None     |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | None     |
### aten.mul.Tensor
|    | ATen Input Variations                               | Status   |
|---:|:----------------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>Tensor<[32]> other = ? | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0 | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  |
|  2 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  |
|  3 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Removed  |
|  4 | Tensor<[2048, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 32                      | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2  | Done     |
|  1 | Tensor<[1, 32, 32]> self = ?,<br>int dim = 1 | Done     |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = 1     | Done     |
|  3 | Tensor<[32, 32]> self = ?,<br>int dim = 0    | Done     |
|  4 | Tensor<[32]> self = ?,<br>int dim = 0        | Done     |

