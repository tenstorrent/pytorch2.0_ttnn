# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._to_copy.default          |                  2 |
|  2 | aten.add.Tensor                |                  2 |
|  3 | aten.addmm.default             |                  1 |
|  4 | aten.bmm.default               |                  1 |
|  5 | aten.cat.default               |                  1 |
|  6 | aten.clone.default             |                  2 |
|  7 | aten.cumsum.default            |                  1 |
|  8 | aten.div.Tensor                |                  1 |
|  9 | aten.embedding.default         |                  1 |
| 10 | aten.eq.Scalar                 |                  1 |
| 11 | aten.expand.default            |                 14 |
| 12 | aten.full.default              |                  1 |
| 13 | aten.gt.Scalar                 |                  1 |
| 14 | aten.lift_fresh_copy.default   |                  1 |
| 15 | aten.lt.Tensor                 |                  1 |
| 16 | aten.masked_fill.Scalar        |                  2 |
| 17 | aten.mm.default                |                  1 |
| 18 | aten.mul.Tensor                |                  3 |
| 19 | aten.native_layer_norm.default |                  1 |
| 20 | aten.new_ones.default          |                  1 |
| 21 | aten.permute.default           |                  1 |
| 22 | aten.pow.Tensor_Scalar         |                  1 |
| 23 | aten.rsub.Scalar               |                  1 |
| 24 | aten.select.int                |                  1 |
| 25 | aten.slice.Tensor              |                 11 |
| 26 | aten.sub.Tensor                |                  1 |
| 27 | aten.sum.default               |                  1 |
| 28 | aten.sym_size.int              |                  3 |
| 29 | aten.t.default                 |                  1 |
| 30 | aten.tanh.default              |                  1 |
| 31 | aten.topk.default              |                  1 |
| 32 | aten.transpose.int             |                  1 |
| 33 | aten.unsqueeze.default         |                  3 |
| 34 | aten.view.default              |                 28 |
| 35 | aten.where.self                |                  1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bool     | Unknown  |
|  1 | Tensor<[1, 1, 45, 45]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0            | Unknown  |
|  1 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ? | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[768]> self = ?,<br>Tensor<[45, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [arg0_1, new_ones],<br>int dim = -1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  1 | Tensor<[1, 45, 768]> self = ?                                                         | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>int dim = -1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ? | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>number other = 50256 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>List[int] size = [1, 1, 1, 46]                      | Unknown  |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, sym_size_int]       | Unknown  |
|  2 | Tensor<[1, 1, 45, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]                    | Unknown  |
|  3 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45]                            | Unknown  |
|  4 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]                    | Unknown  |
|  5 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]                    | Unknown  |
|  6 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, sym_size_int_2]   | Unknown  |
|  7 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]                  | Unknown  |
|  8 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]                  | Unknown  |
|  9 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [1, 12, 46, 64]                  | Unknown  |
| 10 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [1, 12, 64, 45]                  | Unknown  |
| 11 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [1, 12, 64, 46]                  | Unknown  |
| 12 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 64, sym_size_int_1] | Unknown  |
| 13 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 12, sym_size_int_3, 64] | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [45, 45],<br>number fill_value = -3.4028234663852886e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.gt.Scalar
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>number other = 0 | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.lt.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                          | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> mask = ?,<br>number value = -3.4028234663852886e+38 | Unknown  |
|  1 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 50257]> mask = ?,<br>number value = -inf                            | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715          | Unknown  |
|  1 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5              | Unknown  |
|  2 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.new_ones.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 46                 | Unknown  |
|  1 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?         | Unknown  |
|  2 | Tensor<[1, 1, 1, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  3 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1              | Unknown  |
|  4 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ? | Unknown  |
|  5 | Tensor<[1, 1, 45, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 45                | Unknown  |
|  6 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  7 | Tensor<[1, 45]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                         | Unknown  |
|  8 | Tensor<[1, 46]> self = ?,<br>int dim = 1,<br>Optional[int] start = 45,<br>Optional[int] end = -1                        | Unknown  |
|  9 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = -1                        | Unknown  |
| 10 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = -1                 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1 | Unknown  |
### aten.sum.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1]> self = ?    | Unknown  |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3   | Unknown  |
|  1 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[768, 768]> self = ? | Unknown  |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 45, 3072]> self = ? | Unknown  |
### aten.topk.default
|    | ATen Input Variations                      | Status   |
|---:|:-------------------------------------------|:---------|
|  0 | Tensor<[1, 50257]> self = ?,<br>int k = 50 | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 45, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 45]> self = ?,<br>int dim = 2 | Unknown  |
|  1 | Tensor<[1, 45]> self = ?,<br>int dim = 1    | Unknown  |
|  2 | Tensor<[45, 45]> self = ?,<br>int dim = 0   | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                        | Unknown  |
|  1 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 45]                            | Unknown  |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                          | Unknown  |
|  3 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [12, 1, 46]                    | Unknown  |
|  4 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]                    | Unknown  |
|  5 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [12, 1, sym_size_int_2]   | Unknown  |
|  6 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [12, 45, 45]                  | Unknown  |
|  7 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [12, 45, 64]                  | Unknown  |
|  8 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [12, 46, 64]                  | Unknown  |
|  9 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [12, 64, 45]                  | Unknown  |
| 10 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [12, 64, 46]                  | Unknown  |
| 11 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [12, 64, sym_size_int_1] | Unknown  |
| 12 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, sym_size_int_3, 64] | Unknown  |
| 13 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                                | Unknown  |
| 14 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                        | Unknown  |
| 15 | Tensor<[1, 45, 3072]> self = ?,<br>List[int] size = [45, 3072]                      | Unknown  |
| 16 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [45, 768]                        | Unknown  |
| 17 | Tensor<[1, 45]> self = ?,<br>List[int] size = [-1, 45]                              | Unknown  |
| 18 | Tensor<[1, 50257]> self = ?,<br>List[int] size = [1, 1, 50257]                      | Unknown  |
| 19 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                          | Unknown  |
| 20 | Tensor<[12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]                    | Unknown  |
| 21 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]                    | Unknown  |
| 22 | Tensor<[12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, sym_size_int_1]   | Unknown  |
| 23 | Tensor<[12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]                  | Unknown  |
| 24 | Tensor<[12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]                  | Unknown  |
| 25 | Tensor<[45, 3072]> self = ?,<br>List[int] size = [1, 45, 3072]                      | Unknown  |
| 26 | Tensor<[45, 50257]> self = ?,<br>List[int] size = [1, 45, 50257]                    | Unknown  |
| 27 | Tensor<[45, 768]> self = ?,<br>List[int] size = [1, 45, 768]                        | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 45, 45]> condition = ?,<br>Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[]> other = ? | Unknown  |

