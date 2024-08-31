# High Level Operations Status
|    | Operations                                        |   Input Variations |
|---:|:--------------------------------------------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |
|  1 | aten._to_copy.default                             |                  1 |
|  2 | aten._unsafe_index.Tensor                         |                  1 |
|  3 | aten._unsafe_view.default                         |                 15 |
|  4 | aten.add.Tensor                                   |                  2 |
|  5 | aten.arange.default                               |                  1 |
|  6 | aten.arange.start                                 |                  1 |
|  7 | aten.cat.default                                  |                  2 |
|  8 | aten.ceil.default                                 |                  1 |
|  9 | aten.clamp.default                                |                  5 |
| 10 | aten.clone.default                                |                  1 |
| 11 | aten.convolution.default                          |                 20 |
| 12 | aten.div.Tensor                                   |                  8 |
| 13 | aten.exp.default                                  |                  1 |
| 14 | aten.expand.default                               |                  6 |
| 15 | aten.hardsigmoid.default                          |                  1 |
| 16 | aten.hardswish.default                            |                  1 |
| 17 | aten.hardtanh.default                             |                  1 |
| 18 | aten.lift_fresh_copy.default                      |                  1 |
| 19 | aten.mean.dim                                     |                  1 |
| 20 | aten.mul.Tensor                                   |                  3 |
| 21 | aten.new_full.default                             |                  1 |
| 22 | aten.permute.default                              |                  1 |
| 23 | aten.relu.default                                 |                  1 |
| 24 | aten.repeat.default                               |                  1 |
| 25 | aten.rsub.Scalar                                  |                  1 |
| 26 | aten.select.int                                   |                  2 |
| 27 | aten.slice.Tensor                                 |                  3 |
| 28 | aten.stack.default                                |                  1 |
| 29 | aten.sub.Tensor                                   |                  2 |
| 30 | aten.unbind.int                                   |                  1 |
| 31 | aten.unsqueeze.default                            |                  3 |
| 32 | aten.view.default                                 |                 19 |
| 33 | aten.zeros_like.default                           |                  1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 160, 160]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[320]> self = ?,<br>Optional[int] dtype = torch.int64 | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, unsqueeze_6, _to_copy_2] | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 10, 6, 4]> self = ?,<br>List[int] size = [1, 600, 4]    | Unknown  |
|  1 | Tensor<[1, 10, 10, 6, 91]> self = ?,<br>List[int] size = [1, 600, 91]  | Unknown  |
|  2 | Tensor<[1, 2, 2, 6, 4]> self = ?,<br>List[int] size = [1, 24, 4]       | Unknown  |
|  3 | Tensor<[1, 2, 2, 6, 91]> self = ?,<br>List[int] size = [1, 24, 91]     | Unknown  |
|  4 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>List[int] size = [1, 2400, 4]   | Unknown  |
|  5 | Tensor<[1, 20, 20, 6, 91]> self = ?,<br>List[int] size = [1, 2400, 91] | Unknown  |
|  6 | Tensor<[1, 3, 3, 6, 4]> self = ?,<br>List[int] size = [1, 54, 4]       | Unknown  |
|  7 | Tensor<[1, 3, 3, 6, 91]> self = ?,<br>List[int] size = [1, 54, 91]     | Unknown  |
|  8 | Tensor<[1, 5, 5, 6, 4]> self = ?,<br>List[int] size = [1, 150, 4]      | Unknown  |
|  9 | Tensor<[1, 5, 5, 6, 91]> self = ?,<br>List[int] size = [1, 150, 91]    | Unknown  |
| 10 | Tensor<[10, 10]> self = ?,<br>List[int] size = [100]                   | Unknown  |
| 11 | Tensor<[2, 2]> self = ?,<br>List[int] size = [4]                       | Unknown  |
| 12 | Tensor<[20, 20]> self = ?,<br>List[int] size = [400]                   | Unknown  |
| 13 | Tensor<[3, 3]> self = ?,<br>List[int] size = [9]                       | Unknown  |
| 14 | Tensor<[5, 5]> self = ?,<br>List[int] size = [25]                      | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ? | Unknown  |
|  1 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                            | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 320,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 20,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [_unsafe_view, _unsafe_view_1, _unsafe_view_2, _unsafe_view_3, _unsafe_view_4, view_6],<br>int dim = 1 | Unknown  |
|  1 | List[Tensor] tensors = [cat_2, cat_3, cat_4, cat_5, cat_6, cat_7]                                                             | Unknown  |
### aten.ceil.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[320]> self = ?  | Unknown  |
### aten.clamp.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[320]> self = ?,<br>Optional[number] min = 0.0                                                   | Unknown  |
|  1 | Tensor<[320]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 319                   | Unknown  |
|  2 | Tensor<[3234, 1]> self = ?,<br>Optional[number] min = None,<br>Optional[number] max = 4.135166556742356 | Unknown  |
|  3 | Tensor<[3234, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 320                  | Unknown  |
|  4 | Tensor<[6, 2]> self = ?,<br>Optional[number] min = 0,<br>Optional[number] max = 1                       | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 20, 20, 6, 4]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 120, 40, 40]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120 | Unknown  |
|  1 | Tensor<[1, 128, 1, 1]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | Unknown  |
|  2 | Tensor<[1, 128, 5, 5]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128   | Unknown  |
|  3 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16  | Unknown  |
|  4 | Tensor<[1, 16, 160, 160]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Unknown  |
|  5 | Tensor<[1, 184, 20, 20]> input = ?,<br>Tensor<[184, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184 | Unknown  |
|  6 | Tensor<[1, 200, 20, 20]> input = ?,<br>Tensor<[200, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200 | Unknown  |
|  7 | Tensor<[1, 240, 40, 40]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240 | Unknown  |
|  8 | Tensor<[1, 256, 10, 10]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256 | Unknown  |
|  9 | Tensor<[1, 256, 3, 3]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256   | Unknown  |
| 10 | Tensor<[1, 3, 320, 320]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  |
| 11 | Tensor<[1, 480, 10, 10]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480 | Unknown  |
| 12 | Tensor<[1, 480, 20, 20]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480 | Unknown  |
| 13 | Tensor<[1, 512, 5, 5]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512   | Unknown  |
| 14 | Tensor<[1, 64, 160, 160]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64  | Unknown  |
| 15 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672 | Unknown  |
| 16 | Tensor<[1, 672, 20, 20]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672 | Unknown  |
| 17 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
| 18 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72    | Unknown  |
| 19 | Tensor<[1, 72, 80, 80]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72    | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[10]> self = ?,<br>Tensor other = 10                    | Unknown  |
|  1 | Tensor<[1]> self = ?,<br>Tensor other = 1                      | Unknown  |
|  2 | Tensor<[20]> self = ?,<br>Tensor other = 20                    | Unknown  |
|  3 | Tensor<[2]> self = ?,<br>Tensor other = 2                      | Unknown  |
|  4 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
|  5 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0             | Unknown  |
|  6 | Tensor<[3]> self = ?,<br>Tensor other = 3                      | Unknown  |
|  7 | Tensor<[5]> self = ?,<br>Tensor other = 5                      | Unknown  |
### aten.exp.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[3234, 1]> self = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>List[int] size = [1, 1]    | Unknown  |
|  1 | Tensor<[10, 1]> self = ?,<br>List[int] size = [10, 10] | Unknown  |
|  2 | Tensor<[2, 1]> self = ?,<br>List[int] size = [2, 2]    | Unknown  |
|  3 | Tensor<[20, 1]> self = ?,<br>List[int] size = [20, 20] | Unknown  |
|  4 | Tensor<[3, 1]> self = ?,<br>List[int] size = [3, 3]    | Unknown  |
|  5 | Tensor<[5, 1]> self = ?,<br>List[int] size = [5, 5]    | Unknown  |
### aten.hardsigmoid.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 72, 1, 1]> self = ? | Unknown  |
### aten.hardswish.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 16, 160, 160]> self = ? | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 72, 40, 40]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ? | Unknown  |
|  1 | Tensor<[320]> self = ?,<br>Tensor other = 1.0                    | Unknown  |
|  2 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                | Unknown  |
### aten.new_full.default
|    | ATen Input Variations                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 320, 320]> self = ?,<br>List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2] | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 16, 160, 160]> self = ? | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[6, 2]> self = ?,<br>List[int] repeats = [400, 1] | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[320, 1]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0 | Unknown  |
|  1 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 2        | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                              | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 4 | Unknown  |
|  1 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 2                   | Unknown  |
|  2 | Tensor<[3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                        | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                                                                                                                                                                                                                | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [_unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11, _unsafe_view_10, _unsafe_view_11],<br>int dim = -1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Unknown  |
|  1 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                  | Unknown  |
### aten.unbind.int
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[300, 4]> self = ?,<br>int dim = 1 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[3, 1]> self = ?,<br>int dim = 2        | Unknown  |
|  1 | Tensor<[3, 320, 320]> self = ?,<br>int dim = 0 | Unknown  |
|  2 | Tensor<[3]> self = ?,<br>int dim = 1           | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 6, 4]> self = ?,<br>List[int] size = [1, -1, 4]           | Unknown  |
|  1 | Tensor<[1, 1, 1, 6, 91]> self = ?,<br>List[int] size = [1, -1, 91]         | Unknown  |
|  2 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1]                          | Unknown  |
|  3 | Tensor<[1, 24, 1, 1]> self = ?,<br>List[int] size = [1, -1, 4, 1, 1]       | Unknown  |
|  4 | Tensor<[1, 24, 10, 10]> self = ?,<br>List[int] size = [1, -1, 4, 10, 10]   | Unknown  |
|  5 | Tensor<[1, 24, 2, 2]> self = ?,<br>List[int] size = [1, -1, 4, 2, 2]       | Unknown  |
|  6 | Tensor<[1, 24, 20, 20]> self = ?,<br>List[int] size = [1, -1, 4, 20, 20]   | Unknown  |
|  7 | Tensor<[1, 24, 3, 3]> self = ?,<br>List[int] size = [1, -1, 4, 3, 3]       | Unknown  |
|  8 | Tensor<[1, 24, 5, 5]> self = ?,<br>List[int] size = [1, -1, 4, 5, 5]       | Unknown  |
|  9 | Tensor<[1, 546, 1, 1]> self = ?,<br>List[int] size = [1, -1, 91, 1, 1]     | Unknown  |
| 10 | Tensor<[1, 546, 10, 10]> self = ?,<br>List[int] size = [1, -1, 91, 10, 10] | Unknown  |
| 11 | Tensor<[1, 546, 2, 2]> self = ?,<br>List[int] size = [1, -1, 91, 2, 2]     | Unknown  |
| 12 | Tensor<[1, 546, 20, 20]> self = ?,<br>List[int] size = [1, -1, 91, 20, 20] | Unknown  |
| 13 | Tensor<[1, 546, 3, 3]> self = ?,<br>List[int] size = [1, -1, 91, 3, 3]     | Unknown  |
| 14 | Tensor<[1, 546, 5, 5]> self = ?,<br>List[int] size = [1, -1, 91, 5, 5]     | Unknown  |
| 15 | Tensor<[10]> self = ?,<br>List[int] size = [1, -1]                         | Unknown  |
| 16 | Tensor<[20]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  |
| 17 | Tensor<[3234, 1, 4]> self = ?,<br>List[int] size = [3234, 4]               | Unknown  |
| 18 | Tensor<[400, 12]> self = ?,<br>List[int] size = [-1, 2]                    | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[13685]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False | Unknown  |

