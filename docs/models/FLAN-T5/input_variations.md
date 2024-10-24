# High Level Operations Status
|    | Operations              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default   |                  6 |           1 |         0 |          0 | 🚧          |    0.17 |
|  1 | aten._to_copy.default   |                 32 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten.abs.default        |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.add.Tensor         |                 31 |           9 |         0 |          0 | 🚧          |    0.29 |
|  4 | aten.arange.default     |                  6 |           0 |         0 |          0 | ✘           |    0    |
|  5 | aten.bmm.default        |                 12 |           2 |         0 |          0 | 🚧          |    0.17 |
|  6 | aten.cat.default        |                  6 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.clone.default      |                 11 |           4 |         0 |          0 | 🚧          |    0.36 |
|  8 | aten.div.Tensor         |                 10 |           2 |         0 |          0 | 🚧          |    0.2  |
|  9 | aten.embedding.default  |                  7 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.expand.default     |                 16 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.full_like.default  |                  5 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.gt.Scalar          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.le.Tensor          |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.log.default        |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 15 | aten.lt.Scalar          |                  5 |           0 |         0 |          0 | ✘           |    0    |
| 16 | aten.mean.dim           |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 17 | aten.minimum.default    |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 18 | aten.mm.default         |                  9 |           4 |         0 |          0 | 🚧          |    0.44 |
| 19 | aten.mul.Tensor         |                 28 |          10 |         0 |          0 | 🚧          |    0.36 |
| 20 | aten.neg.default        |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.ones.default       |                  7 |           1 |         0 |          0 | 🚧          |    0.14 |
| 22 | aten.permute.default    |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 23 | aten.pow.Tensor_Scalar  |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
| 24 | aten.repeat.default     |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 25 | aten.rsqrt.default      |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 26 | aten.rsub.Scalar        |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 27 | aten.slice.Tensor       |                 51 |           0 |         0 |          0 | ✘           |    0    |
| 28 | aten.sub.Tensor         |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 29 | aten.sym_size.int       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.t.default          |                  5 |           4 |         0 |          0 | 🚧          |    0.8  |
| 31 | aten.tanh.default       |                  2 |           1 |         0 |          0 | 🚧          |    0.5  |
| 32 | aten.transpose.int      |                  9 |           3 |         0 |          0 | 🚧          |    0.33 |
| 33 | aten.unsqueeze.default  |                 30 |           4 |         0 |          0 | 🚧          |    0.13 |
| 34 | aten.view.default       |                 43 |          14 |         0 |          0 | 🚧          |    0.33 |
| 35 | aten.where.self         |                  5 |           1 |         0 |          0 | 🚧          |    0.2  |
| 36 | aten.zeros.default      |                  4 |           0 |         0 |          0 | ✘           |    0    |
| 37 | aten.zeros_like.default |                  4 |           0 |         0 |          0 | ✘           |    0    |
***
### aten._softmax.default
|    | ATen Input Variations                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = -1,<br>bool half_to_float = False     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 6, 1, 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = -1,<br>bool half_to_float = False      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 6, 15, 15]> self = ?,<br>int dim = -1,<br>bool half_to_float = False    | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten._to_copy.default
|    | ATen Input Variations                                                                                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 17]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1, 512]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 1, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 15, 512]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 15, 512]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 6, 1, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 6, 1, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 6, 1, 17]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 6, 1, 17]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 6, 1, 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 6, 1, 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 6, 1, 2]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 6, 1, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 6, 15, 15]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 6, 15, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[15, 15]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[15, 15]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[17, 17]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[17, 17]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.float32                                                                                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[2, 2]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.float32                                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[int] dtype = torch.int64                                                                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.abs.default
|    | ATen Input Variations     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[15, 15]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.arange.default
|    | ATen Input Variations                                                                                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number end = 1,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | number end = 1,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | number end = 15,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | number end = 17,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | number end = 2,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | number<s0 + 1> end = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.bmm.default
|    | ATen Input Variations                                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[6, 1, 17]> self = ?,<br>Tensor<[6, 17, 64]> mat2 = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 17]> mat2 = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.cat.default
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[Tensor] tensors = [<[1, 1, 16]>, <[1, 1, 1]>],<br>int dim = -1        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[Tensor] tensors = [<[1, 1, 1]>, <[1, 1, 1]>],<br>int dim = -1         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | List[Tensor] tensors = [<[1, 1, s0]>, <[1, 1, 1]>],<br>int dim = -1        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | List[Tensor] tensors = [<[1, 6, 1, 64]>, <[1, 6, 1, 64]>],<br>int dim = 2  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | List[Tensor] tensors = [<[1, 6, 16, 64]>, <[1, 6, 1, 64]>],<br>int dim = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | List[Tensor] tensors = [<[1, 6, s0, 64]>, <[1, 6, 1, 64]>],<br>int dim = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.clone.default
|    | ATen Input Variations                                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?                                                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 512]> self = ?                                                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 15, 1024]> self = ?                                                            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 15, 512]> self = ?                                                             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 15, 6, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 6, 1, 15]> self = ?                                                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 6, 1, 17]> self = ?                                                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 6, 1, 1]> self = ?                                                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 6, 1, 2]> self = ?                                                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 6, 1, s0 + 1]> self = ?                                                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 6, 15, 15]> self = ?                                                           | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.div.Tensor
|    | ATen Input Variations                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.embedding.default
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?         | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?     | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.expand.default
|    | ATen Input Variations                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [1, 6, 17, 64]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [1, 6, 2, 64]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [1, 6, 64, 15]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [1, 6, 64, 17]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [1, 6, 64, 1]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [1, 6, 64, 2]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 64, <s0 + 1>] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [1, 6, <s0 + 1>, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.full_like.default
|    | ATen Input Variations                                                                              | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[15, 15]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False         | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[17, 17]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[2, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.gt.Scalar
|    | ATen Input Variations                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[15, 15]> self = ?,<br>number other = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.le.Tensor
|    | ATen Input Variations                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.log.default
|    | ATen Input Variations             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> self = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[15, 15]> self = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[17, 17]> self = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[2, 2]> self = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.lt.Scalar
|    | ATen Input Variations                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 16           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[15, 15]> self = ?,<br>number other = 8          | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[17, 17]> self = ?,<br>number other = 16         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[2, 2]> self = ?,<br>number other = 16           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number other = 16 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mean.dim
|    | ATen Input Variations                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 15, 512]> self = ?,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.minimum.default
|    | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[17, 17]> self = ?,<br>Tensor<[17, 17]> other = ?                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 32128]> mat2 = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[15, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[15, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.mul.Tensor
|    | ATen Input Variations                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.neg.default
|    | ATen Input Variations             | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> self = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[17, 17]> self = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[2, 2]> self = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.ones.default
|    | ATen Input Variations                                                                                                                         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[int] size = [1, 1, 16],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | List[int] size = [1, 1, <s0>],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | List[int] size = [1, 1],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | List[int] size = [1, 2],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | List[int] size = [1, <s0 + 1>],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.permute.default
|    | ATen Input Variations                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[15, 15, 6]> self = ?,<br>List[int] dims = [2, 0, 1]         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[17, 17, 6]> self = ?,<br>List[int] dims = [2, 0, 1]         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[2, 2, 6]> self = ?,<br>List[int] dims = [2, 0, 1]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[s0 + 1, s0 + 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.pow.Tensor_Scalar
|    | ATen Input Variations                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>number exponent = 3.0  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 512]> self = ?,<br>number exponent = 2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 15, 1024]> self = ?,<br>number exponent = 3.0 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 15, 512]> self = ?,<br>number exponent = 2    | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.repeat.default
|    | ATen Input Variations                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1]> self = ?,<br>List[int] repeats = [1, 1, 1] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.rsqrt.default
|    | ATen Input Variations       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 15, 1]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.rsub.Scalar
|    | ATen Input Variations                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 1, 17]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1, 17]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 1, 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 6, 1, 15]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 6, 1, 17]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 6, 1, 2]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[1, 6, 17, 17]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[1, 6, 18, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[1, 6, 2, 2]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[1, 6, 3, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 38 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 39 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 40 | Tensor<[1, 6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 41 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 42 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 43 | Tensor<[1, 6, s0 + 2, 15]> self = ?,<br>int dim = 2,<br>Optional[int] start = -1,<br>Optional[int] end = 9223372036854775807     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 44 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 45 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 46 | Tensor<[15]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 47 | Tensor<[17]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 48 | Tensor<[1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 49 | Tensor<[2]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 50 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.sym_size.int
|    | ATen Input Variations                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.t.default
|    | ATen Input Variations         | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1024, 512]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[32128, 512]> self = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[384, 512]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[512, 1024]> self = ?  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[512, 384]> self = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.tanh.default
|    | ATen Input Variations          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 15, 1024]> self = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.transpose.int
|    | ATen Input Variations                                                 | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 15, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 6, 17, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 6, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                                | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 15]> self = ?,<br>int dim = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 1          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 1           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 15]> self = ?,<br>int dim = 1             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 17]> self = ?,<br>int dim = 1             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 1]> self = ?,<br>int dim = 1              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 1]> self = ?,<br>int dim = 2              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 2]> self = ?,<br>int dim = 1              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[15]> self = ?,<br>int dim = 0                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[15]> self = ?,<br>int dim = 1                | None     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[17]> self = ?,<br>int dim = 0                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[17]> self = ?,<br>int dim = 1                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1]> self = ?,<br>int dim = 0                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1]> self = ?,<br>int dim = 1                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[2]> self = ?,<br>int dim = 0                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[2]> self = ?,<br>int dim = 1                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[6, 1, 1]> self = ?,<br>int dim = 0           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[6, 15, 15]> self = ?,<br>int dim = 0         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[6, 17, 17]> self = ?,<br>int dim = 0         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[6, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[s0 + 1]> self = ?,<br>int dim = 1            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.view.default
|    | ATen Input Variations                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:---------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 1024]> self = ?,<br>List[int] size = [1, 1024]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 384]> self = ?,<br>List[int] size = [1, 384]                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 512]> self = ?,<br>List[int] size = [1, 512]                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1024]> self = ?,<br>List[int] size = [1, 1, 1024]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 15, 1024]> self = ?,<br>List[int] size = [15, 1024]             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [1, -1, 6, 64]          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 15, 384]> self = ?,<br>List[int] size = [15, 384]               | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 15, 512]> self = ?,<br>List[int] size = [15, 512]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 15, 6, 64]> self = ?,<br>List[int] size = [1, -1, 384]          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 15]> self = ?,<br>List[int] size = [-1, 15]                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 1]> self = ?,<br>List[int] size = [-1, 1]                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 32128]> self = ?,<br>List[int] size = [1, 1, 32128]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 384]> self = ?,<br>List[int] size = [1, 1, 384]                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 512]> self = ?,<br>List[int] size = [1, 1, 512]                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 6, 1, 15]> self = ?,<br>List[int] size = [6, 1, 15]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 6, 1, 17]> self = ?,<br>List[int] size = [6, 1, 17]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 6, 1, 1]> self = ?,<br>List[int] size = [6, 1, 1]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 6, 1, 2]> self = ?,<br>List[int] size = [6, 1, 2]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 6, 1, 64]> self = ?,<br>List[int] size = [6, 1, 64]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>List[int] size = [6, 1, <s0 + 1>]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 6, 15, 15]> self = ?,<br>List[int] size = [6, 15, 15]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 6, 15, 64]> self = ?,<br>List[int] size = [6, 15, 64]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 6, 17, 64]> self = ?,<br>List[int] size = [6, 17, 64]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[1, 6, 2, 64]> self = ?,<br>List[int] size = [6, 2, 64]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[1, 6, 64, 15]> self = ?,<br>List[int] size = [6, 64, 15]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[1, 6, 64, 17]> self = ?,<br>List[int] size = [6, 64, 17]           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[1, 6, 64, 1]> self = ?,<br>List[int] size = [6, 64, 1]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[1, 6, 64, 2]> self = ?,<br>List[int] size = [6, 64, 2]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[1, 6, 64, s0 + 1]> self = ?,<br>List[int] size = [6, 64, <s0 + 1>] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>List[int] size = [6, <s0 + 1>, 64] | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[15, 1024]> self = ?,<br>List[int] size = [1, 15, 1024]             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[15, 384]> self = ?,<br>List[int] size = [1, 15, 384]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[15, 512]> self = ?,<br>List[int] size = [1, 15, 512]               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[6, 1, 15]> self = ?,<br>List[int] size = [1, 6, 1, 15]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[6, 1, 17]> self = ?,<br>List[int] size = [1, 6, 1, 17]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[6, 1, 1]> self = ?,<br>List[int] size = [1, 6, 1, 1]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 38 | Tensor<[6, 1, 2]> self = ?,<br>List[int] size = [1, 6, 1, 2]               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 39 | Tensor<[6, 1, 64]> self = ?,<br>List[int] size = [1, 6, 1, 64]             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 40 | Tensor<[6, 1, s0 + 1]> self = ?,<br>List[int] size = [1, 6, 1, <s0 + 1>]   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 41 | Tensor<[6, 15, 15]> self = ?,<br>List[int] size = [1, 6, 15, 15]           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 42 | Tensor<[6, 15, 64]> self = ?,<br>List[int] size = [1, 6, 15, 64]           | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.where.self
|    | ATen Input Variations                                                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:--------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> condition = ?,<br>Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[15, 15]> condition = ?,<br>Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[17, 17]> condition = ?,<br>Tensor<[17, 17]> self = ?,<br>Tensor<[17, 17]> other = ?                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[2, 2]> condition = ?,<br>Tensor<[2, 2]> self = ?,<br>Tensor<[2, 2]> other = ?                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[s0 + 1, s0 + 1]> condition = ?,<br>Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, s0 + 1]> other = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.zeros.default
|    | ATen Input Variations                                                                                                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | List[int] size = [1, 6, 1, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | List[int] size = [1, 6, 18, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | List[int] size = [1, 6, 3, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | List[int] size = [1, 6, <s0 + 2>, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |
### aten.zeros_like.default
|    | ATen Input Variations                                                   | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[17, 17]> self = ?,<br>Optional[bool] pin_memory = False         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[2, 2]> self = ?,<br>Optional[bool] pin_memory = False           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False | Unknown  | N/A                 | N/A          | N/A               | N/A                |

