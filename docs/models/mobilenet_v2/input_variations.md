# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 19 |           0 |         0 |          0 | ✘           |                  0 |
|  1 | aten.add.Tensor                                   |                  5 |           5 |         0 |          0 | ✅          |                  1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  3 | aten.clone.default                                |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  4 | aten.convolution.default                          |                 30 |           0 |         0 |          0 | ✘           |                  0 |
|  5 | aten.hardtanh.default                             |                 12 |           0 |         0 |          0 | ✘           |                  0 |
|  6 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  7 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  8 | aten.view.default                                 |                  1 |           0 |         0 |          1 | ✘           |                  0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 7, 7]> input = ?,<br>Optional[Tensor]<[1280]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>Tensor<[1280]> running_mean = ?,<br>Tensor<[1280]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | None     |
|  1 | Tensor<[1, 144, 28, 28]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
|  2 | Tensor<[1, 144, 56, 56]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
|  3 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | None     |
|  4 | Tensor<[1, 160, 7, 7]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  5 | Tensor<[1, 192, 14, 14]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
|  6 | Tensor<[1, 192, 28, 28]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
|  7 | Tensor<[1, 24, 56, 56]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
|  8 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | None     |
|  9 | Tensor<[1, 32, 28, 28]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 10 | Tensor<[1, 320, 7, 7]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
| 11 | Tensor<[1, 384, 14, 14]> input = ?,<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>Tensor<[384]> running_mean = ?,<br>Tensor<[384]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
| 12 | Tensor<[1, 576, 14, 14]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05    | None     |
| 13 | Tensor<[1, 576, 7, 7]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
| 14 | Tensor<[1, 64, 14, 14]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 15 | Tensor<[1, 96, 112, 112]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05       | None     |
| 16 | Tensor<[1, 96, 14, 14]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 17 | Tensor<[1, 96, 56, 56]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 18 | Tensor<[1, 960, 7, 7]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?   | Done     |
|  1 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ? | Done     |
|  2 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ? | Done     |
|  3 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ? | Done     |
|  4 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ? | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Done     |
### aten.clone.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[1, 1280]> self = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 144, 28, 28]> input = ?,<br>Tensor<[32, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
|  1 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 144 | None     |
|  2 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[144, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 144 | None     |
|  3 | Tensor<[1, 144, 56, 56]> input = ?,<br>Tensor<[24, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
|  4 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[96, 16, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
|  5 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
|  6 | Tensor<[1, 192, 14, 14]> input = ?,<br>Tensor<[64, 192, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
|  7 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 192 | None     |
|  8 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[192, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 192 | None     |
|  9 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[32, 192, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
| 10 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[144, 24, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 11 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
| 12 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[16, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
| 13 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 32  | None     |
| 14 | Tensor<[1, 32, 28, 28]> input = ?,<br>Tensor<[192, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 15 | Tensor<[1, 320, 7, 7]> input = ?,<br>Tensor<[1280, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
| 16 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[384, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 384 | None     |
| 17 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[64, 384, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
| 18 | Tensor<[1, 384, 14, 14]> input = ?,<br>Tensor<[96, 384, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
| 19 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 576 | None     |
| 20 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 576 | None     |
| 21 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[96, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
| 22 | Tensor<[1, 576, 7, 7]> input = ?,<br>Tensor<[160, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 23 | Tensor<[1, 64, 14, 14]> input = ?,<br>Tensor<[384, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 24 | Tensor<[1, 96, 112, 112]> input = ?,<br>Tensor<[96, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 96  | None     |
| 25 | Tensor<[1, 96, 14, 14]> input = ?,<br>Tensor<[576, 96, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 26 | Tensor<[1, 96, 56, 56]> input = ?,<br>Tensor<[24, 96, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
| 27 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[160, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 28 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[320, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 29 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[960, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 960   | None     |
### aten.hardtanh.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 7, 7]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0   | None     |
|  1 | Tensor<[1, 144, 28, 28]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | None     |
|  2 | Tensor<[1, 144, 56, 56]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | None     |
|  3 | Tensor<[1, 192, 14, 14]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | None     |
|  4 | Tensor<[1, 192, 28, 28]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | None     |
|  5 | Tensor<[1, 32, 112, 112]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0 | None     |
|  6 | Tensor<[1, 384, 14, 14]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | None     |
|  7 | Tensor<[1, 576, 14, 14]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0  | None     |
|  8 | Tensor<[1, 576, 7, 7]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0    | None     |
|  9 | Tensor<[1, 96, 112, 112]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0 | None     |
| 10 | Tensor<[1, 96, 56, 56]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0   | None     |
| 11 | Tensor<[1, 960, 7, 7]> self = ?,<br>number<> min_val = 0.0,<br>number<> max_val = 6.0    | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1280]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1280, 1, 1]> self = ?,<br>List[int]<> size = [1, 1280] | Fallback |

