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
|  0 | Tensor<[1, 2016, 14, 14]> input = ?,<br>Optional[Tensor]<[2016]> weight = ?,<br>Optional[Tensor]<[2016]> bias = ?,<br>Tensor<[2016]> running_mean = ?,<br>Tensor<[2016]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999988 |      5 |
|  1 | Tensor<[1, 2016, 7, 7]> input = ?,<br>Optional[Tensor]<[2016]> weight = ?,<br>Optional[Tensor]<[2016]> bias = ?,<br>Tensor<[2016]> running_mean = ?,<br>Tensor<[2016]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999992 |      5 |
|  2 | Tensor<[1, 224, 112, 112]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999989 |      5 |
|  3 | Tensor<[1, 224, 56, 56]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999986 |      5 |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999991 |      5 |
|  5 | Tensor<[1, 448, 28, 28]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      5 |
|  6 | Tensor<[1, 448, 56, 56]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999989 |      5 |
|  7 | Tensor<[1, 896, 14, 14]> input = ?,<br>Optional[Tensor]<[896]> weight = ?,<br>Optional[Tensor]<[896]> bias = ?,<br>Tensor<[896]> running_mean = ?,<br>Tensor<[896]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      5 |
|  8 | Tensor<[1, 896, 28, 28]> input = ?,<br>Optional[Tensor]<[896]> weight = ?,<br>Optional[Tensor]<[896]> bias = ?,<br>Tensor<[896]> running_mean = ?,<br>Tensor<[896]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      5 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2016]> mat1 = ?,<br>Tensor<[2016, 1000]> mat2 = ? | Done     | Done       | 0.999943 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 1, 1]> input = ?,<br>Tensor<[448, 112, 1, 1]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999978 |      6 |
|  1 | Tensor<[1, 112, 1, 1]> input = ?,<br>Tensor<[896, 112, 1, 1]> weight = ?,<br>Optional[Tensor]<[896]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999983 |      6 |
|  2 | Tensor<[1, 2016, 1, 1]> input = ?,<br>Tensor<[224, 2016, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999934 |      6 |
|  3 | Tensor<[1, 2016, 14, 14]> input = ?,<br>Tensor<[2016, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 36      | Done     | Done       | 0.999927 |      4 |
|  4 | Tensor<[1, 2016, 7, 7]> input = ?,<br>Tensor<[2016, 2016, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.99994  |      4 |
|  5 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[2016, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[2016]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.99998  |      6 |
|  6 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[56, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999987 |      6 |
|  7 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[8, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999989 |      6 |
|  8 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[896, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[896]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999975 |      6 |
|  9 | Tensor<[1, 224, 112, 112]> input = ?,<br>Tensor<[224, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4       | Done     | Done       | 0.999923 |      4 |
| 10 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99998  |      4 |
| 11 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4         | Done     | Done       | 0.999923 |      4 |
| 12 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[448, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99998  |      4 |
| 13 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[448, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999969 |      4 |
| 14 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999981 |      4 |
| 15 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999989 |      4 |
| 16 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999991 |      4 |
| 17 | Tensor<[1, 448, 1, 1]> input = ?,<br>Tensor<[112, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999974 |      6 |
| 18 | Tensor<[1, 448, 1, 1]> input = ?,<br>Tensor<[56, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999965 |      6 |
| 19 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999972 |      4 |
| 20 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8         | Done     | Done       | 0.999924 |      4 |
| 21 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[896, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999975 |      4 |
| 22 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[896, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999939 |      4 |
| 23 | Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[448, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8         | Done     | Done       | 0.999923 |      4 |
| 24 | Tensor<[1, 56, 1, 1]> input = ?,<br>Tensor<[224, 56, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999987 |      6 |
| 25 | Tensor<[1, 56, 1, 1]> input = ?,<br>Tensor<[448, 56, 1, 1]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999986 |      6 |
| 26 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[224, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999987 |      6 |
| 27 | Tensor<[1, 896, 1, 1]> input = ?,<br>Tensor<[112, 896, 1, 1]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999966 |      6 |
| 28 | Tensor<[1, 896, 1, 1]> input = ?,<br>Tensor<[224, 896, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999967 |      6 |
| 29 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[2016, 896, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999967 |      4 |
| 30 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[2016, 896, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999865 |      4 |
| 31 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[896, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16        | Done     | Done       | 0.999926 |      4 |
| 32 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[896, 896, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999967 |      4 |
| 33 | Tensor<[1, 896, 28, 28]> input = ?,<br>Tensor<[896, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16        | Done     | Done       | 0.999924 |      4 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 224, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |      0 |
|  2 | Tensor<[1, 448, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |      0 |
|  3 | Tensor<[1, 896, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ? | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ? | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 112, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 2016, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 2016, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 224, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 224, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 224, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 32, 112, 112]> self = ?  | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 448, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 448, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 56, 1, 1]> self = ?      | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 8, 1, 1]> self = ?       | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 896, 14, 14]> self = ?   | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 896, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2016, 1, 1]> self = ? | Done     | Done       | 0.999746 |      0 |
|  1 | Tensor<[1, 224, 1, 1]> self = ?  | Done     | Done       | 0.999794 |      0 |
|  2 | Tensor<[1, 448, 1, 1]> self = ?  | Done     | Done       | 0.999734 |      0 |
|  3 | Tensor<[1, 896, 1, 1]> self = ?  | Done     | Done       | 0.99974  |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 2016]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2016, 1, 1]> self = ?,<br>List[int] size = [1, 2016] | Done     | Done       |     1 |     -1 |

