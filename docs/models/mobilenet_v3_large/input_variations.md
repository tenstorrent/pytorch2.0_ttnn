# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 19 |          19 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  6 |           6 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 44 |          44 |         0 |          0 | ✅          |       1 |
|  4 | aten.hardsigmoid.default                          |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  5 | aten.hardswish.default                            |                 10 |          10 |         0 |          0 | ✅          |       1 |
|  6 | aten.mean.dim                                     |                  6 |           6 |         0 |          0 | ✅          |       1 |
|  7 | aten.mul.Tensor                                   |                  6 |           6 |         0 |          0 | ✅          |       1 |
|  8 | aten.relu.default                                 |                 11 |          11 |         0 |          0 | ✅          |       1 |
|  9 | aten.t.default                                    |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 10 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 112, 14, 14]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 120, 28, 28]> input = ?,<br>Optional[Tensor]<[120]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>Tensor<[120]> running_mean = ?,<br>Tensor<[120]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 112, 112]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001    | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 160, 7, 7]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 184, 14, 14]> input = ?,<br>Optional[Tensor]<[184]> weight = ?,<br>Optional[Tensor]<[184]> bias = ?,<br>Tensor<[184]> running_mean = ?,<br>Tensor<[184]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 200, 14, 14]> input = ?,<br>Optional[Tensor]<[200]> weight = ?,<br>Optional[Tensor]<[200]> bias = ?,<br>Tensor<[200]> running_mean = ?,<br>Tensor<[200]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 24, 56, 56]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 240, 14, 14]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 240, 28, 28]> input = ?,<br>Optional[Tensor]<[240]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>Tensor<[240]> running_mean = ?,<br>Tensor<[240]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 40, 28, 28]> input = ?,<br>Optional[Tensor]<[40]> weight = ?,<br>Optional[Tensor]<[40]> bias = ?,<br>Tensor<[40]> running_mean = ?,<br>Tensor<[40]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 480, 14, 14]> input = ?,<br>Optional[Tensor]<[480]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>Tensor<[480]> running_mean = ?,<br>Tensor<[480]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001    | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 672, 14, 14]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001 | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 672, 7, 7]> input = ?,<br>Optional[Tensor]<[672]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>Tensor<[672]> running_mean = ?,<br>Tensor<[672]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001   | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 72, 28, 28]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 72, 56, 56]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 80, 14, 14]> input = ?,<br>Optional[Tensor]<[80]> weight = ?,<br>Optional[Tensor]<[80]> bias = ?,<br>Tensor<[80]> running_mean = ?,<br>Tensor<[80]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001      | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 960, 7, 7]> input = ?,<br>Optional[Tensor]<[960]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>Tensor<[960]> running_mean = ?,<br>Tensor<[960]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 0.001   | Done     | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?       | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?     | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?     | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?     | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1280]> mat1 = ?,<br>Tensor<[1280, 1000]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1280]> self = ?,<br>Tensor<[1, 960]> mat1 = ?,<br>Tensor<[960, 1280]> mat2 = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[672, 112, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[32, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 120, 1, 1]> input = ?,<br>Tensor<[480, 120, 1, 1]> weight = ?,<br>Optional[Tensor]<[480]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[120, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 120      | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 120, 28, 28]> input = ?,<br>Tensor<[40, 120, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 16       | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[16, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 16, 112, 112]> input = ?,<br>Tensor<[64, 16, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[960, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 168, 1, 1]> input = ?,<br>Tensor<[672, 168, 1, 1]> weight = ?,<br>Optional[Tensor]<[672]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 184, 14, 14]> input = ?,<br>Tensor<[184, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 184      | Done     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 184, 14, 14]> input = ?,<br>Tensor<[80, 184, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 200, 14, 14]> input = ?,<br>Tensor<[200, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 200      | Done     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 200, 14, 14]> input = ?,<br>Tensor<[80, 200, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 24, 1, 1]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 24, 56, 56]> input = ?,<br>Tensor<[72, 24, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 240, 1, 1]> input = ?,<br>Tensor<[960, 240, 1, 1]> weight = ?,<br>Optional[Tensor]<[960]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 240, 14, 14]> input = ?,<br>Tensor<[80, 240, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 240, 28, 28]> input = ?,<br>Tensor<[240, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 240      | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[16, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 32, 1, 1]> input = ?,<br>Tensor<[120, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[120, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 40, 28, 28]> input = ?,<br>Tensor<[240, 40, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 480, 1, 1]> input = ?,<br>Tensor<[120, 480, 1, 1]> weight = ?,<br>Optional[Tensor]<[120]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[112, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[480, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 480      | Done     | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 64, 112, 112]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64       | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[24, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 672, 1, 1]> input = ?,<br>Tensor<[168, 672, 1, 1]> weight = ?,<br>Optional[Tensor]<[168]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[112, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672      | Done     | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 672, 14, 14]> input = ?,<br>Tensor<[672, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 672      | Done     | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 672, 7, 7]> input = ?,<br>Tensor<[160, 672, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 72, 28, 28]> input = ?,<br>Tensor<[40, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[24, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72         | Done     | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 72         | Done     | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[184, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[200, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, 80, 14, 14]> input = ?,<br>Tensor<[480, 80, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, 960, 1, 1]> input = ?,<br>Tensor<[240, 960, 1, 1]> weight = ?,<br>Optional[Tensor]<[240]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[160, 960, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1, 960, 7, 7]> input = ?,<br>Tensor<[960, 1, 5, 5]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 960        | Done     | Unknown    | N/A   | N/A    |
### aten.hardsigmoid.default
|    | ATen Input Variations           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 120, 1, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 480, 1, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 672, 1, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 72, 1, 1]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 960, 1, 1]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.hardswish.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1280]> self = ?         | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, 112, 112]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 184, 14, 14]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 200, 14, 14]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 240, 14, 14]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 240, 28, 28]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 480, 14, 14]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 672, 14, 14]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 672, 7, 7]> self = ?    | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 960, 7, 7]> self = ?    | Done     | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 120, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 480, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 672, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 672, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 72, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 960, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True   | Done     | Unknown    | N/A   | N/A    |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?   | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?   | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 120, 1, 1]> self = ?    | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 120, 28, 28]> self = ?  | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 112, 112]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 168, 1, 1]> self = ?    | Done     | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 24, 1, 1]> self = ?     | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 240, 1, 1]> self = ?    | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 32, 1, 1]> self = ?     | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 64, 112, 112]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 64, 56, 56]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 72, 28, 28]> self = ?   | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 72, 56, 56]> self = ?   | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1000, 1280]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1280, 960]> self = ?  | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 960, 1, 1]> self = ?,<br>List[int] size = [1, 960] | Done     | Unknown    | N/A   | N/A    |

