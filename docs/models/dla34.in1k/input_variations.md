# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  6 |           0 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |
|  2 | aten.cat.default                                  |                  6 |           0 |
|  3 | aten.clone.default                                |                  1 |           1 |
|  4 | aten.convolution.default                          |                 22 |           0 |
|  5 | aten.max_pool2d_with_indices.default              |                  4 |           0 |
|  6 | aten.mean.dim                                     |                  1 |           1 |
|  7 | aten.relu.default                                 |                  6 |           6 |
|  8 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 28, 28]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 16, 224, 224]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  2 | Tensor<[1, 256, 14, 14]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  3 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  4 | Tensor<[1, 512, 7, 7]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05   | Unknown  |
|  5 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ? | Done     |
|  1 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ? | Done     |
|  2 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?     | Done     |
|  3 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?   | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 128, 28, 28])', 'torch.Size([1, 128, 28, 28])', 'torch.Size([1, 64, 28, 28])', 'torch.Size([1, 128, 28, 28])'],<br>int<> dim = 1  | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 128, 28, 28])', 'torch.Size([1, 128, 28, 28])'],<br>int<> dim = 1                                                                 | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 256, 14, 14])', 'torch.Size([1, 256, 14, 14])', 'torch.Size([1, 128, 14, 14])', 'torch.Size([1, 256, 14, 14])'],<br>int<> dim = 1 | Unknown  |
|  3 | List[Tensor]<> tensors = ['torch.Size([1, 256, 14, 14])', 'torch.Size([1, 256, 14, 14])'],<br>int<> dim = 1                                                                 | Unknown  |
|  4 | List[Tensor]<> tensors = ['torch.Size([1, 512, 7, 7])', 'torch.Size([1, 512, 7, 7])', 'torch.Size([1, 256, 7, 7])'],<br>int<> dim = 1                                       | Unknown  |
|  5 | List[Tensor]<> tensors = ['torch.Size([1, 64, 56, 56])', 'torch.Size([1, 64, 56, 56])'],<br>int<> dim = 1                                                                   | Unknown  |
### aten.clone.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 512, 1, 1]> self = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  1 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  2 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  3 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
|  4 | Tensor<[1, 1280, 7, 7]> input = ?,<br>Tensor<[512, 1280, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  5 | Tensor<[1, 16, 224, 224]> input = ?,<br>Tensor<[16, 16, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
|  6 | Tensor<[1, 16, 224, 224]> input = ?,<br>Tensor<[32, 16, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
|  7 | Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  8 | Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  9 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 10 | Tensor<[1, 256, 7, 7]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 11 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[16, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [3, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 12 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 13 | Tensor<[1, 32, 56, 56]> input = ?,<br>Tensor<[64, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 14 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[128, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 15 | Tensor<[1, 512, 1, 1]> input = ?,<br>Tensor<[1000, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[1000]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
| 16 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 17 | Tensor<[1, 512, 7, 7]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 18 | Tensor<[1, 64, 28, 28]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 19 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
| 20 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 21 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[256, 896, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 28, 28]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2]  | Unknown  |
|  1 | Tensor<[1, 256, 14, 14]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2]  | Unknown  |
|  2 | Tensor<[1, 32, 112, 112]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2] | Unknown  |
|  3 | Tensor<[1, 64, 56, 56]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2]   | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 128, 28, 28]> self = ?  | Done     |
|  1 | Tensor<[1, 16, 224, 224]> self = ? | Done     |
|  2 | Tensor<[1, 256, 14, 14]> self = ?  | Done     |
|  3 | Tensor<[1, 32, 112, 112]> self = ? | Done     |
|  4 | Tensor<[1, 512, 7, 7]> self = ?    | Done     |
|  5 | Tensor<[1, 64, 56, 56]> self = ?   | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1000, 1, 1]> self = ?,<br>List[int]<> size = [1, 1000] | Unknown  |

