### aten.new_empty_strided.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC                     | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------------------------|:-------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>List[int] size = [1, 112, 14, 14],<br>List[int] stride = [21952, 196, 14, 1]       | Removed  | Fallback   | 0.7070745659637354      | -1     |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>List[int] size = [1, 16, 112, 112],<br>List[int] stride = [200704, 12544, 112, 1] | Removed  | Fallback   | 0.002577967064676078    | -1     |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>List[int] size = [1, 160, 7, 7],<br>List[int] stride = [7840, 49, 7, 1]              | Removed  | Fallback   | -0.011227804097364725   | -1     |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] size = [1, 24, 56, 56],<br>List[int] stride = [75264, 3136, 56, 1]        | Removed  | Fallback   | 0.011122822062930615    | -1     |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>List[int] size = [1, 40, 28, 28],<br>List[int] stride = [31360, 784, 28, 1]         | Removed  | Fallback   | 0.03898749847736122     | -1     |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>List[int] size = [1, 80, 14, 14],<br>List[int] stride = [15680, 196, 14, 1]         | Removed  | Fallback   | -0.00015624155238846122 | -1     |
|  6 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384, 3, 3],<br>List[int] stride = [9, 3, 1]                       | Removed  | Unknown    | N/A                     | N/A    |

