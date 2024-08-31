# High Level Operations Status
|    | Operations                           |   Input Variations |
|---:|:-------------------------------------|-------------------:|
|  0 | aten._to_copy.default                |                  1 |
|  1 | aten._unsafe_index.Tensor            |                  3 |
|  2 | aten._unsafe_view.default            |                 15 |
|  3 | aten.add.Tensor                      |                  3 |
|  4 | aten.arange.default                  |                  1 |
|  5 | aten.arange.start                    |                  1 |
|  6 | aten.cat.default                     |                  2 |
|  7 | aten.ceil.default                    |                  1 |
|  8 | aten.clamp.default                   |                  5 |
|  9 | aten.clone.default                   |                  1 |
| 10 | aten.convolution.default             |                  8 |
| 11 | aten.div.Tensor                      |                  2 |
| 12 | aten.empty.memory_format             |                  1 |
| 13 | aten.exp.default                     |                  1 |
| 14 | aten.expand.default                  |                  5 |
| 15 | aten.fill.Scalar                     |                  1 |
| 16 | aten.lift_fresh_copy.default         |                  1 |
| 17 | aten.max_pool2d_with_indices.default |                  1 |
| 18 | aten.mul.Tensor                      |                  4 |
| 19 | aten.new_full.default                |                  1 |
| 20 | aten.permute.default                 |                  1 |
| 21 | aten.relu.default                    |                  1 |
| 22 | aten.rsqrt.default                   |                  1 |
| 23 | aten.rsub.Scalar                     |                  1 |
| 24 | aten.select.int                      |                  2 |
| 25 | aten.slice.Tensor                    |                  2 |
| 26 | aten.split_with_sizes.default        |                  2 |
| 27 | aten.stack.default                   |                  1 |
| 28 | aten.sub.Tensor                      |                  2 |
| 29 | aten.unbind.int                      |                  1 |
| 30 | aten.unsqueeze.default               |                  4 |
| 31 | aten.view.default                    |                 17 |
***
### aten._to_copy.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[800]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 25, 34]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_8, _to_copy_5] | Unknown  |
|  1 | Tensor<[1, 256, 50, 68]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_9, _to_copy_7] | Unknown  |
|  2 | Tensor<[1, 3, 480, 640]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_6, _to_copy_2] | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 136, 9, 4]> self = ?,<br>List[int] size = [1, 122400, 4]   | Unknown  |
|  1 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>List[int] size = [1, 122400, 91] | Unknown  |
|  2 | Tensor<[1, 13, 17, 9, 4]> self = ?,<br>List[int] size = [1, 1989, 4]       | Unknown  |
|  3 | Tensor<[1, 13, 17, 9, 91]> self = ?,<br>List[int] size = [1, 1989, 91]     | Unknown  |
|  4 | Tensor<[1, 25, 34, 9, 4]> self = ?,<br>List[int] size = [1, 7650, 4]       | Unknown  |
|  5 | Tensor<[1, 25, 34, 9, 91]> self = ?,<br>List[int] size = [1, 7650, 91]     | Unknown  |
|  6 | Tensor<[1, 50, 68, 9, 4]> self = ?,<br>List[int] size = [1, 30600, 4]      | Unknown  |
|  7 | Tensor<[1, 50, 68, 9, 91]> self = ?,<br>List[int] size = [1, 30600, 91]    | Unknown  |
|  8 | Tensor<[1, 7, 9, 9, 4]> self = ?,<br>List[int] size = [1, 567, 4]          | Unknown  |
|  9 | Tensor<[1, 7, 9, 9, 91]> self = ?,<br>List[int] size = [1, 567, 91]        | Unknown  |
| 10 | Tensor<[100, 136]> self = ?,<br>List[int] size = [13600]                   | Unknown  |
| 11 | Tensor<[13, 17]> self = ?,<br>List[int] size = [221]                       | Unknown  |
| 12 | Tensor<[25, 34]> self = ?,<br>List[int] size = [850]                       | Unknown  |
| 13 | Tensor<[50, 68]> self = ?,<br>List[int] size = [3400]                      | Unknown  |
| 14 | Tensor<[7, 9]> self = ?,<br>List[int] size = [63]                          | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ? | Unknown  |
|  1 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                      | Unknown  |
|  2 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                              | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 800,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 136,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [_unsafe_view, _unsafe_view_1, _unsafe_view_2, _unsafe_view_3, _unsafe_view_4],<br>int dim = 1 | Unknown  |
|  1 | List[Tensor] tensors = [view_226, view_231, view_236, view_241, view_246]                                             | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[800]> self = ?  | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                | Status   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.135166556742356 | Unknown  |
|  1 | Tensor<[0, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1066                 | Unknown  |
|  2 | Tensor<[1066]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 639               | Unknown  |
|  3 | Tensor<[800]> self = ?,<br>Optional[number] min = 0.0                                                | Unknown  |
|  4 | Tensor<[800]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 479                | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 100, 136, 9, 91]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 200, 272]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  1 | Tensor<[1, 2048, 25, 34]> input = ?,<br>Tensor<[256, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  2 | Tensor<[1, 256, 13, 17]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  3 | Tensor<[1, 256, 200, 272]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  4 | Tensor<[1, 256, 25, 34]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  5 | Tensor<[1, 3, 800, 1088]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Unknown  |
|  6 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  |
|  7 | Tensor<[1, 64, 200, 272]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor other = 1.0                 | Unknown  |
|  1 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
### aten.empty.memory_format
|    | ATen Input Variations                                                                                                             | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.exp.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                     | Status   |
|---:|:----------------------------------------------------------|:---------|
|  0 | Tensor<[100, 1]> self = ?,<br>List[int] size = [100, 136] | Unknown  |
|  1 | Tensor<[13, 1]> self = ?,<br>List[int] size = [13, 17]    | Unknown  |
|  2 | Tensor<[25, 1]> self = ?,<br>List[int] size = [25, 34]    | Unknown  |
|  3 | Tensor<[50, 1]> self = ?,<br>List[int] size = [50, 68]    | Unknown  |
|  4 | Tensor<[7, 1]> self = ?,<br>List[int] size = [7, 9]       | Unknown  |
### aten.fill.Scalar
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>number value = 8 | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 400, 544]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ? | Unknown  |
|  1 | Tensor<[1066]> self = ?,<br>Tensor other = 0.600375234521576      | Unknown  |
|  2 | Tensor<[50]> self = ?,<br>Tensor other = 0.5                      | Unknown  |
|  3 | Tensor<[800]> self = ?,<br>Tensor other = 0.6                     | Unknown  |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 800, 1066]> self = ?,<br>List[int] size = [1, 3, 800, 1088],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 9, 91, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 64, 400, 544]> self = ? | Unknown  |
### aten.rsqrt.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 64, 1, 1]> self = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[800, 1]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 2           | Unknown  |
|  1 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 4 | Unknown  |
|  1 | Tensor<[3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
### aten.split_with_sizes.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 163206, 91]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1 | Unknown  |
|  1 | Tensor<[163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567]                     | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [_unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11],<br>int dim = 1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
|  1 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                  | Unknown  |
### aten.unbind.int
|    | ATen Input Variations                   | Status   |
|---:|:----------------------------------------|:---------|
|  0 | Tensor<[0, 4]> self = ?,<br>int dim = 1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Unknown  |
|  1 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0 | Unknown  |
|  2 | Tensor<[3]> self = ?,<br>int dim = 1           | Unknown  |
|  3 | Tensor<[50]> self = ?,<br>int dim = -1         | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1, 4]> self = ?,<br>List[int] size = [0, 4]                         | Unknown  |
|  1 | Tensor<[1, 36, 100, 136]> self = ?,<br>List[int] size = [1, -1, 4, 100, 136]   | Unknown  |
|  2 | Tensor<[1, 36, 13, 17]> self = ?,<br>List[int] size = [1, -1, 4, 13, 17]       | Unknown  |
|  3 | Tensor<[1, 36, 25, 34]> self = ?,<br>List[int] size = [1, -1, 4, 25, 34]       | Unknown  |
|  4 | Tensor<[1, 36, 50, 68]> self = ?,<br>List[int] size = [1, -1, 4, 50, 68]       | Unknown  |
|  5 | Tensor<[1, 36, 7, 9]> self = ?,<br>List[int] size = [1, -1, 4, 7, 9]           | Unknown  |
|  6 | Tensor<[1, 819, 100, 136]> self = ?,<br>List[int] size = [1, -1, 91, 100, 136] | Unknown  |
|  7 | Tensor<[1, 819, 13, 17]> self = ?,<br>List[int] size = [1, -1, 91, 13, 17]     | Unknown  |
|  8 | Tensor<[1, 819, 25, 34]> self = ?,<br>List[int] size = [1, -1, 91, 25, 34]     | Unknown  |
|  9 | Tensor<[1, 819, 50, 68]> self = ?,<br>List[int] size = [1, -1, 91, 50, 68]     | Unknown  |
| 10 | Tensor<[1, 819, 7, 9]> self = ?,<br>List[int] size = [1, -1, 91, 7, 9]         | Unknown  |
| 11 | Tensor<[100]> self = ?,<br>List[int] size = [-1, 1]                            | Unknown  |
| 12 | Tensor<[13600, 4]> self = ?,<br>List[int] size = [-1, 1, 4]                    | Unknown  |
| 13 | Tensor<[13600, 9, 4]> self = ?,<br>List[int] size = [-1, 4]                    | Unknown  |
| 14 | Tensor<[136]> self = ?,<br>List[int] size = [1, -1]                            | Unknown  |
| 15 | Tensor<[64]> self = ?,<br>List[int] size = [1, -1, 1, 1]                       | Unknown  |
| 16 | Tensor<[9, 4]> self = ?,<br>List[int] size = [1, -1, 4]                        | Unknown  |

