# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default           |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  1 | aten._to_copy.default           |                  4 |           1 |         2 |          0 | 🚧          |    0.75 |
|  2 | aten._unsafe_view.default       |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  4 | aten.addmm.default              |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  5 | aten.arange.default             |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.argmax.default             |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.bmm.default                |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  8 | aten.cat.default                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.clone.default              |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 10 | aten.convolution.default        |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.div.Tensor                 |                  2 |           0 |         2 |          0 | ✅          |    1    |
| 12 | aten.embedding.default          |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 13 | aten.exp.default                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.expand.default             |                  3 |           2 |         1 |          0 | ✅          |    1    |
| 15 | aten.full.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.index.Tensor               |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 17 | aten.linalg_vector_norm.default |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.masked_fill.Scalar         |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.mm.default                 |                  3 |           0 |         3 |          0 | ✅          |    1    |
| 20 | aten.mul.Tensor                 |                  7 |           6 |         0 |          0 | 🚧          |    0.86 |
| 21 | aten.native_layer_norm.default  |                  3 |           2 |         1 |          0 | ✅          |    1    |
| 22 | aten.rsub.Scalar                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.select.int                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 24 | aten.sigmoid.default            |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 25 | aten.slice.Tensor               |                  8 |           1 |         7 |          0 | ✅          |    1    |
| 26 | aten.t.default                  |                  9 |           8 |         1 |          0 | ✅          |    1    |
| 27 | aten.transpose.int              |                  7 |           6 |         0 |          0 | 🚧          |    0.86 |
| 28 | aten.unsqueeze.default          |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 29 | aten.view.default               |                 20 |          18 |         2 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  1 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                          | Removed  | Fallback   | True  |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                              | None     | Fallback   | True  |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu | Removed  | Fallback   | True  |
|  3 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                | Done     | Fallback   | True  |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Done     | Done       | True  |
|  1 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Done     | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?   | Done     | Done       | True  |
|  2 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?   | Done     | Done       | True  |
|  3 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ? | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[14, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | True  |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | True  |
### aten.arange.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 2,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.argmax.default
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1 | None     | Fallback   | True  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?   | Done     | Done       | True  |
|  3 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?    | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 49, 768]>],<br>int dim = 1 | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  2 | Tensor<[12, 50, 50]> self = ?                                                              | Done     | Done       | True  |
|  3 | Tensor<[16, 7, 7]> self = ?                                                                | Done     | Done       | True  |
|  4 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
|  5 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
### aten.div.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ? | Removed  | Done       | True  |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ? | Removed  | Done       | True  |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ? | Done     | Done       | True  |
|  1 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?   | Done     | Done       | True  |
|  2 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?    | Done     | Done       | True  |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[]> self = ?     | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       | True  |
|  1 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       | True  |
|  2 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]          | Removed  | Done       | True  |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.index.Tensor
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [<[2]>, <[2]>] | None     | Fallback   | True  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   | True  |
|  1 | Tensor<[2, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   | True  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | None     | Fallback   | True  |
### aten.mm.default
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ? | Removed  | Done       | True  |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?   | Removed  | Done       | True  |
|  2 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ? | Removed  | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702            | Done     | Done       | True  |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125             | Done     | Done       | True  |
|  3 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                   | None     | Fallback   | True  |
|  4 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702             | Done     | Done       | True  |
|  5 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Done     | Done       | True  |
|  6 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125              | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05     | Removed  | Done       | N/A   |
|  2 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0 | None     | Fallback   | True  |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       | True  |
### aten.sigmoid.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 3072]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[2, 7, 2048]> self = ?  | Done     | Done       | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Removed  | Fallback   | True  |
|  4 | Tensor<[1, 77]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Fallback   | True  |
|  5 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Done     | Done       | True  |
|  6 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  7 | Tensor<[2, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Fallback   | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?    | Done     | Done       | True  |
|  1 | Tensor<[2, 1]> self = ?      | Removed  | Done       | True  |
|  2 | Tensor<[2048, 512]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[3072, 768]> self = ? | Done     | Done       | True  |
|  4 | Tensor<[512, 2048]> self = ? | Done     | Done       | True  |
|  5 | Tensor<[512, 512]> self = ?  | Done     | Done       | True  |
|  6 | Tensor<[512, 768]> self = ?  | Done     | Done       | True  |
|  7 | Tensor<[768, 3072]> self = ? | Done     | Done       | True  |
|  8 | Tensor<[768, 768]> self = ?  | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | True  |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | True  |
|  2 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | None     | Fallback   | True  |
|  3 | Tensor<[12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  4 | Tensor<[16, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | True  |
|  5 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  6 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1 | Done     | Done       | True  |
|  1 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2 | Done     | Done       | True  |
|  2 | Tensor<[2, 7]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
|  3 | Tensor<[7, 7]> self = ?,<br>int dim = 0    | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64] | Done     | Done       | True  |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]     | Done     | Done       | True  |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64] | Done     | Done       | True  |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, 12, 64] | Done     | Done       | True  |
|  4 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]       | Done     | Done       | True  |
|  5 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]  | Removed  | Done       | True  |
|  6 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64] | Done     | Done       | True  |
|  7 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]      | Done     | Done       | True  |
|  8 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]        | Done     | Done       | True  |
|  9 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]    | Done     | Done       | True  |
| 10 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]      | Done     | Done       | True  |
| 11 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]      | Done     | Done       | True  |
| 12 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Done     | Done       | True  |
| 13 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, -1, 8, 64]   | Done     | Done       | True  |
| 14 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, 8, 64]    | Done     | Done       | True  |
| 15 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]               | Removed  | Done       | True  |
| 16 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]   | Done     | Done       | True  |
| 17 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]      | Done     | Done       | True  |
| 18 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]     | Done     | Done       | True  |
| 19 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]       | Done     | Done       | True  |

