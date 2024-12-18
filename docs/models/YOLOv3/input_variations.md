# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 13 |          13 |         0 |          0 | ✅          |       1 |
|  1 | aten._to_copy.default                             |                  6 |           4 |         2 |          0 | ✅          |       1 |
|  2 | aten._unsafe_index.Tensor                         |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  3 | aten.add.Tensor                                   |                  7 |           5 |         2 |          0 | ✅          |       1 |
|  4 | aten.arange.default                               |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  5 | aten.cat.default                                  |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  6 | aten.convolution.default                          |                 23 |          23 |         0 |          0 | ✅          |       1 |
|  7 | aten.leaky_relu.default                           |                 13 |          13 |         0 |          0 | ✅          |       1 |
|  8 | aten.mul.Tensor                                   |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  9 | aten.unsqueeze.default                            |                  2 |           0 |         2 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      8 |
|  1 | Tensor<[1, 128, 128, 128]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05    | Done     | Done       | 0.999987 |      8 |
|  2 | Tensor<[1, 128, 32, 32]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05      | Done     | Done       | 0.999992 |      8 |
|  3 | Tensor<[1, 128, 64, 64]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05      | Done     | Done       | 0.999986 |      8 |
|  4 | Tensor<[1, 256, 16, 16]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      8 |
|  5 | Tensor<[1, 256, 32, 32]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05      | Done     | Done       | 0.999986 |      8 |
|  6 | Tensor<[1, 256, 64, 64]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05      | Done     | Done       | 0.999991 |      8 |
|  7 | Tensor<[1, 32, 256, 256]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05         | Done     | Done       | 0.999989 |      8 |
|  8 | Tensor<[1, 32, 512, 512]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05         | Done     | Done       | 0.999985 |      8 |
|  9 | Tensor<[1, 512, 16, 16]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05      | Done     | Done       | 0.999989 |      8 |
| 10 | Tensor<[1, 512, 32, 32]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05      | Done     | Done       | 0.99999  |      8 |
| 11 | Tensor<[1, 64, 128, 128]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05         | Done     | Done       | 0.999991 |      8 |
| 12 | Tensor<[1, 64, 256, 256]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.01,<br>float eps = 1e-05         | Done     | Done       | 0.999988 |      8 |
### aten._to_copy.default
|    | ATen Input Variations                                                      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 32, 32]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 128, 64, 64]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 256, 16, 16]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 256, 32, 32]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   |     1 |     -1 |
|  4 | Tensor<[32]> self = ?,<br>Optional[int] dtype = torch.int64                | Removed  | Fallback   |     1 |     -1 |
|  5 | Tensor<[64]> self = ?,<br>Optional[int] dtype = torch.int64                | Removed  | Fallback   |     1 |     -1 |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 128, 32, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[64, 1]>, <[64]>] | Removed  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[32, 1]>, <[32]>] | Removed  | Unknown    | N/A   | N/A    |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  5 | Tensor<[32]> self = ?,<br>Tensor other = 0.0                                 | Removed  | Done       | 1        |      0 |
|  6 | Tensor<[64]> self = ?,<br>Tensor other = 0.0                                 | Removed  | Done       | 1        |      0 |
### aten.arange.default
|    | ATen Input Variations                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | number end = 32,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |     -1 |
|  1 | number end = 64,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |     -1 |
### aten.cat.default
|    | ATen Input Variations                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 128, 64, 64]>, <[1, 256, 64, 64]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 256, 32, 32]>, <[1, 512, 32, 32]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[255, 1024, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999839 |      8 |
|  1 | Tensor<[1, 1024, 16, 16]> input = ?,<br>Tensor<[512, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999839 |      5 |
|  2 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999814 |      5 |
|  3 | Tensor<[1, 128, 128, 128]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.999981 |      5 |
|  4 | Tensor<[1, 128, 64, 64]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999816 |      5 |
|  5 | Tensor<[1, 256, 32, 32]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999966 |      5 |
|  6 | Tensor<[1, 256, 32, 32]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999551 |      5 |
|  7 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999965 |      5 |
|  8 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[255, 256, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999964 |      8 |
|  9 | Tensor<[1, 256, 64, 64]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999545 |      5 |
| 10 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1             | Done     | Done       | 0.999981 |      5 |
| 11 | Tensor<[1, 32, 256, 256]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999961 |      5 |
| 12 | Tensor<[1, 32, 512, 512]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999961 |      5 |
| 13 | Tensor<[1, 384, 64, 64]> input = ?,<br>Tensor<[128, 384, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999948 |      5 |
| 14 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.99889  |      5 |
| 15 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999929 |      5 |
| 16 | Tensor<[1, 512, 32, 32]> input = ?,<br>Tensor<[1024, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | 0.998851 |      5 |
| 17 | Tensor<[1, 512, 32, 32]> input = ?,<br>Tensor<[255, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[255]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999928 |      8 |
| 18 | Tensor<[1, 512, 32, 32]> input = ?,<br>Tensor<[256, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.99993  |      5 |
| 19 | Tensor<[1, 64, 128, 128]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.99992  |      5 |
| 20 | Tensor<[1, 64, 256, 256]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.99992  |      5 |
| 21 | Tensor<[1, 64, 256, 256]> input = ?,<br>Tensor<[32, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999988 |      5 |
| 22 | Tensor<[1, 768, 32, 32]> input = ?,<br>Tensor<[256, 768, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | 0.999887 |      5 |
### aten.leaky_relu.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 16, 16]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 128, 128, 128]> self = ?,<br>number negative_slope = 0.1 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 32, 32]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 128, 64, 64]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 16, 16]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 256, 32, 32]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 256, 64, 64]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 32, 256, 256]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 32, 512, 512]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 512, 16, 16]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 512, 32, 32]> self = ?,<br>number negative_slope = 0.1   | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 64, 128, 128]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 64, 256, 256]> self = ?,<br>number negative_slope = 0.1  | Done     | Done       |     1 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[32]> self = ?,<br>Tensor other = 0.5 | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[64]> self = ?,<br>Tensor other = 0.5 | Removed  | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                  | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[32]> self = ?,<br>int dim = -1 | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[64]> self = ?,<br>int dim = -1 | Removed  | Done       |     1 |      0 |

