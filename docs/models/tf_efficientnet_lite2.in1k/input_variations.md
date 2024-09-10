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
|  0 | [Tensor<[1, 120, 17, 17]> input = ?, Optional[Tensor]<[120]> weight = ?, Optional[Tensor]<[120]> bias = ?, Tensor<[120]> running_mean = ?, Tensor<[120]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  1 | [Tensor<[1, 1248, 9, 9]> input = ?, Optional[Tensor]<[1248]> weight = ?, Optional[Tensor]<[1248]> bias = ?, Tensor<[1248]> running_mean = ?, Tensor<[1248]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  2 | [Tensor<[1, 1280, 9, 9]> input = ?, Optional[Tensor]<[1280]> weight = ?, Optional[Tensor]<[1280]> bias = ?, Tensor<[1280]> running_mean = ?, Tensor<[1280]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  3 | [Tensor<[1, 144, 33, 33]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  4 | [Tensor<[1, 144, 65, 65]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  5 | [Tensor<[1, 16, 130, 130]> input = ?, Optional[Tensor]<[16]> weight = ?, Optional[Tensor]<[16]> bias = ?, Tensor<[16]> running_mean = ?, Tensor<[16]> running_var = ?, float momentum = 0.1, float eps = 0.001]       | Unknown  |
|  6 | [Tensor<[1, 208, 9, 9]> input = ?, Optional[Tensor]<[208]> weight = ?, Optional[Tensor]<[208]> bias = ?, Tensor<[208]> running_mean = ?, Tensor<[208]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  7 | [Tensor<[1, 24, 65, 65]> input = ?, Optional[Tensor]<[24]> weight = ?, Optional[Tensor]<[24]> bias = ?, Tensor<[24]> running_mean = ?, Tensor<[24]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
|  8 | [Tensor<[1, 288, 17, 17]> input = ?, Optional[Tensor]<[288]> weight = ?, Optional[Tensor]<[288]> bias = ?, Tensor<[288]> running_mean = ?, Tensor<[288]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  9 | [Tensor<[1, 288, 33, 33]> input = ?, Optional[Tensor]<[288]> weight = ?, Optional[Tensor]<[288]> bias = ?, Tensor<[288]> running_mean = ?, Tensor<[288]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
| 10 | [Tensor<[1, 32, 130, 130]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]       | Unknown  |
| 11 | [Tensor<[1, 352, 9, 9]> input = ?, Optional[Tensor]<[352]> weight = ?, Optional[Tensor]<[352]> bias = ?, Tensor<[352]> running_mean = ?, Tensor<[352]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 12 | [Tensor<[1, 48, 33, 33]> input = ?, Optional[Tensor]<[48]> weight = ?, Optional[Tensor]<[48]> bias = ?, Tensor<[48]> running_mean = ?, Tensor<[48]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
| 13 | [Tensor<[1, 528, 17, 17]> input = ?, Optional[Tensor]<[528]> weight = ?, Optional[Tensor]<[528]> bias = ?, Tensor<[528]> running_mean = ?, Tensor<[528]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
| 14 | [Tensor<[1, 720, 17, 17]> input = ?, Optional[Tensor]<[720]> weight = ?, Optional[Tensor]<[720]> bias = ?, Tensor<[720]> running_mean = ?, Tensor<[720]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
| 15 | [Tensor<[1, 720, 9, 9]> input = ?, Optional[Tensor]<[720]> weight = ?, Optional[Tensor]<[720]> bias = ?, Tensor<[720]> running_mean = ?, Tensor<[720]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 16 | [Tensor<[1, 88, 17, 17]> input = ?, Optional[Tensor]<[88]> weight = ?, Optional[Tensor]<[88]> bias = ?, Tensor<[88]> running_mean = ?, Tensor<[88]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
| 17 | [Tensor<[1, 96, 130, 130]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 0.001]       | Unknown  |
| 18 | [Tensor<[1, 96, 65, 65]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 120, 17, 17]> self = ?, Tensor<[1, 120, 17, 17]> other = ?] | Done     |
|  1 | [Tensor<[1, 208, 9, 9]> self = ?, Tensor<[1, 208, 9, 9]> other = ?]     | Done     |
|  2 | [Tensor<[1, 24, 65, 65]> self = ?, Tensor<[1, 24, 65, 65]> other = ?]   | Done     |
|  3 | [Tensor<[1, 48, 33, 33]> self = ?, Tensor<[1, 48, 33, 33]> other = ?]   | Done     |
|  4 | [Tensor<[1, 88, 17, 17]> self = ?, Tensor<[1, 88, 17, 17]> other = ?]   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1280]> mat1 = ?, Tensor<[1280, 1000]> mat2 = ?] | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 144, 65, 65]> self = ?, List[int] pad = [2, 2, 2, 2], number value = 0.0]  | Unknown  |
|  1 | [Tensor<[1, 288, 33, 33]> self = ?, List[int] pad = [1, 1, 1, 1], number value = 0.0]  | Unknown  |
|  2 | [Tensor<[1, 3, 260, 260]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0]  | Unknown  |
|  3 | [Tensor<[1, 720, 17, 17]> self = ?, List[int] pad = [2, 2, 2, 2], number value = 0.0]  | Unknown  |
|  4 | [Tensor<[1, 96, 130, 130]> self = ?, List[int] pad = [0, 1, 0, 1], number value = 0.0] | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 120, 17, 17]> input = ?, Tensor<[720, 120, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  1 | [Tensor<[1, 1248, 9, 9]> input = ?, Tensor<[1248, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1248] | Unknown  |
|  2 | [Tensor<[1, 1248, 9, 9]> input = ?, Tensor<[1248, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1248] | Unknown  |
|  3 | [Tensor<[1, 1248, 9, 9]> input = ?, Tensor<[208, 1248, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  4 | [Tensor<[1, 1248, 9, 9]> input = ?, Tensor<[352, 1248, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  5 | [Tensor<[1, 144, 33, 33]> input = ?, Tensor<[48, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  6 | [Tensor<[1, 144, 65, 65]> input = ?, Tensor<[144, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 144]  | Unknown  |
|  7 | [Tensor<[1, 144, 65, 65]> input = ?, Tensor<[24, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  8 | [Tensor<[1, 144, 69, 69]> input = ?, Tensor<[144, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 144]  | Unknown  |
|  9 | [Tensor<[1, 16, 130, 130]> input = ?, Tensor<[96, 16, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 10 | [Tensor<[1, 208, 9, 9]> input = ?, Tensor<[1248, 208, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 11 | [Tensor<[1, 24, 65, 65]> input = ?, Tensor<[144, 24, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 12 | [Tensor<[1, 288, 17, 17]> input = ?, Tensor<[88, 288, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 13 | [Tensor<[1, 288, 33, 33]> input = ?, Tensor<[288, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 288]  | Unknown  |
| 14 | [Tensor<[1, 288, 33, 33]> input = ?, Tensor<[48, 288, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 15 | [Tensor<[1, 288, 35, 35]> input = ?, Tensor<[288, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 288]  | Unknown  |
| 16 | [Tensor<[1, 3, 261, 261]> input = ?, Tensor<[32, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 17 | [Tensor<[1, 32, 130, 130]> input = ?, Tensor<[16, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 18 | [Tensor<[1, 32, 130, 130]> input = ?, Tensor<[32, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 32]   | Unknown  |
| 19 | [Tensor<[1, 352, 9, 9]> input = ?, Tensor<[1280, 352, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 20 | [Tensor<[1, 48, 33, 33]> input = ?, Tensor<[288, 48, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 21 | [Tensor<[1, 528, 17, 17]> input = ?, Tensor<[120, 528, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 22 | [Tensor<[1, 528, 17, 17]> input = ?, Tensor<[528, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 528]  | Unknown  |
| 23 | [Tensor<[1, 528, 17, 17]> input = ?, Tensor<[528, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 528]  | Unknown  |
| 24 | [Tensor<[1, 528, 17, 17]> input = ?, Tensor<[88, 528, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 25 | [Tensor<[1, 720, 17, 17]> input = ?, Tensor<[120, 720, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 26 | [Tensor<[1, 720, 17, 17]> input = ?, Tensor<[720, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 720]  | Unknown  |
| 27 | [Tensor<[1, 720, 21, 21]> input = ?, Tensor<[720, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 720]  | Unknown  |
| 28 | [Tensor<[1, 720, 9, 9]> input = ?, Tensor<[208, 720, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 29 | [Tensor<[1, 88, 17, 17]> input = ?, Tensor<[528, 88, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 30 | [Tensor<[1, 96, 131, 131]> input = ?, Tensor<[96, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 96]   | Unknown  |
| 31 | [Tensor<[1, 96, 65, 65]> input = ?, Tensor<[24, 96, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1248, 9, 9]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  1 | [Tensor<[1, 1280, 9, 9]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  2 | [Tensor<[1, 144, 33, 33]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  3 | [Tensor<[1, 144, 65, 65]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  4 | [Tensor<[1, 288, 17, 17]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  5 | [Tensor<[1, 288, 33, 33]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  6 | [Tensor<[1, 32, 130, 130]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
|  7 | [Tensor<[1, 528, 17, 17]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  8 | [Tensor<[1, 720, 17, 17]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  9 | [Tensor<[1, 720, 9, 9]> self = ?, number min_val = 0.0, number max_val = 6.0]    | Unknown  |
| 10 | [Tensor<[1, 96, 130, 130]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
| 11 | [Tensor<[1, 96, 65, 65]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 9, 9]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1280]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 1, 1]> self = ?, List[int] size = [1, 1280]] | Unknown  |

