# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._to_copy.default          |                  3 |
|  2 | aten.add.Tensor                |                  2 |
|  3 | aten.addmm.default             |                  1 |
|  4 | aten.bmm.default               |                  1 |
|  5 | aten.clone.default             |                  2 |
|  6 | aten.cumsum.default            |                  1 |
|  7 | aten.div.Tensor                |                  1 |
|  8 | aten.embedding.default         |                  2 |
|  9 | aten.expand.default            |                  4 |
| 10 | aten.gelu.default              |                  1 |
| 11 | aten.mul.Tensor                |                  2 |
| 12 | aten.native_layer_norm.default |                  1 |
| 13 | aten.ne.Scalar                 |                  1 |
| 14 | aten.permute.default           |                  1 |
| 15 | aten.rsub.Scalar               |                  1 |
| 16 | aten.slice.Tensor              |                  2 |
| 17 | aten.t.default                 |                  1 |
| 18 | aten.transpose.int             |                  1 |
| 19 | aten.unsqueeze.default         |                  2 |
| 20 | aten.view.default              |                 10 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                    | Unknown  |
|  1 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32                                                                            | Unknown  |
|  2 | Tensor<[1, 10]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ? | Unknown  |
|  1 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                    | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[10, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ? | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 10, 768]> self = ?                                                              | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                              | Unknown  |
|  1 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>List[int] size = [1, 10]                 | Unknown  |
|  1 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10] | Unknown  |
|  2 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64] | Unknown  |
|  3 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [1, 12, 64, 10] | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 10, 3072]> self = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.4028234663852886e+38 | Unknown  |
|  1 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                    | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>number other = 1 | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 514]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1      | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[768, 768]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2 | Unknown  |
|  1 | Tensor<[1, 10]> self = ?,<br>int dim = 1    | Unknown  |
### aten.view.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]     | Unknown  |
|  1 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]       | Unknown  |
|  2 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10] | Unknown  |
|  3 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64] | Unknown  |
|  4 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10] | Unknown  |
|  5 | Tensor<[10, 250002]> self = ?,<br>List[int] size = [1, 10, 250002] | Unknown  |
|  6 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]     | Unknown  |
|  7 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]       | Unknown  |
|  8 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10] | Unknown  |
|  9 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64] | Unknown  |

