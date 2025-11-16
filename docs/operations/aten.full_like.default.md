### aten.full_like.default
|    | ATen Input Variations                                                                                                                                             | Status   | Isolated   | PCC   | Host   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 193]> self = ?,<br>number fill_value = 1,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False                                                                          | Unknown  | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 2]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False                                                                          | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[1, s0 + 1]> self = ?,<br>number fill_value = 31,<br>Optional[bool] pin_memory = False                                                                     | Unknown  | Unknown    | N/A   | N/A    |
|  4 | Tensor<[10, 10]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False                                                                        | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[15, 15]> self = ?,<br>number fill_value = 15,<br>Optional[bool] pin_memory = False                                                                        | Unknown  | Done       | 1.0   | 0      |

