# High Level Operations Status
|    | Operations                     |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default          |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default          |                  7 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor                |                  9 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.addmm.default             |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bmm.default               |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.cat.default               |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.clone.default             |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.cumsum.default            |                  3 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.embedding.default         |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.eq.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.expand.default            |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.full.default              |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.gt.Scalar                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.masked_fill.Scalar        |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.maximum.default           |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.mm.default                |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.mul.Tensor                |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.native_layer_norm.default |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.new_ones.default          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.relu.default              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.rsub.Scalar               |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.select.int                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.slice.Tensor              |                 11 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.sub.Tensor                |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.sum.default               |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.sym_size.int              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.t.default                 |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.transpose.int             |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.unsqueeze.default         |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.view.default              |                 31 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[16, 1, 60]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9995034131411049 | 0      |
|  1 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[16, 59, 59]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996050078540779 | 0      |
### aten._to_copy.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Optional[int] dtype = torch.bfloat16      | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>Optional[int] dtype = torch.bool          | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Optional[int] dtype = torch.bool     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 59, 59]> self = ?,<br>Optional[int] dtype = torch.bfloat16     | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 1, 59, 59]> self = ?,<br>Optional[int] dtype = torch.bool         | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[59, 59]> self = ?,<br>Optional[int] dtype = torch.bfloat16           | Unknown  | Fallback   | 1.0   | -1     |
### aten._unsafe_view.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 59, 16, 64]> self = ?,<br>List[int] size = [1, 59, 1024] | Unknown  | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999978491756752 | 0      |
|  1 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999976114238806 | 0      |
|  2 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999982098188964 | 0      |
|  3 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Unknown  | Done       | 0.9999979564006173 | 0      |
|  5 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Done       | 1.0                | 0      |
|  6 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Unknown  | Done       | 0.9999980162540556 | 0      |
|  7 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Unknown  | Done       | 0.9999936088923967 | 0      |
|  8 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Unknown  | Done       | 0.999998051425216  | 0      |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  | Done       | 0.999964 |      0 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?  | Unknown  | Done       | 0.999926 |      0 |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  | Done       | 0.999965 |      0 |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[59, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Unknown  | Done       | 0.999933 |      0 |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?  | Unknown  | Done       | 0.999965 |      0 |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Unknown  | Done       | 0.999964 |      0 |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | Done       | 0.9999864427688651 | 0      |
|  1 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | Done       | 0.9999861525013974 | 0      |
|  2 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Unknown  | Done       | 0.9999863065710479 | 0      |
|  5 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Unknown  | Done       | 0.9999865846992688 | 0      |
### aten.cat.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 16, 59, 64]>, <[1, 16, 1, 64]>],<br>int dim = 2  | Unknown  | Done       | 1.0   | 0      |
|  1 | List[Tensor] tensors = [<[1, 16, s10, 64]>, <[1, 16, 1, 64]>],<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 59]>, <[1, 1]>],<br>int dim = -1                 | Unknown  | Done       | 1.0   | 0      |
|  3 | List[Tensor] tensors = [<[1, s48]>, <[1, 1]>],<br>int dim = -1                | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1024]> self = ?                                                                 | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 59, 1024]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[16, 1, 60]> self = ?                                                               | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[16, 1, s10 + 1]> self = ?                                                          | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[16, 59, 59]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[59, 1024]> self = ?                                                                | Unknown  | Done       | 1.0   | 0      |
### aten.cumsum.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999222650764173 | 0      |
|  1 | Tensor<[1, 60]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999102147345227 | 0      |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                          | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                         | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1 | Unknown  | Done       |     1 |      0 |
### aten.eq.Scalar
|    | ATen Input Variations                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?,<br>number other = 1 | Unknown  | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]            | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>List[int] size = [1, 1, 1, 60]             | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 59, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]           | Unknown  | Done       | 1.0   | -1     |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [59, 59],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Done       |     1 |      0 |
### aten.gt.Scalar
|    | ATen Input Variations                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?,<br>number other = 0 | Unknown  | Fallback   |     1 |     -1 |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | 0      |
### aten.maximum.default
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor other = ?      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor other = ?     | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?  | Unknown  | Done       | 0.999965 |      0 |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?   | Unknown  | Done       | 0.999971 |      0 |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?  | Unknown  | Done       | 0.999971 |      0 |
|  3 | Tensor<[59, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Unknown  | Done       | 0.999955 |      0 |
|  4 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?  | Unknown  | Done       | 0.999972 |      0 |
|  5 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ? | Unknown  | Done       | 0.999971 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125           | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125          | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?           | Unknown  | Done       | 0.9999962781186207 | 0      |
|  3 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?           | Unknown  | Done       | 0.9999915040150256 | 0      |
|  4 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   | PCC   |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | N/A   |      1 |
|  1 | Tensor<[1, 59, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      1 |
### aten.new_ones.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False  | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, s48]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 4096]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[59, 4096]> self = ? | Unknown  | Done       |     1 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999970371545867 | 0      |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999935135188937 | 0      |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Done       |     1 |      0 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 59, 59]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 59]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 60]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 60]> self = ?,<br>int dim = 1,<br>Optional[int] start = 59,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s10> start = ?,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                              | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1      | Unknown  | Done       | 0.9999921860032245 | 0      |
|  1 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1      | Unknown  | Done       | 0.9999885579181255 | 0      |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.sum.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?    | Unknown  | Done       |     1 |      0 |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 1024]> self = ? | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1024, 4096]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[1024, 512]> self = ?  | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[4096, 1024]> self = ? | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[50272, 512]> self = ? | Unknown  | Done       |     1 |      0 |
|  5 | Tensor<[512, 1024]> self = ?  | Unknown  | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 59, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[16, 60, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[16, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 59]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 60]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 59, 59]> self = ?,<br>int dim = 1     | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 59]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 60]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1    | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[59, 59]> self = ?,<br>int dim = 0        | Unknown  | Done       | 1.0   | 0      |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [-1, 1024]                | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]           | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 16, 64]            | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]            | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                   | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                 | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 16, 1, 60]> self = ?,<br>List[int] size = [16, 1, 60]             | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]            | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 16, 59, 59]> self = ?,<br>List[int] size = [16, 59, 59]           | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 16, 59, 64]> self = ?,<br>List[int] size = [16, -1, 64]           | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 16, 60, 64]> self = ?,<br>List[int] size = [16, -1, 64]           | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]      | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 50272]> self = ?,<br>List[int] size = [1, 1, 50272]               | Unknown  | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                   | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [-1, 1024]               | Unknown  | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]          | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, 59, 16, 64]          | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [59, 1024]               | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 59, 512]> self = ?,<br>List[int] size = [59, 512]                 | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 59]> self = ?,<br>List[int] size = [-1, 59]                       | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[16, 1, 60]> self = ?,<br>List[int] size = [1, 16, 1, 60]             | Unknown  | Done       | 1.0   | 0      |
| 24 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[16, 59, 59]> self = ?,<br>List[int] size = [1, 16, 59, 59]           | Unknown  | Done       | 1.0   | 0      |
| 27 | Tensor<[16, 59, 64]> self = ?,<br>List[int] size = [1, 16, 59, 64]           | Unknown  | Done       | 1.0   | 0      |
| 28 | Tensor<[59, 1024]> self = ?,<br>List[int] size = [1, 59, 1024]               | Unknown  | Done       | 1.0   | 0      |
| 29 | Tensor<[59, 50272]> self = ?,<br>List[int] size = [1, 59, 50272]             | Unknown  | Done       | 1.0   | 0      |
| 30 | Tensor<[59, 512]> self = ?,<br>List[int] size = [1, 59, 512]                 | Unknown  | Done       | 1.0   | 0      |

