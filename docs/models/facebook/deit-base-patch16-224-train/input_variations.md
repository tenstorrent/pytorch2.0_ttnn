# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                   |                  1 |           0 |         1 |          0 | ✅          |    1    |
|  1 | aten._softmax_backward_data.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._unsafe_view.default               |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor                         |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  4 | aten.addmm.default                      |                  4 |           3 |         1 |          0 | ✅          |    1    |
|  5 | aten.bmm.default                        |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  6 | aten.cat.default                        |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default                      |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  8 | aten.convolution.default                |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.convolution_backward.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.detach.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.div.Tensor                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.expand.default                     |                  4 |           0 |         4 |          0 | ✅          |    1    |
| 13 | aten.gelu.default                       |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 14 | aten.gelu_backward.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.mm.default                         |                  8 |           7 |         1 |          0 | ✅          |    1    |
| 16 | aten.native_layer_norm.default          |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 17 | aten.native_layer_norm_backward.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.permute.default                    |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 19 | aten.select.int                         |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 20 | aten.select_backward.default            |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.slice.Tensor                       |                  4 |           1 |         3 |          0 | ✅          |    1    |
| 22 | aten.slice_backward.default             |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.sum.dim_IntList                    |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.t.default                          |                  8 |           8 |         0 |          0 | ✅          |    1    |
| 25 | aten.transpose.int                      |                  7 |           3 |         1 |          0 | 🚧          |    0.57 |
| 26 | aten.view.default                       |                 17 |           7 |        10 |          0 | ✅          |    1    |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Removed  | Done       | True  |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> grad_output = ?,<br>Tensor<[1, 12, 197, 197]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | None     | Fallback   | True  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768] | Done     | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ? | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?   | Removed  | Done       | True  |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[197, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[197, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | True  |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?  | Done     | Done       | True  |
|  2 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ? | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 196, 768]>],<br>int dim = 1 | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?                                                          | Done     | Done       | True  |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  2 | Tensor<[1, 197, 768]> self = ?                                                              | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 14, 14]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[List[int]] bias_sizes = [768],<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   | True  |
### aten.detach.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> self = ? | None     | Fallback   | True  |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0 | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1]             | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Removed  | Fallback   | True  |
|  3 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Removed  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 3072]> self = ? | Done     | Done       | True  |
### aten.gelu_backward.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 3072]> grad_output = ?,<br>Tensor<[1, 197, 3072]> self = ? | None     | Fallback   | True  |
### aten.mm.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 768]> mat2 = ?   | Removed  | Done       | True  |
|  1 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?      | Done     | Done       | True  |
|  2 | Tensor<[197, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | Done       | True  |
|  4 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | True  |
|  5 | Tensor<[3072, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?  | Done     | Done       | True  |
|  6 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 3072]> mat2 = ?  | Done     | Done       | True  |
|  7 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?   | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Removed  | Done       | N/A   |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> grad_out = ?,<br>Tensor<[1, 197, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 197, 1]> mean = ?,<br>Tensor<[1, 197, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   | True  |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
|  1 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
### aten.select.int
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Removed  | Done       | True  |
### aten.select_backward.default
|    | ATen Input Variations                                                                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 768],<br>int dim = 1,<br>int index = 0 | None     | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Removed  | Done       | True  |
|  2 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 197                 | Done     | Done       | True  |
|  3 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Removed  | Fallback   | True  |
### aten.slice_backward.default
|    | ATen Input Variations                                                                                                                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 197, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 197, 768],<br>int dim = 0,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | None     | Fallback   | True  |
|  1 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 768],<br>int dim = 1,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1           | None     | Fallback   | True  |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True   | None     | Fallback   | True  |
|  1 | Tensor<[197, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | None     | Fallback   | True  |
|  2 | Tensor<[197, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True  | None     | Fallback   | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1000]> self = ?   | Done     | Done       | True  |
|  1 | Tensor<[1000, 768]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[197, 3072]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[197, 768]> self = ?  | Done     | Done       | True  |
|  4 | Tensor<[3072, 768]> self = ? | Done     | Done       | True  |
|  5 | Tensor<[768, 1000]> self = ? | Done     | Done       | True  |
|  6 | Tensor<[768, 3072]> self = ? | Done     | Done       | True  |
|  7 | Tensor<[768, 768]> self = ?  | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
|  1 | Tensor<[1, 12, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | None     | Fallback   | True  |
|  2 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       | True  |
|  3 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Removed  | Done       | True  |
|  4 | Tensor<[12, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | None     | Fallback   | True  |
|  5 | Tensor<[12, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       | True  |
|  6 | Tensor<[12, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | None     | Fallback   | True  |
### aten.view.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                 | Removed  | Done       | True  |
|  1 | Tensor<[1, 12, 197, 197]> self = ?,<br>List[int] size = [12, 197, 197] | Done     | Done       | True  |
|  2 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] size = [12, 197, 64]   | Done     | Done       | True  |
|  3 | Tensor<[1, 12, 64, 197]> self = ?,<br>List[int] size = [12, 64, 197]   | Removed  | Done       | True  |
|  4 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] size = [1, 197, 768]   | Done     | Done       | True  |
|  5 | Tensor<[1, 197, 3072]> self = ?,<br>List[int] size = [197, 3072]       | Removed  | Done       | True  |
|  6 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [1, 197, 12, 64]   | Done     | Done       | True  |
|  7 | Tensor<[1, 197, 768]> self = ?,<br>List[int] size = [197, 768]         | Removed  | Done       | True  |
|  8 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]                 | Removed  | Done       | True  |
|  9 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196]   | Done     | Done       | True  |
| 10 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [1, 768, 14, 14]   | Removed  | Done       | True  |
| 11 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]                   | Removed  | Done       | True  |
| 12 | Tensor<[12, 197, 197]> self = ?,<br>List[int] size = [1, 12, 197, 197] | Removed  | Done       | True  |
| 13 | Tensor<[12, 197, 64]> self = ?,<br>List[int] size = [1, 12, 197, 64]   | Done     | Done       | True  |
| 14 | Tensor<[12, 64, 197]> self = ?,<br>List[int] size = [1, 12, 64, 197]   | Removed  | Done       | True  |
| 15 | Tensor<[197, 3072]> self = ?,<br>List[int] size = [1, 197, 3072]       | Removed  | Done       | True  |
| 16 | Tensor<[197, 768]> self = ?,<br>List[int] size = [1, 197, 768]         | Done     | Done       | True  |

