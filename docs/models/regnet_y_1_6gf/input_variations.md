# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 37 |          37 |         0 |          0 | ✅          |       1 |
|  4 | aten.mean.dim                                     |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  6 | aten.relu.default                                 |                 14 |          14 |         0 |          0 | ✅          |       1 |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  8 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 28, 28]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999987 |     -1 |
|  1 | Tensor<[1, 120, 56, 56]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999986 |     -1 |
|  2 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999989 |     -1 |
|  3 | Tensor<[1, 336, 14, 14]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |     -1 |
|  4 | Tensor<[1, 336, 28, 28]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |     -1 |
|  5 | Tensor<[1, 48, 112, 112]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999987 |     -1 |
|  6 | Tensor<[1, 48, 56, 56]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |     -1 |
|  7 | Tensor<[1, 888, 14, 14]> input = ?,<br>Optional[Tensor]<[888]> weight = ?,<br>Optional[Tensor]<[888]> bias = ?,<br>Tensor<[888]> running_mean = ?,<br>Tensor<[888]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999988 |     -1 |
|  8 | Tensor<[1, 888, 7, 7]> input = ?,<br>Optional[Tensor]<[888]> weight = ?,<br>Optional[Tensor]<[888]> bias = ?,<br>Tensor<[888]> running_mean = ?,<br>Tensor<[888]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999989 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ? | Done     | Done       | 0.999998 |     -1 |
|  1 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ? | Done     | Done       | 0.999998 |     -1 |
|  2 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?   | Done     | Done       | 0.999998 |     -1 |
|  3 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?     | Done     | Done       | 0.999998 |     -1 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 888]> mat1 = ?,<br>Tensor<[888, 1000]> mat2 = ? | Done     | Done       | 0.999967 |     -1 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 1, 1]> input = ?,<br>Tensor<[120, 12, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99999  |     -1 |
|  1 | Tensor<[1, 12, 1, 1]> input = ?,<br>Tensor<[48, 12, 1, 1]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999994 |     -1 |
|  2 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[12, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[12]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999952 |     -1 |
|  3 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[30, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[30]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999965 |     -1 |
|  4 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.99998  |     -1 |
|  5 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 5       | Done     | Done       | 0.999963 |     -1 |
|  6 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[336, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.99998  |     -1 |
|  7 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[336, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.99998  |     -1 |
|  8 | Tensor<[1, 120, 56, 56]> input = ?,<br>Tensor<[120, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 5       | Done     | Done       | 0.999963 |     -1 |
|  9 | Tensor<[1, 222, 1, 1]> input = ?,<br>Tensor<[888, 222, 1, 1]> weight = ?,<br>Optional[Tensor]<[888]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999979 |     -1 |
| 10 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999982 |     -1 |
| 11 | Tensor<[1, 30, 1, 1]> input = ?,<br>Tensor<[120, 30, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99999  |     -1 |
| 12 | Tensor<[1, 30, 1, 1]> input = ?,<br>Tensor<[336, 30, 1, 1]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999989 |     -1 |
| 13 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[48, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.99999  |     -1 |
| 14 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[48, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999991 |     -1 |
| 15 | Tensor<[1, 336, 1, 1]> input = ?,<br>Tensor<[30, 336, 1, 1]> weight = ?,<br>Optional[Tensor]<[30]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999988 |     -1 |
| 16 | Tensor<[1, 336, 1, 1]> input = ?,<br>Tensor<[84, 336, 1, 1]> weight = ?,<br>Optional[Tensor]<[84]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99998  |     -1 |
| 17 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[336, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 14      | Done     | Done       | 0.999965 |     -1 |
| 18 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[336, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999979 |     -1 |
| 19 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[888, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999979 |     -1 |
| 20 | Tensor<[1, 336, 14, 14]> input = ?,<br>Tensor<[888, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999955 |     -1 |
| 21 | Tensor<[1, 336, 28, 28]> input = ?,<br>Tensor<[336, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 14      | Done     | Done       | 0.999963 |     -1 |
| 22 | Tensor<[1, 48, 1, 1]> input = ?,<br>Tensor<[12, 48, 1, 1]> weight = ?,<br>Optional[Tensor]<[12]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999992 |     -1 |
| 23 | Tensor<[1, 48, 1, 1]> input = ?,<br>Tensor<[8, 48, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999994 |     -1 |
| 24 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2       | Done     | Done       | 0.999963 |     -1 |
| 25 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[120, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999988 |     -1 |
| 26 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[120, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.99999  |     -1 |
| 27 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[48, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2         | Done     | Done       | 0.999963 |     -1 |
| 28 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[48, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999988 |     -1 |
| 29 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[48, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999994 |     -1 |
| 30 | Tensor<[1, 84, 1, 1]> input = ?,<br>Tensor<[336, 84, 1, 1]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99998  |     -1 |
| 31 | Tensor<[1, 84, 1, 1]> input = ?,<br>Tensor<[888, 84, 1, 1]> weight = ?,<br>Optional[Tensor]<[888]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999982 |     -1 |
| 32 | Tensor<[1, 888, 1, 1]> input = ?,<br>Tensor<[222, 888, 1, 1]> weight = ?,<br>Optional[Tensor]<[222]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999962 |     -1 |
| 33 | Tensor<[1, 888, 1, 1]> input = ?,<br>Tensor<[84, 888, 1, 1]> weight = ?,<br>Optional[Tensor]<[84]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999974 |     -1 |
| 34 | Tensor<[1, 888, 14, 14]> input = ?,<br>Tensor<[888, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 37      | Done     | Done       | 0.999964 |     -1 |
| 35 | Tensor<[1, 888, 7, 7]> input = ?,<br>Tensor<[888, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 37        | Done     | Done       | 0.999967 |     -1 |
| 36 | Tensor<[1, 888, 7, 7]> input = ?,<br>Tensor<[888, 888, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999966 |     -1 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |     -1 |
|  1 | Tensor<[1, 336, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999997 |     -1 |
|  2 | Tensor<[1, 48, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999997 |     -1 |
|  3 | Tensor<[1, 888, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.999996 |     -1 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ? | Done     | Done       | 0.999996 |     -1 |
|  1 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ? | Done     | Done       | 0.999996 |     -1 |
|  2 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?   | Done     | Done       | 0.999996 |     -1 |
|  3 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?   | Done     | Done       | 0.999996 |     -1 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 12, 1, 1]> self = ?     | Done     | Done       |     1 |     -1 |
|  1 | Tensor<[1, 120, 28, 28]> self = ?  | Done     | Done       |     1 |     -1 |
|  2 | Tensor<[1, 120, 56, 56]> self = ?  | Done     | Done       |     1 |     -1 |
|  3 | Tensor<[1, 222, 1, 1]> self = ?    | Done     | Done       |     1 |     -1 |
|  4 | Tensor<[1, 30, 1, 1]> self = ?     | Done     | Done       |     1 |     -1 |
|  5 | Tensor<[1, 32, 112, 112]> self = ? | Done     | Done       |     1 |     -1 |
|  6 | Tensor<[1, 336, 14, 14]> self = ?  | Done     | Done       |     1 |     -1 |
|  7 | Tensor<[1, 336, 28, 28]> self = ?  | Done     | Done       |     1 |     -1 |
|  8 | Tensor<[1, 48, 112, 112]> self = ? | Done     | Done       |     1 |     -1 |
|  9 | Tensor<[1, 48, 56, 56]> self = ?   | Done     | Done       |     1 |     -1 |
| 10 | Tensor<[1, 8, 1, 1]> self = ?      | Done     | Done       |     1 |     -1 |
| 11 | Tensor<[1, 84, 1, 1]> self = ?     | Done     | Done       |     1 |     -1 |
| 12 | Tensor<[1, 888, 14, 14]> self = ?  | Done     | Done       |     1 |     -1 |
| 13 | Tensor<[1, 888, 7, 7]> self = ?    | Done     | Done       |     1 |     -1 |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | Done     | Done       | 0.999796 |     -1 |
|  1 | Tensor<[1, 336, 1, 1]> self = ? | Done     | Done       | 0.999749 |     -1 |
|  2 | Tensor<[1, 48, 1, 1]> self = ?  | Done     | Done       | 0.999727 |     -1 |
|  3 | Tensor<[1, 888, 1, 1]> self = ? | Done     | Done       | 0.999754 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 888]> self = ? | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 888, 1, 1]> self = ?,<br>List[int] size = [1, 888] | Done     | Done       |     1 |     -1 |

