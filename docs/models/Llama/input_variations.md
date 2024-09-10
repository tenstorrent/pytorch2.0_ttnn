# High Level Operations Status
|    | Operations               |   Input Variations |   Converted |
|---:|:-------------------------|-------------------:|------------:|
|  0 | aten._softmax.default    |                  1 |           0 |
|  1 | aten._to_copy.default    |                  6 |           0 |
|  2 | aten.add.Tensor          |                  4 |           0 |
|  3 | aten.all.dim             |                  1 |           0 |
|  4 | aten.any.default         |                  1 |           0 |
|  5 | aten.arange.start        |                  1 |           0 |
|  6 | aten.bitwise_not.default |                  1 |           0 |
|  7 | aten.bmm.default         |                  3 |           0 |
|  8 | aten.cat.default         |                  2 |           0 |
|  9 | aten.clone.default       |                  1 |           0 |
| 10 | aten.cos.default         |                  1 |           0 |
| 11 | aten.embedding.default   |                  1 |           1 |
| 12 | aten.eq.Tensor           |                  1 |           0 |
| 13 | aten.expand.default      |                  6 |           0 |
| 14 | aten.index.Tensor        |                  1 |           0 |
| 15 | aten.mean.dim            |                  1 |           0 |
| 16 | aten.min.default         |                  1 |           0 |
| 17 | aten.mm.default          |                  4 |           0 |
| 18 | aten.mul.Scalar          |                  2 |           0 |
| 19 | aten.mul.Tensor          |                  6 |           1 |
| 20 | aten.ne.Scalar           |                  1 |           0 |
| 21 | aten.neg.default         |                  1 |           0 |
| 22 | aten.pow.Tensor_Scalar   |                  1 |           0 |
| 23 | aten.repeat.default      |                  1 |           0 |
| 24 | aten.rsqrt.default       |                  1 |           0 |
| 25 | aten.silu.default        |                  1 |           0 |
| 26 | aten.sin.default         |                  1 |           0 |
| 27 | aten.slice.Tensor        |                 10 |           0 |
| 28 | aten.t.default           |                  4 |           0 |
| 29 | aten.transpose.int       |                  3 |           0 |
| 30 | aten.unsqueeze.default   |                  8 |           3 |
| 31 | aten.view.default        |                 15 |           0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                | Status   |
|---:|:-------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 32]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Optional[int]<> dtype = torch.bfloat16 | Unknown  |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>Optional[int]<> dtype = torch.float32          | Unknown  |
|  2 | Tensor<[1, 32, 128]> self = ?,<br>Optional[int]<> dtype = torch.bfloat16       | Unknown  |
|  3 | Tensor<[1, 32, 32000]> self = ?,<br>Optional[int]<> dtype = torch.float32      | Unknown  |
|  4 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int]<> dtype = torch.bfloat16      | Unknown  |
|  5 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int]<> dtype = torch.float32       | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 1]> self = ?,<br>Tensor<> other = 1e-06                   | Unknown  |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 32, 32, 128]> other = ? | Unknown  |
|  2 | Tensor<[1, 32, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> other = ?    | Unknown  |
|  3 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?       | Unknown  |
### aten.all.dim
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int<> dim = -1 | Unknown  |
### aten.any.default
|    | ATen Input Variations    | Status   |
|---:|:-------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ? | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> start = 0,<br>number<> end = 32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.bitwise_not.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 1]> self = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ?       | Unknown  |
|  1 | Tensor<[32, 32, 128]> self = ?,<br>Tensor<[32, 128, 32]> mat2 = ? | Unknown  |
|  2 | Tensor<[32, 32, 32]> self = ?,<br>Tensor<[32, 32, 128]> mat2 = ?  | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 32, 32, 64])', 'torch.Size([1, 32, 32, 64])'],<br>int<> dim = -1 | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 32, 64])', 'torch.Size([1, 32, 64])'],<br>int<> dim = -1         | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Unknown  |
### aten.cos.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int<> padding_idx = 0 | Done     |
### aten.eq.Tensor
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int]<> size = [1, 1, 32]             | Unknown  |
|  1 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int]<> size = [1, 32, 128, 32] | Unknown  |
|  2 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int]<> size = [1, 32, 32, 128] | Unknown  |
|  3 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int]<> size = [1, 32, 32, 32]   | Unknown  |
|  4 | Tensor<[1, 64, 1]> self = ?,<br>List[int]<> size = [1, -1, 1]             | Unknown  |
|  5 | Tensor<[1, 64, 1]> self = ?,<br>List[int]<> size = [1, 64, 1]             | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 32]> self = ?,<br>List[Optional[Tensor]]<> indices = [None, None, 'torch.Size([32])'] | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[List[int]]<> dim = [-1],<br>bool<> keepdim = True | Unknown  |
### aten.min.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[32, 11008]> self = ?,<br>Tensor<[11008, 4096]> mat2 = ? | Unknown  |
|  1 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 11008]> mat2 = ?  | Unknown  |
|  2 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 32000]> mat2 = ?  | Unknown  |
|  3 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 4096]> mat2 = ?   | Unknown  |
### aten.mul.Scalar
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 128, 32]> self = ?,<br>number<> other = 0.29730177875068026 | Unknown  |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>number<> other = 0.29730177875068026 | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<> other = -3.3895313892515355e+38 | Done     |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[1, 1, 2048, 1]> other = ?        | Unknown  |
|  2 | Tensor<[1, 32, 11008]> self = ?,<br>Tensor<[1, 32, 11008]> other = ?             | Unknown  |
|  3 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 1, 32, 128]> other = ?          | Unknown  |
|  4 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 1]> other = ?                  | Unknown  |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?                      | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>number<> other = 1 | Unknown  |
### aten.neg.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 64]> self = ? | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   |
|---:|:---------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>number<> exponent = 2 | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int]<> repeats = [1, 1, 1, 1] | Unknown  |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[1, 32, 1]> self = ? | Unknown  |
### aten.silu.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 32, 11008]> self = ? | Unknown  |
### aten.sin.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  2 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  3 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  4 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 32 | Unknown  |
|  5 | Tensor<[1, 1, 32]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1         | Unknown  |
|  6 | Tensor<[1, 32, 32, 128]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = 64   | Unknown  |
|  7 | Tensor<[1, 32, 32, 128]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 64,<br>Optional[int]<> end = -1  | Unknown  |
|  8 | Tensor<[1, 32]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1            | Unknown  |
|  9 | Tensor<[1, 64]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1            | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[11008, 4096]> self = ? | Unknown  |
|  1 | Tensor<[32000, 4096]> self = ? | Unknown  |
|  2 | Tensor<[4096, 11008]> self = ? | Unknown  |
|  3 | Tensor<[4096, 4096]> self = ?  | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>int<> dim0 = -2,<br>int<> dim1 = -1 | Unknown  |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Unknown  |
|  2 | Tensor<[1, 64, 32]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2        | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048]> self = ?,<br>int<> dim = 3    | Unknown  |
|  1 | Tensor<[1, 2048, 2048]> self = ?,<br>int<> dim = 1 | Done     |
|  2 | Tensor<[1, 32, 128]> self = ?,<br>int<> dim = 1    | Unknown  |
|  3 | Tensor<[1, 32]> self = ?,<br>int<> dim = 1         | Unknown  |
|  4 | Tensor<[1, 64]> self = ?,<br>int<> dim = 2         | Unknown  |
|  5 | Tensor<[2048, 2048]> self = ?,<br>int<> dim = 0    | Done     |
|  6 | Tensor<[32]> self = ?,<br>int<> dim = 0            | Done     |
|  7 | Tensor<[64]> self = ?,<br>int<> dim = 0            | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int]<> size = [1, 1, 32]          | Unknown  |
|  1 | Tensor<[1, 32, 11008]> self = ?,<br>List[int]<> size = [32, 11008]     | Unknown  |
|  2 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int]<> size = [32, 128, 32] | Unknown  |
|  3 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int]<> size = [1, 32, 4096] | Unknown  |
|  4 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int]<> size = [32, 32, 128] | Unknown  |
|  5 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int]<> size = [32, 32, 32]   | Unknown  |
|  6 | Tensor<[1, 32, 4096]> self = ?,<br>List[int]<> size = [1, 32, 32, 128] | Unknown  |
|  7 | Tensor<[1, 32, 4096]> self = ?,<br>List[int]<> size = [32, 4096]       | Unknown  |
|  8 | Tensor<[1, 64, 1]> self = ?,<br>List[int]<> size = [1, 64, 1]          | Unknown  |
|  9 | Tensor<[1, 64, 32]> self = ?,<br>List[int]<> size = [1, 64, 32]        | Unknown  |
| 10 | Tensor<[32, 11008]> self = ?,<br>List[int]<> size = [1, 32, 11008]     | Unknown  |
| 11 | Tensor<[32, 32, 128]> self = ?,<br>List[int]<> size = [1, 32, 32, 128] | Unknown  |
| 12 | Tensor<[32, 32, 32]> self = ?,<br>List[int]<> size = [1, 32, 32, 32]   | Unknown  |
| 13 | Tensor<[32, 32000]> self = ?,<br>List[int]<> size = [1, 32, 32000]     | Unknown  |
| 14 | Tensor<[32, 4096]> self = ?,<br>List[int]<> size = [1, 32, 4096]       | Unknown  |

