# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  1 | aten._to_copy.default          |                  4 |           2 |         0 |          0 | 🚧          |     0.5 |
|  2 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  3 | aten.add.Tensor                |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  4 | aten.addmm.default             |                  3 |           3 |         0 |          0 | ✅          |     1   |
|  5 | aten.arange.start              |                  1 |           0 |         1 |          0 | ✅          |     1   |
|  6 | aten.bmm.default               |                  3 |           3 |         0 |          0 | ✅          |     1   |
|  7 | aten.clone.default             |                  5 |           5 |         0 |          0 | ✅          |     1   |
|  8 | aten.embedding.default         |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  9 | aten.expand.default            |                  4 |           1 |         3 |          0 | ✅          |     1   |
| 10 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 11 | aten.masked_fill.Scalar        |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 12 | aten.mul.Tensor                |                  2 |           1 |         0 |          0 | 🚧          |     0.5 |
| 13 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 14 | aten.rsub.Scalar               |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 15 | aten.slice.Tensor              |                  6 |           1 |         5 |          0 | ✅          |     1   |
| 16 | aten.sub.Tensor                |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 17 | aten.t.default                 |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 18 | aten.transpose.int             |                  6 |           6 |         0 |          0 | ✅          |     1   |
| 19 | aten.unsqueeze.default         |                  4 |           3 |         1 |          0 | ✅          |     1   |
| 20 | aten.view.default              |                 15 |          15 |         0 |          0 | ✅          |     1   |
***
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[12, 24, 24]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int] dtype = torch.bfloat16  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 24]> self = ?,<br>Optional[int] dtype = torch.bool      | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 24, 24]> self = ?,<br>Optional[int] dtype = torch.bool     | None     | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 24, 12, 64]> self = ?,<br>List[int] size = [1, 24, 768] | Done     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?      | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?      | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                      | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[768]> self = ?,<br>Tensor<[24, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[24, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number start = 0,<br>number end = 24,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 24, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 24, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 24, 3072]> self = ?                                                             | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 24, 768]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[12, 24, 24]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                        | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 1, 24]  | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 24]> self = ?,<br>List[int] size = [1, 1, 24, 24] | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]    | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]    | Removed  | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 24, 3072]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> mask = ?,<br>number value = -3.3895313892515355e+38   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ? | None     | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 24, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 24]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 24]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 600, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 24                  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[24]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ? | None     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3072, 768]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[768, 3072]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[768, 768]> self = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 24, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1    | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[24, 12, 24]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[24, 24, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1  | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 24]> self = ?,<br>int dim = 2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 24]> self = ?,<br>int dim = 1    | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[24]> self = ?,<br>int dim = 0       | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[24]> self = ?,<br>int dim = 1       | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64] | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 24, 3072]> self = ?,<br>List[int] size = [24, 3072]     | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64] | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [1, 24, 12, 64] | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 24, 768]> self = ?,<br>List[int] size = [24, 768]       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [1, 12, 24, 24] | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[12, 24, 24]> self = ?,<br>List[int] size = [12, 24, 24]    | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [1, 12, 24, 64] | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[12, 24, 64]> self = ?,<br>List[int] size = [12, -1, 64]    | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[24, 12, 24]> self = ?,<br>List[int] size = [24, 12, 24]    | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[24, 12, 64]> self = ?,<br>List[int] size = [24, 12, 64]    | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[24, 3072]> self = ?,<br>List[int] size = [1, 24, 3072]     | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[24, 64, 24]> self = ?,<br>List[int] size = [24, 64, 24]    | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[24, 768]> self = ?,<br>List[int] size = [1, 24, 768]       | Done     | Unknown    | N/A   | N/A    |

