### aten.new_full.default
|    | ATen Input Variations                                                                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[3, 300, 300]> self = ?,<br>List[int] size = [1, 3, 300, 300],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False   | None     | Fallback   | True  |
|  1 | Tensor<[3, 320, 320]> self = ?,<br>List[int] size = [1, 3, 320, 320],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False   | None     | Fallback   | True  |
|  2 | Tensor<[3, 800, 1066]> self = ?,<br>List[int] size = [1, 3, 800, 1088],<br>number fill_value = 0,<br>Optional[bool] pin_memory = False | None     | Unknown    | N/A   |

