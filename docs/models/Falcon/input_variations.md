# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._to_copy.default   |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  1 | aten.all.default        |                  1 |           0 |         0 |          1 | ✘           |       0 |
|  2 | aten.arange.start_step  |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.argmax.default     |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.embedding.default  |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  5 | aten.eq.Scalar          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.expand.default     |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  7 | aten.full.default       |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.gt.Scalar          |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.index.Tensor       |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 10 | aten.masked_fill.Scalar |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.mul.Tensor         |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.rsub.Scalar        |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 13 | aten.slice.Tensor       |                  5 |           1 |         4 |          0 | ✅          |       1 |
| 14 | aten.unsqueeze.default  |                  5 |           5 |         0 |          0 | ✅          |       1 |
***
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool     | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Done     | Fallback   |     1 |     -1 |
### aten.all.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ? | Fallback | Fallback   |     0 |      0 |
### aten.arange.start_step
|    | ATen Input Variations                                                                                                            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | number start = 7,<br>number end = 0,<br>number step = -1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   |     1 |     -1 |
### aten.argmax.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = 1,<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ? | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[7, 64]> weight = ?,<br>Tensor<[1, 7]> indices = ?       | Done     | Unknown    | N/A   | N/A    |
### aten.eq.Scalar
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 1 | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>List[int] size = [1, 1, 7, 7] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [1, 1, 7, 7] | Removed  | Done       |     1 |     -1 |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | Done       |     1 |      0 |
### aten.gt.Scalar
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 0 | None     | Done       |     1 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 7]>] | Removed  | Done       |     1 |      0 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Done       |     1 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>Tensor<[7]> other = ? | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>number other = 1.0 | Done     | Done       | 0.999994 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                     | Done     | Done       |     1 |     -1 |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2  | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1  | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 7]> self = ?,<br>int dim = 1     | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[7, 7]> self = ?,<br>int dim = 0     | Done     | Done       |     1 |     -1 |

