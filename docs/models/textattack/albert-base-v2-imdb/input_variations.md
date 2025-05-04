# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.add.Tensor                |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  4 | aten.addmm.default             |                  6 |           6 |         0 |          0 | ✅          |       1 |
|  5 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  6 | aten.clone.default             |                  5 |           0 |         5 |          0 | ✅          |       1 |
|  7 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.embedding.default         |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  9 | aten.expand.default            |                  3 |           0 |         3 |          0 | ✅          |       1 |
| 10 | aten.mul.Tensor                |                  5 |           5 |         0 |          0 | ✅          |       1 |
| 11 | aten.native_layer_norm.default |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 12 | aten.permute.default           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 13 | aten.pow.Tensor_Scalar         |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 15 | aten.select.int                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.slice.Tensor              |                  3 |           1 |         2 |          0 | ✅          |       1 |
| 17 | aten.t.default                 |                  5 |           5 |         0 |          0 | ✅          |       1 |
| 18 | aten.tanh.default              |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 19 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 20 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 21 | aten.view.default              |                 11 |          11 |         0 |          0 | ✅          |       1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999545 |     -1 |
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] size = [1, 9, 768] | Done     | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                             | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ? | Done     | Done       | 0.999998 |     -1 |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?    | Done     | Done       | 0.999998 |     -1 |
|  2 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0              | Done     | Done       | 0.999995 |     -1 |
|  3 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?  | Done     | Done       | 0.999998 |     -1 |
|  4 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?    | Done     | Done       | 0.999998 |     -1 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 2]> mat2 = ?       | Done     | Done       | 1        |     -1 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | 0.999967 |     -1 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999969 |     -1 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?   | Done     | Done       | 0.99998  |     -1 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[9, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999944 |     -1 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[9, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999967 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ? | Done     | Done       | 0.999986 |     -1 |
|  1 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?  | Done     | Done       | 0.999992 |     -1 |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 9, 9]> self = ?                                                            | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 768]> self = ?                                                                 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 9, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 9, 128]> self = ?                                                              | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 9, 768]> self = ?                                                              | Removed  | Done       |     1 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0 | Done     | Done       |     1 |     -1 |
### aten.embedding.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                             | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0 | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                           | Done     | Done       |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [1, 12, 64, 9] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]   | Removed  | Done       |     1 |     -1 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | 0.999997 |     -1 |
|  1 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                | Done     | Done       | 0.999995 |     -1 |
|  2 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                     | Done     | Done       | 1        |     -1 |
|  3 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654      | Done     | Done       | 0.999997 |     -1 |
|  4 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?         | Done     | Done       | 0.999996 |     -1 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   | PCC   |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 9, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      0 |
|  1 | Tensor<[1, 9, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      0 |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |     -1 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 9, 3072]> self = ?,<br>number exponent = 3.0 | Done     | Done       | 0.999996 |     -1 |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0 | Done     | Done       |     1 |     -1 |
### aten.select.int
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9                      | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 768]> self = ?    | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[3072, 768]> self = ? | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[768, 128]> self = ?  | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[768, 3072]> self = ? | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[768, 768]> self = ?  | Done     | Done       |     1 |     -1 |
### aten.tanh.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768]> self = ?     | Done     | Done       | 0.999944 |     -1 |
|  1 | Tensor<[1, 9, 3072]> self = ? | Done     | Done       | 0.999942 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1   | Done     | Done       |     1 |     -1 |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 9]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 9]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 64, 9]> self = ?,<br>List[int] size = [12, 64, 9] | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12, 9, 64]> self = ?,<br>List[int] size = [12, 9, 64] | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 12, 9, 9]> self = ?,<br>List[int] size = [12, 9, 9]   | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]       | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 9, 3072]> self = ?,<br>List[int] size = [9, 3072]     | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [1, 9, 12, 64] | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 9, 768]> self = ?,<br>List[int] size = [9, 768]       | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[12, 9, 64]> self = ?,<br>List[int] size = [1, 12, 9, 64] | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[12, 9, 9]> self = ?,<br>List[int] size = [1, 12, 9, 9]   | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[9, 3072]> self = ?,<br>List[int] size = [1, 9, 3072]     | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[9, 768]> self = ?,<br>List[int] size = [1, 9, 768]       | Done     | Done       |     1 |     -1 |

