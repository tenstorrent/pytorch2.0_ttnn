# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten.add.Tensor                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                               |                  5 |           5 |         0 |          0 | ✅          |    1    |
|  3 | aten.cat.default                                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.clone.default                               |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  5 | aten.convolution.default                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.expand.default                              |                  1 |           0 |         1 |          0 | ✅          |    1    |
|  7 | aten.gelu.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  8 | aten.native_layer_norm.default                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.permute.default                             |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 10 | aten.select.int                                  |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.slice.Tensor                                |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 12 | aten.squeeze.dim                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.t.default                                   |                  5 |           5 |         0 |          0 | ✅          |    1    |
| 14 | aten.transpose.int                               |                  4 |           3 |         0 |          0 | 🚧          |    0.75 |
| 15 | aten.unsqueeze.default                           |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 16 | aten.view.default                                |                 12 |           6 |         0 |          0 | 🚧          |    0.5  |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                       | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 50, 64]> query = ?,<br>Tensor<[1, 12, 50, 64]> key = ?,<br>Tensor<[1, 12, 50, 64]> value = ? | None     | Fallback   | True  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ? | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1000]> mat2 = ?  | Done     | Done       | True  |
|  1 | Tensor<[2304]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 2304]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | True  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 49, 768]>],<br>int dim = 1 | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 3072]> self = ?                                                             | Done     | Done       | True  |
|  1 | Tensor<[1, 50, 768]> self = ?                                                              | Done     | Done       | True  |
|  2 | Tensor<[3, 50, 1, 768]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, -1] | Removed  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 3072]> self = ? | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Done     | Done       | N/A   |
### aten.permute.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3] | Done     | Done       | True  |
|  1 | Tensor<[1, 768, 49]> self = ?,<br>List[int] dims = [0, 2, 1]       | None     | Fallback   | True  |
### aten.select.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0    | None     | Fallback   | True  |
|  1 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  2 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  3 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
### aten.squeeze.dim
|    | ATen Input Variations                                | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3, 50, 1, 1, 768]> self = ?,<br>int dim = -2 | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 768]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[2304, 768]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[3072, 768]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[768, 3072]> self = ? | Done     | Done       | True  |
|  4 | Tensor<[768, 768]> self = ?  | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | None     | Fallback   | True  |
|  1 | Tensor<[1, 50, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       | True  |
|  2 | Tensor<[50, 1, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       | True  |
|  3 | Tensor<[50, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1        | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[50, 1, 3, 768]> self = ?,<br>int dim = 0 | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]      | None     | Fallback   | True  |
|  1 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]        | None     | Fallback   | True  |
|  2 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]   | None     | Fallback   | True  |
|  3 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64]  | None     | Fallback   | True  |
|  4 | Tensor<[50, 1, 12, 64]> self = ?,<br>List[int] size = [50, 768]     | Done     | Done       | True  |
|  5 | Tensor<[50, 1, 2304]> self = ?,<br>List[int] size = [50, 1, 3, 768] | Done     | Done       | True  |
|  6 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 12, 64]     | Done     | Done       | True  |
|  7 | Tensor<[50, 1, 768]> self = ?,<br>List[int] size = [50, 768]        | Done     | Done       | True  |
|  8 | Tensor<[50, 2304]> self = ?,<br>List[int] size = [50, 1, 2304]      | Done     | Done       | True  |
|  9 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]      | None     | Fallback   | True  |
| 10 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]        | None     | Fallback   | True  |
| 11 | Tensor<[50, 768]> self = ?,<br>List[int] size = [50, 1, 768]        | Done     | Done       | True  |

