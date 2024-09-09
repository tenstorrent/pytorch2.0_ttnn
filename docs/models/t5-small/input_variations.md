# High Level Operations Status
|    | Operations              |   Input Variations |
|---:|:------------------------|-------------------:|
|  0 | aten._softmax.default   |                  1 |
|  1 | aten._to_copy.default   |                  2 |
|  2 | aten.abs.default        |                  1 |
|  3 | aten.add.Tensor         |                  4 |
|  4 | aten.arange.default     |                  3 |
|  5 | aten.bmm.default        |                  1 |
|  6 | aten.cat.default        |                  1 |
|  7 | aten.clone.default      |                  2 |
|  8 | aten.div.Tensor         |                  3 |
|  9 | aten.embedding.default  |                  1 |
| 10 | aten.expand.default     |                 13 |
| 11 | aten.full_like.default  |                  2 |
| 12 | aten.gt.Scalar          |                  1 |
| 13 | aten.le.Tensor          |                  1 |
| 14 | aten.log.default        |                  1 |
| 15 | aten.lt.Scalar          |                  2 |
| 16 | aten.mean.dim           |                  1 |
| 17 | aten.minimum.default    |                  1 |
| 18 | aten.mm.default         |                  1 |
| 19 | aten.mul.Tensor         |                  5 |
| 20 | aten.neg.default        |                  1 |
| 21 | aten.ones.default       |                  2 |
| 22 | aten.permute.default    |                  1 |
| 23 | aten.pow.Tensor_Scalar  |                  1 |
| 24 | aten.relu.default       |                  1 |
| 25 | aten.repeat.default     |                  1 |
| 26 | aten.rsqrt.default      |                  1 |
| 27 | aten.rsub.Scalar        |                  1 |
| 28 | aten.slice.Tensor       |                  5 |
| 29 | aten.sub.Tensor         |                  1 |
| 30 | aten.sym_size.int       |                  1 |
| 31 | aten.t.default          |                  1 |
| 32 | aten.transpose.int      |                  2 |
| 33 | aten.unsqueeze.default  |                  3 |
| 34 | aten.view.default       |                 32 |
| 35 | aten.where.self         |                  1 |
| 36 | aten.zeros.default      |                  1 |
| 37 | aten.zeros_like.default |                  1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                           | Status   |
|---:|:--------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
|  1 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.int64        | Unknown  |
### aten.abs.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ? | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06     | Unknown  |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16            | Unknown  |
|  2 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0           | Unknown  |
|  3 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ? | Unknown  |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  |
|  1 | number end = 10,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  |
|  2 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [ones_1, _to_copy],<br>int dim = -1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 512]> self = ?                                                             | Unknown  |
|  1 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                 | Unknown  |
|  1 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                | Unknown  |
|  2 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                   | Unknown  |
|  1 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                     | Unknown  |
|  2 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                     | Unknown  |
|  3 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                   | Unknown  |
|  4 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, sym_size_int]     | Unknown  |
|  5 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]                 | Unknown  |
|  6 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]                 | Unknown  |
|  7 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [1, 8, 2, 64]                   | Unknown  |
|  8 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [1, 8, 64, 10]                 | Unknown  |
|  9 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [1, 8, 64, 1]                   | Unknown  |
| 10 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [1, 8, 64, 2]                   | Unknown  |
| 11 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 64, sym_size_int]   | Unknown  |
| 12 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 8, sym_size_int_1, 64] | Unknown  |
### aten.full_like.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False   | Unknown  |
|  1 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Unknown  |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | Unknown  |
### aten.log.default
|    | ATen Input Variations     | Status   |
|---:|:--------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ? | Unknown  |
### aten.lt.Scalar
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16  | Unknown  |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8 | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  |
### aten.minimum.default
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.4028234663852886e+38 | Unknown  |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922       | Unknown  |
|  2 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?            | Unknown  |
|  3 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                              | Unknown  |
|  4 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                           | Unknown  |
### aten.neg.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ? | Unknown  |
### aten.ones.default
|    | ATen Input Variations                                                                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 1],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                       | Unknown  |
|  1 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[10, 10, 8]> self = ?,<br>List[int] dims = [2, 0, 1] | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 512]> self = ?,<br>number exponent = 2 | Unknown  |
### aten.relu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 10, 2048]> self = ? | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[1, 10, 1]> self = ? | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                 | Status   |
|---:|:------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1     | Unknown  |
|  2 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1       | Unknown  |
|  3 | Tensor<[1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1        | Unknown  |
|  4 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = -1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ? | Unknown  |
### aten.sym_size.int
|    | ATen Input Variations                               | Status   |
|---:|:----------------------------------------------------|:---------|
|  0 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  |
### aten.t.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[512, 512]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 10, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
|  1 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2 | Unknown  |
|  1 | Tensor<[1, 10]> self = ?,<br>int dim = 1    | Unknown  |
|  2 | Tensor<[10]> self = ?,<br>int dim = 0       | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048]> self = ?,<br>List[int] size = [1, 2048]                     | Unknown  |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                       | Unknown  |
|  2 | Tensor<[1, 10, 2048]> self = ?,<br>List[int] size = [10, 2048]                   | Unknown  |
|  3 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [10, 512]                     | Unknown  |
|  4 | Tensor<[1, 10, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]                | Unknown  |
|  5 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                           | Unknown  |
|  6 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                             | Unknown  |
|  7 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 1, 2048]                     | Unknown  |
|  8 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]                   | Unknown  |
|  9 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                       | Unknown  |
| 10 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [8, 1, 10]                   | Unknown  |
| 11 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [8, 1, 1]                     | Unknown  |
| 12 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [8, 1, 2]                     | Unknown  |
| 13 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [8, 1, 64]                   | Unknown  |
| 14 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [8, 1, sym_size_int]     | Unknown  |
| 15 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [8, 10, 10]                 | Unknown  |
| 16 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [8, 10, 64]                 | Unknown  |
| 17 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [8, 2, 64]                   | Unknown  |
| 18 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [8, 64, 10]                 | Unknown  |
| 19 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [8, 64, 1]                   | Unknown  |
| 20 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [8, 64, 2]                   | Unknown  |
| 21 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [8, 64, sym_size_int]   | Unknown  |
| 22 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [8, sym_size_int_1, 64] | Unknown  |
| 23 | Tensor<[10, 2048]> self = ?,<br>List[int] size = [1, 10, 2048]                   | Unknown  |
| 24 | Tensor<[10, 512]> self = ?,<br>List[int] size = [1, 10, 512]                     | Unknown  |
| 25 | Tensor<[8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]                   | Unknown  |
| 26 | Tensor<[8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]                     | Unknown  |
| 27 | Tensor<[8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]                     | Unknown  |
| 28 | Tensor<[8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]                   | Unknown  |
| 29 | Tensor<[8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, sym_size_int]     | Unknown  |
| 30 | Tensor<[8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]                 | Unknown  |
| 31 | Tensor<[8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]                 | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ? | Unknown  |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [1, 8, 1, 10],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False | Unknown  |

