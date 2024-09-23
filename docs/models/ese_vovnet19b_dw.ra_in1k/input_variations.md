# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 10 |          10 |
|  1 | aten.addmm.default                                |                  1 |           1 |
|  2 | aten.cat.default                                  |                  8 |           4 |
|  3 | aten.clone.default                                |                  1 |           1 |
|  4 | aten.convolution.default                          |                 25 |          25 |
|  5 | aten.hardsigmoid.default                          |                  4 |           4 |
|  6 | aten.max_pool2d_with_indices.default              |                  3 |           3 |
|  7 | aten.mean.dim                                     |                  5 |           5 |
|  8 | aten.mul.Tensor                                   |                  4 |           4 |
|  9 | aten.relu.default                                 |                 10 |          10 |
| 10 | aten.t.default                                    |                  1 |           1 |
| 11 | aten.view.default                                 |                  1 |           1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
|  1 | Tensor<[1, 128, 56, 56]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
|  2 | Tensor<[1, 160, 28, 28]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
|  3 | Tensor<[1, 192, 14, 14]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
|  4 | Tensor<[1, 224, 7, 7]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Done     |
|  5 | Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
|  6 | Tensor<[1, 512, 28, 28]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
|  7 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | Done     |
|  8 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
|  9 | Tensor<[1, 768, 14, 14]> input = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>Tensor<[768]> running_mean = ?,<br>Tensor<[768]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ? | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                                                                                       | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 256, 28, 28])', 'torch.Size([1, 160, 28, 28])', 'torch.Size([1, 160, 28, 28])', 'torch.Size([1, 160, 28, 28])'],<br>int<> dim = 1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 512, 14, 14])', 'torch.Size([1, 192, 14, 14])', 'torch.Size([1, 192, 14, 14])', 'torch.Size([1, 192, 14, 14])'],<br>int<> dim = 1 | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 64, 56, 56])', 'torch.Size([1, 128, 56, 56])', 'torch.Size([1, 128, 56, 56])', 'torch.Size([1, 128, 56, 56])'],<br>int<> dim = 1  | Unknown  |
|  3 | List[Tensor]<> tensors = ['torch.Size([1, 768, 7, 7])', 'torch.Size([1, 224, 7, 7])', 'torch.Size([1, 224, 7, 7])', 'torch.Size([1, 224, 7, 7])'],<br>int<> dim = 1         | Unknown  |
|  4 | List[Tensor]<> tensors = [Proxy(getitem_24), Proxy(ttnn_relu_9), Proxy(ttnn_relu_10), Proxy(ttnn_relu_11)],<br>int<> dim = 1                                                | Done     |
|  5 | List[Tensor]<> tensors = [Proxy(getitem_41), Proxy(ttnn_relu_14), Proxy(ttnn_relu_15), Proxy(ttnn_relu_16)],<br>int<> dim = 1                                               | Done     |
|  6 | List[Tensor]<> tensors = [Proxy(getitem_58), Proxy(ttnn_relu_19), Proxy(ttnn_relu_20), Proxy(ttnn_relu_21)],<br>int<> dim = 1                                               | Done     |
|  7 | List[Tensor]<> tensors = [Proxy(ttnn_relu_2), Proxy(ttnn_relu_4), Proxy(ttnn_relu_5), Proxy(ttnn_relu_6)],<br>int<> dim = 1                                                 | Done     |
### aten.clone.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[1, 1024]> self = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                           | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> input = ?,<br>Tensor<[1024, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  1 | Tensor<[1, 1088, 14, 14]> input = ?,<br>Tensor<[768, 1088, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
|  2 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 128        | Done     |
|  3 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  4 | Tensor<[1, 1440, 7, 7]> input = ?,<br>Tensor<[1024, 1440, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Done     |
|  5 | Tensor<[1, 160, 28, 28]> input = ?,<br>Tensor<[160, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 160        | Done     |
|  6 | Tensor<[1, 160, 28, 28]> input = ?,<br>Tensor<[160, 160, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  7 | Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 192        | Done     |
|  8 | Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[192, 192, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
|  9 | Tensor<[1, 224, 7, 7]> input = ?,<br>Tensor<[224, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 224          | Done     |
| 10 | Tensor<[1, 224, 7, 7]> input = ?,<br>Tensor<[224, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 11 | Tensor<[1, 256, 1, 1]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 12 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[160, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 13 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 14 | Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[256, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 15 | Tensor<[1, 512, 1, 1]> input = ?,<br>Tensor<[512, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 16 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[192, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 17 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 64         | Done     |
| 18 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 64         | Done     |
| 19 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 20 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
| 21 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1           | Done     |
| 22 | Tensor<[1, 736, 28, 28]> input = ?,<br>Tensor<[512, 736, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1        | Done     |
| 23 | Tensor<[1, 768, 1, 1]> input = ?,<br>Tensor<[768, 768, 1, 1]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 24 | Tensor<[1, 768, 7, 7]> input = ?,<br>Tensor<[224, 768, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1          | Done     |
### aten.hardsigmoid.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ? | Done     |
|  1 | Tensor<[1, 256, 1, 1]> self = ?  | Done     |
|  2 | Tensor<[1, 512, 1, 1]> self = ?  | Done     |
|  3 | Tensor<[1, 768, 1, 1]> self = ?  | Done     |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 256, 56, 56]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> ceil_mode = True | Done     |
|  1 | Tensor<[1, 512, 28, 28]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> ceil_mode = True | Done     |
|  2 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> ceil_mode = True | Done     |
### aten.mean.dim
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
|  1 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [2, 3],<br>bool<> keepdim = True   | Done     |
|  2 | Tensor<[1, 256, 56, 56]> self = ?,<br>Optional[List[int]]<> dim = [2, 3],<br>bool<> keepdim = True  | Done     |
|  3 | Tensor<[1, 512, 28, 28]> self = ?,<br>Optional[List[int]]<> dim = [2, 3],<br>bool<> keepdim = True  | Done     |
|  4 | Tensor<[1, 768, 14, 14]> self = ?,<br>Optional[List[int]]<> dim = [2, 3],<br>bool<> keepdim = True  | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     |
|  1 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ? | Done     |
|  2 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ? | Done     |
|  3 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ? | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?   | Done     |
|  1 | Tensor<[1, 128, 56, 56]> self = ?  | Done     |
|  2 | Tensor<[1, 160, 28, 28]> self = ?  | Done     |
|  3 | Tensor<[1, 192, 14, 14]> self = ?  | Done     |
|  4 | Tensor<[1, 224, 7, 7]> self = ?    | Done     |
|  5 | Tensor<[1, 256, 56, 56]> self = ?  | Done     |
|  6 | Tensor<[1, 512, 28, 28]> self = ?  | Done     |
|  7 | Tensor<[1, 64, 112, 112]> self = ? | Done     |
|  8 | Tensor<[1, 64, 56, 56]> self = ?   | Done     |
|  9 | Tensor<[1, 768, 14, 14]> self = ?  | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1024]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int]<> size = [1, 1024] | Done     |

