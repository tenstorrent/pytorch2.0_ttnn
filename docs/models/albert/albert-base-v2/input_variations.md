# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  1 |           1 |
|  1 | aten._to_copy.default          |                  1 |           0 |
|  2 | aten._unsafe_view.default      |                  1 |           0 |
|  3 | aten.add.Tensor                |                  5 |           5 |
|  4 | aten.addmm.default             |                  5 |           5 |
|  5 | aten.bmm.default               |                  2 |           2 |
|  6 | aten.clone.default             |                  4 |           4 |
|  7 | aten.div.Tensor                |                  1 |           1 |
|  8 | aten.embedding.default         |                  3 |           3 |
|  9 | aten.expand.default            |                  3 |           0 |
| 10 | aten.mul.Tensor                |                  5 |           5 |
| 11 | aten.native_layer_norm.default |                  2 |           2 |
| 12 | aten.permute.default           |                  1 |           1 |
| 13 | aten.pow.Tensor_Scalar         |                  1 |           1 |
| 14 | aten.rsub.Scalar               |                  1 |           1 |
| 15 | aten.slice.Tensor              |                  2 |           0 |
| 16 | aten.t.default                 |                  5 |           5 |
| 17 | aten.tanh.default              |                  1 |           1 |
| 18 | aten.transpose.int             |                  2 |           2 |
| 19 | aten.unsqueeze.default         |                  2 |           2 |
| 20 | aten.view.default              |                 12 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int]<> size = [1, 12, 768] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ? | Done     |
|  1 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?     | Done     |
|  2 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<> other = 1.0              | Done     |
|  3 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?   | Done     |
|  4 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?     | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2]> self = ?,<br>Tensor<[12, 768]> mat1 = ?,<br>Tensor<[768, 2]> mat2 = ?       | Done     |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[12, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[12, 128]> mat1 = ?,<br>Tensor<[128, 768]> mat2 = ?   | Done     |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[12, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[12, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 12, 12]> self = ?,<br>Tensor<[12, 12, 64]> mat2 = ? | Done     |
|  1 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ? | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?                                                             | Done     |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  2 | Tensor<[1, 12, 128]> self = ?                                                                | Done     |
|  3 | Tensor<[1, 12, 768]> self = ?                                                                | Done     |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<> other = 8.0 | Done     |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                               | Done     |
|  1 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int<> padding_idx = 0 | Done     |
|  2 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                             | Done     |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int]<> size = [1, 12, 12, 12] | Unknown  |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int]<> size = [1, 12, 12, 64] | Unknown  |
|  2 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int]<> size = [1, 12, 64, 12] | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38 | Done     |
|  1 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<> other = 0.044715                | Done     |
|  2 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<> other = 0.5                     | Done     |
|  3 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654      | Done     |
|  4 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?          | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 128]> input = ?,<br>List[int]<> normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float<> eps = 1e-12 | Done     |
|  1 | Tensor<[1, 12, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-12 | Done     |
### aten.permute.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 3072]> self = ?,<br>number<> exponent = 3.0 | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 12]> self = ?,<br>number<> other = 1.0 | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  1 | Tensor<[1, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 12 | Unknown  |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[2, 768]> self = ?    | Done     |
|  1 | Tensor<[3072, 768]> self = ? | Done     |
|  2 | Tensor<[768, 128]> self = ?  | Done     |
|  3 | Tensor<[768, 3072]> self = ? | Done     |
|  4 | Tensor<[768, 768]> self = ?  | Done     |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 12, 3072]> self = ? | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>int<> dim0 = 2,<br>int<> dim1 = 1   | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 12]> self = ?,<br>int<> dim = 2 | Done     |
|  1 | Tensor<[1, 12]> self = ?,<br>int<> dim = 1    | Done     |
### aten.view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 12, 12]> self = ?,<br>List[int]<> size = [12, 12, 12] | Unknown  |
|  1 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int]<> size = [12, 12, 64] | Unknown  |
|  2 | Tensor<[1, 12, 128]> self = ?,<br>List[int]<> size = [12, 128]       | Unknown  |
|  3 | Tensor<[1, 12, 3072]> self = ?,<br>List[int]<> size = [12, 3072]     | Unknown  |
|  4 | Tensor<[1, 12, 64, 12]> self = ?,<br>List[int]<> size = [12, 64, 12] | Unknown  |
|  5 | Tensor<[1, 12, 768]> self = ?,<br>List[int]<> size = [1, 12, 12, 64] | Unknown  |
|  6 | Tensor<[1, 12, 768]> self = ?,<br>List[int]<> size = [12, 768]       | Unknown  |
|  7 | Tensor<[12, 12, 12]> self = ?,<br>List[int]<> size = [1, 12, 12, 12] | Unknown  |
|  8 | Tensor<[12, 12, 64]> self = ?,<br>List[int]<> size = [1, 12, 12, 64] | Unknown  |
|  9 | Tensor<[12, 2]> self = ?,<br>List[int]<> size = [1, 12, 2]           | Unknown  |
| 10 | Tensor<[12, 3072]> self = ?,<br>List[int]<> size = [1, 12, 3072]     | Unknown  |
| 11 | Tensor<[12, 768]> self = ?,<br>List[int]<> size = [1, 12, 768]       | Unknown  |

