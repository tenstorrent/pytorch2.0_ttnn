# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default   |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
|  1 | aten._to_copy.default   |                 27 |           9 |         0 |          0 | 🚧          |    0.33 |
|  2 | aten.abs.default        |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor         |                 23 |           9 |         0 |          0 | 🚧          |    0.39 |
|  4 | aten.arange.default     |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default        |                 10 |           2 |         0 |          0 | 🚧          |    0.2  |
|  6 | aten.cat.default        |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default      |                 10 |           4 |         0 |          0 | 🚧          |    0.4  |
|  8 | aten.div.Tensor         |                  8 |           2 |         0 |          0 | 🚧          |    0.25 |
|  9 | aten.embedding.default  |                  6 |           3 |         0 |          0 | 🚧          |    0.5  |
| 10 | aten.expand.default     |                 13 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.full_like.default  |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.gt.Scalar          |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.le.Tensor          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.log.default        |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.lt.Scalar          |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 16 | aten.mean.dim           |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 17 | aten.minimum.default    |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 18 | aten.mm.default         |                  7 |           3 |         0 |          0 | 🚧          |    0.43 |
| 19 | aten.mul.Tensor         |                 18 |           9 |         0 |          0 | 🚧          |    0.5  |
| 20 | aten.neg.default        |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
| 21 | aten.ones.default       |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.permute.default    |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 23 | aten.pow.Tensor_Scalar  |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 24 | aten.relu.default       |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 25 | aten.repeat.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.rsqrt.default      |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 27 | aten.rsub.Scalar        |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 28 | aten.slice.Tensor       |                 38 |           0 |         0 |          0 | ✘           |    0    |
| 29 | aten.sub.Tensor         |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 30 | aten.sym_size.int       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 31 | aten.t.default          |                  4 |           3 |         0 |          0 | 🚧          |    0.75 |
| 32 | aten.transpose.int      |                  8 |           3 |         0 |          0 | 🚧          |    0.38 |
| 33 | aten.unsqueeze.default  |                 24 |          12 |         0 |          0 | 🚧          |    0.5  |
| 34 | aten.view.default       |                 35 |          12 |         0 |          0 | 🚧          |    0.34 |
| 35 | aten.where.self         |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 36 | aten.zeros.default      |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 37 | aten.zeros_like.default |                  3 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996066701819204 | 0      |
|  1 | Tensor<[1, 12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9988490137455995 | 0      |
|  3 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.999647610495207  | 0      |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Done     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Done     | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                             | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Done     | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                   | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 1, 768]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                    | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 10, 768]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Done     | Fallback   | 1.0   | -1     |
|  8 | Tensor<[1, 10, 768]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                   | Done     | Fallback   | 1.0   | -1     |
|  9 | Tensor<[1, 12, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 12, 1, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
| 11 | Tensor<[1, 12, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 12 | Tensor<[1, 12, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 13 | Tensor<[1, 12, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 14 | Tensor<[1, 12, 1, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 15 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 12, 10, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Fallback   | 1.0   | -1     |
| 18 | Tensor<[1, 12, 10, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                | Done     | Fallback   | 1.0   | -1     |
| 19 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                         | Done     | Fallback   | 1.0   | -1     |
| 20 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                           | None     | Fallback   | 1.0   | -1     |
| 21 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                       | Done     | Fallback   | 1.0   | -1     |
| 22 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                         | None     | Fallback   | 1.0   | -1     |
| 23 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                         | Unknown  | Fallback   | 1.0   | -1     |
| 24 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                           | Unknown  | Fallback   | 1.0   | -1     |
| 25 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                 | Unknown  | Unknown    | N/A   | N/A    |
### aten.abs.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10, 10]> self = ? | Done     | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?               | Unknown  | Done       | 0.9999979281658833 | 0      |
|  2 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                         | Done     | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?             | Done     | Done       | 0.9999979472667919 | 0      |
|  4 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.999999484535418  | 0      |
|  5 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?         | Unknown  | Done       | 0.9999996526211676 | 0      |
|  6 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?            | Unknown  | Done       | 1.0                | 0      |
|  7 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?           | Unknown  | Done       | 0.9999934604499161 | 0      |
|  8 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?            | Unknown  | Done       | 0.9999979632003032 | 0      |
|  9 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?           | Unknown  | Done       | 0.9999989934998549 | 0      |
| 10 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?         | Done     | Done       | 0.9999980931542564 | 0      |
| 13 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?       | Done     | Done       | 0.9999982182328475 | 0      |
| 14 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                 | Done     | Done       | 1.0                | 0      |
| 15 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                | Done     | Done       | 1.0                | 0      |
| 16 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                               | Done     | Done       | 1.0                | 0      |
| 17 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                               | Done     | Done       | 0.9998911854514341 | 0      |
| 18 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                     | Done     | Done       | 0.9999974429311648 | 0      |
| 19 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                 | Unknown  | Done       | 1.0                | 0      |
| 20 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                | 0      |
| 21 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                       | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                      | Unknown  | Unknown    | N/A                | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | None     | Fallback   | 1.0   | -1     |
|  1 | number end = 1,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | None     | Fallback   | 1.0   | -1     |
|  2 | number end = 10,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | None     | Fallback   | 1.0   | -1     |
|  3 | number end = 2,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Fallback   | 1.0   | -1     |
|  4 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[12, 1, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?         | Unknown  | Done       | 0.99999453692335   | 0      |
|  1 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?           | Unknown  | Done       | 0.9999967553533249 | 0      |
|  2 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?           | Unknown  | Done       | 0.9999961067493723 | 0      |
|  3 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?         | Unknown  | Done       | 0.9999854963435696 | 0      |
|  4 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?          | Unknown  | Done       | 0.9999957721315945 | 0      |
|  5 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?          | Unknown  | Done       | 0.9999874579074841 | 0      |
|  6 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?        | Done     | Done       | 0.9999944735026027 | 0      |
|  9 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?        | Done     | Done       | 0.9999872132381099 | 0      |
### aten.cat.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 1]>, <[1, 1, 1]>],<br>int dim = -1           | Unknown  | Done       | 1.0   | 0      |
|  1 | List[Tensor] tensors = [<[1, 1, s0]>, <[1, 1, 1]>],<br>int dim = -1          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 12, 1, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | Done       | 1.0   | 0      |
|  3 | List[Tensor] tensors = [<[1, 12, s0, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 3072]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 768]> self = ?                                                               | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 10, 3072]> self = ?                                                             | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 10, 768]> self = ?                                                              | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 12, 1, 10]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 12, 1, 1]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 12, 1, 2]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 12, 1, s0 + 1]> self = ?                                                        | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 12, 10, 10]> self = ?                                                           | Done     | Done       | 1.0   | 0      |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                           | None     | Fallback   | 1.0                | -1     |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357           | Done     | Done       | 1.0                | 0      |
|  2 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781          | Done     | Done       | 0.9999956526484233 | 0      |
|  3 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                          | None     | Fallback   | 1.0                | -1     |
|  4 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                           | Unknown  | Fallback   | 1.0                | -1     |
|  5 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | Done       | 1.0                | 0      |
|  6 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                 | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357 | Unknown  | Unknown    | N/A                | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?           | Done     | Unknown    | N/A   | N/A    |
|  1 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?         | Done     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ? | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?      | Done     | Done       | 1.0   | 2      |
|  5 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?       | Unknown  | Unknown    | N/A   | N/A    |
### aten.expand.default
|    | ATen Input Variations                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]             | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]               | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]               | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]           | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]           | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [1, 12, 2, 64]             | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [1, 12, 64, 10]           | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [1, 12, 64, 1]             | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [1, 12, 64, 2]             | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 12, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
### aten.full_like.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | None     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False         | None     | Fallback   | 1.0   | -1     |
|  2 | Tensor<[2, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Done     | Fallback   |     1 |      0 |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | None     | Fallback   |     1 |     -1 |
### aten.log.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?           | None     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[10, 10]> self = ?         | None     | Fallback   | 1.0   | -1     |
|  2 | Tensor<[2, 2]> self = ?           | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.lt.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16           | Done     | Fallback   | 1.0   | 0      |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8          | Done     | Fallback   | 1.0   | 0      |
|  2 | Tensor<[2, 2]> self = ?,<br>number other = 16           | Unknown  | Fallback   | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                    | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True  | Unknown  | Done       | 1        |      0 |
|  1 | Tensor<[1, 10, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Done     | Done       | 0.999963 |      0 |
### aten.minimum.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                     | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                 | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                     | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  | Done       | 0.99994  |      0 |
|  1 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?   | Unknown  | Done       | 0.999969 |      0 |
|  2 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 32128]> mat2 = ?  | Unknown  | Done       | 0.999884 |      0 |
|  3 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | 0.999971 |      0 |
|  4 | Tensor<[10, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | 0.999943 |      0 |
|  5 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | Done       | 0.999968 |      0 |
|  6 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | 0.999968 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Done       | 0.9999960673263144 | 0      |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Done     | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161           | Unknown  | Done       | 0.9999962776351973 | 0      |
|  8 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999951980116506 | 0      |
|  9 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Done     | Done       | 0.9999958158478717 | 0      |
| 10 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Done     | Done       | 1.0                | 0      |
| 11 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Done     | Done       | 1.0                | 0      |
| 12 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                               | Done     | Done       | 1.0                | 0      |
| 13 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Done     | Done       | 1.0                | 0      |
| 14 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 15 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                      | Unknown  | Done       | 0.999996247177683  | 0      |
| 16 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                     | Done     | Done       | 0.9999962062545852 | 0      |
| 17 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |
### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?           | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.ones.default
|    | ATen Input Variations                                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  | Fallback   | 1.0   | -1     |
|  1 | List[int] size = [1, 1, <s0>],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [1, 1],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Fallback   | 1.0   | -1     |
|  3 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | None     | Fallback   | 1.0   | -1     |
|  4 | List[int] size = [1, 2],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Done       | 1.0   | 0      |
|  5 | List[int] size = [1, <s0 + 1>],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1]           | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[10, 10, 12]> self = ?,<br>List[int] dims = [2, 0, 1]         | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2, 12]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1] | Unknown  | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>number exponent = 2  | Unknown  | Done       | 0.999994 |      0 |
|  1 | Tensor<[1, 10, 768]> self = ?,<br>number exponent = 2 | Done     | Done       | 0.999994 |      0 |
### aten.relu.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 10, 3072]> self = ? | Done     | Done       |     1 |      0 |
### aten.repeat.default
|    | ATen Input Variations                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | Done       |     1 |     -1 |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?  | Unknown  | Fallback   | 1        |     -1 |
|  1 | Tensor<[1, 10, 1]> self = ? | Done     | Done       | 0.999994 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                     | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999951882589773 | 0      |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | 1.0   | -1     |
| 29 | Tensor<[1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | 1.0   | -1     |
| 30 | Tensor<[1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | 1.0   | -1     |
| 31 | Tensor<[1, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Done       | 1.0   | -1     |
| 32 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Done       | 1.0   | -1     |
| 35 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 36 | Tensor<[2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Done       | 1.0   | -1     |
| 37 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?         | None     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?           | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.sym_size.int
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[3072, 768]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[32128, 768]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[768, 3072]> self = ?  | Done     | Done       |     1 |      0 |
|  3 | Tensor<[768, 768]> self = ?   | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 10, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 12, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 1            | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2            | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1            | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 2            | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1       | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2       | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 10]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 1]> self = ?,<br>int dim = 1               | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 1]> self = ?,<br>int dim = 2               | Done     | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 2]> self = ?,<br>int dim = 1               | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1          | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[10]> self = ?,<br>int dim = 0                 | Done     | Done       | 1.0   | 0      |
| 13 | Tensor<[10]> self = ?,<br>int dim = 1                 | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[12, 1, 1]> self = ?,<br>int dim = 0           | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[12, 10, 10]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[12, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1]> self = ?,<br>int dim = 0                  | Done     | Done       | 1.0   | 0      |
| 19 | Tensor<[1]> self = ?,<br>int dim = 1                  | Done     | Done       | 1.0   | 0      |
| 20 | Tensor<[2]> self = ?,<br>int dim = 0                  | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[2]> self = ?,<br>int dim = 1                  | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0             | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[s0 + 1]> self = ?,<br>int dim = 1             | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]            | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                 | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]            | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                   | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]           | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]               | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]           | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]                 | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                       | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [12, 1, 10]             | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [12, 1, 1]               | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [12, 1, 2]               | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [12, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10]           | Done     | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64]           | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, 2, 64]             | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10]           | Done     | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [12, 64, 1]             | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [12, 64, 2]             | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [12, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                 | Unknown  | Done       | 1.0   | 0      |
| 24 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]               | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                   | Unknown  | Done       | 1.0   | 0      |
| 26 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]               | Done     | Done       | 1.0   | 0      |
| 27 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]                 | Done     | Done       | 1.0   | 0      |
| 28 | Tensor<[12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]             | Unknown  | Done       | 1.0   | 0      |
| 29 | Tensor<[12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]               | Unknown  | Done       | 1.0   | 0      |
| 30 | Tensor<[12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]               | Unknown  | Done       | 1.0   | 0      |
| 31 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 32 | Tensor<[12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]           | Done     | Done       | 1.0   | 0      |
| 34 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]           | Done     | Done       | 1.0   | 0      |
### aten.where.self
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                               | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                         | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2]> condition = ?,<br>Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                               | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> condition = ?,<br>Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 12, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | 1.0   | -1     |
|  1 | List[int] size = [1, 12, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | 1.0   | -1     |
|  2 | List[int] size = [1, 12, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros_like.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False           | None     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[2, 2]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | 1      |
|  2 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |

