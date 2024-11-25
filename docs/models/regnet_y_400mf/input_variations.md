# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 34 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.mean.dim                                     |                  4 |           1 |         3 |          0 | ✅          |       1 |
|  5 | aten.mul.Tensor                                   |                  4 |           0 |         4 |          0 | ✅          |       1 |
|  6 | aten.relu.default                                 |                 14 |           4 |        10 |          0 | ✅          |       1 |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  8 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 104, 28, 28]> input = ?,<br>Optional[Tensor]<[104]> weight = ?,<br>Optional[Tensor]<[104]> bias = ?,<br>Tensor<[104]> running_mean = ?,<br>Tensor<[104]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   | True  |
|  1 | Tensor<[1, 104, 56, 56]> input = ?,<br>Optional[Tensor]<[104]> weight = ?,<br>Optional[Tensor]<[104]> bias = ?,<br>Tensor<[104]> running_mean = ?,<br>Tensor<[104]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   | True  |
|  2 | Tensor<[1, 208, 14, 14]> input = ?,<br>Optional[Tensor]<[208]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>Tensor<[208]> running_mean = ?,<br>Tensor<[208]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   | True  |
|  3 | Tensor<[1, 208, 28, 28]> input = ?,<br>Optional[Tensor]<[208]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>Tensor<[208]> running_mean = ?,<br>Tensor<[208]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   | True  |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   | True  |
|  5 | Tensor<[1, 440, 14, 14]> input = ?,<br>Optional[Tensor]<[440]> weight = ?,<br>Optional[Tensor]<[440]> bias = ?,<br>Tensor<[440]> running_mean = ?,<br>Tensor<[440]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   | True  |
|  6 | Tensor<[1, 440, 7, 7]> input = ?,<br>Optional[Tensor]<[440]> weight = ?,<br>Optional[Tensor]<[440]> bias = ?,<br>Tensor<[440]> running_mean = ?,<br>Tensor<[440]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Fallback   | True  |
|  7 | Tensor<[1, 48, 112, 112]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   | True  |
|  8 | Tensor<[1, 48, 56, 56]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Fallback   | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?     | Done     | Done       | True  |
|  3 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?   | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 440]> mat1 = ?,<br>Tensor<[440, 1000]> mat2 = ? | Removed  | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 104, 1, 1]> input = ?,<br>Tensor<[12, 104, 1, 1]> weight = ?,<br>Optional[Tensor]<[12]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
|  1 | Tensor<[1, 104, 1, 1]> input = ?,<br>Tensor<[26, 104, 1, 1]> weight = ?,<br>Optional[Tensor]<[26]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
|  2 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[104, 104, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Fallback   | True  |
|  3 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[104, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 13       | None     | Fallback   | True  |
|  4 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[208, 104, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Fallback   | True  |
|  5 | Tensor<[1, 104, 28, 28]> input = ?,<br>Tensor<[208, 104, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Fallback   | True  |
|  6 | Tensor<[1, 104, 56, 56]> input = ?,<br>Tensor<[104, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 13       | None     | Fallback   | True  |
|  7 | Tensor<[1, 110, 1, 1]> input = ?,<br>Tensor<[440, 110, 1, 1]> weight = ?,<br>Optional[Tensor]<[440]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
|  8 | Tensor<[1, 12, 1, 1]> input = ?,<br>Tensor<[104, 12, 1, 1]> weight = ?,<br>Optional[Tensor]<[104]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
|  9 | Tensor<[1, 208, 1, 1]> input = ?,<br>Tensor<[26, 208, 1, 1]> weight = ?,<br>Optional[Tensor]<[26]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
| 10 | Tensor<[1, 208, 1, 1]> input = ?,<br>Tensor<[52, 208, 1, 1]> weight = ?,<br>Optional[Tensor]<[52]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
| 11 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[208, 208, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Fallback   | True  |
| 12 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[208, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 26       | None     | Fallback   | True  |
| 13 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[440, 208, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Fallback   | True  |
| 14 | Tensor<[1, 208, 14, 14]> input = ?,<br>Tensor<[440, 208, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Fallback   | True  |
| 15 | Tensor<[1, 208, 28, 28]> input = ?,<br>Tensor<[208, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 26       | None     | Fallback   | True  |
| 16 | Tensor<[1, 26, 1, 1]> input = ?,<br>Tensor<[104, 26, 1, 1]> weight = ?,<br>Optional[Tensor]<[104]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
| 17 | Tensor<[1, 26, 1, 1]> input = ?,<br>Tensor<[208, 26, 1, 1]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
| 18 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Fallback   | True  |
| 19 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[48, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Fallback   | True  |
| 20 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[48, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Fallback   | True  |
| 21 | Tensor<[1, 440, 1, 1]> input = ?,<br>Tensor<[110, 440, 1, 1]> weight = ?,<br>Optional[Tensor]<[110]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
| 22 | Tensor<[1, 440, 1, 1]> input = ?,<br>Tensor<[52, 440, 1, 1]> weight = ?,<br>Optional[Tensor]<[52]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
| 23 | Tensor<[1, 440, 14, 14]> input = ?,<br>Tensor<[440, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 55       | None     | Fallback   | True  |
| 24 | Tensor<[1, 440, 7, 7]> input = ?,<br>Tensor<[440, 440, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | Fallback   | True  |
| 25 | Tensor<[1, 440, 7, 7]> input = ?,<br>Tensor<[440, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 55         | None     | Fallback   | True  |
| 26 | Tensor<[1, 48, 1, 1]> input = ?,<br>Tensor<[8, 48, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Fallback   | True  |
| 27 | Tensor<[1, 48, 112, 112]> input = ?,<br>Tensor<[48, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 6        | None     | Fallback   | True  |
| 28 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[104, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | Fallback   | True  |
| 29 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[104, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | Fallback   | True  |
| 30 | Tensor<[1, 48, 56, 56]> input = ?,<br>Tensor<[48, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Fallback   | True  |
| 31 | Tensor<[1, 52, 1, 1]> input = ?,<br>Tensor<[208, 52, 1, 1]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
| 32 | Tensor<[1, 52, 1, 1]> input = ?,<br>Tensor<[440, 52, 1, 1]> weight = ?,<br>Optional[Tensor]<[440]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | None     | Fallback   | True  |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[48, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Fallback   | True  |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 104, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Removed  | Done       | False |
|  1 | Tensor<[1, 208, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Removed  | Done       | False |
|  2 | Tensor<[1, 440, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | False |
|  3 | Tensor<[1, 48, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Removed  | Done       | False |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ? | Removed  | Done       | True  |
|  1 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ? | Removed  | Done       | True  |
|  2 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?   | Removed  | Done       | True  |
|  3 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?   | Removed  | Done       | True  |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 104, 28, 28]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[1, 104, 56, 56]> self = ?  | Removed  | Done       | True  |
|  2 | Tensor<[1, 110, 1, 1]> self = ?    | Removed  | Done       | True  |
|  3 | Tensor<[1, 12, 1, 1]> self = ?     | Removed  | Done       | True  |
|  4 | Tensor<[1, 208, 14, 14]> self = ?  | Done     | Done       | True  |
|  5 | Tensor<[1, 208, 28, 28]> self = ?  | Removed  | Done       | True  |
|  6 | Tensor<[1, 26, 1, 1]> self = ?     | Removed  | Done       | True  |
|  7 | Tensor<[1, 32, 112, 112]> self = ? | Removed  | Done       | True  |
|  8 | Tensor<[1, 440, 14, 14]> self = ?  | Removed  | Done       | True  |
|  9 | Tensor<[1, 440, 7, 7]> self = ?    | Done     | Done       | True  |
| 10 | Tensor<[1, 48, 112, 112]> self = ? | Removed  | Done       | True  |
| 11 | Tensor<[1, 48, 56, 56]> self = ?   | Done     | Done       | True  |
| 12 | Tensor<[1, 52, 1, 1]> self = ?     | Removed  | Done       | True  |
| 13 | Tensor<[1, 8, 1, 1]> self = ?      | Removed  | Done       | True  |
### aten.sigmoid.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 104, 1, 1]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 208, 1, 1]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 440, 1, 1]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 48, 1, 1]> self = ?  | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 440]> self = ? | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 440, 1, 1]> self = ?,<br>List[int] size = [1, 440] | Done     | Done       | True  |

