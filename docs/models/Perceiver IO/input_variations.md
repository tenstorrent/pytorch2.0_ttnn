# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.add.Tensor                |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default             |                  6 |           6 |         0 |          0 | ✅          |       1 |
|  4 | aten.arange.start              |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  5 | aten.bmm.default               |                  6 |           6 |         0 |          0 | ✅          |       1 |
|  6 | aten.clone.default             |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  7 | aten.div.Tensor                |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  8 | aten.embedding.default         |                  3 |           2 |         1 |          0 | ✅          |       1 |
|  9 | aten.expand.default            |                 12 |           2 |        10 |          0 | ✅          |       1 |
| 10 | aten.gelu.default              |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 11 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.mul.Tensor                |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 13 | aten.native_layer_norm.default |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 14 | aten.permute.default           |                  7 |           7 |         0 |          0 | ✅          |       1 |
| 15 | aten.rsub.Scalar               |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 16 | aten.slice.Tensor              |                  2 |           0 |         2 |          0 | ✅          |       1 |
| 17 | aten.t.default                 |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 18 | aten.transpose.int             |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 19 | aten.unsqueeze.default         |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 20 | aten.view.default              |                 32 |          32 |         0 |          0 | ✅          |       1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 2048, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  1 | Tensor<[1, 8, 256, 2048]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  2 | Tensor<[1, 8, 256, 256]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?     | Done     | Done       | True  |
|  1 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?        | Done     | Done       | True  |
|  2 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?     | Done     | Done       | True  |
|  3 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ? | Done     | Done       | True  |
|  4 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                 | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1280]> self = ?,<br>Tensor<[2048, 768]> mat1 = ?,<br>Tensor<[768, 1280]> mat2 = ?  | Done     | Done       | True  |
|  1 | Tensor<[1280]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[256]> self = ?,<br>Tensor<[2048, 768]> mat1 = ?,<br>Tensor<[768, 256]> mat2 = ?    | Done     | Done       | True  |
|  3 | Tensor<[256]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 256]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[2048, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Done     | Done       | True  |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[256, 1280]> mat1 = ?,<br>Tensor<[1280, 768]> mat2 = ?   | Done     | Done       | True  |
### aten.arange.start
|    | ATen Input Variations                                                                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number start = 0,<br>number end = 2048,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Fallback   | True  |
### aten.bmm.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[8, 2048, 256]> self = ?,<br>Tensor<[8, 256, 96]> mat2 = ?   | Done     | Done       | True  |
|  1 | Tensor<[8, 2048, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?    | Done     | Done       | True  |
|  2 | Tensor<[8, 256, 2048]> self = ?,<br>Tensor<[8, 2048, 160]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 160]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?    | Done     | Done       | True  |
|  5 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?     | Done     | Done       | True  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 8, 96]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  1 | Tensor<[1, 256, 8, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  2 | Tensor<[1, 8, 2048, 256]> self = ?                                                          | Done     | Done       | True  |
|  3 | Tensor<[1, 8, 256, 2048]> self = ?                                                          | Done     | Done       | True  |
|  4 | Tensor<[1, 8, 256, 256]> self = ?                                                           | Done     | Done       | True  |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | True  |
|  1 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | True  |
|  2 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | True  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2048, 768]> weight = ?,<br>Tensor indices = ?           | Done     | Unknown    | N/A   |
|  1 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[2048]> indices = ?   | Removed  | Done       | True  |
|  2 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ? | Done     | Done       | True  |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [1, 8, 2048, 160] | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256] | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [1, 8, 2048, 32]   | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]   | Removed  | Fallback   | True  |
|  4 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048] | Removed  | Fallback   | True  |
|  5 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]   | Removed  | Fallback   | True  |
|  6 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [1, 8, 256, 32]     | Removed  | Fallback   | True  |
|  7 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [1, 8, 256, 96]     | Removed  | Fallback   | True  |
|  8 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [1, 8, 32, 2048]   | Removed  | Fallback   | True  |
|  9 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [1, 8, 32, 256]     | Removed  | Fallback   | True  |
| 10 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Done     | Done       | True  |
| 11 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, -1, -1]             | Done     | Done       | True  |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 768]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 256, 1280]> self = ? | Done     | Done       | True  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2048, 768]> self = ?,<br>Tensor<[768, 262]> mat2 = ? | Done     | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | N/A   |
|  1 | Tensor<[1, 256, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
|  1 | Tensor<[1, 2048, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       | True  |
|  2 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       | True  |
|  3 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       | True  |
|  4 | Tensor<[1, 256, 8, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       | True  |
|  5 | Tensor<[1, 8, 2048, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       | True  |
|  6 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Done       | True  |
### aten.rsub.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0 | Done     | Done       | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Removed  | Fallback   | True  |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1280, 1280]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1280, 768]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[256, 1280]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[256, 768]> self = ?   | Done     | Done       | True  |
|  4 | Tensor<[768, 1280]> self = ?  | Done     | Done       | True  |
|  5 | Tensor<[768, 768]> self = ?   | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 8, 2048, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
|  1 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2  | Done     | Done       | True  |
|  2 | Tensor<[262, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 2 | Done     | Done       | True  |
|  1 | Tensor<[1, 2048]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 8, 160] | Done     | Done       | True  |
|  1 | Tensor<[1, 2048, 256]> self = ?,<br>List[int] size = [1, 2048, 8, 32]   | Done     | Done       | True  |
|  2 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [-1, 768]          | Done     | Unknown    | N/A   |
|  3 | Tensor<[1, 2048, 768]> self = ?,<br>List[int] size = [2048, 768]        | Done     | Done       | True  |
|  4 | Tensor<[1, 2048, 8, 96]> self = ?,<br>List[int] size = [1, 2048, 768]   | Done     | Done       | True  |
|  5 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [1, 256, 8, 160]   | Done     | Done       | True  |
|  6 | Tensor<[1, 256, 1280]> self = ?,<br>List[int] size = [256, 1280]        | Done     | Done       | True  |
|  7 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [1, 256, 8, 32]     | Done     | Done       | True  |
|  8 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 256, 8, 96]     | Done     | Done       | True  |
|  9 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] size = [1, 256, 1280]   | Done     | Done       | True  |
| 10 | Tensor<[1, 8, 2048, 160]> self = ?,<br>List[int] size = [8, 2048, 160]  | Done     | Done       | True  |
| 11 | Tensor<[1, 8, 2048, 256]> self = ?,<br>List[int] size = [8, 2048, 256]  | Done     | Done       | True  |
| 12 | Tensor<[1, 8, 2048, 32]> self = ?,<br>List[int] size = [8, 2048, 32]    | Done     | Done       | True  |
| 13 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] size = [8, 256, 160]    | Done     | Done       | True  |
| 14 | Tensor<[1, 8, 256, 2048]> self = ?,<br>List[int] size = [8, 256, 2048]  | Done     | Done       | True  |
| 15 | Tensor<[1, 8, 256, 256]> self = ?,<br>List[int] size = [8, 256, 256]    | Done     | Done       | True  |
| 16 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] size = [8, 256, 32]      | Done     | Done       | True  |
| 17 | Tensor<[1, 8, 256, 96]> self = ?,<br>List[int] size = [8, 256, 96]      | Done     | Done       | True  |
| 18 | Tensor<[1, 8, 32, 2048]> self = ?,<br>List[int] size = [8, 32, 2048]    | Done     | Done       | True  |
| 19 | Tensor<[1, 8, 32, 256]> self = ?,<br>List[int] size = [8, 32, 256]      | Done     | Done       | True  |
| 20 | Tensor<[2048, 1280]> self = ?,<br>List[int] size = [1, 2048, 1280]      | Done     | Done       | True  |
| 21 | Tensor<[2048, 256]> self = ?,<br>List[int] size = [1, 2048, 256]        | Done     | Done       | True  |
| 22 | Tensor<[2048, 262]> self = ?,<br>List[int] size = [1, 2048, 262]        | Done     | Unknown    | N/A   |
| 23 | Tensor<[2048, 768]> self = ?,<br>List[int] size = [1, 2048, 768]        | Done     | Done       | True  |
| 24 | Tensor<[256, 1280]> self = ?,<br>List[int] size = [1, 256, 1280]        | Done     | Done       | True  |
| 25 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]          | Done     | Done       | True  |
| 26 | Tensor<[256, 768]> self = ?,<br>List[int] size = [1, 256, 768]          | Done     | Done       | True  |
| 27 | Tensor<[8, 2048, 256]> self = ?,<br>List[int] size = [1, 8, 2048, 256]  | Done     | Done       | True  |
| 28 | Tensor<[8, 2048, 96]> self = ?,<br>List[int] size = [1, 8, 2048, 96]    | Done     | Done       | True  |
| 29 | Tensor<[8, 256, 160]> self = ?,<br>List[int] size = [1, 8, 256, 160]    | Done     | Done       | True  |
| 30 | Tensor<[8, 256, 2048]> self = ?,<br>List[int] size = [1, 8, 256, 2048]  | Done     | Done       | True  |
| 31 | Tensor<[8, 256, 256]> self = ?,<br>List[int] size = [1, 8, 256, 256]    | Done     | Done       | True  |

