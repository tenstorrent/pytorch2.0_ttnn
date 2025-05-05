# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 12 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten.add.Tensor                                   |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.addmm.default                                |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.clone.default                                |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.convolution.default                          |                 33 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.mean.dim                                     |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.relu.default                                 |                 12 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.t.default                                    |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.view.default                                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 10, 10]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Unknown  | Done       | 0.999989 |     -1 |
|  1 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Unknown  | Done       | 0.999987 |     -1 |
|  2 | Tensor<[1, 128, 150, 150]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001    | Unknown  | Done       | 0.999987 |     -1 |
|  3 | Tensor<[1, 128, 75, 75]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  | Done       | 0.999987 |     -1 |
|  4 | Tensor<[1, 1536, 10, 10]> input = ?,<br>Optional[Tensor]<[1536]> weight = ?,<br>Optional[Tensor]<[1536]> bias = ?,<br>Tensor<[1536]> running_mean = ?,<br>Tensor<[1536]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Unknown  | Done       | 0.999988 |     -1 |
|  5 | Tensor<[1, 2048, 10, 10]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Unknown  | Done       | 0.999988 |     -1 |
|  6 | Tensor<[1, 256, 38, 38]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  | Done       | 0.99999  |     -1 |
|  7 | Tensor<[1, 256, 75, 75]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  | Done       | 0.999988 |     -1 |
|  8 | Tensor<[1, 32, 150, 150]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001         | Unknown  | Done       | 0.99999  |     -1 |
|  9 | Tensor<[1, 64, 150, 150]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001         | Unknown  | Done       | 0.999991 |     -1 |
| 10 | Tensor<[1, 728, 19, 19]> input = ?,<br>Optional[Tensor]<[728]> weight = ?,<br>Optional[Tensor]<[728]> bias = ?,<br>Tensor<[728]> running_mean = ?,<br>Tensor<[728]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  | Done       | 0.999985 |     -1 |
| 11 | Tensor<[1, 728, 38, 38]> input = ?,<br>Optional[Tensor]<[728]> weight = ?,<br>Optional[Tensor]<[728]> bias = ?,<br>Tensor<[728]> running_mean = ?,<br>Tensor<[728]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Unknown  | Done       | 0.99999  |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ? | Unknown  | Done       | 0.999998 |     -1 |
|  1 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?   | Unknown  | Done       | 0.999998 |     -1 |
|  2 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?   | Unknown  | Done       | 0.999998 |     -1 |
|  3 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?   | Unknown  | Done       | 0.999998 |     -1 |
|  4 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?   | Unknown  | Done       | 0.999998 |     -1 |
|  5 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?   | Unknown  | Done       | 0.999998 |     -1 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |     PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|--------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2048]> mat1 = ?,<br>Tensor<[2048, 1000]> mat2 = ? | Unknown  | Done       | 0.99995 |     -1 |
### aten.clone.default
|    | ATen Input Variations      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048]> self = ? | Unknown  | Done       |     1 |     -1 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 10, 10]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | Unknown  | Done       | 0.999985 |     -1 |
|  1 | Tensor<[1, 1024, 10, 10]> input = ?,<br>Tensor<[1024, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.999965 |     -1 |
|  2 | Tensor<[1, 1024, 10, 10]> input = ?,<br>Tensor<[1536, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.999966 |     -1 |
|  3 | Tensor<[1, 1024, 19, 19]> input = ?,<br>Tensor<[1024, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1024 | Unknown  | Done       | 0.999984 |     -1 |
|  4 | Tensor<[1, 128, 150, 150]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128  | Unknown  | Done       | 0.999983 |     -1 |
|  5 | Tensor<[1, 128, 150, 150]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128  | Unknown  | Done       | 0.999983 |     -1 |
|  6 | Tensor<[1, 128, 150, 150]> input = ?,<br>Tensor<[128, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Unknown  | Done       | 0.99998  |     -1 |
|  7 | Tensor<[1, 128, 75, 75]> input = ?,<br>Tensor<[128, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 128    | Unknown  | Done       | 0.999983 |     -1 |
|  8 | Tensor<[1, 128, 75, 75]> input = ?,<br>Tensor<[128, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.99998  |     -1 |
|  9 | Tensor<[1, 128, 75, 75]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.99998  |     -1 |
| 10 | Tensor<[1, 1536, 10, 10]> input = ?,<br>Tensor<[1536, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1536 | Unknown  | Done       | 0.999984 |     -1 |
| 11 | Tensor<[1, 1536, 10, 10]> input = ?,<br>Tensor<[1536, 1536, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.99996  |     -1 |
| 12 | Tensor<[1, 1536, 10, 10]> input = ?,<br>Tensor<[2048, 1536, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  | Done       | 0.99996  |     -1 |
| 13 | Tensor<[1, 256, 38, 38]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256    | Unknown  | Done       | 0.999984 |     -1 |
| 14 | Tensor<[1, 256, 38, 38]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999975 |     -1 |
| 15 | Tensor<[1, 256, 38, 38]> input = ?,<br>Tensor<[728, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999979 |     -1 |
| 16 | Tensor<[1, 256, 75, 75]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256    | Unknown  | Done       | 0.999984 |     -1 |
| 17 | Tensor<[1, 256, 75, 75]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256    | Unknown  | Done       | 0.999984 |     -1 |
| 18 | Tensor<[1, 256, 75, 75]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999975 |     -1 |
| 19 | Tensor<[1, 256, 75, 75]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999965 |     -1 |
| 20 | Tensor<[1, 3, 299, 299]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  | Done       | 0.999981 |     -1 |
| 21 | Tensor<[1, 32, 150, 150]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Unknown  | Done       | 0.999961 |     -1 |
| 22 | Tensor<[1, 64, 150, 150]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999986 |     -1 |
| 23 | Tensor<[1, 64, 150, 150]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999988 |     -1 |
| 24 | Tensor<[1, 64, 150, 150]> input = ?,<br>Tensor<[64, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 64     | Unknown  | Done       | 0.999983 |     -1 |
| 25 | Tensor<[1, 728, 19, 19]> input = ?,<br>Tensor<[1024, 728, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999969 |     -1 |
| 26 | Tensor<[1, 728, 19, 19]> input = ?,<br>Tensor<[1024, 728, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  | Done       | 0.999894 |     -1 |
| 27 | Tensor<[1, 728, 19, 19]> input = ?,<br>Tensor<[728, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 728    | Unknown  | Done       | 0.999984 |     -1 |
| 28 | Tensor<[1, 728, 19, 19]> input = ?,<br>Tensor<[728, 728, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999968 |     -1 |
| 29 | Tensor<[1, 728, 38, 38]> input = ?,<br>Tensor<[728, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 728    | Unknown  | Done       | 0.999983 |     -1 |
| 30 | Tensor<[1, 728, 38, 38]> input = ?,<br>Tensor<[728, 1, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 728    | Unknown  | Done       | 0.999984 |     -1 |
| 31 | Tensor<[1, 728, 38, 38]> input = ?,<br>Tensor<[728, 728, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999968 |     -1 |
| 32 | Tensor<[1, 728, 38, 38]> input = ?,<br>Tensor<[728, 728, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  | Done       | 0.999893 |     -1 |
### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2048, 10, 10]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  | Done       | 0.999996 |     -1 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 10, 10]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1024, 19, 19]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 128, 150, 150]> self = ? | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 128, 75, 75]> self = ?   | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 1536, 10, 10]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[1, 2048, 10, 10]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  6 | Tensor<[1, 256, 38, 38]> self = ?   | Unknown  | Done       |     1 |     -1 |
|  7 | Tensor<[1, 256, 75, 75]> self = ?   | Unknown  | Done       |     1 |     -1 |
|  8 | Tensor<[1, 32, 150, 150]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  9 | Tensor<[1, 64, 150, 150]> self = ?  | Unknown  | Done       |     1 |     -1 |
| 10 | Tensor<[1, 728, 19, 19]> self = ?   | Unknown  | Done       |     1 |     -1 |
| 11 | Tensor<[1, 728, 38, 38]> self = ?   | Unknown  | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 2048]> self = ? | Unknown  | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048] | Unknown  | Done       |     1 |     -1 |

