# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._unsafe_view.default      |                  1 |
|  2 | aten.add.Tensor                |                  1 |
|  3 | aten.all.default               |                  1 |
|  4 | aten.arange.start              |                  1 |
|  5 | aten.bmm.default               |                  1 |
|  6 | aten.cat.default               |                  1 |
|  7 | aten.clone.default             |                  2 |
|  8 | aten.embedding.default         |                  1 |
|  9 | aten.eq.Scalar                 |                  1 |
| 10 | aten.expand.default            |                  3 |
| 11 | aten.gelu.default              |                  1 |
| 12 | aten.index.Tensor              |                  2 |
| 13 | aten.lift_fresh_copy.default   |                  1 |
| 14 | aten.logical_not.default       |                  1 |
| 15 | aten.masked_fill.Scalar        |                  1 |
| 16 | aten.mm.default                |                  1 |
| 17 | aten.mul.Scalar                |                  1 |
| 18 | aten.mul.Tensor                |                  1 |
| 19 | aten.native_layer_norm.default |                  1 |
| 20 | aten.neg.default               |                  1 |
| 21 | aten.ones.default              |                  1 |
| 22 | aten.permute.default           |                  2 |
| 23 | aten.slice.Tensor              |                  5 |
| 24 | aten.t.default                 |                  1 |
| 25 | aten.transpose.int             |                  2 |
| 26 | aten.tril.default              |                  1 |
| 27 | aten.unsqueeze.default         |                  2 |
| 28 | aten.view.default              |                 12 |
| 29 | aten.zeros_like.default        |                  1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 71, 64]> self = ?,<br>List[int] size = [1, 7, 4544] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ? | Unknown  |
### aten.all.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1, 7]> self = ? | Unknown  |
### aten.arange.start
|    | ATen Input Variations                                                                                                                             | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 7,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                  | Status   |
|---:|:-------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [neg, slice_1],<br>int dim = -1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 4544]> self = ?                                                             | Unknown  |
|  1 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ? | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 1 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 64, 7]> self = ?,<br>List[int] size = [1, 71, 64, 7]  | Unknown  |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64] | Unknown  |
|  2 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]   | Unknown  |
### aten.gelu.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[1, 7, 18176]> self = ? | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                                              | Status   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, lift_fresh_copy] | Unknown  |
|  1 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [primals_2]                          | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.logical_not.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = -inf | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4672]> mat2 = ? | Unknown  |
### aten.mul.Scalar
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>number other = 0.3535533905932738 | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 4544]> input = ?,<br>List[int] normalized_shape = [4544],<br>Optional[Tensor]<[4544]> weight = ?,<br>Optional[Tensor]<[4544]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.neg.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 32]> self = ? | Unknown  |
### aten.ones.default
|    | ATen Input Variations                                                                                                                   | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int] size = [7, 7],<br>Optional[int] dtype = torch.bool,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
|  1 | Tensor<[4672, 4544]> self = ?,<br>List[int] dims = [1, 0]         | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                  | Status   |
|---:|:-------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  2 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2 | Unknown  |
|  3 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32 | Unknown  |
|  4 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7      | Unknown  |
### aten.t.default
|    | ATen Input Variations          | Status   |
|---:|:-------------------------------|:---------|
|  0 | Tensor<[65024, 4544]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   |
|---:|:-------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Unknown  |
|  1 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Unknown  |
### aten.tril.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1 | Unknown  |
|  1 | Tensor<[7]> self = ?,<br>int dim = 0        | Unknown  |
### aten.view.default
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]   | Unknown  |
|  1 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]      | Unknown  |
|  2 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]        | Unknown  |
|  3 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]   | Unknown  |
|  4 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]    | Unknown  |
|  5 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64] | Unknown  |
|  6 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]      | Unknown  |
|  7 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]      | Unknown  |
|  8 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]        | Unknown  |
|  9 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]        | Unknown  |
| 10 | Tensor<[7, 65024]> self = ?,<br>List[int] size = [1, 7, 65024]      | Unknown  |
| 11 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]      | Unknown  |
### aten.zeros_like.default
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  |

