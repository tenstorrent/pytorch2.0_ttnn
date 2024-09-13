# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 10 |           0 |
|  1 | aten.addmm.default                                |                  1 |           1 |
|  2 | aten.convolution.default                          |                 19 |           0 |
|  3 | aten.hardtanh.default                             |                 10 |           0 |
|  4 | aten.mean.dim                                     |                  1 |           1 |
|  5 | aten.t.default                                    |                  1 |           1 |
|  6 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> input = ?, Optional[Tensor]<[1024]> weight = ?, Optional[Tensor]<[1024]> bias = ?, Tensor<[1024]> running_mean = ?, Tensor<[1024]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  1 | [Tensor<[1, 128, 28, 28]> input = ?, Optional[Tensor]<[128]> weight = ?, Optional[Tensor]<[128]> bias = ?, Tensor<[128]> running_mean = ?, Tensor<[128]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  2 | [Tensor<[1, 128, 56, 56]> input = ?, Optional[Tensor]<[128]> weight = ?, Optional[Tensor]<[128]> bias = ?, Tensor<[128]> running_mean = ?, Tensor<[128]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  3 | [Tensor<[1, 256, 14, 14]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  4 | [Tensor<[1, 256, 28, 28]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  5 | [Tensor<[1, 32, 112, 112]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 1e-05]       | Unknown  |
|  6 | [Tensor<[1, 512, 14, 14]> input = ?, Optional[Tensor]<[512]> weight = ?, Optional[Tensor]<[512]> bias = ?, Tensor<[512]> running_mean = ?, Tensor<[512]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  7 | [Tensor<[1, 512, 7, 7]> input = ?, Optional[Tensor]<[512]> weight = ?, Optional[Tensor]<[512]> bias = ?, Tensor<[512]> running_mean = ?, Tensor<[512]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
|  8 | [Tensor<[1, 64, 112, 112]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 1e-05]       | Unknown  |
|  9 | [Tensor<[1, 64, 56, 56]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1024]> mat1 = ?, Tensor<[1024, 1000]> mat2 = ?] | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> input = ?, Tensor<[1024, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1024] | Unknown  |
|  1 | [Tensor<[1, 1024, 7, 7]> input = ?, Tensor<[1024, 1024, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  2 | [Tensor<[1, 128, 28, 28]> input = ?, Tensor<[256, 128, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  3 | [Tensor<[1, 128, 56, 56]> input = ?, Tensor<[128, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 128]  | Unknown  |
|  4 | [Tensor<[1, 128, 56, 56]> input = ?, Tensor<[128, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 128]  | Unknown  |
|  5 | [Tensor<[1, 128, 56, 56]> input = ?, Tensor<[128, 128, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  6 | [Tensor<[1, 256, 14, 14]> input = ?, Tensor<[512, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  7 | [Tensor<[1, 256, 28, 28]> input = ?, Tensor<[256, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 256]  | Unknown  |
|  8 | [Tensor<[1, 256, 28, 28]> input = ?, Tensor<[256, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 256]  | Unknown  |
|  9 | [Tensor<[1, 256, 28, 28]> input = ?, Tensor<[256, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 10 | [Tensor<[1, 3, 224, 224]> input = ?, Tensor<[32, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 11 | [Tensor<[1, 32, 112, 112]> input = ?, Tensor<[32, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 32]   | Unknown  |
| 12 | [Tensor<[1, 32, 112, 112]> input = ?, Tensor<[64, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 13 | [Tensor<[1, 512, 14, 14]> input = ?, Tensor<[512, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 512]  | Unknown  |
| 14 | [Tensor<[1, 512, 14, 14]> input = ?, Tensor<[512, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 512]  | Unknown  |
| 15 | [Tensor<[1, 512, 14, 14]> input = ?, Tensor<[512, 512, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
| 16 | [Tensor<[1, 512, 7, 7]> input = ?, Tensor<[1024, 512, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 17 | [Tensor<[1, 64, 112, 112]> input = ?, Tensor<[64, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 64]   | Unknown  |
| 18 | [Tensor<[1, 64, 56, 56]> input = ?, Tensor<[128, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
### aten.hardtanh.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
|  1 | [Tensor<[1, 128, 28, 28]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  2 | [Tensor<[1, 128, 56, 56]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  3 | [Tensor<[1, 256, 14, 14]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  4 | [Tensor<[1, 256, 28, 28]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  5 | [Tensor<[1, 32, 112, 112]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
|  6 | [Tensor<[1, 512, 14, 14]> self = ?, number min_val = 0.0, number max_val = 6.0]  | Unknown  |
|  7 | [Tensor<[1, 512, 7, 7]> self = ?, number min_val = 0.0, number max_val = 6.0]    | Unknown  |
|  8 | [Tensor<[1, 64, 112, 112]> self = ?, number min_val = 0.0, number max_val = 6.0] | Unknown  |
|  9 | [Tensor<[1, 64, 56, 56]> self = ?, number min_val = 0.0, number max_val = 6.0]   | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1024]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 1, 1]> self = ?, List[int] size = [1, 1024]] | Unknown  |

