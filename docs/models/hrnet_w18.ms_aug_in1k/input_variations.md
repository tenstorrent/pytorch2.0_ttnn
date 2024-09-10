# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 22 |           0 |
|  1 | aten._to_copy.default                             |                  3 |           0 |
|  2 | aten._unsafe_index.Tensor                         |                  6 |           0 |
|  3 | aten.add.Tensor                                   |                 12 |          12 |
|  4 | aten.addmm.default                                |                  1 |           1 |
|  5 | aten.arange.default                               |                  3 |           0 |
|  6 | aten.clone.default                                |                  1 |           1 |
|  7 | aten.convolution.default                          |                 47 |           0 |
|  8 | aten.mean.dim                                     |                  1 |           1 |
|  9 | aten.mul.Tensor                                   |                  6 |           6 |
| 10 | aten.relu.default                                 |                 19 |          19 |
| 11 | aten.t.default                                    |                  1 |           1 |
| 12 | aten.unsqueeze.default                            |                  3 |           0 |
| 13 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                 | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> input = ?, Optional[Tensor]<[1024]> weight = ?, Optional[Tensor]<[1024]> bias = ?, Tensor<[1024]> running_mean = ?, Tensor<[1024]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  1 | [Tensor<[1, 128, 14, 14]> input = ?, Optional[Tensor]<[128]> weight = ?, Optional[Tensor]<[128]> bias = ?, Tensor<[128]> running_mean = ?, Tensor<[128]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  2 | [Tensor<[1, 128, 56, 56]> input = ?, Optional[Tensor]<[128]> weight = ?, Optional[Tensor]<[128]> bias = ?, Tensor<[128]> running_mean = ?, Tensor<[128]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  3 | [Tensor<[1, 144, 7, 7]> input = ?, Optional[Tensor]<[144]> weight = ?, Optional[Tensor]<[144]> bias = ?, Tensor<[144]> running_mean = ?, Tensor<[144]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
|  4 | [Tensor<[1, 18, 14, 14]> input = ?, Optional[Tensor]<[18]> weight = ?, Optional[Tensor]<[18]> bias = ?, Tensor<[18]> running_mean = ?, Tensor<[18]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
|  5 | [Tensor<[1, 18, 28, 28]> input = ?, Optional[Tensor]<[18]> weight = ?, Optional[Tensor]<[18]> bias = ?, Tensor<[18]> running_mean = ?, Tensor<[18]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
|  6 | [Tensor<[1, 18, 56, 56]> input = ?, Optional[Tensor]<[18]> weight = ?, Optional[Tensor]<[18]> bias = ?, Tensor<[18]> running_mean = ?, Tensor<[18]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
|  7 | [Tensor<[1, 18, 7, 7]> input = ?, Optional[Tensor]<[18]> weight = ?, Optional[Tensor]<[18]> bias = ?, Tensor<[18]> running_mean = ?, Tensor<[18]> running_var = ?, float momentum = 0.1, float eps = 1e-05]           | Unknown  |
|  8 | [Tensor<[1, 2048, 7, 7]> input = ?, Optional[Tensor]<[2048]> weight = ?, Optional[Tensor]<[2048]> bias = ?, Tensor<[2048]> running_mean = ?, Tensor<[2048]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  9 | [Tensor<[1, 256, 28, 28]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
| 10 | [Tensor<[1, 256, 56, 56]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
| 11 | [Tensor<[1, 256, 7, 7]> input = ?, Optional[Tensor]<[256]> weight = ?, Optional[Tensor]<[256]> bias = ?, Tensor<[256]> running_mean = ?, Tensor<[256]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 12 | [Tensor<[1, 32, 56, 56]> input = ?, Optional[Tensor]<[32]> weight = ?, Optional[Tensor]<[32]> bias = ?, Tensor<[32]> running_mean = ?, Tensor<[32]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 13 | [Tensor<[1, 36, 14, 14]> input = ?, Optional[Tensor]<[36]> weight = ?, Optional[Tensor]<[36]> bias = ?, Tensor<[36]> running_mean = ?, Tensor<[36]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 14 | [Tensor<[1, 36, 28, 28]> input = ?, Optional[Tensor]<[36]> weight = ?, Optional[Tensor]<[36]> bias = ?, Tensor<[36]> running_mean = ?, Tensor<[36]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 15 | [Tensor<[1, 36, 7, 7]> input = ?, Optional[Tensor]<[36]> weight = ?, Optional[Tensor]<[36]> bias = ?, Tensor<[36]> running_mean = ?, Tensor<[36]> running_var = ?, float momentum = 0.1, float eps = 1e-05]           | Unknown  |
| 16 | [Tensor<[1, 512, 14, 14]> input = ?, Optional[Tensor]<[512]> weight = ?, Optional[Tensor]<[512]> bias = ?, Tensor<[512]> running_mean = ?, Tensor<[512]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
| 17 | [Tensor<[1, 64, 112, 112]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 1e-05]       | Unknown  |
| 18 | [Tensor<[1, 64, 28, 28]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 19 | [Tensor<[1, 64, 56, 56]> input = ?, Optional[Tensor]<[64]> weight = ?, Optional[Tensor]<[64]> bias = ?, Tensor<[64]> running_mean = ?, Tensor<[64]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 20 | [Tensor<[1, 72, 14, 14]> input = ?, Optional[Tensor]<[72]> weight = ?, Optional[Tensor]<[72]> bias = ?, Tensor<[72]> running_mean = ?, Tensor<[72]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 21 | [Tensor<[1, 72, 7, 7]> input = ?, Optional[Tensor]<[72]> weight = ?, Optional[Tensor]<[72]> bias = ?, Tensor<[72]> running_mean = ?, Tensor<[72]> running_var = ?, float momentum = 0.1, float eps = 1e-05]           | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | [Tensor<[14]> self = ?, Optional[int] dtype = torch.int64] | Unknown  |
|  1 | [Tensor<[28]> self = ?, Optional[int] dtype = torch.int64] | Unknown  |
|  2 | [Tensor<[56]> self = ?, Optional[int] dtype = torch.int64] | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                        | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 18, 14, 14]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])']] | Unknown  |
|  1 | [Tensor<[1, 18, 28, 28]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])']] | Unknown  |
|  2 | [Tensor<[1, 18, 7, 7]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])']]   | Unknown  |
|  3 | [Tensor<[1, 36, 14, 14]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([28, 1])', 'torch.Size([28])']] | Unknown  |
|  4 | [Tensor<[1, 36, 7, 7]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([28, 1])', 'torch.Size([28])']]   | Unknown  |
|  5 | [Tensor<[1, 72, 7, 7]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([14, 1])', 'torch.Size([14])']]   | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> self = ?, Tensor<[1, 1024, 7, 7]> other = ?]   | Done     |
|  1 | [Tensor<[1, 128, 56, 56]> self = ?, Tensor<[1, 128, 56, 56]> other = ?] | Done     |
|  2 | [Tensor<[1, 144, 7, 7]> self = ?, Tensor<[1, 144, 7, 7]> other = ?]     | Done     |
|  3 | [Tensor<[1, 18, 56, 56]> self = ?, Tensor<[1, 18, 56, 56]> other = ?]   | Done     |
|  4 | [Tensor<[1, 256, 28, 28]> self = ?, Tensor<[1, 256, 28, 28]> other = ?] | Done     |
|  5 | [Tensor<[1, 256, 56, 56]> self = ?, Tensor<[1, 256, 56, 56]> other = ?] | Done     |
|  6 | [Tensor<[1, 36, 28, 28]> self = ?, Tensor<[1, 36, 28, 28]> other = ?]   | Done     |
|  7 | [Tensor<[1, 512, 14, 14]> self = ?, Tensor<[1, 512, 14, 14]> other = ?] | Done     |
|  8 | [Tensor<[1, 72, 14, 14]> self = ?, Tensor<[1, 72, 14, 14]> other = ?]   | Done     |
|  9 | [Tensor<[14]> self = ?, Tensor other = 0.0]                             | Done     |
| 10 | [Tensor<[28]> self = ?, Tensor other = 0.0]                             | Done     |
| 11 | [Tensor<[56]> self = ?, Tensor other = 0.0]                             | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 2048]> mat1 = ?, Tensor<[2048, 1000]> mat2 = ?] | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [number end = 14, Optional[int] dtype = torch.float32, Optional[Device] device = cpu, Optional[bool] pin_memory = False] | Unknown  |
|  1 | [number end = 28, Optional[int] dtype = torch.float32, Optional[Device] device = cpu, Optional[bool] pin_memory = False] | Unknown  |
|  2 | [number end = 56, Optional[int] dtype = torch.float32, Optional[Device] device = cpu, Optional[bool] pin_memory = False] | Unknown  |
### aten.clone.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | [Tensor<[1, 2048]> self = ?] | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> input = ?, Tensor<[2048, 1024, 1, 1]> weight = ?, Optional[Tensor]<[2048]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
|  1 | [Tensor<[1, 128, 14, 14]> input = ?, Tensor<[128, 128, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
|  2 | [Tensor<[1, 128, 14, 14]> input = ?, Tensor<[512, 128, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
|  3 | [Tensor<[1, 128, 56, 56]> input = ?, Tensor<[256, 128, 3, 3]> weight = ?, Optional[Tensor]<[256]> bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  4 | [Tensor<[1, 144, 7, 7]> input = ?, Tensor<[1024, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
|  5 | [Tensor<[1, 144, 7, 7]> input = ?, Tensor<[144, 144, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
|  6 | [Tensor<[1, 144, 7, 7]> input = ?, Tensor<[18, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
|  7 | [Tensor<[1, 144, 7, 7]> input = ?, Tensor<[256, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
|  8 | [Tensor<[1, 144, 7, 7]> input = ?, Tensor<[36, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
|  9 | [Tensor<[1, 144, 7, 7]> input = ?, Tensor<[72, 144, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 10 | [Tensor<[1, 18, 14, 14]> input = ?, Tensor<[144, 18, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 11 | [Tensor<[1, 18, 28, 28]> input = ?, Tensor<[18, 18, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 12 | [Tensor<[1, 18, 28, 28]> input = ?, Tensor<[72, 18, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 13 | [Tensor<[1, 18, 56, 56]> input = ?, Tensor<[128, 18, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 14 | [Tensor<[1, 18, 56, 56]> input = ?, Tensor<[18, 18, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 15 | [Tensor<[1, 18, 56, 56]> input = ?, Tensor<[18, 18, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 16 | [Tensor<[1, 18, 56, 56]> input = ?, Tensor<[32, 18, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 17 | [Tensor<[1, 18, 56, 56]> input = ?, Tensor<[36, 18, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 18 | [Tensor<[1, 256, 28, 28]> input = ?, Tensor<[512, 256, 3, 3]> weight = ?, Optional[Tensor]<[512]> bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 19 | [Tensor<[1, 256, 56, 56]> input = ?, Tensor<[18, 256, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 20 | [Tensor<[1, 256, 56, 56]> input = ?, Tensor<[36, 256, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 21 | [Tensor<[1, 256, 56, 56]> input = ?, Tensor<[64, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 22 | [Tensor<[1, 256, 7, 7]> input = ?, Tensor<[1024, 256, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 23 | [Tensor<[1, 256, 7, 7]> input = ?, Tensor<[256, 256, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 24 | [Tensor<[1, 3, 224, 224]> input = ?, Tensor<[64, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 25 | [Tensor<[1, 32, 56, 56]> input = ?, Tensor<[128, 32, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 26 | [Tensor<[1, 32, 56, 56]> input = ?, Tensor<[32, 32, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 27 | [Tensor<[1, 36, 14, 14]> input = ?, Tensor<[144, 36, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 28 | [Tensor<[1, 36, 28, 28]> input = ?, Tensor<[18, 36, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 29 | [Tensor<[1, 36, 28, 28]> input = ?, Tensor<[256, 36, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 30 | [Tensor<[1, 36, 28, 28]> input = ?, Tensor<[36, 36, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 31 | [Tensor<[1, 36, 28, 28]> input = ?, Tensor<[36, 36, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 32 | [Tensor<[1, 36, 28, 28]> input = ?, Tensor<[64, 36, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 33 | [Tensor<[1, 36, 28, 28]> input = ?, Tensor<[72, 36, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 34 | [Tensor<[1, 512, 14, 14]> input = ?, Tensor<[1024, 512, 3, 3]> weight = ?, Optional[Tensor]<[1024]> bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
| 35 | [Tensor<[1, 64, 112, 112]> input = ?, Tensor<[64, 64, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 36 | [Tensor<[1, 64, 28, 28]> input = ?, Tensor<[256, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 37 | [Tensor<[1, 64, 28, 28]> input = ?, Tensor<[64, 64, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 38 | [Tensor<[1, 64, 56, 56]> input = ?, Tensor<[256, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 39 | [Tensor<[1, 64, 56, 56]> input = ?, Tensor<[64, 64, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 40 | [Tensor<[1, 64, 56, 56]> input = ?, Tensor<[64, 64, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 41 | [Tensor<[1, 72, 14, 14]> input = ?, Tensor<[128, 72, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 42 | [Tensor<[1, 72, 14, 14]> input = ?, Tensor<[144, 72, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 43 | [Tensor<[1, 72, 14, 14]> input = ?, Tensor<[18, 72, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 44 | [Tensor<[1, 72, 14, 14]> input = ?, Tensor<[36, 72, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
| 45 | [Tensor<[1, 72, 14, 14]> input = ?, Tensor<[512, 72, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 46 | [Tensor<[1, 72, 14, 14]> input = ?, Tensor<[72, 72, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]             | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 2048, 7, 7]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | [Tensor<[14]> self = ?, Tensor other = 0.5]   | Done     |
|  1 | [Tensor<[28]> self = ?, Tensor other = 0.25]  | Done     |
|  2 | [Tensor<[28]> self = ?, Tensor other = 0.5]   | Done     |
|  3 | [Tensor<[56]> self = ?, Tensor other = 0.125] | Done     |
|  4 | [Tensor<[56]> self = ?, Tensor other = 0.25]  | Done     |
|  5 | [Tensor<[56]> self = ?, Tensor other = 0.5]   | Done     |
### aten.relu.default
|    | ATen Input Variations                | Status   |
|---:|:-------------------------------------|:---------|
|  0 | [Tensor<[1, 1024, 7, 7]> self = ?]   | Done     |
|  1 | [Tensor<[1, 128, 14, 14]> self = ?]  | Done     |
|  2 | [Tensor<[1, 128, 56, 56]> self = ?]  | Done     |
|  3 | [Tensor<[1, 144, 7, 7]> self = ?]    | Done     |
|  4 | [Tensor<[1, 18, 14, 14]> self = ?]   | Done     |
|  5 | [Tensor<[1, 18, 28, 28]> self = ?]   | Done     |
|  6 | [Tensor<[1, 18, 56, 56]> self = ?]   | Done     |
|  7 | [Tensor<[1, 2048, 7, 7]> self = ?]   | Done     |
|  8 | [Tensor<[1, 256, 28, 28]> self = ?]  | Done     |
|  9 | [Tensor<[1, 256, 56, 56]> self = ?]  | Done     |
| 10 | [Tensor<[1, 256, 7, 7]> self = ?]    | Done     |
| 11 | [Tensor<[1, 32, 56, 56]> self = ?]   | Done     |
| 12 | [Tensor<[1, 36, 14, 14]> self = ?]   | Done     |
| 13 | [Tensor<[1, 36, 28, 28]> self = ?]   | Done     |
| 14 | [Tensor<[1, 512, 14, 14]> self = ?]  | Done     |
| 15 | [Tensor<[1, 64, 112, 112]> self = ?] | Done     |
| 16 | [Tensor<[1, 64, 28, 28]> self = ?]   | Done     |
| 17 | [Tensor<[1, 64, 56, 56]> self = ?]   | Done     |
| 18 | [Tensor<[1, 72, 14, 14]> self = ?]   | Done     |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 2048]> self = ?] | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                 | Status   |
|---:|:--------------------------------------|:---------|
|  0 | [Tensor<[14]> self = ?, int dim = -1] | Unknown  |
|  1 | [Tensor<[28]> self = ?, int dim = -1] | Unknown  |
|  2 | [Tensor<[56]> self = ?, int dim = -1] | Unknown  |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 2048, 1, 1]> self = ?, List[int] size = [1, 2048]] | Unknown  |

