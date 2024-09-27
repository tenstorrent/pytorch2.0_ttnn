# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Generality Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 12 |           0 |         0 |          0 | ✘           |                  0 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |                  1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  3 | aten.convolution.default                          |                 23 |           0 |         0 |          0 | ✘           |                  0 |
|  4 | aten.max_pool2d_with_indices.default              |                  1 |           0 |         0 |          0 | ✘           |                  0 |
|  5 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  6 | aten.relu.default                                 |                 12 |          12 |         0 |          0 | ✅          |                  1 |
|  7 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |                  1 |
|  8 | aten.view.default                                 |                  1 |           0 |         0 |          1 | ✘           |                  0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05 | None     |
|  1 | Tensor<[1, 128, 28, 28]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  2 | Tensor<[1, 128, 56, 56]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  3 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05   | None     |
|  4 | Tensor<[1, 256, 14, 14]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  5 | Tensor<[1, 256, 28, 28]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  6 | Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  7 | Tensor<[1, 512, 14, 14]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  8 | Tensor<[1, 512, 28, 28]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05      | None     |
|  9 | Tensor<[1, 512, 7, 7]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05        | None     |
| 10 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05         | None     |
| 11 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float<> momentum = 0.1,<br>float<> eps = 1e-05           | None     |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ? | Done     |
|  1 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?     | Done     |
|  2 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?   | Done     |
|  3 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?   | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2048]> mat1 = ?,<br>Tensor<[2048, 1000]> mat2 = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1 | None     |
|  1 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
|  2 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1  | None     |
|  3 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
|  4 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[512, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
|  5 | Tensor<[1, 128, 56, 56]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
|  6 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Tensor<[512, 2048, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
|  7 | Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[1024, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
|  8 | Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
|  9 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
| 10 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
| 11 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
| 12 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 13 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [3, 3],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 14 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
| 15 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1   | None     |
| 16 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
| 17 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1    | None     |
| 18 | Tensor<[1, 512, 7, 7]> input = ?,<br>Tensor<[2048, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1     | None     |
| 19 | Tensor<[1, 512, 7, 7]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | None     |
| 20 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1      | None     |
| 21 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [0, 0],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
| 22 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<> bias = ?,<br>List[int]<> stride = [1, 1],<br>List[int]<> padding = [1, 1],<br>List[int]<> dilation = [1, 1],<br>bool<> transposed = False,<br>List[int]<> output_padding = [0, 0],<br>int<> groups = 1       | None     |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int]<> kernel_size = [3, 3],<br>List[int]<> stride = [2, 2],<br>List[int]<> padding = [1, 1] | None     |
### aten.mean.dim
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]]<> dim = [-1, -2],<br>bool<> keepdim = True | Done     |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 1024, 14, 14]> self = ? | Done     |
|  1 | Tensor<[1, 128, 28, 28]> self = ?  | Done     |
|  2 | Tensor<[1, 128, 56, 56]> self = ?  | Done     |
|  3 | Tensor<[1, 2048, 7, 7]> self = ?   | Done     |
|  4 | Tensor<[1, 256, 14, 14]> self = ?  | Done     |
|  5 | Tensor<[1, 256, 28, 28]> self = ?  | Done     |
|  6 | Tensor<[1, 256, 56, 56]> self = ?  | Done     |
|  7 | Tensor<[1, 512, 14, 14]> self = ?  | Done     |
|  8 | Tensor<[1, 512, 28, 28]> self = ?  | Done     |
|  9 | Tensor<[1, 512, 7, 7]> self = ?    | Done     |
| 10 | Tensor<[1, 64, 112, 112]> self = ? | Done     |
| 11 | Tensor<[1, 64, 56, 56]> self = ?   | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 2048]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int]<> size = [1, 2048] | Fallback |

