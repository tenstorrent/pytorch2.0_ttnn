# High Level Operations Status
|    | Operations                                       |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_functional.default |                  5 |           0 |         0 |          0 | ✘           |     0   |
|  1 | aten._to_copy.default                            |                  4 |           0 |         0 |          0 | ✘           |     0   |
|  2 | aten.add.Tensor                                  |                  5 |           4 |         0 |          0 | 🚧          |     0.8 |
|  3 | aten.addmm.default                               |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  4 | aten.convolution.default                         |                 11 |          11 |         0 |          0 | ✅          |     1   |
|  5 | aten.convolution_backward.default                |                 11 |           0 |         0 |          0 | ✘           |     0   |
|  6 | aten.detach.default                              |                  5 |           0 |         0 |          0 | ✘           |     0   |
|  7 | aten.div.Scalar                                  |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  8 | aten.expand.default                              |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  9 | aten.max_pool2d_with_indices.default             |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 10 | aten.max_pool2d_with_indices_backward.default    |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 11 | aten.mean.dim                                    |                  1 |           1 |         0 |          0 | ✅          |     1   |
| 12 | aten.mm.default                                  |                  2 |           2 |         0 |          0 | ✅          |     1   |
| 13 | aten.native_batch_norm_backward.default          |                  5 |           0 |         0 |          0 | ✘           |     0   |
| 14 | aten.relu.default                                |                  5 |           5 |         0 |          0 | ✅          |     1   |
| 15 | aten.sum.dim_IntList                             |                  1 |           0 |         0 |          0 | ✘           |     0   |
| 16 | aten.t.default                                   |                  3 |           3 |         0 |          0 | ✅          |     1   |
| 17 | aten.threshold_backward.default                  |                  5 |           0 |         0 |          0 | ✘           |     0   |
| 18 | aten.view.default                                |                  3 |           3 |         0 |          0 | ✅          |     1   |
***
### aten._native_batch_norm_legit_functional.default
|    | ATen Input Variations                                                                                                                                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 28, 28]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>Tensor<[128]> running_mean = ?,<br>Tensor<[128]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 256, 14, 14]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>Tensor<[256]> running_mean = ?,<br>Tensor<[256]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05 | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[1, 512, 7, 7]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>Tensor<[512]> running_mean = ?,<br>Tensor<[512]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05   | None     | Fallback   |     1 |      0 |
|  3 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05    | None     | Fallback   |     1 |      0 |
|  4 | Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05      | None     | Fallback   |     1 |      0 |
### aten._to_copy.default
|    | ATen Input Variations                                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[128]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[256]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[512]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[64]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided  | None     | Fallback   |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?     | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  4 | Tensor<[]> self = ?,<br>Tensor other = 1                                 | None     | Fallback   | 1        |     -1 |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 512]> mat1 = ?,<br>Tensor<[512, 1000]> mat2 = ? | Done     | Done       | 0.999973 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999819 |      5 |
|  1 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999981 |      5 |
|  2 | Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999817 |      5 |
|  3 | Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999574 |      5 |
|  4 | Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999966 |      5 |
|  5 | Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999565 |      5 |
|  6 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999901 |      5 |
|  7 | Tensor<[1, 512, 7, 7]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.998958 |      5 |
|  8 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999988 |      5 |
|  9 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.99992  |      5 |
| 10 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999921 |      5 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 28, 28]> grad_output = ?,<br>Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[128, 128, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 128, 28, 28]> grad_output = ?,<br>Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[1, 128, 28, 28]> grad_output = ?,<br>Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   |     1 |      0 |
|  3 | Tensor<[1, 256, 14, 14]> grad_output = ?,<br>Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[256, 128, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | None     | Fallback   |     1 |      0 |
|  4 | Tensor<[1, 256, 14, 14]> grad_output = ?,<br>Tensor<[1, 128, 28, 28]> input = ?,<br>Tensor<[256, 128, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | None     | Fallback   |     1 |      0 |
|  5 | Tensor<[1, 256, 14, 14]> grad_output = ?,<br>Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[256, 256, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | None     | Fallback   |     1 |      0 |
|  6 | Tensor<[1, 512, 7, 7]> grad_output = ?,<br>Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[512, 256, 1, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   |     1 |      0 |
|  7 | Tensor<[1, 512, 7, 7]> grad_output = ?,<br>Tensor<[1, 256, 14, 14]> input = ?,<br>Tensor<[512, 256, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   |     1 |      0 |
|  8 | Tensor<[1, 512, 7, 7]> grad_output = ?,<br>Tensor<[1, 512, 7, 7]> input = ?,<br>Tensor<[512, 512, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]     | None     | Fallback   |     1 |      0 |
|  9 | Tensor<[1, 64, 112, 112]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]   | None     | Fallback   |     1 |      0 |
| 10 | Tensor<[1, 64, 56, 56]> grad_output = ?,<br>Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False]     | None     | Fallback   |     1 |      0 |
### aten.detach.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 28, 28]> self = ?  | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 256, 14, 14]> self = ?  | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 512, 7, 7]> self = ?    | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 64, 112, 112]> self = ? | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 64, 56, 56]> self = ?   | None     | Fallback   |     1 |     -1 |
### aten.div.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512, 7, 7]> self = ?,<br>number other = 49 | None     | Fallback   |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512, 7, 7] | None     | Fallback   |     1 |     -1 |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1] | None     | Fallback   |     1 |      0 |
### aten.max_pool2d_with_indices_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 56, 56]> grad_output = ?,<br>Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = False,<br>Tensor<[1, 64, 56, 56]> indices = ? | None     | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       |     0 |      0 |
### aten.mm.default
|    | ATen Input Variations                                       | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 512]> mat2 = ? | Done     | Done       | 0.99985  |      0 |
|  1 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?    | Done     | Done       | 0.999996 |      0 |
### aten.native_batch_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 28, 28]> grad_out = ?,<br>Tensor<[1, 128, 28, 28]> input = ?,<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> running_mean = ?,<br>Optional[Tensor]<[128]> running_var = ?,<br>Optional[Tensor]<[128]> save_mean = ?,<br>Optional[Tensor]<[128]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 256, 14, 14]> grad_out = ?,<br>Tensor<[1, 256, 14, 14]> input = ?,<br>Optional[Tensor]<[256]> weight = ?,<br>Optional[Tensor]<[256]> running_mean = ?,<br>Optional[Tensor]<[256]> running_var = ?,<br>Optional[Tensor]<[256]> save_mean = ?,<br>Optional[Tensor]<[256]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
|  2 | Tensor<[1, 512, 7, 7]> grad_out = ?,<br>Tensor<[1, 512, 7, 7]> input = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> running_mean = ?,<br>Optional[Tensor]<[512]> running_var = ?,<br>Optional[Tensor]<[512]> save_mean = ?,<br>Optional[Tensor]<[512]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]     | None     | Fallback   |     1 |      0 |
|  3 | Tensor<[1, 64, 112, 112]> grad_out = ?,<br>Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> running_mean = ?,<br>Optional[Tensor]<[64]> running_var = ?,<br>Optional[Tensor]<[64]> save_mean = ?,<br>Optional[Tensor]<[64]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]    | None     | Fallback   |     1 |      0 |
|  4 | Tensor<[1, 64, 56, 56]> grad_out = ?,<br>Tensor<[1, 64, 56, 56]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> running_mean = ?,<br>Optional[Tensor]<[64]> running_var = ?,<br>Optional[Tensor]<[64]> save_mean = ?,<br>Optional[Tensor]<[64]> save_invstd = ?,<br>bool train = True,<br>float eps = 1e-05,<br>List[bool] output_mask = [True, True, True]        | None     | Fallback   |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 28, 28]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 256, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 512, 7, 7]> self = ?    | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 64, 112, 112]> self = ? | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 64, 56, 56]> self = ?   | Done     | Done       |     1 |      0 |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?   | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1000, 512]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[512, 1000]> self = ? | Done     | Done       |     1 |      0 |
### aten.threshold_backward.default
|    | ATen Input Variations                                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128, 28, 28]> grad_output = ?,<br>Tensor<[1, 128, 28, 28]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 256, 14, 14]> grad_output = ?,<br>Tensor<[1, 256, 14, 14]> self = ?,<br>number threshold = 0   | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 512, 7, 7]> grad_output = ?,<br>Tensor<[1, 512, 7, 7]> self = ?,<br>number threshold = 0       | None     | Fallback   |     1 |     -1 |
|  3 | Tensor<[1, 64, 112, 112]> grad_output = ?,<br>Tensor<[1, 64, 112, 112]> self = ?,<br>number threshold = 0 | None     | Fallback   |     1 |     -1 |
|  4 | Tensor<[1, 64, 56, 56]> grad_output = ?,<br>Tensor<[1, 64, 56, 56]> self = ?,<br>number threshold = 0     | None     | Fallback   |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]        | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 512, 1, 1]> self = ?,<br>List[int] size = [1, 512] | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 512, 1, 1] | Done     | Done       |     1 |      0 |

