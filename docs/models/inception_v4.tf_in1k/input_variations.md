# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 22 |           0 |
|  1 | aten.addmm.default                                |                  1 |           1 |
|  2 | aten.avg_pool2d.default                           |                  3 |           0 |
|  3 | aten.cat.default                                  |                  9 |           0 |
|  4 | aten.clone.default                                |                  1 |           1 |
|  5 | aten.convolution.default                          |                 38 |           0 |
|  6 | aten.max_pool2d_with_indices.default              |                  4 |           0 |
|  7 | aten.mean.dim                                     |                  1 |           1 |
|  8 | aten.relu.default                                 |                 22 |          22 |
|  9 | aten.t.default                                    |                  1 |           1 |
| 10 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                              | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 128, 17, 17]> input = ?, Optional[Tensor]<[128]> weight = ?, Optional[Tensor]<[128]> bias = ?, Tensor<[128]> running_mean = ?, Tensor<[128]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  1 | [Tensor<[1, 192, 17, 17]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  2 | [Tensor<[1, 192, 35, 35]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  3 | [Tensor<[1, 192, 8, 8]> input = ?, Optional[Tensor]<[192]> weight = ?, Optional[Tensor]<[192]> bias = ?, Tensor<[192]> running_mean = ?, Tensor<[192]> running_var = ?, float momentum = 0.1, float eps = 0.001]   | Unknown  |
|  4 | [Tensor<[1, 224, 17, 17]> input = ?, Optional[Tensor]<[224]> weight = ?, Optional[Tensor]<[224]> bias = ?, Tensor<[224]> running_mean = ?, Tensor<[224]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  5 | [Tensor<[1, 224, 35, 35]> input = ?, Optional[Tensor]<[224]> weight = ?, Optional[Tensor]<[224]> bias = ?, Tensor<[224]> running_mean = ?, Tensor<[224]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  6 | [Tensor<[1, 256, 17, 17]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
|  7 | [Tensor<[1, 256, 8, 8]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 0.001]   | Unknown  |
|  8 | [Tensor<[1, 32, 147, 147]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
|  9 | [Tensor<[1, 32, 149, 149]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
| 10 | [Tensor<[1, 320, 17, 17]> input = ?, Optional[Tensor]<[320]> weight = ?, Optional[Tensor]<[320]> bias = ?, Tensor<[320]> running_mean = ?, Tensor<[320]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
| 11 | [Tensor<[1, 320, 8, 8]> input = ?, Optional[Tensor]<[320]> weight = ?, Optional[Tensor]<[320]> bias = ?, Tensor<[320]> running_mean = ?, Tensor<[320]> running_var = ?, float momentum = 0.1, float eps = 0.001]   | Unknown  |
| 12 | [Tensor<[1, 384, 17, 17]> input = ?, Optional[Tensor]<[384]> weight = ?, Optional[Tensor]<[384]> bias = ?, Tensor<[384]> running_mean = ?, Tensor<[384]> running_var = ?, float momentum = 0.1, float eps = 0.001] | Unknown  |
| 13 | [Tensor<[1, 384, 8, 8]> input = ?, Optional[Tensor]<[384]> weight = ?, Optional[Tensor]<[384]> bias = ?, Tensor<[384]> running_mean = ?, Tensor<[384]> running_var = ?, float momentum = 0.1, float eps = 0.001]   | Unknown  |
| 14 | [Tensor<[1, 448, 8, 8]> input = ?, Optional[Tensor]<[448]> weight = ?, Optional[Tensor]<[448]> bias = ?, Tensor<[448]> running_mean = ?, Tensor<[448]> running_var = ?, float momentum = 0.1, float eps = 0.001]   | Unknown  |
| 15 | [Tensor<[1, 512, 8, 8]> input = ?, Optional[Tensor]<[512]> weight = ?, Optional[Tensor]<[512]> bias = ?, Tensor<[512]> running_mean = ?, Tensor<[512]> running_var = ?, float momentum = 0.1, float eps = 0.001]   | Unknown  |
| 16 | [Tensor<[1, 64, 147, 147]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 0.001]    | Unknown  |
| 17 | [Tensor<[1, 64, 35, 35]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 18 | [Tensor<[1, 64, 73, 73]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 19 | [Tensor<[1, 96, 35, 35]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 20 | [Tensor<[1, 96, 71, 71]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
| 21 | [Tensor<[1, 96, 73, 73]> input = ?, Optional[Tensor]<[96]> weight = ?, Optional[Tensor]<[96]> bias = ?, Tensor<[96]> running_mean = ?, Tensor<[96]> running_var = ?, float momentum = 0.1, float eps = 0.001]      | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1536]> mat1 = ?, Tensor<[1536, 1000]> mat2 = ?] | Done     |
### aten.avg_pool2d.default
|    | ATen Input Variations                                                                                                                                                               | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 17, 17]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [1, 1], List[int] padding = [1, 1], bool ceil_mode = False, bool count_include_pad = False] | Unknown  |
|  1 | [Tensor<[1, 1536, 8, 8]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [1, 1], List[int] padding = [1, 1], bool ceil_mode = False, bool count_include_pad = False]   | Unknown  |
|  2 | [Tensor<[1, 384, 35, 35]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [1, 1], List[int] padding = [1, 1], bool ceil_mode = False, bool count_include_pad = False]  | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [List[Tensor] tensors = ['torch.Size([1, 192, 35, 35])', 'torch.Size([1, 192, 35, 35])'], int dim = 1]                                                                 | Unknown  |
|  1 | [List[Tensor] tensors = ['torch.Size([1, 192, 8, 8])', 'torch.Size([1, 320, 8, 8])', 'torch.Size([1, 1024, 8, 8])'], int dim = 1]                                      | Unknown  |
|  2 | [List[Tensor] tensors = ['torch.Size([1, 256, 8, 8])', 'torch.Size([1, 256, 8, 8])'], int dim = 1]                                                                     | Unknown  |
|  3 | [List[Tensor] tensors = ['torch.Size([1, 256, 8, 8])', 'torch.Size([1, 512, 8, 8])', 'torch.Size([1, 512, 8, 8])', 'torch.Size([1, 256, 8, 8])'], int dim = 1]         | Unknown  |
|  4 | [List[Tensor] tensors = ['torch.Size([1, 384, 17, 17])', 'torch.Size([1, 256, 17, 17])', 'torch.Size([1, 256, 17, 17])', 'torch.Size([1, 128, 17, 17])'], int dim = 1] | Unknown  |
|  5 | [List[Tensor] tensors = ['torch.Size([1, 384, 17, 17])', 'torch.Size([1, 256, 17, 17])', 'torch.Size([1, 384, 17, 17])'], int dim = 1]                                 | Unknown  |
|  6 | [List[Tensor] tensors = ['torch.Size([1, 64, 73, 73])', 'torch.Size([1, 96, 73, 73])'], int dim = 1]                                                                   | Unknown  |
|  7 | [List[Tensor] tensors = ['torch.Size([1, 96, 35, 35])', 'torch.Size([1, 96, 35, 35])', 'torch.Size([1, 96, 35, 35])', 'torch.Size([1, 96, 35, 35])'], int dim = 1]     | Unknown  |
|  8 | [List[Tensor] tensors = ['torch.Size([1, 96, 71, 71])', 'torch.Size([1, 96, 71, 71])'], int dim = 1]                                                                   | Unknown  |
### aten.clone.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | [Tensor<[1, 1536]> self = ?] | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 17, 17]> input = ?, Tensor<[128, 1024, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  1 | [Tensor<[1, 1024, 17, 17]> input = ?, Tensor<[192, 1024, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  2 | [Tensor<[1, 1024, 17, 17]> input = ?, Tensor<[256, 1024, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  3 | [Tensor<[1, 1024, 17, 17]> input = ?, Tensor<[384, 1024, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  4 | [Tensor<[1, 1536, 8, 8]> input = ?, Tensor<[256, 1536, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  5 | [Tensor<[1, 1536, 8, 8]> input = ?, Tensor<[384, 1536, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  6 | [Tensor<[1, 160, 73, 73]> input = ?, Tensor<[64, 160, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
|  7 | [Tensor<[1, 192, 17, 17]> input = ?, Tensor<[192, 192, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  8 | [Tensor<[1, 192, 17, 17]> input = ?, Tensor<[192, 192, 7, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [3, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  9 | [Tensor<[1, 192, 17, 17]> input = ?, Tensor<[224, 192, 1, 7]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 3], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 10 | [Tensor<[1, 192, 35, 35]> input = ?, Tensor<[224, 192, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 11 | [Tensor<[1, 192, 71, 71]> input = ?, Tensor<[192, 192, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 12 | [Tensor<[1, 224, 17, 17]> input = ?, Tensor<[224, 224, 7, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [3, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 13 | [Tensor<[1, 224, 17, 17]> input = ?, Tensor<[256, 224, 1, 7]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 3], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 14 | [Tensor<[1, 224, 17, 17]> input = ?, Tensor<[256, 224, 7, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [3, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 15 | [Tensor<[1, 224, 35, 35]> input = ?, Tensor<[256, 224, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 16 | [Tensor<[1, 256, 17, 17]> input = ?, Tensor<[256, 256, 1, 7]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 3], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 17 | [Tensor<[1, 256, 17, 17]> input = ?, Tensor<[320, 256, 7, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [3, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 18 | [Tensor<[1, 3, 299, 299]> input = ?, Tensor<[32, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 19 | [Tensor<[1, 32, 147, 147]> input = ?, Tensor<[64, 32, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 20 | [Tensor<[1, 32, 149, 149]> input = ?, Tensor<[32, 32, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 21 | [Tensor<[1, 320, 17, 17]> input = ?, Tensor<[320, 320, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 22 | [Tensor<[1, 384, 35, 35]> input = ?, Tensor<[192, 384, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 23 | [Tensor<[1, 384, 35, 35]> input = ?, Tensor<[384, 384, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 24 | [Tensor<[1, 384, 35, 35]> input = ?, Tensor<[64, 384, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 25 | [Tensor<[1, 384, 35, 35]> input = ?, Tensor<[96, 384, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 26 | [Tensor<[1, 384, 8, 8]> input = ?, Tensor<[256, 384, 1, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 27 | [Tensor<[1, 384, 8, 8]> input = ?, Tensor<[256, 384, 3, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 28 | [Tensor<[1, 384, 8, 8]> input = ?, Tensor<[448, 384, 3, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 29 | [Tensor<[1, 448, 8, 8]> input = ?, Tensor<[512, 448, 1, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 30 | [Tensor<[1, 512, 8, 8]> input = ?, Tensor<[256, 512, 1, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 31 | [Tensor<[1, 512, 8, 8]> input = ?, Tensor<[256, 512, 3, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 32 | [Tensor<[1, 64, 147, 147]> input = ?, Tensor<[96, 64, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]    | Unknown  |
| 33 | [Tensor<[1, 64, 35, 35]> input = ?, Tensor<[96, 64, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 34 | [Tensor<[1, 64, 73, 73]> input = ?, Tensor<[64, 64, 1, 7]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 3], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 35 | [Tensor<[1, 64, 73, 73]> input = ?, Tensor<[64, 64, 7, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [3, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 36 | [Tensor<[1, 64, 73, 73]> input = ?, Tensor<[96, 64, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
| 37 | [Tensor<[1, 96, 35, 35]> input = ?, Tensor<[96, 96, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]      | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 17, 17]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [2, 2]] | Unknown  |
|  1 | [Tensor<[1, 192, 71, 71]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [2, 2]]  | Unknown  |
|  2 | [Tensor<[1, 384, 35, 35]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [2, 2]]  | Unknown  |
|  3 | [Tensor<[1, 64, 147, 147]> self = ?, List[int] kernel_size = [3, 3], List[int] stride = [2, 2]] | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1536, 8, 8]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.relu.default
|    | ATen Input Variations                | Status   |
|---:|:-------------------------------------|:---------|
|  0 | [Tensor<[1, 128, 17, 17]> self = ?]  | Done     |
|  1 | [Tensor<[1, 192, 17, 17]> self = ?]  | Done     |
|  2 | [Tensor<[1, 192, 35, 35]> self = ?]  | Done     |
|  3 | [Tensor<[1, 192, 8, 8]> self = ?]    | Done     |
|  4 | [Tensor<[1, 224, 17, 17]> self = ?]  | Done     |
|  5 | [Tensor<[1, 224, 35, 35]> self = ?]  | Done     |
|  6 | [Tensor<[1, 256, 17, 17]> self = ?]  | Done     |
|  7 | [Tensor<[1, 256, 8, 8]> self = ?]    | Done     |
|  8 | [Tensor<[1, 32, 147, 147]> self = ?] | Done     |
|  9 | [Tensor<[1, 32, 149, 149]> self = ?] | Done     |
| 10 | [Tensor<[1, 320, 17, 17]> self = ?]  | Done     |
| 11 | [Tensor<[1, 320, 8, 8]> self = ?]    | Done     |
| 12 | [Tensor<[1, 384, 17, 17]> self = ?]  | Done     |
| 13 | [Tensor<[1, 384, 8, 8]> self = ?]    | Done     |
| 14 | [Tensor<[1, 448, 8, 8]> self = ?]    | Done     |
| 15 | [Tensor<[1, 512, 8, 8]> self = ?]    | Done     |
| 16 | [Tensor<[1, 64, 147, 147]> self = ?] | Done     |
| 17 | [Tensor<[1, 64, 35, 35]> self = ?]   | Done     |
| 18 | [Tensor<[1, 64, 73, 73]> self = ?]   | Done     |
| 19 | [Tensor<[1, 96, 35, 35]> self = ?]   | Done     |
| 20 | [Tensor<[1, 96, 71, 71]> self = ?]   | Done     |
| 21 | [Tensor<[1, 96, 73, 73]> self = ?]   | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1536]> self = ?] | Done     |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1536, 1, 1]> self = ?, List[int] size = [1, 1536]] | Unknown  |

