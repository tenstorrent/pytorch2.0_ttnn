# High Level Operations Status
|    | Operations                                    |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._log_softmax.default                     |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  1 | aten._log_softmax_backward_data.default       |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._softmax.default                         |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.addmm.default                            |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  4 | aten.clone.default                            |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  5 | aten.convolution.default                      |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  6 | aten.convolution_backward.default             |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.detach.default                           |                  4 |           0 |         4 |          0 | ✅          |       1 |
|  8 | aten.log.default                              |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.max_pool2d_with_indices.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.max_pool2d_with_indices_backward.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.mm.default                               |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 12 | aten.relu.default                             |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 13 | aten.sum.dim_IntList                          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.t.default                                |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 15 | aten.threshold_backward.default               |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.view.default                             |                  4 |           4 |         0 |          0 | ✅          |       1 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Removed  | Done       | 0.999896 |      0 |
### aten._log_softmax_backward_data.default
|    | ATen Input Variations                                                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> grad_output = ?,<br>Tensor<[1, 10]> output = ?,<br>int dim = 1,<br>int input_dtype = torch.bfloat16 | None     | Fallback   |     1 |     -1 |
### aten._softmax.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[10]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 10]> mat2 = ?     | Done     | Done       | 0.999987 |      0 |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ? | Done     | Done       | 0.999886 |      0 |
### aten.clone.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ?        | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 64, 12, 12]> self = ? | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999983 |      1 |
|  1 | Tensor<[1, 32, 26, 26]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999959 |      1 |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 32, 26, 26]> grad_output = ?,<br>Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [32],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]   | None     | Fallback   |     1 |      0 |
|  1 | Tensor<[1, 64, 24, 24]> grad_output = ?,<br>Tensor<[1, 32, 26, 26]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [64],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   |     1 |      0 |
### aten.detach.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?         | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 128]> self = ?        | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 32, 26, 26]> self = ? | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 64, 24, 24]> self = ? | Removed  | Done       |     1 |     -1 |
### aten.log.default
|    | ATen Input Variations    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2] | None     | Fallback   |     1 |      0 |
### aten.max_pool2d_with_indices_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 12, 12]> grad_output = ?,<br>Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = False,<br>Tensor<[1, 64, 12, 12]> indices = ? | None     | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                      | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 128]> mat2 = ?    | Done     | Done       | 0.999993 |      0 |
|  1 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 9216]> mat2 = ? | Done     | Done       | 0.99998  |      0 |
|  2 | Tensor<[10, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?     | Done     | Done       | 0.999991 |      0 |
|  3 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 9216]> mat2 = ?   | Done     | Done       | 0.999992 |      0 |
### aten.relu.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ?        | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 26, 26]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 64, 24, 24]> self = ? | Done     | Done       |     1 |      0 |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True  | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 128]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | None     | Fallback   |     1 |     -1 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?     | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 128]> self = ?    | Done     | Done       |     1 |      0 |
|  2 | Tensor<[10, 128]> self = ?   | Done     | Done       |     1 |      0 |
|  3 | Tensor<[128, 10]> self = ?   | Done     | Done       |     1 |      0 |
|  4 | Tensor<[128, 9216]> self = ? | Done     | Done       |     1 |      0 |
|  5 | Tensor<[9216, 128]> self = ? | Done     | Done       |     1 |      0 |
### aten.threshold_backward.default
|    | ATen Input Variations                                                                                 | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> grad_output = ?,<br>Tensor<[1, 128]> self = ?,<br>number threshold = 0               | None     | Fallback   |     1 |     -1 |
|  1 | Tensor<[1, 32, 26, 26]> grad_output = ?,<br>Tensor<[1, 32, 26, 26]> self = ?,<br>number threshold = 0 | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[1, 64, 24, 24]> grad_output = ?,<br>Tensor<[1, 64, 24, 24]> self = ?,<br>number threshold = 0 | None     | Fallback   |     1 |     -1 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10]              | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128]            | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216] | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 9216]> self = ?,<br>List[int] size = [1, 64, 12, 12] | Done     | Done       |     1 |      0 |

