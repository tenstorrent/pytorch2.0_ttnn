# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  1 | aten._unsafe_view.default      |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.add.Tensor                |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  3 | aten.all.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.arange.start              |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default               |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  6 | aten.cat.default               |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default             |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.embedding.default         |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.eq.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.expand.default            |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.gelu.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.index.Tensor              |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.lift_fresh_copy.default   |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.logical_not.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.masked_fill.Scalar        |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.mm.default                |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 17 | aten.mul.Scalar                |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.mul.Tensor                |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.native_layer_norm.default |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 20 | aten.neg.default               |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.ones.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.permute.default           |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 23 | aten.slice.Tensor              |                  8 |           2 |         0 |          0 | 🚧          |    0.25 |
| 24 | aten.t.default                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.transpose.int             |                  3 |           2 |         0 |          0 | 🚧          |    0.67 |
| 26 | aten.tril.default              |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 27 | aten.unsqueeze.default         |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 28 | aten.view.default              |                 14 |           5 |         0 |          0 | 🚧          |    0.36 |
| 29 | aten.zeros_like.default        |                  1 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 71, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_view.default
|    | ATen Input Variations                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 7, 71, 64]> self = ?,<br>List[int] size = [1, 7, 4544] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 7, 4544]> self = ?,<br>Tensor<[1, 7, 4544]> other = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 71, 7, 7]> self = ?,<br>Tensor<[7, 7]> other = ?          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.all.default
|    | ATen Input Variations   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 7]> self = ? | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.arange.start
|    | ATen Input Variations                                                                                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number start = 0,<br>number end = 7,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[71, 7, 7]> self = ?,<br>Tensor<[71, 7, 64]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 1, 7, 32]>, <[1, 1, 7, 32]>],<br>int dim = -1   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[Tensor] tensors = [<[1, 71, 7, 32]>, <[1, 71, 7, 32]>],<br>int dim = -1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 7, 4544]> self = ?                                                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 7, 71, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ? | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.eq.Scalar
|    | ATen Input Variations                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 64, 7]> self = ?,<br>List[int] size = [1, 71, 64, 7]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.gelu.default
|    | ATen Input Variations          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 7, 18176]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.index.Tensor
|    | ATen Input Variations                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 7, 73, 64]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[1]>] | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 7]>]                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor self = ?         | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.logical_not.default
|    | ATen Input Variations   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> mask = ?,<br>number value = -inf | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[7, 18176]> self = ?,<br>Tensor<[18176, 4544]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 18176]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4544]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 4672]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[7, 4544]> self = ?,<br>Tensor<[4544, 65024]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Scalar
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 64, 7]> self = ?,<br>number other = 0.3535533905932738  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>number other = 0.3535533905932738 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 7, 4544]> input = ?,<br>List[int] normalized_shape = [4544],<br>Optional[Tensor]<[4544]> weight = ?,<br>Optional[Tensor]<[4544]> bias = ?,<br>float eps = 1e-05 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.neg.default
|    | ATen Input Variations           | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 7, 32]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 71, 7, 32]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.ones.default
|    | ATen Input Variations                                                                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[int] size = [7, 7],<br>Optional[int] dtype = torch.bool,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[18176, 4544]> self = ?,<br>List[int] dims = [1, 0]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[4544, 18176]> self = ?,<br>List[int] dims = [1, 0]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[4544, 4544]> self = ?,<br>List[int] dims = [1, 0]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[4672, 4544]> self = ?,<br>List[int] dims = [1, 0]         | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -2                   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 7, 73, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 32                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 71, 7, 64]> self = ?,<br>int dim = 3,<br>Optional[int] start = 32,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[65024, 4544]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 7, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.tril.default
|    | ATen Input Variations   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[7, 7]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[7]> self = ?,<br>int dim = 0        | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 7, 64]> self = ?,<br>List[int] size = [1, 1, 7, 64]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 7, 18176]> self = ?,<br>List[int] size = [7, 18176]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 7, 4544]> self = ?,<br>List[int] size = [7, 4544]        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 7, 4672]> self = ?,<br>List[int] size = [1, 7, 73, 64]   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 71, 64, 7]> self = ?,<br>List[int] size = [71, 64, 7]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64] | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] size = [71, 7, 64]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 71, 7, 7]> self = ?,<br>List[int] size = [71, 7, 7]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[7, 18176]> self = ?,<br>List[int] size = [1, 7, 18176]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[7, 4544]> self = ?,<br>List[int] size = [1, 7, 4544]        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[7, 4672]> self = ?,<br>List[int] size = [1, 7, 4672]        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[7, 65024]> self = ?,<br>List[int] size = [1, 7, 65024]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[71, 7, 64]> self = ?,<br>List[int] size = [1, 71, 7, 64]    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[71, 7, 7]> self = ?,<br>List[int] size = [1, 71, 7, 7]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.zeros_like.default
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | N/A                 | N/A          | N/A               | N/A                |

