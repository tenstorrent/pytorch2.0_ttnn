# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 12 |           0 |
|  1 | aten.add.Tensor                                   |                  6 |           6 |
|  2 | aten.addmm.default                                |                  1 |           1 |
|  3 | aten.clone.default                                |                  1 |           1 |
|  4 | aten.convolution.default                          |                 33 |           0 |
|  5 | aten.mean.dim                                     |                  1 |           1 |
|  6 | aten.relu.default                                 |                 12 |          12 |
|  7 | aten.t.default                                    |                  1 |           1 |
|  8 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 10, 10]> input = ?, Optional[Tensor]<[1024]> weight = ?, Optional[Tensor]<[1024]> bias = ?, Tensor<[1024]> running_mean = ?, Tensor<[1024]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  1 | [Tensor<[1, 1024, 19, 19]> input = ?, Optional[Tensor]<[1024]> weight = ?, Optional[Tensor]<[1024]> bias = ?, Tensor<[1024]> running_mean = ?, Tensor<[1024]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  2 | [Tensor<[1, 128, 150, 150]> input = ?, Optional[Tensor]<[128]> weight = ?, Optional[Tensor]<[128]> bias = ?, Tensor<[128]> running_mean = ?, Tensor<[128]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  3 | [Tensor<[1, 128, 75, 75]> input = ?, Optional[Tensor]<[128]> weight = ?, Optional[Tensor]<[128]> bias = ?, Tensor<[128]> running_mean = ?, Tensor<[128]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  4 | [Tensor<[1, 1536, 10, 10]> input = ?, Optional[Tensor]<[1536]> weight = ?, Optional[Tensor]<[1536]> bias = ?, Tensor<[1536]> running_mean = ?, Tensor<[1536]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  5 | [Tensor<[1, 2048, 10, 10]> input = ?, Optional[Tensor]<[2048]> weight = ?, Optional[Tensor]<[2048]> bias = ?, Tensor<[2048]> running_mean = ?, Tensor<[2048]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  6 | [Tensor<[1, 256, 38, 38]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  7 | [Tensor<[1, 256, 75, 75]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
|  8 | [Tensor<[1, 32, 150, 150]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
|  9 | [Tensor<[1, 64, 150, 150]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 0.001]         | Unknown  |
| 10 | [Tensor<[1, 728, 19, 19]> input = ?, Optional[Tensor]<[728]> weight = ?, Optional[Tensor]<[728]> bias = ?, Tensor<[728]> running_mean = ?, Tensor<[728]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 11 | [Tensor<[1, 728, 38, 38]> input = ?, Optional[Tensor]<[728]> weight = ?, Optional[Tensor]<[728]> bias = ?, Tensor<[728]> running_mean = ?, Tensor<[728]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 10, 10]> self = ?, Tensor<[1, 1024, 10, 10]> other = ?] | Done     |
|  1 | [Tensor<[1, 128, 75, 75]> self = ?, Tensor<[1, 128, 75, 75]> other = ?]   | Done     |
|  2 | [Tensor<[1, 256, 38, 38]> self = ?, Tensor<[1, 256, 38, 38]> other = ?]   | Done     |
|  3 | [Tensor<[1, 256, 75, 75]> self = ?, Tensor<[1, 256, 75, 75]> other = ?]   | Done     |
|  4 | [Tensor<[1, 728, 19, 19]> self = ?, Tensor<[1, 728, 19, 19]> other = ?]   | Done     |
|  5 | [Tensor<[1, 728, 38, 38]> self = ?, Tensor<[1, 728, 38, 38]> other = ?]   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 2048]> mat1 = ?, Tensor<[2048, 1000]> mat2 = ?] | Done     |
### aten.clone.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | [Tensor<[1, 2048]> self = ?] | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 10, 10]> input = ?, Tensor<[1024, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1024] | Unknown  |
|  1 | [Tensor<[1, 1024, 10, 10]> input = ?, Tensor<[1024, 1024, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  2 | [Tensor<[1, 1024, 10, 10]> input = ?, Tensor<[1536, 1024, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  3 | [Tensor<[1, 1024, 19, 19]> input = ?, Tensor<[1024, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1024] | Unknown  |
|  4 | [Tensor<[1, 128, 150, 150]> input = ?, Tensor<[128, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 128]  | Unknown  |
|  5 | [Tensor<[1, 128, 150, 150]> input = ?, Tensor<[128, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 128]  | Unknown  |
|  6 | [Tensor<[1, 128, 150, 150]> input = ?, Tensor<[128, 128, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]  | Unknown  |
|  7 | [Tensor<[1, 128, 75, 75]> input = ?, Tensor<[128, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 128]    | Unknown  |
|  8 | [Tensor<[1, 128, 75, 75]> input = ?, Tensor<[128, 128, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
|  9 | [Tensor<[1, 128, 75, 75]> input = ?, Tensor<[256, 128, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 10 | [Tensor<[1, 1536, 10, 10]> input = ?, Tensor<[1536, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1536] | Unknown  |
| 11 | [Tensor<[1, 1536, 10, 10]> input = ?, Tensor<[1536, 1536, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
| 12 | [Tensor<[1, 1536, 10, 10]> input = ?, Tensor<[2048, 1536, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
| 13 | [Tensor<[1, 256, 38, 38]> input = ?, Tensor<[256, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 256]    | Unknown  |
| 14 | [Tensor<[1, 256, 38, 38]> input = ?, Tensor<[256, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 15 | [Tensor<[1, 256, 38, 38]> input = ?, Tensor<[728, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 16 | [Tensor<[1, 256, 75, 75]> input = ?, Tensor<[256, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 256]    | Unknown  |
| 17 | [Tensor<[1, 256, 75, 75]> input = ?, Tensor<[256, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 256]    | Unknown  |
| 18 | [Tensor<[1, 256, 75, 75]> input = ?, Tensor<[256, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 19 | [Tensor<[1, 256, 75, 75]> input = ?, Tensor<[256, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 20 | [Tensor<[1, 3, 299, 299]> input = ?, Tensor<[32, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]       | Unknown  |
| 21 | [Tensor<[1, 32, 150, 150]> input = ?, Tensor<[64, 32, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 22 | [Tensor<[1, 64, 150, 150]> input = ?, Tensor<[128, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 23 | [Tensor<[1, 64, 150, 150]> input = ?, Tensor<[128, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 24 | [Tensor<[1, 64, 150, 150]> input = ?, Tensor<[64, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 64]     | Unknown  |
| 25 | [Tensor<[1, 728, 19, 19]> input = ?, Tensor<[1024, 728, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 26 | [Tensor<[1, 728, 19, 19]> input = ?, Tensor<[1024, 728, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 27 | [Tensor<[1, 728, 19, 19]> input = ?, Tensor<[728, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 728]    | Unknown  |
| 28 | [Tensor<[1, 728, 19, 19]> input = ?, Tensor<[728, 728, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 29 | [Tensor<[1, 728, 38, 38]> input = ?, Tensor<[728, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 728]    | Unknown  |
| 30 | [Tensor<[1, 728, 38, 38]> input = ?, Tensor<[728, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 728]    | Unknown  |
| 31 | [Tensor<[1, 728, 38, 38]> input = ?, Tensor<[728, 728, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 32 | [Tensor<[1, 728, 38, 38]> input = ?, Tensor<[728, 728, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 2048, 10, 10]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.relu.default
|    | ATen Input Variations                 | Status   |
|---:|:--------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 10, 10]> self = ?]  | Done     |
|  1 | [Tensor<[1, 1024, 19, 19]> self = ?]  | Done     |
|  2 | [Tensor<[1, 128, 150, 150]> self = ?] | Done     |
|  3 | [Tensor<[1, 128, 75, 75]> self = ?]   | Done     |
|  4 | [Tensor<[1, 1536, 10, 10]> self = ?]  | Done     |
|  5 | [Tensor<[1, 2048, 10, 10]> self = ?]  | Done     |
|  6 | [Tensor<[1, 256, 38, 38]> self = ?]   | Done     |
|  7 | [Tensor<[1, 256, 75, 75]> self = ?]   | Done     |
|  8 | [Tensor<[1, 32, 150, 150]> self = ?]  | Done     |
|  9 | [Tensor<[1, 64, 150, 150]> self = ?]  | Done     |
| 10 | [Tensor<[1, 728, 19, 19]> self = ?]   | Done     |
| 11 | [Tensor<[1, 728, 38, 38]> self = ?]   | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 2048]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 2048, 1, 1]> self = ?, List[int] size = [1, 2048]] | Unknown  |

