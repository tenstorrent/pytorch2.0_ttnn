# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                          |                 19 |          19 |         0 |          0 | ✅          |       1 |
|  4 | aten.max_pool2d_with_indices.default              |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.relu.default                                 |                  8 |           8 |         0 |          0 | ✅          |       1 |
|  7 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |      0 |
|  1 | Tensor<[1, 1024, 28, 28]> input = ?,<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>Tensor<[1024]> running_mean = ?,<br>Tensor<[1024]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |      0 |
|  2 | Tensor<[1, 2048, 14, 14]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999987 |      0 |
|  3 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Optional[Tensor]<[2048]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>Tensor<[2048]> running_mean = ?,<br>Tensor<[2048]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | 0.999988 |      0 |
|  4 | Tensor<[1, 256, 56, 56]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999993 |      0 |
|  5 | Tensor<[1, 512, 28, 28]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      0 |
|  6 | Tensor<[1, 512, 56, 56]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999992 |      0 |
|  7 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999991 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?   | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 2048]> mat1 = ?,<br>Tensor<[2048, 1000]> mat2 = ? | Done     | Done       | 0.999955 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Tensor<[1024, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999965 |      0 |
|  1 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Tensor<[1024, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32  | Done     | Done       | 0.999963 |      0 |
|  2 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999966 |      0 |
|  3 | Tensor<[1, 1024, 14, 14]> input = ?,<br>Tensor<[2048, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.99984  |      0 |
|  4 | Tensor<[1, 1024, 28, 28]> input = ?,<br>Tensor<[1024, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32  | Done     | Done       | 0.999962 |      0 |
|  5 | Tensor<[1, 2048, 14, 14]> input = ?,<br>Tensor<[2048, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32  | Done     | Done       | 0.999924 |      0 |
|  6 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Tensor<[2048, 2048, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999954 |      0 |
|  7 | Tensor<[1, 2048, 7, 7]> input = ?,<br>Tensor<[2048, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32    | Done     | Done       | 0.999929 |      0 |
|  8 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999975 |      0 |
|  9 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[256, 8, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32     | Done     | Done       | 0.99998  |      0 |
| 10 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999975 |      0 |
| 11 | Tensor<[1, 256, 56, 56]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999965 |      0 |
| 12 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999901 |      0 |
| 13 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999971 |      0 |
| 14 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[1024, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999929 |      0 |
| 15 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[512, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32    | Done     | Done       | 0.99998  |      0 |
| 16 | Tensor<[1, 512, 28, 28]> input = ?,<br>Tensor<[512, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999971 |      0 |
| 17 | Tensor<[1, 512, 56, 56]> input = ?,<br>Tensor<[512, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 32    | Done     | Done       | 0.99998  |      0 |
| 18 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[256, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | 0.999986 |      0 |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | Done     | Done       |     1 |      0 |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 14, 14]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1024, 28, 28]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 2048, 14, 14]> self = ? | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 2048, 7, 7]> self = ?   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 256, 56, 56]> self = ?  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 512, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 512, 56, 56]> self = ?  | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 64, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 2048]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048, 1, 1]> self = ?,<br>List[int] size = [1, 2048] | Done     | Done       |     1 |      0 |

