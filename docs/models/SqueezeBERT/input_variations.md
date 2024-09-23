# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  1 |           0 |
|  1 | aten._to_copy.default          |                  1 |           1 |
|  2 | aten.add.Tensor                |                  3 |           1 |
|  3 | aten.addmm.default             |                  2 |           0 |
|  4 | aten.bmm.default               |                  2 |           0 |
|  5 | aten.clone.default             |                  5 |           1 |
|  6 | aten.convolution.default       |                  4 |           0 |
|  7 | aten.div.Tensor                |                  1 |           0 |
|  8 | aten.embedding.default         |                  3 |           3 |
|  9 | aten.expand.default            |                  3 |           0 |
| 10 | aten.gelu.default              |                  1 |           0 |
| 11 | aten.mul.Tensor                |                  1 |           1 |
| 12 | aten.native_layer_norm.default |                  1 |           1 |
| 13 | aten.permute.default           |                  4 |           0 |
| 14 | aten.rsub.Scalar               |                  1 |           1 |
| 15 | aten.select.int                |                  1 |           0 |
| 16 | aten.slice.Tensor              |                  5 |           4 |
| 17 | aten.t.default                 |                  2 |           0 |
| 18 | aten.tanh.default              |                  1 |           0 |
| 19 | aten.unsqueeze.default         |                  2 |           2 |
| 20 | aten.view.default              |                  7 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 8, 8]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Done     |
### aten.add.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 8, 8]> self = ?,<br>Tensor<[1, 1, 1, 8]> other = ? | Unknown  |
|  1 | Tensor<[1, 768, 8]> self = ?,<br>Tensor<[1, 768, 8]> other = ?    | Unknown  |
|  2 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?    | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3]> mat2 = ?     | Unknown  |
|  1 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 8, 64]> self = ?,<br>Tensor<[12, 64, 8]> mat2 = ? | Unknown  |
|  1 | Tensor<[12, 8, 8]> self = ?,<br>Tensor<[12, 8, 64]> mat2 = ?  | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 8]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 12, 8, 8]> self = ?                                                              | Unknown  |
|  2 | Tensor<[1, 768, 8]> self = ?                                                                | Unknown  |
|  3 | Tensor<[1, 768]> self = ?                                                                   | Unknown  |
|  4 | Tensor<[1, 8, 768]> self = ?                                                                | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3072, 8]> input = ?,<br>Tensor<[768, 768, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [0],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 4  | Unknown  |
|  1 | Tensor<[1, 768, 8]> input = ?,<br>Tensor<[3072, 192, 1]> weight = ?,<br>Optional[Tensor]<[3072]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [0],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 4 | Unknown  |
|  2 | Tensor<[1, 768, 8]> input = ?,<br>Tensor<[768, 192, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [0],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 4   | Unknown  |
|  3 | Tensor<[1, 768, 8]> input = ?,<br>Tensor<[768, 768, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int]<> stride = [1],<br>List[int]<> padding = [0],<br>List[int]<> dilation = [1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0],<br>int<> groups = 1   | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 8, 8]> self = ?,<br>Tensor<> other = 8.0 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | Done     |
|  1 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int<> padding_idx = 0 | Done     |
|  2 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | Done     |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int]<> size = [1, 12, 64, 8] | Unknown  |
|  1 | Tensor<[1, 12, 8, 64]> self = ?,<br>List[int]<> size = [1, 12, 8, 64] | Unknown  |
|  2 | Tensor<[1, 12, 8, 8]> self = ?,<br>List[int]<> size = [1, 12, 8, 8]   | Unknown  |
### aten.gelu.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1, 3072, 8]> self = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38 | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-12 | Done     |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2] | Unknown  |
|  1 | Tensor<[1, 12, 8, 64]> self = ?,<br>List[int]<> dims = [0, 1, 3, 2] | Unknown  |
|  2 | Tensor<[1, 768, 8]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Unknown  |
|  3 | Tensor<[1, 8, 768]> self = ?,<br>List[int]<> dims = [0, 2, 1]       | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8]> self = ?,<br>number<> other = 1.0 | Done     |
### aten.select.int
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 768]> self = ?,<br>int<> dim = 1,<br>int<> index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 8]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Done     |
|  1 | Tensor<[1, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1     | Done     |
|  2 | Tensor<[1, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 8      | Done     |
|  3 | Tensor<[1, 8, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1  | Unknown  |
|  4 | Tensor<[1, 8]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1       | Done     |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[3, 768]> self = ?   | Unknown  |
|  1 | Tensor<[768, 768]> self = ? | Unknown  |
### aten.tanh.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[1, 768]> self = ? | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 8]> self = ?,<br>int<> dim = 2 | Done     |
|  1 | Tensor<[1, 8]> self = ?,<br>int<> dim = 1    | Done     |
### aten.view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int]<> size = [1, 768, 8] | Unknown  |
|  1 | Tensor<[1, 12, 64, 8]> self = ?,<br>List[int]<> size = [12, 64, 8] | Unknown  |
|  2 | Tensor<[1, 12, 8, 64]> self = ?,<br>List[int]<> size = [12, 8, 64] | Unknown  |
|  3 | Tensor<[1, 12, 8, 8]> self = ?,<br>List[int]<> size = [12, 8, 8]   | Unknown  |
|  4 | Tensor<[1, 768, 8]> self = ?,<br>List[int]<> size = [1, 12, 64, 8] | Unknown  |
|  5 | Tensor<[12, 8, 64]> self = ?,<br>List[int]<> size = [1, 12, 8, 64] | Unknown  |
|  6 | Tensor<[12, 8, 8]> self = ?,<br>List[int]<> size = [1, 12, 8, 8]   | Unknown  |

