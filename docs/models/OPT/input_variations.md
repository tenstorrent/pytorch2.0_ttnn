# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
|  1 | aten._to_copy.default          |                  7 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._unsafe_view.default      |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor                |                  9 |           4 |         0 |          0 | 🚧          |    0.44 |
|  4 | aten.addmm.default             |                  6 |           3 |         0 |          0 | 🚧          |    0.5  |
|  5 | aten.bmm.default               |                  6 |           2 |         0 |          0 | 🚧          |    0.33 |
|  6 | aten.cat.default               |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default             |                 10 |           5 |         0 |          0 | 🚧          |    0.5  |
|  8 | aten.cumsum.default            |                  3 |           0 |         0 |          0 | ✘           |    0    |
|  9 | aten.embedding.default         |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.eq.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.expand.default            |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 12 | aten.full.default              |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.gt.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.lift_fresh_copy.default   |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.masked_fill.Scalar        |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
| 16 | aten.maximum.default           |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
| 17 | aten.mm.default                |                  6 |           3 |         0 |          0 | 🚧          |    0.5  |
| 18 | aten.mul.Tensor                |                  5 |           2 |         0 |          0 | 🚧          |    0.4  |
| 19 | aten.native_layer_norm.default |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 20 | aten.new_ones.default          |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.relu.default              |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 22 | aten.rsub.Scalar               |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.select.int                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.slice.Tensor              |                 11 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.sub.Tensor                |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
| 26 | aten.sum.default               |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 27 | aten.sym_size.int              |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.t.default                 |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 29 | aten.transpose.int             |                  7 |           3 |         0 |          0 | 🚧          |    0.43 |
| 30 | aten.unsqueeze.default         |                  8 |           4 |         0 |          0 | 🚧          |    0.5  |
| 31 | aten.view.default              |                 31 |          13 |         0 |          0 | 🚧          |    0.42 |
***
### aten._softmax.default
|    | ATen Input Variations                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 1, 60]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[16, 59, 59]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten._to_copy.default
|    | ATen Input Variations                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>Optional[int] dtype = torch.bool          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bool     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 59, 59]> self = ?,<br>Optional[int] dtype = torch.bfloat16     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 59, 59]> self = ?,<br>Optional[int] dtype = torch.bool         | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[59, 59]> self = ?,<br>Optional[int] dtype = torch.bfloat16           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 59, 16, 64]> self = ?,<br>List[int] size = [1, 59, 1024] | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[59, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 16, 59, 64]>, <[1, 16, 1, 64]>],<br>int dim = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[Tensor] tensors = [<[1, 16, s10, 64]>, <[1, 16, 1, 64]>],<br>int dim = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | List[Tensor] tensors = [<[1, 59]>, <[1, 1]>],<br>int dim = -1                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | List[Tensor] tensors = [<[1, s48]>, <[1, 1]>],<br>int dim = -1                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1024]> self = ?                                                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 59, 1024]> self = ?                                                             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, s10 + 1]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[16, 1, 60]> self = ?                                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[16, 1, s10 + 1]> self = ?                                                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[16, 59, 59]> self = ?                                                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[59, 1024]> self = ?                                                                | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.cumsum.default
|    | ATen Input Variations                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 59]> self = ?,<br>int dim = 1      | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 60]> self = ?,<br>int dim = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                         | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.eq.Scalar
|    | ATen Input Variations                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1]> self = ?,<br>number other = 1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>List[int] size = [1, 1, 1, 60]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, <s10 + 1>] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 59, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[int] size = [59, 59],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.gt.Scalar
|    | ATen Input Variations                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[]> self = ?,<br>number other = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.lift_fresh_copy.default
|    | ATen Input Variations   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor self = ?         | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> mask = ?,<br>number value = -3.3895313892515355e+38         | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.maximum.default
|    | ATen Input Variations                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[]> other = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[59, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 59, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.new_ones.default
|    | ATen Input Variations                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 59]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, s48]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.relu.default
|    | ATen Input Variations       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 4096]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[59, 4096]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>int index = -1 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 59]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 60]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 60]> self = ?,<br>int dim = 1,<br>Optional[int] start = 59,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s10> start = ?,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sub.Tensor
|    | ATen Input Variations                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sum.default
|    | ATen Input Variations   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1]> self = ?    | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1024, 1024]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1024, 4096]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1024, 512]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[4096, 1024]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[50272, 512]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[512, 1024]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 59, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[16, 60, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[16, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 59]> self = ?,<br>int dim = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 60]> self = ?,<br>int dim = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 59, 59]> self = ?,<br>int dim = 1     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 59]> self = ?,<br>int dim = 1         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 60]> self = ?,<br>int dim = 1         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[59, 59]> self = ?,<br>int dim = 0        | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [-1, 1024]                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 16, 64]            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 16, 1, 60]> self = ?,<br>List[int] size = [16, 1, 60]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, <s10 + 1>] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 16, 59, 59]> self = ?,<br>List[int] size = [16, 59, 59]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 16, 59, 64]> self = ?,<br>List[int] size = [16, -1, 64]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 16, 60, 64]> self = ?,<br>List[int] size = [16, -1, 64]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 50272]> self = ?,<br>List[int] size = [1, 1, 50272]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [-1, 1024]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, 59, 16, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [59, 1024]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 59, 512]> self = ?,<br>List[int] size = [59, 512]                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 59]> self = ?,<br>List[int] size = [-1, 59]                       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[16, 1, 60]> self = ?,<br>List[int] size = [1, 16, 1, 60]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[16, 59, 59]> self = ?,<br>List[int] size = [1, 16, 59, 59]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[16, 59, 64]> self = ?,<br>List[int] size = [1, 16, 59, 64]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[59, 1024]> self = ?,<br>List[int] size = [1, 59, 1024]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[59, 50272]> self = ?,<br>List[int] size = [1, 59, 50272]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[59, 512]> self = ?,<br>List[int] size = [1, 59, 512]                 | Done     | N/A                 | N/A          | N/A               | N/A                |

