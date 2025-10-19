### aten.new_empty_strided.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC                    | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-----------------------|:-------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>List[int] size = [1, 112, 14, 14],<br>List[int] stride = [21952, 196, 14, 1]       | Removed  | Fallback   | 0.00018663532249256674 | -1     |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>List[int] size = [1, 16, 112, 112],<br>List[int] stride = [200704, 12544, 112, 1] | Removed  | Fallback   | 0.005173012195474387   | -1     |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>List[int] size = [1, 160, 7, 7],<br>List[int] stride = [7840, 49, 7, 1]              | Removed  | Fallback   | -0.0006945654445164933 | -1     |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] size = [1, 24, 56, 56],<br>List[int] stride = [75264, 3136, 56, 1]        | Removed  | Fallback   | 0.9422606456618138     | -1     |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>List[int] size = [1, 40, 28, 28],<br>List[int] stride = [31360, 784, 28, 1]         | Removed  | Fallback   | 0.00015582298733106997 | -1     |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>List[int] size = [1, 80, 14, 14],<br>List[int] stride = [15680, 196, 14, 1]         | Removed  | Fallback   | 0.00031182614656930684 | -1     |
|  6 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384, 3, 3],<br>List[int] stride = [9, 3, 1]                       | Removed  | Unknown    | N/A                    | N/A    |

