# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.convolution.default                          |                 34 |          32 |         0 |          0 | 🚧          |    0.94 |
|  4 | aten.mean.dim                                     |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  6 | aten.relu.default                                 |                 13 |          13 |         0 |          0 | ✅          |    1    |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  8 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1392, 14, 14]> input = ?,<br>Optional[Tensor]<[1392]> weight = ?,<br>Optional[Tensor]<[1392]> bias = ?,<br>Tensor<[1392]> running_mean = ?,<br>Tensor<[1392]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999985 |      5 |
|  1 | Tensor<[1, 1392, 28, 28]> input = ?,<br>Optional[Tensor]<[1392]> weight = ?,<br>Optional[Tensor]<[1392]> bias = ?,<br>Tensor<[1392]> running_mean = ?,<br>Tensor<[1392]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999988 |      5 |
|  2 | Tensor<[1, 232, 112, 112]> input = ?,<br>Optional[Tensor]<[232]> weight = ?,<br>Optional[Tensor]<[232]> bias = ?,<br>Tensor<[232]> running_mean = ?,<br>Tensor<[232]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999987 |      5 |
|  3 | Tensor<[1, 232, 56, 56]> input = ?,<br>Optional[Tensor]<[232]> weight = ?,<br>Optional[Tensor]<[232]> bias = ?,<br>Tensor<[232]> running_mean = ?,<br>Tensor<[232]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999989 |      5 |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999989 |      5 |
|  5 | Tensor<[1, 3712, 14, 14]> input = ?,<br>Optional[Tensor]<[3712]> weight = ?,<br>Optional[Tensor]<[3712]> bias = ?,<br>Tensor<[3712]> running_mean = ?,<br>Tensor<[3712]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999991 |      5 |
|  6 | Tensor<[1, 3712, 7, 7]> input = ?,<br>Optional[Tensor]<[3712]> weight = ?,<br>Optional[Tensor]<[3712]> bias = ?,<br>Tensor<[3712]> running_mean = ?,<br>Tensor<[3712]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999987 |      5 |
|  7 | Tensor<[1, 696, 28, 28]> input = ?,<br>Optional[Tensor]<[696]> weight = ?,<br>Optional[Tensor]<[696]> bias = ?,<br>Tensor<[696]> running_mean = ?,<br>Tensor<[696]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999986 |      5 |
|  8 | Tensor<[1, 696, 56, 56]> input = ?,<br>Optional[Tensor]<[696]> weight = ?,<br>Optional[Tensor]<[696]> bias = ?,<br>Tensor<[696]> running_mean = ?,<br>Tensor<[696]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999989 |      5 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 3712]> mat1 = ?,<br>Tensor<[3712, 1000]> mat2 = ? | Done     | Done       | 0.999938 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1392, 1, 1]> input = ?,<br>Tensor<[174, 1392, 1, 1]> weight = ?,<br>Optional[Tensor]<[174]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999798 |      6 |
|  1 | Tensor<[1, 1392, 1, 1]> input = ?,<br>Tensor<[348, 1392, 1, 1]> weight = ?,<br>Optional[Tensor]<[348]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999741 |      6 |
|  2 | Tensor<[1, 1392, 14, 14]> input = ?,<br>Tensor<[1392, 1392, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999964 |      4 |
|  3 | Tensor<[1, 1392, 14, 14]> input = ?,<br>Tensor<[1392, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6      | Done     | Done       | 0.999616 |      4 |
|  4 | Tensor<[1, 1392, 14, 14]> input = ?,<br>Tensor<[3712, 1392, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999964 |      4 |
|  5 | Tensor<[1, 1392, 14, 14]> input = ?,<br>Tensor<[3712, 1392, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999763 |      4 |
|  6 | Tensor<[1, 1392, 28, 28]> input = ?,<br>Tensor<[1392, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6      | Done     | Done       | 0.999602 |      4 |
|  7 | Tensor<[1, 174, 1, 1]> input = ?,<br>Tensor<[1392, 174, 1, 1]> weight = ?,<br>Optional[Tensor]<[1392]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999976 |      6 |
|  8 | Tensor<[1, 174, 1, 1]> input = ?,<br>Tensor<[696, 174, 1, 1]> weight = ?,<br>Optional[Tensor]<[696]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999976 |      6 |
|  9 | Tensor<[1, 232, 1, 1]> input = ?,<br>Tensor<[58, 232, 1, 1]> weight = ?,<br>Optional[Tensor]<[58]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999969 |      6 |
| 10 | Tensor<[1, 232, 1, 1]> input = ?,<br>Tensor<[8, 232, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999936 |      6 |
| 11 | Tensor<[1, 232, 112, 112]> input = ?,<br>Tensor<[232, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Fallback   | 1        |     -1 |
| 12 | Tensor<[1, 232, 56, 56]> input = ?,<br>Tensor<[232, 232, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999977 |      4 |
| 13 | Tensor<[1, 232, 56, 56]> input = ?,<br>Tensor<[232, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | Fallback   | 1        |     -1 |
| 14 | Tensor<[1, 232, 56, 56]> input = ?,<br>Tensor<[696, 232, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999981 |      4 |
| 15 | Tensor<[1, 232, 56, 56]> input = ?,<br>Tensor<[696, 232, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999967 |      4 |
| 16 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999981 |      4 |
| 17 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[232, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999991 |      4 |
| 18 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[232, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999991 |      4 |
| 19 | Tensor<[1, 348, 1, 1]> input = ?,<br>Tensor<[1392, 348, 1, 1]> weight = ?,<br>Optional[Tensor]<[1392]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999952 |      6 |
| 20 | Tensor<[1, 348, 1, 1]> input = ?,<br>Tensor<[3712, 348, 1, 1]> weight = ?,<br>Optional[Tensor]<[3712]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999951 |      6 |
| 21 | Tensor<[1, 3712, 1, 1]> input = ?,<br>Tensor<[348, 3712, 1, 1]> weight = ?,<br>Optional[Tensor]<[348]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.99927  |      6 |
| 22 | Tensor<[1, 3712, 14, 14]> input = ?,<br>Tensor<[3712, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16     | Done     | Done       | 0.999609 |      4 |
| 23 | Tensor<[1, 3712, 7, 7]> input = ?,<br>Tensor<[3712, 3712, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999938 |      4 |
| 24 | Tensor<[1, 58, 1, 1]> input = ?,<br>Tensor<[232, 58, 1, 1]> weight = ?,<br>Optional[Tensor]<[232]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999984 |      6 |
| 25 | Tensor<[1, 58, 1, 1]> input = ?,<br>Tensor<[696, 58, 1, 1]> weight = ?,<br>Optional[Tensor]<[696]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999985 |      6 |
| 26 | Tensor<[1, 696, 1, 1]> input = ?,<br>Tensor<[174, 696, 1, 1]> weight = ?,<br>Optional[Tensor]<[174]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999913 |      6 |
| 27 | Tensor<[1, 696, 1, 1]> input = ?,<br>Tensor<[58, 696, 1, 1]> weight = ?,<br>Optional[Tensor]<[58]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999917 |      6 |
| 28 | Tensor<[1, 696, 28, 28]> input = ?,<br>Tensor<[1392, 696, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999969 |      4 |
| 29 | Tensor<[1, 696, 28, 28]> input = ?,<br>Tensor<[1392, 696, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999898 |      4 |
| 30 | Tensor<[1, 696, 28, 28]> input = ?,<br>Tensor<[696, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3        | Done     | Done       | 0.999598 |      4 |
| 31 | Tensor<[1, 696, 28, 28]> input = ?,<br>Tensor<[696, 696, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999969 |      4 |
| 32 | Tensor<[1, 696, 56, 56]> input = ?,<br>Tensor<[696, 232, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3        | Done     | Done       | 0.999591 |      4 |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[232, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[232]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999994 |      6 |
### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   | Isolated   |       PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|----------:|-------:|
|  0 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.157935  |      0 |
|  1 | Tensor<[1, 232, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.183148  |      0 |
|  2 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.128447  |      0 |
|  3 | Tensor<[1, 696, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.0640837 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?   | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1392, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1392, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 174, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 232, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 232, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 32, 112, 112]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 348, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 3712, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 3712, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 58, 1, 1]> self = ?      | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 696, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 696, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 8, 1, 1]> self = ?       | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1392, 1, 1]> self = ? | Done     | Done       | 0.999744 |      0 |
|  1 | Tensor<[1, 232, 1, 1]> self = ?  | Done     | Done       | 0.999764 |      0 |
|  2 | Tensor<[1, 3712, 1, 1]> self = ? | Done     | Done       | 0.999769 |      0 |
|  3 | Tensor<[1, 696, 1, 1]> self = ?  | Done     | Done       | 0.999746 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 3712]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3712, 1, 1]> self = ?,<br>List[int] size = [1, 3712] | Done     | Done       |     1 |     -1 |

