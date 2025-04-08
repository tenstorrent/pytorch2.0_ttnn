# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._to_copy.default   |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  1 | aten.all.default        |                  1 |           0 |         0 |          1 | ✘           |       0 |
|  2 | aten.argmax.default     |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.embedding.default  |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  4 | aten.eq.Scalar          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.expand.default     |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  6 | aten.full.default       |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.gt.Scalar          |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.index.Tensor       |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  9 | aten.masked_fill.Scalar |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.mul.Tensor         |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.rsub.Scalar        |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.slice.Tensor       |                  5 |           1 |         4 |          0 | ✅          |       1 |
| 13 | aten.unsqueeze.default  |                  5 |           5 |         0 |          0 | ✅          |       1 |
***
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool     | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16       | Done     | Unknown    | N/A   | N/A    |
### aten.all.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ? | Fallback | Fallback   |     1 |      0 |
### aten.argmax.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = 1,<br>bool keepdim = True | None     | Unknown    | N/A   | N/A    |
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
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>List[int] size = [1, 1, 7, 7] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [1, 1, 7, 7] | Removed  | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | Unknown    | N/A   | N/A    |
### aten.gt.Scalar
|    | ATen Input Variations                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 0 | None     | Unknown    | N/A   | N/A    |
### aten.index.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 7]>] | Removed  | Done       |     1 |      0 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7]> self = ?,<br>Tensor other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                     | Done     | Done       | 1.0   | 0      |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1 | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 7]> self = ?,<br>int dim = 1     | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[7, 7]> self = ?,<br>int dim = 0     | Done     | Unknown    | N/A   | N/A    |

