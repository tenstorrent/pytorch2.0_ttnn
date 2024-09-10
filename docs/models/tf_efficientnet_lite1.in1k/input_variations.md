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
|    | ATen Input Variations                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 15, 15]> input = ?, Optional[Tensor]<[112]> weight = ?, Optional[Tensor]<[112]> bias = ?, Tensor<[112]> running_mean = ?, Tensor<[112]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  1 | [Tensor<[1, 1152, 8, 8]> input = ?, Optional[Tensor]<[1152]> weight = ?, Optional[Tensor]<[1152]> bias = ?, Tensor<[1152]> running_mean = ?, Tensor<[1152]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  2 | [Tensor<[1, 1280, 8, 8]> input = ?, Optional[Tensor]<[1280]> weight = ?, Optional[Tensor]<[1280]> bias = ?, Tensor<[1280]> running_mean = ?, Tensor<[1280]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  3 | [Tensor<[1, 144, 30, 30]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  4 | [Tensor<[1, 144, 60, 60]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  5 | [Tensor<[1, 16, 120, 120]> input = ?, Optional[Tensor]<[16]> weight = ?, Optional[Tensor]<[16]> bias = ?, Tensor<[16]> running_mean = ?, Tensor<[16]> running_var = ?, float momentum = 0.1, float eps = 0.001]       | Unknown  |
|  6 | [Tensor<[1, 192, 8, 8]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  7 | [Tensor<[1, 24, 60, 60]> input = ?, Optional[Tensor]<[24]> weight = ?, Optional[Tensor]<[24]> bias = ?, Tensor<[24]> running_mean = ?, Tensor<[24]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
|  8 | [Tensor<[1, 240, 15, 15]> input = ?, Optional[Tensor]<[240]> weight = ?, Optional[Tensor]<[240]> bias = ?, Tensor<[240]> running_mean = ?, Tensor<[240]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  9 | [Tensor<[1, 240, 30, 30]> input = ?, Optional[Tensor]<[240]> weight = ?, Optional[Tensor]<[240]> bias = ?, Tensor<[240]> running_mean = ?, Tensor<[240]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
| 10 | [Tensor<[1, 32, 120, 120]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]       | Unknown  |
| 11 | [Tensor<[1, 320, 8, 8]> input = ?, Optional[Tensor]<[320]> weight = ?, Optional[Tensor]<[320]> bias = ?, Tensor<[320]> running_mean = ?, Tensor<[320]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 12 | [Tensor<[1, 40, 30, 30]> input = ?, Optional[Tensor]<[40]> weight = ?, Optional[Tensor]<[40]> bias = ?, Tensor<[40]> running_mean = ?, Tensor<[40]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
| 13 | [Tensor<[1, 480, 15, 15]> input = ?, Optional[Tensor]<[480]> weight = ?, Optional[Tensor]<[480]> bias = ?, Tensor<[480]> running_mean = ?, Tensor<[480]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
| 14 | [Tensor<[1, 672, 15, 15]> input = ?, Optional[Tensor]<[672]> weight = ?, Optional[Tensor]<[672]> bias = ?, Tensor<[672]> running_mean = ?, Tensor<[672]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
| 15 | [Tensor<[1, 672, 8, 8]> input = ?, Optional[Tensor]<[672]> weight = ?, Optional[Tensor]<[672]> bias = ?, Tensor<[672]> running_mean = ?, Tensor<[672]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 16 | [Tensor<[1, 80, 15, 15]> input = ?, Optional[Tensor]<[80]> weight = ?, Optional[Tensor]<[80]> bias = ?, Tensor<[80]> running_mean = ?, Tensor<[80]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
| 17 | [Tensor<[1, 96, 120, 120]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 0.001]       | Unknown  |
| 18 | [Tensor<[1, 96, 60, 60]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 15, 15]> self = ?, Tensor<[1, 112, 15, 15]> other = ?] | Done     |
|  1 | [Tensor<[1, 192, 8, 8]> self = ?, Tensor<[1, 192, 8, 8]> other = ?]     | Done     |
|  2 | [Tensor<[1, 24, 60, 60]> self = ?, Tensor<[1, 24, 60, 60]> other = ?]   | Done     |
|  3 | [Tensor<[1, 40, 30, 30]> self = ?, Tensor<[1, 40, 30, 30]> other = ?]   | Done     |
|  4 | [Tensor<[1, 80, 15, 15]> self = ?, Tensor<[1, 80, 15, 15]> other = ?]   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1280]> mat1 = ?, Tensor<[1280, 1000]> mat2 = ?] | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 144, 60, 60]> self = ?, List[int] pad = [1, 2, 1, 2], number value = 0.0]  | Unknown  |
|  1 | [Tensor<[1, 240, 30, 30]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0]  | Unknown  |
|  2 | [Tensor<[1, 3, 240, 240]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0]  | Unknown  |
|  3 | [Tensor<[1, 672, 15, 15]> self = ?, List[int] pad = [2, 2, 2, 2], number value = 0.0]  | Unknown  |
|  4 | [Tensor<[1, 96, 120, 120]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0] | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 15, 15]> input = ?, Tensor<[672, 112, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  1 | [Tensor<[1, 1152, 8, 8]> input = ?, Tensor<[1152, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1152] | Unknown  |
|  2 | [Tensor<[1, 1152, 8, 8]> input = ?, Tensor<[1152, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1152] | Unknown  |
|  3 | [Tensor<[1, 1152, 8, 8]> input = ?, Tensor<[192, 1152, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  4 | [Tensor<[1, 1152, 8, 8]> input = ?, Tensor<[320, 1152, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  5 | [Tensor<[1, 144, 30, 30]> input = ?, Tensor<[40, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  6 | [Tensor<[1, 144, 60, 60]> input = ?, Tensor<[144, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 144]  | Unknown  |
|  7 | [Tensor<[1, 144, 60, 60]> input = ?, Tensor<[24, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  8 | [Tensor<[1, 144, 63, 63]> input = ?, Tensor<[144, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 144]  | Unknown  |
|  9 | [Tensor<[1, 16, 120, 120]> input = ?, Tensor<[96, 16, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 10 | [Tensor<[1, 192, 8, 8]> input = ?, Tensor<[1152, 192, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 11 | [Tensor<[1, 24, 60, 60]> input = ?, Tensor<[144, 24, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 12 | [Tensor<[1, 240, 15, 15]> input = ?, Tensor<[80, 240, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 13 | [Tensor<[1, 240, 30, 30]> input = ?, Tensor<[240, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 240]  | Unknown  |
| 14 | [Tensor<[1, 240, 30, 30]> input = ?, Tensor<[40, 240, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 15 | [Tensor<[1, 240, 31, 31]> input = ?, Tensor<[240, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 240]  | Unknown  |
| 16 | [Tensor<[1, 3, 241, 241]> input = ?, Tensor<[32, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 17 | [Tensor<[1, 32, 120, 120]> input = ?, Tensor<[16, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 18 | [Tensor<[1, 32, 120, 120]> input = ?, Tensor<[32, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 32]   | Unknown  |
| 19 | [Tensor<[1, 320, 8, 8]> input = ?, Tensor<[1280, 320, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 20 | [Tensor<[1, 40, 30, 30]> input = ?, Tensor<[240, 40, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 21 | [Tensor<[1, 480, 15, 15]> input = ?, Tensor<[112, 480, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 22 | [Tensor<[1, 480, 15, 15]> input = ?, Tensor<[480, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 480]  | Unknown  |
| 23 | [Tensor<[1, 480, 15, 15]> input = ?, Tensor<[480, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 480]  | Unknown  |
| 24 | [Tensor<[1, 480, 15, 15]> input = ?, Tensor<[80, 480, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 25 | [Tensor<[1, 672, 15, 15]> input = ?, Tensor<[112, 672, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 26 | [Tensor<[1, 672, 15, 15]> input = ?, Tensor<[672, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 672]  | Unknown  |
| 27 | [Tensor<[1, 672, 19, 19]> input = ?, Tensor<[672, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 672]  | Unknown  |
| 28 | [Tensor<[1, 672, 8, 8]> input = ?, Tensor<[192, 672, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 29 | [Tensor<[1, 80, 15, 15]> input = ?, Tensor<[480, 80, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 30 | [Tensor<[1, 96, 121, 121]> input = ?, Tensor<[96, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 96]   | Unknown  |
| 31 | [Tensor<[1, 96, 60, 60]> input = ?, Tensor<[24, 96, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1152, 8, 8]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  1 | [Tensor<[1, 1280, 8, 8]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  2 | [Tensor<[1, 144, 30, 30]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  3 | [Tensor<[1, 144, 60, 60]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  4 | [Tensor<[1, 240, 15, 15]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  5 | [Tensor<[1, 240, 30, 30]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  6 | [Tensor<[1, 32, 120, 120]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
|  7 | [Tensor<[1, 480, 15, 15]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  8 | [Tensor<[1, 672, 15, 15]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  9 | [Tensor<[1, 672, 8, 8]> self = ?, number min_val = 0.0, number max_val = 6.0]    | Unknown  |
| 10 | [Tensor<[1, 96, 120, 120]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
| 11 | [Tensor<[1, 96, 60, 60]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 8, 8]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1280]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 1, 1]> self = ?, List[int] size = [1, 1280]] | Unknown  |

