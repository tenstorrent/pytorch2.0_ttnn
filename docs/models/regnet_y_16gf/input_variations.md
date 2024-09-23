# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           0 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |
|  2 | aten.addmm.default                                |                  1 |           1 |
|  3 | aten.convolution.default                          |                 34 |           0 |
|  4 | aten.mean.dim                                     |                  4 |           4 |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |
|  6 | aten.relu.default                                 |                 13 |          13 |
|  7 | aten.sigmoid.default                              |                  4 |           4 |
|  8 | aten.t.default                                    |                  1 |           1 |
|  9 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Optional[Tensor]<[1232]> weight = ?,<br>Optional[Tensor]<[1232]> bias = ?,<br>Tensor<[1232]> running_mean = ?,<br>Tensor<[1232]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 1232, 28, 28]> input = ?,<br>Optional[Tensor]<[1232]> weight = ?,<br>Optional[Tensor]<[1232]> bias = ?,<br>Tensor<[1232]> running_mean = ?,<br>Tensor<[1232]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  2 | Tensor<[1, 224, 112, 112]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Unknown  |
|  3 | Tensor<[1, 224, 56, 56]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  4 | Tensor<[1, 3024, 14, 14]> input = ?,<br>Optional[Tensor]<[3024]> weight = ?,<br>Optional[Tensor]<[3024]> bias = ?,<br>Tensor<[3024]> running_mean = ?,<br>Tensor<[3024]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  5 | Tensor<[1, 3024, 7, 7]> input = ?,<br>Optional[Tensor]<[3024]> weight = ?,<br>Optional[Tensor]<[3024]> bias = ?,<br>Tensor<[3024]> running_mean = ?,<br>Tensor<[3024]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05   | Unknown  |
|  6 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
|  7 | Tensor<[1, 448, 28, 28]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  8 | Tensor<[1, 448, 56, 56]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ? | Done     |
|  1 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?   | Done     |
|  2 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?     | Done     |
|  3 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 3024]> mat1 = ?,<br>Tensor<[3024, 1000]> mat2 = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 1, 1]> input = ?,<br>Tensor<[1232, 112, 1, 1]> weight = ?,<br>Optional[Tensor]<[1232]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
|  1 | Tensor<[1, 112, 1, 1]> input = ?,<br>Tensor<[448, 112, 1, 1]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  2 | Tensor<[1, 1232, 1, 1]> input = ?,<br>Tensor<[112, 1232, 1, 1]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
|  3 | Tensor<[1, 1232, 1, 1]> input = ?,<br>Tensor<[308, 1232, 1, 1]> weight = ?,<br>Optional[Tensor]<[308]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
|  4 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[1232, 112, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 11   | Unknown  |
|  5 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[1232, 1232, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  6 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[3024, 1232, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  7 | Tensor<[1, 1232, 14, 14]> input = ?,<br>Tensor<[3024, 1232, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  8 | Tensor<[1, 1232, 28, 28]> input = ?,<br>Tensor<[1232, 112, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 11   | Unknown  |
|  9 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[56, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 10 | Tensor<[1, 224, 1, 1]> input = ?,<br>Tensor<[8, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
| 11 | Tensor<[1, 224, 112, 112]> input = ?,<br>Tensor<[224, 112, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 2    | Unknown  |
| 12 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 112, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 2      | Unknown  |
| 13 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[224, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 14 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[448, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 15 | Tensor<[1, 224, 56, 56]> input = ?,<br>Tensor<[448, 224, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 16 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Unknown  |
| 17 | Tensor<[1, 3024, 1, 1]> input = ?,<br>Tensor<[308, 3024, 1, 1]> weight = ?,<br>Optional[Tensor]<[308]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
| 18 | Tensor<[1, 3024, 14, 14]> input = ?,<br>Tensor<[3024, 112, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 27   | Unknown  |
| 19 | Tensor<[1, 3024, 7, 7]> input = ?,<br>Tensor<[3024, 3024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 20 | Tensor<[1, 308, 1, 1]> input = ?,<br>Tensor<[1232, 308, 1, 1]> weight = ?,<br>Optional[Tensor]<[1232]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
| 21 | Tensor<[1, 308, 1, 1]> input = ?,<br>Tensor<[3024, 308, 1, 1]> weight = ?,<br>Optional[Tensor]<[3024]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Unknown  |
| 22 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 23 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[224, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 24 | Tensor<[1, 448, 1, 1]> input = ?,<br>Tensor<[112, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 25 | Tensor<[1, 448, 1, 1]> input = ?,<br>Tensor<[56, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 26 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[1232, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 27 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[1232, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 28 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 112, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 4      | Unknown  |
| 29 | Tensor<[1, 448, 28, 28]> input = ?,<br>Tensor<[448, 448, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
| 30 | Tensor<[1, 448, 56, 56]> input = ?,<br>Tensor<[448, 112, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 4      | Unknown  |
| 31 | Tensor<[1, 56, 1, 1]> input = ?,<br>Tensor<[224, 56, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 32 | Tensor<[1, 56, 1, 1]> input = ?,<br>Tensor<[448, 56, 1, 1]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[224, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
|  1 | Tensor<[1, 224, 56, 56]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True  | Done     |
|  2 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True   | Done     |
|  3 | Tensor<[1, 448, 28, 28]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True  | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ? | Done     |
|  1 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?   | Done     |
|  2 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?   | Done     |
|  3 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?   | Done     |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 112, 1, 1]> self = ?     | Done     |
|  1 | Tensor<[1, 1232, 14, 14]> self = ?  | Done     |
|  2 | Tensor<[1, 1232, 28, 28]> self = ?  | Done     |
|  3 | Tensor<[1, 224, 112, 112]> self = ? | Done     |
|  4 | Tensor<[1, 224, 56, 56]> self = ?   | Done     |
|  5 | Tensor<[1, 3024, 14, 14]> self = ?  | Done     |
|  6 | Tensor<[1, 3024, 7, 7]> self = ?    | Done     |
|  7 | Tensor<[1, 308, 1, 1]> self = ?     | Done     |
|  8 | Tensor<[1, 32, 112, 112]> self = ?  | Done     |
|  9 | Tensor<[1, 448, 28, 28]> self = ?   | Done     |
| 10 | Tensor<[1, 448, 56, 56]> self = ?   | Done     |
| 11 | Tensor<[1, 56, 1, 1]> self = ?      | Done     |
| 12 | Tensor<[1, 8, 1, 1]> self = ?       | Done     |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1232, 1, 1]> self = ? | Done     |
|  1 | Tensor<[1, 224, 1, 1]> self = ?  | Done     |
|  2 | Tensor<[1, 3024, 1, 1]> self = ? | Done     |
|  3 | Tensor<[1, 448, 1, 1]> self = ?  | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 3024]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3024, 1, 1]> self = ?,<br>List[int]<> size = [1, 3024] | Unknown  |

