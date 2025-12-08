### aten.new_ones.default
|    | ATen Input Variations                                                                                                | Status   | Isolated   | PCC   | Host   |
|---:|:---------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor self = ?,<br>List[int] size = [32],<br>Optional[int] dtype = torch.bool,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 45]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False                           | Unknown  | Fallback   | 1.0   | -1     |
|  2 | Tensor<[1, 59]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False                           | Unknown  | Fallback   | 1.0   | -1     |
|  3 | Tensor<[1, 5]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False                            | Unknown  | Fallback   | 1.0   | -1     |
|  4 | Tensor<[1, s0]> self = ?,<br>List[int] size = [1, 1],<br>Optional[bool] pin_memory = False                           | Unknown  | Unknown    | N/A   | N/A    |

