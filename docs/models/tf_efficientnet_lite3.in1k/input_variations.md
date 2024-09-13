# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 19 |           0 |
|  1 | aten.add.Tensor                                   |                  5 |           5 |
|  2 | aten.addmm.default                                |                  1 |           1 |
|  3 | aten.constant_pad_nd.default                      |                  5 |           0 |
|  4 | aten.convolution.default                          |                 32 |           0 |
|  5 | aten.hardtanh.default                             |                 12 |           0 |
|  6 | aten.mean.dim                                     |                  1 |           1 |
|  7 | aten.t.default                                    |                  1 |           1 |
|  8 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 10, 10]> input = ?, Optional[Tensor]<[1280]> weight = ?, Optional[Tensor]<[1280]> bias = ?, Tensor<[1280]> running_mean = ?, Tensor<[1280]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  1 | [Tensor<[1, 136, 19, 19]> input = ?, Optional[Tensor]<[136]> weight = ?, Optional[Tensor]<[136]> bias = ?, Tensor<[136]> running_mean = ?, Tensor<[136]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  2 | [Tensor<[1, 1392, 10, 10]> input = ?, Optional[Tensor]<[1392]> weight = ?, Optional[Tensor]<[1392]> bias = ?, Tensor<[1392]> running_mean = ?, Tensor<[1392]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  3 | [Tensor<[1, 144, 150, 150]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  4 | [Tensor<[1, 144, 75, 75]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  5 | [Tensor<[1, 192, 38, 38]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  6 | [Tensor<[1, 192, 75, 75]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  7 | [Tensor<[1, 232, 10, 10]> input = ?, Optional[Tensor]<[232]> weight = ?, Optional[Tensor]<[232]> bias = ?, Tensor<[232]> running_mean = ?, Tensor<[232]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  8 | [Tensor<[1, 24, 150, 150]> input = ?, Optional[Tensor]<[24]> weight = ?, Optional[Tensor]<[24]> bias = ?, Tensor<[24]> running_mean = ?, Tensor<[24]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
|  9 | [Tensor<[1, 288, 19, 19]> input = ?, Optional[Tensor]<[288]> weight = ?, Optional[Tensor]<[288]> bias = ?, Tensor<[288]> running_mean = ?, Tensor<[288]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 10 | [Tensor<[1, 288, 38, 38]> input = ?, Optional[Tensor]<[288]> weight = ?, Optional[Tensor]<[288]> bias = ?, Tensor<[288]> running_mean = ?, Tensor<[288]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 11 | [Tensor<[1, 32, 150, 150]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
| 12 | [Tensor<[1, 32, 75, 75]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]           | Unknown  |
| 13 | [Tensor<[1, 384, 10, 10]> input = ?, Optional[Tensor]<[384]> weight = ?, Optional[Tensor]<[384]> bias = ?, Tensor<[384]> running_mean = ?, Tensor<[384]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 14 | [Tensor<[1, 48, 38, 38]> input = ?, Optional[Tensor]<[48]> weight = ?, Optional[Tensor]<[48]> bias = ?, Tensor<[48]> running_mean = ?, Tensor<[48]> running_var = ?, float momentum = 0.1, float eps = 0.001]           | Unknown  |
| 15 | [Tensor<[1, 576, 19, 19]> input = ?, Optional[Tensor]<[576]> weight = ?, Optional[Tensor]<[576]> bias = ?, Tensor<[576]> running_mean = ?, Tensor<[576]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 16 | [Tensor<[1, 816, 10, 10]> input = ?, Optional[Tensor]<[816]> weight = ?, Optional[Tensor]<[816]> bias = ?, Tensor<[816]> running_mean = ?, Tensor<[816]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 17 | [Tensor<[1, 816, 19, 19]> input = ?, Optional[Tensor]<[816]> weight = ?, Optional[Tensor]<[816]> bias = ?, Tensor<[816]> running_mean = ?, Tensor<[816]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 18 | [Tensor<[1, 96, 19, 19]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 0.001]           | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 136, 19, 19]> self = ?, Tensor<[1, 136, 19, 19]> other = ?] | Done     |
|  1 | [Tensor<[1, 232, 10, 10]> self = ?, Tensor<[1, 232, 10, 10]> other = ?] | Done     |
|  2 | [Tensor<[1, 32, 75, 75]> self = ?, Tensor<[1, 32, 75, 75]> other = ?]   | Done     |
|  3 | [Tensor<[1, 48, 38, 38]> self = ?, Tensor<[1, 48, 38, 38]> other = ?]   | Done     |
|  4 | [Tensor<[1, 96, 19, 19]> self = ?, Tensor<[1, 96, 19, 19]> other = ?]   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1280]> mat1 = ?, Tensor<[1280, 1000]> mat2 = ?] | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 144, 150, 150]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0] | Unknown  |
|  1 | [Tensor<[1, 192, 75, 75]> self = ?, List[int] pad = [2, 2, 2, 2], number value = 0.0]   | Unknown  |
|  2 | [Tensor<[1, 288, 38, 38]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0]   | Unknown  |
|  3 | [Tensor<[1, 3, 300, 300]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0]   | Unknown  |
|  4 | [Tensor<[1, 816, 19, 19]> self = ?, List[int] pad = [2, 2, 2, 2], number value = 0.0]   | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 136, 19, 19]> input = ?, Tensor<[816, 136, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
|  1 | [Tensor<[1, 1392, 10, 10]> input = ?, Tensor<[1392, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1392] | Unknown  |
|  2 | [Tensor<[1, 1392, 10, 10]> input = ?, Tensor<[1392, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1392] | Unknown  |
|  3 | [Tensor<[1, 1392, 10, 10]> input = ?, Tensor<[232, 1392, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  4 | [Tensor<[1, 1392, 10, 10]> input = ?, Tensor<[384, 1392, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  5 | [Tensor<[1, 144, 151, 151]> input = ?, Tensor<[144, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 144]  | Unknown  |
|  6 | [Tensor<[1, 144, 75, 75]> input = ?, Tensor<[32, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
|  7 | [Tensor<[1, 192, 38, 38]> input = ?, Tensor<[48, 192, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
|  8 | [Tensor<[1, 192, 75, 75]> input = ?, Tensor<[192, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 192]    | Unknown  |
|  9 | [Tensor<[1, 192, 75, 75]> input = ?, Tensor<[32, 192, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 10 | [Tensor<[1, 192, 79, 79]> input = ?, Tensor<[192, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 192]    | Unknown  |
| 11 | [Tensor<[1, 232, 10, 10]> input = ?, Tensor<[1392, 232, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 12 | [Tensor<[1, 24, 150, 150]> input = ?, Tensor<[144, 24, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 13 | [Tensor<[1, 288, 19, 19]> input = ?, Tensor<[96, 288, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 14 | [Tensor<[1, 288, 38, 38]> input = ?, Tensor<[288, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 288]    | Unknown  |
| 15 | [Tensor<[1, 288, 38, 38]> input = ?, Tensor<[48, 288, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 16 | [Tensor<[1, 288, 39, 39]> input = ?, Tensor<[288, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 288]    | Unknown  |
| 17 | [Tensor<[1, 3, 301, 301]> input = ?, Tensor<[32, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]       | Unknown  |
| 18 | [Tensor<[1, 32, 150, 150]> input = ?, Tensor<[24, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 19 | [Tensor<[1, 32, 150, 150]> input = ?, Tensor<[32, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 32]     | Unknown  |
| 20 | [Tensor<[1, 32, 75, 75]> input = ?, Tensor<[192, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 21 | [Tensor<[1, 384, 10, 10]> input = ?, Tensor<[1280, 384, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 22 | [Tensor<[1, 48, 38, 38]> input = ?, Tensor<[288, 48, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 23 | [Tensor<[1, 576, 19, 19]> input = ?, Tensor<[136, 576, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 24 | [Tensor<[1, 576, 19, 19]> input = ?, Tensor<[576, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 576]    | Unknown  |
| 25 | [Tensor<[1, 576, 19, 19]> input = ?, Tensor<[576, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 576]    | Unknown  |
| 26 | [Tensor<[1, 576, 19, 19]> input = ?, Tensor<[96, 576, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 27 | [Tensor<[1, 816, 10, 10]> input = ?, Tensor<[232, 816, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 28 | [Tensor<[1, 816, 19, 19]> input = ?, Tensor<[136, 816, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 29 | [Tensor<[1, 816, 19, 19]> input = ?, Tensor<[816, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 816]    | Unknown  |
| 30 | [Tensor<[1, 816, 23, 23]> input = ?, Tensor<[816, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 816]    | Unknown  |
| 31 | [Tensor<[1, 96, 19, 19]> input = ?, Tensor<[576, 96, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                             | Status   |
|---:|:----------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 10, 10]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  1 | [Tensor<[1, 1392, 10, 10]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  2 | [Tensor<[1, 144, 150, 150]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
|  3 | [Tensor<[1, 144, 75, 75]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  4 | [Tensor<[1, 192, 38, 38]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  5 | [Tensor<[1, 192, 75, 75]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  6 | [Tensor<[1, 288, 19, 19]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  7 | [Tensor<[1, 288, 38, 38]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  8 | [Tensor<[1, 32, 150, 150]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  9 | [Tensor<[1, 576, 19, 19]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
| 10 | [Tensor<[1, 816, 10, 10]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
| 11 | [Tensor<[1, 816, 19, 19]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 10, 10]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1280]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 1, 1]> self = ?, List[int] size = [1, 1280]] | Unknown  |

