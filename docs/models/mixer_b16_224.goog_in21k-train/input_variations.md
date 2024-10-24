# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.add.Tensor                         |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  1 | aten.addmm.default                      |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.clone.default                      |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default                |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.convolution_backward.default       |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.div.Scalar                         |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.expand.default                     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.gelu.default                       |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  8 | aten.gelu_backward.default              |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.mean.dim                           |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 10 | aten.mm.default                         |                 10 |          10 |         0 |          0 | ✅          |       1 |
| 11 | aten.native_layer_norm.default          |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 12 | aten.native_layer_norm_backward.default |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.sum.dim_IntList                    |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.t.default                          |                 11 |          11 |         0 |          0 | ✅          |       1 |
| 15 | aten.transpose.int                      |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 16 | aten.unsqueeze.default                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
| 17 | aten.view.default                       |                 15 |          15 |         0 |          0 | ✅          |       1 |
***
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[196]> self = ?,<br>Tensor<[768, 384]> mat1 = ?,<br>Tensor<[384, 196]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[21843]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 21843]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[196, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[196, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 196, 768]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 768, 196]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 768, 384]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 768]> self = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 768, 14, 14]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[List[int]] bias_sizes = [768],<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, True] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Scalar
|    | ATen Input Variations                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>number other = 196 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 196, 768] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu.default
|    | ATen Input Variations           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 768, 384]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu_backward.default
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 3072]> grad_output = ?,<br>Tensor<[1, 196, 3072]> self = ? | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 768, 384]> grad_output = ?,<br>Tensor<[1, 768, 384]> self = ?   | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 21843]> self = ?,<br>Tensor<[21843, 768]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[196, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[196, 384]> self = ?,<br>Tensor<[384, 768]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[21843, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[3072, 196]> self = ?,<br>Tensor<[196, 768]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[384, 768]> self = ?,<br>Tensor<[768, 196]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 3072]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 384]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> grad_out = ?,<br>Tensor<[1, 196, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 196, 1]> mean = ?,<br>Tensor<[1, 196, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True] | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 21843]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 768, 384]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[196, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True      | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[196, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[768, 196]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True       | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 21843]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[196, 3072]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[196, 384]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[196, 768]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[21843, 768]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[3072, 768]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[384, 196]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[768, 196]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[768, 21843]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[768, 3072]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[768, 384]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 768]> self = ?,<br>int dim = 1 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [384]              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 196, 3072]> self = ?,<br>List[int] size = [196, 3072]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 196, 768]> self = ?,<br>List[int] size = [196, 768]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 196]> self = ?,<br>List[int] size = [196]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 21843]> self = ?,<br>List[int] size = [21843]             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]               | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [1, 768, 14, 14] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [768, 196]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 768, 384]> self = ?,<br>List[int] size = [768, 384]       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[196, 3072]> self = ?,<br>List[int] size = [1, 196, 3072]     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[196, 768]> self = ?,<br>List[int] size = [1, 196, 768]       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[768, 196]> self = ?,<br>List[int] size = [1, 768, 196]       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[768, 384]> self = ?,<br>List[int] size = [1, 768, 384]       | Done     | N/A                 | N/A          | N/A               | N/A                |

