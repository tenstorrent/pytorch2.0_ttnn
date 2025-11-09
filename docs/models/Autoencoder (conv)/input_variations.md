# High Level Operations Status
|    | Operations                           |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.convolution.default             |                  4 |           4 |         0 |          0 | ✅          |     1   |
|  1 | aten.max_pool2d_with_indices.default |                  2 |           1 |         0 |          0 | 🚧          |     0.5 |
|  2 | aten.relu.default                    |                  3 |           3 |         0 |          0 | ✅          |     1   |
***
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                       | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 28, 28]> input = ?,<br>Tensor<[16, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999983 |      1 |
|  1 | Tensor<[1, 16, 14, 14]> input = ?,<br>Tensor<[16, 1, 2, 2]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = True,<br>List[int] output_padding = [0, 0],<br>int groups = 1  | Done     | Done       | 0.999992 |      1 |
|  2 | Tensor<[1, 16, 14, 14]> input = ?,<br>Tensor<[4, 16, 3, 3]> weight = ?,<br>Optional[Tensor]<[4]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999978 |      1 |
|  3 | Tensor<[1, 4, 7, 7]> input = ?,<br>Tensor<[4, 16, 2, 2]> weight = ?,<br>Optional[Tensor]<[16]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = True,<br>List[int] output_padding = [0, 0],<br>int groups = 1    | Done     | Done       | 0.999994 |      1 |
### aten.max_pool2d_with_indices.default
|    | ATen Input Variations                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 28, 28]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2] | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 4, 14, 14]> self = ?,<br>List[int] kernel_size = [2, 2],<br>List[int] stride = [2, 2]  | None     | Fallback   |     1 |     -1 |
### aten.relu.default
|    | ATen Input Variations            | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 16, 14, 14]> self = ? | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 16, 28, 28]> self = ? | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 4, 14, 14]> self = ?  | Done     | Done       |     1 |      0 |

