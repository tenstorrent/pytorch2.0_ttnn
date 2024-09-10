# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  1 |           1 |
|  1 | aten._to_copy.default          |                  1 |           0 |
|  2 | aten.add.Tensor                |                  2 |           2 |
|  3 | aten.addmm.default             |                  5 |           5 |
|  4 | aten.bmm.default               |                  2 |           2 |
|  5 | aten.clone.default             |                  4 |           4 |
|  6 | aten.div.Tensor                |                  1 |           1 |
|  7 | aten.embedding.default         |                  3 |           3 |
|  8 | aten.expand.default            |                  4 |           0 |
|  9 | aten.gelu.default              |                  1 |           1 |
| 10 | aten.mul.Tensor                |                  1 |           1 |
| 11 | aten.native_layer_norm.default |                  1 |           1 |
| 12 | aten.permute.default           |                  2 |           2 |
| 13 | aten.rsub.Scalar               |                  1 |           1 |
| 14 | aten.select.int                |                  1 |           0 |
| 15 | aten.slice.Tensor              |                  6 |           0 |
| 16 | aten.split.Tensor              |                  1 |           0 |
| 17 | aten.squeeze.dim               |                  1 |           0 |
| 18 | aten.t.default                 |                  5 |           5 |
| 19 | aten.transpose.int             |                  1 |           1 |
| 20 | aten.unsqueeze.default         |                  2 |           2 |
| 21 | aten.view.default              |                 14 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ? | Done     |
|  1 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?     | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 1]> mat2 = ?        | Done     |
|  1 | Tensor<[2]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 2]> mat2 = ?       | Done     |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[25, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[25, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ? | Done     |
|  1 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ? | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?                                                             | Done     |
|  1 | Tensor<[1, 25, 12, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  2 | Tensor<[1, 25, 768]> self = ?                                                                | Done     |
|  3 | Tensor<[1, 25]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
### aten.div.Tensor
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<> other = 8.0 | Done     |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                               | Done     |
|  1 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int<> padding_idx = 0 | Done     |
|  2 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                             | Done     |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int]<> size = [1, 12, 25, 25] | Unknown  |
|  1 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int]<> size = [1, 12, 25, 64] | Unknown  |
|  2 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int]<> size = [1, 12, 64, 25] | Unknown  |
|  3 | Tensor<[1, 25]> self = ?,<br>List[int]<> size = [1, 25]                 | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 25, 3072]> self = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38 | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 25, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-12 | Done     |
### aten.permute.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>number<> other = 1.0 | Done     |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 25, 768]> self = ?,<br>int<> dim = 1,<br>int<> index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 25]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  1 | Tensor<[1, 25, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1  | Unknown  |
|  2 | Tensor<[1, 25]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1       | Unknown  |
|  3 | Tensor<[1, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Unknown  |
|  4 | Tensor<[1, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 25      | Unknown  |
|  5 | Tensor<[1, 768]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 25, 2]> self = ?,<br>int<> split_size = 1,<br>int<> dim = -1 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 25, 1]> self = ?,<br>int<> dim = -1 | Unknown  |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1, 768]> self = ?    | Done     |
|  1 | Tensor<[2, 768]> self = ?    | Done     |
|  2 | Tensor<[3072, 768]> self = ? | Done     |
|  3 | Tensor<[768, 3072]> self = ? | Done     |
|  4 | Tensor<[768, 768]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 25, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 25]> self = ?,<br>int<> dim = 2 | Done     |
|  1 | Tensor<[1, 25]> self = ?,<br>int<> dim = 1    | Done     |
### aten.view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 25, 25]> self = ?,<br>List[int]<> size = [12, 25, 25] | Unknown  |
|  1 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int]<> size = [12, 25, 64] | Unknown  |
|  2 | Tensor<[1, 12, 64, 25]> self = ?,<br>List[int]<> size = [12, 64, 25] | Unknown  |
|  3 | Tensor<[1, 1]> self = ?,<br>List[int]<> size = [1]                   | Unknown  |
|  4 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int]<> size = [1, 25, 768] | Unknown  |
|  5 | Tensor<[1, 25, 3072]> self = ?,<br>List[int]<> size = [25, 3072]     | Unknown  |
|  6 | Tensor<[1, 25, 768]> self = ?,<br>List[int]<> size = [1, 25, 12, 64] | Unknown  |
|  7 | Tensor<[1, 25, 768]> self = ?,<br>List[int]<> size = [25, 768]       | Unknown  |
|  8 | Tensor<[1, 25]> self = ?,<br>List[int]<> size = [1, 25]              | Unknown  |
|  9 | Tensor<[12, 25, 25]> self = ?,<br>List[int]<> size = [1, 12, 25, 25] | Unknown  |
| 10 | Tensor<[12, 25, 64]> self = ?,<br>List[int]<> size = [1, 12, 25, 64] | Unknown  |
| 11 | Tensor<[25, 2]> self = ?,<br>List[int]<> size = [1, 25, 2]           | Unknown  |
| 12 | Tensor<[25, 3072]> self = ?,<br>List[int]<> size = [1, 25, 3072]     | Unknown  |
| 13 | Tensor<[25, 768]> self = ?,<br>List[int]<> size = [1, 25, 768]       | Unknown  |

