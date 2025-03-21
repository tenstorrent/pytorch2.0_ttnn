# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten.convolution.default                          |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.silu.default                                 |                  1 |           1 |         0 |          0 | ✅          |       1 |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                            | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 256, 256]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.03,<br>float eps = 0.001 | Done     | Done       | 0.999988 |      1 |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                   | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 3, 512, 512]> input = ?,<br>Tensor<[32, 3, 6, 6]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [2, 2],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | 0.999929 |      2 |
### aten.silu.default
|    | ATen Input Variations              | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 256, 256]> self = ? | Done     | Done       | 0.999982 |      0 |

