# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 13 |          13 |
|  1 | aten._to_copy.default                             |                  2 |           2 |
|  2 | aten._unsafe_index.Tensor                         |                  4 |           2 |
|  3 | aten.add.Tensor                                   |                  7 |           7 |
|  4 | aten.arange.default                               |                  2 |           2 |
|  5 | aten.cat.default                                  |                  4 |           2 |
|  6 | aten.convolution.default                          |                 23 |          23 |
|  7 | aten.leaky_relu.default                           |                 13 |          13 |
|  8 | aten.mul.Tensor                                   |                  2 |           2 |
|  9 | aten.unsqueeze.default                            |                  2 |           2 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05 | Done     |
|  1 | Tensor<[1, 128, 128, 128]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05    | Done     |
|  2 | Tensor<[1, 128, 32, 32]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05      | Done     |
|  3 | Tensor<[1, 128, 64, 64]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05      | Done     |
|  4 | Tensor<[1, 256, 16, 16]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05      | Done     |
|  5 | Tensor<[1, 256, 32, 32]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05      | Done     |
|  6 | Tensor<[1, 256, 64, 64]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05      | Done     |
|  7 | Tensor<[1, 32, 256, 256]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05         | Done     |
|  8 | Tensor<[1, 32, 512, 512]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05         | Done     |
|  9 | Tensor<[1, 512, 16, 16]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05      | Done     |
| 10 | Tensor<[1, 512, 32, 32]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05      | Done     |
| 11 | Tensor<[1, 64, 128, 128]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05         | Done     |
| 12 | Tensor<[1, 64, 256, 256]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.01,<br>float<> eps = 1e-05         | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[32]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Done     |
|  1 | Tensor<[64]> self = ?,<br>Optional[int]<> dtype = torch.int64 | Done     |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128, 32, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([64, 1])', 'torch.Size([64])']             | Unknown  |
|  1 | Tensor<[1, 128, 32, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default_1), Proxy(_to_copy_default_3)] | Done     |
|  2 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([32, 1])', 'torch.Size([32])']             | Unknown  |
|  3 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, Proxy(unsqueeze_default), Proxy(_to_copy_default_1)]   | Done     |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?   | Done     |
|  1 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ? | Done     |
|  2 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?     | Done     |
|  3 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?     | Done     |
|  4 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?   | Done     |
|  5 | Tensor<[32]> self = ?,<br>Tensor<> other = 0.0                               | Done     |
|  6 | Tensor<[64]> self = ?,<br>Tensor<> other = 0.0                               | Done     |
### aten.arange.default
|    | ATen Input Variations                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> end = 32,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
|  1 | number<> end = 64,<br>Optional[int]<> dtype = torch.float32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 128, 64, 64])', 'torch.Size([1, 256, 64, 64])'],<br>int<> dim = 1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 256, 32, 32])', 'torch.Size([1, 512, 32, 32])'],<br>int<> dim = 1 | Unknown  |
|  2 | List[Tensor]<> tensors = [Proxy(_unsafe_index_tensor), Proxy(ttnn_add_18)],<br>int<> dim = 1                | Done     |
|  3 | List[Tensor]<> tensors = [Proxy(_unsafe_index_tensor_1), Proxy(ttnn_add_10)],<br>int<> dim = 1              | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[255, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  1 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
|  2 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
|  3 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Done     |
|  4 | Tensor<[1, 128, 64, 64]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  5 | Tensor<[1, 256, 32, 32]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  6 | Tensor<[1, 256, 32, 32]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  7 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  8 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[255, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  9 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 10 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 11 | Tensor<[1, 32, 256, 256]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 12 | Tensor<[1, 32, 512, 512]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 13 | Tensor<[1, 384, 64, 64]> input = ?,<br>Tensor<[128, 384, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 14 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Done     |
| 15 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 16 | Tensor<[1, 512, 32, 32]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Done     |
| 17 | Tensor<[1, 512, 32, 32]> input = ?,<br>Tensor<[255, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 18 | Tensor<[1, 512, 32, 32]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 19 | Tensor<[1, 64, 128, 128]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 20 | Tensor<[1, 64, 256, 256]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 21 | Tensor<[1, 64, 256, 256]> input = ?,<br>Tensor<[32, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 22 | Tensor<[1, 768, 32, 32]> input = ?,<br>Tensor<[256, 768, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
### aten.leaky_relu.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 16, 16]> self = ?,<br>number<> negative_slope = 0.1  | Done     |
|  1 | Tensor<[1, 128, 128, 128]> self = ?,<br>number<> negative_slope = 0.1 | Done     |
|  2 | Tensor<[1, 128, 32, 32]> self = ?,<br>number<> negative_slope = 0.1   | Done     |
|  3 | Tensor<[1, 128, 64, 64]> self = ?,<br>number<> negative_slope = 0.1   | Done     |
|  4 | Tensor<[1, 256, 16, 16]> self = ?,<br>number<> negative_slope = 0.1   | Done     |
|  5 | Tensor<[1, 256, 32, 32]> self = ?,<br>number<> negative_slope = 0.1   | Done     |
|  6 | Tensor<[1, 256, 64, 64]> self = ?,<br>number<> negative_slope = 0.1   | Done     |
|  7 | Tensor<[1, 32, 256, 256]> self = ?,<br>number<> negative_slope = 0.1  | Done     |
|  8 | Tensor<[1, 32, 512, 512]> self = ?,<br>number<> negative_slope = 0.1  | Done     |
|  9 | Tensor<[1, 512, 16, 16]> self = ?,<br>number<> negative_slope = 0.1   | Done     |
| 10 | Tensor<[1, 512, 32, 32]> self = ?,<br>number<> negative_slope = 0.1   | Done     |
| 11 | Tensor<[1, 64, 128, 128]> self = ?,<br>number<> negative_slope = 0.1  | Done     |
| 12 | Tensor<[1, 64, 256, 256]> self = ?,<br>number<> negative_slope = 0.1  | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[32]> self = ?,<br>Tensor<> other = 0.5 | Done     |
|  1 | Tensor<[64]> self = ?,<br>Tensor<> other = 0.5 | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[32]> self = ?,<br>int<> dim = -1 | Done     |
|  1 | Tensor<[64]> self = ?,<br>int<> dim = -1 | Done     |

