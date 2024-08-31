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
|  0 | Tensor<[1, 32, 150, 150]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Unknown  |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 192, 75, 75]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0 | Unknown  |
|  1 | Tensor<[1, 3, 300, 300]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0 | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                            | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Tensor<[1392, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1392 | Unknown  |
|  1 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Tensor<[1392, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1392 | Unknown  |
|  2 | Tensor<[1, 144, 151, 151]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144  | Unknown  |
|  3 | Tensor<[1, 192, 75, 75]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192    | Unknown  |
|  4 | Tensor<[1, 192, 79, 79]> input = ?,<br>Tensor<[192, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192    | Unknown  |
|  5 | Tensor<[1, 288, 38, 38]> input = ?,<br>Tensor<[288, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288    | Unknown  |
|  6 | Tensor<[1, 288, 39, 39]> input = ?,<br>Tensor<[288, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288    | Unknown  |
|  7 | Tensor<[1, 3, 301, 301]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  8 | Tensor<[1, 32, 150, 150]> input = ?,<br>Tensor<[24, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  |
|  9 | Tensor<[1, 32, 150, 150]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32     | Unknown  |
| 10 | Tensor<[1, 576, 19, 19]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576    | Unknown  |
| 11 | Tensor<[1, 576, 19, 19]> input = ?,<br>Tensor<[576, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576    | Unknown  |
| 12 | Tensor<[1, 816, 19, 19]> input = ?,<br>Tensor<[816, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 816    | Unknown  |
| 13 | Tensor<[1, 816, 23, 23]> input = ?,<br>Tensor<[816, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 816    | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 150, 150]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1280]> self = ? | Unknown  |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280] | Unknown  |

