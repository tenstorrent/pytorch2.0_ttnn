# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._to_copy.default          |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  3 | aten.addmm.default             |                  5 |           5 |         0 |          0 | ✅          |    1    |
|  4 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  5 | aten.clone.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  6 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.embedding.default         |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.expand.default            |                  4 |           0 |         4 |          0 | ✅          |    1    |
|  9 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.mul.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 11 | aten.native_layer_norm.default |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 12 | aten.permute.default           |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 13 | aten.rsub.Scalar               |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.select.int                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.slice.Tensor              |                  6 |           0 |         5 |          0 | 🚧          |    0.83 |
| 16 | aten.split.Tensor              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 17 | aten.squeeze.dim               |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 18 | aten.t.default                 |                  5 |           5 |         0 |          0 | ✅          |    1    |
| 19 | aten.transpose.int             |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 20 | aten.unsqueeze.default         |                  2 |           1 |         0 |          1 | 🚧          |    0.5  |
| 21 | aten.view.default              |                 14 |          11 |         0 |          3 | 🚧          |    0.79 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | None     | Fallback   | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?     | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1]> mat2 = ?        | Done     | Done       | True  |
|  1 | Tensor<[2]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 2]> mat2 = ?       | Done     | Done       | True  |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[25, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | True  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | True  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ? | Done     | Done       | True  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?                                                           | Done     | Done       | True  |
|  1 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  2 | Tensor<[1, 25, 768]> self = ?                                                              | Done     | Done       | True  |
|  3 | Tensor<[1, 25]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Done     | Done       | True  |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0 | None     | Fallback   | True  |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                             | None     | Fallback   | True  |
|  1 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0 | None     | Fallback   | True  |
|  2 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                           | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25] | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64] | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [1, 12, 64, 25] | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]                 | Removed  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 25, 3072]> self = ? | Done     | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 25, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Fallback | Done       | N/A   |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
|  1 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0 | None     | Fallback   | True  |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | None     | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 25]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Fallback   | True  |
|  4 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 25                       | None     | Fallback   | True  |
|  5 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Fallback   | True  |
### aten.split.Tensor
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1 | Done     | Done       | True  |
### aten.squeeze.dim
|    | ATen Input Variations                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 25, 1]> self = ?,<br>int dim = -1 | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> self = ?    | Done     | Done       | True  |
|  1 | Tensor<[2, 768]> self = ?    | Done     | Done       | True  |
|  2 | Tensor<[3072, 768]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[768, 3072]> self = ? | Done     | Done       | True  |
|  4 | Tensor<[768, 768]> self = ?  | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 25, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 25]> self = ?,<br>int dim = 2 | Fallback | Done       | True  |
|  1 | Tensor<[1, 25]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int] size = [12, 25, 25] | Done     | Done       | True  |
|  1 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] size = [12, 25, 64] | Done     | Done       | True  |
|  2 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int] size = [12, 64, 25] | Done     | Done       | True  |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1]                   | Fallback | Done       | True  |
|  4 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] size = [1, 25, 768] | Done     | Done       | True  |
|  5 | Tensor<[1, 25, 3072]> self = ?,<br>List[int] size = [25, 3072]     | Done     | Done       | True  |
|  6 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [1, 25, 12, 64] | Done     | Done       | True  |
|  7 | Tensor<[1, 25, 768]> self = ?,<br>List[int] size = [25, 768]       | Done     | Done       | True  |
|  8 | Tensor<[1, 25]> self = ?,<br>List[int] size = [1, 25]              | Fallback | Done       | True  |
|  9 | Tensor<[12, 25, 25]> self = ?,<br>List[int] size = [1, 12, 25, 25] | Fallback | Done       | True  |
| 10 | Tensor<[12, 25, 64]> self = ?,<br>List[int] size = [1, 12, 25, 64] | Done     | Done       | True  |
| 11 | Tensor<[25, 2]> self = ?,<br>List[int] size = [1, 25, 2]           | Done     | Done       | True  |
| 12 | Tensor<[25, 3072]> self = ?,<br>List[int] size = [1, 25, 3072]     | Done     | Done       | True  |
| 13 | Tensor<[25, 768]> self = ?,<br>List[int] size = [1, 25, 768]       | Done     | Done       | True  |

