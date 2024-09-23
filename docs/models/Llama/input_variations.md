# High Level Operations Status
|    | Operations             |   Input Variations |   Converted |
|---:|:-----------------------|-------------------:|------------:|
|  0 | aten.arange.start      |                  1 |           1 |
|  1 | aten.embedding.default |                  1 |           1 |
|  2 | aten.repeat.default    |                  1 |           0 |
|  3 | aten.slice.Tensor      |                  3 |           3 |
|  4 | aten.unsqueeze.default |                  5 |           5 |
***
### aten.arange.start
|    | ATen Input Variations                                                                                                | Status   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number<> start = 0,<br>number<> end = 32,<br>Optional[Device]<> device = cpu,<br>Optional[bool]<> pin_memory = False | Done     |
### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   |
|---:|:-------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int<> padding_idx = 0 | Done     |
### aten.repeat.default
|    | ATen Input Variations                                                      | Status   |
|---:|:---------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int]<> repeats = [1, 1, 1, 1] | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int<> dim = 2,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Done     |
|  1 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int<> dim = 3,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1 | Done     |
|  2 | Tensor<[1, 64]> self = ?,<br>int<> dim = 1,<br>Optional[int]<> start = 0,<br>Optional[int]<> end = -1            | Done     |
### aten.unsqueeze.default
|    | ATen Input Variations                              | Status   |
|---:|:---------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 2048]> self = ?,<br>int<> dim = 1 | Done     |
|  1 | Tensor<[1, 64]> self = ?,<br>int<> dim = 2         | Done     |
|  2 | Tensor<[2048, 2048]> self = ?,<br>int<> dim = 0    | Done     |
|  3 | Tensor<[32]> self = ?,<br>int<> dim = 0            | Done     |
|  4 | Tensor<[64]> self = ?,<br>int<> dim = 0            | Done     |

