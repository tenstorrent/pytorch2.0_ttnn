### aten.zeros_like.default
|    | ATen Input Variations                                                                                                                 | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False                                                                         | Unknown  | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 8]> self = ?,<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 920]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[bool] pin_memory = False                              | Done     | Unknown    | N/A   | N/A    |
|  3 | Tensor<[100, 1, 256]> self = ?,<br>Optional[bool] pin_memory = False                                                                  | Removed  | Done       | 1.0   | 0      |
|  4 | Tensor<[17, 17]> self = ?,<br>Optional[bool] pin_memory = False                                                                       | Unknown  | Done       | 1.0   | 0      |
|  5 | Tensor<[2, 2]> self = ?,<br>Optional[bool] pin_memory = False                                                                         | Unknown  | Done       | 1.0   | 0      |
|  6 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                                                      | Unknown  | Unknown    | N/A   | N/A    |
|  7 | Tensor<[7145]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False                                    | None     | Unknown    | N/A   | N/A    |
|  8 | Tensor<[7931]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False                                    | None     | Unknown    | N/A   | N/A    |
|  9 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False                                                               | Unknown  | Unknown    | N/A   | N/A    |

