# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default          |                  4 |           2 |         2 |          0 | ✅          |       1 |
|  2 | aten._unsafe_index.Tensor      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                |                 10 |          10 |         0 |          0 | ✅          |       1 |
|  4 | aten.addmm.default             |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  5 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  6 | aten.cat.default               |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.clamp.default             |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  8 | aten.clone.default             |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  9 | aten.convolution.default       |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 11 | aten.expand.default            |                  4 |           0 |         4 |          0 | ✅          |       1 |
| 12 | aten.floor.default             |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 13 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.mul.Tensor                |                  9 |           9 |         0 |          0 | ✅          |       1 |
| 15 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.permute.default           |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 17 | aten.rsub.Scalar               |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 18 | aten.select.int                |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 19 | aten.slice.Tensor              |                  4 |           1 |         3 |          0 | ✅          |       1 |
| 20 | aten.sub.Tensor                |                 10 |          10 |         0 |          0 | ✅          |       1 |
| 21 | aten.t.default                 |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 22 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 23 | aten.unsqueeze.default         |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 24 | aten.view.default              |                 14 |          14 |         0 |          0 | ✅          |       1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 257, 257]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>Optional[int] dtype = torch.int64       | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 16, 1]> self = ?,<br>Optional[int] dtype = torch.int64       | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 768, 16, 16]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 768, 37, 37]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Unknown    | N/A   | N/A    |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 768, 37, 37]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_view_2, _folded_view_3, <[1, 1, 16, 1]>, <[1, 1, 1, 16]>] | None     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -6.0                   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1                      | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.0                    | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 2                      | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -6.0                   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                      | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.0                    | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2                      | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[1, 257, 768]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 768, 16, 16]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[257, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[768]> self = ?,<br>Tensor<[257, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[257, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[12, 257, 257]> self = ?,<br>Tensor<[12, 257, 64]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[12, 257, 64]> self = ?,<br>Tensor<[12, 64, 257]> mat2 = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.cat.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 256, 768]>],<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.clamp.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 36 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 16, 1]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 36 | Done     | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 257, 257]> self = ?                                                          | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 257, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 257, 768]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 768, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.channels_last     | Done     | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 14, 14]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [14, 14],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 257, 257]> self = ?,<br>Tensor other = 8.0 | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 257, 257]> self = ?,<br>List[int] size = [1, 12, 257, 257] | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 12, 257, 64]> self = ?,<br>List[int] size = [1, 12, 257, 64]   | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 12, 64, 257]> self = ?,<br>List[int] size = [1, 12, 64, 257]   | Removed  | Unknown    | N/A   | N/A    |
### aten.floor.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?         | Done     | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 257, 3072]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -0.75               | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.25                | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?    | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -0.75               | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.25                | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?    | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[768]> other = ?            | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 257, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Done     | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 257, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 257, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 37, 37, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 768, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Done     | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 2.0 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 2.0 | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1370, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 257, 768]> self = ?,<br>int dim = 1,<br>int index = 0  | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1370, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1370, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 9223372036854775807 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 257, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?     | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -3.0  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -3.75 | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1     | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 2.25  | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.0  | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.75 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1     | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2.25  | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[3072, 768]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[768, 3072]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[768, 768]> self = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 257, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 768, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 768]> self = ?,<br>int dim = 0 | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 257, 257]> self = ?,<br>List[int] size = [12, 257, 257] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 257, 64]> self = ?,<br>List[int] size = [12, 257, 64]   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 12, 64, 257]> self = ?,<br>List[int] size = [12, 64, 257]   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1369, 768]> self = ?,<br>List[int] size = [1, 37, 37, 768]  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 16, 16, 768]> self = ?,<br>List[int] size = [1, -1, 768]    | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 257, 12, 64]> self = ?,<br>List[int] size = [1, 257, 768]   | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 257, 3072]> self = ?,<br>List[int] size = [257, 3072]       | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 257, 768]> self = ?,<br>List[int] size = [1, 257, 12, 64]   | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 257, 768]> self = ?,<br>List[int] size = [257, 768]         | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 768, 16, 16]> self = ?,<br>List[int] size = [1, 768, 256]   | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[12, 257, 257]> self = ?,<br>List[int] size = [1, 12, 257, 257] | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[12, 257, 64]> self = ?,<br>List[int] size = [1, 12, 257, 64]   | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[257, 3072]> self = ?,<br>List[int] size = [1, 257, 3072]       | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[257, 768]> self = ?,<br>List[int] size = [1, 257, 768]         | Done     | Unknown    | N/A   | N/A    |

