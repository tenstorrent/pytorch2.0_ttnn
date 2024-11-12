### aten._log_softmax.default
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 10]> self = ?,<br>int dim = 1,<br>bool half_to_float = False      | Fallback | Unknown    | N/A   |
|  1 | Tensor<[19, 256008]> self = ?,<br>int dim = 1,<br>bool half_to_float = False | None     | Fallback   | True  |

