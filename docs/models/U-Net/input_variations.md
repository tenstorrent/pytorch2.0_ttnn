# High Level Operations Status
|    | Operations                                       |   Input Variations |
|---:|:-------------------------------------------------|-------------------:|
|  0 | aten._native_batch_norm_legit_functional.default |                  1 |
|  1 | aten.add.Tensor                                  |                  1 |
|  2 | aten.cat.default                                 |                  1 |
|  3 | aten.convolution.default                         |                  3 |
|  4 | aten.max_pool2d_with_indices.default             |                  1 |
|  5 | aten.relu.default                                |                  1 |
|  6 | aten.sigmoid.default                             |                  1 |
***
### aten._native_batch_norm_legit_functional.default
|    | ATen Input Variations                                                                                                                                                                                                                                    | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 256, 256]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>bool training = True,<br>float momentum = 0.1,<br>float eps = 1e-05 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>Tensor other = 1 | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [convolution_10, relu_7],<br>int dim = 1 | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                            | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 256, 256]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = None,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Unknown  |
|  1 | Tensor<[1, 32, 256, 256]> input = ?,<br>Tensor<[1, 32, 1, 1]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Unknown  |
|  2 | Tensor<[1, 512, 16, 16]> input = ?,<br>Tensor<[512, 256, 2, 2]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = True,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 256, 256]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2] | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 32, 256, 256]> self = ? | Unknown  |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   |
|---:|:----------------------------------|:---------|
|  0 | Tensor<[1, 1, 256, 256]> self = ? | Unknown  |

