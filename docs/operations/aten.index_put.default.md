### aten.index_put.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 51865]> self = ?,<br>List[Optional[Tensor]] indices = [None, <[51865]>],<br>Tensor values = ?                                    | Unknown  | Unknown    | N/A   | N/A    |
|  1 | Tensor<[1, 51865]> self = ?,<br>List[Optional[Tensor]] indices = [None, _folded_lift_fresh_copy_1],<br>Tensor values = ?                    | Unknown  | Unknown    | N/A   | N/A    |
|  2 | Tensor<[1, 51865]> self = ?,<br>List[Optional[Tensor]] indices = [None, _folded_lift_fresh_copy_3],<br>Tensor values = ?                    | Unknown  | Unknown    | N/A   | N/A    |
|  3 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [<[2]>, <[2]>],<br>Tensor<[2, 512]> values = ?,<br>bool accumulate = True | None     | Fallback   | 1.0   | -1     |
|  4 | Tensor<[24, 24]> self = ?,<br>List[Optional[Tensor]] indices = [<[24, 24]>],<br>Tensor values = ?                                           | None     | Unknown    | N/A   | N/A    |
|  5 | Tensor<[51865]> self = ?,<br>List[Optional[Tensor]] indices = [_folded_lift_fresh_copy_1],<br>Tensor values = ?                             | Unknown  | Unknown    | N/A   | N/A    |

