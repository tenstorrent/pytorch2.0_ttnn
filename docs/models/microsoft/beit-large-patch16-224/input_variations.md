# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default             |                  4 |           0 |         0 |          4 | ✘           |    0    |
|  3 | aten.bmm.default               |                  2 |           0 |         0 |          2 | ✘           |    0    |
|  4 | aten.cat.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.clone.default             |                  4 |           2 |         0 |          2 | 🚧          |    0.5  |
|  6 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.expand.default            |                  4 |           0 |         4 |          0 | ✅          |    1    |
|  9 | aten.gelu.default              |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 10 | aten.index.Tensor              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.mean.dim                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.mm.default                |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 13 | aten.mul.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 14 | aten.native_layer_norm.default |                  2 |           1 |         0 |          1 | 🚧          |    0.5  |
| 15 | aten.permute.default           |                  3 |           2 |         0 |          1 | 🚧          |    0.67 |
| 16 | aten.slice.Tensor              |                  3 |           0 |         2 |          1 | 🚧          |    0.67 |
| 17 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 18 | aten.transpose.int             |                  2 |           0 |         0 |          2 | ✘           |    0    |
| 19 | aten.unsqueeze.default         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 20 | aten.view.default              |                 14 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ? | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?       | Done     | Unknown    | N/A   |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ?   | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[197, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Fallback | Unknown    | N/A   |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[197, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Fallback | Unknown    | N/A   |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 197, 197]> self = ?,<br>Tensor<[16, 197, 64]> mat2 = ? | Fallback | Unknown    | N/A   |
|  1 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ?  | Fallback | Unknown    | N/A   |
### aten.cat.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 1024]>, <[1, 196, 1024]>],<br>int dim = 1 | None     | Unknown    | N/A   |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?                                                          | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> self = ?                                                             | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 197, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Fallback | Unknown    | N/A   |
|  3 | Tensor<[16, 197, 197]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Unknown    | N/A   |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[1024, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Unknown    | N/A   |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0 | None     | Unknown    | N/A   |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, -1]            | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197] | Removed  | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | Removed  | Unknown    | N/A   |
|  3 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [1, 16, 64, 197]   | Removed  | Unknown    | N/A   |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 4096]> self = ? | Fallback | Unknown    | N/A   |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>] | None     | Unknown    | N/A   |
### aten.mean.dim
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>Optional[List[int]] dim = [1] | None     | Unknown    | N/A   |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[197, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Fallback | Unknown    | N/A   |
### aten.mul.Tensor
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ? | Done     | Unknown    | N/A   |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12      | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Fallback | Unknown    | N/A   |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Fallback | Unknown    | N/A   |
|  2 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]      | Done     | Unknown    | N/A   |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 196, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  2 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807 | Fallback | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 1024]> self = ? | Done     | Unknown    | N/A   |
|  1 | Tensor<[1024, 1024]> self = ? | Done     | Unknown    | N/A   |
|  2 | Tensor<[1024, 4096]> self = ? | Done     | Unknown    | N/A   |
|  3 | Tensor<[4096, 1024]> self = ? | Done     | Unknown    | N/A   |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Fallback | Unknown    | N/A   |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0 | Done     | Unknown    | N/A   |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 14, 14]> self = ?,<br>List[int] size = [1, 1024, 196] | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 16, 197, 197]> self = ?,<br>List[int] size = [16, 197, 197] | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] size = [16, 197, 64]   | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 16, 64, 197]> self = ?,<br>List[int] size = [16, 64, 197]   | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [1, 197, 16, 64]  | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 197, 1024]> self = ?,<br>List[int] size = [197, 1024]       | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] size = [1, 197, 1024]  | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 197, 4096]> self = ?,<br>List[int] size = [197, 4096]       | None     | Unknown    | N/A   |
|  8 | Tensor<[16, 197, 197]> self = ?,<br>List[int] size = [1, 16, 197, 197] | None     | Unknown    | N/A   |
|  9 | Tensor<[16, 197, 64]> self = ?,<br>List[int] size = [1, 16, 197, 64]   | None     | Unknown    | N/A   |
| 10 | Tensor<[197, 1024]> self = ?,<br>List[int] size = [1, 197, 1024]       | None     | Unknown    | N/A   |
| 11 | Tensor<[197, 197]> self = ?,<br>List[int] size = [-1]                  | None     | Unknown    | N/A   |
| 12 | Tensor<[197, 4096]> self = ?,<br>List[int] size = [1, 197, 4096]       | None     | Unknown    | N/A   |
| 13 | Tensor<[38809, 16]> self = ?,<br>List[int] size = [197, 197, -1]       | None     | Unknown    | N/A   |

