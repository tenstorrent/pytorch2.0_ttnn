# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           0 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |
|  2 | aten.addmm.default                                |                  1 |           1 |
|  3 | aten.convolution.default                          |                 21 |           0 |
|  4 | aten.mean.dim                                     |                  1 |           1 |
|  5 | aten.relu.default                                 |                  9 |           9 |
|  6 | aten.t.default                                    |                  1 |           1 |
|  7 | aten.view.default                                 |                  1 |           0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1008, 14, 14]> input = ?,<br>Optional[Tensor]<[1008]> weight = ?,<br>Optional[Tensor]<[1008]> bias = ?,<br>Tensor<[1008]> running_mean = ?,<br>Tensor<[1008]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Unknown  |
|  1 | Tensor<[1, 1008, 7, 7]> input = ?,<br>Optional[Tensor]<[1008]> weight = ?,<br>Optional[Tensor]<[1008]> bias = ?,<br>Tensor<[1008]> running_mean = ?,<br>Tensor<[1008]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05   | Unknown  |
|  2 | Tensor<[1, 192, 28, 28]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  3 | Tensor<[1, 192, 56, 56]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
|  5 | Tensor<[1, 432, 14, 14]> input = ?,<br>Optional[Tensor]<[432]> weight = ?,<br>Optional[Tensor]<[432]> bias = ?,<br>Tensor<[432]> running_mean = ?,<br>Tensor<[432]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  6 | Tensor<[1, 432, 28, 28]> input = ?,<br>Optional[Tensor]<[432]> weight = ?,<br>Optional[Tensor]<[432]> bias = ?,<br>Tensor<[432]> running_mean = ?,<br>Tensor<[432]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Unknown  |
|  7 | Tensor<[1, 96, 112, 112]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Unknown  |
|  8 | Tensor<[1, 96, 56, 56]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05           | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?   | Done     |
|  1 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ? | Done     |
|  2 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ? | Done     |
|  3 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1008]> mat1 = ?,<br>Tensor<[1008, 1000]> mat2 = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1008, 14, 14]> input = ?,<br>Tensor<[1008, 48, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 21 | Unknown  |
|  1 | Tensor<[1, 1008, 7, 7]> input = ?,<br>Tensor<[1008, 1008, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
|  2 | Tensor<[1, 1008, 7, 7]> input = ?,<br>Tensor<[1008, 48, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 21   | Unknown  |
|  3 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 192, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  4 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 48, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 4    | Unknown  |
|  5 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[432, 192, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  6 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[432, 192, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
|  7 | Tensor<[1, 192, 56, 56]> input = ?,<br>Tensor<[192, 48, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 4    | Unknown  |
|  8 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
|  9 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[96, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Unknown  |
| 10 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[96, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | Unknown  |
| 11 | Tensor<[1, 432, 14, 14]> input = ?,<br>Tensor<[1008, 432, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
| 12 | Tensor<[1, 432, 14, 14]> input = ?,<br>Tensor<[1008, 432, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | Unknown  |
| 13 | Tensor<[1, 432, 14, 14]> input = ?,<br>Tensor<[432, 432, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Unknown  |
| 14 | Tensor<[1, 432, 14, 14]> input = ?,<br>Tensor<[432, 48, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 9    | Unknown  |
| 15 | Tensor<[1, 432, 28, 28]> input = ?,<br>Tensor<[432, 48, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 9    | Unknown  |
| 16 | Tensor<[1, 96, 112, 112]> input = ?,<br>Tensor<[96, 48, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 2    | Unknown  |
| 17 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[192, 96, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 18 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[192, 96, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Unknown  |
| 19 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[96, 48, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 2      | Unknown  |
| 20 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[96, 96, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 1008, 14, 14]> self = ? | Done     |
|  1 | Tensor<[1, 1008, 7, 7]> self = ?   | Done     |
|  2 | Tensor<[1, 192, 28, 28]> self = ?  | Done     |
|  3 | Tensor<[1, 192, 56, 56]> self = ?  | Done     |
|  4 | Tensor<[1, 32, 112, 112]> self = ? | Done     |
|  5 | Tensor<[1, 432, 14, 14]> self = ?  | Done     |
|  6 | Tensor<[1, 432, 28, 28]> self = ?  | Done     |
|  7 | Tensor<[1, 96, 112, 112]> self = ? | Done     |
|  8 | Tensor<[1, 96, 56, 56]> self = ?   | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1008]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1008, 1, 1]> self = ?,<br>List[int]<> size = [1, 1008] | Unknown  |

