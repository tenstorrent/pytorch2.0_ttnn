# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 19 |           0 |
|  1 | aten.add.Tensor                                   |                  5 |           5 |
|  2 | aten.addmm.default                                |                  1 |           1 |
|  3 | aten.clone.default                                |                  1 |           1 |
|  4 | aten.convolution.default                          |                 30 |           0 |
|  5 | aten.hardtanh.default                             |                 12 |           0 |
|  6 | aten.mean.dim                                     |                  1 |           1 |
|  7 | aten.t.default                                    |                  1 |           1 |
|  8 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 7, 7]> input = ?, Optional[Tensor]<[1280]> weight = ?, Optional[Tensor]<[1280]> bias = ?, Tensor<[1280]> running_mean = ?, Tensor<[1280]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  1 | [Tensor<[1, 144, 28, 28]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  2 | [Tensor<[1, 144, 56, 56]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  3 | [Tensor<[1, 16, 112, 112]> input = ?, Optional[Tensor]<[16]> weight = ?, Optional[Tensor]<[16]> bias = ?, Tensor<[16]> running_mean = ?, Tensor<[16]> running_var = ?, float momentum = 0.1, float eps = 1e-05]       | Unknown  |
|  4 | [Tensor<[1, 160, 7, 7]> input = ?, Optional[Tensor]<[160]> weight = ?, Optional[Tensor]<[160]> bias = ?, Tensor<[160]> running_mean = ?, Tensor<[160]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
|  5 | [Tensor<[1, 192, 14, 14]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  6 | [Tensor<[1, 192, 28, 28]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  7 | [Tensor<[1, 24, 56, 56]> input = ?, Optional[Tensor]<[24]> weight = ?, Optional[Tensor]<[24]> bias = ?, Tensor<[24]> running_mean = ?, Tensor<[24]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
|  8 | [Tensor<[1, 32, 112, 112]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 1e-05]       | Unknown  |
|  9 | [Tensor<[1, 32, 28, 28]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 10 | [Tensor<[1, 320, 7, 7]> input = ?, Optional[Tensor]<[320]> weight = ?, Optional[Tensor]<[320]> bias = ?, Tensor<[320]> running_mean = ?, Tensor<[320]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 11 | [Tensor<[1, 384, 14, 14]> input = ?, Optional[Tensor]<[384]> weight = ?, Optional[Tensor]<[384]> bias = ?, Tensor<[384]> running_mean = ?, Tensor<[384]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
| 12 | [Tensor<[1, 576, 14, 14]> input = ?, Optional[Tensor]<[576]> weight = ?, Optional[Tensor]<[576]> bias = ?, Tensor<[576]> running_mean = ?, Tensor<[576]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
| 13 | [Tensor<[1, 576, 7, 7]> input = ?, Optional[Tensor]<[576]> weight = ?, Optional[Tensor]<[576]> bias = ?, Tensor<[576]> running_mean = ?, Tensor<[576]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 14 | [Tensor<[1, 64, 14, 14]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 15 | [Tensor<[1, 96, 112, 112]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 1e-05]       | Unknown  |
| 16 | [Tensor<[1, 96, 14, 14]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 17 | [Tensor<[1, 96, 56, 56]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 18 | [Tensor<[1, 960, 7, 7]> input = ?, Optional[Tensor]<[960]> weight = ?, Optional[Tensor]<[960]> bias = ?, Tensor<[960]> running_mean = ?, Tensor<[960]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 160, 7, 7]> self = ?, Tensor<[1, 160, 7, 7]> other = ?]   | Done     |
|  1 | [Tensor<[1, 24, 56, 56]> self = ?, Tensor<[1, 24, 56, 56]> other = ?] | Done     |
|  2 | [Tensor<[1, 32, 28, 28]> self = ?, Tensor<[1, 32, 28, 28]> other = ?] | Done     |
|  3 | [Tensor<[1, 64, 14, 14]> self = ?, Tensor<[1, 64, 14, 14]> other = ?] | Done     |
|  4 | [Tensor<[1, 96, 14, 14]> self = ?, Tensor<[1, 96, 14, 14]> other = ?] | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1280]> mat1 = ?, Tensor<[1280, 1000]> mat2 = ?] | Done     |
### aten.clone.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | [Tensor<[1, 1280]> self = ?] | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 144, 28, 28]> input = ?, Tensor<[32, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  1 | [Tensor<[1, 144, 56, 56]> input = ?, Tensor<[144, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 144] | Unknown  |
|  2 | [Tensor<[1, 144, 56, 56]> input = ?, Tensor<[144, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 144] | Unknown  |
|  3 | [Tensor<[1, 144, 56, 56]> input = ?, Tensor<[24, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  4 | [Tensor<[1, 16, 112, 112]> input = ?, Tensor<[96, 16, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  5 | [Tensor<[1, 160, 7, 7]> input = ?, Tensor<[960, 160, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  6 | [Tensor<[1, 192, 14, 14]> input = ?, Tensor<[64, 192, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  7 | [Tensor<[1, 192, 28, 28]> input = ?, Tensor<[192, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 192] | Unknown  |
|  8 | [Tensor<[1, 192, 28, 28]> input = ?, Tensor<[192, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 192] | Unknown  |
|  9 | [Tensor<[1, 192, 28, 28]> input = ?, Tensor<[32, 192, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 10 | [Tensor<[1, 24, 56, 56]> input = ?, Tensor<[144, 24, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 11 | [Tensor<[1, 3, 224, 224]> input = ?, Tensor<[32, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 12 | [Tensor<[1, 32, 112, 112]> input = ?, Tensor<[16, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 13 | [Tensor<[1, 32, 112, 112]> input = ?, Tensor<[32, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 32]  | Unknown  |
| 14 | [Tensor<[1, 32, 28, 28]> input = ?, Tensor<[192, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 15 | [Tensor<[1, 320, 7, 7]> input = ?, Tensor<[1280, 320, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 16 | [Tensor<[1, 384, 14, 14]> input = ?, Tensor<[384, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 384] | Unknown  |
| 17 | [Tensor<[1, 384, 14, 14]> input = ?, Tensor<[64, 384, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 18 | [Tensor<[1, 384, 14, 14]> input = ?, Tensor<[96, 384, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 19 | [Tensor<[1, 576, 14, 14]> input = ?, Tensor<[576, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 576] | Unknown  |
| 20 | [Tensor<[1, 576, 14, 14]> input = ?, Tensor<[576, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 576] | Unknown  |
| 21 | [Tensor<[1, 576, 14, 14]> input = ?, Tensor<[96, 576, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 22 | [Tensor<[1, 576, 7, 7]> input = ?, Tensor<[160, 576, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 23 | [Tensor<[1, 64, 14, 14]> input = ?, Tensor<[384, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 24 | [Tensor<[1, 96, 112, 112]> input = ?, Tensor<[96, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 96]  | Unknown  |
| 25 | [Tensor<[1, 96, 14, 14]> input = ?, Tensor<[576, 96, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 26 | [Tensor<[1, 96, 56, 56]> input = ?, Tensor<[24, 96, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 27 | [Tensor<[1, 960, 7, 7]> input = ?, Tensor<[160, 960, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 28 | [Tensor<[1, 960, 7, 7]> input = ?, Tensor<[320, 960, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 29 | [Tensor<[1, 960, 7, 7]> input = ?, Tensor<[960, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 960]   | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 7, 7]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  1 | [Tensor<[1, 144, 28, 28]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  2 | [Tensor<[1, 144, 56, 56]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  3 | [Tensor<[1, 192, 14, 14]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  4 | [Tensor<[1, 192, 28, 28]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  5 | [Tensor<[1, 32, 112, 112]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
|  6 | [Tensor<[1, 384, 14, 14]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  7 | [Tensor<[1, 576, 14, 14]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  8 | [Tensor<[1, 576, 7, 7]> self = ?, number min_val = 0.0, number max_val = 6.0]    | Unknown  |
|  9 | [Tensor<[1, 96, 112, 112]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
| 10 | [Tensor<[1, 96, 56, 56]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
| 11 | [Tensor<[1, 960, 7, 7]> self = ?, number min_val = 0.0, number max_val = 6.0]    | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 7, 7]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1280]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 1, 1]> self = ?, List[int] size = [1, 1280]] | Unknown  |

