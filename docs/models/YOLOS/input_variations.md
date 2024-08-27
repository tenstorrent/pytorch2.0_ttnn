# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._to_copy.default          |                  1 |
|  2 | aten._unsafe_index.Tensor      |                  1 |
|  3 | aten.add.Tensor                |                  3 |
|  4 | aten.addmm.default             |                  1 |
|  5 | aten.arange.default            |                  1 |
|  6 | aten.bmm.default               |                  1 |
|  7 | aten.cat.default               |                  1 |
|  8 | aten.clamp.default             |                  2 |
|  9 | aten.clone.default             |                  3 |
| 10 | aten.convolution.default       |                  1 |
| 11 | aten.div.Tensor                |                  1 |
| 12 | aten.expand.default            |                  4 |
| 13 | aten.floor.default             |                  1 |
| 14 | aten.gelu.default              |                  1 |
| 15 | aten.mul.Tensor                |                  3 |
| 16 | aten.native_layer_norm.default |                  1 |
| 17 | aten.permute.default           |                  1 |
| 18 | aten.relu.default              |                  1 |
| 19 | aten.rsub.Scalar               |                  2 |
| 20 | aten.select.int                |                  1 |
| 21 | aten.sigmoid.default           |                  1 |
| 22 | aten.slice.Tensor              |                  4 |
| 23 | aten.sub.Tensor                |                  3 |
| 24 | aten.t.default                 |                  1 |
| 25 | aten.transpose.int             |                  2 |
| 26 | aten.unsqueeze.default         |                  1 |
| 27 | aten.view.default              |                 19 |
***
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 192, 50, 83]> self = ?,<br>List[Optional[Tensor]] indices = [view_2, view_3, clamp, clamp_1] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                      | Unknown  |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                    | Unknown  |
|  2 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[192]> self = ?,<br>Tensor<[1445, 192]> mat1 = ?,<br>Tensor<[192, 192]> mat2 = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [expand, transpose, expand_1],<br>int dim = 1 | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 1]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 49 | Unknown  |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 82 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 192]> self = ?                                                             | Unknown  |
|  1 | Tensor<[1, 1445, 3, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  2 | Tensor<[1, 192, 32, 42]> self = ?,<br>Optional[int] memory_format = torch.channels_last     | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 512, 672]> input = ?,<br>Tensor<[192, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]     | Unknown  |
|  1 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [1, 3, 64, 1445]     | Unknown  |
|  2 | Tensor<[1, 1, 192]> self = ?,<br>List[int] size = [1, -1, -1]               | Unknown  |
|  3 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445] | Unknown  |
### aten.floor.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ? | Unknown  |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 1445, 768]> self = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?   | Unknown  |
|  1 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.5625             | Unknown  |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.9761904761904763 | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 192]> input = ?,<br>List[int] normalized_shape = [192],<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>float eps = 1e-12 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.relu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 100, 192]> self = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0 | Unknown  |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>int index = 0 | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[1, 100, 4]> self = ? | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1445, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = -100,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 192]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1          | Unknown  |
|  2 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1    | Unknown  |
|  3 | Tensor<[1, 100, 192]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                | Unknown  |
|  1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5              | Unknown  |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[192, 192]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 192, 1344]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  |
|  1 | Tensor<[1, 3, 1445, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[1, 192]> self = ?,<br>int dim = 1 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[100, 192]> self = ?,<br>List[int] size = [1, 100, 192]           | Unknown  |
|  1 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] size = [3, 1445, 64]     | Unknown  |
|  2 | Tensor<[100, 4]> self = ?,<br>List[int] size = [1, 100, 4]               | Unknown  |
|  3 | Tensor<[1, 1445, 192]> self = ?,<br>List[int] size = [1445, 192]         | Unknown  |
|  4 | Tensor<[1445, 192]> self = ?,<br>List[int] size = [1, 1445, 192]         | Unknown  |
|  5 | Tensor<[1, 192, 32, 42]> self = ?,<br>List[int] size = [1, 192, 1344]    | Unknown  |
|  6 | Tensor<[1, 1445, 768]> self = ?,<br>List[int] size = [1445, 768]         | Unknown  |
|  7 | Tensor<[32]> self = ?,<br>List[int] size = [1, 1, 32, 1]                 | Unknown  |
|  8 | Tensor<[100, 92]> self = ?,<br>List[int] size = [1, 100, 92]             | Unknown  |
|  9 | Tensor<[3, 1445, 64]> self = ?,<br>List[int] size = [1, 3, 1445, 64]     | Unknown  |
| 10 | Tensor<[1445, 768]> self = ?,<br>List[int] size = [1, 1445, 768]         | Unknown  |
| 11 | Tensor<[1]> self = ?,<br>List[int] size = [1, 1, 1, 1]                   | Unknown  |
| 12 | Tensor<[42]> self = ?,<br>List[int] size = [1, 1, 1, 42]                 | Unknown  |
| 13 | Tensor<[3, 1445, 1445]> self = ?,<br>List[int] size = [1, 3, 1445, 1445] | Unknown  |
| 14 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>List[int] size = [3, 1445, 1445] | Unknown  |
| 15 | Tensor<[1, 100, 192]> self = ?,<br>List[int] size = [100, 192]           | Unknown  |
| 16 | Tensor<[1, 192, 4150]> self = ?,<br>List[int] size = [1, 192, 50, 83]    | Unknown  |
| 17 | Tensor<[192]> self = ?,<br>List[int] size = [1, 192, 1, 1]               | Unknown  |
| 18 | Tensor<[1, 3, 64, 1445]> self = ?,<br>List[int] size = [3, 64, 1445]     | Unknown  |

