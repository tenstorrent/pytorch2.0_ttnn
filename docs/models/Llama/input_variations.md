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
|    | ATen Input Variations                                                                                        | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | number start = 0,<br>number end = 32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | N/A                 | N/A          | N/A               | N/A                |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0 | Done     | N/A                 | N/A          | N/A               | N/A                |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Removed  | N/A                 | N/A          | N/A               | N/A                |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                       | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Removed  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807            | Removed  | N/A                 | N/A          | N/A               | N/A                |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 64]> self = ?,<br>int dim = 2         | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[2048, 2048]> self = ?,<br>int dim = 0    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[32]> self = ?,<br>int dim = 0            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[64]> self = ?,<br>int dim = 0            | Done     | N/A                 | N/A          | N/A               | N/A                |

