# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.convolution.default                          |                 34 |          33 |         0 |          0 | 🚧          |    0.97 |
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
|  0 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Optional[Tensor]<[1232]> weight = ?,<br>Optional[Tensor]<[1232]> bias = ?,<br>Tensor<[1232]> running_mean = ?,<br>Tensor<[1232]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      1 |
|  1 | Tensor<[1, 1232, 28, 28]> input = ?,<br>Optional[Tensor]<[1232]> weight = ?,<br>Optional[Tensor]<[1232]> bias = ?,<br>Tensor<[1232]> running_mean = ?,<br>Tensor<[1232]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999986 |      1 |
|  2 | Tensor<[1, 224, 112, 112]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999992 |      1 |
|  3 | Tensor<[1, 224, 56, 56]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      1 |
|  4 | Tensor<[1, 3024, 14, 14]> input = ?,<br>Optional[Tensor]<[3024]> weight = ?,<br>Optional[Tensor]<[3024]> bias = ?,<br>Tensor<[3024]> running_mean = ?,<br>Tensor<[3024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      1 |
|  5 | Tensor<[1, 3024, 7, 7]> input = ?,<br>Optional[Tensor]<[3024]> weight = ?,<br>Optional[Tensor]<[3024]> bias = ?,<br>Tensor<[3024]> running_mean = ?,<br>Tensor<[3024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.99999  |      1 |
|  6 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999992 |      1 |
|  7 | Tensor<[1, 448, 28, 28]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      1 |
|  8 | Tensor<[1, 448, 56, 56]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999989 |      1 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 3024]> mat1 = ?,<br>Tensor<[3024, 1000]> mat2 = ? | Done     | Done       | 0.999915 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 1, 1]> input = ?,<br>Tensor<[1232, 112, 1, 1]> weight = ?,<br>Optional[Tensor]<[1232]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.99998  |      3 |
|  1 | Tensor<[1, 112, 1, 1]> input = ?,<br>Tensor<[448, 112, 1, 1]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99998  |      3 |
|  2 | Tensor<[1, 1232, 1, 1]> input = ?,<br>Tensor<[112, 1232, 1, 1]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999958 |      3 |
|  3 | Tensor<[1, 1232, 1, 1]> input = ?,<br>Tensor<[308, 1232, 1, 1]> weight = ?,<br>Optional[Tensor]<[308]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999961 |      3 |
|  4 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[1232, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11     | Done     | Done       | 0.999854 |      2 |
|  5 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[1232, 1232, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999959 |      2 |
|  6 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[3024, 1232, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999959 |      2 |
|  7 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[3024, 1232, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Fallback   | 1        |     -1 |
|  8 | Tensor<[1, 1232, 28, 28]> input = ?,<br>Tensor<[1232, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11     | Done     | Done       | 0.999847 |      2 |
|  9 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[56, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999975 |      3 |
| 10 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[8, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999977 |      3 |
| 11 | Tensor<[1, 224, 112, 112]> input = ?,<br>Tensor<[224, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2      | Done     | Done       | 0.999844 |      2 |
| 12 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2        | Done     | Done       | 0.999845 |      2 |
| 13 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99998  |      2 |
| 14 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[448, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99998  |      2 |
| 15 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[448, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999969 |      2 |
| 16 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999981 |      2 |
| 17 | Tensor<[1, 3024, 1, 1]> input = ?,<br>Tensor<[308, 3024, 1, 1]> weight = ?,<br>Optional[Tensor]<[308]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999927 |      3 |
| 18 | Tensor<[1, 3024, 14, 14]> input = ?,<br>Tensor<[3024, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 27     | Done     | Done       | 0.999854 |      2 |
| 19 | Tensor<[1, 3024, 7, 7]> input = ?,<br>Tensor<[3024, 3024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.99992  |      2 |
| 20 | Tensor<[1, 308, 1, 1]> input = ?,<br>Tensor<[1232, 308, 1, 1]> weight = ?,<br>Optional[Tensor]<[1232]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999974 |      3 |
| 21 | Tensor<[1, 308, 1, 1]> input = ?,<br>Tensor<[3024, 308, 1, 1]> weight = ?,<br>Optional[Tensor]<[3024]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999974 |      3 |
| 22 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999989 |      2 |
| 23 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999991 |      2 |
| 24 | Tensor<[1, 448, 1, 1]> input = ?,<br>Tensor<[112, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999982 |      3 |
| 25 | Tensor<[1, 448, 1, 1]> input = ?,<br>Tensor<[56, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999981 |      3 |
| 26 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[1232, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999975 |      2 |
| 27 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[1232, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999939 |      2 |
| 28 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4        | Done     | Done       | 0.999847 |      2 |
| 29 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999972 |      2 |
| 30 | Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[448, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4        | Done     | Done       | 0.999845 |      2 |
| 31 | Tensor<[1, 56, 1, 1]> input = ?,<br>Tensor<[224, 56, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999984 |      3 |
| 32 | Tensor<[1, 56, 1, 1]> input = ?,<br>Tensor<[448, 56, 1, 1]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999985 |      3 |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[224, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999988 |      3 |
### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 224, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 448, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999997 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?   | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 112, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1232, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 1232, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 224, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 224, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 3024, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 3024, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 308, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 32, 112, 112]> self = ?  | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 448, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 448, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 56, 1, 1]> self = ?      | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 8, 1, 1]> self = ?       | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1232, 1, 1]> self = ? | Done     | Done       | 0.999762 |      0 |
|  1 | Tensor<[1, 224, 1, 1]> self = ?  | Done     | Done       | 0.999719 |      0 |
|  2 | Tensor<[1, 3024, 1, 1]> self = ? | Done     | Done       | 0.99976  |      0 |
|  3 | Tensor<[1, 448, 1, 1]> self = ?  | Done     | Done       | 0.999743 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 3024]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3024, 1, 1]> self = ?,<br>List[int] size = [1, 3024] | Done     | Done       |     1 |     -1 |

