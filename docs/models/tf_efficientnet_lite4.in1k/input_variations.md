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
|  0 | [Tensor<[1, 112, 24, 24]> input = ?, Optional[Tensor]<[112]> weight = ?, Optional[Tensor]<[112]> bias = ?, Tensor<[112]> running_mean = ?, Tensor<[112]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  1 | [Tensor<[1, 1280, 12, 12]> input = ?, Optional[Tensor]<[1280]> weight = ?, Optional[Tensor]<[1280]> bias = ?, Tensor<[1280]> running_mean = ?, Tensor<[1280]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  2 | [Tensor<[1, 144, 190, 190]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  3 | [Tensor<[1, 144, 95, 95]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  4 | [Tensor<[1, 160, 24, 24]> input = ?, Optional[Tensor]<[160]> weight = ?, Optional[Tensor]<[160]> bias = ?, Tensor<[160]> running_mean = ?, Tensor<[160]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  5 | [Tensor<[1, 1632, 12, 12]> input = ?, Optional[Tensor]<[1632]> weight = ?, Optional[Tensor]<[1632]> bias = ?, Tensor<[1632]> running_mean = ?, Tensor<[1632]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  6 | [Tensor<[1, 192, 48, 48]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  7 | [Tensor<[1, 192, 95, 95]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  8 | [Tensor<[1, 24, 190, 190]> input = ?, Optional[Tensor]<[24]> weight = ?, Optional[Tensor]<[24]> bias = ?, Tensor<[24]> running_mean = ?, Tensor<[24]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
|  9 | [Tensor<[1, 272, 12, 12]> input = ?, Optional[Tensor]<[272]> weight = ?, Optional[Tensor]<[272]> bias = ?, Tensor<[272]> running_mean = ?, Tensor<[272]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 10 | [Tensor<[1, 32, 190, 190]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
| 11 | [Tensor<[1, 32, 95, 95]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]           | Unknown  |
| 12 | [Tensor<[1, 336, 24, 24]> input = ?, Optional[Tensor]<[336]> weight = ?, Optional[Tensor]<[336]> bias = ?, Tensor<[336]> running_mean = ?, Tensor<[336]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 13 | [Tensor<[1, 336, 48, 48]> input = ?, Optional[Tensor]<[336]> weight = ?, Optional[Tensor]<[336]> bias = ?, Tensor<[336]> running_mean = ?, Tensor<[336]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 14 | [Tensor<[1, 448, 12, 12]> input = ?, Optional[Tensor]<[448]> weight = ?, Optional[Tensor]<[448]> bias = ?, Tensor<[448]> running_mean = ?, Tensor<[448]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 15 | [Tensor<[1, 56, 48, 48]> input = ?, Optional[Tensor]<[56]> weight = ?, Optional[Tensor]<[56]> bias = ?, Tensor<[56]> running_mean = ?, Tensor<[56]> running_var = ?, float momentum = 0.1, float eps = 0.001]           | Unknown  |
| 16 | [Tensor<[1, 672, 24, 24]> input = ?, Optional[Tensor]<[672]> weight = ?, Optional[Tensor]<[672]> bias = ?, Tensor<[672]> running_mean = ?, Tensor<[672]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 17 | [Tensor<[1, 960, 12, 12]> input = ?, Optional[Tensor]<[960]> weight = ?, Optional[Tensor]<[960]> bias = ?, Tensor<[960]> running_mean = ?, Tensor<[960]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 18 | [Tensor<[1, 960, 24, 24]> input = ?, Optional[Tensor]<[960]> weight = ?, Optional[Tensor]<[960]> bias = ?, Tensor<[960]> running_mean = ?, Tensor<[960]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 24, 24]> self = ?, Tensor<[1, 112, 24, 24]> other = ?] | Done     |
|  1 | [Tensor<[1, 160, 24, 24]> self = ?, Tensor<[1, 160, 24, 24]> other = ?] | Done     |
|  2 | [Tensor<[1, 272, 12, 12]> self = ?, Tensor<[1, 272, 12, 12]> other = ?] | Done     |
|  3 | [Tensor<[1, 32, 95, 95]> self = ?, Tensor<[1, 32, 95, 95]> other = ?]   | Done     |
|  4 | [Tensor<[1, 56, 48, 48]> self = ?, Tensor<[1, 56, 48, 48]> other = ?]   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1280]> mat1 = ?, Tensor<[1280, 1000]> mat2 = ?] | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 144, 190, 190]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0] | Unknown  |
|  1 | [Tensor<[1, 192, 95, 95]> self = ?, List[int] pad = [2, 2, 2, 2], number value = 0.0]   | Unknown  |
|  2 | [Tensor<[1, 3, 380, 380]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0]   | Unknown  |
|  3 | [Tensor<[1, 336, 48, 48]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0]   | Unknown  |
|  4 | [Tensor<[1, 960, 24, 24]> self = ?, List[int] pad = [1, 2, 1, 2], number value = 0.0]   | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 24, 24]> input = ?, Tensor<[672, 112, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
|  1 | [Tensor<[1, 144, 191, 191]> input = ?, Tensor<[144, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 144]  | Unknown  |
|  2 | [Tensor<[1, 144, 95, 95]> input = ?, Tensor<[32, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
|  3 | [Tensor<[1, 160, 24, 24]> input = ?, Tensor<[960, 160, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
|  4 | [Tensor<[1, 1632, 12, 12]> input = ?, Tensor<[1632, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1632] | Unknown  |
|  5 | [Tensor<[1, 1632, 12, 12]> input = ?, Tensor<[1632, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1632] | Unknown  |
|  6 | [Tensor<[1, 1632, 12, 12]> input = ?, Tensor<[272, 1632, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  7 | [Tensor<[1, 1632, 12, 12]> input = ?, Tensor<[448, 1632, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  8 | [Tensor<[1, 192, 48, 48]> input = ?, Tensor<[56, 192, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
|  9 | [Tensor<[1, 192, 95, 95]> input = ?, Tensor<[192, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 192]    | Unknown  |
| 10 | [Tensor<[1, 192, 95, 95]> input = ?, Tensor<[32, 192, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 11 | [Tensor<[1, 192, 99, 99]> input = ?, Tensor<[192, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 192]    | Unknown  |
| 12 | [Tensor<[1, 24, 190, 190]> input = ?, Tensor<[144, 24, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 13 | [Tensor<[1, 272, 12, 12]> input = ?, Tensor<[1632, 272, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 14 | [Tensor<[1, 3, 381, 381]> input = ?, Tensor<[32, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]       | Unknown  |
| 15 | [Tensor<[1, 32, 190, 190]> input = ?, Tensor<[24, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 16 | [Tensor<[1, 32, 190, 190]> input = ?, Tensor<[32, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 32]     | Unknown  |
| 17 | [Tensor<[1, 32, 95, 95]> input = ?, Tensor<[192, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 18 | [Tensor<[1, 336, 24, 24]> input = ?, Tensor<[112, 336, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 19 | [Tensor<[1, 336, 48, 48]> input = ?, Tensor<[336, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 336]    | Unknown  |
| 20 | [Tensor<[1, 336, 48, 48]> input = ?, Tensor<[56, 336, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 21 | [Tensor<[1, 336, 49, 49]> input = ?, Tensor<[336, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 336]    | Unknown  |
| 22 | [Tensor<[1, 448, 12, 12]> input = ?, Tensor<[1280, 448, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 23 | [Tensor<[1, 56, 48, 48]> input = ?, Tensor<[336, 56, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 24 | [Tensor<[1, 672, 24, 24]> input = ?, Tensor<[112, 672, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 25 | [Tensor<[1, 672, 24, 24]> input = ?, Tensor<[160, 672, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 26 | [Tensor<[1, 672, 24, 24]> input = ?, Tensor<[672, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 672]    | Unknown  |
| 27 | [Tensor<[1, 672, 24, 24]> input = ?, Tensor<[672, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 672]    | Unknown  |
| 28 | [Tensor<[1, 960, 12, 12]> input = ?, Tensor<[272, 960, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 29 | [Tensor<[1, 960, 24, 24]> input = ?, Tensor<[160, 960, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 30 | [Tensor<[1, 960, 24, 24]> input = ?, Tensor<[960, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 960]    | Unknown  |
| 31 | [Tensor<[1, 960, 27, 27]> input = ?, Tensor<[960, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 960]    | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                             | Status   |
|---:|:----------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 12, 12]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  1 | [Tensor<[1, 144, 190, 190]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
|  2 | [Tensor<[1, 144, 95, 95]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  3 | [Tensor<[1, 1632, 12, 12]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  4 | [Tensor<[1, 192, 48, 48]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  5 | [Tensor<[1, 192, 95, 95]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  6 | [Tensor<[1, 32, 190, 190]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  7 | [Tensor<[1, 336, 24, 24]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  8 | [Tensor<[1, 336, 48, 48]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  9 | [Tensor<[1, 672, 24, 24]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
| 10 | [Tensor<[1, 960, 12, 12]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
| 11 | [Tensor<[1, 960, 24, 24]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 12, 12]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1280]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 1, 1]> self = ?, List[int] size = [1, 1280]] | Unknown  |

