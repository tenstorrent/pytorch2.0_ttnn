# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  1 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |       1 |
|  2 | aten.clone.default             |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  3 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.gelu.default              |                  2 |           2 |         0 |          0 | ✅          |       1 |
|  5 | aten.mean.dim                  |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  7 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  8 | aten.t.default                 |                  5 |           5 |         0 |          0 | ✅          |       1 |
|  9 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |       1 |
| 10 | aten.view.default              |                  9 |           9 |         0 |          0 | ✅          |       1 |
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
### aten.gelu.default
|    | ATen Input Variations           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 3072]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 768, 384]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 384]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[196, 384]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[21843, 768]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[3072, 768]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[384, 196]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[768, 3072]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 196, 3072]> self = ?,<br>List[int] size = [196, 3072]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 196, 768]> self = ?,<br>List[int] size = [196, 768]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [768, 196]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 768, 384]> self = ?,<br>List[int] size = [768, 384]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[196, 3072]> self = ?,<br>List[int] size = [1, 196, 3072]     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[196, 768]> self = ?,<br>List[int] size = [1, 196, 768]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[768, 196]> self = ?,<br>List[int] size = [1, 768, 196]       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[768, 384]> self = ?,<br>List[int] size = [1, 768, 384]       | Done     | N/A                 | N/A          | N/A               | N/A                |

