# High Level Operations Status
|    | Operations                                    |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._log_softmax.default                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten._log_softmax_backward_data.default       |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.addmm.default                            |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  3 | aten.clone.default                            |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  4 | aten.convolution.default                      |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  5 | aten.convolution_backward.default             |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.detach.default                           |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.max_pool2d_with_indices.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.max_pool2d_with_indices_backward.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.mm.default                               |                  4 |           4 |         0 |          0 | ✅          |       1 |
| 10 | aten.relu.default                             |                  3 |           3 |         0 |          0 | ✅          |       1 |
| 11 | aten.sum.dim_IntList                          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.t.default                                |                  6 |           6 |         0 |          0 | ✅          |       1 |
| 13 | aten.threshold_backward.default               |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.view.default                             |                  4 |           4 |         0 |          0 | ✅          |       1 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Done     | Done       | True  |
### aten._log_softmax_backward_data.default
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> grad_output = ?,<br>Tensor<[1, 10]> output = ?,<br>int dim = 1,<br>int input_dtype = torch.bfloat16 | None     | Fallback   | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[10]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 10]> mat2 = ?     | Done     | Done       | True  |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ? | Done     | Done       | True  |
### aten.clone.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 128]> self = ?        | Done     | Done       | True  |
|  1 | Tensor<[1, 64, 12, 12]> self = ? | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  1 | Tensor<[1, 32, 26, 26]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 32, 26, 26]> grad_output = ?,<br>Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [32],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]   | None     | Fallback   | True  |
|  1 | Tensor<[1, 64, 24, 24]> grad_output = ?,<br>Tensor<[1, 32, 26, 26]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[List[int]] bias_sizes = [64],<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | Fallback   | True  |
### aten.detach.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?         | None     | Fallback   | True  |
|  1 | Tensor<[1, 128]> self = ?        | None     | Fallback   | True  |
|  2 | Tensor<[1, 32, 26, 26]> self = ? | None     | Fallback   | True  |
|  3 | Tensor<[1, 64, 24, 24]> self = ? | None     | Fallback   | True  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2] | None     | Fallback   | True  |
### aten.max_pool2d_with_indices_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 64, 12, 12]> grad_output = ?,<br>Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = False,<br>Tensor<[1, 64, 12, 12]> indices = ? | None     | Unknown    | N/A   |
### aten.mm.default
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 128]> mat2 = ?    | Done     | Done       | True  |
|  1 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 9216]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[10, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?     | Done     | Done       | True  |
|  3 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 9216]> mat2 = ?   | Done     | Done       | True  |
### aten.relu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 128]> self = ?        | Done     | Done       | True  |
|  1 | Tensor<[1, 32, 26, 26]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 64, 24, 24]> self = ? | Done     | Done       | True  |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True  | None     | Fallback   | True  |
|  1 | Tensor<[1, 128]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | None     | Fallback   | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?     | Done     | Done       | True  |
|  1 | Tensor<[1, 128]> self = ?    | Done     | Done       | True  |
|  2 | Tensor<[10, 128]> self = ?   | Done     | Done       | True  |
|  3 | Tensor<[128, 10]> self = ?   | Done     | Done       | True  |
|  4 | Tensor<[128, 9216]> self = ? | Done     | Done       | True  |
|  5 | Tensor<[9216, 128]> self = ? | Done     | Done       | True  |
### aten.threshold_backward.default
|    | ATen Input Variations                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 128]> grad_output = ?,<br>Tensor<[1, 128]> self = ?,<br>number threshold = 0               | None     | Fallback   | True  |
|  1 | Tensor<[1, 32, 26, 26]> grad_output = ?,<br>Tensor<[1, 32, 26, 26]> self = ?,<br>number threshold = 0 | None     | Fallback   | True  |
|  2 | Tensor<[1, 64, 24, 24]> grad_output = ?,<br>Tensor<[1, 64, 24, 24]> self = ?,<br>number threshold = 0 | None     | Fallback   | True  |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [10]              | Done     | Done       | True  |
|  1 | Tensor<[1, 128]> self = ?,<br>List[int] size = [128]            | Done     | Done       | True  |
|  2 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216] | Done     | Done       | True  |
|  3 | Tensor<[1, 9216]> self = ?,<br>List[int] size = [1, 64, 12, 12] | Done     | Done       | True  |

