# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  4 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  5 | aten.clone.default             |                  4 |           0 |         4 |          0 | ✅          |       1 |
|  6 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.embedding.default         |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  8 | aten.expand.default            |                  3 |           0 |         3 |          0 | ✅          |       1 |
|  9 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.mul.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.permute.default           |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 13 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.slice.Tensor              |                  4 |           1 |         3 |          0 | ✅          |       1 |
| 15 | aten.split.Tensor              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.squeeze.dim               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 17 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 18 | aten.transpose.int             |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 19 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 20 | aten.view.default              |                 12 |          12 |         0 |          0 | ✅          |       1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999596 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor<[1, 1, 1, 256]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?    | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[256, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | 0.999933 |      0 |
|  2 | Tensor<[2]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 2]> mat2 = ?       | Done     | Done       | 0.999972 |      0 |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[16, 256, 256]> self = ?,<br>Tensor<[16, 256, 64]> mat2 = ? | Done     | Done       | 0.999979 |      0 |
|  1 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ?  | Done     | Done       | 0.999986 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 256, 256]> self = ?                                                          | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 256, 1024]> self = ?                                                             | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[1, 256]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Removed  | Done       |     1 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0 | Done     | Done       |     1 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                             | Done     | Done       |     1 |      0 |
|  1 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                           | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]   | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [1, 16, 64, 256]   | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 256, 4096]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | 0.999995 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   | Isolated   | PCC   |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 256, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0 | Done     | Done       | 0.999993 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 256]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 256                       | Done     | Done       |     1 |      0 |
### aten.split.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1 | Done     | Done       |     1 |      0 |
### aten.squeeze.dim
|    | ATen Input Variations                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 1]> self = ?,<br>int dim = -1 | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1024, 4096]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[2, 1024]> self = ?    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[4096, 1024]> self = ? | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 256, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 256]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int] size = [16, 256, 256] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] size = [16, 256, 64]   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int] size = [16, 64, 256]   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [1, 256, 16, 64]  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] size = [256, 1024]       | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] size = [1, 256, 1024]  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] size = [256, 4096]       | Done     | Done       |     1 |      0 |
|  7 | Tensor<[16, 256, 256]> self = ?,<br>List[int] size = [1, 16, 256, 256] | Done     | Done       |     1 |      0 |
|  8 | Tensor<[16, 256, 64]> self = ?,<br>List[int] size = [1, 16, 256, 64]   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[256, 1024]> self = ?,<br>List[int] size = [1, 256, 1024]       | Done     | Done       |     1 |      0 |
| 10 | Tensor<[256, 2]> self = ?,<br>List[int] size = [1, 256, 2]             | Done     | Done       |     1 |      0 |
| 11 | Tensor<[256, 4096]> self = ?,<br>List[int] size = [1, 256, 4096]       | Done     | Done       |     1 |      0 |

