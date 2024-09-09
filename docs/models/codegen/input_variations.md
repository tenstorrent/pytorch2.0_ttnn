# High Level Operations Status
|    | Operations                     |   Input Variations |
|---:|:-------------------------------|-------------------:|
|  0 | aten._softmax.default          |                  1 |
|  1 | aten._to_copy.default          |                  1 |
|  2 | aten._unsafe_view.default      |                  2 |
|  3 | aten.add.Tensor                |                  2 |
|  4 | aten.addmm.default             |                  1 |
|  5 | aten.bmm.default               |                  1 |
|  6 | aten.cat.default               |                  1 |
|  7 | aten.clone.default             |                  2 |
|  8 | aten.cumsum.default            |                  1 |
|  9 | aten.div.Tensor                |                  1 |
| 10 | aten.embedding.default         |                  1 |
| 11 | aten.eq.Scalar                 |                  1 |
| 12 | aten.expand.default            |                 12 |
| 13 | aten.gt.Scalar                 |                  1 |
| 14 | aten.index.Tensor              |                  1 |
| 15 | aten.lift_fresh_copy.default   |                  1 |
| 16 | aten.mm.default                |                  1 |
| 17 | aten.mul.Tensor                |                  4 |
| 18 | aten.native_layer_norm.default |                  1 |
| 19 | aten.neg.default               |                  1 |
| 20 | aten.new_ones.default          |                  1 |
| 21 | aten.permute.default           |                  1 |
| 22 | aten.pow.Tensor_Scalar         |                  1 |
| 23 | aten.rsub.Scalar               |                  1 |
| 24 | aten.select.int                |                  1 |
| 25 | aten.slice.Tensor              |                 15 |
| 26 | aten.split.Tensor              |                  2 |
| 27 | aten.stack.default             |                  1 |
| 28 | aten.sub.Tensor                |                  1 |
| 29 | aten.sum.default               |                  1 |
| 30 | aten.sym_size.int              |                  2 |
| 31 | aten.t.default                 |                  1 |
| 32 | aten.tanh.default              |                  1 |
| 33 | aten.transpose.int             |                  1 |
| 34 | aten.unsqueeze.default         |                  3 |
| 35 | aten.view.default              |                 38 |
| 36 | aten.where.self                |                  1 |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   |
|---:|:-------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 5, 5]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  |
### aten._to_copy.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 5]> self = ?,<br>Optional[int] dtype = torch.float32 | Unknown  |
### aten._unsafe_view.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 4, 4, 64]> self = ?,<br>List[int] size = [1, 1, 16, 64] | Unknown  |
|  1 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>List[int] size = [1, 5, 16, 64] | Unknown  |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   |
|---:|:---------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ? | Unknown  |
|  1 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                 | Unknown  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[4096]> self = ?,<br>Tensor<[5, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Unknown  |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ? | Unknown  |
### aten.cat.default
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [add, slice_10],<br>int dim = -1 | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5, 1024]> self = ?                                                               | Unknown  |
|  1 | Tensor<[1, 5, 4, 4, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  |
### aten.cumsum.default
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[1, 5]> self = ?,<br>int dim = -1 | Unknown  |
### aten.div.Tensor
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ? | Unknown  |
### aten.eq.Scalar
|    | ATen Input Variations                         | Status   |
|---:|:----------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>number other = 50256 | Unknown  |
### aten.expand.default
|    | ATen Input Variations                                                                  | Status   |
|---:|:---------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 16, 1]> self = ?,<br>List[int] size = [1, 1, 1, 16, 2]                | Unknown  |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]                    | Unknown  |
|  2 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                      | Unknown  |
|  3 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int_1]   | Unknown  |
|  4 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                      | Unknown  |
|  5 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]                    | Unknown  |
|  6 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [1, 16, 6, 64]                    | Unknown  |
|  7 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [1, 16, 64, 5]                    | Unknown  |
|  8 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [1, 16, 64, 6]                    | Unknown  |
|  9 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 64, sym_size_int]   | Unknown  |
| 10 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [1, 16, sym_size_int_2, 64] | Unknown  |
| 11 | Tensor<[1, 5, 1, 16, 1]> self = ?,<br>List[int] size = [1, 5, 1, 16, 2]                | Unknown  |
### aten.gt.Scalar
|    | ATen Input Variations                    | Status   |
|---:|:-----------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>number other = 0 | Unknown  |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   |
|---:|:----------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2048, 32]> self = ?,<br>List[Optional[Tensor]] indices = [arg226_1] | Unknown  |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor self = ?         | Unknown  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ? | Unknown  |
### aten.mul.Tensor
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.4028234663852886e+38 | Unknown  |
|  1 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                | Unknown  |
|  2 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?      | Unknown  |
|  3 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                     | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  |
### aten.neg.default
|    | ATen Input Variations           | Status   |
|---:|:--------------------------------|:---------|
|  0 | Tensor<[1, 5, 16, 16]> self = ? | Unknown  |
### aten.new_ones.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  |
### aten.permute.default
|    | ATen Input Variations                                             | Status   |
|---:|:------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5, 4096]> self = ?,<br>number exponent = 3.0 | Unknown  |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0 | Unknown  |
### aten.select.int
|    | ATen Input Variations                                      | Status   |
|---:|:-----------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                   | Status   |
|---:|:------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 6                  | Unknown  |
|  1 | Tensor<[1, 1, 1, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s10 + 1> end = ?         | Unknown  |
|  2 | Tensor<[1, 1, 1, 5]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1                    | Unknown  |
|  3 | Tensor<[1, 1, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 1,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
|  4 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                  | Unknown  |
|  5 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 5               | Unknown  |
|  6 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int]<s10> start = ?,<br>Optional[int]<s10 + 1> end = ? | Unknown  |
|  7 | Tensor<[1, 1, 5, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 5                  | Unknown  |
|  8 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
|  9 | Tensor<[1, 5, 16, 32]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = -1,<br>int step = 2 | Unknown  |
| 10 | Tensor<[1, 5, 16, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1                  | Unknown  |
| 11 | Tensor<[1, 5]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = -1                          | Unknown  |
| 12 | Tensor<[1, 6]> self = ?,<br>int dim = 1,<br>Optional[int] start = 5,<br>Optional[int] end = -1                          | Unknown  |
| 13 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>Optional[int] start = -1,<br>Optional[int] end = -1                        | Unknown  |
| 14 | Tensor<[1, s1 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s1> start = ?,<br>Optional[int] end = -1                 | Unknown  |
### aten.split.Tensor
|    | ATen Input Variations                                                     | Status   |
|---:|:--------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1      | Unknown  |
|  1 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1 | Unknown  |
### aten.stack.default
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | List[Tensor] tensors = [neg, slice_28],<br>int dim = -1 | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                        | Status   |
|---:|:---------------------------------------------|:---------|
|  0 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1 | Unknown  |
### aten.sum.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1]> self = ?    | Unknown  |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   |
|---:|:------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3   | Unknown  |
|  1 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[3072, 1024]> self = ? | Unknown  |
### aten.tanh.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1, 5, 4096]> self = ? | Unknown  |
### aten.transpose.int
|    | ATen Input Variations                                               | Status   |
|---:|:--------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 5, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   |
|---:|:-----------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 5]> self = ?,<br>int dim = 2     | Unknown  |
|  1 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 4 | Unknown  |
|  2 | Tensor<[1, 5]> self = ?,<br>int dim = 1        | Unknown  |
### aten.view.default
|    | ATen Input Variations                                                               | Status   |
|---:|:------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 16, 2]> self = ?,<br>List[int] size = [1, 1, 1, 32]                | Unknown  |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                        | Unknown  |
|  2 | Tensor<[1, 1, 16, 16, 2]> self = ?,<br>List[int] size = [1, 1, 16, 32]              | Unknown  |
|  3 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]                   | Unknown  |
|  4 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 1, 4, -1]                    | Unknown  |
|  5 | Tensor<[1, 1, 4, 256]> self = ?,<br>List[int] size = [1, 1, 4, 4, 64]               | Unknown  |
|  6 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                        | Unknown  |
|  7 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]                    | Unknown  |
|  8 | Tensor<[1, 16, 1, 6]> self = ?,<br>List[int] size = [16, 1, 6]                      | Unknown  |
|  9 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, sym_size_int_1]   | Unknown  |
| 10 | Tensor<[1, 16, 5, 5]> self = ?,<br>List[int] size = [16, 5, 5]                      | Unknown  |
| 11 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] size = [16, 5, 64]                    | Unknown  |
| 12 | Tensor<[1, 16, 6, 64]> self = ?,<br>List[int] size = [16, 6, 64]                    | Unknown  |
| 13 | Tensor<[1, 16, 64, 5]> self = ?,<br>List[int] size = [16, 64, 5]                    | Unknown  |
| 14 | Tensor<[1, 16, 64, 6]> self = ?,<br>List[int] size = [16, 64, 6]                    | Unknown  |
| 15 | Tensor<[1, 16, 64, s10 + 1]> self = ?,<br>List[int] size = [16, 64, sym_size_int]   | Unknown  |
| 16 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, sym_size_int_2, 64] | Unknown  |
| 17 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                                | Unknown  |
| 18 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                        | Unknown  |
| 19 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                        | Unknown  |
| 20 | Tensor<[1, 5, 1, 16, 2]> self = ?,<br>List[int] size = [1, 5, 1, 32]                | Unknown  |
| 21 | Tensor<[1, 5, 1024]> self = ?,<br>List[int] size = [5, 1024]                        | Unknown  |
| 22 | Tensor<[1, 5, 16, 16, 2]> self = ?,<br>List[int] size = [1, 5, 16, 32]              | Unknown  |
| 23 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] size = [1, 5, 1024]                   | Unknown  |
| 24 | Tensor<[1, 5, 3072]> self = ?,<br>List[int] size = [1, 5, 4, -1]                    | Unknown  |
| 25 | Tensor<[1, 5, 4, 256]> self = ?,<br>List[int] size = [1, 5, 4, 4, 64]               | Unknown  |
| 26 | Tensor<[1, 5, 4096]> self = ?,<br>List[int] size = [5, 4096]                        | Unknown  |
| 27 | Tensor<[1, 51200]> self = ?,<br>List[int] size = [1, 1, 51200]                      | Unknown  |
| 28 | Tensor<[1, 5]> self = ?,<br>List[int] size = [-1, 5]                                | Unknown  |
| 29 | Tensor<[1, 6]> self = ?,<br>List[int] size = [1, -1]                                | Unknown  |
| 30 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]                    | Unknown  |
| 31 | Tensor<[16, 1, 6]> self = ?,<br>List[int] size = [1, 16, 1, 6]                      | Unknown  |
| 32 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, sym_size_int]     | Unknown  |
| 33 | Tensor<[16, 5, 5]> self = ?,<br>List[int] size = [1, 16, 5, 5]                      | Unknown  |
| 34 | Tensor<[16, 5, 64]> self = ?,<br>List[int] size = [1, 16, 5, 64]                    | Unknown  |
| 35 | Tensor<[5, 3072]> self = ?,<br>List[int] size = [1, 5, 3072]                        | Unknown  |
| 36 | Tensor<[5, 4096]> self = ?,<br>List[int] size = [1, 5, 4096]                        | Unknown  |
| 37 | Tensor<[5, 51200]> self = ?,<br>List[int] size = [1, 5, 51200]                      | Unknown  |
### aten.where.self
|    | ATen Input Variations                                                                          | Status   |
|---:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 5, 5]> condition = ?,<br>Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ? | Unknown  |

