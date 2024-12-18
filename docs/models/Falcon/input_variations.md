# High Level Operations Status
|    | Operations             |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-----------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.all.default       |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  1 | aten.arange.start      |                  1 |           0 |         1 |          0 | ✅          |       1 |
|  2 | aten.embedding.default |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  3 | aten.eq.Scalar         |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  4 | aten.index.Tensor      |                  1 |           0 |         0 |          0 | ✘           |       0 |
|  5 | aten.slice.Tensor      |                  1 |           1 |         0 |          0 | ✅          |       1 |
|  6 | aten.unsqueeze.default |                  2 |           1 |         1 |          0 | ✅          |       1 |
***
### aten.all.default
|    | ATen Input Variations   | Status   | Isolated   |   PCC |   Host |
|---:|:------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ? | None     | Fallback   |     1 |     -1 |
### aten.arange.start
|    | ATen Input Variations                                                                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | number start = 0,<br>number end = 7,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Removed  | Done       |     1 |     -1 |
### aten.embedding.default
|    | ATen Input Variations                                           | Status   | Isolated   |   PCC |   Host |
|---:|:----------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ? | Done     | Done       |     1 |      2 |
### aten.eq.Scalar
|    | ATen Input Variations                        | Status   | Isolated   |   PCC |   Host |
|---:|:---------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7]> self = ?,<br>number other = 1 | Done     | Done       |     1 |      0 |
### aten.index.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[7, 64]> self = ?,<br>List[Optional[Tensor]] indices = [<[1, 7]>] | None     | Fallback   |     1 |     -1 |
### aten.slice.Tensor
|    | ATen Input Variations                                                                             | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2048, 64]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 7 | Done     | Done       |     1 |      0 |
### aten.unsqueeze.default
|    | ATen Input Variations                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1 | Done     | Done       |     1 |      0 |
|  1 | Tensor<[7]> self = ?,<br>int dim = 0        | Removed  | Done       |     1 |      0 |

