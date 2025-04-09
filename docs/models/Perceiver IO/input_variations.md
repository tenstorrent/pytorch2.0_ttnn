# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.add.Tensor                |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default             |                  6 |           6 |         0 |          0 | ✅          |       1 |
|  4 | aten.bmm.default               |                  6 |           6 |         0 |          0 | ✅          |       1 |
|  5 | aten.clone.default             |                  5 |           0 |         5 |          0 | ✅          |       1 |
|  6 | aten.div.Tensor                |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  7 | aten.embedding.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  8 | aten.expand.default            |                 12 |           2 |        10 |          0 | ✅          |       1 |
|  9 | aten.gelu.default              |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 10 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.mul.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.native_layer_norm.default |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 13 | aten.permute.default           |                  7 |           7 |         0 |          0 | ✅          |       1 |
| 14 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 15 | aten.slice.Tensor              |                  2 |           0 |         2 |          0 | ✅          |       1 |
| 16 | aten.t.default                 |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 17 | aten.transpose.int             |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 18 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 19 | aten.view.default              |                 32 |          32 |         0 |          0 | ✅          |       1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 8, 2048, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999595 |      0 |
|  1 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999525 |      0 |
|  2 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | 0.999589 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?        | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ? | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                 | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1280]> self = ?,<br>Tensor<[2048, 768]> mat1 = ?,<br>Tensor<[768, 1280]> mat2 = ?  | Done     | Done       | 0.999962 |      0 |
|  1 | Tensor<[1280]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Done     | Done       | 0.999962 |      0 |
|  2 | Tensor<[256]> self = ?,<br>Tensor<[2048, 768]> mat1 = ?,<br>Tensor<[768, 256]> mat2 = ?    | Done     | Done       | 0.999967 |      0 |
|  3 | Tensor<[256]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 256]> mat2 = ?   | Done     | Done       | 0.999946 |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[2048, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Done     | Done       | 0.999962 |      0 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 768]> mat2 = ?   | Done     | Done       | 0.999962 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                               | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[8, 2048, 256]> self = ?,<br>Tensor<[8, 256, 96]> mat2 = ?   | Done     | Done       | 0.999975 |      0 |
|  1 | Tensor<[8, 2048, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?    | Done     | Done       | 0.999989 |      0 |
|  2 | Tensor<[8, 256, 2048]> self = ?,<br>Tensor<[8, 2048, 160]> mat2 = ? | Done     | Done       | 0.999921 |      0 |
|  3 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 160]> mat2 = ?   | Done     | Done       | 0.999979 |      0 |
|  4 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?    | Done     | Done       | 0.999989 |      0 |
|  5 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?     | Done     | Done       | 0.999989 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 8, 2048, 256]> self = ?                                                          | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1, 8, 256, 2048]> self = ?                                                          | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[1, 8, 256, 256]> self = ?                                                           | Removed  | Done       |     1 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.999996 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2048, 768]> weight = ?,<br>Tensor indices = ?           | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ? | Done     | Done       | 1.0   | 0      |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [1, 8, 2048, 160] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [1, 8, 2048, 32]   | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]   | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048] | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]   | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]     | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [1, 8, 256, 96]     | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [1, 8, 32, 2048]   | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]     | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Done     | Done       |     1 |      0 |
| 11 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, -1, -1]             | Done     | Done       |     1 |      0 |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2048, 768]> self = ? | Done     | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 256, 1280]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2048, 768]> self = ?,<br>Tensor<[768, 262]> mat2 = ? | Done     | Done       | 0.999968 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | 0.999995 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   | Isolated   | PCC   |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 2048, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | N/A   |      1 |
|  1 | Tensor<[1, 256, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 2048, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 8, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 8, 2048, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0 | Done     | Done       | 0.999994 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1280, 1280]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1280, 768]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[256, 1280]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[256, 768]> self = ?   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[768, 1280]> self = ?  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[768, 768]> self = ?   | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 8, 2048, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[262, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 2048]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 8, 160] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 2048, 256]> self = ?,<br>List[int] size = [1, 2048, 8, 32]   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [-1, 768]          | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [2048, 768]        | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 2048, 8, 96]> self = ?,<br>List[int] size = [1, 2048, 768]   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, 256, 8, 160]   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]        | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]     | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 256, 8, 96]     | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, 256, 1280]   | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [8, 2048, 160]  | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [8, 2048, 256]  | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [8, 2048, 32]    | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [8, 256, 160]    | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [8, 256, 2048]  | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]    | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]      | Done     | Done       |     1 |      0 |
| 17 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [8, 256, 96]      | Done     | Done       |     1 |      0 |
| 18 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [8, 32, 2048]    | Done     | Done       |     1 |      0 |
| 19 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]      | Done     | Done       |     1 |      0 |
| 20 | Tensor<[2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 1280]      | Done     | Done       |     1 |      0 |
| 21 | Tensor<[2048, 256]> self = ?,<br>List[int] size = [1, 2048, 256]        | Done     | Done       |     1 |      0 |
| 22 | Tensor<[2048, 262]> self = ?,<br>List[int] size = [1, 2048, 262]        | Done     | Done       |     1 |      0 |
| 23 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, 2048, 768]        | Done     | Done       |     1 |      0 |
| 24 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, 256, 1280]        | Done     | Done       |     1 |      0 |
| 25 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]          | Done     | Done       |     1 |      0 |
| 26 | Tensor<[256, 768]> self = ?,<br>List[int] size = [1, 256, 768]          | Done     | Done       |     1 |      0 |
| 27 | Tensor<[8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]  | Done     | Done       |     1 |      0 |
| 28 | Tensor<[8, 2048, 96]> self = ?,<br>List[int] size = [1, 8, 2048, 96]    | Done     | Done       |     1 |      0 |
| 29 | Tensor<[8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]    | Done     | Done       |     1 |      0 |
| 30 | Tensor<[8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]  | Done     | Done       |     1 |      0 |
| 31 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]    | Done     | Done       |     1 |      0 |

