# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._to_copy.default          |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._unsafe_index.Tensor      |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.add.Tensor                |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
|  3 | aten.arange.default            |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.cat.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.clone.default             |                  1 |           0 |         0 |          1 | ✘           |    0    |
|  6 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.embedding.default         |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.expand.default            |                  2 |           0 |         0 |          1 | ✘           |    0    |
|  9 | aten.mul.Tensor                |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 11 | aten.select.int                |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.slice.Tensor              |                 11 |           1 |         9 |          1 | 🚧          |    0.91 |
| 13 | aten.stack.default             |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.sum.dim_IntList           |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.transpose.int             |                  2 |           1 |         0 |          1 | 🚧          |    0.5  |
| 16 | aten.unsqueeze.default         |                  2 |           0 |         0 |          1 | ✘           |    0    |
| 17 | aten.view.default              |                  4 |           1 |         0 |          2 | 🚧          |    0.25 |
***
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>Optional[int] dtype = torch.int64     | None     | Fallback   | True  |
|  1 | Tensor<[1, 1, 384, 512]> self = ?,<br>Optional[int] dtype = torch.float32 | None     | Fallback   | True  |
|  2 | Tensor<[12]> self = ?,<br>Optional[int] dtype = torch.int64               | None     | Fallback   | True  |
|  3 | Tensor<[16]> self = ?,<br>Optional[int] dtype = torch.int64               | None     | Fallback   | True  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 384, 512]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[12, 1]>, <[16]>] | None     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[12]> self = ?,<br>Tensor other = 0.0                   | None     | Fallback   | True  |
|  2 | Tensor<[16]> self = ?,<br>Tensor other = 0.0                   | None     | Fallback   | True  |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 12,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                         | None     | Fallback   | True  |
|  1 | number end = 12,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  2 | number end = 16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                         | None     | Fallback   | True  |
|  3 | number end = 16,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.cat.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 768, 12, 16]>] | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 768]> self = ? | Fallback | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 384, 512]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?     | None     | Fallback   | True  |
|  1 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ? | None     | Fallback   | True  |
|  2 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?    | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16]> self = ?,<br>List[int] size = [12, 16] | Fallback | Done       | True  |
|  1 | Tensor<[12, 1]> self = ?,<br>List[int] size = [12, 16] | None     | Fallback   | True  |
### aten.mul.Tensor
|    | ATen Input Variations                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12]> self = ?,<br>Tensor other = 32.0 | None     | Fallback   | True  |
|  1 | Tensor<[16]> self = ?,<br>Tensor other = 32.0 | None     | Fallback   | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0 | None     | Fallback   | True  |
|  1 | Tensor<[1, 12]> self = ?,<br>int dim = 1,<br>int index = 0        | None     | Fallback   | True  |
|  2 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>int index = 0        | None     | Fallback   | True  |
|  3 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0            | None     | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 1, 384, 512]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 12]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Fallback   | True  |
|  4 | Tensor<[1, 144, 768]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Fallback   | True  |
|  5 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Fallback   | True  |
|  6 | Tensor<[1, 145, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807    | Done     | Done       | True  |
|  7 | Tensor<[1, 16]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Fallback   | True  |
|  8 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Removed  | Fallback   | True  |
|  9 | Tensor<[1, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Removed  | Fallback   | True  |
| 10 | Tensor<[1, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 8                            | Fallback | Done       | True  |
### aten.stack.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[12, 16]>, <[12, 16]>],<br>int dim = -1 | None     | Fallback   | True  |
### aten.sum.dim_IntList
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [1] | None     | Fallback   | True  |
|  1 | Tensor<[1, 12, 16]> self = ?,<br>Optional[List[int]] dim = [2] | None     | Fallback   | True  |
### aten.transpose.int
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 144, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | True  |
|  1 | Tensor<[1, 768, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Fallback | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 1 | Fallback | Done       | True  |
|  1 | Tensor<[12]> self = ?,<br>int dim = -1         | None     | Fallback   | True  |
### aten.view.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 12, 16]> self = ?,<br>List[int] size = [1, 768, 192] | None     | Fallback   | True  |
|  1 | Tensor<[1, 768, 144]> self = ?,<br>List[int] size = [1, 768, 12, 12] | Fallback | Done       | True  |
|  2 | Tensor<[12]> self = ?,<br>List[int] size = [-1, 1]                   | Fallback | Done       | True  |
|  3 | Tensor<[16]> self = ?,<br>List[int] size = [1, -1]                   | Done     | Done       | True  |

