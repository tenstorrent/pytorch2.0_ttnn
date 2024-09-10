# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 10 |           0 |
|  1 | aten.addmm.default                                |                  1 |           1 |
|  2 | aten.cat.default                                  |                  4 |           0 |
|  3 | aten.clone.default                                |                  1 |           1 |
|  4 | aten.convolution.default                          |                 25 |           0 |
|  5 | aten.hardsigmoid.default                          |                  4 |           0 |
|  6 | aten.max_pool2d_with_indices.default              |                  3 |           0 |
|  7 | aten.mean.dim                                     |                  5 |           5 |
|  8 | aten.mul.Tensor                                   |                  4 |           4 |
|  9 | aten.relu.default                                 |                 10 |          10 |
| 10 | aten.t.default                                    |                  1 |           1 |
| 11 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> input = ?, Optional[Tensor]<[1024]> weight = ?, Optional[Tensor]<[1024]> bias = ?, Tensor<[1024]> running_mean = ?, Tensor<[1024]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  1 | [Tensor<[1, 128, 56, 56]> input = ?, Optional[Tensor]<[128]> weight = ?, Optional[Tensor]<[128]> bias = ?, Tensor<[128]> running_mean = ?, Tensor<[128]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  2 | [Tensor<[1, 160, 28, 28]> input = ?, Optional[Tensor]<[160]> weight = ?, Optional[Tensor]<[160]> bias = ?, Tensor<[160]> running_mean = ?, Tensor<[160]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  3 | [Tensor<[1, 192, 14, 14]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  4 | [Tensor<[1, 224, 7, 7]> input = ?, Optional[Tensor]<[224]> weight = ?, Optional[Tensor]<[224]> bias = ?, Tensor<[224]> running_mean = ?, Tensor<[224]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
|  5 | [Tensor<[1, 256, 56, 56]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  6 | [Tensor<[1, 512, 28, 28]> input = ?, Optional[Tensor]<[512]> weight = ?, Optional[Tensor]<[512]> bias = ?, Tensor<[512]> running_mean = ?, Tensor<[512]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  7 | [Tensor<[1, 64, 112, 112]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 1e-05]       | Unknown  |
|  8 | [Tensor<[1, 64, 56, 56]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
|  9 | [Tensor<[1, 768, 14, 14]> input = ?, Optional[Tensor]<[768]> weight = ?, Optional[Tensor]<[768]> bias = ?, Tensor<[768]> running_mean = ?, Tensor<[768]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1024]> mat1 = ?, Tensor<[1024, 1000]> mat2 = ?] | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [List[Tensor] tensors = ['torch.Size([1, 256, 28, 28])', 'torch.Size([1, 160, 28, 28])', 'torch.Size([1, 160, 28, 28])', 'torch.Size([1, 160, 28, 28])'], int dim = 1] | Unknown  |
|  1 | [List[Tensor] tensors = ['torch.Size([1, 512, 14, 14])', 'torch.Size([1, 192, 14, 14])', 'torch.Size([1, 192, 14, 14])', 'torch.Size([1, 192, 14, 14])'], int dim = 1] | Unknown  |
|  2 | [List[Tensor] tensors = ['torch.Size([1, 64, 56, 56])', 'torch.Size([1, 128, 56, 56])', 'torch.Size([1, 128, 56, 56])', 'torch.Size([1, 128, 56, 56])'], int dim = 1]  | Unknown  |
|  3 | [List[Tensor] tensors = ['torch.Size([1, 768, 7, 7])', 'torch.Size([1, 224, 7, 7])', 'torch.Size([1, 224, 7, 7])', 'torch.Size([1, 224, 7, 7])'], int dim = 1]         | Unknown  |
### aten.clone.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | [Tensor<[1, 1024]> self = ?] | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 1, 1]> input = ?, Tensor<[1024, 1024, 1, 1]> weight = ?, Optional[Tensor]<[1024]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  1 | [Tensor<[1, 1088, 14, 14]> input = ?, Tensor<[768, 1088, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]        | Unknown  |
|  2 | [Tensor<[1, 128, 56, 56]> input = ?, Tensor<[128, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 128]          | Unknown  |
|  3 | [Tensor<[1, 128, 56, 56]> input = ?, Tensor<[128, 128, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
|  4 | [Tensor<[1, 1440, 7, 7]> input = ?, Tensor<[1024, 1440, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]         | Unknown  |
|  5 | [Tensor<[1, 160, 28, 28]> input = ?, Tensor<[160, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 160]          | Unknown  |
|  6 | [Tensor<[1, 160, 28, 28]> input = ?, Tensor<[160, 160, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
|  7 | [Tensor<[1, 192, 14, 14]> input = ?, Tensor<[192, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 192]          | Unknown  |
|  8 | [Tensor<[1, 192, 14, 14]> input = ?, Tensor<[192, 192, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
|  9 | [Tensor<[1, 224, 7, 7]> input = ?, Tensor<[224, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 224]            | Unknown  |
| 10 | [Tensor<[1, 224, 7, 7]> input = ?, Tensor<[224, 224, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 11 | [Tensor<[1, 256, 1, 1]> input = ?, Tensor<[256, 256, 1, 1]> weight = ?, Optional[Tensor]<[256]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 12 | [Tensor<[1, 256, 28, 28]> input = ?, Tensor<[160, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 13 | [Tensor<[1, 3, 224, 224]> input = ?, Tensor<[64, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 14 | [Tensor<[1, 448, 56, 56]> input = ?, Tensor<[256, 448, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 15 | [Tensor<[1, 512, 1, 1]> input = ?, Tensor<[512, 512, 1, 1]> weight = ?, Optional[Tensor]<[512]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 16 | [Tensor<[1, 512, 14, 14]> input = ?, Tensor<[192, 512, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 17 | [Tensor<[1, 64, 112, 112]> input = ?, Tensor<[64, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 64]           | Unknown  |
| 18 | [Tensor<[1, 64, 112, 112]> input = ?, Tensor<[64, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 64]           | Unknown  |
| 19 | [Tensor<[1, 64, 112, 112]> input = ?, Tensor<[64, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 20 | [Tensor<[1, 64, 56, 56]> input = ?, Tensor<[128, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 21 | [Tensor<[1, 64, 56, 56]> input = ?, Tensor<[64, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 22 | [Tensor<[1, 736, 28, 28]> input = ?, Tensor<[512, 736, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 23 | [Tensor<[1, 768, 1, 1]> input = ?, Tensor<[768, 768, 1, 1]> weight = ?, Optional[Tensor]<[768]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 24 | [Tensor<[1, 768, 7, 7]> input = ?, Tensor<[224, 768, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
### aten.hardsigmoid.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 1, 1]> self = ?] | Unknown  |
|  1 | [Tensor<[1, 256, 1, 1]> self = ?]  | Unknown  |
|  2 | [Tensor<[1, 512, 1, 1]> self = ?]  | Unknown  |
|  3 | [Tensor<[1, 768, 1, 1]> self = ?]  | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                                                          | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 256, 56, 56]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool ceil_mode = True] | Unknown  |
|  1 | [Tensor<[1, 512, 28, 28]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool ceil_mode = True] | Unknown  |
|  2 | [Tensor<[1, 768, 14, 14]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool ceil_mode = True] | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
|  1 | [Tensor<[1, 1024, 7, 7]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True]   | Done     |
|  2 | [Tensor<[1, 256, 56, 56]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True]  | Done     |
|  3 | [Tensor<[1, 512, 28, 28]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True]  | Done     |
|  4 | [Tensor<[1, 768, 14, 14]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True]  | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> self = ?, Tensor<[1, 1024, 1, 1]> other = ?] | Done     |
|  1 | [Tensor<[1, 256, 56, 56]> self = ?, Tensor<[1, 256, 1, 1]> other = ?] | Done     |
|  2 | [Tensor<[1, 512, 28, 28]> self = ?, Tensor<[1, 512, 1, 1]> other = ?] | Done     |
|  3 | [Tensor<[1, 768, 14, 14]> self = ?, Tensor<[1, 768, 1, 1]> other = ?] | Done     |
### aten.relu.default
|    | ATen Input Variations                | Status   |
|---:|:-------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> self = ?]   | Done     |
|  1 | [Tensor<[1, 128, 56, 56]> self = ?]  | Done     |
|  2 | [Tensor<[1, 160, 28, 28]> self = ?]  | Done     |
|  3 | [Tensor<[1, 192, 14, 14]> self = ?]  | Done     |
|  4 | [Tensor<[1, 224, 7, 7]> self = ?]    | Done     |
|  5 | [Tensor<[1, 256, 56, 56]> self = ?]  | Done     |
|  6 | [Tensor<[1, 512, 28, 28]> self = ?]  | Done     |
|  7 | [Tensor<[1, 64, 112, 112]> self = ?] | Done     |
|  8 | [Tensor<[1, 64, 56, 56]> self = ?]   | Done     |
|  9 | [Tensor<[1, 768, 14, 14]> self = ?]  | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1024]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 1, 1]> self = ?, List[int] size = [1, 1024]] | Unknown  |

