# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten.add.Tensor                |                  1 |
|  1 | aten.addmm.default             |                  1 |
|  2 | aten.clone.default             |                  1 |
|  3 | aten.convolution.default       |                  1 |
|  4 | aten.gelu.default              |                  1 |
|  5 | aten.mean.dim                  |                  1 |
|  6 | aten.mm.default                |                  1 |
|  7 | aten.native_layer_norm.default |                  1 |
|  8 | aten.t.default                 |                  1 |
|  9 | aten.transpose.int             |                  1 |
| 10 | aten.view.default              |                  8 |
***
### aten.add.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[196]> self = ?,<br>Tensor<[768, 384]> mat1 = ?,<br>Tensor<[384, 196]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 768, 384]> self = ? | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 768, 384]> self = ? | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1] | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 384]> mat2 = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[384, 196]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 3072]> self = ?,<br>List[int] size = [196, 3072]     | Unknown  |
|  1 | Tensor<[1, 196, 768]> self = ?,<br>List[int] size = [196, 768]       | Unknown  |
|  2 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196] | Unknown  |
|  3 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [768, 196]       | Unknown  |
|  4 | Tensor<[1, 768, 384]> self = ?,<br>List[int] size = [768, 384]       | Unknown  |
|  5 | Tensor<[196, 3072]> self = ?,<br>List[int] size = [1, 196, 3072]     | Unknown  |
|  6 | Tensor<[196, 768]> self = ?,<br>List[int] size = [1, 196, 768]       | Unknown  |
|  7 | Tensor<[768, 384]> self = ?,<br>List[int] size = [1, 768, 384]       | Unknown  |

