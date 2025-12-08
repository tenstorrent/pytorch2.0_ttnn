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
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 144, 28, 28]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.9999911461788277 | 0      |
|  1 | Tensor<[1, 144, 56, 56]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999990759134066  | 0      |
|  3 | Tensor<[1, 320, 14, 14]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 320, 28, 28]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.9999914891054004 | 0      |
|  6 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.9999925915786683 | 0      |
|  7 | Tensor<[1, 784, 14, 14]> input = ?,<br>Optional[Tensor]<[784]> weight = ?,<br>Optional[Tensor]<[784]> bias = ?,<br>Tensor<[784]> running_mean = ?,<br>Tensor<[784]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 784, 7, 7]> input = ?,<br>Optional[Tensor]<[784]> weight = ?,<br>Optional[Tensor]<[784]> bias = ?,<br>Tensor<[784]> running_mean = ?,<br>Tensor<[784]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Unknown    | N/A                | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |     PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|--------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 784]> mat1 = ?,<br>Tensor<[784, 1000]> mat2 = ? | Done     | Done       | 0.99997 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[16, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999981 |      1 |
|  1 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[36, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999985 |      1 |
|  2 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[144, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999979 |      0 |
|  3 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[144, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9       | Done     | Done       | 0.99998  |      0 |
|  4 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[320, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999979 |      0 |
|  5 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[320, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999979 |      0 |
|  6 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9       | Done     | Done       | 0.99998  |      0 |
|  7 | Tensor<[1, 16, 1, 1]> input = ?,<br>Tensor<[144, 16, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999993 |      1 |
|  8 | Tensor<[1, 196, 1, 1]> input = ?,<br>Tensor<[784, 196, 1, 1]> weight = ?,<br>Optional[Tensor]<[784]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999966 |      1 |
|  9 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999981 |      0 |
| 10 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[64, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999991 |      0 |
| 11 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[64, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999991 |      0 |
| 12 | Tensor<[1, 320, 1, 1]> input = ?,<br>Tensor<[36, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999935 |      1 |
| 13 | Tensor<[1, 320, 1, 1]> input = ?,<br>Tensor<[80, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999968 |      1 |
| 14 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[320, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20      | Done     | Done       | 0.999981 |      0 |
| 15 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999957 |      0 |
| 16 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[784, 320, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999956 |      0 |
| 17 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[784, 320, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999957 |      0 |
| 18 | Tensor<[1, 320, 28, 28]> input = ?,<br>Tensor<[320, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20      | Done     | Done       | 0.99998  |      0 |
| 19 | Tensor<[1, 36, 1, 1]> input = ?,<br>Tensor<[144, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999989 |      1 |
| 20 | Tensor<[1, 36, 1, 1]> input = ?,<br>Tensor<[320, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99999  |      1 |
| 21 | Tensor<[1, 64, 1, 1]> input = ?,<br>Tensor<[8, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999975 |      1 |
| 22 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4       | Done     | Done       | 0.99998  |      0 |
| 23 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[144, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999988 |      0 |
| 24 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[144, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999988 |      0 |
| 25 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999988 |      0 |
| 26 | Tensor<[1, 784, 1, 1]> input = ?,<br>Tensor<[196, 784, 1, 1]> weight = ?,<br>Optional[Tensor]<[196]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999866 |      1 |
| 27 | Tensor<[1, 784, 1, 1]> input = ?,<br>Tensor<[80, 784, 1, 1]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999889 |      1 |
| 28 | Tensor<[1, 784, 14, 14]> input = ?,<br>Tensor<[784, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 49      | Done     | Done       | 0.99998  |      0 |
| 29 | Tensor<[1, 784, 7, 7]> input = ?,<br>Tensor<[784, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 49        | Done     | Done       | 0.999981 |      0 |
| 30 | Tensor<[1, 784, 7, 7]> input = ?,<br>Tensor<[784, 784, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999883 |      0 |
| 31 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[64, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999996 |      1 |
| 32 | Tensor<[1, 80, 1, 1]> input = ?,<br>Tensor<[320, 80, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999985 |      1 |
| 33 | Tensor<[1, 80, 1, 1]> input = ?,<br>Tensor<[784, 80, 1, 1]> weight = ?,<br>Optional[Tensor]<[784]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999985 |      1 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 320, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 64, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999995 |      0 |
|  3 | Tensor<[1, 784, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | 0.999997 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ? | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?   | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 144, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 144, 56, 56]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 16, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 196, 1, 1]> self = ?    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 32, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 320, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 320, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 36, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 64, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 64, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 784, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 784, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 8, 1, 1]> self = ?      | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 80, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 1, 1]> self = ? | Done     | Done       | 0.999772 |      0 |
|  1 | Tensor<[1, 320, 1, 1]> self = ? | Done     | Done       | 0.999776 |      0 |
|  2 | Tensor<[1, 64, 1, 1]> self = ?  | Done     | Done       | 0.999822 |      0 |
|  3 | Tensor<[1, 784, 1, 1]> self = ? | Done     | Done       | 0.999765 |      0 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 784]> self = ? | Removed  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 784, 1, 1]> self = ?,<br>List[int] size = [1, 784] | Done     | Done       |     1 |      0 |

