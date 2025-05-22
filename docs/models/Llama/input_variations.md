# High Level Operations Status
|    | Operations             |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-----------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._to_copy.default  |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  1 | aten.bmm.default       |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  2 | aten.cat.default       |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.cos.default       |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  4 | aten.embedding.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  5 | aten.expand.default    |                  3 |           0 |         3 |          0 | ✅          |       1 |
|  6 | aten.repeat.default    |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  7 | aten.slice.Tensor      |                  5 |           0 |         5 |          0 | ✅          |       1 |
|  8 | aten.transpose.int     |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  9 | aten.unsqueeze.default |                  5 |           5 |         0 |          0 | ✅          |       1 |
| 10 | aten.view.default      |                  3 |           3 |         0 |          0 | ✅          |       1 |
***
### aten._to_copy.default
|    | ATen Input Variations                                               | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>Optional[int] dtype = torch.float32 | Done     | Fallback   |     1 |     -1 |
### aten.bmm.default
|    | ATen Input Variations                                       | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ? | Done     | Done       | 0.999992 |      0 |
### aten.cat.default
|    | ATen Input Variations                                                  | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[Tensor] tensors = [<[1, 32, 64]>, <[1, 32, 64]>],<br>int dim = -1 | Done     | Done       |     1 |      0 |
### aten.cos.default
|    | ATen Input Variations         | Status   | Isolated   |      PCC |   Host |
|---:|:------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 32, 128]> self = ? | Done     | Done       | 0.999992 |      0 |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0 | Done     | Done       |     1 |      0 |
### aten.expand.default
|    | ATen Input Variations                                       | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32] | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, -1, 1] | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1] | Removed  | Done       |     1 |     -1 |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Removed  | Done       |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Done       |     1 |     -1 |
|  2 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807         | Removed  | Done       |     1 |     -1 |
|  3 | Tensor<[1, 32]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Removed  | Done       |     1 |     -1 |
|  4 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Removed  | Done       |     1 |     -1 |
### aten.transpose.int
|    | ATen Input Variations                                          | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 32]> self = ?,<br>int dim = 1         | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 64]> self = ?,<br>int dim = 2         | Done     | Done       |     1 |      0 |
|  3 | Tensor<[2048, 2048]> self = ?,<br>int dim = 0    | Done     | Done       |     1 |      0 |
|  4 | Tensor<[64]> self = ?,<br>int dim = 0            | Done     | Done       |     1 |      0 |
### aten.view.default
|    | ATen Input Variations                                         | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>List[int] size = [1, 1, 32]   | Done     | Done       |     1 |      0 |
|  1 | Tensor<[1, 64, 1]> self = ?,<br>List[int] size = [1, 64, 1]   | Done     | Done       |     1 |      0 |
|  2 | Tensor<[1, 64, 32]> self = ?,<br>List[int] size = [1, 64, 32] | Done     | Done       |     1 |      0 |

