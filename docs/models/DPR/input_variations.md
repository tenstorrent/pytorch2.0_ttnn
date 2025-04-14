# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default             |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  4 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  5 | aten.clone.default             |                  4 |           0 |         4 |          0 | ✅          |       1 |
|  6 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.embedding.default         |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  8 | aten.expand.default            |                  4 |           0 |         4 |          0 | ✅          |       1 |
|  9 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.mul.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.permute.default           |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 13 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.select.int                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 15 | aten.slice.Tensor              |                  6 |           1 |         5 |          0 | ✅          |       1 |
| 16 | aten.split.Tensor              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 17 | aten.squeeze.dim               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 18 | aten.t.default                 |                  5 |           5 |         0 |          0 | ✅          |       1 |
| 19 | aten.transpose.int             |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 20 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 21 | aten.view.default              |                 14 |          14 |         0 |          0 | ✅          |       1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999594 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?     | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1]> mat2 = ?        | Done     | Done       | 1        |      0 |
|  1 | Tensor<[2]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 2]> mat2 = ?       | Done     | Done       | 0.999965 |      0 |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | 0.999967 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[25, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999944 |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999967 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ? | Done     | Done       | 0.999989 |      0 |
|  1 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ? | Done     | Done       | 0.999986 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 25, 25]> self = ?                                                           | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 25, 768]> self = ?                                                              | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1, 25]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       |     1 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0 | Done     | Done       |     1 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                             | Done     | Done       |     1 |      0 |
|  1 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                           | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [1, 12, 64, 25] | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                 | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 25, 3072]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 25, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0 | Done     | Done       | 0.999997 |      0 |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 25]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 25                       | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       |     1 |     -1 |
### aten.split.Tensor
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1 | Done     | Done       |     1 |      0 |
### aten.squeeze.dim
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 25, 1]> self = ?,<br>int dim = -1 | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768]> self = ?    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 768]> self = ?    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[3072, 768]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[768, 3072]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[768, 768]> self = ?  | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 25, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 25]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 25]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [12, 25, 25] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [12, 25, 64] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [12, 64, 25] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1]                   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] size = [1, 25, 768] | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 25, 3072]> self = ?,<br>List[int] size = [25, 3072]     | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [1, 25, 12, 64] | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [25, 768]       | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]              | Done     | Done       |     1 |      0 |
|  9 | Tensor<[12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25] | Done     | Done       |     1 |      0 |
| 10 | Tensor<[12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64] | Done     | Done       |     1 |      0 |
| 11 | Tensor<[25, 2]> self = ?,<br>List[int] size = [1, 25, 2]           | Done     | Done       |     1 |      0 |
| 12 | Tensor<[25, 3072]> self = ?,<br>List[int] size = [1, 25, 3072]     | Done     | Done       |     1 |      0 |
| 13 | Tensor<[25, 768]> self = ?,<br>List[int] size = [1, 25, 768]       | Done     | Done       |     1 |      0 |

