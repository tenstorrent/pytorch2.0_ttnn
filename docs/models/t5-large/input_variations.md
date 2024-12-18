# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default   |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
|  1 | aten._to_copy.default   |                 27 |           6 |         0 |          0 | 🚧          |    0.22 |
|  2 | aten.abs.default        |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor         |                 23 |           7 |         0 |          0 | 🚧          |    0.3  |
|  4 | aten.arange.default     |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default        |                 10 |           2 |         0 |          0 | 🚧          |    0.2  |
|  6 | aten.cat.default        |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default      |                 10 |           4 |         0 |          0 | 🚧          |    0.4  |
|  8 | aten.div.Tensor         |                  8 |           2 |         0 |          0 | 🚧          |    0.25 |
|  9 | aten.embedding.default  |                  6 |           2 |         0 |          0 | 🚧          |    0.33 |
| 10 | aten.expand.default     |                 13 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.full_like.default  |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.gt.Scalar          |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 13 | aten.le.Tensor          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.log.default        |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 15 | aten.lt.Scalar          |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 16 | aten.mean.dim           |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 17 | aten.minimum.default    |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 18 | aten.mm.default         |                  7 |           3 |         0 |          0 | 🚧          |    0.43 |
| 19 | aten.mul.Tensor         |                 18 |           5 |         0 |          0 | 🚧          |    0.28 |
| 20 | aten.neg.default        |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.ones.default       |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.permute.default    |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 23 | aten.pow.Tensor_Scalar  |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 24 | aten.relu.default       |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 25 | aten.repeat.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.rsqrt.default      |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 27 | aten.rsub.Scalar        |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 28 | aten.slice.Tensor       |                 38 |           0 |         0 |          0 | ✘           |    0    |
| 29 | aten.sub.Tensor         |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.sym_size.int       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 31 | aten.t.default          |                  4 |           3 |         0 |          0 | 🚧          |    0.75 |
| 32 | aten.transpose.int      |                  8 |           3 |         0 |          0 | 🚧          |    0.38 |
| 33 | aten.unsqueeze.default  |                 24 |           4 |         0 |          0 | 🚧          |    0.17 |
| 34 | aten.view.default       |                 35 |          12 |         0 |          0 | 🚧          |    0.34 |
| 35 | aten.where.self         |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 36 | aten.zeros.default      |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 37 | aten.zeros_like.default |                  3 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9994770415465073 | 0      |
|  1 | Tensor<[1, 16, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9993941841529228 | 0      |
|  3 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 16, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | 0.999630084119031  | 0      |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Done     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                             | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1024]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 1, 1024]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                   | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 10, 1024]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Done     | Fallback   | 1.0   | -1     |
|  8 | Tensor<[1, 10, 1024]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Done     | Fallback   | 1.0   | -1     |
|  9 | Tensor<[1, 16, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 16, 1, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
| 11 | Tensor<[1, 16, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 12 | Tensor<[1, 16, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 13 | Tensor<[1, 16, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 14 | Tensor<[1, 16, 1, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 15 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 16, 10, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Fallback   | 1.0   | -1     |
| 18 | Tensor<[1, 16, 10, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                | Done     | Fallback   | 1.0   | -1     |
| 19 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                         | Unknown  | Fallback   | 1.0   | -1     |
| 20 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                           | Unknown  | Fallback   | 1.0   | -1     |
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
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?             | Unknown  | Done       | 0.9999978670851309 | 0      |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?           | Done     | Done       | 0.9999980719610716 | 0      |
|  3 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                         | Done     | Done       | 1.0                | 0      |
|  4 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.9999963822301441 | 0      |
|  5 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?         | Unknown  | Done       | 0.9999980875865225 | 0      |
|  6 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?            | Unknown  | Done       | 0.9999966496365543 | 0      |
|  7 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?           | Unknown  | Done       | 1.0                | 0      |
|  8 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?            | Unknown  | Done       | 0.9999953317919815 | 0      |
|  9 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?           | Unknown  | Done       | 0.9999999768847452 | 0      |
| 10 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?         | Done     | Done       | 0.9999978651653738 | 0      |
| 13 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?       | Done     | Done       | 0.9999980493395021 | 0      |
| 14 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                 | Unknown  | Done       | 1.0                | 0      |
| 15 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                | 0      |
| 16 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                               | Done     | Done       | 1.0                | 0      |
| 17 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                               | Done     | Done       | 0.9998805782393794 | 0      |
| 18 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                     | Done     | Done       | 0.9999996695457644 | 0      |
| 19 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                 | Unknown  | Done       | 1.0                | 0      |
| 20 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                | 0      |
| 21 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                       | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                      | Unknown  | Unknown    | N/A                | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Done       | 1.0   | -1     |
|  1 | number end = 1,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | -1     |
|  2 | number end = 10,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | -1     |
|  3 | number end = 2,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | -1     |
|  4 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[16, 1, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?         | Unknown  | Done       | 0.9999944446275958 | 0      |
|  1 | Tensor<[16, 1, 1]> self = ?,<br>Tensor<[16, 1, 64]> mat2 = ?           | Unknown  | Done       | 0.9999965148693168 | 0      |
|  2 | Tensor<[16, 1, 2]> self = ?,<br>Tensor<[16, 2, 64]> mat2 = ?           | Unknown  | Done       | 0.9999950266563523 | 0      |
|  3 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?         | Unknown  | Done       | 0.9999894711333182 | 0      |
|  4 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> mat2 = ?          | Unknown  | Done       | 0.9999846353936265 | 0      |
|  5 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 2]> mat2 = ?          | Unknown  | Done       | 0.9999903537055738 | 0      |
|  6 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s0 + 1]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[16, 1, s0 + 1]> self = ?,<br>Tensor<[16, s0 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[16, 10, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?        | Done     | Done       | 0.9999944599230176 | 0      |
|  9 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?        | Done     | Done       | 0.9999878901618322 | 0      |
### aten.cat.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, 1]>, <[1, 1, 1]>],<br>int dim = -1           | Unknown  | Done       | 1.0   | 0      |
|  1 | List[Tensor] tensors = [<[1, 1, s0]>, <[1, 1, 1]>],<br>int dim = -1          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[Tensor] tensors = [<[1, 16, 1, 64]>, <[1, 16, 1, 64]>],<br>int dim = 2  | Unknown  | Done       | 1.0   | 0      |
|  3 | List[Tensor] tensors = [<[1, 16, s0, 64]>, <[1, 16, 1, 64]>],<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 4096]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 10, 1024]> self = ?                                                             | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 10, 16, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 10, 4096]> self = ?                                                             | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 16, 1, 10]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 16, 1, 1]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 16, 1, 2]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 16, 1, s0 + 1]> self = ?                                                        | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 16, 10, 10]> self = ?                                                           | Done     | Done       | 1.0   | 0      |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                           | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781          | Done     | Done       | 0.9999963536375557 | 0      |
|  3 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                          | Done     | Done       | 1.0                | 0      |
|  4 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                           | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | Done       | 1.0                | 0      |
|  6 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                 | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357 | Unknown  | Unknown    | N/A                | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 16]> weight = ?,<br>Tensor<[1, 1]> indices = ?           | Unknown  | Done       | 1.0   | 2      |
|  1 | Tensor<[32, 16]> weight = ?,<br>Tensor<[10, 10]> indices = ?         | Done     | Done       | 1.0   | 2      |
|  2 | Tensor<[32, 16]> weight = ?,<br>Tensor<[2, 2]> indices = ?           | Unknown  | Done       | 1.0   | 2      |
|  3 | Tensor<[32, 16]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ? | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?     | Done     | Done       | 1.0   | 2      |
|  5 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?      | Unknown  | Done       | 1.0   | 2      |
### aten.expand.default
|    | ATen Input Variations                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]             | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]               | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]               | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]           | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]           | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [1, 16, 2, 64]             | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [1, 16, 64, 10]           | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [1, 16, 64, 1]             | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [1, 16, 64, 2]             | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 16, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
### aten.full_like.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False         | None     | Fallback   | 1.0   | -1     |
|  2 | Tensor<[2, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Done     | Done       |     1 |      0 |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | Unknown  | Fallback   |     1 |     -1 |
### aten.log.default
|    | ATen Input Variations             | Status   | Isolated   | PCC                  | Host   |
|---:|:----------------------------------|:---------|:-----------|:---------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?           | Unknown  | Done       | 1.0                  | 0      |
|  1 | Tensor<[10, 10]> self = ?         | Done     | Done       | -0.17483331485579878 | 0      |
|  2 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | -0.4921952351205055  | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A                  | N/A    |
### aten.lt.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8          | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2]> self = ?,<br>number other = 16           | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                     | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 10, 1024]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Done     | Done       |     1 |      0 |
### aten.minimum.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                     | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                 | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                     | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                         | Status   | Isolated   |      PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?  | Unknown  | Done       | 0.999966 |      0 |
|  1 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 32128]> mat2 = ? | Unknown  | Done       | 0.999834 |      0 |
|  2 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?  | Unknown  | Done       | 0.999965 |      0 |
|  3 | Tensor<[1, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?  | Unknown  | Done       | 0.999935 |      0 |
|  4 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ? | Done     | Done       | 0.999965 |      0 |
|  5 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ? | Done     | Done       | 0.999966 |      0 |
|  6 | Tensor<[10, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ? | Done     | Done       | 0.999935 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Done       | 0.9999993549752692 | 0      |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                      | Unknown  | Done       | 1.0                | 0      |
|  8 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Unknown  | Done       | 0.9999963392698429 | 0      |
|  9 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?               | Done     | Done       | 0.9999956630469743 | 0      |
| 10 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                | 0      |
| 11 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 12 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                               | Done     | Done       | 1.0                | 0      |
| 13 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Done     | Done       | 1.0                | 0      |
| 14 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                    | Unknown  | Done       | 0.9999952519688861 | 0      |
| 15 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                   | Done     | Done       | 0.9999954473637787 | 0      |
| 16 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 17 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |
### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.ones.default
|    | ATen Input Variations                                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  | Done       | 1.0   | -1     |
|  1 | List[int] size = [1, 1, <s0>],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [1, 1],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Done       | 1.0   | -1     |
|  3 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | -1     |
|  4 | List[int] size = [1, 2],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Done       | 1.0   | -1     |
|  5 | List[int] size = [1, <s0 + 1>],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[10, 10, 16]> self = ?,<br>List[int] dims = [2, 0, 1]         | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2, 16]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1] | Unknown  | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                  | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>number exponent = 2  | Unknown  | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 10, 1024]> self = ?,<br>number exponent = 2 | Done     | Done       | 0.999994 |      0 |
### aten.relu.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 4096]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 10, 4096]> self = ? | Done     | Done       |     1 |      0 |
### aten.repeat.default
|    | ATen Input Variations                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | Done       |     1 |     -1 |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?  | Unknown  | Fallback   | 1        |     -1 |
|  1 | Tensor<[1, 10, 1]> self = ? | Done     | Done       | 0.999989 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0     | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A   | N/A    |
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
| 13 | Tensor<[1, 16, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 16, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[1, 16, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 16, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 16, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
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
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?         | None     | Done       | 0.8718761059449699 | 0      |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?           | Unknown  | Done       | 0.754173891803983  | 0      |
|  3 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
### aten.sym_size.int
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 1024]> self = ?  | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1024, 4096]> self = ?  | Done     | Done       |     1 |      0 |
|  2 | Tensor<[32128, 1024]> self = ? | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[4096, 1024]> self = ?  | Done     | Done       |     1 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 10, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 16, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 1            | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2            | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1            | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 2            | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1       | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2       | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 10]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 1]> self = ?,<br>int dim = 1               | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 1]> self = ?,<br>int dim = 2               | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 2]> self = ?,<br>int dim = 1               | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1          | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[10]> self = ?,<br>int dim = 0                 | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[10]> self = ?,<br>int dim = 1                 | Done     | Done       | 1.0   | 0      |
| 14 | Tensor<[16, 1, 1]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[16, 10, 10]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 16 | Tensor<[16, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1]> self = ?,<br>int dim = 0                  | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1]> self = ?,<br>int dim = 1                  | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[2]> self = ?,<br>int dim = 0                  | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[2]> self = ?,<br>int dim = 1                  | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0             | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[s0 + 1]> self = ?,<br>int dim = 1             | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]                 | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]           | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 4096]> self = ?,<br>List[int] size = [1, 4096]                 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [1, -1, 16, 64]          | Done     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 10, 1024]> self = ?,<br>List[int] size = [10, 1024]               | Done     | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 10, 16, 64]> self = ?,<br>List[int] size = [1, -1, 1024]          | Done     | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 10, 4096]> self = ?,<br>List[int] size = [10, 4096]               | Done     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]                 | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                       | Done     | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 16, 1, 10]> self = ?,<br>List[int] size = [16, 1, 10]             | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 16, 1, 1]> self = ?,<br>List[int] size = [16, 1, 1]               | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 16, 1, 2]> self = ?,<br>List[int] size = [16, 1, 2]               | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] size = [16, 1, 64]             | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>List[int] size = [16, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 16, 10, 10]> self = ?,<br>List[int] size = [16, 10, 10]           | Done     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 16, 10, 64]> self = ?,<br>List[int] size = [16, 10, 64]           | Done     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 16, 2, 64]> self = ?,<br>List[int] size = [16, 2, 64]             | Unknown  | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 16, 64, 10]> self = ?,<br>List[int] size = [16, 64, 10]           | Done     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 16, 64, 1]> self = ?,<br>List[int] size = [16, 64, 1]             | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 16, 64, 2]> self = ?,<br>List[int] size = [16, 64, 2]             | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 16, 64, s0 + 1]> self = ?,<br>List[int] size = [16, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>List[int] size = [16, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]               | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[1, 4096]> self = ?,<br>List[int] size = [1, 1, 4096]                 | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[10, 1024]> self = ?,<br>List[int] size = [1, 10, 1024]               | Done     | Unknown    | N/A   | N/A    |
| 27 | Tensor<[10, 4096]> self = ?,<br>List[int] size = [1, 10, 4096]               | Done     | Unknown    | N/A   | N/A    |
| 28 | Tensor<[16, 1, 10]> self = ?,<br>List[int] size = [1, 16, 1, 10]             | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[16, 1, 1]> self = ?,<br>List[int] size = [1, 16, 1, 1]               | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[16, 1, 2]> self = ?,<br>List[int] size = [1, 16, 1, 2]               | Unknown  | Done       | 1.0   | 0      |
| 31 | Tensor<[16, 1, 64]> self = ?,<br>List[int] size = [1, 16, 1, 64]             | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[16, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 16, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[16, 10, 10]> self = ?,<br>List[int] size = [1, 16, 10, 10]           | Done     | Unknown    | N/A   | N/A    |
| 34 | Tensor<[16, 10, 64]> self = ?,<br>List[int] size = [1, 16, 10, 64]           | Done     | Unknown    | N/A   | N/A    |
### aten.where.self
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                               | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                         | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2]> condition = ?,<br>Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                               | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> condition = ?,<br>Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 16, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | 1.0   | -1     |
|  1 | List[int] size = [1, 16, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | 1.0   | -1     |
|  2 | List[int] size = [1, 16, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros_like.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[2, 2]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | 1      |
|  2 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |

