# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.convolution.default                          |                 34 |          30 |         0 |          0 | 🚧          |    0.88 |
|  4 | aten.mean.dim                                     |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  6 | aten.relu.default                                 |                 13 |          13 |         0 |          0 | ✅          |    1    |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  8 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Optional[Tensor]<[1056]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>Tensor<[1056]> running_mean = ?,<br>Tensor<[1056]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999993 |      5 |
|  1 | Tensor<[1, 1056, 96, 96]> input = ?,<br>Optional[Tensor]<[1056]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>Tensor<[1056]> running_mean = ?,<br>Tensor<[1056]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      5 |
|  2 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Optional[Tensor]<[2904]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>Tensor<[2904]> running_mean = ?,<br>Tensor<[2904]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      5 |
|  3 | Tensor<[1, 2904, 48, 48]> input = ?,<br>Optional[Tensor]<[2904]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>Tensor<[2904]> running_mean = ?,<br>Tensor<[2904]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.99999  |      5 |
|  4 | Tensor<[1, 32, 192, 192]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | 0.999991 |      5 |
|  5 | Tensor<[1, 528, 192, 192]> input = ?,<br>Optional[Tensor]<[528]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>Tensor<[528]> running_mean = ?,<br>Tensor<[528]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05    | Done     | Done       | 0.999987 |      5 |
|  6 | Tensor<[1, 528, 96, 96]> input = ?,<br>Optional[Tensor]<[528]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>Tensor<[528]> running_mean = ?,<br>Tensor<[528]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | 0.999988 |      5 |
|  7 | Tensor<[1, 7392, 12, 12]> input = ?,<br>Optional[Tensor]<[7392]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>Tensor<[7392]> running_mean = ?,<br>Tensor<[7392]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999988 |      5 |
|  8 | Tensor<[1, 7392, 24, 24]> input = ?,<br>Optional[Tensor]<[7392]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>Tensor<[7392]> running_mean = ?,<br>Tensor<[7392]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | 0.999988 |      5 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ? | Done     | Done       | 0.999998 |      0 |
|  1 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ? | Done     | Done       | 0.999998 |      0 |
|  2 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?   | Done     | Done       | 0.999998 |      0 |
|  3 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ? | Done     | Done       | 0.999998 |      0 |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 7392]> mat1 = ?,<br>Tensor<[7392, 1000]> mat2 = ? | Done     | Done       | 0.997726 |      0 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1056, 1, 1]> input = ?,<br>Tensor<[132, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<[132]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999816 |      6 |
|  1 | Tensor<[1, 1056, 1, 1]> input = ?,<br>Tensor<[264, 1056, 1, 1]> weight = ?,<br>Optional[Tensor]<[264]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999817 |      6 |
|  2 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[1056, 1056, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999833 |      4 |
|  3 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[1056, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4      | Done     | Done       | 0.99952  |      4 |
|  4 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[2904, 1056, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999833 |      4 |
|  5 | Tensor<[1, 1056, 48, 48]> input = ?,<br>Tensor<[2904, 1056, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999833 |      4 |
|  6 | Tensor<[1, 1056, 96, 96]> input = ?,<br>Tensor<[1056, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 4      | None     | Fallback   | 1        |     -1 |
|  7 | Tensor<[1, 132, 1, 1]> input = ?,<br>Tensor<[1056, 132, 1, 1]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999974 |      6 |
|  8 | Tensor<[1, 132, 1, 1]> input = ?,<br>Tensor<[528, 132, 1, 1]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999976 |      6 |
|  9 | Tensor<[1, 264, 1, 1]> input = ?,<br>Tensor<[1056, 264, 1, 1]> weight = ?,<br>Optional[Tensor]<[1056]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.99996  |      6 |
| 10 | Tensor<[1, 264, 1, 1]> input = ?,<br>Tensor<[2904, 264, 1, 1]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999962 |      6 |
| 11 | Tensor<[1, 2904, 1, 1]> input = ?,<br>Tensor<[264, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<[264]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999452 |      6 |
| 12 | Tensor<[1, 2904, 1, 1]> input = ?,<br>Tensor<[726, 2904, 1, 1]> weight = ?,<br>Optional[Tensor]<[726]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999439 |      6 |
| 13 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[2904, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11     | Done     | Done       | 0.999524 |      4 |
| 14 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[2904, 2904, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999375 |      4 |
| 15 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[7392, 2904, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.999375 |      4 |
| 16 | Tensor<[1, 2904, 24, 24]> input = ?,<br>Tensor<[7392, 2904, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | None     | Fallback   | 1        |     -1 |
| 17 | Tensor<[1, 2904, 48, 48]> input = ?,<br>Tensor<[2904, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 11     | None     | Fallback   | 1        |     -1 |
| 18 | Tensor<[1, 3, 384, 384]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | 0.99998  |      4 |
| 19 | Tensor<[1, 32, 192, 192]> input = ?,<br>Tensor<[528, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999991 |      4 |
| 20 | Tensor<[1, 32, 192, 192]> input = ?,<br>Tensor<[528, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999991 |      4 |
| 21 | Tensor<[1, 528, 1, 1]> input = ?,<br>Tensor<[132, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<[132]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | 0.999923 |      6 |
| 22 | Tensor<[1, 528, 1, 1]> input = ?,<br>Tensor<[8, 528, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999936 |      6 |
| 23 | Tensor<[1, 528, 192, 192]> input = ?,<br>Tensor<[528, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2      | None     | Fallback   | 1        |     -1 |
| 24 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[1056, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999927 |      4 |
| 25 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[1056, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999927 |      4 |
| 26 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[528, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2        | Done     | Done       | 0.999516 |      4 |
| 27 | Tensor<[1, 528, 96, 96]> input = ?,<br>Tensor<[528, 528, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | 0.999927 |      4 |
| 28 | Tensor<[1, 726, 1, 1]> input = ?,<br>Tensor<[2904, 726, 1, 1]> weight = ?,<br>Optional[Tensor]<[2904]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999892 |      6 |
| 29 | Tensor<[1, 726, 1, 1]> input = ?,<br>Tensor<[7392, 726, 1, 1]> weight = ?,<br>Optional[Tensor]<[7392]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999889 |      6 |
| 30 | Tensor<[1, 7392, 1, 1]> input = ?,<br>Tensor<[726, 7392, 1, 1]> weight = ?,<br>Optional[Tensor]<[726]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.997792 |      6 |
| 31 | Tensor<[1, 7392, 12, 12]> input = ?,<br>Tensor<[7392, 7392, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | 0.997678 |      4 |
| 32 | Tensor<[1, 7392, 24, 24]> input = ?,<br>Tensor<[7392, 264, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 28     | Done     | Done       | 0.999523 |      4 |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[528, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[528]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | 0.999994 |      6 |
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
|  0 | Tensor<[1, 1056, 1, 1]> self = ? | Done     | Done       | 0.999757 |      0 |
|  1 | Tensor<[1, 2904, 1, 1]> self = ? | Done     | Done       | 0.999764 |      0 |
|  2 | Tensor<[1, 528, 1, 1]> self = ?  | Done     | Done       | 0.999723 |      0 |
|  3 | Tensor<[1, 7392, 1, 1]> self = ? | Done     | Done       | 0.999749 |      0 |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1000, 7392]> self = ? | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7392, 1, 1]> self = ?,<br>List[int] size = [1, 7392] | Done     | Done       |     1 |     -1 |

