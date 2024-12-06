# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._to_copy.default          |                  4 |           1 |         2 |          0 | 🚧          |    0.75 |
|  2 | aten.add.Tensor                |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  3 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  4 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  5 | aten.clone.default             |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  6 | aten.cumsum.default            |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.div.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  8 | aten.embedding.default         |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  9 | aten.expand.default            |                  4 |           0 |         4 |          0 | ✅          |    1    |
| 10 | aten.gelu.default              |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 11 | aten.mul.Tensor                |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 12 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.ne.Scalar                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 14 | aten.permute.default           |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 15 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 16 | aten.slice.Tensor              |                  4 |           1 |         3 |          0 | ✅          |    1    |
| 17 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 18 | aten.transpose.int             |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 19 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 20 | aten.view.default              |                 12 |          12 |         0 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32                                                                            | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int64                                                                            | Removed  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                        | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                        | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ? | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[250002]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 250002]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[10, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?     | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?       | Done     | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10, 768]> self = ?                                                              | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 12, 10, 10]> self = ?                                                           | Done     | Unknown    | N/A   | N/A    |
### aten.cumsum.default
|    | ATen Input Variations                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0 | Done     | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                              | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1    | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [1, 10]                 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10] | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64] | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [1, 12, 64, 10] | Removed  | Unknown    | N/A   | N/A    |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10, 3072]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10, 768]> self = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                    | Done     | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Unknown    | N/A   | N/A    |
### aten.ne.Scalar
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>number other = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 514]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 514]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 10                       | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[250002, 768]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[3072, 768]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[768, 3072]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[768, 768]> self = ?    | Done     | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10]> self = ?,<br>int dim = 1    | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, 10, 768] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]     | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, 10, 12, 64] | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10] | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64] | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10] | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[10, 250002]> self = ?,<br>List[int] size = [1, 10, 250002] | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]     | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]       | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10] | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64] | Done     | Unknown    | N/A   | N/A    |

