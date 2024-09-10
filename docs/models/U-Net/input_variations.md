# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |
|---:|:-------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_functional.default |                  5 |           0 |
|  1 | aten.add.Tensor                                  |                  1 |           1 |
|  2 | aten.cat.default                                 |                  4 |           0 |
|  3 | aten.convolution.default                         |                 19 |           0 |
|  4 | aten.max_pool2d_with_indices.default             |                  4 |           0 |
|  5 | aten.relu.default                                |                  5 |           5 |
|  6 | aten.sigmoid.default                             |                  1 |           1 |
***
### aten._native_batch_norm_legit_functional.default
|    | ATen Input Variations                                                                                                                                                                                                                                             | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 64, 64]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>bool<> training = True,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 256, 32, 32]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>bool<> training = True,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  2 | Tensor<[1, 32, 256, 256]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>bool<> training = True,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  3 | Tensor<[1, 512, 16, 16]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>bool<> training = True,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  4 | Tensor<[1, 64, 128, 128]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>bool<> training = True,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                      | Status   |
|---:|:-------------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>Tensor<> other = 1 | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 128, 64, 64])', 'torch.Size([1, 128, 64, 64])'],<br>int<> dim = 1   | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 256, 32, 32])', 'torch.Size([1, 256, 32, 32])'],<br>int<> dim = 1   | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 32, 256, 256])', 'torch.Size([1, 32, 256, 256])'],<br>int<> dim = 1 | Unknown  |
|  3 | List[Tensor]<> tensors = ['torch.Size([1, 64, 128, 128])', 'torch.Size([1, 64, 128, 128])'],<br>int<> dim = 1 | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Unknown  |
|  1 | Tensor<[1, 128, 32, 32]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  2 | Tensor<[1, 128, 64, 64]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  3 | Tensor<[1, 128, 64, 64]> input = ?,<br>Tensor<[128, 64, 2, 2]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = True,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  4 | Tensor<[1, 256, 16, 16]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  5 | Tensor<[1, 256, 32, 32]> input = ?,<br>Tensor<[256, 128, 2, 2]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = True,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
|  6 | Tensor<[1, 256, 32, 32]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  7 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[128, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
|  8 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Unknown  |
|  9 | Tensor<[1, 32, 128, 128]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 10 | Tensor<[1, 32, 256, 256]> input = ?,<br>Tensor<[1, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Unknown  |
| 11 | Tensor<[1, 32, 256, 256]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 12 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[512, 256, 2, 2]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = True,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
| 13 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 14 | Tensor<[1, 512, 32, 32]> input = ?,<br>Tensor<[256, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 15 | Tensor<[1, 64, 128, 128]> input = ?,<br>Tensor<[64, 32, 2, 2]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = True,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 16 | Tensor<[1, 64, 128, 128]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 17 | Tensor<[1, 64, 256, 256]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 18 | Tensor<[1, 64, 64, 64]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                   | Status   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 64, 64]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2]  | Unknown  |
|  1 | Tensor<[1, 256, 32, 32]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2]  | Unknown  |
|  2 | Tensor<[1, 32, 256, 256]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2] | Unknown  |
|  3 | Tensor<[1, 64, 128, 128]> self = ?,<br>List[int]<> kernel_size = [2, 2],<br>List[int]<> stride = [2, 2] | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 128, 64, 64]> self = ?  | Done     |
|  1 | Tensor<[1, 256, 32, 32]> self = ?  | Done     |
|  2 | Tensor<[1, 32, 256, 256]> self = ? | Done     |
|  3 | Tensor<[1, 512, 16, 16]> self = ?  | Done     |
|  4 | Tensor<[1, 64, 128, 128]> self = ? | Done     |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 1, 256, 256]> self = ? | Done     |

