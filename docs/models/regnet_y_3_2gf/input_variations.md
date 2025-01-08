# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 34 |          34 |         0 |          0 | ✅          |       1 |
|  4 | aten.mean.dim                                     |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  6 | aten.relu.default                                 |                 13 |          13 |         0 |          0 | ✅          |       1 |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  8 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1512, 14, 14]> input = ?,<br>Optional[Tensor]<[1512]> weight = ?,<br>Optional[Tensor]<[1512]> bias = ?,<br>Tensor<[1512]> running_mean = ?,<br>Tensor<[1512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999991 |      5 |
|  1 | Tensor<[1, 1512, 7, 7]> input = ?,<br>Optional[Tensor]<[1512]> weight = ?,<br>Optional[Tensor]<[1512]> bias = ?,<br>Tensor<[1512]> running_mean = ?,<br>Tensor<[1512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.99999  |      5 |
|  2 | Tensor<[1, 216, 28, 28]> input = ?,<br>Optional[Tensor]<[216]> weight = ?,<br>Optional[Tensor]<[216]> bias = ?,<br>Tensor<[216]> running_mean = ?,<br>Tensor<[216]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      5 |
|  3 | Tensor<[1, 216, 56, 56]> input = ?,<br>Optional[Tensor]<[216]> weight = ?,<br>Optional[Tensor]<[216]> bias = ?,<br>Tensor<[216]> running_mean = ?,<br>Tensor<[216]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999983 |      5 |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999991 |      5 |
|  5 | Tensor<[1, 576, 14, 14]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      5 |
|  6 | Tensor<[1, 576, 28, 28]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      5 |
|  7 | Tensor<[1, 72, 112, 112]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.99999  |      5 |
|  8 | Tensor<[1, 72, 56, 56]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | Done     | Done       | 0.999987 |      5 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1512]> mat1 = ?,<br>Tensor<[1512, 1000]> mat2 = ? | Done     | Done       | 0.999958 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[1512, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[1512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999983 |      6 |
|  1 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[576, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999984 |      6 |
|  2 | Tensor<[1, 1512, 1, 1]> input = ?,<br>Tensor<[144, 1512, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999962 |      6 |
|  3 | Tensor<[1, 1512, 14, 14]> input = ?,<br>Tensor<[1512, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 63      | Done     | Done       | 0.999964 |      4 |
|  4 | Tensor<[1, 1512, 7, 7]> input = ?,<br>Tensor<[1512, 1512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999963 |      4 |
|  5 | Tensor<[1, 18, 1, 1]> input = ?,<br>Tensor<[216, 18, 1, 1]> weight = ?,<br>Optional[Tensor]<[216]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999992 |      6 |
|  6 | Tensor<[1, 18, 1, 1]> input = ?,<br>Tensor<[72, 18, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999991 |      6 |
|  7 | Tensor<[1, 216, 1, 1]> input = ?,<br>Tensor<[18, 216, 1, 1]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999976 |      6 |
|  8 | Tensor<[1, 216, 1, 1]> input = ?,<br>Tensor<[54, 216, 1, 1]> weight = ?,<br>Optional[Tensor]<[54]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999987 |      6 |
|  9 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[216, 216, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99998  |      4 |
| 10 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[216, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9         | Done     | Done       | 0.999963 |      4 |
| 11 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[576, 216, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99998  |      4 |
| 12 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[576, 216, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999969 |      4 |
| 13 | Tensor<[1, 216, 56, 56]> input = ?,<br>Tensor<[216, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9         | Done     | Done       | 0.999963 |      4 |
| 14 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999982 |      4 |
| 15 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[72, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999989 |      4 |
| 16 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[72, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999991 |      4 |
| 17 | Tensor<[1, 54, 1, 1]> input = ?,<br>Tensor<[216, 54, 1, 1]> weight = ?,<br>Optional[Tensor]<[216]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999981 |      6 |
| 18 | Tensor<[1, 54, 1, 1]> input = ?,<br>Tensor<[576, 54, 1, 1]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999988 |      6 |
| 19 | Tensor<[1, 576, 1, 1]> input = ?,<br>Tensor<[144, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999967 |      6 |
| 20 | Tensor<[1, 576, 1, 1]> input = ?,<br>Tensor<[54, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<[54]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999977 |      6 |
| 21 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[1512, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999971 |      4 |
| 22 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[1512, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999919 |      4 |
| 23 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24        | Done     | Done       | 0.999965 |      4 |
| 24 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999971 |      4 |
| 25 | Tensor<[1, 576, 28, 28]> input = ?,<br>Tensor<[576, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24        | Done     | Done       | 0.999963 |      4 |
| 26 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[18, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999988 |      6 |
| 27 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[8, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999991 |      6 |
| 28 | Tensor<[1, 72, 112, 112]> input = ?,<br>Tensor<[72, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3         | Done     | Done       | 0.999963 |      4 |
| 29 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[216, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999986 |      4 |
| 30 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[216, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999985 |      4 |
| 31 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3           | Done     | Done       | 0.999963 |      4 |
| 32 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999986 |      4 |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[72, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.99999  |      6 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.971674 |      0 |
|  1 | Tensor<[1, 216, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.959388 |      0 |
|  2 | Tensor<[1, 576, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.964221 |      0 |
|  3 | Tensor<[1, 72, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.928291 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ? | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?   | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 144, 1, 1]> self = ?    | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1512, 14, 14]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1512, 7, 7]> self = ?   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 18, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 216, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 216, 56, 56]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 32, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 54, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 576, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 576, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 72, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 72, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 8, 1, 1]> self = ?      | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1512, 1, 1]> self = ? | Done     | Done       | 0.999763 |      0 |
|  1 | Tensor<[1, 216, 1, 1]> self = ?  | Done     | Done       | 0.999785 |      0 |
|  2 | Tensor<[1, 576, 1, 1]> self = ?  | Done     | Done       | 0.999771 |      0 |
|  3 | Tensor<[1, 72, 1, 1]> self = ?   | Done     | Done       | 0.999762 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1512]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1512, 1, 1]> self = ?,<br>List[int] size = [1, 1512] | Done     | Done       |     1 |     -1 |

