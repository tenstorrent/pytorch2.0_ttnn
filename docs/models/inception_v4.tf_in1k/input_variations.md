# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                 22 |          22 |         0 |          0 | ✅          |    1    |
|  1 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  2 | aten.avg_pool2d.default                           |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten.cat.default                                  |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  4 | aten.clone.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  5 | aten.convolution.default                          |                 38 |          37 |         0 |          0 | 🚧          |    0.97 |
|  6 | aten.max_pool2d_with_indices.default              |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
|  7 | aten.mean.dim                                     |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  8 | aten.relu.default                                 |                 22 |          22 |         0 |          0 | ✅          |    1    |
|  9 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 128, 17, 17]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | True  |
|  1 | Tensor<[1, 192, 17, 17]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | True  |
|  2 | Tensor<[1, 192, 35, 35]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | True  |
|  3 | Tensor<[1, 192, 8, 8]> input = ?,<br>Optional[Tensor]<[192]> weight = ?,<br>Optional[Tensor]<[192]> bias = ?,<br>Tensor<[192]> running_mean = ?,<br>Tensor<[192]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | True  |
|  4 | Tensor<[1, 224, 17, 17]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | True  |
|  5 | Tensor<[1, 224, 35, 35]> input = ?,<br>Optional[Tensor]<[224]> weight = ?,<br>Optional[Tensor]<[224]> bias = ?,<br>Tensor<[224]> running_mean = ?,<br>Tensor<[224]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | True  |
|  6 | Tensor<[1, 256, 17, 17]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | True  |
|  7 | Tensor<[1, 256, 8, 8]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | True  |
|  8 | Tensor<[1, 32, 147, 147]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001    | Done     | Done       | True  |
|  9 | Tensor<[1, 32, 149, 149]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001    | Done     | Done       | True  |
| 10 | Tensor<[1, 320, 17, 17]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | True  |
| 11 | Tensor<[1, 320, 8, 8]> input = ?,<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>Tensor<[320]> running_mean = ?,<br>Tensor<[320]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | True  |
| 12 | Tensor<[1, 384, 17, 17]> input = ?,<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>Tensor<[384]> running_mean = ?,<br>Tensor<[384]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Done     | Done       | True  |
| 13 | Tensor<[1, 384, 8, 8]> input = ?,<br>Optional[Tensor]<[384]> weight = ?,<br>Optional[Tensor]<[384]> bias = ?,<br>Tensor<[384]> running_mean = ?,<br>Tensor<[384]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | True  |
| 14 | Tensor<[1, 448, 8, 8]> input = ?,<br>Optional[Tensor]<[448]> weight = ?,<br>Optional[Tensor]<[448]> bias = ?,<br>Tensor<[448]> running_mean = ?,<br>Tensor<[448]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | True  |
| 15 | Tensor<[1, 512, 8, 8]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001   | Done     | Done       | True  |
| 16 | Tensor<[1, 64, 147, 147]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001    | Done     | Done       | True  |
| 17 | Tensor<[1, 64, 35, 35]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | True  |
| 18 | Tensor<[1, 64, 73, 73]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | True  |
| 19 | Tensor<[1, 96, 35, 35]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | True  |
| 20 | Tensor<[1, 96, 71, 71]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | True  |
| 21 | Tensor<[1, 96, 73, 73]> input = ?,<br>Optional[Tensor]<[96]> weight = ?,<br>Optional[Tensor]<[96]> bias = ?,<br>Tensor<[96]> running_mean = ?,<br>Tensor<[96]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001      | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1536]> mat1 = ?,<br>Tensor<[1536, 1000]> mat2 = ? | Done     | Done       | True  |
### aten.avg_pool2d.default
|    | ATen Input Variations                                                                                                                                                                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 17, 17]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>bool ceil_mode = False,<br>bool count_include_pad = False | None     | Fallback   | True  |
|  1 | Tensor<[1, 1536, 8, 8]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>bool ceil_mode = False,<br>bool count_include_pad = False   | None     | Fallback   | True  |
|  2 | Tensor<[1, 384, 35, 35]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>bool ceil_mode = False,<br>bool count_include_pad = False  | None     | Fallback   | True  |
### aten.cat.default
|    | ATen Input Variations                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 192, 35, 35]>, <[1, 192, 35, 35]>],<br>int dim = 1                                         | Done     | Done       | True  |
|  1 | List[Tensor] tensors = [<[1, 192, 8, 8]>, <[1, 320, 8, 8]>, <[1, 1024, 8, 8]>],<br>int dim = 1                          | Done     | Done       | True  |
|  2 | List[Tensor] tensors = [<[1, 256, 8, 8]>, <[1, 256, 8, 8]>],<br>int dim = 1                                             | Done     | Done       | True  |
|  3 | List[Tensor] tensors = [<[1, 256, 8, 8]>, <[1, 512, 8, 8]>, <[1, 512, 8, 8]>, <[1, 256, 8, 8]>],<br>int dim = 1         | Done     | Done       | True  |
|  4 | List[Tensor] tensors = [<[1, 384, 17, 17]>, <[1, 256, 17, 17]>, <[1, 256, 17, 17]>, <[1, 128, 17, 17]>],<br>int dim = 1 | Done     | Done       | True  |
|  5 | List[Tensor] tensors = [<[1, 384, 17, 17]>, <[1, 256, 17, 17]>, <[1, 384, 17, 17]>],<br>int dim = 1                     | Done     | Done       | True  |
|  6 | List[Tensor] tensors = [<[1, 64, 73, 73]>, <[1, 96, 73, 73]>],<br>int dim = 1                                           | Done     | Done       | True  |
|  7 | List[Tensor] tensors = [<[1, 96, 35, 35]>, <[1, 96, 35, 35]>, <[1, 96, 35, 35]>, <[1, 96, 35, 35]>],<br>int dim = 1     | Done     | Done       | True  |
|  8 | List[Tensor] tensors = [<[1, 96, 71, 71]>, <[1, 96, 71, 71]>],<br>int dim = 1                                           | Done     | Done       | True  |
### aten.clone.default
|    | ATen Input Variations      | Status   | Isolated   | PCC   |
|---:|:---------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1536]> self = ? | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 17, 17]> input = ?,<br>Tensor<[128, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  1 | Tensor<[1, 1024, 17, 17]> input = ?,<br>Tensor<[192, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  2 | Tensor<[1, 1024, 17, 17]> input = ?,<br>Tensor<[256, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  3 | Tensor<[1, 1024, 17, 17]> input = ?,<br>Tensor<[384, 1024, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  4 | Tensor<[1, 1536, 8, 8]> input = ?,<br>Tensor<[256, 1536, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  5 | Tensor<[1, 1536, 8, 8]> input = ?,<br>Tensor<[384, 1536, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  6 | Tensor<[1, 160, 73, 73]> input = ?,<br>Tensor<[64, 160, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | True  |
|  7 | Tensor<[1, 192, 17, 17]> input = ?,<br>Tensor<[192, 192, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  8 | Tensor<[1, 192, 17, 17]> input = ?,<br>Tensor<[192, 192, 7, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [3, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  9 | Tensor<[1, 192, 17, 17]> input = ?,<br>Tensor<[224, 192, 1, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 10 | Tensor<[1, 192, 35, 35]> input = ?,<br>Tensor<[224, 192, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 11 | Tensor<[1, 192, 71, 71]> input = ?,<br>Tensor<[192, 192, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 12 | Tensor<[1, 224, 17, 17]> input = ?,<br>Tensor<[224, 224, 7, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [3, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 13 | Tensor<[1, 224, 17, 17]> input = ?,<br>Tensor<[256, 224, 1, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 14 | Tensor<[1, 224, 17, 17]> input = ?,<br>Tensor<[256, 224, 7, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [3, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 15 | Tensor<[1, 224, 35, 35]> input = ?,<br>Tensor<[256, 224, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 16 | Tensor<[1, 256, 17, 17]> input = ?,<br>Tensor<[256, 256, 1, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 17 | Tensor<[1, 256, 17, 17]> input = ?,<br>Tensor<[320, 256, 7, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [3, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 18 | Tensor<[1, 3, 299, 299]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | None     | Fallback   | True  |
| 19 | Tensor<[1, 32, 147, 147]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | True  |
| 20 | Tensor<[1, 32, 149, 149]> input = ?,<br>Tensor<[32, 32, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | True  |
| 21 | Tensor<[1, 320, 17, 17]> input = ?,<br>Tensor<[320, 320, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 22 | Tensor<[1, 384, 35, 35]> input = ?,<br>Tensor<[192, 384, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 23 | Tensor<[1, 384, 35, 35]> input = ?,<br>Tensor<[384, 384, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 24 | Tensor<[1, 384, 35, 35]> input = ?,<br>Tensor<[64, 384, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | True  |
| 25 | Tensor<[1, 384, 35, 35]> input = ?,<br>Tensor<[96, 384, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | True  |
| 26 | Tensor<[1, 384, 8, 8]> input = ?,<br>Tensor<[256, 384, 1, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 27 | Tensor<[1, 384, 8, 8]> input = ?,<br>Tensor<[256, 384, 3, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 28 | Tensor<[1, 384, 8, 8]> input = ?,<br>Tensor<[448, 384, 3, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 29 | Tensor<[1, 448, 8, 8]> input = ?,<br>Tensor<[512, 448, 1, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 30 | Tensor<[1, 512, 8, 8]> input = ?,<br>Tensor<[256, 512, 1, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 31 | Tensor<[1, 512, 8, 8]> input = ?,<br>Tensor<[256, 512, 3, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 32 | Tensor<[1, 64, 147, 147]> input = ?,<br>Tensor<[96, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | True  |
| 33 | Tensor<[1, 64, 35, 35]> input = ?,<br>Tensor<[96, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | True  |
| 34 | Tensor<[1, 64, 73, 73]> input = ?,<br>Tensor<[64, 64, 1, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | True  |
| 35 | Tensor<[1, 64, 73, 73]> input = ?,<br>Tensor<[64, 64, 7, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [3, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | True  |
| 36 | Tensor<[1, 64, 73, 73]> input = ?,<br>Tensor<[96, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | True  |
| 37 | Tensor<[1, 96, 35, 35]> input = ?,<br>Tensor<[96, 96, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1      | Done     | Done       | True  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                               | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1024, 17, 17]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2] | Done     | Done       | True  |
|  1 | Tensor<[1, 192, 71, 71]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2]  | None     | Fallback   | True  |
|  2 | Tensor<[1, 384, 35, 35]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2]  | None     | Fallback   | True  |
|  3 | Tensor<[1, 64, 147, 147]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2] | Done     | Done       | True  |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | False |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 128, 17, 17]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[1, 192, 17, 17]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1, 192, 35, 35]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 192, 8, 8]> self = ?    | Done     | Done       | True  |
|  4 | Tensor<[1, 224, 17, 17]> self = ?  | Done     | Done       | True  |
|  5 | Tensor<[1, 224, 35, 35]> self = ?  | Done     | Done       | True  |
|  6 | Tensor<[1, 256, 17, 17]> self = ?  | Done     | Done       | True  |
|  7 | Tensor<[1, 256, 8, 8]> self = ?    | Done     | Done       | True  |
|  8 | Tensor<[1, 32, 147, 147]> self = ? | Done     | Done       | True  |
|  9 | Tensor<[1, 32, 149, 149]> self = ? | Done     | Done       | True  |
| 10 | Tensor<[1, 320, 17, 17]> self = ?  | Done     | Done       | True  |
| 11 | Tensor<[1, 320, 8, 8]> self = ?    | Done     | Done       | True  |
| 12 | Tensor<[1, 384, 17, 17]> self = ?  | Done     | Done       | True  |
| 13 | Tensor<[1, 384, 8, 8]> self = ?    | Done     | Done       | True  |
| 14 | Tensor<[1, 448, 8, 8]> self = ?    | Done     | Done       | True  |
| 15 | Tensor<[1, 512, 8, 8]> self = ?    | Done     | Done       | True  |
| 16 | Tensor<[1, 64, 147, 147]> self = ? | Done     | Done       | True  |
| 17 | Tensor<[1, 64, 35, 35]> self = ?   | Done     | Done       | True  |
| 18 | Tensor<[1, 64, 73, 73]> self = ?   | Done     | Done       | True  |
| 19 | Tensor<[1, 96, 35, 35]> self = ?   | Done     | Done       | True  |
| 20 | Tensor<[1, 96, 71, 71]> self = ?   | Done     | Done       | True  |
| 21 | Tensor<[1, 96, 73, 73]> self = ?   | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 1536]> self = ? | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1536, 1, 1]> self = ?,<br>List[int] size = [1, 1536] | Done     | Done       | True  |

