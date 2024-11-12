# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                                |                  1 |           0 |         0 |          1 | ✘           |    0    |
|  3 | aten.convolution.default                          |                 20 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  5 | aten.relu.default                                 |                  9 |           1 |         0 |          8 | 🚧          |    0.11 |
|  6 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1920, 14, 14]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>Tensor<[1920]> running_mean = ?,<br>Tensor<[1920]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 1920, 7, 7]> input = ?,<br>Optional[Tensor]<[1920]> weight = ?,<br>Optional[Tensor]<[1920]> bias = ?,<br>Tensor<[1920]> running_mean = ?,<br>Tensor<[1920]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 240, 28, 28]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 240, 56, 56]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 720, 14, 14]> input = ?,<br>Optional[Tensor]<[720]> weight = ?,<br>Optional[Tensor]<[720]> bias = ?,<br>Tensor<[720]> running_mean = ?,<br>Tensor<[720]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 720, 28, 28]> input = ?,<br>Optional[Tensor]<[720]> weight = ?,<br>Optional[Tensor]<[720]> bias = ?,<br>Tensor<[720]> running_mean = ?,<br>Tensor<[720]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 80, 112, 112]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | None     | Unknown    | N/A   |
|  8 | Tensor<[1, 80, 56, 56]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | None     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?   | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ? | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ? | Done     | Unknown    | N/A   |
|  3 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?   | Done     | Unknown    | N/A   |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1920]> mat1 = ?,<br>Tensor<[1920, 1000]> mat2 = ? | Fallback | Unknown    | N/A   |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1920, 14, 14]> input = ?,<br>Tensor<[1920, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16 | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 1920, 7, 7]> input = ?,<br>Tensor<[1920, 1920, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2    | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[720, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     | Unknown    | N/A   |
|  5 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[720, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     | Unknown    | N/A   |
|  6 | Tensor<[1, 240, 56, 56]> input = ?,<br>Tensor<[240, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2    | None     | Unknown    | N/A   |
|  7 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Unknown    | N/A   |
|  8 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[80, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Unknown    | N/A   |
|  9 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[80, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Unknown    | N/A   |
| 10 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[1920, 720, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
| 11 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[1920, 720, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Unknown    | N/A   |
| 12 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[720, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6    | None     | Unknown    | N/A   |
| 13 | Tensor<[1, 720, 14, 14]> input = ?,<br>Tensor<[720, 720, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | None     | Unknown    | N/A   |
| 14 | Tensor<[1, 720, 28, 28]> input = ?,<br>Tensor<[720, 120, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6    | None     | Unknown    | N/A   |
| 15 | Tensor<[1, 80, 112, 112]> input = ?,<br>Tensor<[80, 80, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Unknown    | N/A   |
| 16 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[240, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Unknown    | N/A   |
| 17 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[240, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Unknown    | N/A   |
| 18 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[80, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Unknown    | N/A   |
| 19 | Tensor<[1, 80, 56, 56]> input = ?,<br>Tensor<[80, 80, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Unknown    | N/A   |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Unknown    | N/A   |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1920, 14, 14]> self = ? | Fallback | Unknown    | N/A   |
|  1 | Tensor<[1, 1920, 7, 7]> self = ?   | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 240, 28, 28]> self = ?  | Fallback | Unknown    | N/A   |
|  3 | Tensor<[1, 240, 56, 56]> self = ?  | Fallback | Unknown    | N/A   |
|  4 | Tensor<[1, 32, 112, 112]> self = ? | Fallback | Unknown    | N/A   |
|  5 | Tensor<[1, 720, 14, 14]> self = ?  | Fallback | Unknown    | N/A   |
|  6 | Tensor<[1, 720, 28, 28]> self = ?  | Fallback | Unknown    | N/A   |
|  7 | Tensor<[1, 80, 112, 112]> self = ? | Fallback | Unknown    | N/A   |
|  8 | Tensor<[1, 80, 56, 56]> self = ?   | Fallback | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 1920]> self = ? | Done     | Unknown    | N/A   |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1920, 1, 1]> self = ?,<br>List[int] size = [1, 1920] | Done     | Unknown    | N/A   |

