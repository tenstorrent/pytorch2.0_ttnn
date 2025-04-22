# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default          |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.addmm.default             |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.baddbmm.default           |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.bmm.default               |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.clone.default             |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.cumsum.default            |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.embedding.default         |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.expand.default            |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.full.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.lt.Tensor                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.masked_fill.Scalar        |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.mm.default                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.mul.Tensor                |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.native_layer_norm.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.permute.default           |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.rsub.Scalar               |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.select.int                |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.slice.Tensor              |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.sub.Tensor                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.t.default                 |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.tanh.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.transpose.int             |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.unsqueeze.default         |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.view.default              |                 13 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 16, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Done       | 0.999622 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bool                                                                                | Unknown  | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 16, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                           | Unknown  | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 16, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Fallback   |     1 |     -1 |
|  4 | Tensor<[16, 1, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                               | Unknown  | Fallback   |     1 |     -1 |
|  5 | Tensor<[32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   |     1 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] size = [1, 32, 1536] | Unknown  | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ? | Unknown  | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                | Unknown  | Done       | 0.999995 |      0 |
|  2 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0              | Unknown  | Done       | 0.999995 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1536]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 1536]> mat2 = ? | Unknown  | Done       | 0.999959 |      0 |
|  1 | Tensor<[1536]> self = ?,<br>Tensor<[32, 6144]> mat1 = ?,<br>Tensor<[6144, 1536]> mat2 = ? | Unknown  | Done       | 0.999912 |      0 |
|  2 | Tensor<[4608]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 4608]> mat2 = ? | Unknown  | Done       | 0.999959 |      0 |
|  3 | Tensor<[6144]> self = ?,<br>Tensor<[32, 1536]> mat1 = ?,<br>Tensor<[1536, 6144]> mat2 = ? | Unknown  | Done       | 0.999959 |      0 |
### aten.baddbmm.default
|    | ATen Input Variations                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[16, 1, 32]> self = ?,<br>Tensor<[16, 32, 96]> batch1 = ?,<br>Tensor<[16, 96, 32]> batch2 = ?,<br>number beta = 1.0,<br>number alpha = 0.10206207261596577 | Unknown  | Done       | 0.999989 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   |     PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|--------:|-------:|
|  0 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ? | Unknown  | Done       | 0.99999 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 32, 32]> self = ?                                                           | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 1536]> self = ?                                                             | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 32, 16, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       |     1 |      0 |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32]> self = ?,<br>int dim = -1 | Unknown  | Done       | 0.999808 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ? | Unknown  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32]  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>List[int] size = [1, 1, 32, 32] | Unknown  | Done       |     1 |     -1 |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Done       |     1 |      0 |
### aten.lt.Tensor
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38  | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 16, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[32, 32]> self = ?,<br>Tensor<[32, 32]> mask = ?,<br>number value = 0                                    | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                           | Status   | Isolated   |     PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|--------:|-------:|
|  0 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ? | Unknown  | Done       | 0.99996 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                   | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715         | Unknown  | Done       | 0.9999953316937843 | 0      |
|  2 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5              | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456       | Unknown  | Done       | 0.9999972196629102 | 0      |
|  4 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ? | Unknown  | Done       | 0.9999959773666404 | 0      |
|  5 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?             | Unknown  | Done       | 0.9999953661868788 | 0      |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   | PCC   |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 32, 1536]> input = ?,<br>List[int] normalized_shape = [1536],<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1] | Unknown  | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0 | Unknown  | Done       | 0.999994 |      0 |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 1 | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 2 | Unknown  | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 32, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807         | Unknown  | Done       |     1 |     -1 |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1 | Unknown  | Done       | 0.999999 |      0 |
### aten.t.default
|    | ATen Input Variations           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1536, 1536]> self = ?   | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1536, 6144]> self = ?   | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[250880, 1536]> self = ? | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[4608, 1536]> self = ?   | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[6144, 1536]> self = ?   | Unknown  | Done       |     1 |      0 |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 6144]> self = ? | Unknown  | Done       | 0.999985 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 32]> self = ?,<br>int dim = 1 | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = 1     | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[32, 32]> self = ?,<br>int dim = 0    | Unknown  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 32, 32]> self = ?,<br>List[int] size = [16, 32, 32]     | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] size = [16, 32, 96]     | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 32]> self = ?,<br>List[int] size = [16, 1, 32]          | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[1, 16, 96, 32]> self = ?,<br>List[int] size = [16, 96, 32]     | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[1, 32, 1536]> self = ?,<br>List[int] size = [32, 1536]         | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[1, 32, 4608]> self = ?,<br>List[int] size = [1, 32, 16, 3, 96] | Unknown  | Done       |     1 |      0 |
|  6 | Tensor<[1, 32, 6144]> self = ?,<br>List[int] size = [32, 6144]         | Unknown  | Done       |     1 |      0 |
|  7 | Tensor<[16, 32, 32]> self = ?,<br>List[int] size = [1, 16, 32, 32]     | Unknown  | Done       |     1 |      0 |
|  8 | Tensor<[16, 32, 96]> self = ?,<br>List[int] size = [1, 16, 32, 96]     | Unknown  | Done       |     1 |      0 |
|  9 | Tensor<[32, 1536]> self = ?,<br>List[int] size = [1, 32, 1536]         | Unknown  | Done       |     1 |      0 |
| 10 | Tensor<[32, 250880]> self = ?,<br>List[int] size = [1, 32, 250880]     | Unknown  | Done       |     1 |      0 |
| 11 | Tensor<[32, 4608]> self = ?,<br>List[int] size = [1, 32, 4608]         | Unknown  | Done       |     1 |      0 |
| 12 | Tensor<[32, 6144]> self = ?,<br>List[int] size = [1, 32, 6144]         | Unknown  | Done       |     1 |      0 |

