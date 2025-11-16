# High Level Operations Status
|    | Operations                                |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_multi_head_attention.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten.add.Tensor                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                        |                  3 |           1 |         2 |          0 | ✅          |       1 |
|  3 | aten.cat.default                          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  4 | aten.clone.default                        |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  5 | aten.convolution.default                  |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.expand.default                       |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  7 | aten.gelu.default                         |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  8 | aten.native_layer_norm.default            |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.permute.default                      |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.select.int                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.slice.Tensor                         |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 12 | aten.t.default                            |                  3 |           0 |         3 |          0 | ✅          |       1 |
| 13 | aten.view.default                         |                  5 |           4 |         1 |          0 | ✅          |       1 |
***
### aten._native_multi_head_attention.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 50, 768]> query = ?,<br>Tensor<[1, 50, 768]> key = ?,<br>Tensor<[1, 50, 768]> value = ?,<br>int embed_dim = 768,<br>int num_head = 12,<br>Tensor<[2304, 768]> qkv_weight = ?,<br>Tensor<[2304]> qkv_bias = ?,<br>Tensor<[768, 768]> proj_weight = ?,<br>Tensor<[768]> proj_bias = ?,<br>Optional[Tensor] mask = ?,<br>bool need_weights = False | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?  | Done     | Done       | 0.999968 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Removed  | Done       | 0.999967 |      0 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Removed  | Done       | 0.999944 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 49, 768]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 50, 768]> self = ?  | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1] | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ? | Removed  | Done       | 0.999991 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Done     | Done       | 0.997205 |      3 |
### aten.permute.default
|    | ATen Input Variations                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768, 49]> self = ?,<br>List[int] dims = [0, 2, 1] | Done     | Done       |     1 |      0 |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 768]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[3072, 768]> self = ? | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[768, 3072]> self = ? | Removed  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]      | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]    | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]      | Done     | Done       |     1 |      0 |

