# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._log_softmax.default            |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  1 | aten._softmax.default                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.addmm.default                   |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  3 | aten.clone.default                   |                  2 |           0 |         2 |          0 | ✅          |       1 |
|  4 | aten.convolution.default             |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  5 | aten.log.default                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.max_pool2d_with_indices.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.relu.default                    |                  3 |           3 |         0 |          0 | ✅          |       1 |
|  8 | aten.t.default                       |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  9 | aten.view.default                    |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._log_softmax.default
|    | ATen Input Variations                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Removed  | Done       | 0.999556 |      0 |
### aten._softmax.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | Done     | Unknown    | N/A   | N/A    |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[10]> self = ?,<br>Tensor<[1, 128]> mat1 = ?,<br>Tensor<[128, 10]> mat2 = ?     | Done     | Done       | 0.999997 |      0 |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[1, 9216]> mat1 = ?,<br>Tensor<[9216, 128]> mat2 = ? | Done     | Done       | 0.999902 |      0 |
### aten.clone.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ?        | Removed  | Done       |     1 |      0 |
|  1 | Tensor<[1, 64, 12, 12]> self = ? | Removed  | Done       |     1 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                         | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[32, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999984 |      1 |
|  1 | Tensor<[1, 32, 26, 26]> input = ?,<br>Tensor<[64, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.99996  |      1 |
### aten.log.default
|    | ATen Input Variations    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ? | Done     | Unknown    | N/A   | N/A    |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 24, 24]> self = ?,<br>List[int] kernel_size = [2, 2] | Done     | Done       |     1 |      0 |
### aten.relu.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 128]> self = ?        | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 32, 26, 26]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 64, 24, 24]> self = ? | Done     | Done       |     1 |      0 |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10, 128]> self = ?   | Done     | Done       |     1 |      0 |
|  1 | Tensor<[128, 9216]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 12, 12]> self = ?,<br>List[int] size = [1, 9216] | Done     | Done       |     1 |      0 |

