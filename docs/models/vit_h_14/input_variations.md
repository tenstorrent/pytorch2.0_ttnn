# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten.add.Tensor                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                               |                  5 |           5 |         0 |          0 | ✅          |    1    |
|  3 | aten.cat.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  4 | aten.clone.default                               |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  5 | aten.convolution.default                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.expand.default                              |                  1 |           0 |         1 |          0 | ✅          |    1    |
|  7 | aten.gelu.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  8 | aten.native_layer_norm.default                   |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.permute.default                             |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 10 | aten.select.int                                  |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 11 | aten.slice.Tensor                                |                  1 |           0 |         1 |          0 | ✅          |    1    |
| 12 | aten.squeeze.dim                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.t.default                                   |                  5 |           5 |         0 |          0 | ✅          |    1    |
| 14 | aten.transpose.int                               |                  4 |           3 |         0 |          0 | 🚧          |    0.75 |
| 15 | aten.unsqueeze.default                           |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 16 | aten.view.default                                |                 12 |          12 |         0 |          0 | ✅          |    1    |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 1370, 80]> query = ?,<br>Tensor<[1, 16, 1370, 80]> key = ?,<br>Tensor<[1, 16, 1370, 80]> value = ? | None     | Fallback   |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                       | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ?    | Done     | Done       | 0.999966 |      0 |
|  1 | Tensor<[1280]> self = ?,<br>Tensor<[1370, 1280]> mat1 = ?,<br>Tensor<[1280, 1280]> mat2 = ? | Done     | Done       | 0.999962 |      0 |
|  2 | Tensor<[1280]> self = ?,<br>Tensor<[1370, 5120]> mat1 = ?,<br>Tensor<[5120, 1280]> mat2 = ? | Done     | Done       | 0.999922 |      0 |
|  3 | Tensor<[3840]> self = ?,<br>Tensor<[1370, 1280]> mat1 = ?,<br>Tensor<[1280, 3840]> mat2 = ? | Done     | Done       | 0.999962 |      0 |
|  4 | Tensor<[5120]> self = ?,<br>Tensor<[1370, 1280]> mat1 = ?,<br>Tensor<[1280, 5120]> mat2 = ? | Done     | Done       | 0.999785 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 1280]>, <[1, 1369, 1280]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> self = ?                                                              | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1370, 5120]> self = ?                                                              | Done     | Done       |     1 |      0 |
|  2 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 518, 518]> input = ?,<br>Tensor<[1280, 3, 14, 14]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [14, 14],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1280]> self = ?,<br>List[int] size = [1, -1, -1] | Removed  | Done       |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1370, 5120]> self = ? | Done     | Done       | 0.999991 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                         | Status   | Isolated   | PCC   |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1370, 1280]> input = ?,<br>List[int] normalized_shape = [1280],<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>float eps = 1e-06 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1280, 1369]> self = ?,<br>List[int] dims = [0, 2, 1]      | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 1370, 80]> self = ?,<br>List[int] dims = [2, 0, 1, 3] | Done     | Done       |     1 |      0 |
### aten.select.int
|    | ATen Input Variations                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 1,<br>int index = 0    | Done     | Done       |     1 |      1 |
|  1 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       |     1 |      1 |
|  2 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       |     1 |      1 |
|  3 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       |     1 |      1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
### aten.squeeze.dim
|    | ATen Input Variations                                   | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3, 1370, 1, 1, 1280]> self = ?,<br>int dim = -2 | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1280]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1280, 1280]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1280, 5120]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[3840, 1280]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[5120, 1280]> self = ? | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1370, 1, 3, 1280]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1370, 1, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1370, 16, 80]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1370, 1, 3, 1280]> self = ?,<br>int dim = 0 | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1280, 37, 37]> self = ?,<br>List[int] size = [1, 1280, 1369]  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1370, 1280]> self = ?,<br>List[int] size = [1370, 1280]       | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1370, 5120]> self = ?,<br>List[int] size = [1370, 5120]       | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 1280]       | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1370, 1, 1280]> self = ?,<br>List[int] size = [1370, 16, 80]     | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1370, 1, 16, 80]> self = ?,<br>List[int] size = [1370, 1280]     | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1370, 1, 3840]> self = ?,<br>List[int] size = [1370, 1, 3, 1280] | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1, 1370, 1280]       | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1370, 1280]> self = ?,<br>List[int] size = [1370, 1, 1280]       | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1370, 3840]> self = ?,<br>List[int] size = [1370, 1, 3840]       | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1370, 5120]> self = ?,<br>List[int] size = [1, 1370, 5120]       | Done     | Done       |     1 |      0 |
| 11 | Tensor<[16, 1370, 80]> self = ?,<br>List[int] size = [1, 16, 1370, 80]   | Done     | Done       |     1 |      0 |

