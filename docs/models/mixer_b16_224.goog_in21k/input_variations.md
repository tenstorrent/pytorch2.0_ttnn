# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.add.Tensor                |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  1 | aten.addmm.default             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten.clone.default             |                  5 |           5 |         0 |          0 | ✅          |    1    |
|  3 | aten.convolution.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.gelu.default              |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  5 | aten.mean.dim                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  6 | aten.mm.default                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  7 | aten.native_layer_norm.default |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  8 | aten.t.default                 |                  5 |           5 |         0 |          0 | ✅          |    1    |
|  9 | aten.transpose.int             |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 10 | aten.view.default              |                  9 |           6 |         0 |          3 | 🚧          |    0.67 |
***
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ? | Done     |
|  1 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?         | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[196]> self = ?,<br>Tensor<[768, 384]> mat1 = ?,<br>Tensor<[384, 196]> mat2 = ?   | Done     |
|  1 | Tensor<[21843]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 21843]> mat2 = ? | Done     |
|  2 | Tensor<[3072]> self = ?,<br>Tensor<[196, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[196, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     |
### aten.clone.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 196, 3072]> self = ? | Done     |
|  1 | Tensor<[1, 196, 768]> self = ?  | Done     |
|  2 | Tensor<[1, 768, 196]> self = ?  | Done     |
|  3 | Tensor<[1, 768, 384]> self = ?  | Done     |
|  4 | Tensor<[1, 768]> self = ?       | Done     |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                               | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 16, 16]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[int] stride = [16, 16],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     |
### aten.gelu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 196, 3072]> self = ? | Done     |
|  1 | Tensor<[1, 768, 384]> self = ?  | Done     |
### aten.mean.dim
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>Optional[List[int]] dim = [1] | Done     |
### aten.mm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 384]> mat2 = ? | Done     |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-06 | Done     |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[196, 384]> self = ?   | Done     |
|  1 | Tensor<[21843, 768]> self = ? | Done     |
|  2 | Tensor<[3072, 768]> self = ?  | Done     |
|  3 | Tensor<[384, 196]> self = ?   | Done     |
|  4 | Tensor<[768, 3072]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
|  1 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     |
### aten.view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 196, 3072]> self = ?,<br>List[int] size = [196, 3072]     | Done     |
|  1 | Tensor<[1, 196, 768]> self = ?,<br>List[int] size = [196, 768]       | Done     |
|  2 | Tensor<[1, 768, 14, 14]> self = ?,<br>List[int] size = [1, 768, 196] | Fallback |
|  3 | Tensor<[1, 768, 196]> self = ?,<br>List[int] size = [768, 196]       | Fallback |
|  4 | Tensor<[1, 768, 384]> self = ?,<br>List[int] size = [768, 384]       | Done     |
|  5 | Tensor<[196, 3072]> self = ?,<br>List[int] size = [1, 196, 3072]     | Done     |
|  6 | Tensor<[196, 768]> self = ?,<br>List[int] size = [1, 196, 768]       | Done     |
|  7 | Tensor<[768, 196]> self = ?,<br>List[int] size = [1, 768, 196]       | Fallback |
|  8 | Tensor<[768, 384]> self = ?,<br>List[int] size = [1, 768, 384]       | Done     |

