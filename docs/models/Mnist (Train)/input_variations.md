# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |
|---:|:-------------------------------------|-------------------:|------------:|
|  0 | aten._log_softmax.default            |                  1 |           0 |
|  1 | aten.addmm.default                   |                  2 |           2 |
|  2 | aten.convolution.default             |                  2 |           0 |
|  3 | aten.max_pool2d_with_indices.default |                  1 |           0 |
|  4 | aten.native_dropout.default          |                  2 |           0 |
|  5 | aten.relu.default                    |                  3 |           3 |
|  6 | aten.t.default                       |                  2 |           2 |
|  7 | aten.view.default                    |                  1 |           0 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[10]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 10]> mat2 = ?     | Done     |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ? | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Unknown  |
|  1 | Tensor<[1, 32, 26, 26]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2] | Unknown  |
### aten.native_dropout.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 128]> input = ?,<br>float p = 0.5,<br>Optional[bool] train = True         | Unknown  |
|  1 | Tensor<[1, 64, 12, 12]> input = ?,<br>float p = 0.25,<br>Optional[bool] train = True | Unknown  |
### aten.relu.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 128]> self = ?        | Done     |
|  1 | Tensor<[1, 32, 26, 26]> self = ? | Done     |
|  2 | Tensor<[1, 64, 24, 24]> self = ? | Done     |
### aten.t.default
|    | ATen Input Variations        | Status   |
|---:|:-----------------------------|:---------|
|  0 | Tensor<[10, 128]> self = ?   | Done     |
|  1 | Tensor<[128, 9216]> self = ? | Done     |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216] | Unknown  |

