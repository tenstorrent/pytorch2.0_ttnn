# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 20 |          20 |         0 |          0 | ✅          |       1 |
|  4 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.relu.default                                 |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  6 | aten.t.default                                    |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  7 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1344, 14, 14]> input = ?,<br>Optional[Tensor]<[1344]> weight = ?,<br>Optional[Tensor]<[1344]> bias = ?,<br>Tensor<[1344]> running_mean = ?,<br>Tensor<[1344]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |      0 |
|  1 | Tensor<[1, 1344, 28, 28]> input = ?,<br>Optional[Tensor]<[1344]> weight = ?,<br>Optional[Tensor]<[1344]> bias = ?,<br>Tensor<[1344]> running_mean = ?,<br>Tensor<[1344]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      0 |
|  2 | Tensor<[1, 2520, 14, 14]> input = ?,<br>Optional[Tensor]<[2520]> weight = ?,<br>Optional[Tensor]<[2520]> bias = ?,<br>Tensor<[2520]> running_mean = ?,<br>Tensor<[2520]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999991 |      0 |
|  3 | Tensor<[1, 2520, 7, 7]> input = ?,<br>Optional[Tensor]<[2520]> weight = ?,<br>Optional[Tensor]<[2520]> bias = ?,<br>Tensor<[2520]> running_mean = ?,<br>Tensor<[2520]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999985 |      0 |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999989 |      0 |
|  5 | Tensor<[1, 336, 112, 112]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999992 |      0 |
|  6 | Tensor<[1, 336, 56, 56]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      0 |
|  7 | Tensor<[1, 672, 28, 28]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999986 |      0 |
|  8 | Tensor<[1, 672, 56, 56]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999987 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2520]> mat1 = ?,<br>Tensor<[2520, 1000]> mat2 = ? | Done     | Done       | 0.999933 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1344, 14, 14]> input = ?,<br>Tensor<[1344, 1344, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999773 |      0 |
|  1 | Tensor<[1, 1344, 14, 14]> input = ?,<br>Tensor<[1344, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8  | Done     | Done       | 0.999745 |      0 |
|  2 | Tensor<[1, 1344, 14, 14]> input = ?,<br>Tensor<[2520, 1344, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999772 |      0 |
|  3 | Tensor<[1, 1344, 14, 14]> input = ?,<br>Tensor<[2520, 1344, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999776 |      0 |
|  4 | Tensor<[1, 1344, 28, 28]> input = ?,<br>Tensor<[1344, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8  | Done     | Done       | 0.999736 |      0 |
|  5 | Tensor<[1, 2520, 14, 14]> input = ?,<br>Tensor<[2520, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 15 | Done     | Done       | 0.999741 |      0 |
|  6 | Tensor<[1, 2520, 7, 7]> input = ?,<br>Tensor<[2520, 2520, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999485 |      0 |
|  7 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999981 |      0 |
|  8 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[336, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999991 |      0 |
|  9 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[336, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999991 |      0 |
| 10 | Tensor<[1, 336, 112, 112]> input = ?,<br>Tensor<[336, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2  | Done     | Done       | 0.999727 |      0 |
| 11 | Tensor<[1, 336, 56, 56]> input = ?,<br>Tensor<[336, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2    | Done     | Done       | 0.99973  |      0 |
| 12 | Tensor<[1, 336, 56, 56]> input = ?,<br>Tensor<[336, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999955 |      0 |
| 13 | Tensor<[1, 336, 56, 56]> input = ?,<br>Tensor<[672, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999955 |      0 |
| 14 | Tensor<[1, 336, 56, 56]> input = ?,<br>Tensor<[672, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999955 |      0 |
| 15 | Tensor<[1, 672, 28, 28]> input = ?,<br>Tensor<[1344, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999903 |      0 |
| 16 | Tensor<[1, 672, 28, 28]> input = ?,<br>Tensor<[1344, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999904 |      0 |
| 17 | Tensor<[1, 672, 28, 28]> input = ?,<br>Tensor<[672, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4    | Done     | Done       | 0.999736 |      0 |
| 18 | Tensor<[1, 672, 28, 28]> input = ?,<br>Tensor<[672, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999903 |      0 |
| 19 | Tensor<[1, 672, 56, 56]> input = ?,<br>Tensor<[672, 168, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4    | Done     | Done       | 0.999733 |      0 |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1344, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1344, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 2520, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 2520, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 32, 112, 112]> self = ?  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 336, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 336, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 672, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 672, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 2520]> self = ? | Removed  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2520, 1, 1]> self = ?,<br>List[int] size = [1, 2520] | Done     | Done       |     1 |      0 |

