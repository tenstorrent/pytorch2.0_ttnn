# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 19 |           0 |         0 |          0 | ✘           |     0   |
|  1 | aten.add.Tensor                                   |                  5 |           5 |         0 |          0 | ✅          |     1   |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  3 | aten.constant_pad_nd.default                      |                  5 |           3 |         0 |          0 | 🚧          |     0.6 |
|  4 | aten.convolution.default                          |                 32 |           0 |         0 |          0 | ✘           |     0   |
|  5 | aten.hardtanh.default                             |                 12 |           0 |         0 |          0 | ✘           |     0   |
|  6 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  7 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  8 | aten.view.default                                 |                  1 |           0 |         0 |          1 | ✘           |     0   |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 10, 10]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>Tensor<[1280]> running_mean = ?,<br>Tensor<[1280]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | None     |
|  1 | Tensor<[1, 136, 19, 19]> input = ?,<br>Optional[Tensor]<[136]> weight = ?,<br>Optional[Tensor]<[136]> bias = ?,<br>Tensor<[136]> running_mean = ?,<br>Tensor<[136]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  2 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Optional[Tensor]<[1392]> weight = ?,<br>Optional[Tensor]<[1392]> bias = ?,<br>Tensor<[1392]> running_mean = ?,<br>Tensor<[1392]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | None     |
|  3 | Tensor<[1, 144, 150, 150]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001    | None     |
|  4 | Tensor<[1, 144, 75, 75]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  5 | Tensor<[1, 192, 38, 38]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  6 | Tensor<[1, 192, 75, 75]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  7 | Tensor<[1, 232, 10, 10]> input = ?,<br>Optional[Tensor]<[232]> weight = ?,<br>Optional[Tensor]<[232]> bias = ?,<br>Tensor<[232]> running_mean = ?,<br>Tensor<[232]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
|  8 | Tensor<[1, 24, 150, 150]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001         | None     |
|  9 | Tensor<[1, 288, 19, 19]> input = ?,<br>Optional[Tensor]<[288]> weight = ?,<br>Optional[Tensor]<[288]> bias = ?,<br>Tensor<[288]> running_mean = ?,<br>Tensor<[288]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 10 | Tensor<[1, 288, 38, 38]> input = ?,<br>Optional[Tensor]<[288]> weight = ?,<br>Optional[Tensor]<[288]> bias = ?,<br>Tensor<[288]> running_mean = ?,<br>Tensor<[288]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 11 | Tensor<[1, 32, 150, 150]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001         | None     |
| 12 | Tensor<[1, 32, 75, 75]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001           | None     |
| 13 | Tensor<[1, 384, 10, 10]> input = ?,<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>Tensor<[384]> running_mean = ?,<br>Tensor<[384]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 14 | Tensor<[1, 48, 38, 38]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001           | None     |
| 15 | Tensor<[1, 576, 19, 19]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 16 | Tensor<[1, 816, 10, 10]> input = ?,<br>Optional[Tensor]<[816]> weight = ?,<br>Optional[Tensor]<[816]> bias = ?,<br>Tensor<[816]> running_mean = ?,<br>Tensor<[816]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 17 | Tensor<[1, 816, 19, 19]> input = ?,<br>Optional[Tensor]<[816]> weight = ?,<br>Optional[Tensor]<[816]> bias = ?,<br>Tensor<[816]> running_mean = ?,<br>Tensor<[816]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | None     |
| 18 | Tensor<[1, 96, 19, 19]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001           | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ? | Done     |
|  1 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ? | Done     |
|  2 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?   | Done     |
|  3 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?   | Done     |
|  4 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Done     |
### aten.constant_pad_nd.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 144, 150, 150]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0 | Done     |
|  1 | Tensor<[1, 192, 75, 75]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0   | None     |
|  2 | Tensor<[1, 288, 38, 38]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0   | Done     |
|  3 | Tensor<[1, 3, 300, 300]> self = ?,<br>List[int] pad = [0, 1, 0, 1],<br>number value = 0.0   | Done     |
|  4 | Tensor<[1, 816, 19, 19]> self = ?,<br>List[int] pad = [2, 2, 2, 2],<br>number value = 0.0   | None     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 136, 19, 19]> input = ?,<br>Tensor<[816, 136, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
|  1 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Tensor<[1392, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1392 | None     |
|  2 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Tensor<[1392, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1392 | None     |
|  3 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Tensor<[232, 1392, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | None     |
|  4 | Tensor<[1, 1392, 10, 10]> input = ?,<br>Tensor<[384, 1392, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | None     |
|  5 | Tensor<[1, 144, 151, 151]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144  | None     |
|  6 | Tensor<[1, 144, 75, 75]> input = ?,<br>Tensor<[32, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
|  7 | Tensor<[1, 192, 38, 38]> input = ?,<br>Tensor<[48, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
|  8 | Tensor<[1, 192, 75, 75]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192    | None     |
|  9 | Tensor<[1, 192, 75, 75]> input = ?,<br>Tensor<[32, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 10 | Tensor<[1, 192, 79, 79]> input = ?,<br>Tensor<[192, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 192    | None     |
| 11 | Tensor<[1, 232, 10, 10]> input = ?,<br>Tensor<[1392, 232, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 12 | Tensor<[1, 24, 150, 150]> input = ?,<br>Tensor<[144, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 13 | Tensor<[1, 288, 19, 19]> input = ?,<br>Tensor<[96, 288, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 14 | Tensor<[1, 288, 38, 38]> input = ?,<br>Tensor<[288, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288    | None     |
| 15 | Tensor<[1, 288, 38, 38]> input = ?,<br>Tensor<[48, 288, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 16 | Tensor<[1, 288, 39, 39]> input = ?,<br>Tensor<[288, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288    | None     |
| 17 | Tensor<[1, 3, 301, 301]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     |
| 18 | Tensor<[1, 32, 150, 150]> input = ?,<br>Tensor<[24, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 19 | Tensor<[1, 32, 150, 150]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32     | None     |
| 20 | Tensor<[1, 32, 75, 75]> input = ?,<br>Tensor<[192, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     |
| 21 | Tensor<[1, 384, 10, 10]> input = ?,<br>Tensor<[1280, 384, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     |
| 22 | Tensor<[1, 48, 38, 38]> input = ?,<br>Tensor<[288, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     |
| 23 | Tensor<[1, 576, 19, 19]> input = ?,<br>Tensor<[136, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 24 | Tensor<[1, 576, 19, 19]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576    | None     |
| 25 | Tensor<[1, 576, 19, 19]> input = ?,<br>Tensor<[576, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576    | None     |
| 26 | Tensor<[1, 576, 19, 19]> input = ?,<br>Tensor<[96, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     |
| 27 | Tensor<[1, 816, 10, 10]> input = ?,<br>Tensor<[232, 816, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 28 | Tensor<[1, 816, 19, 19]> input = ?,<br>Tensor<[136, 816, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     |
| 29 | Tensor<[1, 816, 19, 19]> input = ?,<br>Tensor<[816, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 816    | None     |
| 30 | Tensor<[1, 816, 23, 23]> input = ?,<br>Tensor<[816, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 816    | None     |
| 31 | Tensor<[1, 96, 19, 19]> input = ?,<br>Tensor<[576, 96, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     |
### aten.hardtanh.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0  | None     |
|  1 | Tensor<[1, 1392, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0  | None     |
|  2 | Tensor<[1, 144, 150, 150]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0 | None     |
|  3 | Tensor<[1, 144, 75, 75]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  4 | Tensor<[1, 192, 38, 38]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  5 | Tensor<[1, 192, 75, 75]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  6 | Tensor<[1, 288, 19, 19]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  7 | Tensor<[1, 288, 38, 38]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
|  8 | Tensor<[1, 32, 150, 150]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0  | None     |
|  9 | Tensor<[1, 576, 19, 19]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
| 10 | Tensor<[1, 816, 10, 10]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
| 11 | Tensor<[1, 816, 19, 19]> self = ?,<br>number min_val = 0.0,<br>number max_val = 6.0   | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1280]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int] size = [1, 1280] | Fallback |

