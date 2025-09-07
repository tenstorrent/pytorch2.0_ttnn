# High Level Operations Status
|    | Operations                                    |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.convolution.default                      |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  1 | aten.convolution_backward.default             |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.detach.default                           |                  3 |           0 |         3 |          0 | ✅          |       1 |
|  3 | aten.max_pool2d_with_indices.default          |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.max_pool2d_with_indices_backward.default |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.relu.default                             |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  6 | aten.threshold_backward.default               |                  3 |           0 |         0 |          0 | ✘           |       0 |
***
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                       | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999983 |      1 |
|  1 | Tensor<[1, 16, 14, 14]> input = ?,<br>Tensor<[16, 1, 2, 2]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = True,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999991 |      1 |
|  2 | Tensor<[1, 16, 14, 14]> input = ?,<br>Tensor<[4, 16, 3, 3]> weight = ?,<br>Optional[Tensor]<[4]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.99998  |      1 |
|  3 | Tensor<[1, 4, 7, 7]> input = ?,<br>Tensor<[4, 16, 2, 2]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = True,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999994 |      1 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                         | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 28, 28]> grad_output = ?,<br>Tensor<[1, 16, 14, 14]> input = ?,<br>Tensor<[16, 1, 2, 2]> weight = ?,<br>Optional[List[int]] bias_sizes = [1],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = True,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]   | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 16, 14, 14]> grad_output = ?,<br>Tensor<[1, 4, 7, 7]> input = ?,<br>Tensor<[4, 16, 2, 2]> weight = ?,<br>Optional[List[int]] bias_sizes = [16],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = True,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]    | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[1, 16, 28, 28]> grad_output = ?,<br>Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [16],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
|  3 | Tensor<[1, 4, 14, 14]> grad_output = ?,<br>Tensor<[1, 16, 14, 14]> input = ?,<br>Tensor<[4, 16, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [4],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]  | None     | Fallback   |     1 |      0 |
### aten.detach.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 14, 14]> self = ? | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 16, 28, 28]> self = ? | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 4, 14, 14]> self = ?  | Removed  | Done       |     1 |     -1 |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 28, 28]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2] | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 4, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | Fallback   |     1 |      0 |
### aten.max_pool2d_with_indices_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 14, 14]> grad_output = ?,<br>Tensor<[1, 16, 28, 28]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = False,<br>Tensor<[1, 16, 14, 14]> indices = ? | None     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 4, 7, 7]> grad_output = ?,<br>Tensor<[1, 4, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = False,<br>Tensor<[1, 4, 7, 7]> indices = ?        | None     | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 14, 14]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 28, 28]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 4, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
### aten.threshold_backward.default
|    | ATen Input Variations                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 14, 14]> grad_output = ?,<br>Tensor<[1, 16, 14, 14]> self = ?,<br>number threshold = 0 | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 16, 28, 28]> grad_output = ?,<br>Tensor<[1, 16, 28, 28]> self = ?,<br>number threshold = 0 | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 4, 14, 14]> grad_output = ?,<br>Tensor<[1, 4, 14, 14]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |

