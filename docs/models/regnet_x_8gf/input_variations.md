# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 20 |          20 |         0 |          0 | ✅          |       1 |
|  4 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.relu.default                                 |                  9 |           9 |         0 |          0 | ✅          |       1 |
|  6 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1920, 14, 14]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>Tensor<[1920]> running_mean = ?,<br>Tensor<[1920]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999983 |      5 |
|  1 | Tensor<[1, 1920, 7, 7]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>Tensor<[1920]> running_mean = ?,<br>Tensor<[1920]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999988 |      5 |
|  2 | Tensor<[1, 240, 28, 28]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      5 |
|  3 | Tensor<[1, 240, 56, 56]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.99999  |      5 |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999989 |      5 |
|  5 | Tensor<[1, 720, 14, 14]> input = ?,<br>Optional[Tensor]<[720]> weight = ?,<br>Optional[Tensor]<[720]> bias = ?,<br>Tensor<[720]> running_mean = ?,<br>Tensor<[720]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      5 |
|  6 | Tensor<[1, 720, 28, 28]> input = ?,<br>Optional[Tensor]<[720]> weight = ?,<br>Optional[Tensor]<[720]> bias = ?,<br>Tensor<[720]> running_mean = ?,<br>Tensor<[720]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      5 |
|  7 | Tensor<[1, 80, 112, 112]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999989 |      5 |
|  8 | Tensor<[1, 80, 56, 56]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | Done     | Done       | 0.999989 |      5 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1920]> mat1 = ?,<br>Tensor<[1920, 1000]> mat2 = ? | Done     | Done       | 0.999954 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1920, 14, 14]> input = ?,<br>Tensor<[1920, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16 | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1920, 7, 7]> input = ?,<br>Tensor<[1920, 1920, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2    | Done     | Done       | 0.9998254100638346 | 4      |
|  3 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999977462073399  | 4      |
|  4 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[720, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[720, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 240, 56, 56]> input = ?,<br>Tensor<[240, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2    | Done     | Done       | 0.9998246144583341 | 4      |
|  7 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.9999801747766058 | 4      |
|  8 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[80, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9999894533165681 | 4      |
|  9 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[80, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9999911471028974 | 4      |
| 10 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[1920, 720, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[1920, 720, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[720, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6    | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[720, 720, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 720, 28, 28]> input = ?,<br>Tensor<[720, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6    | Done     | Unknown    | N/A                | N/A    |
| 15 | Tensor<[1, 80, 112, 112]> input = ?,<br>Tensor<[80, 80, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.9998959693413638 | 4      |
| 16 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[240, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.9999862129718531 | 4      |
| 17 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[240, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.9999863114530528 | 4      |
| 18 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[80, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.9999862987182652 | 4      |
| 19 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[80, 80, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.9998971027059077 | 4      |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1920, 14, 14]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1920, 7, 7]> self = ?   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 240, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 240, 56, 56]> self = ?  | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 32, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 720, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 720, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 80, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 80, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1920]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1920, 1, 1]> self = ?,<br>List[int] size = [1, 1920] | Done     | Done       |     1 |     -1 |

