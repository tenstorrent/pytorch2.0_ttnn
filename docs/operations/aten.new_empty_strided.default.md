### aten.new_empty_strided.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   |          PCC |   Host |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|-------------:|-------:|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>List[int] size = [1, 112, 14, 14],<br>List[int] stride = [21952, 196, 14, 1]       | Removed  | Fallback   | -0.000235215 |     -1 |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>List[int] size = [1, 16, 112, 112],<br>List[int] stride = [200704, 12544, 112, 1] | Removed  | Fallback   | -0.003755    |     -1 |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>List[int] size = [1, 160, 7, 7],<br>List[int] stride = [7840, 49, 7, 1]              | Removed  | Fallback   | -0.00553902  |     -1 |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] size = [1, 24, 56, 56],<br>List[int] stride = [75264, 3136, 56, 1]        | Removed  | Fallback   |  0.000282385 |     -1 |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>List[int] size = [1, 40, 28, 28],<br>List[int] stride = [31360, 784, 28, 1]         | Removed  | Fallback   |  0.000295704 |     -1 |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>List[int] size = [1, 80, 14, 14],<br>List[int] stride = [15680, 196, 14, 1]         | Removed  | Fallback   | -0.00190167  |     -1 |

