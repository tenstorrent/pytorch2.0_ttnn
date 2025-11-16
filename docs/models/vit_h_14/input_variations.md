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
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1370, 1280]> query = ?,<br>Tensor<[1, 1370, 1280]> key = ?,<br>Tensor<[1, 1370, 1280]> value = ?,<br>int embed_dim = 1280,<br>int num_head = 16,<br>Tensor<[3840, 1280]> qkv_weight = ?,<br>Tensor<[3840]> qkv_bias = ?,<br>Tensor<[1280, 1280]> proj_weight = ?,<br>Tensor<[1280]> proj_bias = ?,<br>Optional[Tensor] mask = ?,<br>bool need_weights = False | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ?    | Done     | Done       | 0.999961 |      0 |
|  1 | Tensor<[1280]> self = ?,<br>Tensor<[1370, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ? | Removed  | Done       | 0.999802 |      0 |
|  2 | Tensor<[5120]> self = ?,<br>Tensor<[1370, 1280]> mat1 = ?,<br>Tensor<[1280, 5120]> mat2 = ? | Removed  | Done       | 0.999946 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 1280]>, <[1, 1369, 1280]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1370, 5120]> self = ? | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 518, 518]> input = ?,<br>Tensor<[1280, 3, 14, 14]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [14, 14],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, -1, -1] | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1370, 5120]> self = ? | Removed  | Done       | 0.999991 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                         | Status   | Isolated   |    PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|-------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-06 | Done     | Done       | 0.9967 |      3 |
### aten.permute.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1280, 1369]> self = ?,<br>List[int] dims = [0, 2, 1] | Done     | Done       |     1 |      0 |
### aten.select.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1280]> self = ? | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1280, 5120]> self = ? | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[5120, 1280]> self = ? | Removed  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1280, 37, 37]> self = ?,<br>List[int] size = [1, 1280, 1369] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1370, 1280]> self = ?,<br>List[int] size = [1370, 1280]      | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1370, 5120]> self = ?,<br>List[int] size = [1370, 5120]      | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1, 1370, 1280]      | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1370, 5120]> self = ?,<br>List[int] size = [1, 1370, 5120]      | Removed  | Done       |     1 |      0 |

