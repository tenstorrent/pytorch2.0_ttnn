# High Level Operations Status
|    | Operations             |   Input Variations |
|---:|:-----------------------|-------------------:|
|  0 | aten.arange.start      |                  1 |
|  1 | aten.embedding.default |                  1 |
|  2 | aten.repeat.default    |                  1 |
|  3 | aten.slice.Tensor      |                  2 |
|  4 | aten.unsqueeze.default |                  3 |
***
### aten.arange.start
|    | ATen Input Variations                                                                                        | Status   |
|---:|:-------------------------------------------------------------------------------------------------------------|:---------|
|  0 | number start = 0,<br>number end = 32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  |
### aten.embedding.default
|    | ATen Input Variations                                                                    | Status   |
|---:|:-----------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0 | Unknown  |
### aten.repeat.default
|    | ATen Input Variations                                                    | Status   |
|---:|:-------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>List[int] repeats = [1, 1, 1, 1] | Unknown  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                      | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = -1 | Unknown  |
|  1 | Tensor<[1, 64]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = -1            | Unknown  |
### aten.unsqueeze.default
|    | ATen Input Variations                            | Status   |
|---:|:-------------------------------------------------|:---------|
|  0 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1 | Unknown  |
|  1 | Tensor<[1, 64]> self = ?,<br>int dim = 2         | Unknown  |
|  2 | Tensor<[32]> self = ?,<br>int dim = 0            | Unknown  |

