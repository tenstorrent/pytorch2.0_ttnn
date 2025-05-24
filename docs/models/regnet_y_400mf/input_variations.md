# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 34 |          34 |         0 |          0 | ✅          |       1 |
|  4 | aten.mean.dim                                     |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  6 | aten.relu.default                                 |                 14 |          14 |         0 |          0 | ✅          |       1 |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  8 | aten.t.default                                    |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 104, 28, 28]> input = ?,<br>Optional[Tensor]<[104]> weight = ?,<br>Optional[Tensor]<[104]> bias = ?,<br>Tensor<[104]> running_mean = ?,<br>Tensor<[104]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      0 |
|  1 | Tensor<[1, 104, 56, 56]> input = ?,<br>Optional[Tensor]<[104]> weight = ?,<br>Optional[Tensor]<[104]> bias = ?,<br>Tensor<[104]> running_mean = ?,<br>Tensor<[104]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |      0 |
|  2 | Tensor<[1, 208, 14, 14]> input = ?,<br>Optional[Tensor]<[208]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>Tensor<[208]> running_mean = ?,<br>Tensor<[208]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999987 |      0 |
|  3 | Tensor<[1, 208, 28, 28]> input = ?,<br>Optional[Tensor]<[208]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>Tensor<[208]> running_mean = ?,<br>Tensor<[208]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |      0 |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999989 |      0 |
|  5 | Tensor<[1, 440, 14, 14]> input = ?,<br>Optional[Tensor]<[440]> weight = ?,<br>Optional[Tensor]<[440]> bias = ?,<br>Tensor<[440]> running_mean = ?,<br>Tensor<[440]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999988 |      0 |
|  6 | Tensor<[1, 440, 7, 7]> input = ?,<br>Optional[Tensor]<[440]> weight = ?,<br>Optional[Tensor]<[440]> bias = ?,<br>Tensor<[440]> running_mean = ?,<br>Tensor<[440]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999983 |      0 |
|  7 | Tensor<[1, 48, 112, 112]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999989 |      0 |
|  8 | Tensor<[1, 48, 56, 56]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 440]> mat1 = ?,<br>Tensor<[440, 1000]> mat2 = ? | Done     | Done       | 0.999969 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 104, 1, 1]> input = ?,<br>Tensor<[12, 104, 1, 1]> weight = ?,<br>Optional[Tensor]<[12]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999988 |      1 |
|  1 | Tensor<[1, 104, 1, 1]> input = ?,<br>Tensor<[26, 104, 1, 1]> weight = ?,<br>Optional[Tensor]<[26]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999984 |      1 |
|  2 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[104, 104, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999981 |      0 |
|  3 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[104, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 13       | Done     | Done       | 0.999981 |      0 |
|  4 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[208, 104, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999981 |      0 |
|  5 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[208, 104, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999982 |      0 |
|  6 | Tensor<[1, 104, 56, 56]> input = ?,<br>Tensor<[104, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 13       | Done     | Done       | 0.99998  |      0 |
|  7 | Tensor<[1, 110, 1, 1]> input = ?,<br>Tensor<[440, 110, 1, 1]> weight = ?,<br>Optional[Tensor]<[440]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999983 |      1 |
|  8 | Tensor<[1, 12, 1, 1]> input = ?,<br>Tensor<[104, 12, 1, 1]> weight = ?,<br>Optional[Tensor]<[104]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99999  |      1 |
|  9 | Tensor<[1, 208, 1, 1]> input = ?,<br>Tensor<[26, 208, 1, 1]> weight = ?,<br>Optional[Tensor]<[26]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99998  |      1 |
| 10 | Tensor<[1, 208, 1, 1]> input = ?,<br>Tensor<[52, 208, 1, 1]> weight = ?,<br>Optional[Tensor]<[52]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999987 |      1 |
| 11 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[208, 208, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999982 |      0 |
| 12 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[208, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 26       | Done     | Done       | 0.999981 |      0 |
| 13 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[440, 208, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999982 |      0 |
| 14 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[440, 208, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999971 |      0 |
| 15 | Tensor<[1, 208, 28, 28]> input = ?,<br>Tensor<[208, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 26       | Done     | Done       | 0.99998  |      0 |
| 16 | Tensor<[1, 26, 1, 1]> input = ?,<br>Tensor<[104, 26, 1, 1]> weight = ?,<br>Optional[Tensor]<[104]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999989 |      1 |
| 17 | Tensor<[1, 26, 1, 1]> input = ?,<br>Tensor<[208, 26, 1, 1]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999988 |      1 |
| 18 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999981 |      0 |
| 19 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[48, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999989 |      0 |
| 20 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[48, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999991 |      0 |
| 21 | Tensor<[1, 440, 1, 1]> input = ?,<br>Tensor<[110, 440, 1, 1]> weight = ?,<br>Optional[Tensor]<[110]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999971 |      1 |
| 22 | Tensor<[1, 440, 1, 1]> input = ?,<br>Tensor<[52, 440, 1, 1]> weight = ?,<br>Optional[Tensor]<[52]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999958 |      1 |
| 23 | Tensor<[1, 440, 14, 14]> input = ?,<br>Tensor<[440, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 55       | Done     | Done       | 0.999981 |      0 |
| 24 | Tensor<[1, 440, 7, 7]> input = ?,<br>Tensor<[440, 440, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999975 |      0 |
| 25 | Tensor<[1, 440, 7, 7]> input = ?,<br>Tensor<[440, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 55         | Done     | Done       | 0.999982 |      0 |
| 26 | Tensor<[1, 48, 1, 1]> input = ?,<br>Tensor<[8, 48, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999978 |      1 |
| 27 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6        | Done     | Done       | 0.99998  |      0 |
| 28 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[104, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999988 |      0 |
| 29 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[104, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99999  |      0 |
| 30 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[48, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999988 |      0 |
| 31 | Tensor<[1, 52, 1, 1]> input = ?,<br>Tensor<[208, 52, 1, 1]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999986 |      1 |
| 32 | Tensor<[1, 52, 1, 1]> input = ?,<br>Tensor<[440, 52, 1, 1]> weight = ?,<br>Optional[Tensor]<[440]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999985 |      1 |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[48, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999993 |      1 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 104, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 208, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |      0 |
|  2 | Tensor<[1, 440, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 48, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999997 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ? | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?   | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 104, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 104, 56, 56]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 110, 1, 1]> self = ?    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 12, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 208, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 208, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 26, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 32, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 440, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 440, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 48, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 48, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 52, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 8, 1, 1]> self = ?      | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 104, 1, 1]> self = ? | Done     | Done       | 0.999742 |      0 |
|  1 | Tensor<[1, 208, 1, 1]> self = ? | Done     | Done       | 0.999786 |      0 |
|  2 | Tensor<[1, 440, 1, 1]> self = ? | Done     | Done       | 0.999744 |      0 |
|  3 | Tensor<[1, 48, 1, 1]> self = ?  | Done     | Done       | 0.999725 |      0 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 440]> self = ? | Removed  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 440, 1, 1]> self = ?,<br>List[int] size = [1, 440] | Done     | Done       |     1 |      0 |

