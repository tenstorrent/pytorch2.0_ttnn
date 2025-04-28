# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default   |                  5 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default   |                 27 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.abs.default        |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor         |                 23 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.arange.default     |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bmm.default        |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.cat.default        |                  4 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.clone.default      |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.div.Tensor         |                  8 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.embedding.default  |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.expand.default     |                 13 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.full_like.default  |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.gt.Scalar          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.le.Tensor          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.log.default        |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.lt.Scalar          |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.mean.dim           |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.minimum.default    |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.mm.default         |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.mul.Tensor         |                 17 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.neg.default        |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.ones.default       |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.permute.default    |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.pow.Tensor_Scalar  |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.relu.default       |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.repeat.default     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.rsqrt.default      |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.rsub.Scalar        |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.slice.Tensor       |                 32 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.sub.Tensor         |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.sym_size.int       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.t.default          |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.transpose.int      |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.unsqueeze.default  |                 21 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.view.default       |                 35 |           0 |         0 |          0 | ✘           |       0 |
| 35 | aten.where.self         |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 36 | aten.zeros.default      |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 37 | aten.zeros_like.default |                  3 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9996093731601781 | -1     |
|  1 | Tensor<[1, 8, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 1.0                | -1     |
|  2 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9991710762280672 | -1     |
|  3 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 8, 10, 10]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Done       | 0.9996560072670619 | -1     |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                     | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 1, 512]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 1, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                   | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 10, 512]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
|  8 | Tensor<[1, 10, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  9 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                          | Unknown  | Fallback   | 1.0   | -1     |
| 11 | Tensor<[1, 8, 1, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | Fallback   | 1.0   | -1     |
| 12 | Tensor<[1, 8, 1, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
| 13 | Tensor<[1, 8, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 14 | Tensor<[1, 8, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 15 | Tensor<[1, 8, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 16 | Tensor<[1, 8, 1, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 17 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 8, 10, 10]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Unknown  | Fallback   | 1.0   | -1     |
| 20 | Tensor<[1, 8, 10, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                | Unknown  | Fallback   | 1.0   | -1     |
| 21 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Unknown  | Fallback   | 1.0   | -1     |
| 22 | Tensor<[10, 10]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
| 23 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
| 24 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                          | Unknown  | Fallback   | 1.0   | -1     |
| 25 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                | Unknown  | Unknown    | N/A   | N/A    |
### aten.abs.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10, 10]> self = ? | Unknown  | Done       |     1 |     -1 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                        | Unknown  | Done       | 1.0                | -1     |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?             | Unknown  | Done       | 0.9999982345471026 | -1     |
|  2 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  | Done       | 1.0                | -1     |
|  3 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?           | Unknown  | Done       | 0.9999979913323888 | -1     |
|  4 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                               | Unknown  | Done       | 1.0                | -1     |
|  5 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                              | Unknown  | Done       | 1.0                | -1     |
|  6 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?         | Unknown  | Done       | 0.9999989773126583 | -1     |
|  7 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?         | Unknown  | Done       | 0.9999985258398209 | -1     |
|  8 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?           | Unknown  | Done       | 1.0                | -1     |
|  9 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?           | Unknown  | Done       | 1.0                | -1     |
| 10 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?           | Unknown  | Done       | 1.0                | -1     |
| 11 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?           | Unknown  | Done       | 1.0                | -1     |
| 12 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?        | Unknown  | Done       | 0.9999978837161538 | -1     |
| 15 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?       | Unknown  | Done       | 0.999997941661275  | -1     |
| 16 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                             | Unknown  | Done       | 1.0                | -1     |
| 17 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                             | Unknown  | Done       | 0.9999126654931606 | -1     |
| 18 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                   | Unknown  | Done       | 0.99999750630306   | -1     |
| 19 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                               | Unknown  | Done       | 1.0                | -1     |
| 20 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                              | Unknown  | Done       | 1.0                | -1     |
| 21 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                     | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                    | Unknown  | Unknown    | N/A                | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[8, 1, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?         | Unknown  | Done       | 0.999992165138328  | -1     |
|  1 | Tensor<[8, 1, 1]> self = ?,<br>Tensor<[8, 1, 64]> mat2 = ?           | Unknown  | Done       | 0.9999972180688906 | -1     |
|  2 | Tensor<[8, 1, 2]> self = ?,<br>Tensor<[8, 2, 64]> mat2 = ?           | Unknown  | Done       | 0.9999916501205756 | -1     |
|  3 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?         | Unknown  | Done       | 0.9999873372965735 | -1     |
|  4 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 1]> mat2 = ?          | Unknown  | Done       | 0.9999975672600352 | -1     |
|  5 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 2]> mat2 = ?          | Unknown  | Done       | 0.9999908799173123 | -1     |
|  6 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, s0 + 1]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[8, 1, s0 + 1]> self = ?,<br>Tensor<[8, s0 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[8, 10, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?        | Unknown  | Done       | 0.9999912982090731 | -1     |
|  9 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?        | Unknown  | Done       | 0.9999855595899058 | -1     |
### aten.cat.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, s0]>, <[1, 1, 1]>],<br>int dim = -1        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 8, 1, 64]>, <[1, 8, 1, 64]>],<br>int dim = 2  | Unknown  | Done       | 1.0   | -1     |
|  2 | List[Tensor] tensors = [<[1, 8, s0, 64]>, <[1, 8, 1, 64]>],<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[Tensor] tensors = [_folded_ones_1, <[1, 1, 1]>],<br>int dim = -1      | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048]> self = ?                                                             | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 512]> self = ?                                                              | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 10, 2048]> self = ?                                                            | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 10, 512]> self = ?                                                             | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 10, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 8, 1, 10]> self = ?                                                            | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 8, 1, 1]> self = ?                                                             | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 8, 1, 2]> self = ?                                                             | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 8, 1, s0 + 1]> self = ?                                                        | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 8, 10, 10]> self = ?                                                           | Unknown  | Done       | 1.0   | -1     |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                           | Unknown  | Done       | 1.0                | -1     |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | Done       | 1.0                | -1     |
|  2 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781          | Unknown  | Done       | 0.9999964882265104 | -1     |
|  3 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                          | Unknown  | Done       | 1.0                | -1     |
|  4 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                           | Unknown  | Done       | 1.0                | -1     |
|  5 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | Done       | 0.9999970367304378 | -1     |
|  6 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                 | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357 | Unknown  | Unknown    | N/A                | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 8]> weight = ?,<br>Tensor<[1, 1]> indices = ?           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[32, 8]> weight = ?,<br>Tensor<[10, 10]> indices = ?         | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[32, 8]> weight = ?,<br>Tensor<[2, 2]> indices = ?           | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[32, 8]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ? | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?     | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?      | Unknown  | Done       | 1.0   | -1     |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]             | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]               | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]               | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]           | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]           | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [1, 8, 2, 64]             | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [1, 8, 64, 10]           | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [1, 8, 64, 1]             | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [1, 8, 64, 2]             | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 8, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
### aten.full_like.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[2, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[10, 10]> self = ?,<br>number other = 0 | Unknown  | Done       |     1 |     -1 |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | Unknown  | Fallback   |     1 |     -1 |
### aten.log.default
|    | ATen Input Variations             | Status   | Isolated   | PCC                  | Host   |
|---:|:----------------------------------|:---------|:-----------|:---------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?           | Unknown  | Done       | 0.0                  | -1     |
|  1 | Tensor<[10, 10]> self = ?         | Unknown  | Done       | -0.16670943022527607 | -1     |
|  2 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | 0.09131065275870258  | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A                  | N/A    |
### aten.lt.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[10, 10]> self = ?,<br>number other = 8          | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[2, 2]> self = ?,<br>number other = 16           | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True  | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 10, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  | Done       |     1 |     -1 |
### aten.minimum.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                     | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                 | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                     | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Unknown  | Done       | 0.999948 |     -1 |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?   | Unknown  | Done       | 0.999972 |     -1 |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 32128]> mat2 = ?  | Unknown  | Done       | 0.999972 |     -1 |
|  3 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?    | Unknown  | Done       | 0.999969 |     -1 |
|  4 | Tensor<[10, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ? | Unknown  | Done       | 0.999954 |     -1 |
|  5 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Unknown  | Done       | 0.999971 |     -1 |
|  6 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?   | Unknown  | Done       | 0.999971 |     -1 |
### aten.mul.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  | Done       | 0.9999958796788917 | -1     |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 1.0                | -1     |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | -1     |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 1.0                | -1     |
|  4 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 1.0                | -1     |
|  5 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922           | Unknown  | Done       | 0.9999951246434653 | -1     |
|  8 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999968931756343 | -1     |
|  9 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  | Done       | 0.9999958077690518 | -1     |
| 10 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | -1     |
| 11 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 1.0                | -1     |
| 12 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 1.0                | -1     |
| 13 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | -1     |
| 14 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                      | Unknown  | Done       | 0.9999974943252419 | -1     |
| 15 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                     | Unknown  | Done       | 0.9999957606890493 | -1     |
| 16 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |
### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.ones.default
|    | ATen Input Variations                                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 1, <s0>],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [1, <s0 + 1>],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 8]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[10, 10, 8]> self = ?,<br>List[int] dims = [2, 0, 1]         | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[2, 2, 8]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1, 8]> self = ?,<br>List[int] dims = [2, 0, 1] | Unknown  | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 512]> self = ?,<br>number exponent = 2  | Unknown  | Done       | 0.999993 |     -1 |
|  1 | Tensor<[1, 10, 512]> self = ?,<br>number exponent = 2 | Unknown  | Done       | 0.999994 |     -1 |
### aten.relu.default
|    | ATen Input Variations          | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 2048]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 10, 2048]> self = ? | Unknown  | Done       |     1 |     -1 |
### aten.repeat.default
|    | ATen Input Variations                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | Done       |     1 |     -1 |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?  | Unknown  | Done       | 0        |     -1 |
|  1 | Tensor<[1, 10, 1]> self = ? | Unknown  | Done       | 0.999998 |     -1 |
### aten.rsub.Scalar
|    | ATen Input Variations                                     | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999965692460262 | -1     |
|  1 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 1.0                | -1     |
|  2 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 1.0                | -1     |
|  3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 8, 1, 10]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 8, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 16 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 19 | Tensor<[1, 8, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 8, 3, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Done       | 1.0   | -1     |
| 23 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 8, s0 + 2, 10]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?         | Unknown  | Done       | 0.718909331679292  | -1     |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Done       | 1.0                | -1     |
|  2 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?           | Unknown  | Done       | 0.9780852544773829 | -1     |
|  3 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
### aten.sym_size.int
|    | ATen Input Variations                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2048, 512]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  1 | Tensor<[32128, 512]> self = ? | Unknown  | Done       |     1 |     -1 |
|  2 | Tensor<[512, 2048]> self = ?  | Unknown  | Done       |     1 |     -1 |
|  3 | Tensor<[512, 512]> self = ?   | Unknown  | Done       |     1 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 10, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 8, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 8, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 8, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2          | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 1           | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1           | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1      | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 10]> self = ?,<br>int dim = 1             | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 1]> self = ?,<br>int dim = 1              | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 1]> self = ?,<br>int dim = 2              | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 2]> self = ?,<br>int dim = 1              | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1         | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[10]> self = ?,<br>int dim = 1                | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1]> self = ?,<br>int dim = 1                 | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[2]> self = ?,<br>int dim = 1                 | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[8, 1, 1]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | -1     |
| 16 | Tensor<[8, 10, 10]> self = ?,<br>int dim = 0         | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[8, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | -1     |
| 18 | Tensor<[8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0            | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[s0 + 1]> self = ?,<br>int dim = 1            | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 2048]> self = ?,<br>List[int] size = [1, 2048]               | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, -1, 8, 64]           | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                 | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 1, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]           | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 10, 2048]> self = ?,<br>List[int] size = [10, 2048]             | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [1, -1, 8, 64]          | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 10, 512]> self = ?,<br>List[int] size = [10, 512]               | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 10, 8, 64]> self = ?,<br>List[int] size = [1, -1, 512]          | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 10]> self = ?,<br>List[int] size = [-1, 10]                     | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                       | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [1, 1, 2048]               | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]             | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                 | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 8, 1, 10]> self = ?,<br>List[int] size = [8, 1, 10]             | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 8, 1, 1]> self = ?,<br>List[int] size = [8, 1, 1]               | Unknown  | Done       | 1.0   | -1     |
| 15 | Tensor<[1, 8, 1, 2]> self = ?,<br>List[int] size = [8, 1, 2]               | Unknown  | Done       | 1.0   | -1     |
| 16 | Tensor<[1, 8, 1, 64]> self = ?,<br>List[int] size = [8, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>List[int] size = [8, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 8, 10, 10]> self = ?,<br>List[int] size = [8, 10, 10]           | Unknown  | Done       | 1.0   | -1     |
| 19 | Tensor<[1, 8, 10, 64]> self = ?,<br>List[int] size = [8, 10, 64]           | Unknown  | Done       | 1.0   | -1     |
| 20 | Tensor<[1, 8, 2, 64]> self = ?,<br>List[int] size = [8, 2, 64]             | Unknown  | Done       | 1.0   | -1     |
| 21 | Tensor<[1, 8, 64, 10]> self = ?,<br>List[int] size = [8, 64, 10]           | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 8, 64, 1]> self = ?,<br>List[int] size = [8, 64, 1]             | Unknown  | Done       | 1.0   | -1     |
| 23 | Tensor<[1, 8, 64, 2]> self = ?,<br>List[int] size = [8, 64, 2]             | Unknown  | Done       | 1.0   | -1     |
| 24 | Tensor<[1, 8, 64, s0 + 1]> self = ?,<br>List[int] size = [8, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>List[int] size = [8, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[10, 2048]> self = ?,<br>List[int] size = [1, 10, 2048]             | Unknown  | Done       | 1.0   | -1     |
| 27 | Tensor<[10, 512]> self = ?,<br>List[int] size = [1, 10, 512]               | Unknown  | Done       | 1.0   | -1     |
| 28 | Tensor<[8, 1, 10]> self = ?,<br>List[int] size = [1, 8, 1, 10]             | Unknown  | Done       | 1.0   | -1     |
| 29 | Tensor<[8, 1, 1]> self = ?,<br>List[int] size = [1, 8, 1, 1]               | Unknown  | Done       | 1.0   | -1     |
| 30 | Tensor<[8, 1, 2]> self = ?,<br>List[int] size = [1, 8, 1, 2]               | Unknown  | Done       | 1.0   | -1     |
| 31 | Tensor<[8, 1, 64]> self = ?,<br>List[int] size = [1, 8, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
| 32 | Tensor<[8, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 8, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[8, 10, 10]> self = ?,<br>List[int] size = [1, 8, 10, 10]           | Unknown  | Done       | 1.0   | -1     |
| 34 | Tensor<[8, 10, 64]> self = ?,<br>List[int] size = [1, 8, 10, 64]           | Unknown  | Done       | 1.0   | -1     |
### aten.where.self
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                               | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[10, 10]> condition = ?,<br>Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                         | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[2, 2]> condition = ?,<br>Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                               | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[s0 + 1, s0 + 1]> condition = ?,<br>Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 8, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | -1     |
|  1 | List[int] size = [1, 8, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | -1     |
|  2 | List[int] size = [1, 8, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros_like.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[2, 2]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |

