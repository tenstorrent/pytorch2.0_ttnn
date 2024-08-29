# High Level Operations Status
|    | Operations                                       |   Input Variations |
|---:|:-------------------------------------------------|-------------------:|
|  0 | aten._scaled_dot_product_flash_attention.default |                  2 |
|  1 | aten.add.Tensor                                  |                  1 |
|  2 | aten.addmm.default                               |                  1 |
|  3 | aten.argmax.default                              |                  1 |
|  4 | aten.cat.default                                 |                  1 |
|  5 | aten.clone.default                               |                  2 |
|  6 | aten.convolution.default                         |                  2 |
|  7 | aten.embedding.default                           |                  1 |
|  8 | aten.gelu.default                                |                  1 |
|  9 | aten.mm.default                                  |                  1 |
| 10 | aten.mul.Tensor                                  |                  1 |
| 11 | aten.native_layer_norm.default                   |                  1 |
| 12 | aten.ones.default                                |                  1 |
| 13 | aten.permute.default                             |                  1 |
| 14 | aten.select.int                                  |                  2 |
| 15 | aten.slice.Tensor                                |                  3 |
| 16 | aten.t.default                                   |                  1 |
| 17 | aten.transpose.int                               |                  1 |
| 18 | aten.view.default                                |                 16 |
***
### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 1500, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                            | Unknown  |
|  1 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>float dropout_p = 0.0,<br>bool is_causal = True | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[1500, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.argmax.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 51865]> self = ?,<br>Optional[int] dim = -1 | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [mul, mul_1, mul_2, mul_3],<br>int dim = -1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 1500, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 1500, 768]> self = ?                                                              | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 3000]> input = ?,<br>Tensor<[768, 768, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [2],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | Unknown  |
|  1 | Tensor<[1, 80, 3000]> input = ?,<br>Tensor<[768, 80, 3]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [1],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1   | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 768, 3000]> self = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50258 | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1500, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.ones.default
|    | ATen Input Variations                                                                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1] | Unknown  |
### aten.select.int
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  |
|  1 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0            | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 80, 3000]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1         | Unknown  |
|  1 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 1             | Unknown  |
|  2 | Tensor<[448, 768]> self = ?,<br>int dim = 0,<br>Optional[int]<s2> start = ?,<br>Optional[int]<s2 + 1> end = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[768, 768]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]       | Unknown  |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]         | Unknown  |
|  2 | Tensor<[1, 1500, 3072]> self = ?,<br>List[int] size = [1500, 3072] | Unknown  |
|  3 | Tensor<[1, 1500, 768]> self = ?,<br>List[int] size = [1500, 768]   | Unknown  |
|  4 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]               | Unknown  |
|  5 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]       | Unknown  |
|  6 | Tensor<[1, 4, 3072]> self = ?,<br>List[int] size = [4, 3072]       | Unknown  |
|  7 | Tensor<[1, 4, 768]> self = ?,<br>List[int] size = [4, 768]         | Unknown  |
|  8 | Tensor<[1, 4]> self = ?,<br>List[int] size = [-1, 4]               | Unknown  |
|  9 | Tensor<[1, 51865]> self = ?,<br>List[int] size = [1, 1, 51865]     | Unknown  |
| 10 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]         | Unknown  |
| 11 | Tensor<[1500, 3072]> self = ?,<br>List[int] size = [1, 1500, 3072] | Unknown  |
| 12 | Tensor<[1500, 768]> self = ?,<br>List[int] size = [1, 1500, 768]   | Unknown  |
| 13 | Tensor<[4, 3072]> self = ?,<br>List[int] size = [1, 4, 3072]       | Unknown  |
| 14 | Tensor<[4, 51865]> self = ?,<br>List[int] size = [1, 4, 51865]     | Unknown  |
| 15 | Tensor<[4, 768]> self = ?,<br>List[int] size = [1, 4, 768]         | Unknown  |

