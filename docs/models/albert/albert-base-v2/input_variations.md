# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._to_copy.default          |                  1 |
|  2 | aten._unsafe_view.default      |                  1 |
|  3 | aten.add.Tensor                |                  2 |
|  4 | aten.addmm.default             |                  1 |
|  5 | aten.bmm.default               |                  1 |
|  6 | aten.clone.default             |                  2 |
|  7 | aten.div.Tensor                |                  1 |
|  8 | aten.embedding.default         |                  2 |
|  9 | aten.expand.default            |                  3 |
| 10 | aten.mul.Tensor                |                  3 |
| 11 | aten.native_layer_norm.default |                  2 |
| 12 | aten.permute.default           |                  1 |
| 13 | aten.pow.Tensor_Scalar         |                  1 |
| 14 | aten.rsub.Scalar               |                  1 |
| 15 | aten.slice.Tensor              |                  1 |
| 16 | aten.t.default                 |                  1 |
| 17 | aten.tanh.default              |                  1 |
| 18 | aten.transpose.int             |                  1 |
| 19 | aten.unsqueeze.default         |                  2 |
| 20 | aten.view.default              |                 11 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 768] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ? | Unknown  |
|  1 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0            | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[12, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 128]> self = ?                                                              | Unknown  |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                             | Unknown  |
|  1 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12] | Unknown  |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64] | Unknown  |
|  2 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [1, 12, 64, 12] | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.4028234663852886e+38 | Unknown  |
|  1 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?        | Unknown  |
|  2 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                     | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-12 | Unknown  |
|  1 | Tensor<[1, 12, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-12 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                            | Status   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[768, 128]> self = ? | Unknown  |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 12, 3072]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 12]> self = ?,<br>int dim = 1    | Unknown  |
|  1 | Tensor<[1, 1, 12]> self = ?,<br>int dim = 2 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 12, 64]> self = ?,<br>List[int] size = [1, 12, 12, 64] | Unknown  |
|  1 | Tensor<[1, 12, 3072]> self = ?,<br>List[int] size = [12, 3072]     | Unknown  |
|  2 | Tensor<[1, 12, 128]> self = ?,<br>List[int] size = [12, 128]       | Unknown  |
|  3 | Tensor<[12, 3072]> self = ?,<br>List[int] size = [1, 12, 3072]     | Unknown  |
|  4 | Tensor<[12, 12, 12]> self = ?,<br>List[int] size = [1, 12, 12, 12] | Unknown  |
|  5 | Tensor<[12, 2]> self = ?,<br>List[int] size = [1, 12, 2]           | Unknown  |
|  6 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] size = [12, 12, 64] | Unknown  |
|  7 | Tensor<[1, 12, 768]> self = ?,<br>List[int] size = [12, 768]       | Unknown  |
|  8 | Tensor<[12, 768]> self = ?,<br>List[int] size = [1, 12, 768]       | Unknown  |
|  9 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int] size = [12, 64, 12] | Unknown  |
| 10 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int] size = [12, 12, 12] | Unknown  |

