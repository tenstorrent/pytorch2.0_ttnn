# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._to_copy.default          |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
|  1 | aten._unsafe_index.Tensor      |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.add.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.cat.default               |                  1 |           0 |         1 |          0 | ✅          |    1    |
|  4 | aten.clone.default             |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  5 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.embedding.default         |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  7 | aten.expand.default            |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.select.int                |                  4 |           3 |         0 |          1 | 🚧          |    0.75 |
| 10 | aten.slice.Tensor              |                 11 |           2 |         9 |          0 | ✅          |    1    |
| 11 | aten.stack.default             |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.sum.dim_IntList           |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 14 | aten.unsqueeze.default         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 15 | aten.view.default              |                  3 |           3 |         0 |          0 | ✅          |    1    |
***
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>Optional[int] dtype = torch.int64     | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1, 384, 512]> self = ?,<br>Optional[int] dtype = torch.float32 | Done     | Fallback   |     1 |     -1 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 384, 512]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, _folded_unsqueeze_1, _folded__to_copy_2] | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.cat.default
|    | ATen Input Variations                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 768, 12, 16]>] | Removed  | Done       |     1 |     -1 |
### aten.clone.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 8, 768]> self = ? | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 384, 512]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?     | Done     | Done       |     1 |      0 |
|  1 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?    | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[12, 1]> self = ?,<br>List[int] size = [12, 16] | None     | Fallback   |     1 |     -1 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   | PCC   |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |      1 |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0            | Fallback | Fallback   |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 12]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 144, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807    | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                            | Done     | Done       |     1 |     -1 |
### aten.stack.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[12, 16]>, _folded_expand_1],<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
### aten.sum.dim_IntList
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [1] | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [2] | None     | Fallback   |     1 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 144, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 768, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int] size = [1, 768, 192] | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 768, 144]> self = ?,<br>List[int] size = [1, 768, 12, 12] | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[12]> self = ?,<br>List[int] size = [-1, 1]                   | Done     | Done       |     1 |     -1 |

