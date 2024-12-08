### aten.full.default
|    | ATen Input Variations                                                                                                                                                                | Status   | Isolated   |   PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | List[int] size = [19, 19],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                    | None     | Fallback   |     1 |     -1 |
|  1 | List[int] size = [32, 32],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                    | Done     | Done       |     1 |      0 |
|  2 | List[int] size = [45, 45],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                    | None     | Fallback   |     1 |     -1 |
|  3 | List[int] size = [59, 59],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                    | None     | Fallback   |     1 |     -1 |
|  4 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                                      | None     | Fallback   |     1 |     -1 |
|  5 | List[int] size = [],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   |     1 |     -1 |
|  6 | List[int] size = [],<br>number fill_value = 8.0,<br>Optional[int] dtype = torch.bfloat16,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False                     | Removed  | Fallback   |     1 |     -1 |

