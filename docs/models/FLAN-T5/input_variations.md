# High Level Operations Status
|    | Operations                |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default     |                  5 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten._to_copy.default     |                 23 |           0 |         0 |          0 | ✘           |       0 |
|  2 | aten._unsafe_view.default |                  7 |           0 |         0 |          0 | ✘           |       0 |
|  3 | aten.abs.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  4 | aten.add.Tensor           |                 28 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.any.default          |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  6 | aten.arange.default       |                  2 |           0 |         0 |          0 | ✘           |       0 |
|  7 | aten.bitwise_or.Tensor    |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  8 | aten.bmm.default          |                 10 |           0 |         0 |          0 | ✘           |       0 |
|  9 | aten.cat.default          |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 10 | aten.clone.default        |                 11 |           0 |         0 |          0 | ✘           |       0 |
| 11 | aten.div.Tensor           |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 12 | aten.embedding.default    |                  6 |           0 |         0 |          0 | ✘           |       0 |
| 13 | aten.expand.default       |                 16 |           0 |         0 |          0 | ✘           |       0 |
| 14 | aten.full.default         |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 15 | aten.full_like.default    |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 16 | aten.gt.Scalar            |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 17 | aten.gt.Tensor            |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 18 | aten.index.Tensor         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 19 | aten.isin.Tensor_Tensor   |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 20 | aten.log.default          |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 21 | aten.lt.Scalar            |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 22 | aten.mean.dim             |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 23 | aten.minimum.default      |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 24 | aten.mm.default           |                  9 |           0 |         0 |          0 | ✘           |       0 |
| 25 | aten.mul.Tensor           |                 22 |           0 |         0 |          0 | ✘           |       0 |
| 26 | aten.neg.default          |                  3 |           0 |         0 |          0 | ✘           |       0 |
| 27 | aten.permute.default      |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 28 | aten.pow.Tensor_Scalar    |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 29 | aten.rsqrt.default        |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 30 | aten.rsub.Scalar          |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 31 | aten.select.int           |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 32 | aten.slice.Tensor         |                 44 |           0 |         0 |          0 | ✘           |       0 |
| 33 | aten.sub.Tensor           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 34 | aten.t.default            |                  5 |           0 |         0 |          0 | ✘           |       0 |
| 35 | aten.tanh.default         |                  2 |           0 |         0 |          0 | ✘           |       0 |
| 36 | aten.transpose.int        |                  8 |           0 |         0 |          0 | ✘           |       0 |
| 37 | aten.unsqueeze.default    |                 15 |           0 |         0 |          0 | ✘           |       0 |
| 38 | aten.view.default         |                 33 |           0 |         0 |          0 | ✘           |       0 |
| 39 | aten.where.self           |                  4 |           0 |         0 |          0 | ✘           |       0 |
| 40 | aten.zeros.default        |                  1 |           0 |         0 |          0 | ✘           |       0 |
| 41 | aten.zeros_like.default   |                  3 |           0 |         0 |          0 | ✘           |       0 |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | Done       | 0.9997535970940763 | 0      |
|  1 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | Done       | 0.9996436881039042 | 0      |
|  3 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Unknown  | Done       | 0.9996360083699752 | 0      |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 1, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                   | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 15, 512]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[1, 15, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
|  6 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                          | Unknown  | Fallback   | 1.0   | -1     |
|  7 | Tensor<[1, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                        | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 2]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                          | Unknown  | Unknown    | N/A   | N/A    |
|  9 | Tensor<[1, 6, 1, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | Fallback   | 1.0   | -1     |
| 10 | Tensor<[1, 6, 1, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | Fallback   | 1.0   | -1     |
| 11 | Tensor<[1, 6, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 12 | Tensor<[1, 6, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 13 | Tensor<[1, 6, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | Fallback   | 1.0   | -1     |
| 14 | Tensor<[1, 6, 1, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | Fallback   | 1.0   | -1     |
| 15 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 6, 15, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Unknown  | Fallback   | 1.0   | -1     |
| 18 | Tensor<[1, 6, 15, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                | Unknown  | Fallback   | 1.0   | -1     |
| 19 | Tensor<[1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                   | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                     | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[15, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Unknown  | Fallback   | 1.0   | -1     |
| 22 | Tensor<[15, 15]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  | Fallback   | 1.0   | -1     |
### aten._unsafe_view.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]   | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128] | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 384]> self = ?,<br>List[int] size = [1, 1, 384]     | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[15, 1024]> self = ?,<br>List[int] size = [1, 15, 1024] | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[15, 384]> self = ?,<br>List[int] size = [1, 15, 384]   | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[15, 512]> self = ?,<br>List[int] size = [1, 15, 512]   | Unknown  | Unknown    | N/A   | N/A    |
### aten.abs.default
|    | ATen Input Variations     | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[15, 15]> self = ? | Unknown  | Done       |     1 |      0 |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                       | Unknown  | Done       | 0.9999950840423011 | 0      |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?           | Unknown  | Done       | 0.9999978216991892 | 0      |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                        | Unknown  | Done       | 1.0                | 0      |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?             | Unknown  | Done       | 0.9999983839309707 | 0      |
|  4 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                      | Unknown  | Done       | 0.9999947446058011 | 0      |
|  5 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?         | Unknown  | Done       | 0.9999980560859794 | 0      |
|  6 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                       | Unknown  | Done       | 1.0                | 0      |
|  7 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?           | Unknown  | Done       | 0.9999978099399699 | 0      |
|  8 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                               | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                              | Unknown  | Done       | 1.0                | 0      |
| 10 | Tensor<[1, 2]> self = ?,<br>Tensor other = 0                               | Unknown  | Unknown    | N/A                | N/A    |
| 11 | Tensor<[1, 2]> self = ?,<br>Tensor other = 16                              | Unknown  | Unknown    | N/A                | N/A    |
| 12 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?         | Unknown  | Done       | 0.9999983632808066 | 0      |
| 13 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?         | Unknown  | Done       | 0.9999993249676742 | 0      |
| 14 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?           | Unknown  | Done       | 1.0                | 0      |
| 15 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?           | Unknown  | Done       | 0.9999942303957439 | 0      |
| 16 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?           | Unknown  | Done       | 1.0                | 0      |
| 17 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?           | Unknown  | Done       | 0.9999997494438243 | 0      |
| 18 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 19 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 20 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?        | Unknown  | Done       | 0.9999971485331847 | 0      |
| 21 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?       | Unknown  | Done       | 0.9999975168691554 | 0      |
| 22 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 0                          | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 16                         | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                             | Unknown  | Done       | 1.0                | 0      |
| 25 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                             | Unknown  | Done       | 0.9999303823329366 | 0      |
| 26 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                   | Unknown  | Done       | 0.9999979668779759 | 0      |
| 27 | Tensor<[1]> self = ?,<br>Tensor other = 1                                  | Unknown  | Unknown    | N/A                | N/A    |
### aten.any.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?    | Unknown  | Unknown    | N/A   | N/A    |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  1 | number<s0 + 2> end = ?,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                       | Unknown  | Unknown    | N/A   | N/A    |
### aten.bitwise_or.Tensor
|    | ATen Input Variations                          | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.bmm.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?         | Unknown  | Done       | 0.999993007999331  | 0      |
|  1 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?           | Unknown  | Done       | 0.9999935690723534 | 0      |
|  2 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?           | Unknown  | Done       | 0.9999937750889882 | 0      |
|  3 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?         | Unknown  | Done       | 0.9999880906623534 | 0      |
|  4 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?          | Unknown  | Done       | 0.9999927893184396 | 0      |
|  5 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?          | Unknown  | Done       | 0.9999882405796569 | 0      |
|  6 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  8 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?        | Unknown  | Done       | 0.9999912969241996 | 0      |
|  9 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?        | Unknown  | Done       | 0.9999863783369959 | 0      |
### aten.cat.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[Tensor] tensors = [<[1, 6, 1, 64]>, <[1, 6, 1, 64]>],<br>int dim = -2  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[Tensor] tensors = [<[1, 6, s0, 64]>, <[1, 6, 1, 64]>],<br>int dim = -2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 512]> self = ?                                                              | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 15, 1024]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 15, 512]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 1]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format         | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 6, 1, 15]> self = ?                                                            | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 6, 1, 1]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 6, 1, 2]> self = ?                                                             | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 6, 1, s0 + 1]> self = ?                                                        | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 6, 15, 15]> self = ?                                                           | Unknown  | Done       | 1.0   | 0      |
### aten.div.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                      | Unknown  | Done       | 1.0                | 0      |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357      | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 2]> self = ?,<br>Tensor other = 16                      | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 2]> self = ?,<br>Tensor other = 2.0794415416798357      | Unknown  | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 16                 | Unknown  | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357 | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781     | Unknown  | Done       | 0.9999962939050889 | 0      |
|  7 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                     | Unknown  | Done       | 1.0                | 0      |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?       | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 2]> indices = ?       | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, s0 + 1]> indices = ?  | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?     | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ? | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?  | Unknown  | Done       | 1.0   | 0      |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1, 2]> self = ?,<br>List[int] size = [1, 1, -1, -1]             | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1, 1, 3]> self = ?,<br>List[int] size = [1, 1, -1, -1]             | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, s0 + 2]> self = ?,<br>List[int] size = [1, 1, -1, -1]        | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]             | Unknown  | Done       | 1.0   | -1     |
|  4 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]               | Unknown  | Done       | 1.0   | -1     |
|  5 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]               | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]             | Unknown  | Done       | 1.0   | -1     |
|  7 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]           | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]           | Unknown  | Done       | 1.0   | -1     |
| 10 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [1, 6, 2, 64]             | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [1, 6, 64, 15]           | Unknown  | Done       | 1.0   | -1     |
| 12 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [1, 6, 64, 1]             | Unknown  | Done       | 1.0   | -1     |
| 13 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [1, 6, 64, 2]             | Unknown  | Done       | 1.0   | -1     |
| 14 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 6, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
### aten.full.default
|    | ATen Input Variations                                                                                                                                                                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 2],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Unknown    | N/A   | N/A    |
|  1 | List[int] size = [1, 3],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [1, <s0 + 2>],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[int] size = [1],<br>number fill_value = False,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | List[int] size = [1],<br>number<s0 >= 21> fill_value = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                           | Unknown  | Unknown    | N/A   | N/A    |
### aten.full_like.default
|    | ATen Input Variations                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[15, 15]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False    | Unknown  | Done       | 1.0   | 0      |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[15, 15]> self = ?,<br>number other = 0 | Unknown  | Done       |     1 |      0 |
### aten.gt.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[s0 + 2]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.index.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[1]>]  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[1]>] | Unknown  | Unknown    | N/A   | N/A    |
### aten.isin.Tensor_Tensor
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor elements = ?,<br>Tensor test_elements = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1]> elements = ?,<br>Tensor<[1]> test_elements = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.log.default
|    | ATen Input Variations        | Status   | Isolated   | PCC                  | Host   |
|---:|:-----------------------------|:---------|:-----------|:---------------------|:-------|
|  0 | Tensor<[1, 1]> self = ?      | Unknown  | Done       | 0.0                  | 0      |
|  1 | Tensor<[1, 2]> self = ?      | Unknown  | Unknown    | N/A                  | N/A    |
|  2 | Tensor<[1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A                  | N/A    |
|  3 | Tensor<[15, 15]> self = ?    | Unknown  | Done       | -0.22294320093744074 | 0      |
### aten.lt.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2]> self = ?,<br>number other = 16      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[15, 15]> self = ?,<br>number other = 8     | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1]> self = ?,<br>number other = 0          | Unknown  | Unknown    | N/A   | N/A    |
### aten.mean.dim
|    | ATen Input Variations                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True  | Unknown  | Done       |     1 |      0 |
|  1 | Tensor<[1, 15, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Unknown  | Done       |     1 |      0 |
### aten.minimum.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2]> self = ?,<br>Tensor<[1, 2]> other = ?           | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?       | Unknown  | Done       | 1.0   | 0      |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?  | Unknown  | Done       | 0.999966 |      0 |
|  1 | Tensor<[1, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?    | Unknown  | Done       | 0.999974 |      0 |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?   | Unknown  | Done       | 0.999973 |      0 |
|  3 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 32128]> mat2 = ?  | Unknown  | Done       | 0.999971 |      0 |
|  4 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?    | Unknown  | Done       | 0.999974 |      0 |
|  5 | Tensor<[15, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Unknown  | Done       | 0.999966 |      0 |
|  6 | Tensor<[15, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?   | Unknown  | Done       | 0.999973 |      0 |
|  7 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?  | Unknown  | Done       | 0.999971 |      0 |
|  8 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?   | Unknown  | Done       | 0.999971 |      0 |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC                | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Done       | 0.9999981054487544 | 0      |
|  2 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                 | Unknown  | Done       | 0.9999941958840586 | 0      |
|  3 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                      | Unknown  | Done       | 1.0                | 0      |
|  4 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654       | Unknown  | Done       | 0.9999976506375162 | 0      |
|  5 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?          | Unknown  | Done       | 0.9999959334157156 | 0      |
|  6 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999998877312276 | 0      |
|  7 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                | Unknown  | Done       | 0.9999953936481457 | 0      |
|  8 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                     | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654      | Unknown  | Done       | 0.9999971863061885 | 0      |
| 10 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?        | Unknown  | Done       | 0.9999961433535078 | 0      |
| 11 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?            | Unknown  | Done       | 0.9999954832726955 | 0      |
| 12 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                             | Unknown  | Done       | 1.0                | 0      |
| 13 | Tensor<[1, 2]> self = ?,<br>Tensor other = 16                             | Unknown  | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 2]> self = ?,<br>Tensor<[1, 2]> other = ?                      | Unknown  | Unknown    | N/A                | N/A    |
| 15 | Tensor<[1, 3]> self = ?,<br>Tensor<[1, 3]> other = ?                      | Unknown  | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                | N/A    |
| 17 | Tensor<[1, s0 + 2]> self = ?,<br>Tensor<[1, s0 + 2]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 18 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                           | Unknown  | Done       | 1.0                | 0      |
| 19 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                            | Unknown  | Done       | 1.0                | 0      |
| 20 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                  | Unknown  | Done       | 0.9999967010897297 | 0      |
| 21 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                 | Unknown  | Done       | 0.9999961999225291 | 0      |
### aten.neg.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2]> self = ?      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0 + 1]> self = ? | Unknown  | Unknown    | N/A   | N/A    |
### aten.permute.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2, 6]> self = ?,<br>List[int] dims = [2, 0, 1]      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0 + 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1] | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[15, 15, 6]> self = ?,<br>List[int] dims = [2, 0, 1]    | Unknown  | Done       | 1.0   | 0      |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   | Isolated   | PCC                | Host   |
|---:|:---------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>number exponent = 3.0  | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>number exponent = 2     | Unknown  | Unknown    | N/A                | N/A    |
|  2 | Tensor<[1, 15, 1024]> self = ?,<br>number exponent = 3.0 | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, 15, 512]> self = ?,<br>number exponent = 2    | Unknown  | Done       | 0.9999941010827373 | 0      |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Isolated   |      PCC |   Host |
|---:|:----------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1]> self = ?  | Unknown  | Done       | 0        |      0 |
|  1 | Tensor<[1, 15, 1]> self = ? | Unknown  | Done       | 0.999994 |      0 |
### aten.rsub.Scalar
|    | ATen Input Variations                                 | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0 | Unknown  | Done       | 0.999994 |      0 |
### aten.select.int
|    | ATen Input Variations                                       | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 2]> self = ?,<br>int dim = 1,<br>int index = -1  | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>int index = -1 | Unknown  | Unknown    | N/A   | N/A    |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
|  5 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Done       | 1.0   | -1     |
|  6 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Done       | 1.0   | -1     |
|  9 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 1                         | Unknown  | Unknown    | N/A   | N/A    |
| 10 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Done       | 1.0   | -1     |
| 11 | Tensor<[1, 1, 1, 3]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[1, 1, 1, 3]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[1, 1, 1, 3]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 14 | Tensor<[1, 1, 1, 3]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 2                         | Unknown  | Unknown    | N/A   | N/A    |
| 15 | Tensor<[1, 1, 1, 3]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 16 | Tensor<[1, 1, 1, s0 + 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 1, 1, s0 + 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 18 | Tensor<[1, 1, 1, s0 + 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 19 | Tensor<[1, 1, 1, s0 + 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 20 | Tensor<[1, 1, 1, s0 + 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int]<s0 + 1> end = ?            | Unknown  | Unknown    | N/A   | N/A    |
| 21 | Tensor<[1, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Done       | 1.0   | -1     |
| 22 | Tensor<[1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
| 23 | Tensor<[1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 27 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 28 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 29 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Unknown    | N/A   | N/A    |
| 30 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807      | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Done       | 1.0   | -1     |
| 32 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 33 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 34 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807 | Unknown  | Unknown    | N/A   | N/A    |
| 35 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | Unknown    | N/A   | N/A    |
| 36 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
| 37 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
| 38 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -15,<br>Optional[int] end = 9223372036854775807   | Unknown  | Unknown    | N/A   | N/A    |
| 39 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Unknown    | N/A   | N/A    |
| 40 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807        | Unknown  | Unknown    | N/A   | N/A    |
| 41 | Tensor<[1, s0]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | Unknown    | N/A   | N/A    |
| 42 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807               | Unknown  | Unknown    | N/A   | N/A    |
| 43 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | Unknown    | N/A   | N/A    |
### aten.sub.Tensor
|    | ATen Input Variations                                     | Status   | Isolated   | PCC                | Host   |
|---:|:----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?    | Unknown  | Done       | 0.9999984247810844 | 0      |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?      | Unknown  | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 2]> self = ?,<br>Tensor<[1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  3 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
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
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | Done       | 0.999993 |      0 |
|  1 | Tensor<[1, 15, 1024]> self = ? | Unknown  | Done       | 0.999992 |      0 |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 15, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 6, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2 | Unknown  | Unknown    | N/A   | N/A    |
### aten.unsqueeze.default
|    | ATen Input Variations                           | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 15]> self = ?,<br>int dim = 2     | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1      | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 3]> self = ?,<br>int dim = 1      | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, 1, s0 + 2]> self = ?,<br>int dim = 1 | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[1, 15]> self = ?,<br>int dim = 1        | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 2]> self = ?,<br>int dim = 0         | Unknown  | Unknown    | N/A   | N/A    |
|  6 | Tensor<[1, 3]> self = ?,<br>int dim = 0         | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[1, s0 + 2]> self = ?,<br>int dim = 0    | Unknown  | Unknown    | N/A   | N/A    |
|  8 | Tensor<[15]> self = ?,<br>int dim = 1           | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1]> self = ?,<br>int dim = 1            | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[6, 1, 1]> self = ?,<br>int dim = 0      | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[6, 1, 2]> self = ?,<br>int dim = 0      | Unknown  | Unknown    | N/A   | N/A    |
| 12 | Tensor<[6, 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
| 13 | Tensor<[6, 15, 15]> self = ?,<br>int dim = 0    | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0       | Unknown  | Unknown    | N/A   | N/A    |
### aten.view.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]               | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]           | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, 384]                 | Unknown  | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                 | Unknown  | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 1, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]           | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 15, 1024]> self = ?,<br>List[int] size = [15, 1024]             | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]          | Unknown  | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [15, 384]               | Unknown  | Done       | 1.0   | 0      |
|  8 | Tensor<[1, 15, 512]> self = ?,<br>List[int] size = [15, 512]               | Unknown  | Done       | 1.0   | 0      |
|  9 | Tensor<[1, 15, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]          | Unknown  | Done       | 1.0   | 0      |
| 10 | Tensor<[1, 15]> self = ?,<br>List[int] size = [-1, 15]                     | Unknown  | Done       | 1.0   | 0      |
| 11 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                       | Unknown  | Done       | 1.0   | 0      |
| 12 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [6, 1, 15]             | Unknown  | Done       | 1.0   | 0      |
| 13 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [6, 1, 1]               | Unknown  | Done       | 1.0   | 0      |
| 14 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [6, 1, 2]               | Unknown  | Done       | 1.0   | 0      |
| 15 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [6, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 16 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [6, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 17 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [6, 15, 15]           | Unknown  | Done       | 1.0   | 0      |
| 18 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [6, 15, 64]           | Unknown  | Done       | 1.0   | 0      |
| 19 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [6, 2, 64]             | Unknown  | Done       | 1.0   | 0      |
| 20 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [6, 64, 15]           | Unknown  | Done       | 1.0   | 0      |
| 21 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [6, 64, 1]             | Unknown  | Done       | 1.0   | 0      |
| 22 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [6, 64, 2]             | Unknown  | Done       | 1.0   | 0      |
| 23 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [6, 64, <s0 + 1>] | Unknown  | Unknown    | N/A   | N/A    |
| 24 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [6, <s0 + 1>, 64] | Unknown  | Unknown    | N/A   | N/A    |
| 25 | Tensor<[1]> self = ?,<br>List[int] size = [-1, 1]                          | Unknown  | Unknown    | N/A   | N/A    |
| 26 | Tensor<[6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]             | Unknown  | Done       | 1.0   | 0      |
| 27 | Tensor<[6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]               | Unknown  | Done       | 1.0   | 0      |
| 28 | Tensor<[6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]               | Unknown  | Done       | 1.0   | 0      |
| 29 | Tensor<[6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]             | Unknown  | Done       | 1.0   | 0      |
| 30 | Tensor<[6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]   | Unknown  | Unknown    | N/A   | N/A    |
| 31 | Tensor<[6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]           | Unknown  | Done       | 1.0   | 0      |
| 32 | Tensor<[6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]           | Unknown  | Done       | 1.0   | 0      |
### aten.where.self
|    | ATen Input Variations                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:-----------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2]> condition = ?,<br>Tensor<[1, 2]> self = ?,<br>Tensor<[1, 2]> other = ?                | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0 + 1]> condition = ?,<br>Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[15, 15]> condition = ?,<br>Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?          | Unknown  | Done       | 1.0   | 0      |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [1, 6, 1, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Done       |     1 |      0 |
### aten.zeros_like.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False      | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 2]> self = ?,<br>Optional[bool] pin_memory = False      | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |

