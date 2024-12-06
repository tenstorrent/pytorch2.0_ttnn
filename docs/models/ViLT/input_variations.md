# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._to_copy.default          |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
|  1 | aten._unsafe_index.Tensor      |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.add.Tensor                |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
|  3 | aten.arange.default            |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.cat.default               |                  1 |           0 |         1 |          0 | ✅          |    1    |
|  5 | aten.clone.default             |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  6 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.embedding.default         |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  8 | aten.expand.default            |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
|  9 | aten.mul.Tensor                |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 11 | aten.select.int                |                  4 |           3 |         0 |          1 | 🚧          |    0.75 |
| 12 | aten.slice.Tensor              |                 11 |           2 |         9 |          0 | ✅          |    1    |
| 13 | aten.stack.default             |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.sum.dim_IntList           |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 16 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 17 | aten.view.default              |                  4 |           4 |         0 |          0 | ✅          |    1    |
***
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>Optional[int] dtype = torch.int64     | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 384, 512]> self = ?,<br>Optional[int] dtype = torch.float32 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[12]> self = ?,<br>Optional[int] dtype = torch.int64               | None     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16]> self = ?,<br>Optional[int] dtype = torch.int64               | None     | Unknown    | N/A   | N/A    |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 384, 512]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[12, 1]>, <[16]>] | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[12]> self = ?,<br>Tensor other = 0.0                   | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[16]> self = ?,<br>Tensor other = 0.0                   | None     | Unknown    | N/A   | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number end = 12,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                         | None     | Unknown    | N/A   | N/A    |
|  1 | number end = 12,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
|  2 | number end = 16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                         | None     | Unknown    | N/A   | N/A    |
|  3 | number end = 16,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 768, 12, 16]>] | Removed  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 8, 768]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 384, 512]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?    | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16]> self = ?,<br>List[int] size = [12, 16] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[12, 1]> self = ?,<br>List[int] size = [12, 16] | None     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[12]> self = ?,<br>Tensor other = 32.0 | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[16]> self = ?,<br>Tensor other = 32.0 | None     | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0            | Fallback | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 12]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 144, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807    | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                            | Done     | Unknown    | N/A   | N/A    |
### aten.stack.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[12, 16]>, <[12, 16]>],<br>int dim = -1 | None     | Unknown    | N/A   | N/A    |
### aten.sum.dim_IntList
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [1] | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [2] | None     | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 144, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 768, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[12]> self = ?,<br>int dim = -1         | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int] size = [1, 768, 192] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 768, 144]> self = ?,<br>List[int] size = [1, 768, 12, 12] | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[12]> self = ?,<br>List[int] size = [-1, 1]                   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16]> self = ?,<br>List[int] size = [1, -1]                   | Done     | Unknown    | N/A   | N/A    |

