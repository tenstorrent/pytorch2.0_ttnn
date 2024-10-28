### aten.zeros.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [1, 12, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | True  |
|  1 | List[int] size = [1, 12, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | True  |
|  2 | List[int] size = [1, 12, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
|  3 | List[int] size = [1, 16, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | True  |
|  4 | List[int] size = [1, 16, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | True  |
|  5 | List[int] size = [1, 16, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   |
|  6 | List[int] size = [1, 3, 720, 1280],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | None     | Fallback   | True  |
|  7 | List[int] size = [1, 6, 1, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Fallback   | True  |
|  8 | List[int] size = [1, 6, 18, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Fallback   | True  |
|  9 | List[int] size = [1, 6, 3, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Fallback   | True  |
| 10 | List[int] size = [1, 6, <s0 + 2>, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  | Unknown    | N/A   |
| 11 | List[int] size = [1, 8, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Fallback   | True  |
| 12 | List[int] size = [1, 8, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Fallback   | True  |
| 13 | List[int] size = [1, 8, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  | Unknown    | N/A   |

