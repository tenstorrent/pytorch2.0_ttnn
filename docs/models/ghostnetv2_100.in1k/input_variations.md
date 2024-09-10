# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 32 |           0 |
|  1 | aten._to_copy.default                             |                  4 |           0 |
|  2 | aten._unsafe_index.Tensor                         |                  8 |           0 |
|  3 | aten.add.Tensor                                   |                 10 |          10 |
|  4 | aten.addmm.default                                |                  1 |           1 |
|  5 | aten.arange.default                               |                  4 |           0 |
|  6 | aten.avg_pool2d.default                           |                  5 |           0 |
|  7 | aten.cat.default                                  |                 15 |           0 |
|  8 | aten.clone.default                                |                  1 |           1 |
|  9 | aten.convolution.default                          |                 87 |           0 |
| 10 | aten.hardsigmoid.default                          |                  5 |           0 |
| 11 | aten.mean.dim                                     |                  7 |           7 |
| 12 | aten.mul.Tensor                                   |                 18 |          18 |
| 13 | aten.relu.default                                 |                 18 |          18 |
| 14 | aten.sigmoid.default                              |                  8 |           8 |
| 15 | aten.slice.Tensor                                 |                 45 |           0 |
| 16 | aten.slice_scatter.default                        |                 18 |           0 |
| 17 | aten.t.default                                    |                  1 |           1 |
| 18 | aten.unsqueeze.default                            |                  4 |           0 |
| 19 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                              | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 100, 14, 14]> input = ?, Optional[Tensor]<[100]> weight = ?, Optional[Tensor]<[100]> bias = ?, Tensor<[100]> running_mean = ?, Tensor<[100]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  1 | [Tensor<[1, 112, 14, 14]> input = ?, Optional[Tensor]<[112]> weight = ?, Optional[Tensor]<[112]> bias = ?, Tensor<[112]> running_mean = ?, Tensor<[112]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  2 | [Tensor<[1, 112, 7, 7]> input = ?, Optional[Tensor]<[112]> weight = ?, Optional[Tensor]<[112]> bias = ?, Tensor<[112]> running_mean = ?, Tensor<[112]> running_var = ?, float momentum = 0.1, float eps = 1e-05]   | Unknown  |
|  3 | [Tensor<[1, 12, 56, 56]> input = ?, Optional[Tensor]<[12]> weight = ?, Optional[Tensor]<[12]> bias = ?, Tensor<[12]> running_mean = ?, Tensor<[12]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
|  4 | [Tensor<[1, 120, 14, 14]> input = ?, Optional[Tensor]<[120]> weight = ?, Optional[Tensor]<[120]> bias = ?, Tensor<[120]> running_mean = ?, Tensor<[120]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  5 | [Tensor<[1, 120, 28, 28]> input = ?, Optional[Tensor]<[120]> weight = ?, Optional[Tensor]<[120]> bias = ?, Tensor<[120]> running_mean = ?, Tensor<[120]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
|  6 | [Tensor<[1, 16, 112, 112]> input = ?, Optional[Tensor]<[16]> weight = ?, Optional[Tensor]<[16]> bias = ?, Tensor<[16]> running_mean = ?, Tensor<[16]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
|  7 | [Tensor<[1, 16, 56, 56]> input = ?, Optional[Tensor]<[16]> weight = ?, Optional[Tensor]<[16]> bias = ?, Tensor<[16]> running_mean = ?, Tensor<[16]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
|  8 | [Tensor<[1, 160, 7, 7]> input = ?, Optional[Tensor]<[160]> weight = ?, Optional[Tensor]<[160]> bias = ?, Tensor<[160]> running_mean = ?, Tensor<[160]> running_var = ?, float momentum = 0.1, float eps = 1e-05]   | Unknown  |
|  9 | [Tensor<[1, 184, 7, 7]> input = ?, Optional[Tensor]<[184]> weight = ?, Optional[Tensor]<[184]> bias = ?, Tensor<[184]> running_mean = ?, Tensor<[184]> running_var = ?, float momentum = 0.1, float eps = 1e-05]   | Unknown  |
| 10 | [Tensor<[1, 20, 28, 28]> input = ?, Optional[Tensor]<[20]> weight = ?, Optional[Tensor]<[20]> bias = ?, Tensor<[20]> running_mean = ?, Tensor<[20]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 11 | [Tensor<[1, 200, 7, 7]> input = ?, Optional[Tensor]<[200]> weight = ?, Optional[Tensor]<[200]> bias = ?, Tensor<[200]> running_mean = ?, Tensor<[200]> running_var = ?, float momentum = 0.1, float eps = 1e-05]   | Unknown  |
| 12 | [Tensor<[1, 24, 112, 112]> input = ?, Optional[Tensor]<[24]> weight = ?, Optional[Tensor]<[24]> bias = ?, Tensor<[24]> running_mean = ?, Tensor<[24]> running_var = ?, float momentum = 0.1, float eps = 1e-05]    | Unknown  |
| 13 | [Tensor<[1, 24, 28, 28]> input = ?, Optional[Tensor]<[24]> weight = ?, Optional[Tensor]<[24]> bias = ?, Tensor<[24]> running_mean = ?, Tensor<[24]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 14 | [Tensor<[1, 24, 56, 56]> input = ?, Optional[Tensor]<[24]> weight = ?, Optional[Tensor]<[24]> bias = ?, Tensor<[24]> running_mean = ?, Tensor<[24]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 15 | [Tensor<[1, 240, 14, 14]> input = ?, Optional[Tensor]<[240]> weight = ?, Optional[Tensor]<[240]> bias = ?, Tensor<[240]> running_mean = ?, Tensor<[240]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
| 16 | [Tensor<[1, 336, 14, 14]> input = ?, Optional[Tensor]<[336]> weight = ?, Optional[Tensor]<[336]> bias = ?, Tensor<[336]> running_mean = ?, Tensor<[336]> running_var = ?, float momentum = 0.1, float eps = 1e-05] | Unknown  |
| 17 | [Tensor<[1, 36, 56, 56]> input = ?, Optional[Tensor]<[36]> weight = ?, Optional[Tensor]<[36]> bias = ?, Tensor<[36]> running_mean = ?, Tensor<[36]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 18 | [Tensor<[1, 40, 14, 14]> input = ?, Optional[Tensor]<[40]> weight = ?, Optional[Tensor]<[40]> bias = ?, Tensor<[40]> running_mean = ?, Tensor<[40]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 19 | [Tensor<[1, 40, 28, 28]> input = ?, Optional[Tensor]<[40]> weight = ?, Optional[Tensor]<[40]> bias = ?, Tensor<[40]> running_mean = ?, Tensor<[40]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 20 | [Tensor<[1, 48, 56, 56]> input = ?, Optional[Tensor]<[48]> weight = ?, Optional[Tensor]<[48]> bias = ?, Tensor<[48]> running_mean = ?, Tensor<[48]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 21 | [Tensor<[1, 480, 7, 7]> input = ?, Optional[Tensor]<[480]> weight = ?, Optional[Tensor]<[480]> bias = ?, Tensor<[480]> running_mean = ?, Tensor<[480]> running_var = ?, float momentum = 0.1, float eps = 1e-05]   | Unknown  |
| 22 | [Tensor<[1, 56, 14, 14]> input = ?, Optional[Tensor]<[56]> weight = ?, Optional[Tensor]<[56]> bias = ?, Tensor<[56]> running_mean = ?, Tensor<[56]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 23 | [Tensor<[1, 60, 28, 28]> input = ?, Optional[Tensor]<[60]> weight = ?, Optional[Tensor]<[60]> bias = ?, Tensor<[60]> running_mean = ?, Tensor<[60]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 24 | [Tensor<[1, 672, 7, 7]> input = ?, Optional[Tensor]<[672]> weight = ?, Optional[Tensor]<[672]> bias = ?, Tensor<[672]> running_mean = ?, Tensor<[672]> running_var = ?, float momentum = 0.1, float eps = 1e-05]   | Unknown  |
| 25 | [Tensor<[1, 72, 28, 28]> input = ?, Optional[Tensor]<[72]> weight = ?, Optional[Tensor]<[72]> bias = ?, Tensor<[72]> running_mean = ?, Tensor<[72]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 26 | [Tensor<[1, 8, 112, 112]> input = ?, Optional[Tensor]<[8]> weight = ?, Optional[Tensor]<[8]> bias = ?, Tensor<[8]> running_mean = ?, Tensor<[8]> running_var = ?, float momentum = 0.1, float eps = 1e-05]         | Unknown  |
| 27 | [Tensor<[1, 80, 14, 14]> input = ?, Optional[Tensor]<[80]> weight = ?, Optional[Tensor]<[80]> bias = ?, Tensor<[80]> running_mean = ?, Tensor<[80]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 28 | [Tensor<[1, 80, 7, 7]> input = ?, Optional[Tensor]<[80]> weight = ?, Optional[Tensor]<[80]> bias = ?, Tensor<[80]> running_mean = ?, Tensor<[80]> running_var = ?, float momentum = 0.1, float eps = 1e-05]        | Unknown  |
| 29 | [Tensor<[1, 92, 14, 14]> input = ?, Optional[Tensor]<[92]> weight = ?, Optional[Tensor]<[92]> bias = ?, Tensor<[92]> running_mean = ?, Tensor<[92]> running_var = ?, float momentum = 0.1, float eps = 1e-05]      | Unknown  |
| 30 | [Tensor<[1, 960, 3, 3]> input = ?, Optional[Tensor]<[960]> weight = ?, Optional[Tensor]<[960]> bias = ?, Tensor<[960]> running_mean = ?, Tensor<[960]> running_var = ?, float momentum = 0.1, float eps = 1e-05]   | Unknown  |
| 31 | [Tensor<[1, 960, 7, 7]> input = ?, Optional[Tensor]<[960]> weight = ?, Optional[Tensor]<[960]> bias = ?, Tensor<[960]> running_mean = ?, Tensor<[960]> running_var = ?, float momentum = 0.1, float eps = 1e-05]   | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | [Tensor<[14]> self = ?, Optional[int] dtype = torch.int64] | Unknown  |
|  1 | [Tensor<[28]> self = ?, Optional[int] dtype = torch.int64] | Unknown  |
|  2 | [Tensor<[56]> self = ?, Optional[int] dtype = torch.int64] | Unknown  |
|  3 | [Tensor<[7]> self = ?, Optional[int] dtype = torch.int64]  | Unknown  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                         | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 120, 14, 14]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([28, 1])', 'torch.Size([28])']] | Unknown  |
|  1 | [Tensor<[1, 184, 7, 7]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([14, 1])', 'torch.Size([14])']]   | Unknown  |
|  2 | [Tensor<[1, 200, 7, 7]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([14, 1])', 'torch.Size([14])']]   | Unknown  |
|  3 | [Tensor<[1, 240, 14, 14]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([28, 1])', 'torch.Size([28])']] | Unknown  |
|  4 | [Tensor<[1, 480, 7, 7]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([14, 1])', 'torch.Size([14])']]   | Unknown  |
|  5 | [Tensor<[1, 672, 7, 7]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([14, 1])', 'torch.Size([14])']]   | Unknown  |
|  6 | [Tensor<[1, 72, 28, 28]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([56, 1])', 'torch.Size([56])']]  | Unknown  |
|  7 | [Tensor<[1, 960, 3, 3]> self = ?, List[Optional[Tensor]] indices = [None, None, 'torch.Size([7, 1])', 'torch.Size([7])']]     | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 14, 14]> self = ?, Tensor<[1, 112, 14, 14]> other = ?]   | Done     |
|  1 | [Tensor<[1, 16, 112, 112]> self = ?, Tensor<[1, 16, 112, 112]> other = ?] | Done     |
|  2 | [Tensor<[1, 160, 7, 7]> self = ?, Tensor<[1, 160, 7, 7]> other = ?]       | Done     |
|  3 | [Tensor<[1, 24, 56, 56]> self = ?, Tensor<[1, 24, 56, 56]> other = ?]     | Done     |
|  4 | [Tensor<[1, 40, 28, 28]> self = ?, Tensor<[1, 40, 28, 28]> other = ?]     | Done     |
|  5 | [Tensor<[1, 80, 14, 14]> self = ?, Tensor<[1, 80, 14, 14]> other = ?]     | Done     |
|  6 | [Tensor<[14]> self = ?, Tensor other = 0.0]                               | Done     |
|  7 | [Tensor<[28]> self = ?, Tensor other = 0.0]                               | Done     |
|  8 | [Tensor<[56]> self = ?, Tensor other = 0.0]                               | Done     |
|  9 | [Tensor<[7]> self = ?, Tensor other = 0.0]                                | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1000]> self = ?, Tensor<[1, 1280]> mat1 = ?, Tensor<[1280, 1000]> mat2 = ?] | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [number end = 14, Optional[int] dtype = torch.float32, Optional[Device] device = cpu, Optional[bool] pin_memory = False] | Unknown  |
|  1 | [number end = 28, Optional[int] dtype = torch.float32, Optional[Device] device = cpu, Optional[bool] pin_memory = False] | Unknown  |
|  2 | [number end = 56, Optional[int] dtype = torch.float32, Optional[Device] device = cpu, Optional[bool] pin_memory = False] | Unknown  |
|  3 | [number end = 7, Optional[int] dtype = torch.float32, Optional[Device] device = cpu, Optional[bool] pin_memory = False]  | Unknown  |
### aten.avg_pool2d.default
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 14, 14]> self = ?, List[int] kernel_size = [2, 2], List[int] stride = [2, 2]] | Unknown  |
|  1 | [Tensor<[1, 160, 7, 7]> self = ?, List[int] kernel_size = [2, 2], List[int] stride = [2, 2]]   | Unknown  |
|  2 | [Tensor<[1, 24, 56, 56]> self = ?, List[int] kernel_size = [2, 2], List[int] stride = [2, 2]]  | Unknown  |
|  3 | [Tensor<[1, 40, 28, 28]> self = ?, List[int] kernel_size = [2, 2], List[int] stride = [2, 2]]  | Unknown  |
|  4 | [Tensor<[1, 80, 14, 14]> self = ?, List[int] kernel_size = [2, 2], List[int] stride = [2, 2]]  | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|
|  0 | [List[Tensor] tensors = ['torch.Size([1, 100, 14, 14])', 'torch.Size([1, 100, 14, 14])'], int dim = 1]   | Unknown  |
|  1 | [List[Tensor] tensors = ['torch.Size([1, 12, 56, 56])', 'torch.Size([1, 12, 56, 56])'], int dim = 1]     | Unknown  |
|  2 | [List[Tensor] tensors = ['torch.Size([1, 120, 28, 28])', 'torch.Size([1, 120, 28, 28])'], int dim = 1]   | Unknown  |
|  3 | [List[Tensor] tensors = ['torch.Size([1, 20, 28, 28])', 'torch.Size([1, 20, 28, 28])'], int dim = 1]     | Unknown  |
|  4 | [List[Tensor] tensors = ['torch.Size([1, 24, 112, 112])', 'torch.Size([1, 24, 112, 112])'], int dim = 1] | Unknown  |
|  5 | [List[Tensor] tensors = ['torch.Size([1, 240, 14, 14])', 'torch.Size([1, 240, 14, 14])'], int dim = 1]   | Unknown  |
|  6 | [List[Tensor] tensors = ['torch.Size([1, 336, 14, 14])', 'torch.Size([1, 336, 14, 14])'], int dim = 1]   | Unknown  |
|  7 | [List[Tensor] tensors = ['torch.Size([1, 36, 56, 56])', 'torch.Size([1, 36, 56, 56])'], int dim = 1]     | Unknown  |
|  8 | [List[Tensor] tensors = ['torch.Size([1, 40, 14, 14])', 'torch.Size([1, 40, 14, 14])'], int dim = 1]     | Unknown  |
|  9 | [List[Tensor] tensors = ['torch.Size([1, 480, 7, 7])', 'torch.Size([1, 480, 7, 7])'], int dim = 1]       | Unknown  |
| 10 | [List[Tensor] tensors = ['torch.Size([1, 56, 14, 14])', 'torch.Size([1, 56, 14, 14])'], int dim = 1]     | Unknown  |
| 11 | [List[Tensor] tensors = ['torch.Size([1, 60, 28, 28])', 'torch.Size([1, 60, 28, 28])'], int dim = 1]     | Unknown  |
| 12 | [List[Tensor] tensors = ['torch.Size([1, 8, 112, 112])', 'torch.Size([1, 8, 112, 112])'], int dim = 1]   | Unknown  |
| 13 | [List[Tensor] tensors = ['torch.Size([1, 80, 7, 7])', 'torch.Size([1, 80, 7, 7])'], int dim = 1]         | Unknown  |
| 14 | [List[Tensor] tensors = ['torch.Size([1, 92, 14, 14])', 'torch.Size([1, 92, 14, 14])'], int dim = 1]     | Unknown  |
### aten.clone.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | [Tensor<[1, 1280]> self = ?] | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 100, 14, 14]> input = ?, Tensor<[100, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 100]        | Unknown  |
|  1 | [Tensor<[1, 112, 14, 14]> input = ?, Tensor<[112, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 112]        | Unknown  |
|  2 | [Tensor<[1, 112, 14, 14]> input = ?, Tensor<[336, 112, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]        | Unknown  |
|  3 | [Tensor<[1, 112, 7, 7]> input = ?, Tensor<[160, 112, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
|  4 | [Tensor<[1, 112, 7, 7]> input = ?, Tensor<[672, 112, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
|  5 | [Tensor<[1, 12, 56, 56]> input = ?, Tensor<[12, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 12]           | Unknown  |
|  6 | [Tensor<[1, 120, 1, 1]> input = ?, Tensor<[32, 120, 1, 1]> weight = ?, Optional[Tensor]<[32]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
|  7 | [Tensor<[1, 120, 1, 1]> input = ?, Tensor<[480, 120, 1, 1]> weight = ?, Optional[Tensor]<[480]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
|  8 | [Tensor<[1, 120, 14, 14]> input = ?, Tensor<[120, 1, 1, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 120]        | Unknown  |
|  9 | [Tensor<[1, 120, 14, 14]> input = ?, Tensor<[120, 1, 5, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 120]        | Unknown  |
| 10 | [Tensor<[1, 120, 28, 28]> input = ?, Tensor<[120, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 120]        | Unknown  |
| 11 | [Tensor<[1, 120, 28, 28]> input = ?, Tensor<[20, 120, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]         | Unknown  |
| 12 | [Tensor<[1, 16, 112, 112]> input = ?, Tensor<[16, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 16]         | Unknown  |
| 13 | [Tensor<[1, 16, 112, 112]> input = ?, Tensor<[24, 16, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]         | Unknown  |
| 14 | [Tensor<[1, 16, 112, 112]> input = ?, Tensor<[8, 16, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 15 | [Tensor<[1, 16, 56, 56]> input = ?, Tensor<[24, 16, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 16 | [Tensor<[1, 160, 3, 3]> input = ?, Tensor<[960, 160, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 17 | [Tensor<[1, 160, 7, 7]> input = ?, Tensor<[480, 160, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 18 | [Tensor<[1, 160, 7, 7]> input = ?, Tensor<[960, 160, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 19 | [Tensor<[1, 168, 1, 1]> input = ?, Tensor<[672, 168, 1, 1]> weight = ?, Optional[Tensor]<[672]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 20 | [Tensor<[1, 184, 14, 14]> input = ?, Tensor<[40, 184, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]         | Unknown  |
| 21 | [Tensor<[1, 184, 7, 7]> input = ?, Tensor<[184, 1, 1, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 184]          | Unknown  |
| 22 | [Tensor<[1, 184, 7, 7]> input = ?, Tensor<[184, 1, 5, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 184]          | Unknown  |
| 23 | [Tensor<[1, 20, 1, 1]> input = ?, Tensor<[72, 20, 1, 1]> weight = ?, Optional[Tensor]<[72]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]       | Unknown  |
| 24 | [Tensor<[1, 20, 28, 28]> input = ?, Tensor<[20, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 20]           | Unknown  |
| 25 | [Tensor<[1, 200, 14, 14]> input = ?, Tensor<[40, 200, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]         | Unknown  |
| 26 | [Tensor<[1, 200, 7, 7]> input = ?, Tensor<[200, 1, 1, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 200]          | Unknown  |
| 27 | [Tensor<[1, 200, 7, 7]> input = ?, Tensor<[200, 1, 5, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 200]          | Unknown  |
| 28 | [Tensor<[1, 24, 112, 112]> input = ?, Tensor<[24, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 24]         | Unknown  |
| 29 | [Tensor<[1, 24, 28, 28]> input = ?, Tensor<[40, 24, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 30 | [Tensor<[1, 24, 28, 28]> input = ?, Tensor<[72, 24, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 31 | [Tensor<[1, 24, 56, 56]> input = ?, Tensor<[24, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 24]           | Unknown  |
| 32 | [Tensor<[1, 24, 56, 56]> input = ?, Tensor<[36, 24, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 33 | [Tensor<[1, 240, 1, 1]> input = ?, Tensor<[960, 240, 1, 1]> weight = ?, Optional[Tensor]<[960]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 34 | [Tensor<[1, 240, 14, 14]> input = ?, Tensor<[240, 1, 1, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 240]        | Unknown  |
| 35 | [Tensor<[1, 240, 14, 14]> input = ?, Tensor<[240, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 240]        | Unknown  |
| 36 | [Tensor<[1, 240, 14, 14]> input = ?, Tensor<[240, 1, 5, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 240]        | Unknown  |
| 37 | [Tensor<[1, 240, 14, 14]> input = ?, Tensor<[40, 240, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]         | Unknown  |
| 38 | [Tensor<[1, 240, 28, 28]> input = ?, Tensor<[240, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 240]        | Unknown  |
| 39 | [Tensor<[1, 3, 224, 224]> input = ?, Tensor<[16, 3, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 40 | [Tensor<[1, 32, 1, 1]> input = ?, Tensor<[120, 32, 1, 1]> weight = ?, Optional[Tensor]<[120]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]     | Unknown  |
| 41 | [Tensor<[1, 336, 14, 14]> input = ?, Tensor<[336, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 336]        | Unknown  |
| 42 | [Tensor<[1, 36, 56, 56]> input = ?, Tensor<[36, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 36]           | Unknown  |
| 43 | [Tensor<[1, 40, 14, 14]> input = ?, Tensor<[120, 40, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 44 | [Tensor<[1, 40, 14, 14]> input = ?, Tensor<[240, 40, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 45 | [Tensor<[1, 40, 14, 14]> input = ?, Tensor<[40, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 40]           | Unknown  |
| 46 | [Tensor<[1, 40, 14, 14]> input = ?, Tensor<[80, 40, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 47 | [Tensor<[1, 40, 28, 28]> input = ?, Tensor<[120, 40, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 48 | [Tensor<[1, 40, 28, 28]> input = ?, Tensor<[40, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 40]           | Unknown  |
| 49 | [Tensor<[1, 40, 28, 28]> input = ?, Tensor<[60, 40, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 50 | [Tensor<[1, 48, 112, 112]> input = ?, Tensor<[48, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 48]         | Unknown  |
| 51 | [Tensor<[1, 48, 56, 56]> input = ?, Tensor<[12, 48, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 52 | [Tensor<[1, 480, 1, 1]> input = ?, Tensor<[120, 480, 1, 1]> weight = ?, Optional[Tensor]<[120]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 53 | [Tensor<[1, 480, 14, 14]> input = ?, Tensor<[56, 480, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]         | Unknown  |
| 54 | [Tensor<[1, 480, 7, 7]> input = ?, Tensor<[480, 1, 1, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 480]          | Unknown  |
| 55 | [Tensor<[1, 480, 7, 7]> input = ?, Tensor<[480, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 480]          | Unknown  |
| 56 | [Tensor<[1, 480, 7, 7]> input = ?, Tensor<[480, 1, 5, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 480]          | Unknown  |
| 57 | [Tensor<[1, 56, 14, 14]> input = ?, Tensor<[56, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 56]           | Unknown  |
| 58 | [Tensor<[1, 60, 28, 28]> input = ?, Tensor<[60, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 60]           | Unknown  |
| 59 | [Tensor<[1, 672, 1, 1]> input = ?, Tensor<[168, 672, 1, 1]> weight = ?, Optional[Tensor]<[168]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 60 | [Tensor<[1, 672, 14, 14]> input = ?, Tensor<[56, 672, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]         | Unknown  |
| 61 | [Tensor<[1, 672, 14, 14]> input = ?, Tensor<[672, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 672]        | Unknown  |
| 62 | [Tensor<[1, 672, 7, 7]> input = ?, Tensor<[672, 1, 1, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 672]          | Unknown  |
| 63 | [Tensor<[1, 672, 7, 7]> input = ?, Tensor<[672, 1, 5, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 672]          | Unknown  |
| 64 | [Tensor<[1, 672, 7, 7]> input = ?, Tensor<[80, 672, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 65 | [Tensor<[1, 72, 1, 1]> input = ?, Tensor<[20, 72, 1, 1]> weight = ?, Optional[Tensor]<[20]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]       | Unknown  |
| 66 | [Tensor<[1, 72, 28, 28]> input = ?, Tensor<[20, 72, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 67 | [Tensor<[1, 72, 28, 28]> input = ?, Tensor<[72, 1, 1, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 72]           | Unknown  |
| 68 | [Tensor<[1, 72, 28, 28]> input = ?, Tensor<[72, 1, 5, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 72]           | Unknown  |
| 69 | [Tensor<[1, 72, 56, 56]> input = ?, Tensor<[12, 72, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 70 | [Tensor<[1, 72, 56, 56]> input = ?, Tensor<[72, 1, 5, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [2, 2], List[int] padding = [2, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 72]           | Unknown  |
| 71 | [Tensor<[1, 8, 112, 112]> input = ?, Tensor<[8, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 8]            | Unknown  |
| 72 | [Tensor<[1, 80, 14, 14]> input = ?, Tensor<[100, 80, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 73 | [Tensor<[1, 80, 14, 14]> input = ?, Tensor<[112, 80, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 74 | [Tensor<[1, 80, 14, 14]> input = ?, Tensor<[240, 80, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]          | Unknown  |
| 75 | [Tensor<[1, 80, 14, 14]> input = ?, Tensor<[80, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 80]           | Unknown  |
| 76 | [Tensor<[1, 80, 14, 14]> input = ?, Tensor<[92, 80, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
| 77 | [Tensor<[1, 80, 7, 7]> input = ?, Tensor<[184, 80, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 78 | [Tensor<[1, 80, 7, 7]> input = ?, Tensor<[200, 80, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 79 | [Tensor<[1, 80, 7, 7]> input = ?, Tensor<[480, 80, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]            | Unknown  |
| 80 | [Tensor<[1, 80, 7, 7]> input = ?, Tensor<[80, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 80]             | Unknown  |
| 81 | [Tensor<[1, 92, 14, 14]> input = ?, Tensor<[92, 1, 3, 3]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [1, 1], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 92]           | Unknown  |
| 82 | [Tensor<[1, 960, 1, 1]> input = ?, Tensor<[1280, 960, 1, 1]> weight = ?, Optional[Tensor]<[1280]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1] | Unknown  |
| 83 | [Tensor<[1, 960, 1, 1]> input = ?, Tensor<[240, 960, 1, 1]> weight = ?, Optional[Tensor]<[240]> bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]   | Unknown  |
| 84 | [Tensor<[1, 960, 3, 3]> input = ?, Tensor<[960, 1, 1, 5]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 2], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 960]          | Unknown  |
| 85 | [Tensor<[1, 960, 3, 3]> input = ?, Tensor<[960, 1, 5, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [2, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 960]          | Unknown  |
| 86 | [Tensor<[1, 960, 7, 7]> input = ?, Tensor<[80, 960, 1, 1]> weight = ?, Optional[Tensor] bias = ?, List[int] stride = [1, 1], List[int] padding = [0, 0], List[int] dilation = [1, 1], bool transposed = False, List[int] output_padding = [0, 0], int groups = 1]           | Unknown  |
### aten.hardsigmoid.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | [Tensor<[1, 120, 1, 1]> self = ?] | Unknown  |
|  1 | [Tensor<[1, 480, 1, 1]> self = ?] | Unknown  |
|  2 | [Tensor<[1, 672, 1, 1]> self = ?] | Unknown  |
|  3 | [Tensor<[1, 72, 1, 1]> self = ?]  | Unknown  |
|  4 | [Tensor<[1, 960, 1, 1]> self = ?] | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 120, 28, 28]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True] | Done     |
|  1 | [Tensor<[1, 480, 14, 14]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True] | Done     |
|  2 | [Tensor<[1, 672, 14, 14]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True] | Done     |
|  3 | [Tensor<[1, 672, 7, 7]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True]   | Done     |
|  4 | [Tensor<[1, 72, 28, 28]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True]  | Done     |
|  5 | [Tensor<[1, 960, 7, 7]> self = ?, Optional[List[int]] dim = [-1, -2], bool keepdim = True] | Done     |
|  6 | [Tensor<[1, 960, 7, 7]> self = ?, Optional[List[int]] dim = [2, 3], bool keepdim = True]   | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 120, 28, 28]> self = ?, Tensor<[1, 120, 1, 1]> other = ?]   | Done     |
|  1 | [Tensor<[1, 120, 28, 28]> self = ?, Tensor<[1, 120, 28, 28]> other = ?] | Done     |
|  2 | [Tensor<[1, 184, 14, 14]> self = ?, Tensor<[1, 184, 14, 14]> other = ?] | Done     |
|  3 | [Tensor<[1, 200, 14, 14]> self = ?, Tensor<[1, 200, 14, 14]> other = ?] | Done     |
|  4 | [Tensor<[1, 240, 28, 28]> self = ?, Tensor<[1, 240, 28, 28]> other = ?] | Done     |
|  5 | [Tensor<[1, 480, 14, 14]> self = ?, Tensor<[1, 480, 1, 1]> other = ?]   | Done     |
|  6 | [Tensor<[1, 480, 14, 14]> self = ?, Tensor<[1, 480, 14, 14]> other = ?] | Done     |
|  7 | [Tensor<[1, 672, 14, 14]> self = ?, Tensor<[1, 672, 1, 1]> other = ?]   | Done     |
|  8 | [Tensor<[1, 672, 14, 14]> self = ?, Tensor<[1, 672, 14, 14]> other = ?] | Done     |
|  9 | [Tensor<[1, 672, 7, 7]> self = ?, Tensor<[1, 672, 1, 1]> other = ?]     | Done     |
| 10 | [Tensor<[1, 72, 28, 28]> self = ?, Tensor<[1, 72, 1, 1]> other = ?]     | Done     |
| 11 | [Tensor<[1, 72, 56, 56]> self = ?, Tensor<[1, 72, 56, 56]> other = ?]   | Done     |
| 12 | [Tensor<[1, 960, 7, 7]> self = ?, Tensor<[1, 960, 1, 1]> other = ?]     | Done     |
| 13 | [Tensor<[1, 960, 7, 7]> self = ?, Tensor<[1, 960, 7, 7]> other = ?]     | Done     |
| 14 | [Tensor<[14]> self = ?, Tensor other = 0.5]                             | Done     |
| 15 | [Tensor<[28]> self = ?, Tensor other = 0.5]                             | Done     |
| 16 | [Tensor<[56]> self = ?, Tensor other = 0.5]                             | Done     |
| 17 | [Tensor<[7]> self = ?, Tensor other = 0.42857142857142855]              | Done     |
### aten.relu.default
|    | ATen Input Variations                | Status   |
|---:|:-------------------------------------|:---------|
|  0 | [Tensor<[1, 100, 14, 14]> self = ?]  | Done     |
|  1 | [Tensor<[1, 120, 1, 1]> self = ?]    | Done     |
|  2 | [Tensor<[1, 120, 28, 28]> self = ?]  | Done     |
|  3 | [Tensor<[1, 1280, 1, 1]> self = ?]   | Done     |
|  4 | [Tensor<[1, 16, 112, 112]> self = ?] | Done     |
|  5 | [Tensor<[1, 168, 1, 1]> self = ?]    | Done     |
|  6 | [Tensor<[1, 20, 1, 1]> self = ?]     | Done     |
|  7 | [Tensor<[1, 24, 112, 112]> self = ?] | Done     |
|  8 | [Tensor<[1, 240, 1, 1]> self = ?]    | Done     |
|  9 | [Tensor<[1, 240, 14, 14]> self = ?]  | Done     |
| 10 | [Tensor<[1, 32, 1, 1]> self = ?]     | Done     |
| 11 | [Tensor<[1, 336, 14, 14]> self = ?]  | Done     |
| 12 | [Tensor<[1, 36, 56, 56]> self = ?]   | Done     |
| 13 | [Tensor<[1, 480, 7, 7]> self = ?]    | Done     |
| 14 | [Tensor<[1, 60, 28, 28]> self = ?]   | Done     |
| 15 | [Tensor<[1, 8, 112, 112]> self = ?]  | Done     |
| 16 | [Tensor<[1, 92, 14, 14]> self = ?]   | Done     |
| 17 | [Tensor<[1, 960, 7, 7]> self = ?]    | Done     |
### aten.sigmoid.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | [Tensor<[1, 120, 14, 14]> self = ?] | Done     |
|  1 | [Tensor<[1, 184, 7, 7]> self = ?]   | Done     |
|  2 | [Tensor<[1, 200, 7, 7]> self = ?]   | Done     |
|  3 | [Tensor<[1, 240, 14, 14]> self = ?] | Done     |
|  4 | [Tensor<[1, 480, 7, 7]> self = ?]   | Done     |
|  5 | [Tensor<[1, 672, 7, 7]> self = ?]   | Done     |
|  6 | [Tensor<[1, 72, 28, 28]> self = ?]  | Done     |
|  7 | [Tensor<[1, 960, 3, 3]> self = ?]   | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 14, 14]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
|  1 | [Tensor<[1, 112, 14, 14]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
|  2 | [Tensor<[1, 112, 14, 14]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
|  3 | [Tensor<[1, 120, 28, 28]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
|  4 | [Tensor<[1, 120, 28, 28]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
|  5 | [Tensor<[1, 120, 28, 28]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
|  6 | [Tensor<[1, 16, 112, 112]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
|  7 | [Tensor<[1, 16, 112, 112]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
|  8 | [Tensor<[1, 16, 112, 112]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
|  9 | [Tensor<[1, 160, 7, 7]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]    | Unknown  |
| 10 | [Tensor<[1, 160, 7, 7]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]    | Unknown  |
| 11 | [Tensor<[1, 160, 7, 7]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]    | Unknown  |
| 12 | [Tensor<[1, 184, 14, 14]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 13 | [Tensor<[1, 184, 14, 14]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 14 | [Tensor<[1, 184, 14, 14]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 15 | [Tensor<[1, 200, 14, 14]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 16 | [Tensor<[1, 200, 14, 14]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 17 | [Tensor<[1, 200, 14, 14]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 18 | [Tensor<[1, 24, 56, 56]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 19 | [Tensor<[1, 24, 56, 56]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 20 | [Tensor<[1, 24, 56, 56]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 21 | [Tensor<[1, 240, 28, 28]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 22 | [Tensor<[1, 240, 28, 28]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 23 | [Tensor<[1, 240, 28, 28]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 24 | [Tensor<[1, 40, 28, 28]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 25 | [Tensor<[1, 40, 28, 28]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 26 | [Tensor<[1, 40, 28, 28]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 27 | [Tensor<[1, 48, 112, 112]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
| 28 | [Tensor<[1, 48, 112, 112]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
| 29 | [Tensor<[1, 48, 112, 112]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
| 30 | [Tensor<[1, 480, 14, 14]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 31 | [Tensor<[1, 480, 14, 14]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 32 | [Tensor<[1, 480, 14, 14]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 33 | [Tensor<[1, 672, 14, 14]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 34 | [Tensor<[1, 672, 14, 14]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 35 | [Tensor<[1, 672, 14, 14]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]  | Unknown  |
| 36 | [Tensor<[1, 72, 56, 56]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 37 | [Tensor<[1, 72, 56, 56]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 38 | [Tensor<[1, 72, 56, 56]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 39 | [Tensor<[1, 80, 14, 14]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 40 | [Tensor<[1, 80, 14, 14]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 41 | [Tensor<[1, 80, 14, 14]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
| 42 | [Tensor<[1, 960, 7, 7]> self = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]    | Unknown  |
| 43 | [Tensor<[1, 960, 7, 7]> self = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]    | Unknown  |
| 44 | [Tensor<[1, 960, 7, 7]> self = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]    | Unknown  |
### aten.slice_scatter.default
|    | ATen Input Variations                                                                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 112, 14, 14]> self = ?, Tensor<[1, 112, 14, 14]> src = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
|  1 | [Tensor<[1, 112, 14, 14]> self = ?, Tensor<[1, 112, 14, 14]> src = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
|  2 | [Tensor<[1, 112, 14, 14]> self = ?, Tensor<[1, 112, 14, 14]> src = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]   | Unknown  |
|  3 | [Tensor<[1, 16, 112, 112]> self = ?, Tensor<[1, 16, 112, 112]> src = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
|  4 | [Tensor<[1, 16, 112, 112]> self = ?, Tensor<[1, 16, 112, 112]> src = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
|  5 | [Tensor<[1, 16, 112, 112]> self = ?, Tensor<[1, 16, 112, 112]> src = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1] | Unknown  |
|  6 | [Tensor<[1, 160, 7, 7]> self = ?, Tensor<[1, 160, 7, 7]> src = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]       | Unknown  |
|  7 | [Tensor<[1, 160, 7, 7]> self = ?, Tensor<[1, 160, 7, 7]> src = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]       | Unknown  |
|  8 | [Tensor<[1, 160, 7, 7]> self = ?, Tensor<[1, 160, 7, 7]> src = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]       | Unknown  |
|  9 | [Tensor<[1, 24, 56, 56]> self = ?, Tensor<[1, 24, 56, 56]> src = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
| 10 | [Tensor<[1, 24, 56, 56]> self = ?, Tensor<[1, 24, 56, 56]> src = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
| 11 | [Tensor<[1, 24, 56, 56]> self = ?, Tensor<[1, 24, 56, 56]> src = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
| 12 | [Tensor<[1, 40, 28, 28]> self = ?, Tensor<[1, 40, 28, 28]> src = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
| 13 | [Tensor<[1, 40, 28, 28]> self = ?, Tensor<[1, 40, 28, 28]> src = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
| 14 | [Tensor<[1, 40, 28, 28]> self = ?, Tensor<[1, 40, 28, 28]> src = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
| 15 | [Tensor<[1, 80, 14, 14]> self = ?, Tensor<[1, 80, 14, 14]> src = ?, int dim = 0, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
| 16 | [Tensor<[1, 80, 14, 14]> self = ?, Tensor<[1, 80, 14, 14]> src = ?, int dim = 2, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
| 17 | [Tensor<[1, 80, 14, 14]> self = ?, Tensor<[1, 80, 14, 14]> src = ?, int dim = 3, Optional[int] start = 0, Optional[int] end = -1]     | Unknown  |
### aten.t.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | [Tensor<[1000, 1280]> self = ?] | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                 | Status   |
|---:|:--------------------------------------|:---------|
|  0 | [Tensor<[14]> self = ?, int dim = -1] | Unknown  |
|  1 | [Tensor<[28]> self = ?, int dim = -1] | Unknown  |
|  2 | [Tensor<[56]> self = ?, int dim = -1] | Unknown  |
|  3 | [Tensor<[7]> self = ?, int dim = -1]  | Unknown  |
### aten.view.default
|    | ATen Input Variations                                          | Status   |
|---:|:---------------------------------------------------------------|:---------|
|  0 | [Tensor<[1, 1280, 1, 1]> self = ?, List[int] size = [1, 1280]] | Unknown  |

