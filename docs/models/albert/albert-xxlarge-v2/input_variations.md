# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  1 |           1 |
|  1 | aten._to_copy.default          |                  1 |           0 |
|  2 | aten._unsafe_view.default      |                  1 |           0 |
|  3 | aten.add.Tensor                |                  6 |           6 |
|  4 | aten.addmm.default             |                  6 |           6 |
|  5 | aten.bmm.default               |                  2 |           2 |
|  6 | aten.clone.default             |                  4 |           3 |
|  7 | aten.div.Tensor                |                  1 |           1 |
|  8 | aten.embedding.default         |                  3 |           3 |
|  9 | aten.expand.default            |                  3 |           0 |
| 10 | aten.mul.Tensor                |                  9 |           9 |
| 11 | aten.native_layer_norm.default |                  2 |           2 |
| 12 | aten.permute.default           |                  1 |           1 |
| 13 | aten.pow.Tensor_Scalar         |                  2 |           2 |
| 14 | aten.rsub.Scalar               |                  1 |           1 |
| 15 | aten.slice.Tensor              |                  2 |           0 |
| 16 | aten.t.default                 |                  6 |           6 |
| 17 | aten.tanh.default              |                  2 |           2 |
| 18 | aten.transpose.int             |                  2 |           2 |
| 19 | aten.unsqueeze.default         |                  2 |           2 |
| 20 | aten.view.default              |                 13 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 9, 9]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int]<> size = [1, 9, 4096] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?  | Done     |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 1.0              | Done     |
|  2 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?     | Done     |
|  3 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 1.0            | Done     |
|  4 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ? | Done     |
|  5 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[128]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 128]> mat2 = ?     | Done     |
|  1 | Tensor<[16384]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 16384]> mat2 = ? | Done     |
|  2 | Tensor<[30000]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 30000]> mat2 = ?   | Done     |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[9, 128]> mat1 = ?,<br>Tensor<[128, 4096]> mat2 = ?     | Done     |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[9, 16384]> mat1 = ?,<br>Tensor<[16384, 4096]> mat2 = ? | Done     |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[9, 4096]> mat1 = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Done     |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ? | Done     |
|  1 | Tensor<[64, 9, 9]> self = ?,<br>Tensor<[64, 9, 64]> mat2 = ?  | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 9, 9]> self = ?                                                              | Done     |
|  1 | Tensor<[1, 9, 128]> self = ?                                                                | Done     |
|  2 | Tensor<[1, 9, 4096]> self = ?                                                               | Unknown  |
|  3 | Tensor<[1, 9, 64, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<> other = 8.0 | Done     |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                               | Done     |
|  1 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int<> padding_idx = 0 | Done     |
|  2 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                             | Done     |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int]<> size = [1, 64, 64, 9] | Unknown  |
|  1 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int]<> size = [1, 64, 9, 64] | Unknown  |
|  2 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int]<> size = [1, 64, 9, 9]   | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38 | Done     |
|  1 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.044715                 | Done     |
|  2 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.5                      | Done     |
|  3 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.7978845608028654       | Done     |
|  4 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?             | Done     |
|  5 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.044715               | Done     |
|  6 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.5                    | Done     |
|  7 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.7978845608028654     | Done     |
|  8 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?         | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                          | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-12     | Done     |
|  1 | Tensor<[1, 9, 4096]> input = ?,<br>List[int]<> normalized_shape = [4096],<br>Optional[Tensor]<[4096]> weight = ?,<br>Optional[Tensor]<[4096]> bias = ?,<br>float<> eps = 1e-12 | Done     |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 128]> self = ?,<br>number<> exponent = 3.0   | Done     |
|  1 | Tensor<[1, 9, 16384]> self = ?,<br>number<> exponent = 3.0 | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 9]> self = ?,<br>number<> other = 1.0 | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  1 | Tensor<[1, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 9  | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[128, 4096]> self = ?   | Done     |
|  1 | Tensor<[16384, 4096]> self = ? | Done     |
|  2 | Tensor<[30000, 128]> self = ?  | Done     |
|  3 | Tensor<[4096, 128]> self = ?   | Done     |
|  4 | Tensor<[4096, 16384]> self = ? | Done     |
|  5 | Tensor<[4096, 4096]> self = ?  | Done     |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 9, 128]> self = ?   | Done     |
|  1 | Tensor<[1, 9, 16384]> self = ? | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 9, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  1 | Tensor<[1, 64, 9, 64]> self = ?,<br>int<> dim0 = 2,<br>int<> dim1 = 1   | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 9]> self = ?,<br>int<> dim = 2 | Done     |
|  1 | Tensor<[1, 9]> self = ?,<br>int<> dim = 1    | Done     |
### aten.view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 64, 9]> self = ?,<br>List[int]<> size = [64, 64, 9]  | Unknown  |
|  1 | Tensor<[1, 64, 9, 64]> self = ?,<br>List[int]<> size = [64, 9, 64]  | Unknown  |
|  2 | Tensor<[1, 64, 9, 9]> self = ?,<br>List[int]<> size = [64, 9, 9]    | Unknown  |
|  3 | Tensor<[1, 9, 128]> self = ?,<br>List[int]<> size = [9, 128]        | Unknown  |
|  4 | Tensor<[1, 9, 16384]> self = ?,<br>List[int]<> size = [9, 16384]    | Unknown  |
|  5 | Tensor<[1, 9, 4096]> self = ?,<br>List[int]<> size = [1, 9, 64, 64] | Unknown  |
|  6 | Tensor<[1, 9, 4096]> self = ?,<br>List[int]<> size = [9, 4096]      | Unknown  |
|  7 | Tensor<[64, 9, 64]> self = ?,<br>List[int]<> size = [1, 64, 9, 64]  | Unknown  |
|  8 | Tensor<[64, 9, 9]> self = ?,<br>List[int]<> size = [1, 64, 9, 9]    | Unknown  |
|  9 | Tensor<[9, 128]> self = ?,<br>List[int]<> size = [1, 9, 128]        | Unknown  |
| 10 | Tensor<[9, 16384]> self = ?,<br>List[int]<> size = [1, 9, 16384]    | Unknown  |
| 11 | Tensor<[9, 30000]> self = ?,<br>List[int]<> size = [1, 9, 30000]    | Unknown  |
| 12 | Tensor<[9, 4096]> self = ?,<br>List[int]<> size = [1, 9, 4096]      | Unknown  |

