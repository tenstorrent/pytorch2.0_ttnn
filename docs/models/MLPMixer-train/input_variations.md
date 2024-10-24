# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._unsafe_view.default               |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten.add.Tensor                         |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                      |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  3 | aten.clone.default                      |                  5 |           4 |         0 |          0 | 🚧          |    0.8  |
|  4 | aten.convolution.default                |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.convolution_backward.default       |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.div.Scalar                         |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.expand.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.gelu.default                       |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  9 | aten.gelu_backward.default              |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.mean.dim                           |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 11 | aten.mm.default                         |                  7 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.native_layer_norm.default          |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.native_layer_norm_backward.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.permute.default                    |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 15 | aten.sum.dim_IntList                    |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.t.default                          |                  8 |           4 |         0 |          0 | 🚧          |    0.5  |
| 17 | aten.unsqueeze.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.view.default                       |                 11 |           5 |         0 |          0 | 🚧          |    0.45 |
***
### aten._unsafe_view.default
|    | ATen Input Variations                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] size = [1, 256, 768]    | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] size = [1, 3, 256, 256] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 512]> mat1 = ?,<br>Tensor<[512, 1000]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[256]> self = ?,<br>Tensor<[256, 512]> mat1 = ?,<br>Tensor<[512, 256]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[256, 256]> mat1 = ?,<br>Tensor<[256, 512]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[256, 768]> mat1 = ?,<br>Tensor<[768, 512]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 512]> self = ?                                                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 256]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 512]> self = ?                                                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 512]> input = ?,<br>Tensor<[256, 1024, 1]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 512]> input = ?,<br>Tensor<[1024, 256, 1]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 512]> grad_output = ?,<br>Tensor<[1, 256, 512]> input = ?,<br>Tensor<[1024, 256, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [1024],<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 512]> grad_output = ?,<br>Tensor<[1, 1024, 512]> input = ?,<br>Tensor<[256, 1024, 1]> weight = ?,<br>Optional[List[int]] bias_sizes = [256],<br>List[int] stride = [1],<br>List[int] padding = [0],<br>List[int] dilation = [1],<br>bool transposed = False,<br>List[int] output_padding = [0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Scalar
|    | ATen Input Variations                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 512, 256]> self = ?,<br>number other = 256 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 512, 1]> self = ?,<br>List[int] size = [1, 512, 256] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 512]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 256]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu_backward.default
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024, 512]> grad_output = ?,<br>Tensor<[1, 1024, 512]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 256]> grad_output = ?,<br>Tensor<[1, 256, 256]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 512, 256]> self = ?,<br>Optional[List[int]] dim = [2] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 512]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 512]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[256, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[256, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[512, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[512, 256]> self = ?,<br>Tensor<[256, 768]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 256, 512]> grad_out = ?,<br>Tensor<[1, 256, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Tensor<[1, 256, 1]> mean = ?,<br>Tensor<[1, 256, 1]> rstd = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[bool] output_mask = [True, True, True] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] dims = [0, 5, 1, 3, 2, 4] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 512]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 4, 3, 5, 1] | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 512, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1000]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[256, 256]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[256, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1000]> self = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1000, 512]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[256, 256]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[256, 512]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[512, 1000]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[512, 256]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[512, 768]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[768, 512]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 512]> self = ?,<br>int dim = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1000]> self = ?,<br>List[int] size = [1000]                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 256, 256]> self = ?,<br>List[int] size = [256, 256]                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 256, 512]> self = ?,<br>List[int] size = [256, 512]                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [1, 16, 16, 16, 16, 3]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 256, 768]> self = ?,<br>List[int] size = [256, 768]                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 256]> self = ?,<br>List[int] size = [256]                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 3, 256, 256]> self = ?,<br>List[int] size = [1, 3, 16, 16, 16, 16] | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 512]> self = ?,<br>List[int] size = [512]                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[256, 256]> self = ?,<br>List[int] size = [1, 256, 256]                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[256, 512]> self = ?,<br>List[int] size = [1, 256, 512]                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[256, 768]> self = ?,<br>List[int] size = [1, 256, 768]                | Unknown  | N/A                 | N/A          | N/A               | N/A                |

