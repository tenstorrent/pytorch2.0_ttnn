# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default   |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
|  1 | aten._to_copy.default   |                 27 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.abs.default        |                  1 |           0 |         0 |          1 | ✘           |    0    |
|  3 | aten.add.Tensor         |                 23 |           5 |         0 |          4 | 🚧          |    0.22 |
|  4 | aten.arange.default     |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default        |                 10 |           2 |         0 |          0 | 🚧          |    0.2  |
|  6 | aten.cat.default        |                  4 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default      |                 10 |           3 |         0 |          1 | 🚧          |    0.3  |
|  8 | aten.div.Tensor         |                  8 |           1 |         0 |          0 | 🚧          |    0.12 |
|  9 | aten.embedding.default  |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.expand.default     |                 13 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.full_like.default  |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.gt.Scalar          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.le.Tensor          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.log.default        |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.lt.Scalar          |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.mean.dim           |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 17 | aten.minimum.default    |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 18 | aten.mm.default         |                  7 |           3 |         0 |          0 | 🚧          |    0.43 |
| 19 | aten.mul.Tensor         |                 18 |           3 |         0 |          6 | 🚧          |    0.17 |
| 20 | aten.neg.default        |                  3 |           0 |         0 |          1 | ✘           |    0    |
| 21 | aten.ones.default       |                  6 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.permute.default    |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 23 | aten.pow.Tensor_Scalar  |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 24 | aten.relu.default       |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 25 | aten.repeat.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 26 | aten.rsqrt.default      |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 27 | aten.rsub.Scalar        |                  4 |           1 |         0 |          0 | 🚧          |    0.25 |
| 28 | aten.slice.Tensor       |                 38 |           0 |         0 |          0 | ✘           |    0    |
| 29 | aten.sub.Tensor         |                  4 |           0 |         0 |          1 | ✘           |    0    |
| 30 | aten.sym_size.int       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 31 | aten.t.default          |                  4 |           3 |         0 |          0 | 🚧          |    0.75 |
| 32 | aten.transpose.int      |                  8 |           3 |         0 |          0 | 🚧          |    0.38 |
| 33 | aten.unsqueeze.default  |                 24 |           7 |         0 |          4 | 🚧          |    0.29 |
| 34 | aten.view.default       |                 35 |          11 |         0 |          0 | 🚧          |    0.31 |
| 35 | aten.where.self         |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 36 | aten.zeros.default      |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 37 | aten.zeros_like.default |                  3 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | True  |
|  1 | Tensor<[1, 12, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | True  |
|  2 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | True  |
|  3 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 12, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | Done       | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | None     | Fallback   | True  |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 1, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                             | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 1, 768]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                   | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 1, 768]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                    | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 10, 768]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | True  |
|  8 | Tensor<[1, 10, 768]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                   | Unknown  | Fallback   | True  |
|  9 | Tensor<[1, 12, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | Fallback   | True  |
| 10 | Tensor<[1, 12, 1, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | Fallback   | True  |
| 11 | Tensor<[1, 12, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | True  |
| 12 | Tensor<[1, 12, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | True  |
| 13 | Tensor<[1, 12, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | True  |
| 14 | Tensor<[1, 12, 1, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | True  |
| 15 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  | Unknown    | N/A   |
| 17 | Tensor<[1, 12, 10, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Unknown  | Fallback   | True  |
| 18 | Tensor<[1, 12, 10, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                | Unknown  | Fallback   | True  |
| 19 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                         | None     | Fallback   | True  |
| 20 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                           | None     | Fallback   | True  |
| 21 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                       | None     | Fallback   | True  |
| 22 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                         | None     | Fallback   | True  |
| 23 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                         | Unknown  | Fallback   | True  |
| 24 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                           | Unknown  | Fallback   | True  |
| 25 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                               | Unknown  | Unknown    | N/A   |
| 26 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                 | Unknown  | Unknown    | N/A   |
### aten.abs.default
|    | ATen Input Variations     | Status   | Isolated   | PCC   |
|---:|:--------------------------|:---------|:-----------|:------|
|  0 | Tensor<[10, 10]> self = ? | Fallback | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?               | Unknown  | Done       | True  |
|  2 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                         | Done     | Done       | True  |
|  3 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?             | Done     | Done       | True  |
|  4 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | True  |
|  5 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?         | Unknown  | Done       | True  |
|  6 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?            | Unknown  | Done       | True  |
|  7 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?           | Unknown  | Done       | True  |
|  8 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?            | Unknown  | Done       | True  |
|  9 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?           | Unknown  | Done       | True  |
| 10 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?         | Done     | Done       | True  |
| 13 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?       | Done     | Done       | True  |
| 14 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                 | Fallback | Done       | True  |
| 15 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                | Fallback | Done       | True  |
| 16 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                               | Done     | Done       | True  |
| 17 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                               | Fallback | Done       | True  |
| 18 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                     | Fallback | Done       | True  |
| 19 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                 | Unknown  | Done       | True  |
| 20 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | True  |
| 21 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                       | Unknown  | Unknown    | N/A   |
| 22 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                      | Unknown  | Unknown    | N/A   |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | None     | Fallback   | True  |
|  1 | number end = 1,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | None     | Fallback   | True  |
|  2 | number end = 10,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | None     | Fallback   | True  |
|  3 | number end = 2,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Fallback   | True  |
|  4 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
### aten.bmm.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 1, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?         | Unknown  | Done       | True  |
|  1 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?           | Unknown  | Done       | True  |
|  2 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?           | Unknown  | Done       | True  |
|  3 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?         | Unknown  | Done       | True  |
|  4 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?          | Unknown  | Done       | True  |
|  5 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?          | Unknown  | Done       | True  |
|  6 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?     | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A   |
|  8 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?        | Done     | Done       | True  |
|  9 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?        | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 1]>, <[1, 1, 1]>],<br>int dim = -1           | Unknown  | Fallback   | True  |
|  1 | List[Tensor] tensors = [<[1, 1, s0]>, <[1, 1, 1]>],<br>int dim = -1          | Unknown  | Unknown    | N/A   |
|  2 | List[Tensor] tensors = [<[1, 12, 1, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2  | Unknown  | Fallback   | True  |
|  3 | List[Tensor] tensors = [<[1, 12, s0, 64]>, <[1, 12, 1, 64]>],<br>int dim = 2 | Unknown  | Unknown    | N/A   |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 3072]> self = ?                                                              | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 768]> self = ?                                                               | Unknown  | Done       | True  |
|  2 | Tensor<[1, 10, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  3 | Tensor<[1, 10, 3072]> self = ?                                                             | Done     | Done       | True  |
|  4 | Tensor<[1, 10, 768]> self = ?                                                              | Fallback | Done       | True  |
|  5 | Tensor<[1, 12, 1, 10]> self = ?                                                            | Unknown  | Done       | True  |
|  6 | Tensor<[1, 12, 1, 1]> self = ?                                                             | Unknown  | Done       | True  |
|  7 | Tensor<[1, 12, 1, 2]> self = ?                                                             | Unknown  | Done       | True  |
|  8 | Tensor<[1, 12, 1, s0 + 1]> self = ?                                                        | Unknown  | Unknown    | N/A   |
|  9 | Tensor<[1, 12, 10, 10]> self = ?                                                           | Done     | Done       | True  |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                           | None     | Fallback   | True  |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357           | None     | Fallback   | True  |
|  2 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781          | Done     | Done       | True  |
|  3 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                          | None     | Fallback   | True  |
|  4 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                           | Unknown  | Fallback   | True  |
|  5 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | Done       | True  |
|  6 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                 | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357 | Unknown  | Unknown    | N/A   |
### aten.embedding.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?           | None     | Fallback   | True  |
|  1 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?         | None     | Fallback   | True  |
|  2 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?           | Unknown  | Fallback   | True  |
|  3 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ? | Unknown  | Unknown    | N/A   |
|  4 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?      | None     | Fallback   | True  |
|  5 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?       | Unknown  | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                                           | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]             | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]               | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]               | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]             | Unknown  | Fallback   | True  |
|  4 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   |
|  5 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]           | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]           | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [1, 12, 2, 64]             | Unknown  | Fallback   | True  |
|  8 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [1, 12, 64, 10]           | Unknown  | Fallback   | True  |
|  9 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [1, 12, 64, 1]             | Unknown  | Fallback   | True  |
| 10 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [1, 12, 64, 2]             | Unknown  | Fallback   | True  |
| 11 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 12, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   |
### aten.full_like.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | None     | Fallback   | True  |
|  1 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False         | None     | Fallback   | True  |
|  2 | Tensor<[2, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Fallback   | True  |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | None     | Fallback   | True  |
### aten.log.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   |
|---:|:----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?           | None     | Fallback   | True  |
|  1 | Tensor<[10, 10]> self = ?         | None     | Fallback   | True  |
|  2 | Tensor<[2, 2]> self = ?           | Unknown  | Fallback   | True  |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   |
### aten.lt.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16           | None     | Fallback   | True  |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8          | None     | Fallback   | True  |
|  2 | Tensor<[2, 2]> self = ?,<br>number other = 16           | Unknown  | Fallback   | True  |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | Unknown    | N/A   |
### aten.mean.dim
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True  | Unknown  | Done       | True  |
|  1 | Tensor<[1, 10, 768]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Done     | Done       | True  |
### aten.minimum.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                     | Done     | Done       | True  |
|  1 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                 | Done     | Done       | True  |
|  2 | Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                     | Unknown  | Done       | True  |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?  | Unknown  | Done       | True  |
|  1 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?   | Unknown  | Done       | True  |
|  2 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 32128]> mat2 = ?  | Unknown  | Done       | True  |
|  3 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | True  |
|  4 | Tensor<[10, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | True  |
|  5 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Done     | Done       | True  |
|  6 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Fallback | Done       | True  |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Fallback | Done       | True  |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Fallback | Done       | True  |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | True  |
|  4 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | True  |
|  5 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161           | Unknown  | Done       | True  |
|  8 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | True  |
|  9 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Done     | Done       | True  |
| 10 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Fallback | Done       | True  |
| 11 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Fallback | Done       | True  |
| 12 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                               | Done     | Done       | True  |
| 13 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Fallback | Done       | True  |
| 14 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | True  |
| 15 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                      | Unknown  | Done       | True  |
| 16 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                     | Done     | Done       | True  |
| 17 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A   |
### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   |
|---:|:----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?           | Fallback | Done       | True  |
|  1 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | True  |
|  2 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   |
### aten.ones.default
|    | ATen Input Variations                                                                                                                         | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  | Fallback   | True  |
|  1 | List[int] size = [1, 1, <s0>],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
|  2 | List[int] size = [1, 1],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Fallback   | True  |
|  3 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | None     | Fallback   | True  |
|  4 | List[int] size = [1, 2],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Done       | True  |
|  5 | List[int] size = [1, <s0 + 1>],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  | Unknown    | N/A   |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1]           | Done     | Done       | True  |
|  1 | Tensor<[10, 10, 12]> self = ?,<br>List[int] dims = [2, 0, 1]         | Done     | Done       | True  |
|  2 | Tensor<[2, 2, 12]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | Done       | True  |
|  3 | Tensor<[s0 + 1, s0 + 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1] | Unknown  | Unknown    | N/A   |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>number exponent = 2  | Unknown  | Done       | True  |
|  1 | Tensor<[1, 10, 768]> self = ?,<br>number exponent = 2 | Done     | Done       | True  |
### aten.relu.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 3072]> self = ?  | Unknown  | Done       | True  |
|  1 | Tensor<[1, 10, 3072]> self = ? | Done     | Done       | True  |
### aten.repeat.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | Fallback   | True  |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   | PCC   |
|---:|:----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1]> self = ?  | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 10, 1]> self = ? | Done     | Done       | True  |
### aten.rsub.Scalar
|    | ATen Input Variations                                     | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0     | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0      | None     | Fallback   | True  |
|  2 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0      | Unknown  | Done       | True  |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A   |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                             | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Fallback   | True  |
|  4 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  8 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
|  9 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Fallback   | True  |
| 10 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   |
| 11 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 12 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | Fallback   | True  |
| 13 | Tensor<[1, 12, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Fallback   | True  |
| 14 | Tensor<[1, 12, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Fallback   | True  |
| 15 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   |
| 16 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Fallback   | True  |
| 17 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Fallback   | True  |
| 18 | Tensor<[1, 12, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | True  |
| 19 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Fallback   | True  |
| 20 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Fallback   | True  |
| 21 | Tensor<[1, 12, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Done       | True  |
| 22 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   |
| 23 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   |
| 24 | Tensor<[1, 12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   |
| 25 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   |
| 26 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   |
| 27 | Tensor<[1, 12, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   |
| 28 | Tensor<[1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 29 | Tensor<[1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 30 | Tensor<[1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 31 | Tensor<[1, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                   | Unknown  | Fallback   | True  |
| 32 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   |
| 33 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   |
| 34 | Tensor<[10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Fallback   | True  |
| 35 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 36 | Tensor<[2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                      | Unknown  | Fallback   | True  |
| 37 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?         | None     | Fallback   | True  |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Fallback | Done       | True  |
|  2 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?           | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ? | Unknown  | Unknown    | N/A   |
### aten.sym_size.int
|    | ATen Input Variations                                | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3072, 768]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[32128, 768]> self = ? | Unknown  | Done       | True  |
|  2 | Tensor<[768, 3072]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[768, 768]> self = ?   | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | True  |
|  1 | Tensor<[1, 10, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | True  |
|  2 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | True  |
|  3 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | True  |
|  4 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | True  |
|  5 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Done     | Done       | True  |
|  6 | Tensor<[1, 12, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | True  |
|  7 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   |
### aten.unsqueeze.default
|    | ATen Input Variations                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2           | Fallback | Done       | True  |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 1            | Done     | Done       | True  |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2            | Done     | Done       | True  |
|  3 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1            | Unknown  | Done       | True  |
|  4 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 2            | Unknown  | Done       | True  |
|  5 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1       | Unknown  | Unknown    | N/A   |
|  6 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2       | Unknown  | Unknown    | N/A   |
|  7 | Tensor<[1, 10]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  8 | Tensor<[1, 1]> self = ?,<br>int dim = 1               | Done     | Done       | True  |
|  9 | Tensor<[1, 1]> self = ?,<br>int dim = 2               | Fallback | Done       | True  |
| 10 | Tensor<[1, 2]> self = ?,<br>int dim = 1               | Unknown  | Done       | True  |
| 11 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1          | Unknown  | Unknown    | N/A   |
| 12 | Tensor<[10]> self = ?,<br>int dim = 0                 | Fallback | Done       | True  |
| 13 | Tensor<[10]> self = ?,<br>int dim = 1                 | None     | Fallback   | True  |
| 14 | Tensor<[12, 1, 1]> self = ?,<br>int dim = 0           | Fallback | Done       | True  |
| 15 | Tensor<[12, 10, 10]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 16 | Tensor<[12, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | True  |
| 17 | Tensor<[12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   |
| 18 | Tensor<[1]> self = ?,<br>int dim = 0                  | Done     | Done       | True  |
| 19 | Tensor<[1]> self = ?,<br>int dim = 1                  | Done     | Done       | True  |
| 20 | Tensor<[2]> self = ?,<br>int dim = 0                  | Unknown  | Done       | True  |
| 21 | Tensor<[2]> self = ?,<br>int dim = 1                  | Unknown  | Fallback   | True  |
| 22 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0             | Unknown  | Unknown    | N/A   |
| 23 | Tensor<[s0 + 1]> self = ?,<br>int dim = 1             | Unknown  | Unknown    | N/A   |
### aten.view.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]            | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 3072]> self = ?,<br>List[int] size = [1, 3072]                 | Unknown  | Done       | True  |
|  2 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]            | Unknown  | Done       | True  |
|  3 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [1, 768]                   | Unknown  | Done       | True  |
|  4 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] size = [1, -1, 768]           | Done     | Done       | True  |
|  5 | Tensor<[1, 10, 3072]> self = ?,<br>List[int] size = [10, 3072]               | Done     | Done       | True  |
|  6 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64]           | Done     | Done       | True  |
|  7 | Tensor<[1, 10, 768]> self = ?,<br>List[int] size = [10, 768]                 | Done     | Done       | True  |
|  8 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                       | None     | Fallback   | True  |
|  9 | Tensor<[1, 12, 1, 10]> self = ?,<br>List[int] size = [12, 1, 10]             | Unknown  | Done       | True  |
| 10 | Tensor<[1, 12, 1, 1]> self = ?,<br>List[int] size = [12, 1, 1]               | Unknown  | Done       | True  |
| 11 | Tensor<[1, 12, 1, 2]> self = ?,<br>List[int] size = [12, 1, 2]               | Unknown  | Done       | True  |
| 12 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] size = [12, 1, 64]             | Unknown  | Done       | True  |
| 13 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>List[int] size = [12, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   |
| 14 | Tensor<[1, 12, 10, 10]> self = ?,<br>List[int] size = [12, 10, 10]           | Done     | Done       | True  |
| 15 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] size = [12, 10, 64]           | Done     | Done       | True  |
| 16 | Tensor<[1, 12, 2, 64]> self = ?,<br>List[int] size = [12, 2, 64]             | Unknown  | Done       | True  |
| 17 | Tensor<[1, 12, 64, 10]> self = ?,<br>List[int] size = [12, 64, 10]           | Done     | Done       | True  |
| 18 | Tensor<[1, 12, 64, 1]> self = ?,<br>List[int] size = [12, 64, 1]             | Unknown  | Done       | True  |
| 19 | Tensor<[1, 12, 64, 2]> self = ?,<br>List[int] size = [12, 64, 2]             | Unknown  | Done       | True  |
| 20 | Tensor<[1, 12, 64, s0 + 1]> self = ?,<br>List[int] size = [12, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   |
| 21 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>List[int] size = [12, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   |
| 22 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                         | Unknown  | Fallback   | True  |
| 23 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [1, 1, 3072]                 | Unknown  | Done       | True  |
| 24 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]               | Unknown  | Done       | True  |
| 25 | Tensor<[1, 768]> self = ?,<br>List[int] size = [1, 1, 768]                   | Unknown  | Done       | True  |
| 26 | Tensor<[10, 3072]> self = ?,<br>List[int] size = [1, 10, 3072]               | Done     | Done       | True  |
| 27 | Tensor<[10, 768]> self = ?,<br>List[int] size = [1, 10, 768]                 | Done     | Done       | True  |
| 28 | Tensor<[12, 1, 10]> self = ?,<br>List[int] size = [1, 12, 1, 10]             | Unknown  | Done       | True  |
| 29 | Tensor<[12, 1, 1]> self = ?,<br>List[int] size = [1, 12, 1, 1]               | Unknown  | Done       | True  |
| 30 | Tensor<[12, 1, 2]> self = ?,<br>List[int] size = [1, 12, 1, 2]               | Unknown  | Done       | True  |
| 31 | Tensor<[12, 1, 64]> self = ?,<br>List[int] size = [1, 12, 1, 64]             | Unknown  | Done       | True  |
| 32 | Tensor<[12, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 12, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   |
| 33 | Tensor<[12, 10, 10]> self = ?,<br>List[int] size = [1, 12, 10, 10]           | Done     | Done       | True  |
| 34 | Tensor<[12, 10, 64]> self = ?,<br>List[int] size = [1, 12, 10, 64]           | Done     | Done       | True  |
### aten.where.self
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                               | Done     | Done       | True  |
|  1 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                         | Done     | Done       | True  |
|  2 | Tensor<[2, 2]> condition = ?,<br>Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                               | Unknown  | Done       | True  |
|  3 | Tensor<[s0 + 1, s0 + 1]> condition = ?,<br>Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [1, 12, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | True  |
|  1 | List[int] size = [1, 12, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | True  |
|  2 | List[int] size = [1, 12, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
### aten.zeros_like.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False           | None     | Fallback   | True  |
|  1 | Tensor<[2, 2]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | True  |
|  2 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |

