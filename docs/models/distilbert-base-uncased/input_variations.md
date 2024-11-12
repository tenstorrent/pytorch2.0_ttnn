# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default             |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  3 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  4 | aten.clone.default             |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  5 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  6 | aten.embedding.default         |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.eq.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.expand.default            |                  4 |           0 |         3 |          1 | 🚧          |    0.75 |
|  9 | aten.gelu.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.lift_fresh_copy.default   |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 11 | aten.masked_fill.Tensor        |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 12 | aten.native_layer_norm.default |                  1 |           0 |         0 |          1 | ✘           |    0    |
| 13 | aten.slice.Tensor              |                  2 |           0 |         1 |          1 | 🚧          |    0.5  |
| 14 | aten.t.default                 |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 15 | aten.transpose.int             |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 16 | aten.view.default              |                 12 |          11 |         0 |          1 | 🚧          |    0.92 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 16, 16]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ? | Done     | Unknown    | N/A   |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[16, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Unknown    | N/A   |
|  1 | Tensor<[768]> self = ?,<br>Tensor<[16, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Unknown    | N/A   |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[16, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Unknown    | N/A   |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 16, 16]> self = ?,<br>Tensor<[12, 16, 64]> mat2 = ? | Done     | Unknown    | N/A   |
|  1 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ? | Done     | Unknown    | N/A   |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 16, 16]> self = ?                                                           | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 16, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 768]> self = ?                                                              | Done     | Unknown    | N/A   |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0 | Done     | Unknown    | N/A   |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0 | None     | Unknown    | N/A   |
|  1 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                           | None     | Unknown    | N/A   |
### aten.eq.Scalar
|    | ATen Input Variations                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16]> self = ?,<br>number other = 0 | None     | Unknown    | N/A   |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16]   | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16] | Removed  | Unknown    | N/A   |
|  2 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64] | Removed  | Unknown    | N/A   |
|  3 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [1, 12, 64, 16] | Removed  | Unknown    | N/A   |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 3072]> self = ? | Done     | Unknown    | N/A   |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor self = ?         | Removed  | Unknown    | N/A   |
### aten.masked_fill.Tensor
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 16, 16]> self = ?,<br>Tensor<[1, 12, 16, 16]> mask = ?,<br>Tensor<[]> value = ? | Removed  | Unknown    | N/A   |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Fallback | Unknown    | N/A   |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   |
|  1 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 16                  | Fallback | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3072, 768]> self = ? | Done     | Unknown    | N/A   |
|  1 | Tensor<[768, 3072]> self = ? | Done     | Unknown    | N/A   |
|  2 | Tensor<[768, 768]> self = ?  | Done     | Unknown    | N/A   |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 3 | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 16, 16]> self = ?,<br>List[int] size = [12, 16, 16] | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 12, 16, 64]> self = ?,<br>List[int] size = [12, 16, 64] | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 12, 64, 16]> self = ?,<br>List[int] size = [12, 64, 16] | Done     | Unknown    | N/A   |
|  3 | Tensor<[1, 16, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768] | Done     | Unknown    | N/A   |
|  4 | Tensor<[1, 16, 3072]> self = ?,<br>List[int] size = [16, 3072]     | Done     | Unknown    | N/A   |
|  5 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64] | Done     | Unknown    | N/A   |
|  6 | Tensor<[1, 16, 768]> self = ?,<br>List[int] size = [16, 768]       | Done     | Unknown    | N/A   |
|  7 | Tensor<[1, 16]> self = ?,<br>List[int] size = [1, 1, 1, 16]        | Done     | Unknown    | N/A   |
|  8 | Tensor<[12, 16, 16]> self = ?,<br>List[int] size = [1, 12, 16, 16] | Fallback | Unknown    | N/A   |
|  9 | Tensor<[12, 16, 64]> self = ?,<br>List[int] size = [1, 12, 16, 64] | Done     | Unknown    | N/A   |
| 10 | Tensor<[16, 3072]> self = ?,<br>List[int] size = [1, 16, 3072]     | Done     | Unknown    | N/A   |
| 11 | Tensor<[16, 768]> self = ?,<br>List[int] size = [1, 16, 768]       | Done     | Unknown    | N/A   |

