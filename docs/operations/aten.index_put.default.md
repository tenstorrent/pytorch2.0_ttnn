### aten.index_put.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   |   PCC |   Host |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|------:|-------:|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [<[2]>, <[2]>],<br>Tensor<[2, 512]> values = ?,<br>bool accumulate = True | Unknown  | Fallback   |     1 |     -1 |
|  1 | Tensor<[732, 12]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>],<br>Tensor<[38809, 12]> values = ?,<br>bool accumulate = True   | None     | Fallback   |     1 |     -1 |
|  2 | Tensor<[732, 16]> self = ?,<br>List[Optional[Tensor]] indices = [<[38809]>],<br>Tensor<[38809, 16]> values = ?,<br>bool accumulate = True   | None     | Fallback   |     1 |     -1 |

