# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default          |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.add.Tensor                |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.addmm.default             |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.argmax.default            |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bmm.default               |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.clone.default             |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.div.Tensor                |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.embedding.default         |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.eq.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.expand.default            |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.full.default              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.index.Tensor              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.mm.default                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.mul.Tensor                |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.native_layer_norm.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.permute.default           |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.pow.Tensor_Scalar         |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.remainder.Scalar          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.rsub.Scalar               |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.slice.Tensor              |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.split.Tensor              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.sub.Tensor                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.t.default                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.tanh.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.transpose.int             |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.unsqueeze.default         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.view.default              |                 17 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.where.self                |                  1 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Done       | 0.999672 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 7]> self = ?,<br>Optional[int] dtype = torch.int32          | Unknown  | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                             | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0              | Unknown  | Done       | 0.999995 |      0 |
|  2 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?  | Unknown  | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?    | Unknown  | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2304]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ? | Unknown  | Done       | 0.999967 |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  | Done       | 0.999966 |      0 |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[7, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Done       | 0.999943 |      0 |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[7, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | 0.999965 |      0 |
### aten.argmax.default
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = -1 | Unknown  | Fallback   |     1 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ? | Unknown  | Done       | 0.999985 |      0 |
|  1 | Tensor<[12, 7, 7]> self = ?,<br>Tensor<[12, 7, 64]> mat2 = ?  | Unknown  | Done       | 0.999991 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 7, 7]> self = ?                                                            | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 7, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 7, 768]> self = ?                                                              | Unknown  | Done       |     1 |      0 |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Done       | 0.999996 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1024, 768]> weight = ?,<br>Tensor indices = ?          | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ? | Unknown  | Done       | 1.0   | 0      |
### aten.eq.Scalar
|    | ATen Input Variations                            | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 50256 | Unknown  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [1, 12, 64, 7] | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64] | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]   | Unknown  | Done       |     1 |     -1 |
### aten.full.default
|    | ATen Input Variations                                                                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Done       |     1 |      0 |
|  1 | List[int] size = [],<br>number fill_value = 8.0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                     | Unknown  | Done       |     1 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 7, 2]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_arange_1, <[1]>] | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ? | Unknown  | Done       | 0.999951 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                | Unknown  | Done       | 0.999995 |      0 |
|  2 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                     | Unknown  | Done       | 1        |      0 |
|  3 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654      | Unknown  | Done       | 0.999997 |      0 |
|  4 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?         | Unknown  | Done       | 0.999996 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 7, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | 0.994378 |      3 |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 7, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  | Done       | 0.999996 |      0 |
### aten.remainder.Scalar
|    | ATen Input Variations                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?,<br>number other = 7 | Unknown  | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0 | Unknown  | Done       | 0.999998 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 1, 1024, 1024]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 7                   | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 1, 7, 1024]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 7                      | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Done       |     1 |     -1 |
### aten.split.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2 | Unknown  | Done       |     1 |      0 |
### aten.sub.Tensor
|    | ATen Input Variations                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?,<br>Tensor other = 1 | Unknown  | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 768]> self = ? | Unknown  | Done       |     1 |      0 |
### aten.tanh.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 7, 3072]> self = ? | Unknown  | Done       | 0.999942 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 7]> self = ?,<br>int dim = 1    | Unknown  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 64, 7]> self = ?,<br>List[int] size = [12, 64, 7] | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] size = [12, 7, 64] | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 12, 7, 7]> self = ?,<br>List[int] size = [12, 7, 7]   | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] size = [1, 7, 768] | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 7, 3072]> self = ?,<br>List[int] size = [-1, 3072]    | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 7, 768]   | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [-1, 768]      | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [1, 7, 12, 64] | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[1, 7, 768]> self = ?,<br>List[int] size = [7, 768]       | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[1, 7]> self = ?,<br>List[int] size = [-1, 7]             | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[1, 7]> self = ?,<br>List[int] size = [1, -1]             | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[12, 7, 64]> self = ?,<br>List[int] size = [1, 12, 7, 64] | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[12, 7, 7]> self = ?,<br>List[int] size = [1, 12, 7, 7]   | Unknown  | Done       |     1 |      0 |
| 13 | Tensor<[7, 2304]> self = ?,<br>List[int] size = [1, 7, 2304]     | Unknown  | Done       |     1 |      0 |
| 14 | Tensor<[7, 2]> self = ?,<br>List[int] size = [1, 7, 2]           | Unknown  | Done       |     1 |      0 |
| 15 | Tensor<[7, 3072]> self = ?,<br>List[int] size = [1, 7, 3072]     | Unknown  | Done       |     1 |      0 |
| 16 | Tensor<[7, 768]> self = ?,<br>List[int] size = [1, 7, 768]       | Unknown  | Done       |     1 |      0 |
### aten.where.self
|    | ATen Input Variations                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> condition = ?,<br>Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ? | Unknown  | Done       |     1 |      0 |

