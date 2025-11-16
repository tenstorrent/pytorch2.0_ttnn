### aten.zeros.default
|    | ATen Input Variations                                                                                                                                  | Status   | Isolated   | PCC   | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | List[int] size = [1, 12, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False       | Unknown  | Done       | 1.0   | 0      |
|  1 | List[int] size = [1, 120, 14, 14],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Unknown    | N/A   | N/A    |
|  2 | List[int] size = [1, 16, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False       | Unknown  | Done       | 1.0   | 0      |
|  3 | List[int] size = [1, 18, 14, 14],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
|  4 | List[int] size = [1, 18, 28, 28],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
|  5 | List[int] size = [1, 18, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Done     | Unknown    | N/A   | N/A    |
|  6 | List[int] size = [1, 184, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
|  7 | List[int] size = [1, 200, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
|  8 | List[int] size = [1, 240, 14, 14],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Unknown    | N/A   | N/A    |
|  9 | List[int] size = [1, 256, 128, 128],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Done     | Unknown    | N/A   | N/A    |
| 10 | List[int] size = [1, 256, 16, 16],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Unknown    | N/A   | N/A    |
| 11 | List[int] size = [1, 256, 32, 32],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Unknown    | N/A   | N/A    |
| 12 | List[int] size = [1, 256, 64, 64],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu   | Done     | Unknown    | N/A   | N/A    |
| 13 | List[int] size = [1, 3, 720, 1280],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False    | Removed  | Done       | 1.0   | 0      |
| 14 | List[int] size = [1, 36, 14, 14],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
| 15 | List[int] size = [1, 36, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Done     | Unknown    | N/A   | N/A    |
| 16 | List[int] size = [1, 480, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
| 17 | List[int] size = [1, 6, 1, 15],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
| 18 | List[int] size = [1, 672, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
| 19 | List[int] size = [1, 72, 28, 28],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu    | Done     | Unknown    | N/A   | N/A    |
| 20 | List[int] size = [1, 72, 7, 7],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu      | Done     | Unknown    | N/A   | N/A    |
| 21 | List[int] size = [1, 8, 1, 10],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False        | Unknown  | Done       | 1.0   | 0      |
| 22 | List[int] size = [1, 960, 3, 3],<br>Optional[int] dtype = torch.float32,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu     | Done     | Unknown    | N/A   | N/A    |
| 23 | List[int] size = [16384, 3, 3],<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                                 | Done     | Unknown    | N/A   | N/A    |
| 24 | List[int] size = [1],<br>Optional[int] dtype = torch.int64,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                     | Unknown  | Unknown    | N/A   | N/A    |
| 25 | List[int] size = [2, 7, 512],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu       | Done     | Unknown    | N/A   | N/A    |

