# High Level Operations Status
|    | Operations                           |   Input Variations |
|---:|:-------------------------------------|-------------------:|
|  0 | aten._adaptive_avg_pool2d.default    |                  1 |
|  1 | aten.addmm.default                   |                  1 |
|  2 | aten.clone.default                   |                  1 |
|  3 | aten.convolution.default             |                  1 |
|  4 | aten.max_pool2d_with_indices.default |                  1 |
|  5 | aten.relu.default                    |                  1 |
|  6 | aten.t.default                       |                  1 |
|  7 | aten.view.default                    |                  1 |
***
### aten._adaptive_avg_pool2d.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] output_size = [7, 7] | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[4096]> self = ?,<br>Tensor<[1, 25088]> mat1 = ?,<br>Tensor<[25088, 4096]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations      | Status   |
|---:|:---------------------------|:---------|
|  0 | Tensor<[1, 4096]> self = ? | Unknown  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[64, 3, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Unknown  |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 224, 224]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2] | Unknown  |
### aten.relu.default
|    | ATen Input Variations              | Status   |
|---:|:-----------------------------------|:---------|
|  0 | Tensor<[1, 64, 224, 224]> self = ? | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[4096, 25088]> self = ? | Unknown  |
### aten.view.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 512, 7, 7]> self = ?,<br>List[int] size = [1, 25088] | Unknown  |

