# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           0 |         0 |          0 | ✘           |                  0 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |                  1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  3 | aten.convolution.default                          |                 34 |           0 |         0 |          0 | ✘           |                  0 |
|  4 | aten.mean.dim                                     |                  4 |           4 |         0 |          0 | ✅          |                  1 |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |                  1 |
|  6 | aten.relu.default                                 |                 13 |          13 |         0 |          0 | ✅          |                  1 |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |                  1 |
|  8 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  9 | aten.view.default                                 |                  1 |           0 |         0 |          1 | ✘           |                  0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2016, 14, 14]> input = ?,<br>Optional[Tensor]<[2016]> weight = ?,<br>Optional[Tensor]<[2016]> bias = ?,<br>Tensor<[2016]> running_mean = ?,<br>Tensor<[2016]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     |
|  1 | Tensor<[1, 2016, 7, 7]> input = ?,<br>Optional[Tensor]<[2016]> weight = ?,<br>Optional[Tensor]<[2016]> bias = ?,<br>Tensor<[2016]> running_mean = ?,<br>Tensor<[2016]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     |
|  2 | Tensor<[1, 224, 112, 112]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     |
|  3 | Tensor<[1, 224, 56, 56]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     |
|  5 | Tensor<[1, 448, 28, 28]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
|  6 | Tensor<[1, 448, 56, 56]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
|  7 | Tensor<[1, 896, 14, 14]> input = ?,<br>Optional[Tensor]<[896]> weight = ?,<br>Optional[Tensor]<[896]> bias = ?,<br>Tensor<[896]> running_mean = ?,<br>Tensor<[896]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
|  8 | Tensor<[1, 896, 28, 28]> input = ?,<br>Optional[Tensor]<[896]> weight = ?,<br>Optional[Tensor]<[896]> bias = ?,<br>Tensor<[896]> running_mean = ?,<br>Tensor<[896]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?   | Done     |
|  1 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ? | Done     |
|  2 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ? | Done     |
|  3 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ? | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2016]> mat1 = ?,<br>Tensor<[2016, 1000]> mat2 = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 1, 1]> input = ?,<br>Tensor<[448, 112, 1, 1]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
|  1 | Tensor<[1, 112, 1, 1]> input = ?,<br>Tensor<[896, 112, 1, 1]> weight = ?,<br>Optional[Tensor]<[896]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
|  2 | Tensor<[1, 2016, 1, 1]> input = ?,<br>Tensor<[224, 2016, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     |
|  3 | Tensor<[1, 2016, 14, 14]> input = ?,<br>Tensor<[2016, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 36      | None     |
|  4 | Tensor<[1, 2016, 7, 7]> input = ?,<br>Tensor<[2016, 2016, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
|  5 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[2016, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[2016]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     |
|  6 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[56, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
|  7 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[8, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
|  8 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[896, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[896]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
|  9 | Tensor<[1, 224, 112, 112]> input = ?,<br>Tensor<[224, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4       | None     |
| 10 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 11 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4         | None     |
| 12 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[448, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 13 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[448, 224, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 14 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | None     |
| 15 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 16 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 17 | Tensor<[1, 448, 1, 1]> input = ?,<br>Tensor<[112, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 18 | Tensor<[1, 448, 1, 1]> input = ?,<br>Tensor<[56, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 19 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 20 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8         | None     |
| 21 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[896, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 22 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[896, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 23 | Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[448, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 8         | None     |
| 24 | Tensor<[1, 56, 1, 1]> input = ?,<br>Tensor<[224, 56, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 25 | Tensor<[1, 56, 1, 1]> input = ?,<br>Tensor<[448, 56, 1, 1]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 26 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[224, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
| 27 | Tensor<[1, 896, 1, 1]> input = ?,<br>Tensor<[112, 896, 1, 1]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 28 | Tensor<[1, 896, 1, 1]> input = ?,<br>Tensor<[224, 896, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 29 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[2016, 896, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
| 30 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[2016, 896, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
| 31 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[896, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16        | None     |
| 32 | Tensor<[1, 896, 14, 14]> input = ?,<br>Tensor<[896, 896, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     |
| 33 | Tensor<[1, 896, 28, 28]> input = ?,<br>Tensor<[896, 56, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16        | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     |
|  1 | Tensor<[1, 224, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
|  2 | Tensor<[1, 448, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
|  3 | Tensor<[1, 896, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ? | Done     |
|  1 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ? | Done     |
|  2 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ? | Done     |
|  3 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ? | Done     |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 112, 1, 1]> self = ?     | Done     |
|  1 | Tensor<[1, 2016, 14, 14]> self = ?  | Done     |
|  2 | Tensor<[1, 2016, 7, 7]> self = ?    | Done     |
|  3 | Tensor<[1, 224, 1, 1]> self = ?     | Done     |
|  4 | Tensor<[1, 224, 112, 112]> self = ? | Done     |
|  5 | Tensor<[1, 224, 56, 56]> self = ?   | Done     |
|  6 | Tensor<[1, 32, 112, 112]> self = ?  | Done     |
|  7 | Tensor<[1, 448, 28, 28]> self = ?   | Done     |
|  8 | Tensor<[1, 448, 56, 56]> self = ?   | Done     |
|  9 | Tensor<[1, 56, 1, 1]> self = ?      | Done     |
| 10 | Tensor<[1, 8, 1, 1]> self = ?       | Done     |
| 11 | Tensor<[1, 896, 14, 14]> self = ?   | Done     |
| 12 | Tensor<[1, 896, 28, 28]> self = ?   | Done     |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 2016, 1, 1]> self = ? | Done     |
|  1 | Tensor<[1, 224, 1, 1]> self = ?  | Done     |
|  2 | Tensor<[1, 448, 1, 1]> self = ?  | Done     |
|  3 | Tensor<[1, 896, 1, 1]> self = ?  | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 2016]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2016, 1, 1]> self = ?,<br>List[int] size = [1, 2016] | Fallback |

