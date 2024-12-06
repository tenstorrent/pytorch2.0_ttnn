# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._to_copy.default          |                  6 |           5 |         0 |          0 | 🚧          |    0.83 |
|  2 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor                |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  4 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  5 | aten.arange.start              |                  1 |           0 |         1 |          0 | ✅          |    1    |
|  6 | aten.baddbmm.default           |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.bmm.default               |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  8 | aten.clone.default             |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  9 | aten.cumsum.default            |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.embedding.default         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 11 | aten.expand.default            |                  2 |           1 |         1 |          0 | ✅          |    1    |
| 12 | aten.full.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.lift_fresh_copy.default   |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 14 | aten.masked_fill.Scalar        |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 15 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 16 | aten.mul.Tensor                |                  7 |           6 |         1 |          0 | ✅          |    1    |
| 17 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 18 | aten.permute.default           |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 19 | aten.pow.Tensor_Tensor         |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 20 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 21 | aten.select.int                |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 22 | aten.slice.Tensor              |                  6 |           0 |         6 |          0 | ✅          |    1    |
| 23 | aten.sub.Tensor                |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 24 | aten.t.default                 |                  5 |           5 |         0 |          0 | ✅          |    1    |
| 25 | aten.tanh.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 26 | aten.transpose.int             |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 27 | aten.unsqueeze.default         |                  5 |           4 |         1 |          0 | ✅          |    1    |
| 28 | aten.view.default              |                 13 |          13 |         0 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Unknown    | N/A   | N/A    |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                           | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 16, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[16, 1, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                               | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Done     | Unknown    | N/A   | N/A    |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] size = [1, 32, 1536] | Done     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0              | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1536]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 1536]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1536]> self = ?,<br>Tensor<[32, 6144]> mat1 = ?,<br>Tensor<[6144, 1536]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[4608]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 4608]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[6144]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 6144]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.arange.start
|    | ATen Input Variations                                                                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number start = 1,<br>number end = 17,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Unknown    | N/A   | N/A    |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16, 1, 32]> self = ?,<br>Tensor<[16, 32, 96]> batch1 = ?,<br>Tensor<[16, 96, 32]> batch2 = ?,<br>number beta = 1.0,<br>number alpha = 0.10206207261596577 | Done     | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 32, 32]> self = ?                                                           | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 1536]> self = ?                                                             | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Unknown    | N/A   | N/A    |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32]> self = ?,<br>int dim = -1 | Done     | Unknown    | N/A   | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ? | Done     | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32] | Removed  | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | Unknown    | N/A   | N/A    |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?         | Removed  | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715         | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5              | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456       | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?             | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[16, 1]> self = ?,<br>Tensor<[1, 1, 32]> other = ?          | Removed  | Unknown    | N/A   | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05 | Done     | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Done     | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Tensor
|    | ATen Input Variations                             | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[]> self = ?,<br>Tensor<[16]> exponent = ? | Removed  | Unknown    | N/A   | N/A    |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0 | Done     | Unknown    | N/A   | N/A    |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 1 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Removed  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807         | Removed  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1536, 1536]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1536, 6144]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[250880, 1536]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[4608, 1536]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[6144, 1536]> self = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 6144]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2  | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 32]> self = ?,<br>int dim = 1 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = 1     | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[16]> self = ?,<br>int dim = 1        | Removed  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32, 32]> self = ?,<br>int dim = 0    | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]     | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]          | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]     | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]         | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96] | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]         | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]     | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]     | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]         | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]     | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]         | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]         | Done     | Unknown    | N/A   | N/A    |

