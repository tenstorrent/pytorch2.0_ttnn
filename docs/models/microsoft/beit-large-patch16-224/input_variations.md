# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  3 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  4 | aten.cat.default               |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  5 | aten.clone.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  6 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  8 | aten.expand.default            |                  4 |           0 |         4 |          0 | ✅          |    1    |
|  9 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.index.Tensor              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.mean.dim                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.mul.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 14 | aten.native_layer_norm.default |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 15 | aten.permute.default           |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 16 | aten.slice.Tensor              |                  3 |           1 |         2 |          0 | ✅          |    1    |
| 17 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 18 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 19 | aten.unsqueeze.default         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 20 | aten.view.default              |                 14 |          13 |         0 |          0 | 🚧          |    0.93 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999586 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?       | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?   | Done     | Done       | 0.999964 |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[197, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | 0.999932 |      0 |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[16, 197, 197]> self = ?,<br>Tensor<[16, 197, 64]> mat2 = ? | Done     | Done       | 0.999971 |      0 |
|  1 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ?  | Done     | Done       | 0.999988 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 1024]>, <[1, 196, 1024]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> self = ?                                                          | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 197, 1024]> self = ?                                                             | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  3 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0 | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]            | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]   | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 197, 4096]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>] | None     | Fallback   |     1 |     -1 |
### aten.mean.dim
|    | ATen Input Variations                                             | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>Optional[List[int]] dim = [1] | Done     | Done       | 0.999998 |      0 |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999966 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ? | Done     | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   | Isolated   | PCC   |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12      | Done     | Done       | N/A   |      1 |
|  1 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]      | Done     | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807 | Done     | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1024, 1024]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1024, 4096]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[4096, 1024]> self = ? | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196] | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197] | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]   | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]   | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [1, 197, 16, 64]  | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]       | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024]  | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]       | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197] | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]       | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                  | None     | Fallback   |     1 |     -1 |
| 12 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]       | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]       | Done     | Done       |     1 |     -1 |

