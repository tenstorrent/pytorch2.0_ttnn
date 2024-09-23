# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  1 |           1 |
|  1 | aten._to_copy.default          |                  2 |           0 |
|  2 | aten._unsafe_index.Tensor      |                  1 |           0 |
|  3 | aten.add.Tensor                |                 12 |          12 |
|  4 | aten.addmm.default             |                  6 |           6 |
|  5 | aten.arange.default            |                  4 |           0 |
|  6 | aten.bmm.default               |                  2 |           2 |
|  7 | aten.cat.default               |                  1 |           0 |
|  8 | aten.clamp.default             |                  2 |           2 |
|  9 | aten.clone.default             |                  4 |           4 |
| 10 | aten.convolution.default       |                  1 |           0 |
| 11 | aten.div.Tensor                |                  1 |           0 |
| 12 | aten.expand.default            |                  5 |           0 |
| 13 | aten.floor.default             |                  2 |           0 |
| 14 | aten.gelu.default              |                  1 |           1 |
| 15 | aten.mul.Tensor                |                 10 |          10 |
| 16 | aten.native_layer_norm.default |                  1 |           1 |
| 17 | aten.permute.default           |                  2 |           2 |
| 18 | aten.relu.default              |                  1 |           1 |
| 19 | aten.rsub.Scalar               |                  4 |           0 |
| 20 | aten.select.int                |                  1 |           0 |
| 21 | aten.sigmoid.default           |                  1 |           1 |
| 22 | aten.slice.Tensor              |                  9 |           0 |
| 23 | aten.sub.Tensor                |                 12 |          12 |
| 24 | aten.t.default                 |                  5 |           5 |
| 25 | aten.transpose.int             |                  3 |           3 |
| 26 | aten.unsqueeze.default         |                  1 |           1 |
| 27 | aten.view.default              |                 21 |           9 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
|  1 | Tensor<[1, 1, 32, 1]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 192, 50, 83]> self = ?,<br>List[Optional[Tensor]]<> indices = ['torch.Size([1, 1, 1, 1])', 'torch.Size([1, 192, 1, 1])', 'torch.Size([1, 1, 32, 1])', 'torch.Size([1, 1, 1, 42])'] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = -6.0                 | Done     |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 0.5                  | Done     |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 1                    | Done     |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 1.0                  | Done     |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 2                    | Done     |
|  5 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = -6.0                 | Done     |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 0.5                  | Done     |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 1                    | Done     |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 1.0                  | Done     |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 2                    | Done     |
| 10 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?     | Done     |
| 11 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ? | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[192]> self = ?,<br>Tensor<[100, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ?  | Done     |
|  1 | Tensor<[192]> self = ?,<br>Tensor<[1445, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ? | Done     |
|  2 | Tensor<[192]> self = ?,<br>Tensor<[1445, 768]> mat1 = ?,<br>Tensor<[768, 192]> mat2 = ? | Done     |
|  3 | Tensor<[4]> self = ?,<br>Tensor<[100, 192]> mat1 = ?,<br>Tensor<[192, 4]> mat2 = ?      | Done     |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[1445, 192]> mat1 = ?,<br>Tensor<[192, 768]> mat2 = ? | Done     |
|  5 | Tensor<[92]> self = ?,<br>Tensor<[100, 192]> mat1 = ?,<br>Tensor<[192, 92]> mat2 = ?    | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 1,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False   | Unknown  |
|  1 | number<> end = 192,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
|  2 | number<> end = 32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  3 | number<> end = 42,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False  | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1445, 1445]> self = ?,<br>Tensor<[3, 1445, 64]> mat2 = ? | Done     |
|  1 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ?   | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 1, 192])', 'torch.Size([1, 1344, 192])', 'torch.Size([1, 100, 192])'],<br>int<> dim = 1 | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[number]<> min = 0,<br>Optional[number]<> max = 82 | Done     |
|  1 | Tensor<[1, 1, 32, 1]> self = ?,<br>Optional[number]<> min = 0,<br>Optional[number]<> max = 49 | Done     |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 192]> self = ?                                                               | Done     |
|  1 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  2 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int]<> memory_format = torch.channels_last     | Done     |
|  3 | Tensor<[1, 3, 1445, 1445]> self = ?                                                           | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 512, 672]> input = ?,<br>Tensor<[192, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>List[int]<> stride = [16, 16],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor<> other = 8.0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 192]> self = ?,<br>List[int]<> size = [1, -1, -1]               | Unknown  |
|  1 | Tensor<[1, 100, 192]> self = ?,<br>List[int]<> size = [1, -1, -1]             | Unknown  |
|  2 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int]<> size = [1, 3, 1445, 1445] | Unknown  |
|  3 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int]<> size = [1, 3, 1445, 64]     | Unknown  |
|  4 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int]<> size = [1, 3, 64, 1445]     | Unknown  |
### aten.floor.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ? | Unknown  |
|  1 | Tensor<[1, 1, 32, 1]> self = ? | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 1445, 768]> self = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = -0.75              | Done     |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 1.25               | Done     |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 1.9761904761904763 | Done     |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?     | Done     |
|  4 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = -0.75              | Done     |
|  5 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 1.25               | Done     |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 1.5625             | Done     |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?     | Done     |
|  8 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?  | Done     |
|  9 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?  | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 192]> input = ?,<br>List[int]<> normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float<> eps = 1e-12 | Done     |
### aten.permute.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
|  1 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int]<> dims = [0, 2, 1, 3] | Done     |
### aten.relu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 100, 192]> self = ? | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>number<> other = 1.0 | Unknown  |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>number<> other = 2.0 | Unknown  |
|  2 | Tensor<[1, 1, 32, 1]> self = ?,<br>number<> other = 1.0 | Unknown  |
|  3 | Tensor<[1, 1, 32, 1]> self = ?,<br>number<> other = 2.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 4251, 192]> self = ?,<br>int<> dim = 1,<br>int<> index = 0 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1, 100, 4]> self = ? | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 192]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1     | Unknown  |
|  1 | Tensor<[1, 1445, 192]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1    | Unknown  |
|  2 | Tensor<[1, 1445, 192]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = -100,<br>Optional[int]<> end = -1 | Unknown  |
|  3 | Tensor<[1, 192]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1          | Unknown  |
|  4 | Tensor<[1, 192]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1          | Unknown  |
|  5 | Tensor<[1, 4150, 192]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1    | Unknown  |
|  6 | Tensor<[1, 4251, 192]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1    | Unknown  |
|  7 | Tensor<[1, 4251, 192]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = -100,<br>Optional[int]<> end = -1 | Unknown  |
|  8 | Tensor<[1, 4251, 192]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 1,<br>Optional[int]<> end = -100  | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = -3.0           | Done     |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = -3.75          | Done     |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 0.5            | Done     |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 1              | Done     |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 2.25           | Done     |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ? | Done     |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = -3.0           | Done     |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = -3.75          | Done     |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 0.5            | Done     |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 1              | Done     |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 2.25           | Done     |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ? | Done     |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[192, 192]> self = ? | Done     |
|  1 | Tensor<[192, 768]> self = ? | Done     |
|  2 | Tensor<[4, 192]> self = ?   | Done     |
|  3 | Tensor<[768, 192]> self = ? | Done     |
|  4 | Tensor<[92, 192]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 192, 1344]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2     | Done     |
|  1 | Tensor<[1, 3, 1445, 64]> self = ?,<br>int<> dim0 = -1,<br>int<> dim1 = -2 | Done     |
|  2 | Tensor<[1, 4150, 192]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2     | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 192]> self = ?,<br>int<> dim = 1 | Done     |
### aten.view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 192]> self = ?,<br>List[int]<> size = [100, 192]           | Done     |
|  1 | Tensor<[1, 1445, 192]> self = ?,<br>List[int]<> size = [1, 1445, 3, 64]    | Unknown  |
|  2 | Tensor<[1, 1445, 192]> self = ?,<br>List[int]<> size = [1445, 192]         | Done     |
|  3 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int]<> size = [1, 1445, 192]    | Unknown  |
|  4 | Tensor<[1, 1445, 768]> self = ?,<br>List[int]<> size = [1445, 768]         | Done     |
|  5 | Tensor<[1, 192, 32, 42]> self = ?,<br>List[int]<> size = [1, 192, 1344]    | Unknown  |
|  6 | Tensor<[1, 192, 4150]> self = ?,<br>List[int]<> size = [1, 192, 50, 83]    | Unknown  |
|  7 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int]<> size = [3, 1445, 1445] | Unknown  |
|  8 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int]<> size = [3, 1445, 64]     | Done     |
|  9 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int]<> size = [3, 64, 1445]     | Unknown  |
| 10 | Tensor<[100, 192]> self = ?,<br>List[int]<> size = [1, 100, 192]           | Done     |
| 11 | Tensor<[100, 4]> self = ?,<br>List[int]<> size = [1, 100, 4]               | Done     |
| 12 | Tensor<[100, 92]> self = ?,<br>List[int]<> size = [1, 100, 92]             | Unknown  |
| 13 | Tensor<[1445, 192]> self = ?,<br>List[int]<> size = [1, 1445, 192]         | Done     |
| 14 | Tensor<[1445, 768]> self = ?,<br>List[int]<> size = [1, 1445, 768]         | Done     |
| 15 | Tensor<[192]> self = ?,<br>List[int]<> size = [1, 192, 1, 1]               | Unknown  |
| 16 | Tensor<[1]> self = ?,<br>List[int]<> size = [1, 1, 1, 1]                   | Unknown  |
| 17 | Tensor<[3, 1445, 1445]> self = ?,<br>List[int]<> size = [1, 3, 1445, 1445] | Unknown  |
| 18 | Tensor<[3, 1445, 64]> self = ?,<br>List[int]<> size = [1, 3, 1445, 64]     | Done     |
| 19 | Tensor<[32]> self = ?,<br>List[int]<> size = [1, 1, 32, 1]                 | Unknown  |
| 20 | Tensor<[42]> self = ?,<br>List[int]<> size = [1, 1, 1, 42]                 | Unknown  |

