### aten._softmax.default
|    | ATen Input Variations                                                          | Status   | Isolated   |      PCC |   Host |
|---:|:-------------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 12, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Removed  | Done       | 0.999511 |      0 |
|  1 | Tensor<[1, 16, 9, 9]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Removed  | Done       | 0.999541 |      0 |

