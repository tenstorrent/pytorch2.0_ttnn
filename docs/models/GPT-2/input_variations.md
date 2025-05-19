# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default          |                  2 |           1 |         1 |          0 | ✅          |       1 |
|  2 | aten.add.Tensor                |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  4 | aten.argmax.default            |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  6 | aten.clone.default             |                  3 |           0 |         3 |          0 | ✅          |       1 |
|  7 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.embedding.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  9 | aten.eq.Scalar                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.expand.default            |                  3 |           0 |         3 |          0 | ✅          |       1 |
| 11 | aten.full.default              |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 12 | aten.index.Tensor              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.mul.Tensor                |                  5 |           5 |         0 |          0 | ✅          |       1 |
| 15 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.permute.default           |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 17 | aten.pow.Tensor_Scalar         |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 18 | aten.remainder.Scalar          |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 19 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 20 | aten.slice.Tensor              |                  6 |           2 |         4 |          0 | ✅          |       1 |
| 21 | aten.split.Tensor              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 22 | aten.sub.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 23 | aten.t.default                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 24 | aten.tanh.default              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 25 | aten.transpose.int             |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 26 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 27 | aten.view.default              |                 17 |          17 |         0 |          0 | ✅          |       1 |
| 28 | aten.where.self                |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999696 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 7]> self = ?,<br>Optional[int] dtype = torch.int32          | Removed  | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                             | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0              | Done     | Done       | 0.999995 |      0 |
|  2 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?  | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?    | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2304]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ? | Done     | Done       | 0.999967 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | 0.999967 |      0 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[7, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999945 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999967 |      0 |
### aten.argmax.default
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = -1 | None     | Fallback   |     1 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ? | Done     | Done       | 0.999987 |      0 |
|  1 | Tensor<[12, 7, 7]> self = ?,<br>Tensor<[12, 7, 64]> mat2 = ?  | Done     | Done       | 0.999992 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 7, 7]> self = ?                                                            | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 7, 768]> self = ?                                                              | Removed  | Done       |     1 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ? | Done     | Done       | 0.999995 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1024, 768]> weight = ?,<br>Tensor indices = ?          | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ? | Done     | Done       | 1.0   | 0      |
### aten.eq.Scalar
|    | ATen Input Variations                            | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 50256 | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [1, 12, 64, 7] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]   | Removed  | Done       |     1 |     -1 |
### aten.full.default
|    | ATen Input Variations                                                                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | Done       |     1 |      0 |
|  1 | List[int] size = [],<br>number fill_value = 8.0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                     | Done     | Done       |     1 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 2]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_arange_1, <[1]>] | None     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ? | Done     | Done       | 0.999951 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                | Done     | Done       | 0.999995 |      0 |
|  2 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                     | Done     | Done       | 1        |      0 |
|  3 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654      | Done     | Done       | 0.999997 |      0 |
|  4 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?         | Done     | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   | PCC   |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 7, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 7, 3072]> self = ?,<br>number exponent = 3.0 | Done     | Done       | 0.999996 |      0 |
### aten.remainder.Scalar
|    | ATen Input Variations                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?,<br>number other = 7 | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0 | Done     | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 7                   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 1, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 7                      | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Removed  | Done       |     1 |     -1 |
### aten.split.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2 | Done     | Done       |     1 |      0 |
### aten.sub.Tensor
|    | ATen Input Variations                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?,<br>Tensor other = 1 | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 768]> self = ? | Done     | Done       |     1 |      0 |
### aten.tanh.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 7, 3072]> self = ? | Done     | Done       | 0.999942 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 7]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [12, 64, 7] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [12, 7, 64] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [12, 7, 7]   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, 768] | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]    | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 7, 768]   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]      | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 12, 64] | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [7, 768]       | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]             | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 7]> self = ?,<br>List[int] size = [1, -1]             | Done     | Done       |     1 |      0 |
| 11 | Tensor<[12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64] | Done     | Done       |     1 |      0 |
| 12 | Tensor<[12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]   | Done     | Done       |     1 |      0 |
| 13 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]     | Done     | Done       |     1 |      0 |
| 14 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2]           | Done     | Done       |     1 |      0 |
| 15 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]     | Done     | Done       |     1 |      0 |
| 16 | Tensor<[7, 768]> self = ?,<br>List[int] size = [1, 7, 768]       | Done     | Done       |     1 |      0 |
### aten.where.self
|    | ATen Input Variations                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> condition = ?,<br>Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ? | Done     | Done       |     1 |      0 |

