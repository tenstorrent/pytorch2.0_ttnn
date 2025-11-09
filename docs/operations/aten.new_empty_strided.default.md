### aten.new_empty_strided.default
|    | ATen Input Variations                                                                                                    | Status   | Isolated   | PCC                    | Host   |
|---:|:-------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:-----------------------|:-------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>List[int] size = [1, 112, 14, 14],<br>List[int] stride = [21952, 196, 14, 1]       | Removed  | Fallback   | 0.016795289712988246   | -1     |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>List[int] size = [1, 16, 112, 112],<br>List[int] stride = [200704, 12544, 112, 1] | Removed  | Fallback   | 0.052468556275502856   | -1     |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>List[int] size = [1, 160, 7, 7],<br>List[int] stride = [7840, 49, 7, 1]              | Removed  | Fallback   | 0.03193115311736884    | -1     |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] size = [1, 24, 56, 56],<br>List[int] stride = [75264, 3136, 56, 1]        | Removed  | Fallback   | 2.4207675388270247e-05 | -1     |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>List[int] size = [1, 40, 28, 28],<br>List[int] stride = [31360, 784, 28, 1]         | Removed  | Fallback   | -0.033093045377852716  | -1     |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>List[int] size = [1, 80, 14, 14],<br>List[int] stride = [15680, 196, 14, 1]         | Removed  | Fallback   | 0.05707147155551542    | -1     |
|  6 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384, 3, 3],<br>List[int] stride = [9, 3, 1]                       | Removed  | Unknown    | N/A                    | N/A    |

