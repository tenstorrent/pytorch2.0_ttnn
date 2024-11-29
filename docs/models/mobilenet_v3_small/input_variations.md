# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 17 |          17 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 41 |          41 |         0 |          0 | ✅          |       1 |
|  4 | aten.hardsigmoid.default                          |                  7 |           7 |         0 |          0 | ✅          |       1 |
|  5 | aten.hardswish.default                            |                 10 |          10 |         0 |          0 | ✅          |       1 |
|  6 | aten.mean.dim                                     |                  7 |           7 |         0 |          0 | ✅          |       1 |
|  7 | aten.mul.Tensor                                   |                  7 |           7 |         0 |          0 | ✅          |       1 |
|  8 | aten.relu.default                                 |                 11 |          11 |         0 |          0 | ✅          |       1 |
|  9 | aten.t.default                                    |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 10 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                               | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 14, 14]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Done       | True  |
|  1 | Tensor<[1, 144, 14, 14]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Done       | True  |
|  2 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001    | Done     | Done       | True  |
|  3 | Tensor<[1, 16, 56, 56]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
|  4 | Tensor<[1, 24, 28, 28]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
|  5 | Tensor<[1, 240, 14, 14]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Done       | True  |
|  6 | Tensor<[1, 288, 14, 14]> input = ?,<br>Optional[Tensor]<[288]> weight = ?,<br>Optional[Tensor]<[288]> bias = ?,<br>Tensor<[288]> running_mean = ?,<br>Tensor<[288]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Done       | True  |
|  7 | Tensor<[1, 288, 7, 7]> input = ?,<br>Optional[Tensor]<[288]> weight = ?,<br>Optional[Tensor]<[288]> bias = ?,<br>Tensor<[288]> running_mean = ?,<br>Tensor<[288]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001   | Done     | Done       | True  |
|  8 | Tensor<[1, 40, 14, 14]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
|  9 | Tensor<[1, 48, 14, 14]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
| 10 | Tensor<[1, 576, 7, 7]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001   | Done     | Done       | True  |
| 11 | Tensor<[1, 72, 28, 28]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
| 12 | Tensor<[1, 72, 56, 56]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
| 13 | Tensor<[1, 88, 28, 28]> input = ?,<br>Optional[Tensor]<[88]> weight = ?,<br>Optional[Tensor]<[88]> bias = ?,<br>Tensor<[88]> running_mean = ?,<br>Tensor<[88]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
| 14 | Tensor<[1, 96, 14, 14]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
| 15 | Tensor<[1, 96, 28, 28]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Done       | True  |
| 16 | Tensor<[1, 96, 7, 7]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001        | Done     | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?     | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1, 576]> mat1 = ?,<br>Tensor<[576, 1024]> mat2 = ?   | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  1 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120      | Done     | Done       | True  |
|  2 | Tensor<[1, 120, 14, 14]> input = ?,<br>Tensor<[48, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
|  3 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[40, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  4 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[576, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  5 | Tensor<[1, 144, 14, 14]> input = ?,<br>Tensor<[144, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 144      | Done     | Done       | True  |
|  6 | Tensor<[1, 144, 14, 14]> input = ?,<br>Tensor<[48, 144, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
|  7 | Tensor<[1, 16, 1, 1]> input = ?,<br>Tensor<[8, 16, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
|  8 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16       | Done     | Done       | True  |
|  9 | Tensor<[1, 16, 56, 56]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 10 | Tensor<[1, 16, 56, 56]> input = ?,<br>Tensor<[72, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 11 | Tensor<[1, 24, 1, 1]> input = ?,<br>Tensor<[96, 24, 1, 1]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 12 | Tensor<[1, 24, 28, 28]> input = ?,<br>Tensor<[88, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 13 | Tensor<[1, 24, 28, 28]> input = ?,<br>Tensor<[96, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 14 | Tensor<[1, 240, 1, 1]> input = ?,<br>Tensor<[64, 240, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 15 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[240, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240      | Done     | Done       | True  |
| 16 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[40, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 17 | Tensor<[1, 288, 1, 1]> input = ?,<br>Tensor<[72, 288, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 18 | Tensor<[1, 288, 14, 14]> input = ?,<br>Tensor<[288, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 288      | Done     | Done       | True  |
| 19 | Tensor<[1, 288, 7, 7]> input = ?,<br>Tensor<[96, 288, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 20 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 21 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 22 | Tensor<[1, 40, 1, 1]> input = ?,<br>Tensor<[144, 40, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 23 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | True  |
| 24 | Tensor<[1, 40, 14, 14]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | True  |
| 25 | Tensor<[1, 48, 14, 14]> input = ?,<br>Tensor<[144, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | True  |
| 26 | Tensor<[1, 48, 14, 14]> input = ?,<br>Tensor<[288, 48, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | True  |
| 27 | Tensor<[1, 576, 1, 1]> input = ?,<br>Tensor<[144, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
| 28 | Tensor<[1, 576, 7, 7]> input = ?,<br>Tensor<[576, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 576        | Done     | Done       | True  |
| 29 | Tensor<[1, 576, 7, 7]> input = ?,<br>Tensor<[96, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 30 | Tensor<[1, 64, 1, 1]> input = ?,<br>Tensor<[240, 64, 1, 1]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 31 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[288, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[288]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 32 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 33 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72         | Done     | Done       | True  |
| 34 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[16, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 35 | Tensor<[1, 88, 28, 28]> input = ?,<br>Tensor<[24, 88, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 36 | Tensor<[1, 88, 28, 28]> input = ?,<br>Tensor<[88, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 88         | Done     | Done       | True  |
| 37 | Tensor<[1, 96, 1, 1]> input = ?,<br>Tensor<[24, 96, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 38 | Tensor<[1, 96, 14, 14]> input = ?,<br>Tensor<[40, 96, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 39 | Tensor<[1, 96, 28, 28]> input = ?,<br>Tensor<[96, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 96         | Done     | Done       | True  |
| 40 | Tensor<[1, 96, 7, 7]> input = ?,<br>Tensor<[576, 96, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | True  |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   |
|---:|:--------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 144, 1, 1]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 16, 1, 1]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 240, 1, 1]> self = ? | Done     | Done       | True  |
|  4 | Tensor<[1, 288, 1, 1]> self = ? | Done     | Done       | True  |
|  5 | Tensor<[1, 576, 1, 1]> self = ? | Done     | Done       | True  |
|  6 | Tensor<[1, 96, 1, 1]> self = ?  | Done     | Done       | True  |
### aten.hardswish.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024]> self = ?         | Done     | Done       | True  |
|  1 | Tensor<[1, 120, 14, 14]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1, 144, 14, 14]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 16, 112, 112]> self = ? | Done     | Done       | True  |
|  4 | Tensor<[1, 240, 14, 14]> self = ?  | Done     | Done       | True  |
|  5 | Tensor<[1, 288, 14, 14]> self = ?  | Done     | Done       | True  |
|  6 | Tensor<[1, 288, 7, 7]> self = ?    | Done     | Done       | True  |
|  7 | Tensor<[1, 576, 7, 7]> self = ?    | Done     | Done       | True  |
|  8 | Tensor<[1, 96, 14, 14]> self = ?   | Done     | Done       | True  |
|  9 | Tensor<[1, 96, 28, 28]> self = ?   | Done     | Done       | True  |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | False |
|  1 | Tensor<[1, 144, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | False |
|  2 | Tensor<[1, 16, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | False |
|  3 | Tensor<[1, 240, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | False |
|  4 | Tensor<[1, 288, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | False |
|  5 | Tensor<[1, 576, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Done       | False |
|  6 | Tensor<[1, 96, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | False |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?   | Done     | Done       | True  |
|  3 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ? | Done     | Done       | True  |
|  4 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?   | Done     | Done       | True  |
|  5 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?   | Done     | Done       | True  |
|  6 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?   | Done     | Done       | True  |
### aten.relu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 144, 1, 1]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[1, 16, 56, 56]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 24, 1, 1]> self = ?   | Done     | Done       | True  |
|  3 | Tensor<[1, 32, 1, 1]> self = ?   | Done     | Done       | True  |
|  4 | Tensor<[1, 40, 1, 1]> self = ?   | Done     | Done       | True  |
|  5 | Tensor<[1, 64, 1, 1]> self = ?   | Done     | Done       | True  |
|  6 | Tensor<[1, 72, 1, 1]> self = ?   | Done     | Done       | True  |
|  7 | Tensor<[1, 72, 28, 28]> self = ? | Done     | Done       | True  |
|  8 | Tensor<[1, 72, 56, 56]> self = ? | Done     | Done       | True  |
|  9 | Tensor<[1, 8, 1, 1]> self = ?    | Done     | Done       | True  |
| 10 | Tensor<[1, 88, 28, 28]> self = ? | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 1024]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1024, 576]> self = ?  | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 576, 1, 1]> self = ?,<br>List[int] size = [1, 576] | Done     | Done       | True  |

