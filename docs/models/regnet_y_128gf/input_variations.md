# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.convolution.default                          |                 34 |          31 |         0 |          0 | 🚧          |    0.91 |
|  4 | aten.mean.dim                                     |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  6 | aten.relu.default                                 |                 13 |          13 |         0 |          0 | ✅          |    1    |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  8 | aten.t.default                                    |                  1 |           0 |         1 |          0 | ✅          |    1    |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Optional[Tensor]<[1056]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>Tensor<[1056]> running_mean = ?,<br>Tensor<[1056]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |      0 |
|  1 | Tensor<[1, 1056, 96, 96]> input = ?,<br>Optional[Tensor]<[1056]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>Tensor<[1056]> running_mean = ?,<br>Tensor<[1056]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999989 |      0 |
|  2 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Optional[Tensor]<[2904]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>Tensor<[2904]> running_mean = ?,<br>Tensor<[2904]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999987 |      0 |
|  3 | Tensor<[1, 2904, 48, 48]> input = ?,<br>Optional[Tensor]<[2904]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>Tensor<[2904]> running_mean = ?,<br>Tensor<[2904]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      0 |
|  4 | Tensor<[1, 32, 192, 192]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999987 |      0 |
|  5 | Tensor<[1, 528, 192, 192]> input = ?,<br>Optional[Tensor]<[528]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>Tensor<[528]> running_mean = ?,<br>Tensor<[528]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999992 |      0 |
|  6 | Tensor<[1, 528, 96, 96]> input = ?,<br>Optional[Tensor]<[528]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>Tensor<[528]> running_mean = ?,<br>Tensor<[528]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999989 |      0 |
|  7 | Tensor<[1, 7392, 12, 12]> input = ?,<br>Optional[Tensor]<[7392]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>Tensor<[7392]> running_mean = ?,<br>Tensor<[7392]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      0 |
|  8 | Tensor<[1, 7392, 24, 24]> input = ?,<br>Optional[Tensor]<[7392]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>Tensor<[7392]> running_mean = ?,<br>Tensor<[7392]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999987 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |     PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|--------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 7392]> mat1 = ?,<br>Tensor<[7392, 1000]> mat2 = ? | Done     | Done       | 0.99984 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 1, 1]> input = ?,<br>Tensor<[132, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<[132]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999855 |      1 |
|  1 | Tensor<[1, 1056, 1, 1]> input = ?,<br>Tensor<[264, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<[264]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999843 |      1 |
|  2 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[1056, 1056, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999832 |      0 |
|  3 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[1056, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4      | Done     | Done       | 0.999523 |      0 |
|  4 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[2904, 1056, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999833 |      0 |
|  5 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[2904, 1056, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999833 |      0 |
|  6 | Tensor<[1, 1056, 96, 96]> input = ?,<br>Tensor<[1056, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4      | None     | Fallback   | 1        |     -1 |
|  7 | Tensor<[1, 132, 1, 1]> input = ?,<br>Tensor<[1056, 132, 1, 1]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999976 |      1 |
|  8 | Tensor<[1, 132, 1, 1]> input = ?,<br>Tensor<[528, 132, 1, 1]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999975 |      1 |
|  9 | Tensor<[1, 264, 1, 1]> input = ?,<br>Tensor<[1056, 264, 1, 1]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999965 |      1 |
| 10 | Tensor<[1, 264, 1, 1]> input = ?,<br>Tensor<[2904, 264, 1, 1]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999959 |      1 |
| 11 | Tensor<[1, 2904, 1, 1]> input = ?,<br>Tensor<[264, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<[264]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999402 |      1 |
| 12 | Tensor<[1, 2904, 1, 1]> input = ?,<br>Tensor<[726, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<[726]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999459 |      1 |
| 13 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[2904, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11     | Done     | Done       | 0.999525 |      0 |
| 14 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[2904, 2904, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999375 |      0 |
| 15 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[7392, 2904, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999375 |      0 |
| 16 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[7392, 2904, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999373 |      0 |
| 17 | Tensor<[1, 2904, 48, 48]> input = ?,<br>Tensor<[2904, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11     | None     | Fallback   | 1        |     -1 |
| 18 | Tensor<[1, 3, 384, 384]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.999981 |      0 |
| 19 | Tensor<[1, 32, 192, 192]> input = ?,<br>Tensor<[528, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999991 |      0 |
| 20 | Tensor<[1, 32, 192, 192]> input = ?,<br>Tensor<[528, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999991 |      0 |
| 21 | Tensor<[1, 528, 1, 1]> input = ?,<br>Tensor<[132, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<[132]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999941 |      1 |
| 22 | Tensor<[1, 528, 1, 1]> input = ?,<br>Tensor<[8, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999901 |      1 |
| 23 | Tensor<[1, 528, 192, 192]> input = ?,<br>Tensor<[528, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2      | None     | Fallback   | 1        |     -1 |
| 24 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[1056, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999927 |      0 |
| 25 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[1056, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999927 |      0 |
| 26 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[528, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2        | Done     | Done       | 0.999516 |      0 |
| 27 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[528, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999927 |      0 |
| 28 | Tensor<[1, 726, 1, 1]> input = ?,<br>Tensor<[2904, 726, 1, 1]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999899 |      1 |
| 29 | Tensor<[1, 726, 1, 1]> input = ?,<br>Tensor<[7392, 726, 1, 1]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999893 |      1 |
| 30 | Tensor<[1, 7392, 1, 1]> input = ?,<br>Tensor<[726, 7392, 1, 1]> weight = ?,<br>Optional[Tensor]<[726]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.997483 |      1 |
| 31 | Tensor<[1, 7392, 12, 12]> input = ?,<br>Tensor<[7392, 7392, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.997686 |      0 |
| 32 | Tensor<[1, 7392, 24, 24]> input = ?,<br>Tensor<[7392, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 28     | Done     | Done       | 0.999524 |      0 |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[528, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999994 |      1 |
### aten.mean.dim
|    | ATen Input Variations                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999995 |      0 |
|  1 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999995 |      0 |
|  2 | Tensor<[1, 528, 96, 96]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | 0.999995 |      0 |
|  3 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | 0.999995 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ? | Done     | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ? | Done     | Done       | 0.999996 |      0 |
|  2 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?   | Done     | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ? | Done     | Done       | 0.999996 |      0 |
### aten.relu.default
|    | ATen Input Variations               | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1056, 48, 48]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 1056, 96, 96]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 132, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  3 | Tensor<[1, 264, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
|  4 | Tensor<[1, 2904, 24, 24]> self = ?  | Done     | Done       |     1 |      0 |
|  5 | Tensor<[1, 2904, 48, 48]> self = ?  | Done     | Done       |     1 |      0 |
|  6 | Tensor<[1, 32, 192, 192]> self = ?  | Done     | Done       |     1 |      0 |
|  7 | Tensor<[1, 528, 192, 192]> self = ? | Done     | Done       |     1 |      0 |
|  8 | Tensor<[1, 528, 96, 96]> self = ?   | Done     | Done       |     1 |      0 |
|  9 | Tensor<[1, 726, 1, 1]> self = ?     | Done     | Done       |     1 |      0 |
| 10 | Tensor<[1, 7392, 12, 12]> self = ?  | Done     | Done       |     1 |      0 |
| 11 | Tensor<[1, 7392, 24, 24]> self = ?  | Done     | Done       |     1 |      0 |
| 12 | Tensor<[1, 8, 1, 1]> self = ?       | Done     | Done       |     1 |      0 |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 1, 1]> self = ? | Done     | Done       | 0.999749 |      0 |
|  1 | Tensor<[1, 2904, 1, 1]> self = ? | Done     | Done       | 0.999751 |      0 |
|  2 | Tensor<[1, 528, 1, 1]> self = ?  | Done     | Done       | 0.999742 |      0 |
|  3 | Tensor<[1, 7392, 1, 1]> self = ? | Done     | Done       | 0.999756 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 7392]> self = ? | Removed  | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7392, 1, 1]> self = ?,<br>List[int] size = [1, 7392] | Done     | Done       |     1 |      0 |

