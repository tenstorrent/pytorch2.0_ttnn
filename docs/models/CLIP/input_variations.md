# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default           |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  1 | aten._to_copy.default           |                  4 |           3 |         1 |          0 | ✅          |     1   |
|  2 | aten._unsafe_view.default       |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  3 | aten.add.Tensor                 |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  4 | aten.addmm.default              |                  6 |           3 |         3 |          0 | ✅          |     1   |
|  5 | aten.argmax.default             |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  6 | aten.bmm.default                |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  7 | aten.cat.default                |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  8 | aten.clone.default              |                  6 |           0 |         6 |          0 | ✅          |     1   |
|  9 | aten.convolution.default        |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 10 | aten.div.Tensor                 |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 11 | aten.embedding.default          |                  3 |           1 |         2 |          0 | ✅          |     1   |
| 12 | aten.exp.default                |                  1 |           0 |         1 |          0 | ✅          |     1   |
| 13 | aten.expand.default             |                  3 |           2 |         1 |          0 | ✅          |     1   |
| 14 | aten.full.default               |                  1 |           0 |         1 |          0 | ✅          |     1   |
| 15 | aten.index.Tensor               |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 16 | aten.linalg_vector_norm.default |                  2 |           0 |         0 |          0 | ✘           |     0   |
| 17 | aten.lt.Tensor                  |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 18 | aten.masked_fill.Scalar         |                  2 |           1 |         0 |          0 | 🚧          |     0.5 |
| 19 | aten.mm.default                 |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 20 | aten.mul.Tensor                 |                  7 |           7 |         0 |          0 | ✅          |     1   |
| 21 | aten.native_layer_norm.default  |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 22 | aten.rsub.Scalar                |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 23 | aten.select.int                 |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 24 | aten.sigmoid.default            |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 25 | aten.slice.Tensor               |                  8 |           0 |         8 |          0 | ✅          |     1   |
| 26 | aten.t.default                  |                  9 |           2 |         7 |          0 | ✅          |     1   |
| 27 | aten.transpose.int              |                  7 |           7 |         0 |          0 | ✅          |     1   |
| 28 | aten.unsqueeze.default          |                  4 |           4 |         0 |          0 | ✅          |     1   |
| 29 | aten.view.default               |                 20 |          20 |         0 |          0 | ✅          |     1   |
***
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | 0.999628 |      0 |
|  1 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | 0.999562 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                          | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                              | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu | Removed  | Fallback   |     1 |     -1 |
|  3 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                | Done     | Fallback   |     1 |     -1 |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Done     | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ? | Done     | Done       | 0.99997  |      0 |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Removed  | Done       | 0.999967 |      0 |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[14, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ? | Done     | Done       | 0.99995  |      0 |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?   | Done     | Done       | 0.99997  |      0 |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Removed  | Done       | 0.999943 |      0 |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Removed  | Done       | 0.999968 |      0 |
### aten.argmax.default
|    | ATen Input Variations                              | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1 | None     | Fallback   |     1 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ? | Done     | Done       | 0.999986 |      0 |
|  1 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ? | Done     | Done       | 0.999986 |      0 |
|  2 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?   | Done     | Done       | 0.999985 |      0 |
|  3 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?    | Done     | Done       | 0.999991 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 49, 768]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[12, 50, 50]> self = ?                                                              | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[16, 7, 7]> self = ?                                                                | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.div.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ? | Done     | Done       | 0.999997 |      0 |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ? | Done     | Done       | 0.999996 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?   | Removed  | Done       |     1 |      0 |
|  2 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?    | Removed  | Done       |     1 |      0 |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?     | Removed  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]          | Removed  | Done       |     1 |      0 |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_arange_1, <[2]>] | None     | Unknown    | N/A   | N/A    |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[2, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
### aten.lt.Tensor
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ? | None     | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = 0                                   | None     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                     | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ? | Done     | Done       | 0.99997  |      0 |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?   | Done     | Done       | 1        |      0 |
|  2 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ? | Done     | Done       | 0.999972 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702            | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125             | Done     | Done       | 1        |      0 |
|  3 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                   | Done     | Done       | 1        |      0 |
|  4 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702             | Done     | Done       | 0.999996 |      0 |
|  5 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  6 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125              | Done     | Done       | 1        |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | 0.997292 |      3 |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | 0.999997 |      3 |
|  2 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | 0.99867  |      3 |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0 | Done     | Done       | 0.999994 |      0 |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 50, 3072]> self = ? | Done     | Done       | 0.999755 |      0 |
|  1 | Tensor<[2, 7, 2048]> self = ?  | Done     | Done       | 0.999753 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 77]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  7 | Tensor<[2, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512]> self = ?    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 1]> self = ?      | Done     | Done       |     1 |      0 |
|  2 | Tensor<[2048, 512]> self = ? | Removed  | Done       |     1 |      0 |
|  3 | Tensor<[3072, 768]> self = ? | Removed  | Done       |     1 |      0 |
|  4 | Tensor<[512, 2048]> self = ? | Removed  | Done       |     1 |      0 |
|  5 | Tensor<[512, 512]> self = ?  | Removed  | Done       |     1 |      0 |
|  6 | Tensor<[512, 768]> self = ?  | Removed  | Done       |     1 |      0 |
|  7 | Tensor<[768, 3072]> self = ? | Removed  | Done       |     1 |      0 |
|  8 | Tensor<[768, 768]> self = ?  | Removed  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[16, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       |     1 |      0 |
|  5 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[2, 7]> self = ?,<br>int dim = 1    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[7, 7]> self = ?,<br>int dim = 0    | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]     | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, 12, 64] | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]       | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64] | Done     | Done       |     1 |      0 |
|  7 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]      | Done     | Done       |     1 |      0 |
|  8 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]        | Done     | Done       |     1 |      0 |
|  9 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]    | Done     | Done       |     1 |      0 |
| 10 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]      | Done     | Done       |     1 |      0 |
| 11 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]      | Done     | Done       |     1 |      0 |
| 12 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Done     | Done       |     1 |      0 |
| 13 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, -1, 8, 64]   | Done     | Done       |     1 |      0 |
| 14 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, 8, 64]    | Done     | Done       |     1 |      0 |
| 15 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]               | Done     | Done       |     1 |      0 |
| 16 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]   | Done     | Done       |     1 |      0 |
| 17 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]      | Done     | Done       |     1 |      0 |
| 18 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]     | Done     | Done       |     1 |      0 |
| 19 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]       | Done     | Done       |     1 |      0 |

