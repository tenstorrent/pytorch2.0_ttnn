# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |
|---:|:--------------------------------------------------|-------------------:|------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |
|  2 | aten.addmm.default                                |                  1 |           1 |
|  3 | aten.convolution.default                          |                 34 |          34 |
|  4 | aten.mean.dim                                     |                  4 |           4 |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |
|  6 | aten.relu.default                                 |                 13 |          13 |
|  7 | aten.sigmoid.default                              |                  4 |           4 |
|  8 | aten.t.default                                    |                  1 |           1 |
|  9 | aten.view.default                                 |                  1 |           1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Optional[Tensor]<[1056]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>Tensor<[1056]> running_mean = ?,<br>Tensor<[1056]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
|  1 | Tensor<[1, 1056, 96, 96]> input = ?,<br>Optional[Tensor]<[1056]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>Tensor<[1056]> running_mean = ?,<br>Tensor<[1056]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
|  2 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Optional[Tensor]<[2904]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>Tensor<[2904]> running_mean = ?,<br>Tensor<[2904]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
|  3 | Tensor<[1, 2904, 48, 48]> input = ?,<br>Optional[Tensor]<[2904]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>Tensor<[2904]> running_mean = ?,<br>Tensor<[2904]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
|  4 | Tensor<[1, 32, 192, 192]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | Done     |
|  5 | Tensor<[1, 528, 192, 192]> input = ?,<br>Optional[Tensor]<[528]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>Tensor<[528]> running_mean = ?,<br>Tensor<[528]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | Done     |
|  6 | Tensor<[1, 528, 96, 96]> input = ?,<br>Optional[Tensor]<[528]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>Tensor<[528]> running_mean = ?,<br>Tensor<[528]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | Done     |
|  7 | Tensor<[1, 7392, 12, 12]> input = ?,<br>Optional[Tensor]<[7392]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>Tensor<[7392]> running_mean = ?,<br>Tensor<[7392]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
|  8 | Tensor<[1, 7392, 24, 24]> input = ?,<br>Optional[Tensor]<[7392]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>Tensor<[7392]> running_mean = ?,<br>Tensor<[7392]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | Done     |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ? | Done     |
|  1 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ? | Done     |
|  2 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?   | Done     |
|  3 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ? | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 7392]> mat1 = ?,<br>Tensor<[7392, 1000]> mat2 = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                         | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1056, 1, 1]> input = ?,<br>Tensor<[132, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<[132]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  1 | Tensor<[1, 1056, 1, 1]> input = ?,<br>Tensor<[264, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<[264]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  2 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[1056, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  3 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[1056, 264, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 4    | Done     |
|  4 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[2904, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  5 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[2904, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  6 | Tensor<[1, 1056, 96, 96]> input = ?,<br>Tensor<[1056, 264, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 4    | Done     |
|  7 | Tensor<[1, 132, 1, 1]> input = ?,<br>Tensor<[1056, 132, 1, 1]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
|  8 | Tensor<[1, 132, 1, 1]> input = ?,<br>Tensor<[528, 132, 1, 1]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
|  9 | Tensor<[1, 264, 1, 1]> input = ?,<br>Tensor<[1056, 264, 1, 1]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 10 | Tensor<[1, 264, 1, 1]> input = ?,<br>Tensor<[2904, 264, 1, 1]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 11 | Tensor<[1, 2904, 1, 1]> input = ?,<br>Tensor<[264, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<[264]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 12 | Tensor<[1, 2904, 1, 1]> input = ?,<br>Tensor<[726, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<[726]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 13 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[2904, 264, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 11   | Done     |
| 14 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[2904, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 15 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[7392, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 16 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[7392, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 17 | Tensor<[1, 2904, 48, 48]> input = ?,<br>Tensor<[2904, 264, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 11   | Done     |
| 18 | Tensor<[1, 3, 384, 384]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1         | Done     |
| 19 | Tensor<[1, 32, 192, 192]> input = ?,<br>Tensor<[528, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
| 20 | Tensor<[1, 32, 192, 192]> input = ?,<br>Tensor<[528, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
| 21 | Tensor<[1, 528, 1, 1]> input = ?,<br>Tensor<[132, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<[132]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 22 | Tensor<[1, 528, 1, 1]> input = ?,<br>Tensor<[8, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Done     |
| 23 | Tensor<[1, 528, 192, 192]> input = ?,<br>Tensor<[528, 264, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 2    | Done     |
| 24 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[1056, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 25 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[1056, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | Done     |
| 26 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[528, 264, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 2      | Done     |
| 27 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[528, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | Done     |
| 28 | Tensor<[1, 726, 1, 1]> input = ?,<br>Tensor<[2904, 726, 1, 1]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 29 | Tensor<[1, 726, 1, 1]> input = ?,<br>Tensor<[7392, 726, 1, 1]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 30 | Tensor<[1, 7392, 1, 1]> input = ?,<br>Tensor<[726, 7392, 1, 1]> weight = ?,<br>Optional[Tensor]<[726]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | Done     |
| 31 | Tensor<[1, 7392, 12, 12]> input = ?,<br>Tensor<[7392, 7392, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | Done     |
| 32 | Tensor<[1, 7392, 24, 24]> input = ?,<br>Tensor<[7392, 264, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 28   | Done     |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[528, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | Done     |
### aten.mean.dim
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
|  1 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
|  2 | Tensor<[1, 528, 96, 96]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True  | Done     |
|  3 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ? | Done     |
|  1 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ? | Done     |
|  2 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?   | Done     |
|  3 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ? | Done     |
### aten.relu.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 1056, 48, 48]> self = ?  | Done     |
|  1 | Tensor<[1, 1056, 96, 96]> self = ?  | Done     |
|  2 | Tensor<[1, 132, 1, 1]> self = ?     | Done     |
|  3 | Tensor<[1, 264, 1, 1]> self = ?     | Done     |
|  4 | Tensor<[1, 2904, 24, 24]> self = ?  | Done     |
|  5 | Tensor<[1, 2904, 48, 48]> self = ?  | Done     |
|  6 | Tensor<[1, 32, 192, 192]> self = ?  | Done     |
|  7 | Tensor<[1, 528, 192, 192]> self = ? | Done     |
|  8 | Tensor<[1, 528, 96, 96]> self = ?   | Done     |
|  9 | Tensor<[1, 726, 1, 1]> self = ?     | Done     |
| 10 | Tensor<[1, 7392, 12, 12]> self = ?  | Done     |
| 11 | Tensor<[1, 7392, 24, 24]> self = ?  | Done     |
| 12 | Tensor<[1, 8, 1, 1]> self = ?       | Done     |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1056, 1, 1]> self = ? | Done     |
|  1 | Tensor<[1, 2904, 1, 1]> self = ? | Done     |
|  2 | Tensor<[1, 528, 1, 1]> self = ?  | Done     |
|  3 | Tensor<[1, 7392, 1, 1]> self = ? | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 7392]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 7392, 1, 1]> self = ?,<br>List[int]<> size = [1, 7392] | Done     |

