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
|  8 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 28, 28]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999987 |      8 |
|  1 | Tensor<[1, 144, 56, 56]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999991 |      8 |
|  2 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.99999  |      8 |
|  3 | Tensor<[1, 320, 14, 14]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999991 |      8 |
|  4 | Tensor<[1, 320, 28, 28]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999991 |      8 |
|  5 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999992 |      8 |
|  6 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999992 |      8 |
|  7 | Tensor<[1, 784, 14, 14]> input = ?,<br>Optional[Tensor]<[784]> weight = ?,<br>Optional[Tensor]<[784]> bias = ?,<br>Tensor<[784]> running_mean = ?,<br>Tensor<[784]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999992 |      8 |
|  8 | Tensor<[1, 784, 7, 7]> input = ?,<br>Optional[Tensor]<[784]> weight = ?,<br>Optional[Tensor]<[784]> bias = ?,<br>Tensor<[784]> running_mean = ?,<br>Tensor<[784]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999991 |      8 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 784]> mat1 = ?,<br>Tensor<[784, 1000]> mat2 = ? | Done     | Done       | 0.999892 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[16, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999978 |      7 |
|  1 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[36, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999971 |      7 |
|  2 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[144, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999979 |      5 |
|  3 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[144, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9       | Done     | Done       | 0.99998  |      5 |
|  4 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[320, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999979 |      5 |
|  5 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[320, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999979 |      5 |
|  6 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9       | Done     | Done       | 0.99998  |      5 |
|  7 | Tensor<[1, 16, 1, 1]> input = ?,<br>Tensor<[144, 16, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999995 |      7 |
|  8 | Tensor<[1, 196, 1, 1]> input = ?,<br>Tensor<[784, 196, 1, 1]> weight = ?,<br>Optional[Tensor]<[784]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999972 |      7 |
|  9 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999981 |      5 |
| 10 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[64, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999991 |      5 |
| 11 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[64, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999991 |      5 |
| 12 | Tensor<[1, 320, 1, 1]> input = ?,<br>Tensor<[36, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[36]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999952 |      7 |
| 13 | Tensor<[1, 320, 1, 1]> input = ?,<br>Tensor<[80, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999953 |      7 |
| 14 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[320, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20      | Done     | Done       | 0.99998  |      5 |
| 15 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[320, 320, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999957 |      5 |
| 16 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[784, 320, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999957 |      5 |
| 17 | Tensor<[1, 320, 14, 14]> input = ?,<br>Tensor<[784, 320, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999957 |      5 |
| 18 | Tensor<[1, 320, 28, 28]> input = ?,<br>Tensor<[320, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 20      | Done     | Done       | 0.99998  |      5 |
| 19 | Tensor<[1, 36, 1, 1]> input = ?,<br>Tensor<[144, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999987 |      7 |
| 20 | Tensor<[1, 36, 1, 1]> input = ?,<br>Tensor<[320, 36, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999988 |      7 |
| 21 | Tensor<[1, 64, 1, 1]> input = ?,<br>Tensor<[8, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999992 |      7 |
| 22 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4       | Done     | Done       | 0.99998  |      5 |
| 23 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[144, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999988 |      5 |
| 24 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[144, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999988 |      5 |
| 25 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999988 |      5 |
| 26 | Tensor<[1, 784, 1, 1]> input = ?,<br>Tensor<[196, 784, 1, 1]> weight = ?,<br>Optional[Tensor]<[196]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999897 |      7 |
| 27 | Tensor<[1, 784, 1, 1]> input = ?,<br>Tensor<[80, 784, 1, 1]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999885 |      7 |
| 28 | Tensor<[1, 784, 14, 14]> input = ?,<br>Tensor<[784, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 49      | Done     | Done       | 0.999981 |      5 |
| 29 | Tensor<[1, 784, 7, 7]> input = ?,<br>Tensor<[784, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 49        | Done     | Done       | 0.999982 |      5 |
| 30 | Tensor<[1, 784, 7, 7]> input = ?,<br>Tensor<[784, 784, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999882 |      5 |
| 31 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[64, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999994 |      7 |
| 32 | Tensor<[1, 80, 1, 1]> input = ?,<br>Tensor<[320, 80, 1, 1]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999984 |      7 |
| 33 | Tensor<[1, 80, 1, 1]> input = ?,<br>Tensor<[784, 80, 1, 1]> weight = ?,<br>Optional[Tensor]<[784]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999984 |      7 |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 144, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       |     0 |      0 |
|  1 | Tensor<[1, 320, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       |     0 |      0 |
|  2 | Tensor<[1, 64, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       |     0 |      0 |
|  3 | Tensor<[1, 784, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       |     0 |      0 |
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
|  0 | Tensor<[1, 144, 1, 1]> self = ? | Done     | Done       | 0.999769 |      0 |
|  1 | Tensor<[1, 320, 1, 1]> self = ? | Done     | Done       | 0.99978  |      0 |
|  2 | Tensor<[1, 64, 1, 1]> self = ?  | Done     | Done       | 0.999757 |      0 |
|  3 | Tensor<[1, 784, 1, 1]> self = ? | Done     | Done       | 0.999775 |      0 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 784]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 784, 1, 1]> self = ?,<br>List[int] size = [1, 784] | Done     | Done       |     1 |      0 |

