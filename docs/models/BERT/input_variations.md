# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  1 |           1 |
|  1 | aten._to_copy.default          |                  1 |           0 |
|  2 | aten.add.Tensor                |                  2 |           2 |
|  3 | aten.addmm.default             |                  4 |           4 |
|  4 | aten.bmm.default               |                  2 |           2 |
|  5 | aten.clone.default             |                  4 |           4 |
|  6 | aten.div.Tensor                |                  1 |           1 |
|  7 | aten.embedding.default         |                  3 |           3 |
|  8 | aten.expand.default            |                  3 |           0 |
|  9 | aten.gelu.default              |                  1 |           1 |
| 10 | aten.mul.Tensor                |                  1 |           1 |
| 11 | aten.native_layer_norm.default |                  1 |           1 |
| 12 | aten.permute.default           |                  2 |           2 |
| 13 | aten.rsub.Scalar               |                  1 |           1 |
| 14 | aten.slice.Tensor              |                  4 |           0 |
| 15 | aten.split.Tensor              |                  1 |           0 |
| 16 | aten.squeeze.dim               |                  1 |           0 |
| 17 | aten.t.default                 |                  4 |           4 |
| 18 | aten.transpose.int             |                  1 |           1 |
| 19 | aten.unsqueeze.default         |                  2 |           2 |
| 20 | aten.view.default              |                 12 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>Optional[int]<> dtype = torch.bfloat16 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor<[1, 1, 1, 256]> other = ? | Done     |
|  1 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?    | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[256, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     |
|  2 | Tensor<[2]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 2]> mat2 = ?       | Done     |
|  3 | Tensor<[4096]> self = ?,<br>Tensor<[256, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 256, 256]> self = ?,<br>Tensor<[16, 256, 64]> mat2 = ? | Done     |
|  1 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ?  | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 256]> self = ?                                                            | Done     |
|  1 | Tensor<[1, 256, 1024]> self = ?                                                               | Done     |
|  2 | Tensor<[1, 256, 16, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[1, 256]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format         | Done     |
### aten.div.Tensor
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor<> other = 8.0 | Done     |
### aten.embedding.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                               | Done     |
|  1 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int<> padding_idx = 0 | Done     |
|  2 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                             | Done     |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int]<> size = [1, 16, 256, 256] | Unknown  |
|  1 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int]<> size = [1, 16, 256, 64]   | Unknown  |
|  2 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int]<> size = [1, 16, 64, 256]   | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 256, 4096]> self = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor<> other = -3.3895313892515355e+38 | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-12 | Done     |
### aten.permute.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>number<> other = 1.0 | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 256]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  1 | Tensor<[1, 256]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1       | Unknown  |
|  2 | Tensor<[1, 512]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1       | Unknown  |
|  3 | Tensor<[1, 512]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 256      | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 2]> self = ?,<br>int<> split_size = 1,<br>int<> dim = -1 | Unknown  |
### aten.squeeze.dim
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 1]> self = ?,<br>int<> dim = -1 | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1024, 1024]> self = ? | Done     |
|  1 | Tensor<[1024, 4096]> self = ? | Done     |
|  2 | Tensor<[2, 1024]> self = ?    | Done     |
|  3 | Tensor<[4096, 1024]> self = ? | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 256]> self = ?,<br>int<> dim = 2 | Done     |
|  1 | Tensor<[1, 256]> self = ?,<br>int<> dim = 1    | Done     |
### aten.view.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 256, 256]> self = ?,<br>List[int]<> size = [16, 256, 256] | Unknown  |
|  1 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int]<> size = [16, 256, 64]   | Unknown  |
|  2 | Tensor<[1, 16, 64, 256]> self = ?,<br>List[int]<> size = [16, 64, 256]   | Unknown  |
|  3 | Tensor<[1, 256, 1024]> self = ?,<br>List[int]<> size = [1, 256, 16, 64]  | Unknown  |
|  4 | Tensor<[1, 256, 1024]> self = ?,<br>List[int]<> size = [256, 1024]       | Unknown  |
|  5 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int]<> size = [1, 256, 1024]  | Unknown  |
|  6 | Tensor<[1, 256, 4096]> self = ?,<br>List[int]<> size = [256, 4096]       | Unknown  |
|  7 | Tensor<[16, 256, 256]> self = ?,<br>List[int]<> size = [1, 16, 256, 256] | Unknown  |
|  8 | Tensor<[16, 256, 64]> self = ?,<br>List[int]<> size = [1, 16, 256, 64]   | Unknown  |
|  9 | Tensor<[256, 1024]> self = ?,<br>List[int]<> size = [1, 256, 1024]       | Unknown  |
| 10 | Tensor<[256, 2]> self = ?,<br>List[int]<> size = [1, 256, 2]             | Unknown  |
| 11 | Tensor<[256, 4096]> self = ?,<br>List[int]<> size = [1, 256, 4096]       | Unknown  |

