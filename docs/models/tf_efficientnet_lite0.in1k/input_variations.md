# High Level Operations Status
|    | Operations                                        |   Input Variations |
|---:|:--------------------------------------------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |
|  1 | aten.add.Tensor                                   |                  1 |
|  2 | aten.addmm.default                                |                  1 |
|  3 | aten.constant_pad_nd.default                      |                  2 |
|  4 | aten.convolution.default                          |                 14 |
|  5 | aten.hardtanh.default                             |                  1 |
|  6 | aten.mean.dim                                     |                  1 |
|  7 | aten.t.default                                    |                  1 |
|  8 | aten.view.default                                 |                  1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Unknown  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 144, 56, 56]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0 | Unknown  |
|  1 | Tensor<[1, 3, 224, 224]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0 | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1152, 7, 7]> input = ?,<br>Tensor<[1152, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1152 | Unknown  |
|  1 | Tensor<[1, 1152, 7, 7]> input = ?,<br>Tensor<[1152, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1152 | Unknown  |
|  2 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144  | Unknown  |
|  3 | Tensor<[1, 144, 59, 59]> input = ?,<br>Tensor<[144, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144  | Unknown  |
|  4 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240  | Unknown  |
|  5 | Tensor<[1, 240, 29, 29]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240  | Unknown  |
|  6 | Tensor<[1, 3, 225, 225]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  7 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[16, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  8 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32   | Unknown  |
|  9 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480  | Unknown  |
| 10 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[480, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480  | Unknown  |
| 11 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672  | Unknown  |
| 12 | Tensor<[1, 672, 17, 17]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672  | Unknown  |
| 13 | Tensor<[1, 96, 113, 113]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96   | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 112, 112]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1280]> self = ? | Unknown  |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280] | Unknown  |

