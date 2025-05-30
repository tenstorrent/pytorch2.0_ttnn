# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default   |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default   |                 32 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten.abs.default        |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.add.Tensor         |                 31 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.arange.default     |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.bmm.default        |                 12 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.cat.default        |                  6 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.clone.default      |                 11 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.div.Tensor         |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.embedding.default  |                  7 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.expand.default     |                 16 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.full_like.default  |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.gt.Scalar          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.le.Tensor          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.log.default        |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.lt.Scalar          |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.mean.dim           |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.minimum.default    |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.mm.default         |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.mul.Tensor         |                 27 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.neg.default        |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.ones.default       |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.permute.default    |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.pow.Tensor_Scalar  |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.repeat.default     |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.rsqrt.default      |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.rsub.Scalar        |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.slice.Tensor       |                 43 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.sub.Tensor         |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.sym_size.int       |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.t.default          |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.tanh.default       |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.transpose.int      |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.unsqueeze.default  |                 26 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.view.default       |                 43 |           0 |         0 |          0 | ✘           |       0 |
| 35 | aten.where.self         |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 36 | aten.zeros.default      |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 37 | aten.zeros_like.default |                  4 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9997450206753418 | 0      |
|  1 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9994717181488434 | 0      |
|  2 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9994868075423916 | 0      |
|  4 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Done       | 0.9996286950383058 | 0      |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1, 1, 17]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                     | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 1, 512]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 1, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                   | Unknown  | Fallback   | 1.0   | -1     |
|  8 | Tensor<[1, 15, 512]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
|  9 | Tensor<[1, 15, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
| 11 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                          | Unknown  | Fallback   | 1.0   | -1     |
| 12 | Tensor<[1, 6, 1, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | Fallback   | 1.0   | -1     |
| 13 | Tensor<[1, 6, 1, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
| 14 | Tensor<[1, 6, 1, 17]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | Fallback   | 1.0   | -1     |
| 15 | Tensor<[1, 6, 1, 17]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
| 16 | Tensor<[1, 6, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 17 | Tensor<[1, 6, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 18 | Tensor<[1, 6, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 19 | Tensor<[1, 6, 1, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 20 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 6, 15, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Unknown  | Fallback   | 1.0   | -1     |
| 23 | Tensor<[1, 6, 15, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                | Unknown  | Fallback   | 1.0   | -1     |
| 24 | Tensor<[15, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Unknown  | Fallback   | 1.0   | -1     |
| 25 | Tensor<[15, 15]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
| 26 | Tensor<[17, 17]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Unknown  | Fallback   | 1.0   | -1     |
| 27 | Tensor<[17, 17]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
| 28 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
| 29 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                          | Unknown  | Fallback   | 1.0   | -1     |
| 30 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                | Unknown  | Unknown    | N/A   | N/A    |
### aten.abs.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[15, 15]> self = ? | Unknown  | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                       | Unknown  | Done       | 0.9999957200976748 | 0      |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?           | Unknown  | Done       | 0.9999976607859195 | 0      |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                        | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?             | Unknown  | Done       | 0.9999983433784767 | 0      |
|  4 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                      | Unknown  | Done       | 0.9999948340385814 | 0      |
|  5 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?         | Unknown  | Done       | 0.9999980178631364 | 0      |
|  6 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  | Done       | 1.0                | 0      |
|  7 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?           | Unknown  | Done       | 0.9999980205336273 | 0      |
|  8 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                               | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                              | Unknown  | Done       | 1.0                | 0      |
| 10 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?         | Unknown  | Done       | 0.9999969441632407 | 0      |
| 11 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?         | Unknown  | Done       | 0.9999981294082922 | 0      |
| 12 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?         | Unknown  | Done       | 0.9999981553683513 | 0      |
| 13 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?         | Unknown  | Done       | 0.9999989205866502 | 0      |
| 14 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?           | Unknown  | Done       | 1.0                | 0      |
| 15 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?           | Unknown  | Done       | 1.0                | 0      |
| 16 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?           | Unknown  | Done       | 0.9999953867930481 | 0      |
| 17 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?           | Unknown  | Done       | 0.9999980583137815 | 0      |
| 18 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 19 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 20 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?        | Unknown  | Done       | 0.9999978029556253 | 0      |
| 21 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?       | Unknown  | Done       | 0.9999977736026043 | 0      |
| 22 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                             | Unknown  | Done       | 1.0                | 0      |
| 23 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                             | Unknown  | Done       | 0.9998762975015592 | 0      |
| 24 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                   | Unknown  | Done       | 0.9999986977082914 | 0      |
| 25 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                             | Unknown  | Done       | 1.0                | 0      |
| 26 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 0.9995824308144986 | 0      |
| 27 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                               | Unknown  | Done       | 1.0                | 0      |
| 28 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                              | Unknown  | Done       | 1.0                | 0      |
| 29 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                     | Unknown  | Unknown    | N/A                | N/A    |
| 30 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                    | Unknown  | Unknown    | N/A                | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?         | Unknown  | Done       | 0.9999905663189702 | 0      |
|  1 | Tensor<[6, 1, 17]> self = ?,<br>Tensor<[6, 17, 64]> mat2 = ?         | Unknown  | Done       | 0.9999867738448412 | 0      |
|  2 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?           | Unknown  | Done       | 0.9999917460483131 | 0      |
|  3 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?           | Unknown  | Done       | 0.9999910898252775 | 0      |
|  4 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?         | Unknown  | Done       | 0.9999896206723551 | 0      |
|  5 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 17]> mat2 = ?         | Unknown  | Done       | 0.9999855032756101 | 0      |
|  6 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?          | Unknown  | Done       | 0.9999985215725167 | 0      |
|  7 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?          | Unknown  | Done       | 0.9999833553831768 | 0      |
|  8 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?        | Unknown  | Done       | 0.9999915128114115 | 0      |
| 11 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?        | Unknown  | Done       | 0.9999855263975547 | 0      |
### aten.cat.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 1, s0]>, <[1, 1, 1]>],<br>int dim = -1        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 6, 1, 64]>, <[1, 6, 1, 64]>],<br>int dim = 2  | Unknown  | Done       | 1.0   | 0      |
|  2 | List[Tensor] tensors = [<[1, 6, 16, 64]>, <[1, 6, 1, 64]>],<br>int dim = 2 | Unknown  | Done       | 1.0   | 0      |
|  3 | List[Tensor] tensors = [<[1, 6, s0, 64]>, <[1, 6, 1, 64]>],<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[Tensor] tensors = [_folded_ones, <[1, 1, 1]>],<br>int dim = -1        | Unknown  | Unknown    | N/A   | N/A    |
|  5 | List[Tensor] tensors = [_folded_ones_1, <[1, 1, 1]>],<br>int dim = -1      | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 512]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 15, 1024]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 15, 512]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 6, 1, 15]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 6, 1, 17]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 6, 1, 1]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 6, 1, 2]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 6, 1, s0 + 1]> self = ?                                                        | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 6, 15, 15]> self = ?                                                           | Unknown  | Done       | 1.0   | 0      |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                           | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781          | Unknown  | Done       | 0.9999961666658069 | 0      |
|  3 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                          | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                         | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357         | Unknown  | Done       | 0.9999995280552639 | 0      |
|  6 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                           | Unknown  | Done       | 1.0                | 0      |
|  7 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | Done       | 1.0                | 0      |
|  8 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                 | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357 | Unknown  | Unknown    | N/A                | N/A    |
### aten.embedding.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?           | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?         | Unknown  | Done       | 0.9532522851154814 | 0      |
|  2 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?         | Unknown  | Done       | 0.9044725812441631 | 0      |
|  3 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?           | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ? | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?     | Unknown  | Done       | 1.0                | 0      |
|  6 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?      | Unknown  | Done       | 1.0                | 0      |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]             | Unknown  | Done       | 1.0   | -1     |
|  1 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]             | Unknown  | Done       | 1.0   | -1     |
|  2 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]               | Unknown  | Done       | 1.0   | -1     |
|  3 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]               | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]           | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]           | Unknown  | Done       | 1.0   | -1     |
|  8 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [1, 6, 17, 64]           | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [1, 6, 2, 64]             | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [1, 6, 64, 15]           | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [1, 6, 64, 17]           | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [1, 6, 64, 1]             | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [1, 6, 64, 2]             | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 6, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
### aten.full_like.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[15, 15]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[17, 17]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[2, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[15, 15]> self = ?,<br>number other = 0 | Unknown  | Done       |     1 |      0 |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | Unknown  | Fallback   |     1 |     -1 |
### aten.log.default
|    | ATen Input Variations             | Status   | Isolated   | PCC                  | Host   |
|---:|:----------------------------------|:---------|:-----------|:---------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?           | Unknown  | Done       | 0.0                  | 0      |
|  1 | Tensor<[15, 15]> self = ?         | Unknown  | Done       | -0.24846408445138168 | 0      |
|  2 | Tensor<[17, 17]> self = ?         | Unknown  | Done       | -0.14814751218798022 | 0      |
|  3 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | 0.48650530030592093  | 0      |
|  4 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A                  | N/A    |
### aten.lt.Scalar
|    | ATen Input Variations                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[15, 15]> self = ?,<br>number other = 8          | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[17, 17]> self = ?,<br>number other = 16         | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[2, 2]> self = ?,<br>number other = 16           | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 15, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  | Done       |     1 |      0 |
### aten.minimum.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                     | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                 | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[17, 17]> self = ?,<br>Tensor<[17, 17]> other = ?                 | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                     | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?  | Unknown  | Done       | 0.999968 |      0 |
|  1 | Tensor<[1, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?    | Unknown  | Done       | 0.999971 |      0 |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?   | Unknown  | Done       | 0.999974 |      0 |
|  3 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 32128]> mat2 = ?  | Unknown  | Done       | 0.99997  |      0 |
|  4 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?    | Unknown  | Done       | 0.99997  |      0 |
|  5 | Tensor<[15, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Unknown  | Done       | 0.999966 |      0 |
|  6 | Tensor<[15, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?   | Unknown  | Done       | 0.999972 |      0 |
|  7 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?  | Unknown  | Done       | 0.999972 |      0 |
|  8 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?   | Unknown  | Done       | 0.999973 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  | Done       | 0.9999951085576546 | 0      |
|  1 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  | Done       | 0.9999973613221163 | 0      |
|  2 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | Done       | 0.9999994050553365 | 0      |
|  3 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 1.0                | 0      |
|  6 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 1.0                | 0      |
|  7 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
|  9 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999944810941491 | 0      |
| 10 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                | 0      |
| 11 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.999997204083732  | 0      |
| 12 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999961052816204 | 0      |
| 13 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999959933791307 | 0      |
| 14 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                    | Unknown  | Done       | 0.9999951441283497 | 0      |
| 15 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                         | Unknown  | Done       | 1.0                | 0      |
| 16 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654          | Unknown  | Done       | 0.9999971645627681 | 0      |
| 17 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Unknown  | Done       | 0.9999959389231038 | 0      |
| 18 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                | Unknown  | Done       | 0.9999966803384215 | 0      |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 20 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 1.0                | 0      |
| 21 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 1.0                | 0      |
| 22 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 1.0                | 0      |
| 23 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 24 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                      | Unknown  | Done       | 0.9999966463765841 | 0      |
| 25 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                     | Unknown  | Done       | 0.9999957435575971 | 0      |
| 26 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |
### aten.neg.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[17, 17]> self = ?         | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2]> self = ?           | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.ones.default
|    | ATen Input Variations                                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 1, <s0>],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [1, <s0 + 1>],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[15, 15, 6]> self = ?,<br>List[int] dims = [2, 0, 1]         | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[17, 17, 6]> self = ?,<br>List[int] dims = [2, 0, 1]         | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[2, 2, 6]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[s0 + 1, s0 + 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1] | Unknown  | Unknown    | N/A   | N/A    |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   | Isolated   |      PCC |   Host |
|---:|:---------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>number exponent = 3.0  | Unknown  | Done       | 0.999996 |      0 |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>number exponent = 2     | Unknown  | Done       | 0.999993 |      0 |
|  2 | Tensor<[1, 15, 1024]> self = ?,<br>number exponent = 3.0 | Unknown  | Done       | 0.999996 |      0 |
|  3 | Tensor<[1, 15, 512]> self = ?,<br>number exponent = 2    | Unknown  | Done       | 0.999994 |      0 |
### aten.repeat.default
|    | ATen Input Variations                                        | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | Done       |     1 |     -1 |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?  | Unknown  | Done       | 1        |      0 |
|  1 | Tensor<[1, 15, 1]> self = ? | Unknown  | Done       | 0.999999 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                     | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999981583643264 | 0      |
|  1 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999948799537023 | 0      |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                            | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                          | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 1, 1, 17]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1, 17]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 11 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Done       | 1.0   | -1     |
| 17 | Tensor<[1, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807         | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807         | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?         | Unknown  | Done       | 0.8008508476765747 | 0      |
|  1 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?         | Unknown  | Done       | 0.6357689012935359 | 0      |
|  2 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?           | Unknown  | Done       | 0.9878528885306047 | 0      |
|  4 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
### aten.sym_size.int
|    | ATen Input Variations                               | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1024, 512]> self = ?  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[32128, 512]> self = ? | Unknown  | Done       |     1 |      0 |
|  2 | Tensor<[384, 512]> self = ?   | Unknown  | Done       |     1 |      0 |
|  3 | Tensor<[512, 1024]> self = ?  | Unknown  | Done       |     1 |      0 |
|  4 | Tensor<[512, 384]> self = ?   | Unknown  | Done       |     1 |      0 |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.999942 |      0 |
|  1 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.999941 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 15, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 6, 17, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 6, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 15]> self = ?,<br>int dim = 2          | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 1          | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 2          | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 1           | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1           | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1      | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2      | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 15]> self = ?,<br>int dim = 1             | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 17]> self = ?,<br>int dim = 1             | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 1]> self = ?,<br>int dim = 1              | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 1]> self = ?,<br>int dim = 2              | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 2]> self = ?,<br>int dim = 1              | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1         | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[15]> self = ?,<br>int dim = 1                | Unknown  | Done       | 1.0   | 0      |
| 16 | Tensor<[17]> self = ?,<br>int dim = 1                | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[1]> self = ?,<br>int dim = 1                 | Unknown  | Done       | 1.0   | 0      |
| 18 | Tensor<[2]> self = ?,<br>int dim = 1                 | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[6, 1, 1]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[6, 15, 15]> self = ?,<br>int dim = 0         | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[6, 17, 17]> self = ?,<br>int dim = 0         | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[6, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0            | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[s0 + 1]> self = ?,<br>int dim = 1            | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]               | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]           | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, 384]                 | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                 | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]           | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]               | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 15, 1024]> self = ?,<br>List[int] size = [15, 1024]             | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]          | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [15, 384]               | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 15, 512]> self = ?,<br>List[int] size = [15, 512]               | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 15, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]          | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 15]> self = ?,<br>List[int] size = [-1, 15]                     | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                       | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]             | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 384]> self = ?,<br>List[int] size = [1, 1, 384]                 | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                 | Unknown  | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [6, 1, 15]             | Unknown  | Done       | 1.0   | 0      |
| 17 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [6, 1, 17]             | Unknown  | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [6, 1, 1]               | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [6, 1, 2]               | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [6, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [6, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 22 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [6, 15, 15]           | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [6, 15, 64]           | Unknown  | Done       | 1.0   | 0      |
| 24 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [6, 17, 64]           | Unknown  | Done       | 1.0   | 0      |
| 25 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [6, 2, 64]             | Unknown  | Done       | 1.0   | 0      |
| 26 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [6, 64, 15]           | Unknown  | Done       | 1.0   | 0      |
| 27 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [6, 64, 17]           | Unknown  | Done       | 1.0   | 0      |
| 28 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [6, 64, 1]             | Unknown  | Done       | 1.0   | 0      |
| 29 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [6, 64, 2]             | Unknown  | Done       | 1.0   | 0      |
| 30 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [6, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [6, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 32 | Tensor<[15, 1024]> self = ?,<br>List[int] size = [1, 15, 1024]             | Unknown  | Done       | 1.0   | 0      |
| 33 | Tensor<[15, 384]> self = ?,<br>List[int] size = [1, 15, 384]               | Unknown  | Done       | 1.0   | 0      |
| 34 | Tensor<[15, 512]> self = ?,<br>List[int] size = [1, 15, 512]               | Unknown  | Done       | 1.0   | 0      |
| 35 | Tensor<[6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]             | Unknown  | Done       | 1.0   | 0      |
| 36 | Tensor<[6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]             | Unknown  | Done       | 1.0   | 0      |
| 37 | Tensor<[6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]               | Unknown  | Done       | 1.0   | 0      |
| 38 | Tensor<[6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]               | Unknown  | Done       | 1.0   | 0      |
| 39 | Tensor<[6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 40 | Tensor<[6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]           | Unknown  | Done       | 1.0   | 0      |
| 42 | Tensor<[6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]           | Unknown  | Done       | 1.0   | 0      |
### aten.where.self
|    | ATen Input Variations                                                                                               | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                               | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[15, 15]> condition = ?,<br>Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                         | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[17, 17]> condition = ?,<br>Tensor<[17, 17]> self = ?,<br>Tensor<[17, 17]> other = ?                         | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[2, 2]> condition = ?,<br>Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                               | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[s0 + 1, s0 + 1]> condition = ?,<br>Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 6, 1, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
|  1 | List[int] size = [1, 6, 18, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False       | Unknown  | Done       | 1.0   | 0      |
|  2 | List[int] size = [1, 6, 3, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
|  3 | List[int] size = [1, 6, <s0 + 2>, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
### aten.zeros_like.default
|    | ATen Input Variations                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[17, 17]> self = ?,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[2, 2]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |

