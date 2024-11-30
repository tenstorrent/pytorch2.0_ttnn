# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |     1   |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  3 | aten.convolution.default                          |                 21 |          19 |         0 |          0 | 🚧          |     0.9 |
|  4 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  5 | aten.relu.default                                 |                  9 |           9 |         0 |          0 | ✅          |     1   |
|  6 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  7 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |     1   |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 168, 28, 28]> input = ?,<br>Optional[Tensor]<[168]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>Tensor<[168]> running_mean = ?,<br>Tensor<[168]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
|  1 | Tensor<[1, 168, 56, 56]> input = ?,<br>Optional[Tensor]<[168]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>Tensor<[168]> running_mean = ?,<br>Tensor<[168]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
|  2 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | True  |
|  3 | Tensor<[1, 408, 14, 14]> input = ?,<br>Optional[Tensor]<[408]> weight = ?,<br>Optional[Tensor]<[408]> bias = ?,<br>Tensor<[408]> running_mean = ?,<br>Tensor<[408]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
|  4 | Tensor<[1, 408, 28, 28]> input = ?,<br>Optional[Tensor]<[408]> weight = ?,<br>Optional[Tensor]<[408]> bias = ?,<br>Tensor<[408]> running_mean = ?,<br>Tensor<[408]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
|  5 | Tensor<[1, 72, 112, 112]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | True  |
|  6 | Tensor<[1, 72, 56, 56]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | True  |
|  7 | Tensor<[1, 912, 14, 14]> input = ?,<br>Optional[Tensor]<[912]> weight = ?,<br>Optional[Tensor]<[912]> bias = ?,<br>Tensor<[912]> running_mean = ?,<br>Tensor<[912]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
|  8 | Tensor<[1, 912, 7, 7]> input = ?,<br>Optional[Tensor]<[912]> weight = ?,<br>Optional[Tensor]<[912]> bias = ?,<br>Tensor<[912]> running_mean = ?,<br>Tensor<[912]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?   | Done     | Done       | True  |
|  3 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?     | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 912]> mat1 = ?,<br>Tensor<[912, 1000]> mat2 = ? | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 168, 28, 28]> input = ?,<br>Tensor<[168, 168, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  1 | Tensor<[1, 168, 28, 28]> input = ?,<br>Tensor<[168, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 7  | Done     | Done       | True  |
|  2 | Tensor<[1, 168, 28, 28]> input = ?,<br>Tensor<[408, 168, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  3 | Tensor<[1, 168, 28, 28]> input = ?,<br>Tensor<[408, 168, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  4 | Tensor<[1, 168, 56, 56]> input = ?,<br>Tensor<[168, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 7  | Done     | Done       | True  |
|  5 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | True  |
|  6 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[72, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | True  |
|  7 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[72, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | True  |
|  8 | Tensor<[1, 408, 14, 14]> input = ?,<br>Tensor<[408, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 17 | Done     | Done       | True  |
|  9 | Tensor<[1, 408, 14, 14]> input = ?,<br>Tensor<[408, 408, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
| 10 | Tensor<[1, 408, 14, 14]> input = ?,<br>Tensor<[912, 408, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
| 11 | Tensor<[1, 408, 14, 14]> input = ?,<br>Tensor<[912, 408, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
| 12 | Tensor<[1, 408, 28, 28]> input = ?,<br>Tensor<[408, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 17 | Done     | Done       | True  |
| 13 | Tensor<[1, 72, 112, 112]> input = ?,<br>Tensor<[72, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3  | Done     | Done       | True  |
| 14 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[168, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 15 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[168, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 16 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3    | Done     | Done       | True  |
| 17 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | True  |
| 18 | Tensor<[1, 912, 14, 14]> input = ?,<br>Tensor<[912, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 38 | Done     | Done       | True  |
| 19 | Tensor<[1, 912, 7, 7]> input = ?,<br>Tensor<[912, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 38   | Done     | Done       | True  |
| 20 | Tensor<[1, 912, 7, 7]> input = ?,<br>Tensor<[912, 912, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 912, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | True  |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 168, 28, 28]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[1, 168, 56, 56]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1, 32, 112, 112]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 408, 14, 14]> self = ?  | Done     | Done       | True  |
|  4 | Tensor<[1, 408, 28, 28]> self = ?  | Done     | Done       | True  |
|  5 | Tensor<[1, 72, 112, 112]> self = ? | Done     | Done       | True  |
|  6 | Tensor<[1, 72, 56, 56]> self = ?   | Done     | Done       | True  |
|  7 | Tensor<[1, 912, 14, 14]> self = ?  | Done     | Done       | True  |
|  8 | Tensor<[1, 912, 7, 7]> self = ?    | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 912]> self = ? | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 912, 1, 1]> self = ?,<br>List[int] size = [1, 912] | Done     | Done       | True  |

