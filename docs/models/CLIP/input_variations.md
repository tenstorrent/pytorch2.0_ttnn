# High Level Operations Status
|    | Operations                      |   Input Variations |   Converted |
|---:|:--------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default           |                  2 |           2 |
|  1 | aten._to_copy.default           |                  5 |           0 |
|  2 | aten._unsafe_view.default       |                  2 |           0 |
|  3 | aten.add.Tensor                 |                  4 |           4 |
|  4 | aten.addmm.default              |                  6 |           6 |
|  5 | aten.arange.default             |                  1 |           0 |
|  6 | aten.argmax.default             |                  1 |           0 |
|  7 | aten.bmm.default                |                  4 |           4 |
|  8 | aten.cat.default                |                  1 |           0 |
|  9 | aten.clone.default              |                  6 |           6 |
| 10 | aten.convolution.default        |                  1 |           0 |
| 11 | aten.div.Tensor                 |                  2 |           2 |
| 12 | aten.embedding.default          |                  3 |           3 |
| 13 | aten.exp.default                |                  1 |           1 |
| 14 | aten.expand.default             |                  3 |           2 |
| 15 | aten.full.default               |                  1 |           1 |
| 16 | aten.index.Tensor               |                  1 |           0 |
| 17 | aten.linalg_vector_norm.default |                  2 |           0 |
| 18 | aten.masked_fill.Scalar         |                  1 |           0 |
| 19 | aten.mm.default                 |                  3 |           3 |
| 20 | aten.mul.Tensor                 |                  7 |           7 |
| 21 | aten.native_layer_norm.default  |                  3 |           3 |
| 22 | aten.rsub.Scalar                |                  1 |           1 |
| 23 | aten.select.int                 |                  1 |           0 |
| 24 | aten.sigmoid.default            |                  2 |           2 |
| 25 | aten.slice.Tensor               |                  8 |           0 |
| 26 | aten.t.default                  |                  9 |           9 |
| 27 | aten.transpose.int              |                  7 |           7 |
| 28 | aten.unsqueeze.default          |                  4 |           4 |
| 29 | aten.view.default               |                 20 |           5 |
***
### aten._softmax.default
|    | ATen Input Variations                                                             | Status   |
|---:|:----------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
|  1 | Tensor<[16, 7, 7]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False   | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> self = ?,<br>Optional[int]<> dtype = torch.bfloat16                        | Unknown  |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int]<> dtype = torch.bfloat16                            | Unknown  |
|  2 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int]<> dtype = torch.bool                                | Unknown  |
|  3 | Tensor<[2, 7]> self = ?,<br>Optional[int]<> dtype = torch.int32,<br>Optional[Device]<> device = cpu | Unknown  |
|  4 | Tensor<[7, 7]> self = ?,<br>Optional[int]<> dtype = torch.bfloat16                                  | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int]<> size = [1, 50, 768] | Unknown  |
|  1 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int]<> size = [2, 7, 512]    | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ? | Done     |
|  1 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?   | Done     |
|  2 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?   | Done     |
|  3 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ? | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ? | Done     |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[14, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ? | Done     |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?   | Done     |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 2,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.argmax.default
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[2, 7]> self = ?,<br>Optional[int]<> dim = -1 | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ? | Done     |
|  1 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ? | Done     |
|  2 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?   | Done     |
|  3 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?    | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 1, 768])', 'torch.Size([1, 49, 768])'],<br>int<> dim = 1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  2 | Tensor<[12, 50, 50]> self = ?                                                                | Done     |
|  3 | Tensor<[16, 7, 7]> self = ?                                                                  | Done     |
|  4 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
|  5 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format   | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [32, 32],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ? | Done     |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ? | Done     |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ? | Done     |
|  1 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?   | Done     |
|  2 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?    | Done     |
### aten.exp.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[]> self = ?     | Done     |
### aten.expand.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int]<> size = [2, 1, 7, 7] | Unknown  |
|  1 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int]<> size = [2, 1, 7, 7] | Done     |
|  2 | Tensor<[768]> self = ?,<br>List[int]<> size = [1, 1, -1]          | Done     |
### aten.full.default
|    | ATen Input Variations                                                                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int]<> size = [7, 7],<br>number<> fill_value = -3.3895313892515355e+38,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
### aten.index.Tensor
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([2])', 'torch.Size([2])'] | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?,<br>number<> ord = 2,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
|  1 | Tensor<[2, 512]> self = ?,<br>number<> ord = 2,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number<> value = -3.3895313892515355e+38 | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ? | Done     |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?   | Done     |
|  2 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<> other = 1.702          | Done     |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Done     |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<> other = 0.125           | Done     |
|  3 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                   | Done     |
|  4 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<> other = 1.702           | Done     |
|  5 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Done     |
|  6 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<> other = 0.125            | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-05 | Done     |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int]<> normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float<> eps = 1e-05     | Done     |
|  2 | Tensor<[2, 7, 512]> input = ?,<br>List[int]<> normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float<> eps = 1e-05  | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>number<> other = 1.0 | Done     |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int<> dim = 1,<br>int<> index = 0 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 50, 3072]> self = ? | Done     |
|  1 | Tensor<[2, 7, 2048]> self = ?  | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  3 | Tensor<[1, 768]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1     | Unknown  |
|  4 | Tensor<[1, 77]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Unknown  |
|  5 | Tensor<[1, 77]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 7       | Unknown  |
|  6 | Tensor<[2, 1, 1, 7]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  7 | Tensor<[2, 7]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1       | Unknown  |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1, 512]> self = ?    | Done     |
|  1 | Tensor<[2, 1]> self = ?      | Done     |
|  2 | Tensor<[2048, 512]> self = ? | Done     |
|  3 | Tensor<[3072, 768]> self = ? | Done     |
|  4 | Tensor<[512, 2048]> self = ? | Done     |
|  5 | Tensor<[512, 512]> self = ?  | Done     |
|  6 | Tensor<[512, 768]> self = ?  | Done     |
|  7 | Tensor<[768, 3072]> self = ? | Done     |
|  8 | Tensor<[768, 768]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Done     |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Done     |
|  2 | Tensor<[1, 768, 49]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  3 | Tensor<[12, 50, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Done     |
|  4 | Tensor<[16, 7, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2     | Done     |
|  5 | Tensor<[2, 7, 8, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  6 | Tensor<[2, 8, 7, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 7]> self = ?,<br>int<> dim = 1 | Done     |
|  1 | Tensor<[2, 1, 7]> self = ?,<br>int<> dim = 2 | Done     |
|  2 | Tensor<[2, 7]> self = ?,<br>int<> dim = 1    | Done     |
|  3 | Tensor<[7, 7]> self = ?,<br>int<> dim = 0    | Done     |
### aten.view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int]<> size = [12, -1, 64] | Unknown  |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>List[int]<> size = [50, 3072]     | Done     |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>List[int]<> size = [1, -1, 12, 64] | Unknown  |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>List[int]<> size = [1, 50, 12, 64] | Unknown  |
|  4 | Tensor<[1, 50, 768]> self = ?,<br>List[int]<> size = [50, 768]       | Done     |
|  5 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int]<> size = [1, 768, 49]  | Unknown  |
|  6 | Tensor<[12, 50, 64]> self = ?,<br>List[int]<> size = [1, 12, 50, 64] | Done     |
|  7 | Tensor<[14, 2048]> self = ?,<br>List[int]<> size = [2, 7, 2048]      | Unknown  |
|  8 | Tensor<[14, 512]> self = ?,<br>List[int]<> size = [2, 7, 512]        | Unknown  |
|  9 | Tensor<[16, 7, 64]> self = ?,<br>List[int]<> size = [2, 8, 7, 64]    | Unknown  |
| 10 | Tensor<[16, 7, 7]> self = ?,<br>List[int]<> size = [2, 8, 7, 7]      | Unknown  |
| 11 | Tensor<[2, 7, 2048]> self = ?,<br>List[int]<> size = [14, 2048]      | Unknown  |
| 12 | Tensor<[2, 7, 512]> self = ?,<br>List[int]<> size = [14, 512]        | Unknown  |
| 13 | Tensor<[2, 7, 512]> self = ?,<br>List[int]<> size = [2, -1, 8, 64]   | Unknown  |
| 14 | Tensor<[2, 7, 512]> self = ?,<br>List[int]<> size = [2, 7, 8, 64]    | Unknown  |
| 15 | Tensor<[2, 7]> self = ?,<br>List[int]<> size = [-1, 7]               | Unknown  |
| 16 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int]<> size = [16, -1, 64]   | Unknown  |
| 17 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int]<> size = [16, 7, 7]      | Unknown  |
| 18 | Tensor<[50, 3072]> self = ?,<br>List[int]<> size = [1, 50, 3072]     | Done     |
| 19 | Tensor<[50, 768]> self = ?,<br>List[int]<> size = [1, 50, 768]       | Done     |

