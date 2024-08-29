# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._unsafe_view.default      |                  1 |
|  1 | aten.add.Tensor                |                  1 |
|  2 | aten.addmm.default             |                  1 |
|  3 | aten.clone.default             |                  2 |
|  4 | aten.convolution.default       |                  1 |
|  5 | aten.gelu.default              |                  1 |
|  6 | aten.mean.dim                  |                  1 |
|  7 | aten.native_layer_norm.default |                  1 |
|  8 | aten.permute.default           |                  2 |
|  9 | aten.t.default                 |                  1 |
| 10 | aten.view.default              |                  7 |
***
### aten._unsafe_view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] size = [1, 256, 768] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[512]> self = ?,<br>Tensor<[256, 768]> mat1 = ?,<br>Tensor<[768, 512]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 512]> self = ?                                                                   | Unknown  |
|  1 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 512]> input = ?,<br>Tensor<[1024, 256, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 1024, 512]> self = ? | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 512]> self = ?,<br>Optional[List[int]] dim = [1] | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 4, 3, 5, 1] | Unknown  |
|  1 | Tensor<[1, 512]> self = ?,<br>List[int] dims = [0, 1]                           | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[512, 768]> self = ? | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                | Unknown  |
|  1 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                | Unknown  |
|  2 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                | Unknown  |
|  3 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16] | Unknown  |
|  4 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 512]                       | Unknown  |
|  5 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                | Unknown  |
|  6 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                | Unknown  |

