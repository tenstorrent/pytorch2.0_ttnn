# High Level Operations Status
|    | Operations               |   Input Variations |
|---:|:-------------------------|-------------------:|
|  0 | aten._softmax.default    |                  1 |
|  1 | aten._to_copy.default    |                  2 |
|  2 | aten.add.Tensor          |                  2 |
|  3 | aten.all.dim             |                  1 |
|  4 | aten.any.default         |                  1 |
|  5 | aten.arange.start        |                  1 |
|  6 | aten.bitwise_not.default |                  1 |
|  7 | aten.bmm.default         |                  1 |
|  8 | aten.cat.default         |                  1 |
|  9 | aten.clone.default       |                  1 |
| 10 | aten.cos.default         |                  1 |
| 11 | aten.embedding.default   |                  1 |
| 12 | aten.eq.Tensor           |                  1 |
| 13 | aten.expand.default      |                  5 |
| 14 | aten.index.Tensor        |                  1 |
| 15 | aten.mean.dim            |                  1 |
| 16 | aten.min.default         |                  1 |
| 17 | aten.mm.default          |                  1 |
| 18 | aten.mul.Scalar          |                  1 |
| 19 | aten.mul.Tensor          |                  2 |
| 20 | aten.ne.Scalar           |                  1 |
| 21 | aten.neg.default         |                  1 |
| 22 | aten.pow.Tensor_Scalar   |                  1 |
| 23 | aten.repeat.default      |                  1 |
| 24 | aten.rsqrt.default       |                  1 |
| 25 | aten.silu.default        |                  1 |
| 26 | aten.sin.default         |                  1 |
| 27 | aten.slice.Tensor        |                  4 |
| 28 | aten.t.default           |                  1 |
| 29 | aten.transpose.int       |                  1 |
| 30 | aten.unsqueeze.default   |                  4 |
| 31 | aten.view.default        |                 13 |
***
### aten._softmax.default
|    | ATen Input Variations                                                            | Status   |
|---:|:---------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 32]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                        | Status   |
|---:|:-----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[int] dtype = torch.float32       | Unknown  |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 1]> self = ?,<br>Tensor other = 1e-06                     | Unknown  |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 32, 32, 128]> other = ? | Unknown  |
### aten.all.dim
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = -1 | Unknown  |
### aten.any.default
|    | ATen Input Variations    | Status   |
|---:|:-------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ? | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bitwise_not.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 1]> self = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                       | Status   |
|---:|:------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [transpose_3, transpose_3],<br>int dim = -1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.cos.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1, 32, 128]> self = ? | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0 | Unknown  |
### aten.eq.Tensor
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                   | Status   |
|---:|:------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [1, 32, 128, 32] | Unknown  |
|  1 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]             | Unknown  |
|  2 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1]             | Unknown  |
|  3 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128] | Unknown  |
|  4 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]   | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                                         | Status   |
|---:|:----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, arg324_1] | Unknown  |
### aten.mean.dim
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  |
### aten.min.default
|    | ATen Input Variations               | Status   |
|---:|:------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ? | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[32, 4096]> self = ?,<br>Tensor<[4096, 4096]> mat2 = ? | Unknown  |
### aten.mul.Scalar
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>number other = 0.29730177875068026 | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[1, 1, 2048, 1]> other = ?      | Unknown  |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  |
### aten.ne.Scalar
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1, 32]> self = ?,<br>number other = 1 | Unknown  |
### aten.neg.default
|    | ATen Input Variations            | Status   |
|---:|:---------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 64]> self = ? | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 4096]> self = ?,<br>number exponent = 2 | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Unknown  |
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
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1            | Unknown  |
|  2 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1            | Unknown  |
|  3 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 64   | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[4096, 4096]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 32, 32, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 64]> self = ?,<br>int dim = 2         | Unknown  |
|  1 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1 | Unknown  |
|  2 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 3    | Unknown  |
|  3 | Tensor<[32]> self = ?,<br>int dim = 0            | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]          | Unknown  |
|  1 | Tensor<[1, 32, 32, 128]> self = ?,<br>List[int] size = [32, 32, 128] | Unknown  |
|  2 | Tensor<[1, 32, 128, 32]> self = ?,<br>List[int] size = [32, 128, 32] | Unknown  |
|  3 | Tensor<[32, 32000]> self = ?,<br>List[int] size = [1, 32, 32000]     | Unknown  |
|  4 | Tensor<[32, 4096]> self = ?,<br>List[int] size = [1, 32, 4096]       | Unknown  |
|  5 | Tensor<[1, 32, 32, 32]> self = ?,<br>List[int] size = [32, 32, 32]   | Unknown  |
|  6 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]          | Unknown  |
|  7 | Tensor<[32, 32, 32]> self = ?,<br>List[int] size = [1, 32, 32, 32]   | Unknown  |
|  8 | Tensor<[32, 32, 128]> self = ?,<br>List[int] size = [1, 32, 32, 128] | Unknown  |
|  9 | Tensor<[1, 32, 11008]> self = ?,<br>List[int] size = [32, 11008]     | Unknown  |
| 10 | Tensor<[1, 32, 4096]> self = ?,<br>List[int] size = [32, 4096]       | Unknown  |
| 11 | Tensor<[32, 11008]> self = ?,<br>List[int] size = [1, 32, 11008]     | Unknown  |
| 12 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32]        | Unknown  |

