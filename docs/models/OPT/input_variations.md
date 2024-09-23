# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |
|---:|:-------------------------------|-------------------:|------------:|
|  0 | aten._softmax.default          |                  3 |           1 |
|  1 | aten._to_copy.default          |                  6 |           2 |
|  2 | aten._unsafe_view.default      |                  1 |           1 |
|  3 | aten.add.Tensor                |                  9 |           4 |
|  4 | aten.addmm.default             |                  6 |           3 |
|  5 | aten.bmm.default               |                  6 |           2 |
|  6 | aten.cat.default               |                  4 |           0 |
|  7 | aten.clone.default             |                 10 |           5 |
|  8 | aten.cumsum.default            |                  3 |           1 |
|  9 | aten.embedding.default         |                  4 |           2 |
| 10 | aten.eq.Scalar                 |                  1 |           1 |
| 11 | aten.expand.default            |                  4 |           1 |
| 12 | aten.full.default              |                  1 |           1 |
| 13 | aten.gt.Scalar                 |                  1 |           1 |
| 14 | aten.lift_fresh_copy.default   |                  1 |           1 |
| 15 | aten.masked_fill.Scalar        |                  3 |           1 |
| 16 | aten.maximum.default           |                  3 |           1 |
| 17 | aten.mm.default                |                  6 |           3 |
| 18 | aten.mul.Tensor                |                  5 |           2 |
| 19 | aten.native_layer_norm.default |                  2 |           1 |
| 20 | aten.new_ones.default          |                  2 |           0 |
| 21 | aten.relu.default              |                  2 |           1 |
| 22 | aten.rsub.Scalar               |                  3 |           1 |
| 23 | aten.select.int                |                  1 |           1 |
| 24 | aten.slice.Tensor              |                 11 |           5 |
| 25 | aten.sub.Tensor                |                  3 |           1 |
| 26 | aten.sum.default               |                  1 |           1 |
| 27 | aten.sym_size.int              |                  2 |           0 |
| 28 | aten.t.default                 |                  6 |           6 |
| 29 | aten.transpose.int             |                  7 |           3 |
| 30 | aten.unsqueeze.default         |                  8 |           4 |
| 31 | aten.view.default              |                 31 |          13 |
***
### aten._softmax.default
|    | ATen Input Variations                                                                 | Status   |
|---:|:--------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 60]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False      | Unknown  |
|  1 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False | Unknown  |
|  2 | Tensor<[16, 59, 59]> self = ?,<br>int<> dim = -1,<br>bool<> half_to_float = False     | Done     |
### aten._to_copy.default
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Optional[int]<> dtype = torch.bool         | Unknown  |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>Optional[int]<> dtype = torch.float32      | Unknown  |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int]<> dtype = torch.bool    | Unknown  |
|  3 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int]<> dtype = torch.float32 | Unknown  |
|  4 | Tensor<[1, 1, 59, 59]> self = ?,<br>Optional[int]<> dtype = torch.bool        | Done     |
|  5 | Tensor<[1, 1, 59, 59]> self = ?,<br>Optional[int]<> dtype = torch.float32     | Done     |
### aten._unsafe_view.default
|    | ATen Input Variations                                                 | Status   |
|---:|:----------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 59, 16, 64]> self = ?,<br>List[int]<> size = [1, 59, 1024] | Done     |
### aten.add.Tensor
|    | ATen Input Variations                                                         | Status   |
|---:|:------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  |
|  1 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  |
|  2 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  |
|  3 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  |
|  4 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Done     |
|  5 | Tensor<[1, 1]> self = ?,<br>Tensor<> other = 2                                | Unknown  |
|  6 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Done     |
|  7 | Tensor<[1, 59]> self = ?,<br>Tensor<> other = 2                               | Done     |
|  8 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Done     |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?  | Unknown  |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[59, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?  | Unknown  |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  |
|  1 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  |
|  2 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  |
|  3 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  |
|  4 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Done     |
|  5 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Done     |
### aten.cat.default
|    | ATen Input Variations                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[Tensor]<> tensors = ['torch.Size([1, 16, 59, 64])', 'torch.Size([1, 16, 1, 64])'],<br>int<> dim = 2  | Unknown  |
|  1 | List[Tensor]<> tensors = ['torch.Size([1, 16, s10, 64])', 'torch.Size([1, 16, 1, 64])'],<br>int<> dim = 2 | Unknown  |
|  2 | List[Tensor]<> tensors = ['torch.Size([1, 59])', 'torch.Size([1, 1])'],<br>int<> dim = -1                 | Unknown  |
|  3 | List[Tensor]<> tensors = ['torch.Size([1, s48])', 'torch.Size([1, 1])'],<br>int<> dim = -1                | Unknown  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   |
|---:|:---------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1024]> self = ?                                                                | Unknown  |
|  1 | Tensor<[1, 1024]> self = ?                                                                   | Unknown  |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  3 | Tensor<[1, 59, 1024]> self = ?                                                               | Done     |
|  4 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int]<> memory_format = torch.contiguous_format | Done     |
|  5 | Tensor<[1, s10 + 1]> self = ?                                                                | Unknown  |
|  6 | Tensor<[16, 1, 60]> self = ?                                                                 | Unknown  |
|  7 | Tensor<[16, 1, s10 + 1]> self = ?                                                            | Unknown  |
|  8 | Tensor<[16, 59, 59]> self = ?                                                                | Done     |
|  9 | Tensor<[59, 1024]> self = ?                                                                  | Done     |
### aten.cumsum.default
|    | ATen Input Variations                           | Status   |
|---:|:------------------------------------------------|:---------|
|  0 | Tensor<[1, 59]> self = ?,<br>int<> dim = 1      | Done     |
|  1 | Tensor<[1, 60]> self = ?,<br>int<> dim = 1      | Unknown  |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>int<> dim = 1 | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                     | Status   |
|---:|:------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  |
|  1 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                           | Done     |
|  2 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int<> padding_idx = 1  | Unknown  |
|  3 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int<> padding_idx = 1 | Done     |
### aten.eq.Scalar
|    | ATen Input Variations                       | Status   |
|---:|:--------------------------------------------|:---------|
|  0 | Tensor<[1]> self = ?,<br>number<> other = 1 | Done     |
### aten.expand.default
|    | ATen Input Variations                                                                       | Status   |
|---:|:--------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 59]> self = ?,<br>List[int]<> size = [1, 1, 59, 59]                        | Done     |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>List[int]<> size = [1, 1, 1, 60]                         | Unknown  |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int]<> size = [1, 1, 1, 'torch.Size(s10 + 1)'] | Unknown  |
|  3 | Tensor<[1, 1, 59, 59]> self = ?,<br>List[int]<> size = [1, 1, 59, 59]                       | Unknown  |
### aten.full.default
|    | ATen Input Variations                                                                                                                                     | Status   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | List[int]<> size = [59, 59],<br>number<> fill_value = -3.4028234663852886e+38,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
### aten.gt.Scalar
|    | ATen Input Variations                      | Status   |
|---:|:-------------------------------------------|:---------|
|  0 | Tensor<[]> self = ?,<br>number<> other = 0 | Done     |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<> self = ?       | Done     |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                    | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> mask = ?,<br>number<> value = -3.4028234663852886e+38           | Unknown  |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> mask = ?,<br>number<> value = -3.4028234663852886e+38 | Unknown  |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> mask = ?,<br>number<> value = -3.4028234663852886e+38         | Done     |
### aten.maximum.default
|    | ATen Input Variations                                         | Status   |
|---:|:--------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[]> other = ?      | Unknown  |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  |
|  2 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[]> other = ?     | Done     |
### aten.mm.default
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?  | Unknown  |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?   | Unknown  |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?  | Unknown  |
|  3 | Tensor<[59, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Done     |
|  4 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?  | Done     |
|  5 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ? | Done     |
### aten.mul.Tensor
|    | ATen Input Variations                                            | Status   |
|---:|:-----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<> other = 0.125         | Unknown  |
|  1 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<> other = 0.125        | Done     |
|  2 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?           | Done     |
|  3 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?           | Unknown  |
|  4 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ? | Unknown  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                           | Status   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-05  | Unknown  |
|  1 | Tensor<[1, 59, 1024]> input = ?,<br>List[int]<> normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float<> eps = 1e-05 | Done     |
### aten.new_ones.default
|    | ATen Input Variations                                                                           | Status   |
|---:|:------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 59]> self = ?,<br>List[int]<> size = [1, 1],<br>Optional[bool]<> pin_memory = False  | Unknown  |
|  1 | Tensor<[1, s48]> self = ?,<br>List[int]<> size = [1, 1],<br>Optional[bool]<> pin_memory = False | Unknown  |
### aten.relu.default
|    | ATen Input Variations       | Status   |
|---:|:----------------------------|:---------|
|  0 | Tensor<[1, 4096]> self = ?  | Unknown  |
|  1 | Tensor<[59, 4096]> self = ? | Done     |
### aten.rsub.Scalar
|    | ATen Input Variations                                        | Status   |
|---:|:-------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>number<> other = 1.0      | Unknown  |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number<> other = 1.0 | Unknown  |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>number<> other = 1.0     | Done     |
### aten.select.int
|    | ATen Input Variations                                           | Status   |
|---:|:----------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 59]> self = ?,<br>int<> dim = 1,<br>int<> index = -1 | Done     |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1, 59]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Done     |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1      | Unknown  |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Unknown  |
|  3 | Tensor<[1, 1, 59, 59]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1     | Done     |
|  4 | Tensor<[1, 1, 59, 59]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1     | Done     |
|  5 | Tensor<[1, 59]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1            | Done     |
|  6 | Tensor<[1, 59]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1            | Done     |
|  7 | Tensor<[1, 60]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1            | Unknown  |
|  8 | Tensor<[1, 60]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 59,<br>Optional[int]<> end = -1           | Unknown  |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int<> dim = 0,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1       | Unknown  |
| 10 | Tensor<[1, s10 + 1]> self = ?,<br>int<> dim = 1,<br>Optional[int]<s10> start = ?,<br>Optional[int]<> end = -1    | Unknown  |
### aten.sub.Tensor
|    | ATen Input Variations                                | Status   |
|---:|:-----------------------------------------------------|:---------|
|  0 | Tensor<[1, 59]> self = ?,<br>Tensor<> other = 1      | Done     |
|  1 | Tensor<[1, 60]> self = ?,<br>Tensor<> other = 1      | Unknown  |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<> other = 1 | Unknown  |
### aten.sum.default
|    | ATen Input Variations   | Status   |
|---:|:------------------------|:---------|
|  0 | Tensor<[1]> self = ?    | Done     |
### aten.sym_size.int
|    | ATen Input Variations                                   | Status   |
|---:|:--------------------------------------------------------|:---------|
|  0 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int<> dim = 2 | Unknown  |
|  1 | Tensor<[1, s10 + 1]> self = ?,<br>int<> dim = 1         | Unknown  |
### aten.t.default
|    | ATen Input Variations         | Status   |
|---:|:------------------------------|:---------|
|  0 | Tensor<[1024, 1024]> self = ? | Done     |
|  1 | Tensor<[1024, 4096]> self = ? | Done     |
|  2 | Tensor<[1024, 512]> self = ?  | Done     |
|  3 | Tensor<[4096, 1024]> self = ? | Done     |
|  4 | Tensor<[50272, 512]> self = ? | Done     |
|  5 | Tensor<[512, 1024]> self = ?  | Done     |
### aten.transpose.int
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 16, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Unknown  |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2    | Unknown  |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  3 | Tensor<[1, 59, 16, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2   | Done     |
|  4 | Tensor<[16, 59, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2      | Done     |
|  5 | Tensor<[16, 60, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2      | Unknown  |
|  6 | Tensor<[16, s10 + 1, 64]> self = ?,<br>int<> dim0 = 1,<br>int<> dim1 = 2 | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 59]> self = ?,<br>int<> dim = 2      | Done     |
|  1 | Tensor<[1, 1, 60]> self = ?,<br>int<> dim = 2      | Unknown  |
|  2 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int<> dim = 2 | Unknown  |
|  3 | Tensor<[1, 59, 59]> self = ?,<br>int<> dim = 1     | Done     |
|  4 | Tensor<[1, 59]> self = ?,<br>int<> dim = 1         | Done     |
|  5 | Tensor<[1, 60]> self = ?,<br>int<> dim = 1         | Unknown  |
|  6 | Tensor<[1, s10 + 1]> self = ?,<br>int<> dim = 1    | Unknown  |
|  7 | Tensor<[59, 59]> self = ?,<br>int<> dim = 0        | Done     |
### aten.view.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int]<> size = [-1, 1024]                            | Unknown  |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int]<> size = [1, -1, 16, 64]                       | Unknown  |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>List[int]<> size = [1, 1, 16, 64]                        | Unknown  |
|  3 | Tensor<[1, 1, 1024]> self = ?,<br>List[int]<> size = [1, 1024]                             | Unknown  |
|  4 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int]<> size = [1, 1, 1024]                        | Unknown  |
|  5 | Tensor<[1, 1, 512]> self = ?,<br>List[int]<> size = [1, 512]                               | Unknown  |
|  6 | Tensor<[1, 1024]> self = ?,<br>List[int]<> size = [1, 1, 1024]                             | Unknown  |
|  7 | Tensor<[1, 16, 1, 60]> self = ?,<br>List[int]<> size = [16, 1, 60]                         | Unknown  |
|  8 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int]<> size = [16, -1, 64]                        | Unknown  |
|  9 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int]<> size = [16, 1, 'torch.Size(s10 + 1)'] | Unknown  |
| 10 | Tensor<[1, 16, 59, 59]> self = ?,<br>List[int]<> size = [16, 59, 59]                       | Done     |
| 11 | Tensor<[1, 16, 59, 64]> self = ?,<br>List[int]<> size = [16, -1, 64]                       | Done     |
| 12 | Tensor<[1, 16, 60, 64]> self = ?,<br>List[int]<> size = [16, -1, 64]                       | Unknown  |
| 13 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int]<> size = [16, -1, 64]                  | Unknown  |
| 14 | Tensor<[1, 1]> self = ?,<br>List[int]<> size = [-1, 1]                                     | Unknown  |
| 15 | Tensor<[1, 50272]> self = ?,<br>List[int]<> size = [1, 1, 50272]                           | Unknown  |
| 16 | Tensor<[1, 512]> self = ?,<br>List[int]<> size = [1, 1, 512]                               | Unknown  |
| 17 | Tensor<[1, 59, 1024]> self = ?,<br>List[int]<> size = [-1, 1024]                           | Done     |
| 18 | Tensor<[1, 59, 1024]> self = ?,<br>List[int]<> size = [1, -1, 16, 64]                      | Done     |
| 19 | Tensor<[1, 59, 1024]> self = ?,<br>List[int]<> size = [1, 59, 16, 64]                      | Done     |
| 20 | Tensor<[1, 59, 1024]> self = ?,<br>List[int]<> size = [59, 1024]                           | Done     |
| 21 | Tensor<[1, 59, 512]> self = ?,<br>List[int]<> size = [59, 512]                             | Done     |
| 22 | Tensor<[1, 59]> self = ?,<br>List[int]<> size = [-1, 59]                                   | Done     |
| 23 | Tensor<[16, 1, 60]> self = ?,<br>List[int]<> size = [1, 16, 1, 60]                         | Unknown  |
| 24 | Tensor<[16, 1, 64]> self = ?,<br>List[int]<> size = [1, 16, 1, 64]                         | Unknown  |
| 25 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int]<> size = [1, 16, 1, 'torch.Size(s10 + 1)'] | Unknown  |
| 26 | Tensor<[16, 59, 59]> self = ?,<br>List[int]<> size = [1, 16, 59, 59]                       | Done     |
| 27 | Tensor<[16, 59, 64]> self = ?,<br>List[int]<> size = [1, 16, 59, 64]                       | Done     |
| 28 | Tensor<[59, 1024]> self = ?,<br>List[int]<> size = [1, 59, 1024]                           | Done     |
| 29 | Tensor<[59, 50272]> self = ?,<br>List[int]<> size = [1, 59, 50272]                         | Done     |
| 30 | Tensor<[59, 512]> self = ?,<br>List[int]<> size = [1, 59, 512]                             | Done     |

