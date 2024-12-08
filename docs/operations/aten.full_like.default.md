### aten.full_like.default
|    | ATen Input Variations                                                                              | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | None     | Fallback   | 1.0   | -1     |
|  1 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False         | None     | Fallback   | 1.0   | -1     |
|  2 | Tensor<[15, 15]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False         | None     | Fallback   | 1.0   | -1     |
|  3 | Tensor<[17, 17]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False         | Unknown  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[2, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False           | Unknown  | Fallback   | 1.0   | -1     |
|  5 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |

