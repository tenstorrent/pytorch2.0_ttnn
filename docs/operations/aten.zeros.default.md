### aten.zeros.default
|    | ATen Input Variations                                                                                                                                   | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 12, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
|  1 | List[int] size = [1, 12, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
|  2 | List[int] size = [1, 12, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  3 | List[int] size = [1, 120, 14, 14],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
|  4 | List[int] size = [1, 16, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
|  5 | List[int] size = [1, 16, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
|  6 | List[int] size = [1, 16, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | Unknown  | Unknown    | N/A   | N/A    |
|  7 | List[int] size = [1, 18, 14, 14],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
|  8 | List[int] size = [1, 18, 28, 28],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
|  9 | List[int] size = [1, 18, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu       | Done     | Unknown    | N/A   | N/A    |
| 10 | List[int] size = [1, 184, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Done     | Unknown    | N/A   | N/A    |
| 11 | List[int] size = [1, 19],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.int64                                                    | Done     | Unknown    | N/A   | N/A    |
| 12 | List[int] size = [1, 200, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Done     | Unknown    | N/A   | N/A    |
| 13 | List[int] size = [1, 240, 14, 14],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
| 14 | List[int] size = [1, 256, 128, 128],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu  | Done     | Unknown    | N/A   | N/A    |
| 15 | List[int] size = [1, 256, 16, 16],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
| 16 | List[int] size = [1, 256, 32, 32],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
| 17 | List[int] size = [1, 256, 64, 64],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
| 18 | List[int] size = [1, 3, 720, 1280],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False     | Done     | Done       | 1.0   | 0      |
| 19 | List[int] size = [1, 36, 14, 14],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
| 20 | List[int] size = [1, 36, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu       | Done     | Unknown    | N/A   | N/A    |
| 21 | List[int] size = [1, 480, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Done     | Unknown    | N/A   | N/A    |
| 22 | List[int] size = [1, 6, 1, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | 0      |
| 23 | List[int] size = [1, 6, 18, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
| 24 | List[int] size = [1, 6, 3, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | 0      |
| 25 | List[int] size = [1, 6, <s0 + 2>, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  | Unknown    | N/A   | N/A    |
| 26 | List[int] size = [1, 672, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Done     | Unknown    | N/A   | N/A    |
| 27 | List[int] size = [1, 72, 28, 28],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
| 28 | List[int] size = [1, 72, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu       | Done     | Unknown    | N/A   | N/A    |
| 29 | List[int] size = [1, 8, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | 0      |
| 30 | List[int] size = [1, 8, 3, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False         | Unknown  | Done       | 1.0   | 0      |
| 31 | List[int] size = [1, 8, <s0 + 2>, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | Unknown  | Unknown    | N/A   | N/A    |
| 32 | List[int] size = [1, 960, 3, 3],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Done     | Unknown    | N/A   | N/A    |
| 33 | List[int] size = [14, 14],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16                                                | Done     | Unknown    | N/A   | N/A    |
| 34 | List[int] size = [15680],<br>Optional[int] dtype = torch.bfloat16                                                                                       | Done     | Unknown    | N/A   | N/A    |
| 35 | List[int] size = [16, 16],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16                                                | Done     | Unknown    | N/A   | N/A    |
| 36 | List[int] size = [2, 7, 512],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu        | Done     | Unknown    | N/A   | N/A    |
| 37 | List[int] size = [200704],<br>Optional[int] dtype = torch.bfloat16                                                                                      | Done     | Unknown    | N/A   | N/A    |
| 38 | List[int] size = [21952],<br>Optional[int] dtype = torch.bfloat16                                                                                       | Done     | Unknown    | N/A   | N/A    |
| 39 | List[int] size = [28, 28],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16                                                | Done     | Unknown    | N/A   | N/A    |
| 40 | List[int] size = [31360],<br>Optional[int] dtype = torch.bfloat16                                                                                       | Done     | Unknown    | N/A   | N/A    |
| 41 | List[int] size = [32, 32],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16                                                | Done     | Unknown    | N/A   | N/A    |
| 42 | List[int] size = [56, 56],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16                                                | Done     | Unknown    | N/A   | N/A    |
| 43 | List[int] size = [64, 64],<br>Optional[bool] pin_memory = False,<br>Optional[int] dtype = torch.bfloat16                                                | Done     | Unknown    | N/A   | N/A    |
| 44 | List[int] size = [75264],<br>Optional[int] dtype = torch.bfloat16                                                                                       | Done     | Unknown    | N/A   | N/A    |
| 45 | List[int] size = [7840],<br>Optional[int] dtype = torch.bfloat16                                                                                        | Done     | Unknown    | N/A   | N/A    |

