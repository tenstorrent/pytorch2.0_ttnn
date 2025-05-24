### aten.argmax.default
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 51865]> self = ?,<br>Optional[int] dim = -1                    | Unknown  | Fallback   | 1.0   | -1     |
|  1 | Tensor<[1, 7]> self = ?,<br>Optional[int] dim = 1,<br>bool keepdim = True | None     | Unknown    | N/A   | N/A    |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1                        | None     | Fallback   | 1.0   | -1     |

