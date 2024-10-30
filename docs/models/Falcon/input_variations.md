# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  2 | aten.add.Tensor                |                  4 |           3 |         0 |          0 | 🚧          |    0.75 |
|  3 | aten.all.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.arange.start              |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  6 | aten.cat.default               |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default             |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  8 | aten.embedding.default         |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.eq.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.expand.default            |                  4 |           1 |         2 |          0 | 🚧          |    0.75 |
| 11 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 12 | aten.index.Tensor              |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.lift_fresh_copy.default   |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.logical_not.default       |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 15 | aten.masked_fill.Scalar        |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.mm.default                |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 17 | aten.mul.Scalar                |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.mul.Tensor                |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 19 | aten.native_layer_norm.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.neg.default               |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 21 | aten.ones.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.permute.default           |                  5 |           5 |         0 |          0 | ✅          |    1    |
| 23 | aten.slice.Tensor              |                  8 |           6 |         2 |          0 | ✅          |    1    |
| 24 | aten.transpose.int             |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 25 | aten.tril.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 26 | aten.unsqueeze.default         |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 27 | aten.view.default              |                 13 |          13 |         0 |          0 | ✅          |    1    |
| 28 | aten.zeros_like.default        |                  1 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 71, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
### aten._unsafe_view.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7, 71, 64]> self = ?,<br>List[int] size = [1, 7, 4544] | Done     | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?   | Done     | Done       | True  |
|  1 | Tensor<[1, 7, 4544]> self = ?,<br>Tensor<[1, 7, 4544]> other = ?     | Done     | Done       | True  |
|  2 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 71, 7, 7]> self = ?,<br>Tensor<[7, 7]> other = ?          | None     | Fallback   | True  |
### aten.all.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7]> self = ? | None     | Fallback   | True  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number start = 0,<br>number end = 7,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[71, 7, 7]> self = ?,<br>Tensor<[71, 7, 64]> mat2 = ?  | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 7, 32]>, <[1, 1, 7, 32]>],<br>int dim = -1   | None     | Fallback   | True  |
|  1 | List[Tensor] tensors = [<[1, 71, 7, 32]>, <[1, 71, 7, 32]>],<br>int dim = -1 | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7, 4544]> self = ?                                                             | Done     | Done       | True  |
|  1 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ? | None     | Fallback   | True  |
### aten.eq.Scalar
|    | ATen Input Variations                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 1 | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 64, 7]> self = ?,<br>List[int] size = [1, 71, 64, 7]  | None     | Fallback   | True  |
|  1 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]  | Done     | Done       | True  |
|  2 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64] | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]   | Removed  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7, 18176]> self = ? | Done     | Done       | True  |
### aten.index.Tensor
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[1]>] | None     | Unknown    | N/A   |
|  1 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 7]>]                 | None     | Fallback   | True  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor self = ?         | None     | Unknown    | N/A   |
### aten.logical_not.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[7, 7]> self = ? | Done     | Done       | True  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = -inf | None     | Fallback   | True  |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[7, 18176]> self = ?,<br>Tensor<[18176, 4544]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 18176]> mat2 = ?  | Done     | Done       | True  |
|  2 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4544]> mat2 = ?   | Done     | Done       | True  |
|  3 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4672]> mat2 = ?   | Done     | Done       | True  |
### aten.mul.Scalar
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 64, 7]> self = ?,<br>number other = 0.3535533905932738  | None     | Fallback   | True  |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>number other = 0.3535533905932738 | None     | Fallback   | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?  | Done     | Done       | True  |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ? | None     | Fallback   | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7, 4544]> input = ?,<br>List[int] normalized_shape = [4544],<br>Optional[Tensor]<[4544]> weight = ?,<br>Optional[Tensor]<[4544]> bias = ?,<br>float eps = 1e-05 | None     | Fallback   | True  |
### aten.neg.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 32]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[1, 71, 7, 32]> self = ? | Done     | Done       | True  |
### aten.ones.default
|    | ATen Input Variations                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [7, 7],<br>Optional[int] dtype = torch.bool,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | None     | Fallback   | True  |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
|  1 | Tensor<[18176, 4544]> self = ?,<br>List[int] dims = [1, 0]        | Done     | Done       | True  |
|  2 | Tensor<[4544, 18176]> self = ?,<br>List[int] dims = [1, 0]        | Done     | Done       | True  |
|  3 | Tensor<[4544, 4544]> self = ?,<br>List[int] dims = [1, 0]         | Done     | Done       | True  |
|  4 | Tensor<[4672, 4544]> self = ?,<br>List[int] dims = [1, 0]         | Done     | Done       | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                    | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807  | Done     | Done       | True  |
|  2 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2                   | Done     | Done       | True  |
|  4 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Fallback   | True  |
|  5 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                   | Done     | Done       | True  |
|  6 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807 | Done     | Done       | True  |
|  7 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Done     | Done       | True  |
|  1 | Tensor<[1, 7, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  2 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Done     | Done       | True  |
### aten.tril.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[7, 7]> self = ? | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1 | Done     | Done       | True  |
|  1 | Tensor<[7]> self = ?,<br>int dim = 0        | None     | Fallback   | True  |
### aten.view.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]   | Done     | Done       | True  |
|  1 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]      | Done     | Done       | True  |
|  2 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]        | Done     | Done       | True  |
|  3 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]   | Done     | Done       | True  |
|  4 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]    | Done     | Done       | True  |
|  5 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64] | Done     | Done       | True  |
|  6 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [71, 7, 64]    | Done     | Done       | True  |
|  7 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]      | Done     | Done       | True  |
|  8 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]      | Done     | Done       | True  |
|  9 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]        | Done     | Done       | True  |
| 10 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]        | Done     | Done       | True  |
| 11 | Tensor<[71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]    | Done     | Done       | True  |
| 12 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]      | Done     | Done       | True  |
### aten.zeros_like.default
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | None     | Fallback   | True  |

