# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._to_copy.default          |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.add.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.addmm.default             |                  4 |           0 |         0 |          4 | ✘           |    0    |
|  4 | aten.bmm.default               |                  2 |           0 |         0 |          2 | ✘           |    0    |
|  5 | aten.cat.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.clone.default             |                  3 |           1 |         0 |          2 | 🚧          |    0.33 |
|  7 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.expand.default            |                  4 |           0 |         4 |          0 | ✅          |    1    |
| 10 | aten.gelu.default              |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 11 | aten.native_layer_norm.default |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 12 | aten.permute.default           |                  2 |           1 |         0 |          1 | 🚧          |    0.5  |
| 13 | aten.select.int                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.slice.Tensor              |                  2 |           0 |         2 |          0 | ✅          |    1    |
| 15 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 16 | aten.transpose.int             |                  2 |           0 |         0 |          2 | ✘           |    0    |
| 17 | aten.view.default              |                 12 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Unknown    | N/A   |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | None     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ? | Done     | Unknown    | N/A   |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Fallback | Unknown    | N/A   |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Fallback | Unknown    | N/A   |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[197, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Fallback | Unknown    | N/A   |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Fallback | Unknown    | N/A   |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ? | Fallback | Unknown    | N/A   |
|  1 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?  | Fallback | Unknown    | N/A   |
### aten.cat.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 196, 768]>],<br>int dim = 1 | None     | Unknown    | N/A   |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?                                                          | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Fallback | Unknown    | N/A   |
|  2 | Tensor<[1, 197, 768]> self = ?                                                              | Done     | Unknown    | N/A   |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Unknown    | N/A   |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0 | None     | Unknown    | N/A   |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Removed  | Unknown    | N/A   |
|  2 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Removed  | Unknown    | N/A   |
|  3 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Removed  | Unknown    | N/A   |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 3072]> self = ? | Fallback | Unknown    | N/A   |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Fallback | Unknown    | N/A   |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Fallback | Unknown    | N/A   |
### aten.select.int
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | None     | Unknown    | N/A   |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 768]> self = ? | Done     | Unknown    | N/A   |
|  1 | Tensor<[3072, 768]> self = ? | Done     | Unknown    | N/A   |
|  2 | Tensor<[768, 3072]> self = ? | Done     | Unknown    | N/A   |
|  3 | Tensor<[768, 768]> self = ?  | Done     | Unknown    | N/A   |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Fallback | Unknown    | N/A   |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197] | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]   | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]   | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]   | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]       | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]   | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]         | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]   | None     | Unknown    | N/A   |
|  8 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | None     | Unknown    | N/A   |
|  9 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | None     | Unknown    | N/A   |
| 10 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]       | None     | Unknown    | N/A   |
| 11 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]         | None     | Unknown    | N/A   |

