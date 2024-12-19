# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  1 | aten.add.Tensor                |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  2 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  3 | aten.clone.default             |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  4 | aten.convolution.default       |                  2 |           0 |         0 |          0 | ✘           |     0   |
|  5 | aten.gelu.default              |                  2 |           2 |         0 |          0 | ✅          |     1   |
|  6 | aten.mean.dim                  |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  7 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  8 | aten.permute.default           |                  2 |           1 |         0 |          0 | 🚧          |     0.5 |
|  9 | aten.t.default                 |                  4 |           4 |         0 |          0 | ✅          |     1   |
| 10 | aten.view.default              |                  6 |           6 |         0 |          0 | ✅          |     1   |
***
### aten._unsafe_view.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] size = [1, 256, 768] | Done     | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 512]> mat1 = ?,<br>Tensor<[512, 1000]> mat2 = ? | Done     | Done       | 0.999968 |      0 |
|  1 | Tensor<[256]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 256]> mat2 = ? | Done     | Done       | 0.999927 |      0 |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 512]> mat2 = ? | Done     | Done       | 0.999964 |      0 |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[256, 768]> mat1 = ?,<br>Tensor<[768, 512]> mat2 = ? | Done     | Done       | 0.999885 |      0 |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 512]> self = ?                                                                   | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 256, 256]> self = ?                                                                    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 256, 512]> self = ?                                                                    | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 512]> input = ?,<br>Tensor<[256, 1024, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 256, 512]> input = ?,<br>Tensor<[1024, 256, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | None     | Fallback   |     1 |     -1 |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 512]> self = ? | Done     | Done       | 0.999991 |      0 |
|  1 | Tensor<[1, 256, 256]> self = ?  | Done     | Done       | 0.999992 |      0 |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512, 256]> self = ?,<br>Optional[List[int]] dim = [2] | Done     | Done       |     1 |      0 |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Isolated   | PCC   |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 256, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |      1 |
### aten.permute.default
|    | ATen Input Variations                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 512]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 4, 3, 5, 1] | None     | Fallback   |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 512]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[256, 512]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[512, 256]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[512, 768]> self = ?  | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16] | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                | Done     | Done       |     1 |     -1 |

