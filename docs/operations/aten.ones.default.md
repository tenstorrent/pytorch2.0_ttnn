### aten.ones.default
|    | ATen Input Variations                                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 1, 16],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False   | Unknown  | Done       | 1.0   | 0      |
|  1 | List[int] size = [1, 1, 1],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Unknown  | Fallback   | 1.0   | -1     |
|  2 | List[int] size = [1, 1, <s0>],<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[int] size = [1, 1],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Fallback   | 1.0   | -1     |
|  4 | List[int] size = [1, 1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | None     | Fallback   | 1.0   | -1     |
|  5 | List[int] size = [1, 2],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                               | Unknown  | Done       | 1.0   | 0      |
|  6 | List[int] size = [1, 720, 1280],<br>Optional[int] dtype = torch.bool,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Done     | Done       | 1.0   | 0      |
|  7 | List[int] size = [1, <s0 + 1>],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                        | Unknown  | Unknown    | N/A   | N/A    |

