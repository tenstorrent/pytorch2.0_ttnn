# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  1 | aten._to_copy.default          |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor                |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  4 | aten.addmm.default             |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  5 | aten.bmm.default               |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  6 | aten.clone.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  7 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.embedding.default         |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.expand.default            |                  3 |           0 |         3 |          0 | ✅          |    1    |
| 10 | aten.mul.Tensor                |                  9 |           9 |         0 |          0 | ✅          |    1    |
| 11 | aten.native_layer_norm.default |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 12 | aten.permute.default           |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.pow.Tensor_Scalar         |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 14 | aten.rsub.Scalar               |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.slice.Tensor              |                  2 |           0 |         1 |          0 | 🚧          |    0.5  |
| 16 | aten.t.default                 |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 17 | aten.tanh.default              |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 18 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 19 | aten.unsqueeze.default         |                  2 |           1 |         0 |          1 | 🚧          |    0.5  |
| 20 | aten.view.default              |                 13 |          11 |         0 |          2 | 🚧          |    0.85 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | None     | Fallback   | True  |
### aten._unsafe_view.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] size = [1, 9, 1024] | Done     | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?  | Done     | Done       | True  |
|  2 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0               | Done     | Done       | True  |
|  3 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?    | Done     | Done       | True  |
|  4 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0              | Done     | Done       | True  |
|  5 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?  | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 1024]> mat2 = ?   | Done     | Done       | True  |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[128]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 128]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[30000]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 30000]> mat2 = ? | Done     | Done       | True  |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[9, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | True  |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?  | Done     | Done       | True  |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 9, 9]> self = ?                                                            | Done     | Done       | True  |
|  1 | Tensor<[1, 9, 1024]> self = ?                                                             | Done     | Done       | True  |
|  2 | Tensor<[1, 9, 128]> self = ?                                                              | Done     | Done       | True  |
|  3 | Tensor<[1, 9, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
### aten.div.Tensor
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0 | None     | Fallback   | True  |
### aten.embedding.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                             | None     | Fallback   | True  |
|  1 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0 | None     | Fallback   | True  |
|  2 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                           | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [1, 16, 64, 9] | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64] | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]   | Removed  | Fallback   | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | True  |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                 | Done     | Done       | True  |
|  2 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                      | Done     | Done       | True  |
|  3 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654       | Done     | Done       | True  |
|  4 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?           | Done     | Done       | True  |
|  5 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                | Done     | Done       | True  |
|  6 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                     | Done     | Done       | True  |
|  7 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654      | Done     | Done       | True  |
|  8 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?         | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 9, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-12 | Done     | Done       | N/A   |
|  1 | Tensor<[1, 9, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12     | Done     | Done       | N/A   |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 9, 128]> self = ?,<br>number exponent = 3.0  | Done     | Done       | True  |
|  1 | Tensor<[1, 9, 4096]> self = ?,<br>number exponent = 3.0 | Done     | Done       | True  |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0 | None     | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 512]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9                   | None     | Fallback   | True  |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1024, 1024]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1024, 128]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1024, 4096]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[128, 1024]> self = ?  | Done     | Done       | True  |
|  4 | Tensor<[30000, 128]> self = ? | Done     | Done       | True  |
|  5 | Tensor<[4096, 1024]> self = ? | Done     | Done       | True  |
### aten.tanh.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 9, 128]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[1, 9, 4096]> self = ? | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
|  1 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1   | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 9]> self = ?,<br>int dim = 2 | Fallback | Done       | True  |
|  1 | Tensor<[1, 9]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                             | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16, 64, 9]> self = ?,<br>List[int] size = [16, 64, 9]  | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 16, 9, 64]> self = ?,<br>List[int] size = [16, 9, 64]  | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 16, 9, 9]> self = ?,<br>List[int] size = [16, 9, 9]    | Done     | Unknown    | N/A   |
|  3 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [1, 9, 16, 64] | Done     | Unknown    | N/A   |
|  4 | Tensor<[1, 9, 1024]> self = ?,<br>List[int] size = [9, 1024]      | Done     | Unknown    | N/A   |
|  5 | Tensor<[1, 9, 128]> self = ?,<br>List[int] size = [9, 128]        | Done     | Done       | True  |
|  6 | Tensor<[1, 9, 4096]> self = ?,<br>List[int] size = [9, 4096]      | Done     | Unknown    | N/A   |
|  7 | Tensor<[16, 9, 64]> self = ?,<br>List[int] size = [1, 16, 9, 64]  | Done     | Unknown    | N/A   |
|  8 | Tensor<[16, 9, 9]> self = ?,<br>List[int] size = [1, 16, 9, 9]    | Fallback | Unknown    | N/A   |
|  9 | Tensor<[9, 1024]> self = ?,<br>List[int] size = [1, 9, 1024]      | Done     | Done       | True  |
| 10 | Tensor<[9, 128]> self = ?,<br>List[int] size = [1, 9, 128]        | Done     | Unknown    | N/A   |
| 11 | Tensor<[9, 30000]> self = ?,<br>List[int] size = [1, 9, 30000]    | Fallback | Unknown    | N/A   |
| 12 | Tensor<[9, 4096]> self = ?,<br>List[int] size = [1, 9, 4096]      | Done     | Unknown    | N/A   |

