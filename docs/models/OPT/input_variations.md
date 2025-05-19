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
| 14 | aten.lt.Tensor                 |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.masked_fill.Scalar        |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.maximum.default           |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.mm.default                |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.mul.Tensor                |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.native_layer_norm.default |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.new_ones.default          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.relu.default              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.rsub.Scalar               |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.select.int                |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.slice.Tensor              |                 11 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.sub.Tensor                |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.sum.default               |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.sym_size.int              |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.t.default                 |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.transpose.int             |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.unsqueeze.default         |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.view.default              |                 31 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[16, 1, 60]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996581386590605 | -1     |
|  1 | Tensor<[16, 1, s10 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[16, 59, 59]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996018948576791 | -1     |
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
|  0 | Tensor<[1, 59, 16, 64]> self = ?,<br>List[int] size = [1, 59, 1024] | Unknown  | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999980100070343 | -1     |
|  1 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999981470622101 | -1     |
|  2 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999981065030811 | -1     |
|  3 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Unknown  | Done       | 0.9999979810730094 | -1     |
|  5 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Done       | 1.0                | -1     |
|  6 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Unknown  | Done       | 0.9999979949011689 | -1     |
|  7 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Unknown  | Done       | 0.9999857070398074 | -1     |
|  8 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Unknown  | Done       | 0.9999980404104364 | -1     |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  | Done       | 0.999965 |     -1 |
|  1 | Tensor<[1024]> self = ?,<br>Tensor<[1, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ?  | Unknown  | Done       | 0.999927 |     -1 |
|  2 | Tensor<[1024]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Unknown  | Done       | 0.999964 |     -1 |
|  3 | Tensor<[1024]> self = ?,<br>Tensor<[59, 4096]> mat1 = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Unknown  | Done       | 0.999933 |     -1 |
|  4 | Tensor<[4096]> self = ?,<br>Tensor<[1, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ?  | Unknown  | Done       | 0.999966 |     -1 |
|  5 | Tensor<[4096]> self = ?,<br>Tensor<[59, 1024]> mat1 = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Unknown  | Done       | 0.999964 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | Done       | 0.9999851735451676 | -1     |
|  1 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | Done       | 0.9999847705987238 | -1     |
|  2 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Unknown  | Done       | 0.9999863292548117 | -1     |
|  5 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Unknown  | Done       | 0.9999863252227004 | -1     |
### aten.cat.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 16, 59, 64]>, <[1, 16, 1, 64]>],<br>int dim = 2  | Unknown  | Done       | 1.0   | -1     |
|  1 | List[Tensor] tensors = [<[1, 16, s10, 64]>, <[1, 16, 1, 64]>],<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 59]>, <[1, 1]>],<br>int dim = -1                 | Unknown  | Failed     | N/A   | N/A    |
|  3 | List[Tensor] tensors = [<[1, s48]>, <[1, 1]>],<br>int dim = -1                | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?                                                              | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1024]> self = ?                                                                 | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 59, 1024]> self = ?                                                             | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 59, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, s10 + 1]> self = ?                                                              | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[16, 1, 60]> self = ?                                                               | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[16, 1, s10 + 1]> self = ?                                                          | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[16, 59, 59]> self = ?                                                              | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[59, 1024]> self = ?                                                                | Unknown  | Done       | 1.0   | -1     |
### aten.cumsum.default
|    | ATen Input Variations                         | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9999897052853521 | -1     |
|  1 | Tensor<[1, 60]> self = ?,<br>int dim = 1      | Unknown  | Done       | 0.9998320262147442 | -1     |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                                   | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                          | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                         | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1  | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1 | Unknown  | Done       |     1 |     -1 |
### aten.eq.Scalar
|    | ATen Input Variations                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?,<br>number other = 1 | Unknown  | Done       |     1 |     -1 |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]            | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 60]> self = ?,<br>List[int] size = [1, 1, 1, 60]             | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 1, 1, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 59, 59]> self = ?,<br>List[int] size = [1, 1, 59, 59]           | Unknown  | Done       | 1.0   | -1     |
### aten.full.default
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [59, 59],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Done       |     1 |     -1 |
### aten.gt.Scalar
|    | ATen Input Variations                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[]> self = ?,<br>number other = 0 | Unknown  | Fallback   |     1 |     -1 |
### aten.lt.Tensor
|    | ATen Input Variations                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> mask = ?,<br>number value = -3.3895313892515355e+38           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> mask = ?,<br>number value = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> mask = ?,<br>number value = -3.3895313892515355e+38         | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[59, 59]> self = ?,<br>Tensor<[59, 59]> mask = ?,<br>number value = 0                                           | Unknown  | Unknown    | N/A   | N/A    |
### aten.maximum.default
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor other = ?      | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor other = ?     | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?  | Unknown  | Done       | 0.999962 |     -1 |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?   | Unknown  | Done       | 0.999973 |     -1 |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?  | Unknown  | Done       | 0.999971 |     -1 |
|  3 | Tensor<[59, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Unknown  | Done       | 0.999956 |     -1 |
|  4 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?  | Unknown  | Done       | 0.999972 |     -1 |
|  5 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ? | Unknown  | Done       | 0.999971 |     -1 |
### aten.mul.Tensor
|    | ATen Input Variations                                            | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125           | Unknown  | Done       | 1.0                | -1     |
|  1 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125          | Unknown  | Done       | 1.0                | -1     |
|  2 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?           | Unknown  | Done       | 0.9999975260474453 | -1     |
|  3 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?           | Unknown  | Done       | 0.9999959341448066 | -1     |
|  4 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                       | Status   | Isolated   | PCC   |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|-------:|
|  0 | Tensor<[1, 1, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05  | Unknown  | Done       | N/A   |      0 |
|  1 | Tensor<[1, 59, 1024]> input = ?,<br>List[int] normalized_shape = [1024],<br>Optional[Tensor]<[1024]> weight = ?,<br>Optional[Tensor]<[1024]> bias = ?,<br>float eps = 1e-05 | Unknown  | Done       | N/A   |      0 |
### aten.new_ones.default
|    | ATen Input Variations                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False  | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, s48]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.relu.default
|    | ATen Input Variations       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 4096]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[59, 4096]> self = ? | Unknown  | Done       |     1 |     -1 |
### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999928893925581 | -1     |
|  1 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999938839283163 | -1     |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Done       |     1 |     -1 |
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
|  8 | Tensor<[1, 60]> self = ?,<br>int dim = 1,<br>Optional[int] start = 59,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1,<br>Optional[int]<s10> start = ?,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                              | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1      | Unknown  | Done       | 0.9999997235254992 | -1     |
|  1 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1      | Unknown  | Done       | 0.9999975032031787 | -1     |
|  2 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1 | Unknown  | Unknown    | N/A                | N/A    |
### aten.sum.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1]> self = ?    | Unknown  | Done       |     1 |     -1 |
### aten.sym_size.int
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 1024]> self = ? | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1024, 4096]> self = ? | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[1024, 512]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[4096, 1024]> self = ? | Unknown  | Done       |     1 |     -1 |
|  4 | Tensor<[50272, 512]> self = ? | Unknown  | Done       |     1 |     -1 |
|  5 | Tensor<[512, 1024]> self = ?  | Unknown  | Done       |     1 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 59, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[16, 60, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[16, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 59]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 60]> self = ?,<br>int dim = 2      | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 59, 59]> self = ?,<br>int dim = 1     | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 59]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 60]> self = ?,<br>int dim = 1         | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1    | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[59, 59]> self = ?,<br>int dim = 0        | Unknown  | Done       | 1.0   | -1     |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [-1, 1024]                | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]           | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1, 16, 64]            | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                 | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, 1, 1024]            | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                   | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                 | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 16, 1, 60]> self = ?,<br>List[int] size = [16, 1, 60]             | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]            | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>List[int] size = [16, 1, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 16, 59, 59]> self = ?,<br>List[int] size = [16, 59, 59]           | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 16, 59, 64]> self = ?,<br>List[int] size = [16, -1, 64]           | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 16, 60, 64]> self = ?,<br>List[int] size = [16, -1, 64]           | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>List[int] size = [16, -1, 64]      | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 50272]> self = ?,<br>List[int] size = [1, 1, 50272]               | Unknown  | Done       | 1.0   | -1     |
| 16 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                   | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [-1, 1024]               | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]          | Unknown  | Done       | 1.0   | -1     |
| 19 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [1, 59, 16, 64]          | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 59, 1024]> self = ?,<br>List[int] size = [59, 1024]               | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 59, 512]> self = ?,<br>List[int] size = [59, 512]                 | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 59]> self = ?,<br>List[int] size = [-1, 59]                       | Unknown  | Done       | 1.0   | -1     |
| 23 | Tensor<[16, 1, 60]> self = ?,<br>List[int] size = [1, 16, 1, 60]             | Unknown  | Done       | 1.0   | -1     |
| 24 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
| 25 | Tensor<[16, 1, s10 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s10 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[16, 59, 59]> self = ?,<br>List[int] size = [1, 16, 59, 59]           | Unknown  | Done       | 1.0   | -1     |
| 27 | Tensor<[16, 59, 64]> self = ?,<br>List[int] size = [1, 16, 59, 64]           | Unknown  | Done       | 1.0   | -1     |
| 28 | Tensor<[59, 1024]> self = ?,<br>List[int] size = [1, 59, 1024]               | Unknown  | Done       | 1.0   | -1     |
| 29 | Tensor<[59, 50272]> self = ?,<br>List[int] size = [1, 59, 50272]             | Unknown  | Done       | 1.0   | -1     |
| 30 | Tensor<[59, 512]> self = ?,<br>List[int] size = [1, 59, 512]                 | Unknown  | Done       | 1.0   | -1     |

