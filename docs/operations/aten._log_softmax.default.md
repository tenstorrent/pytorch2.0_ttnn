### aten._log_softmax.default
|    | ATen Input Variations                                                        | Status   | Isolated   |      PCC |   Host |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False      | Removed  | Done       | 0.999885 |      0 |
|  1 | Tensor<[19, 256008]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | None     | Fallback   | 1        |     -1 |

