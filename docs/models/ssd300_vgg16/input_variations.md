# High Level Operations Status
|    | Operations                           |   Input Variations |
|---:|:-------------------------------------|-------------------:|
|  0 | aten._to_copy.default                |                  2 |
|  1 | aten._unsafe_index.Tensor            |                  1 |
|  2 | aten._unsafe_view.default            |                 15 |
|  3 | aten.add.Tensor                      |                  2 |
|  4 | aten.arange.default                  |                  1 |
|  5 | aten.arange.start                    |                  1 |
|  6 | aten.cat.default                     |                  2 |
|  7 | aten.ceil.default                    |                  1 |
|  8 | aten.clamp.default                   |                  5 |
|  9 | aten.clamp_min.default               |                  1 |
| 10 | aten.clone.default                   |                  1 |
| 11 | aten.convolution.default             |                  4 |
| 12 | aten.div.Tensor                      |                  8 |
| 13 | aten.exp.default                     |                  1 |
| 14 | aten.expand.default                  |                  7 |
| 15 | aten.lift_fresh_copy.default         |                  1 |
| 16 | aten.linalg_vector_norm.default      |                  1 |
| 17 | aten.max.default                     |                  1 |
| 18 | aten.max_pool2d_with_indices.default |                  3 |
| 19 | aten.mul.Tensor                      |                  3 |
| 20 | aten.new_full.default                |                  1 |
| 21 | aten.permute.default                 |                  1 |
| 22 | aten.relu.default                    |                  1 |
| 23 | aten.repeat.default                  |                  2 |
| 24 | aten.rsub.Scalar                     |                  1 |
| 25 | aten.select.int                      |                  2 |
| 26 | aten.slice.Tensor                    |                  3 |
| 27 | aten.stack.default                   |                  1 |
| 28 | aten.sub.Tensor                      |                  2 |
| 29 | aten.unbind.int                      |                  1 |
| 30 | aten.unsqueeze.default               |                  3 |
| 31 | aten.view.default                    |                 20 |
***
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[25]> self = ?,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu | Unknown  |
|  1 | Tensor<[300]> self = ?,<br>Optional[int] dtype = torch.int64                                    | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_6, _to_copy_2] | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int] size = [1, 600, 4]    | Unknown  |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int] size = [1, 600, 91]  | Unknown  |
|  2 | Tensor<[1, 19, 19, 6, 4]> self = ?,<br>List[int] size = [1, 2166, 4]   | Unknown  |
|  3 | Tensor<[1, 19, 19, 6, 91]> self = ?,<br>List[int] size = [1, 2166, 91] | Unknown  |
|  4 | Tensor<[1, 3, 3, 4, 4]> self = ?,<br>List[int] size = [1, 36, 4]       | Unknown  |
|  5 | Tensor<[1, 3, 3, 4, 91]> self = ?,<br>List[int] size = [1, 36, 91]     | Unknown  |
|  6 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>List[int] size = [1, 5776, 4]   | Unknown  |
|  7 | Tensor<[1, 38, 38, 4, 91]> self = ?,<br>List[int] size = [1, 5776, 91] | Unknown  |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int] size = [1, 150, 4]      | Unknown  |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int] size = [1, 150, 91]    | Unknown  |
| 10 | Tensor<[10, 10]> self = ?,<br>List[int] size = [100]                   | Unknown  |
| 11 | Tensor<[19, 19]> self = ?,<br>List[int] size = [361]                   | Unknown  |
| 12 | Tensor<[3, 3]> self = ?,<br>List[int] size = [9]                       | Unknown  |
| 13 | Tensor<[38, 38]> self = ?,<br>List[int] size = [1444]                  | Unknown  |
| 14 | Tensor<[5, 5]> self = ?,<br>List[int] size = [25]                      | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ? | Unknown  |
|  1 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                            | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 300,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [_unsafe_view, _unsafe_view_1, _unsafe_view_2, _unsafe_view_3, _unsafe_view_4, view_7],<br>int dim = 1 | Unknown  |
|  1 | List[Tensor] tensors = [cat_2, cat_3, cat_4, cat_5, cat_6, cat_7]                                                             | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[300]> self = ?  | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[300]> self = ?,<br>Optional[number] min = 0.0                                                   | Unknown  |
|  1 | Tensor<[300]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 479                   | Unknown  |
|  2 | Tensor<[4, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                       | Unknown  |
|  3 | Tensor<[8732, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.135166556742356 | Unknown  |
|  4 | Tensor<[8732, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 300                  | Unknown  |
### aten.clamp_min.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 38, 38]> self = ?,<br>number min = 1e-12 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 38, 38, 4, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Tensor<[1024, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  1 | Tensor<[1, 256, 19, 19]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  2 | Tensor<[1, 3, 300, 300]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  3 | Tensor<[1, 512, 19, 19]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [6, 6],<br>List[int] dilation = [6, 6],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[10]> self = ?,<br>Tensor other = 9.375                 | Unknown  |
|  1 | Tensor<[19]> self = ?,<br>Tensor other = 18.75                 | Unknown  |
|  2 | Tensor<[1]> self = ?,<br>Tensor other = 1.0                    | Unknown  |
|  3 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
|  4 | Tensor<[38]> self = ?,<br>Tensor other = 37.5                  | Unknown  |
|  5 | Tensor<[3]> self = ?,<br>Tensor other = 3.0                    | Unknown  |
|  6 | Tensor<[5]> self = ?,<br>Tensor other = 4.6875                 | Unknown  |
|  7 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 10.0             | Unknown  |
### aten.exp.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[8732, 1]> self = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 38, 38]> self = ?,<br>List[int] size = [1, 512, 38, 38] | Unknown  |
|  1 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]                   | Unknown  |
|  2 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10]                | Unknown  |
|  3 | Tensor<[19, 1]> self = ?,<br>List[int] size = [19, 19]                | Unknown  |
|  4 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]                   | Unknown  |
|  5 | Tensor<[38, 1]> self = ?,<br>List[int] size = [38, 38]                | Unknown  |
|  6 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]                   | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512, 38, 38]> self = ?,<br>number ord = 2.0,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True | Unknown  |
### aten.max.default
|    | ATen Input Variations    | Status   |
|---:|:-------------------------|:---------|
|  0 | Tensor<[25, 4]> self = ? | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 75, 75]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True | Unknown  |
|  1 | Tensor<[1, 512, 19, 19]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1]                                                           | Unknown  |
|  2 | Tensor<[1, 64, 300, 300]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]                                                                                         | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ? | Unknown  |
|  1 | Tensor<[300]> self = ?,<br>Tensor other = 1.6                    | Unknown  |
|  2 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                | Unknown  |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 300, 300]> self = ?,<br>List[int] size = [1, 3, 300, 300],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 4, 4, 38, 38]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 64, 300, 300]> self = ? | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[4, 2]> self = ?,<br>List[int] repeats = [1444, 1] | Unknown  |
|  1 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [361, 1]  | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[300, 1]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
|  1 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 2        | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                              | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                        | Unknown  |
|  1 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 4 | Unknown  |
|  2 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                   | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [_unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11],<br>int dim = -1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
|  1 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                  | Unknown  |
### aten.unbind.int
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[12, 4]> self = ?,<br>int dim = 1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Unknown  |
|  1 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0 | Unknown  |
|  2 | Tensor<[3]> self = ?,<br>int dim = 1           | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 4, 4]> self = ?,<br>List[int] size = [1, -1, 4]           | Unknown  |
|  1 | Tensor<[1, 1, 1, 4, 91]> self = ?,<br>List[int] size = [1, -1, 91]         | Unknown  |
|  2 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]       | Unknown  |
|  3 | Tensor<[1, 16, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]       | Unknown  |
|  4 | Tensor<[1, 16, 38, 38]> self = ?,<br>List[int] size = [1, -1, 4, 38, 38]   | Unknown  |
|  5 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                          | Unknown  |
|  6 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]   | Unknown  |
|  7 | Tensor<[1, 24, 19, 19]> self = ?,<br>List[int] size = [1, -1, 4, 19, 19]   | Unknown  |
|  8 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]       | Unknown  |
|  9 | Tensor<[1, 364, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]     | Unknown  |
| 10 | Tensor<[1, 364, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]     | Unknown  |
| 11 | Tensor<[1, 364, 38, 38]> self = ?,<br>List[int] size = [1, -1, 91, 38, 38] | Unknown  |
| 12 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10] | Unknown  |
| 13 | Tensor<[1, 546, 19, 19]> self = ?,<br>List[int] size = [1, -1, 91, 19, 19] | Unknown  |
| 14 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]     | Unknown  |
| 15 | Tensor<[1444, 8]> self = ?,<br>List[int] size = [-1, 2]                    | Unknown  |
| 16 | Tensor<[19]> self = ?,<br>List[int] size = [1, -1]                         | Unknown  |
| 17 | Tensor<[38]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  |
| 18 | Tensor<[512]> self = ?,<br>List[int] size = [1, -1, 1, 1]                  | Unknown  |
| 19 | Tensor<[8732, 1, 4]> self = ?,<br>List[int] size = [8732, 4]               | Unknown  |

