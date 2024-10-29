# High Level Operations Status
|    | Operations             |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:-----------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten.arange.start      |                  1 |           0 |         0 |          0 | ✘           |     0   |
|  1 | aten.embedding.default |                  1 |           1 |         0 |          0 | ✅          |     1   |
|  2 | aten.repeat.default    |                  1 |           0 |         1 |          0 | ✅          |     1   |
|  3 | aten.slice.Tensor      |                  3 |           0 |         3 |          0 | ✅          |     1   |
|  4 | aten.unsqueeze.default |                  5 |           4 |         0 |          0 | 🚧          |     0.8 |
***
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number start = 0,<br>number end = 32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0 | Done     | Done       | True  |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Removed  | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | Fallback   | True  |
|  2 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Removed  | Fallback   | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1 | Done     | Done       | True  |
|  1 | Tensor<[1, 64]> self = ?,<br>int dim = 2         | None     | Fallback   | True  |
|  2 | Tensor<[2048, 2048]> self = ?,<br>int dim = 0    | Done     | Done       | True  |
|  3 | Tensor<[32]> self = ?,<br>int dim = 0            | Done     | Done       | True  |
|  4 | Tensor<[64]> self = ?,<br>int dim = 0            | Done     | Done       | True  |

