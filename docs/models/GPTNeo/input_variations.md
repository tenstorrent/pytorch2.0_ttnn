# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  3 |           0 |
|  1 | aten._to_copy.default          |                  6 |           0 |
|  2 | aten.add.Tensor                |                  9 |           0 |
|  3 | aten.addmm.default             |                  6 |           0 |
|  4 | aten.bmm.default               |                  6 |           0 |
|  5 | aten.cat.default               |                  4 |           0 |
|  6 | aten.clone.default             |                  8 |           0 |
|  7 | aten.cumsum.default            |                  2 |           0 |
|  8 | aten.div.Tensor                |                  1 |           0 |
|  9 | aten.embedding.default         |                  4 |           0 |
| 10 | aten.eq.Scalar                 |                  1 |           0 |
| 11 | aten.expand.default            |                 15 |           0 |
| 12 | aten.full.default              |                  1 |           0 |
| 13 | aten.gt.Scalar                 |                  1 |           0 |
| 14 | aten.lift_fresh_copy.default   |                  1 |           0 |
| 15 | aten.lt.Tensor                 |                  1 |           0 |
| 16 | aten.masked_fill.Scalar        |                  4 |           0 |
| 17 | aten.mm.default                |                  4 |           0 |
| 18 | aten.mul.Tensor                |                  8 |           0 |
| 19 | aten.native_layer_norm.default |                  2 |           0 |
| 20 | aten.new_ones.default          |                  2 |           0 |
| 21 | aten.permute.default           |                  4 |           0 |
| 22 | aten.pow.Tensor_Scalar         |                  2 |           0 |
| 23 | aten.rsub.Scalar               |                  3 |           0 |
| 24 | aten.select.int                |                  2 |           0 |
| 25 | aten.slice.Tensor              |                 21 |           0 |
| 26 | aten.sub.Tensor                |                  2 |           0 |
| 27 | aten.sum.default               |                  1 |           0 |
| 28 | aten.sym_size.int              |                  3 |           0 |
| 29 | aten.t.default                 |                  4 |           0 |
| 30 | aten.tanh.default              |                  2 |           0 |
| 31 | aten.topk.default              |                  1 |           0 |
| 32 | aten.transpose.int             |                  3 |           0 |
| 33 | aten.unsqueeze.default         |                  9 |           0 |
| 34 | aten.view.default              |                 34 |           0 |
| 35 | aten.where.self                |                  3 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 1, 46]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  |
|  1 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
|  2 | Tensor<[1, 12, 45, 45]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>Optional[int] dtype = torch.bool         | Unknown  |
|  1 | Tensor<[1, 1, 1, 46]> self = ?,<br>Optional[int] dtype = torch.float32      | Unknown  |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bool    | Unknown  |
|  3 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
|  4 | Tensor<[1, 1, 45, 45]> self = ?,<br>Optional[int] dtype = torch.bool        | Unknown  |
|  5 | Tensor<[1, 1, 45, 45]> self = ?,<br>Optional[int] dtype = torch.float32     | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Unknown  |
|  3 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  |
|  4 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  |
|  5 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  |
|  6 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  |
|  7 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  |
|  8 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[3072]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[45, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Unknown  |
|  2 | Tensor<[768]> self = ?,<br>Tensor<[1, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  |
|  3 | Tensor<[768]> self = ?,<br>Tensor<[1, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[45, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[45, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  |
|  1 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  |
|  2 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  |
|  3 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  |
|  4 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  |
|  5 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = ['torch.Size([1, 12, 45, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int dim = -2  | Unknown  |
|  1 | List[Tensor] tensors = ['torch.Size([1, 12, s10, 64])', 'torch.Size([1, 12, 1, 64])'],<br>int dim = -2 | Unknown  |
|  2 | List[Tensor] tensors = ['torch.Size([1, 45])', 'torch.Size([1, 1])'],<br>int dim = -1                  | Unknown  |
|  3 | List[Tensor] tensors = ['torch.Size([1, s24])', 'torch.Size([1, 1])'],<br>int dim = -1                 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 45]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format      | Unknown  |
|  1 | Tensor<[1, 1, 768]> self = ?                                                               | Unknown  |
|  2 | Tensor<[1, 12, 1, 46]> self = ?                                                            | Unknown  |
|  3 | Tensor<[1, 12, 1, s10 + 1]> self = ?                                                       | Unknown  |
|  4 | Tensor<[1, 12, 45, 45]> self = ?                                                           | Unknown  |
|  5 | Tensor<[1, 45, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
|  6 | Tensor<[1, 45, 768]> self = ?                                                              | Unknown  |
|  7 | Tensor<[1, s10 + 1]> self = ?                                                              | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                     | Status   |
|---:|:------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>int dim = -1 | Unknown  |
|  1 | Tensor<[1, s0]> self = ?,<br>int dim = -1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?   | Unknown  |
|  1 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?  | Unknown  |
|  2 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?  | Unknown  |
|  3 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ? | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>number other = 50256 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]                            | Unknown  |
|  1 | Tensor<[1, 1, 1, 46]> self = ?,<br>List[int] size = [1, 1, 1, 46]                             | Unknown  |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, 'torch.Size(s10 + 1)']     | Unknown  |
|  3 | Tensor<[1, 1, 45, 45]> self = ?,<br>List[int] size = [1, 1, 45, 45]                           | Unknown  |
|  4 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 1, 45]                                   | Unknown  |
|  5 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]                           | Unknown  |
|  6 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]                           | Unknown  |
|  7 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, 'torch.Size(s10 + 1)']   | Unknown  |
|  8 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]                         | Unknown  |
|  9 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]                         | Unknown  |
| 10 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [1, 12, 46, 64]                         | Unknown  |
| 11 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [1, 12, 64, 45]                         | Unknown  |
| 12 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [1, 12, 64, 46]                         | Unknown  |
| 13 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 64, 'torch.Size(s10 + 1)'] | Unknown  |
| 14 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 12, 'torch.Size(s10 + 1)', 64] | Unknown  |
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
|    | ATen Input Variations                                                                                                  | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> mask = ?,<br>number value = -3.4028234663852886e+38           | Unknown  |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> mask = ?,<br>number value = -3.4028234663852886e+38 | Unknown  |
|  2 | Tensor<[1, 1, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> mask = ?,<br>number value = -3.4028234663852886e+38         | Unknown  |
|  3 | Tensor<[1, 50257]> self = ?,<br>Tensor<[1, 50257]> mask = ?,<br>number value = -inf                                    | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?  | Unknown  |
|  1 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  |
|  2 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ? | Unknown  |
|  3 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715            | Unknown  |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                 | Unknown  |
|  2 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654  | Unknown  |
|  3 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?     | Unknown  |
|  4 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715           | Unknown  |
|  5 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                | Unknown  |
|  6 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654 | Unknown  |
|  7 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?   | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05  | Unknown  |
|  1 | Tensor<[1, 45, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.new_ones.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False  | Unknown  |
|  1 | Tensor<[1, s24]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  |
|  1 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Unknown  |
|  2 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
|  3 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?,<br>number exponent = 3.0  | Unknown  |
|  1 | Tensor<[1, 45, 3072]> self = ?,<br>number exponent = 3.0 | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  |
|  2 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  |
### aten.select.int
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  |
|  1 | Tensor<[1, 50]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 46                 | Unknown  |
|  1 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?         | Unknown  |
|  2 | Tensor<[1, 1, 1, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  3 | Tensor<[1, 1, 1, 46]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                   | Unknown  |
|  4 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1              | Unknown  |
|  5 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1              | Unknown  |
|  6 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1              | Unknown  |
|  7 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 45              | Unknown  |
|  8 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 45,<br>Optional[int] end = 46             | Unknown  |
|  9 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ? | Unknown  |
| 10 | Tensor<[1, 1, 45, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 45                | Unknown  |
| 11 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
| 12 | Tensor<[1, 1, 45, 45]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
| 13 | Tensor<[1, 45]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                         | Unknown  |
| 14 | Tensor<[1, 46]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                         | Unknown  |
| 15 | Tensor<[1, 46]> self = ?,<br>int dim = 1,<br>Optional[int] start = 45,<br>Optional[int] end = -1                        | Unknown  |
| 16 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                         | Unknown  |
| 17 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = -1                        | Unknown  |
| 18 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                     | Unknown  |
| 19 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = -1                 | Unknown  |
| 20 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1 | Unknown  |
|  1 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1 | Unknown  |
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
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[3072, 768]> self = ?  | Unknown  |
|  1 | Tensor<[50257, 768]> self = ? | Unknown  |
|  2 | Tensor<[768, 3072]> self = ?  | Unknown  |
|  3 | Tensor<[768, 768]> self = ?   | Unknown  |
### aten.tanh.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 1, 3072]> self = ?  | Unknown  |
|  1 | Tensor<[1, 45, 3072]> self = ? | Unknown  |
### aten.topk.default
|    | ATen Input Variations                      | Status   |
|---:|:-------------------------------------------|:---------|
|  0 | Tensor<[1, 50257]> self = ?,<br>int k = 50 | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 45, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
|  1 | Tensor<[1, 12, 46, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  |
|  2 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 45]> self = ?,<br>int dim = 2      | Unknown  |
|  1 | Tensor<[1, 1, 46]> self = ?,<br>int dim = 2      | Unknown  |
|  2 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2 | Unknown  |
|  3 | Tensor<[1, 45, 45]> self = ?,<br>int dim = 1     | Unknown  |
|  4 | Tensor<[1, 45]> self = ?,<br>int dim = 1         | Unknown  |
|  5 | Tensor<[1, 46]> self = ?,<br>int dim = 1         | Unknown  |
|  6 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1    | Unknown  |
|  7 | Tensor<[1]> self = ?,<br>int dim = 1             | Unknown  |
|  8 | Tensor<[45, 45]> self = ?,<br>int dim = 0        | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, 1, 768]                           | Unknown  |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                               | Unknown  |
|  2 | Tensor<[1, 1, 45]> self = ?,<br>List[int] size = [1, 45]                                   | Unknown  |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [-1, 1, 768]                             | Unknown  |
|  4 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 1, 12, 64]                           | Unknown  |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                                 | Unknown  |
|  6 | Tensor<[1, 12, 1, 46]> self = ?,<br>List[int] size = [12, 1, 46]                           | Unknown  |
|  7 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]                           | Unknown  |
|  8 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>List[int] size = [12, 1, 'torch.Size(s10 + 1)']   | Unknown  |
|  9 | Tensor<[1, 12, 45, 45]> self = ?,<br>List[int] size = [12, 45, 45]                         | Unknown  |
| 10 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] size = [12, 45, 64]                         | Unknown  |
| 11 | Tensor<[1, 12, 46, 64]> self = ?,<br>List[int] size = [12, 46, 64]                         | Unknown  |
| 12 | Tensor<[1, 12, 64, 45]> self = ?,<br>List[int] size = [12, 64, 45]                         | Unknown  |
| 13 | Tensor<[1, 12, 64, 46]> self = ?,<br>List[int] size = [12, 64, 46]                         | Unknown  |
| 14 | Tensor<[1, 12, 64, s10 + 1]> self = ?,<br>List[int] size = [12, 64, 'torch.Size(s10 + 1)'] | Unknown  |
| 15 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>List[int] size = [12, 'torch.Size(s10 + 1)', 64] | Unknown  |
| 16 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                                       | Unknown  |
| 17 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                               | Unknown  |
| 18 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] size = [1, 45, 768]                         | Unknown  |
| 19 | Tensor<[1, 45, 3072]> self = ?,<br>List[int] size = [45, 3072]                             | Unknown  |
| 20 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [-1, 45, 768]                           | Unknown  |
| 21 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [1, 45, 12, 64]                         | Unknown  |
| 22 | Tensor<[1, 45, 768]> self = ?,<br>List[int] size = [45, 768]                               | Unknown  |
| 23 | Tensor<[1, 45]> self = ?,<br>List[int] size = [-1, 45]                                     | Unknown  |
| 24 | Tensor<[1, 50257]> self = ?,<br>List[int] size = [1, 1, 50257]                             | Unknown  |
| 25 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                                 | Unknown  |
| 26 | Tensor<[12, 1, 46]> self = ?,<br>List[int] size = [1, 12, 1, 46]                           | Unknown  |
| 27 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]                           | Unknown  |
| 28 | Tensor<[12, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 12, 1, 'torch.Size(s10 + 1)']   | Unknown  |
| 29 | Tensor<[12, 45, 45]> self = ?,<br>List[int] size = [1, 12, 45, 45]                         | Unknown  |
| 30 | Tensor<[12, 45, 64]> self = ?,<br>List[int] size = [1, 12, 45, 64]                         | Unknown  |
| 31 | Tensor<[45, 3072]> self = ?,<br>List[int] size = [1, 45, 3072]                             | Unknown  |
| 32 | Tensor<[45, 50257]> self = ?,<br>List[int] size = [1, 45, 50257]                           | Unknown  |
| 33 | Tensor<[45, 768]> self = ?,<br>List[int] size = [1, 45, 768]                               | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 46]> condition = ?,<br>Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[]> other = ?           | Unknown  |
|  1 | Tensor<[1, 1, 1, s10 + 1]> condition = ?,<br>Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
|  2 | Tensor<[1, 1, 45, 45]> condition = ?,<br>Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[]> other = ?         | Unknown  |

