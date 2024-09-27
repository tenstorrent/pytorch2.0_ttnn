# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 19 |           0 |         0 |          0 | ✘           |                0   |
|  1 | aten.add.Tensor                                   |                  5 |           5 |         0 |          0 | ✅          |                1   |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |                1   |
|  3 | aten.constant_pad_nd.default                      |                  5 |           3 |         0 |          0 | 🚧          |                0.6 |
|  4 | aten.convolution.default                          |                 32 |           0 |         0 |          0 | ✘           |                0   |
|  5 | aten.hardtanh.default                             |                 12 |           0 |         0 |          0 | ✘           |                0   |
|  6 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |                1   |
|  7 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |                1   |
|  8 | aten.view.default                                 |                  1 |           0 |         0 |          1 | ✘           |                0   |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 24, 24]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  1 | Tensor<[1, 1280, 12, 12]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>Tensor<[1280]> running_mean = ?,<br>Tensor<[1280]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | None     |
|  2 | Tensor<[1, 144, 190, 190]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001    | None     |
|  3 | Tensor<[1, 144, 95, 95]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  4 | Tensor<[1, 160, 24, 24]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  5 | Tensor<[1, 1632, 12, 12]> input = ?,<br>Optional[Tensor]<[1632]> weight = ?,<br>Optional[Tensor]<[1632]> bias = ?,<br>Tensor<[1632]> running_mean = ?,<br>Tensor<[1632]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | None     |
|  6 | Tensor<[1, 192, 48, 48]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  7 | Tensor<[1, 192, 95, 95]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  8 | Tensor<[1, 24, 190, 190]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001         | None     |
|  9 | Tensor<[1, 272, 12, 12]> input = ?,<br>Optional[Tensor]<[272]> weight = ?,<br>Optional[Tensor]<[272]> bias = ?,<br>Tensor<[272]> running_mean = ?,<br>Tensor<[272]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 10 | Tensor<[1, 32, 190, 190]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001         | None     |
| 11 | Tensor<[1, 32, 95, 95]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001           | None     |
| 12 | Tensor<[1, 336, 24, 24]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 13 | Tensor<[1, 336, 48, 48]> input = ?,<br>Optional[Tensor]<[336]> weight = ?,<br>Optional[Tensor]<[336]> bias = ?,<br>Tensor<[336]> running_mean = ?,<br>Tensor<[336]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 14 | Tensor<[1, 448, 12, 12]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 15 | Tensor<[1, 56, 48, 48]> input = ?,<br>Optional[Tensor]<[56]> weight = ?,<br>Optional[Tensor]<[56]> bias = ?,<br>Tensor<[56]> running_mean = ?,<br>Tensor<[56]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001           | None     |
| 16 | Tensor<[1, 672, 24, 24]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 17 | Tensor<[1, 960, 12, 12]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 18 | Tensor<[1, 960, 24, 24]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ? | Done     |
|  1 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ? | Done     |
|  2 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ? | Done     |
|  3 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?   | Done     |
|  4 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 144, 190, 190]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0 | Done     |
|  1 | Tensor<[1, 192, 95, 95]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0   | None     |
|  2 | Tensor<[1, 3, 380, 380]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0   | Done     |
|  3 | Tensor<[1, 336, 48, 48]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0   | Done     |
|  4 | Tensor<[1, 960, 24, 24]> self = ?,<br>List[int] pad = [1, 2, 1, 2],<br>number value = 0.0   | None     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 112, 24, 24]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
|  1 | Tensor<[1, 144, 191, 191]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144  | None     |
|  2 | Tensor<[1, 144, 95, 95]> input = ?,<br>Tensor<[32, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
|  3 | Tensor<[1, 160, 24, 24]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
|  4 | Tensor<[1, 1632, 12, 12]> input = ?,<br>Tensor<[1632, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1632 | None     |
|  5 | Tensor<[1, 1632, 12, 12]> input = ?,<br>Tensor<[1632, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1632 | None     |
|  6 | Tensor<[1, 1632, 12, 12]> input = ?,<br>Tensor<[272, 1632, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | None     |
|  7 | Tensor<[1, 1632, 12, 12]> input = ?,<br>Tensor<[448, 1632, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | None     |
|  8 | Tensor<[1, 192, 48, 48]> input = ?,<br>Tensor<[56, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
|  9 | Tensor<[1, 192, 95, 95]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192    | None     |
| 10 | Tensor<[1, 192, 95, 95]> input = ?,<br>Tensor<[32, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 11 | Tensor<[1, 192, 99, 99]> input = ?,<br>Tensor<[192, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192    | None     |
| 12 | Tensor<[1, 24, 190, 190]> input = ?,<br>Tensor<[144, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 13 | Tensor<[1, 272, 12, 12]> input = ?,<br>Tensor<[1632, 272, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 14 | Tensor<[1, 3, 381, 381]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
| 15 | Tensor<[1, 32, 190, 190]> input = ?,<br>Tensor<[24, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 16 | Tensor<[1, 32, 190, 190]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32     | None     |
| 17 | Tensor<[1, 32, 95, 95]> input = ?,<br>Tensor<[192, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     |
| 18 | Tensor<[1, 336, 24, 24]> input = ?,<br>Tensor<[112, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 19 | Tensor<[1, 336, 48, 48]> input = ?,<br>Tensor<[336, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 336    | None     |
| 20 | Tensor<[1, 336, 48, 48]> input = ?,<br>Tensor<[56, 336, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 21 | Tensor<[1, 336, 49, 49]> input = ?,<br>Tensor<[336, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 336    | None     |
| 22 | Tensor<[1, 448, 12, 12]> input = ?,<br>Tensor<[1280, 448, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 23 | Tensor<[1, 56, 48, 48]> input = ?,<br>Tensor<[336, 56, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     |
| 24 | Tensor<[1, 672, 24, 24]> input = ?,<br>Tensor<[112, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 25 | Tensor<[1, 672, 24, 24]> input = ?,<br>Tensor<[160, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 26 | Tensor<[1, 672, 24, 24]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672    | None     |
| 27 | Tensor<[1, 672, 24, 24]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672    | None     |
| 28 | Tensor<[1, 960, 12, 12]> input = ?,<br>Tensor<[272, 960, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 29 | Tensor<[1, 960, 24, 24]> input = ?,<br>Tensor<[160, 960, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 30 | Tensor<[1, 960, 24, 24]> input = ?,<br>Tensor<[960, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960    | None     |
| 31 | Tensor<[1, 960, 27, 27]> input = ?,<br>Tensor<[960, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960    | None     |
### aten.hardtanh.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 12, 12]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0  | None     |
|  1 | Tensor<[1, 144, 190, 190]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | None     |
|  2 | Tensor<[1, 144, 95, 95]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  3 | Tensor<[1, 1632, 12, 12]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0  | None     |
|  4 | Tensor<[1, 192, 48, 48]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  5 | Tensor<[1, 192, 95, 95]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  6 | Tensor<[1, 32, 190, 190]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0  | None     |
|  7 | Tensor<[1, 336, 24, 24]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  8 | Tensor<[1, 336, 48, 48]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  9 | Tensor<[1, 672, 24, 24]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
| 10 | Tensor<[1, 960, 12, 12]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
| 11 | Tensor<[1, 960, 24, 24]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 12, 12]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1280]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280] | Fallback |

