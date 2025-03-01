# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 33 |          33 |         0 |          0 | ✅          |       1 |
|  1 | aten.add.Tensor                                   |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.cat.default                                  |                 10 |          10 |         0 |          0 | ✅          |       1 |
|  4 | aten.clone.default                                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.convolution.default                          |                 49 |          49 |         0 |          0 | ✅          |       1 |
|  6 | aten.max_pool2d_with_indices.default              |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.mul.Tensor                                   |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  9 | aten.relu.default                                 |                 33 |          33 |         0 |          0 | ✅          |       1 |
| 10 | aten.select.int                                   |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 11 | aten.slice.Tensor                                 |                  1 |           0 |         1 |          0 | ✅          |       1 |
| 12 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 13 | aten.unsqueeze.default                            |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 14 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 14, 14]> input = ?,<br>Optional[Tensor]<[112]> weight = ?,<br>Optional[Tensor]<[112]> bias = ?,<br>Tensor<[112]> running_mean = ?,<br>Tensor<[112]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999988 |      5 |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.99999  |      5 |
|  2 | Tensor<[1, 128, 28, 28]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.99999  |      5 |
|  3 | Tensor<[1, 128, 7, 7]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | 0.999987 |      5 |
|  4 | Tensor<[1, 144, 14, 14]> input = ?,<br>Optional[Tensor]<[144]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>Tensor<[144]> running_mean = ?,<br>Tensor<[144]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999988 |      5 |
|  5 | Tensor<[1, 16, 14, 14]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.999989 |      5 |
|  6 | Tensor<[1, 16, 28, 28]> input = ?,<br>Optional[Tensor]<[16]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>Tensor<[16]> running_mean = ?,<br>Tensor<[16]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.999991 |      5 |
|  7 | Tensor<[1, 160, 14, 14]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999988 |      5 |
|  8 | Tensor<[1, 160, 7, 7]> input = ?,<br>Optional[Tensor]<[160]> weight = ?,<br>Optional[Tensor]<[160]> bias = ?,<br>Tensor<[160]> running_mean = ?,<br>Tensor<[160]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | 0.99999  |      5 |
|  9 | Tensor<[1, 192, 14, 14]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999992 |      5 |
| 10 | Tensor<[1, 192, 28, 28]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999989 |      5 |
| 11 | Tensor<[1, 192, 56, 56]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999986 |      5 |
| 12 | Tensor<[1, 192, 7, 7]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | 0.999988 |      5 |
| 13 | Tensor<[1, 208, 14, 14]> input = ?,<br>Optional[Tensor]<[208]> weight = ?,<br>Optional[Tensor]<[208]> bias = ?,<br>Tensor<[208]> running_mean = ?,<br>Tensor<[208]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.99999  |      5 |
| 14 | Tensor<[1, 224, 14, 14]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999988 |      5 |
| 15 | Tensor<[1, 24, 14, 14]> input = ?,<br>Optional[Tensor]<[24]> weight = ?,<br>Optional[Tensor]<[24]> bias = ?,<br>Tensor<[24]> running_mean = ?,<br>Tensor<[24]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.999992 |      5 |
| 16 | Tensor<[1, 256, 14, 14]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999991 |      5 |
| 17 | Tensor<[1, 256, 7, 7]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | 0.999989 |      5 |
| 18 | Tensor<[1, 288, 14, 14]> input = ?,<br>Optional[Tensor]<[288]> weight = ?,<br>Optional[Tensor]<[288]> bias = ?,<br>Tensor<[288]> running_mean = ?,<br>Tensor<[288]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999985 |      5 |
| 19 | Tensor<[1, 32, 14, 14]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.99999  |      5 |
| 20 | Tensor<[1, 32, 28, 28]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.999991 |      5 |
| 21 | Tensor<[1, 32, 7, 7]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001        | Done     | Done       | 0.999992 |      5 |
| 22 | Tensor<[1, 320, 14, 14]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | 0.999989 |      5 |
| 23 | Tensor<[1, 320, 7, 7]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | 0.999989 |      5 |
| 24 | Tensor<[1, 384, 7, 7]> input = ?,<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>Tensor<[384]> running_mean = ?,<br>Tensor<[384]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | 0.999988 |      5 |
| 25 | Tensor<[1, 48, 14, 14]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.999991 |      5 |
| 26 | Tensor<[1, 48, 7, 7]> input = ?,<br>Optional[Tensor]<[48]> weight = ?,<br>Optional[Tensor]<[48]> bias = ?,<br>Tensor<[48]> running_mean = ?,<br>Tensor<[48]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001        | Done     | Done       | 0.999989 |      5 |
| 27 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001    | Done     | Done       | 0.999989 |      5 |
| 28 | Tensor<[1, 64, 14, 14]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.999991 |      5 |
| 29 | Tensor<[1, 64, 28, 28]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.999989 |      5 |
| 30 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.99999  |      5 |
| 31 | Tensor<[1, 96, 14, 14]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.99999  |      5 |
| 32 | Tensor<[1, 96, 28, 28]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | 0.999988 |      5 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027 | Done     | Done       | 1        |      0 |
|  1 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997  | Done     | Done       | 0.999999 |      0 |
|  2 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994  | Done     | Done       | 1        |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ? | Done     | Done       | 0.999966 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 1, 224, 224]>, <[1, 1, 224, 224]>, <[1, 1, 224, 224]>],<br>int dim = 1                     | Done     | Done       |     1 |      0 |
|  1 | List[Tensor] tensors = [<[1, 112, 14, 14]>, <[1, 288, 14, 14]>, <[1, 64, 14, 14]>, <[1, 64, 14, 14]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  2 | List[Tensor] tensors = [<[1, 128, 14, 14]>, <[1, 256, 14, 14]>, <[1, 64, 14, 14]>, <[1, 64, 14, 14]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  3 | List[Tensor] tensors = [<[1, 128, 28, 28]>, <[1, 192, 28, 28]>, <[1, 96, 28, 28]>, <[1, 64, 28, 28]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  4 | List[Tensor] tensors = [<[1, 160, 14, 14]>, <[1, 224, 14, 14]>, <[1, 64, 14, 14]>, <[1, 64, 14, 14]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  5 | List[Tensor] tensors = [<[1, 192, 14, 14]>, <[1, 208, 14, 14]>, <[1, 48, 14, 14]>, <[1, 64, 14, 14]>],<br>int dim = 1   | Done     | Done       |     1 |      0 |
|  6 | List[Tensor] tensors = [<[1, 256, 14, 14]>, <[1, 320, 14, 14]>, <[1, 128, 14, 14]>, <[1, 128, 14, 14]>],<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  7 | List[Tensor] tensors = [<[1, 256, 7, 7]>, <[1, 320, 7, 7]>, <[1, 128, 7, 7]>, <[1, 128, 7, 7]>],<br>int dim = 1         | Done     | Done       |     1 |      0 |
|  8 | List[Tensor] tensors = [<[1, 384, 7, 7]>, <[1, 384, 7, 7]>, <[1, 128, 7, 7]>, <[1, 128, 7, 7]>],<br>int dim = 1         | Done     | Done       |     1 |      0 |
|  9 | List[Tensor] tensors = [<[1, 64, 28, 28]>, <[1, 128, 28, 28]>, <[1, 32, 28, 28]>, <[1, 32, 28, 28]>],<br>int dim = 1    | Done     | Done       |     1 |      0 |
### aten.clone.default
|    | ATen Input Variations      | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024]> self = ? | Done     | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 112, 14, 14]> input = ?,<br>Tensor<[224, 112, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999854 |      4 |
|  1 | Tensor<[1, 128, 14, 14]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999828 |      4 |
|  2 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[192, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999817 |      4 |
|  3 | Tensor<[1, 144, 14, 14]> input = ?,<br>Tensor<[288, 144, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.9998   |      4 |
|  4 | Tensor<[1, 16, 14, 14]> input = ?,<br>Tensor<[48, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999981 |      4 |
|  5 | Tensor<[1, 16, 28, 28]> input = ?,<br>Tensor<[32, 16, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.99998  |      4 |
|  6 | Tensor<[1, 160, 14, 14]> input = ?,<br>Tensor<[320, 160, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999769 |      4 |
|  7 | Tensor<[1, 160, 7, 7]> input = ?,<br>Tensor<[320, 160, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999784 |      4 |
|  8 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[16, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999978 |      4 |
|  9 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[32, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999977 |      4 |
| 10 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[64, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999977 |      4 |
| 11 | Tensor<[1, 192, 28, 28]> input = ?,<br>Tensor<[96, 192, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999977 |      4 |
| 12 | Tensor<[1, 192, 7, 7]> input = ?,<br>Tensor<[384, 192, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999725 |      4 |
| 13 | Tensor<[1, 24, 14, 14]> input = ?,<br>Tensor<[64, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999965 |      4 |
| 14 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[128, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999975 |      4 |
| 15 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[32, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999976 |      4 |
| 16 | Tensor<[1, 256, 28, 28]> input = ?,<br>Tensor<[64, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999975 |      4 |
| 17 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999901 |      4 |
| 18 | Tensor<[1, 32, 14, 14]> input = ?,<br>Tensor<[128, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999963 |      4 |
| 19 | Tensor<[1, 32, 14, 14]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999964 |      4 |
| 20 | Tensor<[1, 32, 28, 28]> input = ?,<br>Tensor<[96, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999962 |      4 |
| 21 | Tensor<[1, 32, 7, 7]> input = ?,<br>Tensor<[128, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999966 |      4 |
| 22 | Tensor<[1, 48, 7, 7]> input = ?,<br>Tensor<[128, 48, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999949 |      4 |
| 23 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[16, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999974 |      4 |
| 24 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[192, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999974 |      4 |
| 25 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[64, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999974 |      4 |
| 26 | Tensor<[1, 480, 14, 14]> input = ?,<br>Tensor<[96, 480, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999974 |      4 |
| 27 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[112, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999971 |      4 |
| 28 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[128, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999972 |      4 |
| 29 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[144, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999971 |      4 |
| 30 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[160, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999971 |      4 |
| 31 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[24, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999971 |      4 |
| 32 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[32, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999971 |      4 |
| 33 | Tensor<[1, 512, 14, 14]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999971 |      4 |
| 34 | Tensor<[1, 528, 14, 14]> input = ?,<br>Tensor<[128, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999974 |      4 |
| 35 | Tensor<[1, 528, 14, 14]> input = ?,<br>Tensor<[160, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999975 |      4 |
| 36 | Tensor<[1, 528, 14, 14]> input = ?,<br>Tensor<[256, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999975 |      4 |
| 37 | Tensor<[1, 528, 14, 14]> input = ?,<br>Tensor<[32, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999974 |      4 |
| 38 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[192, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99992  |      4 |
| 39 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999986 |      4 |
| 40 | Tensor<[1, 832, 7, 7]> input = ?,<br>Tensor<[128, 832, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999966 |      4 |
| 41 | Tensor<[1, 832, 7, 7]> input = ?,<br>Tensor<[160, 832, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999965 |      4 |
| 42 | Tensor<[1, 832, 7, 7]> input = ?,<br>Tensor<[192, 832, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999967 |      4 |
| 43 | Tensor<[1, 832, 7, 7]> input = ?,<br>Tensor<[256, 832, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999966 |      4 |
| 44 | Tensor<[1, 832, 7, 7]> input = ?,<br>Tensor<[32, 832, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999967 |      4 |
| 45 | Tensor<[1, 832, 7, 7]> input = ?,<br>Tensor<[384, 832, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999966 |      4 |
| 46 | Tensor<[1, 832, 7, 7]> input = ?,<br>Tensor<[48, 832, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999967 |      4 |
| 47 | Tensor<[1, 96, 14, 14]> input = ?,<br>Tensor<[208, 96, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999878 |      4 |
| 48 | Tensor<[1, 96, 28, 28]> input = ?,<br>Tensor<[128, 96, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999873 |      4 |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                                                                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 192, 28, 28]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 192, 56, 56]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 256, 28, 28]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 480, 14, 14]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 480, 28, 28]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | None     | Fallback   |     1 |     -1 |
|  5 | Tensor<[1, 512, 14, 14]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | None     | Fallback   |     1 |     -1 |
|  6 | Tensor<[1, 528, 14, 14]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | None     | Fallback   |     1 |     -1 |
|  7 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True | None     | Fallback   |     1 |     -1 |
|  8 | Tensor<[1, 832, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | None     | Fallback   |     1 |     -1 |
|  9 | Tensor<[1, 832, 7, 7]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True    | None     | Fallback   |     1 |     -1 |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999996 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448 | Done     | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45  | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458 | Done     | Done       | 0.999997 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 112, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 128, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 128, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 128, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 144, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 16, 14, 14]> self = ?   | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 16, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 160, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 160, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 192, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 192, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 192, 56, 56]> self = ?  | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 192, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
| 13 | Tensor<[1, 208, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 14 | Tensor<[1, 224, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 15 | Tensor<[1, 24, 14, 14]> self = ?   | Done     | Done       |     1 |      0 |
| 16 | Tensor<[1, 256, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 17 | Tensor<[1, 256, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
| 18 | Tensor<[1, 288, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 19 | Tensor<[1, 32, 14, 14]> self = ?   | Done     | Done       |     1 |      0 |
| 20 | Tensor<[1, 32, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
| 21 | Tensor<[1, 32, 7, 7]> self = ?     | Done     | Done       |     1 |      0 |
| 22 | Tensor<[1, 320, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
| 23 | Tensor<[1, 320, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
| 24 | Tensor<[1, 384, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
| 25 | Tensor<[1, 48, 14, 14]> self = ?   | Done     | Done       |     1 |      0 |
| 26 | Tensor<[1, 48, 7, 7]> self = ?     | Done     | Done       |     1 |      0 |
| 27 | Tensor<[1, 64, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
| 28 | Tensor<[1, 64, 14, 14]> self = ?   | Done     | Done       |     1 |      0 |
| 29 | Tensor<[1, 64, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
| 30 | Tensor<[1, 64, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
| 31 | Tensor<[1, 96, 14, 14]> self = ?   | Done     | Done       |     1 |      0 |
| 32 | Tensor<[1, 96, 28, 28]> self = ?   | Done     | Done       |     1 |      0 |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 1 | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 2 | Done     | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 1024]> self = ? | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 224, 224]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024] | Done     | Done       |     1 |     -1 |

