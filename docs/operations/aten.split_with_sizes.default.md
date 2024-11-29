### aten.split_with_sizes.default
|    | ATen Input Variations                                                                                         | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1  | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 163206, 91]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567],<br>int dim = 1 | Unknown  | Fallback   | True  |
|  2 | Tensor<[163206, 4]> self = ?,<br>List[int] split_sizes = [122400, 30600, 7650, 1989, 567]                     | Unknown  | Fallback   | True  |

