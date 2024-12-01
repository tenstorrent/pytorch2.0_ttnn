### aten.zeros_like.default
|    | ATen Input Variations                                                                                    | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>Optional[bool] pin_memory = False                                            | None     | Fallback   | True  |
|  1 | Tensor<[1, 920]> self = ?,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  2 | Tensor<[100, 1, 256]> self = ?,<br>Optional[bool] pin_memory = False                                     | None     | Fallback   | True  |
|  3 | Tensor<[13685]> self = ?,<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False      | Unknown  | Fallback   | True  |
|  4 | Tensor<[17, 17]> self = ?,<br>Optional[bool] pin_memory = False                                          | Unknown  | Fallback   | True  |
|  5 | Tensor<[2, 2]> self = ?,<br>Optional[bool] pin_memory = False                                            | Unknown  | Done       | True  |
|  6 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Optional[bool] pin_memory = False                                  | Unknown  | Unknown    | N/A   |

