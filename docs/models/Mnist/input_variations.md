# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._log_softmax.default            |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten.addmm.default                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  2 | aten.clone.default                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default             |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  4 | aten.max_pool2d_with_indices.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.relu.default                    |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  6 | aten.t.default                       |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  7 | aten.view.default                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[10]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 10]> mat2 = ?     | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ? | Done     | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 128]> self = ?        | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 64, 12, 12]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 26, 26]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Unknown    | N/A   | N/A    |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2] | Done     | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 128]> self = ?        | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32, 26, 26]> self = ? | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 64, 24, 24]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[10, 128]> self = ?   | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[128, 9216]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216] | Done     | Unknown    | N/A   | N/A    |

