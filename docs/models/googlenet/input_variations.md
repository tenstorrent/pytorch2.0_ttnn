# High Level Operations Status
|    | Operations                                        |   Input Variations |
|---:|:--------------------------------------------------|-------------------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |
|  1 | aten.add.Tensor                                   |                  1 |
|  2 | aten.addmm.default                                |                  1 |
|  3 | aten.cat.default                                  |                  1 |
|  4 | aten.clone.default                                |                  1 |
|  5 | aten.convolution.default                          |                  3 |
|  6 | aten.max_pool2d_with_indices.default              |                  3 |
|  7 | aten.mean.dim                                     |                  1 |
|  8 | aten.mul.Tensor                                   |                  1 |
|  9 | aten.relu.default                                 |                  1 |
| 10 | aten.select.int                                   |                  1 |
| 11 | aten.slice.Tensor                                 |                  1 |
| 12 | aten.t.default                                    |                  1 |
| 13 | aten.unsqueeze.default                            |                  1 |
| 14 | aten.view.default                                 |                  1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 112, 112]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 0.001 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027 | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1000]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [add, add_1, add_2],<br>int dim = 1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[1, 1024]> self = ? | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [2, 2],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Unknown  |
|  1 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[192, 64, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
|  2 | Tensor<[1, 64, 56, 56]> input = ?,<br>Tensor<[64, 64, 1, 1]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                                                                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 192, 28, 28]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | Unknown  |
|  1 | Tensor<[1, 64, 112, 112]> self = ?,<br>List[int] kernel_size = [3, 3],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True | Unknown  |
|  2 | Tensor<[1, 832, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool ceil_mode = True  | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458 | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 64, 112, 112]> self = ? | Unknown  |
### aten.select.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1000, 1024]> self = ? | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 224, 224]> self = ?,<br>int dim = 1 | Unknown  |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024] | Unknown  |

