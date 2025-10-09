### aten.as_strided.default
|    | ATen Input Variations                                                                                                                                         | Status   | Isolated   | PCC   | Host   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|  0 | Tensor<[1, 1024, 1, 1]> self = ?,<br>List[int] size = [1, 1024, 1, 1],<br>List[int] stride = [1024, 1, 1024, 1024]                                            | Done     | Done       | 1.0   | 0      |
|  1 | Tensor<[1, 112, 14, 14]> self = ?,<br>List[int] size = [1, 112, 14, 14],<br>List[int] stride = [21952, 196, 14, 1],<br>Optional[int] storage_offset = 0       | Done     | Done       | 1.0   | 0      |
|  2 | Tensor<[1, 16, 112, 112]> self = ?,<br>List[int] size = [1, 16, 112, 112],<br>List[int] stride = [200704, 12544, 112, 1],<br>Optional[int] storage_offset = 0 | Done     | Done       | 1.0   | 0      |
|  3 | Tensor<[1, 160, 7, 7]> self = ?,<br>List[int] size = [1, 160, 7, 7],<br>List[int] stride = [7840, 49, 7, 1],<br>Optional[int] storage_offset = 0              | Done     | Done       | 1.0   | 0      |
|  4 | Tensor<[1, 24, 56, 56]> self = ?,<br>List[int] size = [1, 24, 56, 56],<br>List[int] stride = [75264, 3136, 56, 1],<br>Optional[int] storage_offset = 0        | Done     | Done       | 1.0   | 0      |
|  5 | Tensor<[1, 40, 28, 28]> self = ?,<br>List[int] size = [1, 40, 28, 28],<br>List[int] stride = [31360, 784, 28, 1],<br>Optional[int] storage_offset = 0         | Done     | Done       | 1.0   | 0      |
|  6 | Tensor<[1, 768, 1, 1]> self = ?,<br>List[int] size = [1, 768, 1, 1],<br>List[int] stride = [768, 1, 768, 768]                                                 | Done     | Done       | 1.0   | 0      |
|  7 | Tensor<[1, 80, 14, 14]> self = ?,<br>List[int] size = [1, 80, 14, 14],<br>List[int] stride = [15680, 196, 14, 1],<br>Optional[int] storage_offset = 0         | Done     | Done       | 1.0   | 0      |
|  8 | Tensor<[15680]> self = ?,<br>List[int] size = [1, 80, 14, 14],<br>List[int] stride = [15680, 196, 14, 1],<br>Optional[int] storage_offset = 0                 | Done     | Done       | 1.0   | 0      |
|  9 | Tensor<[15680]> self = ?,<br>List[int] size = [80, 14, 14],<br>List[int] stride = [196, 14, 1],<br>Optional[int] storage_offset = 0                           | Removed  | Done       | 1.0   | 0      |
| 10 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 0                                   | None     | Unknown    | N/A   | N/A    |
| 11 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 1                                   | None     | Unknown    | N/A   | N/A    |
| 12 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 2                                   | None     | Unknown    | N/A   | N/A    |
| 13 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 3                                   | None     | Unknown    | N/A   | N/A    |
| 14 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 4                                   | None     | Unknown    | N/A   | N/A    |
| 15 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 5                                   | None     | Unknown    | N/A   | N/A    |
| 16 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 6                                   | None     | Unknown    | N/A   | N/A    |
| 17 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 7                                   | None     | Unknown    | N/A   | N/A    |
| 18 | Tensor<[16384, 3, 3]> self = ?,<br>List[int] size = [16384],<br>List[int] stride = [9],<br>Optional[int] storage_offset = 8                                   | None     | Unknown    | N/A   | N/A    |
| 19 | Tensor<[200704]> self = ?,<br>List[int] size = [1, 16, 112, 112],<br>List[int] stride = [200704, 12544, 112, 1],<br>Optional[int] storage_offset = 0          | Done     | Done       | 1.0   | 0      |
| 20 | Tensor<[200704]> self = ?,<br>List[int] size = [16, 112, 112],<br>List[int] stride = [12544, 112, 1],<br>Optional[int] storage_offset = 0                     | Removed  | Done       | 1.0   | 0      |
| 21 | Tensor<[21952]> self = ?,<br>List[int] size = [1, 112, 14, 14],<br>List[int] stride = [21952, 196, 14, 1],<br>Optional[int] storage_offset = 0                | Done     | Done       | 1.0   | 0      |
| 22 | Tensor<[21952]> self = ?,<br>List[int] size = [112, 14, 14],<br>List[int] stride = [196, 14, 1],<br>Optional[int] storage_offset = 0                          | Removed  | Done       | 1.0   | 0      |
| 23 | Tensor<[31360]> self = ?,<br>List[int] size = [1, 40, 28, 28],<br>List[int] stride = [31360, 784, 28, 1],<br>Optional[int] storage_offset = 0                 | Done     | Done       | 1.0   | 0      |
| 24 | Tensor<[31360]> self = ?,<br>List[int] size = [40, 28, 28],<br>List[int] stride = [784, 28, 1],<br>Optional[int] storage_offset = 0                           | Removed  | Done       | 1.0   | 0      |
| 25 | Tensor<[75264]> self = ?,<br>List[int] size = [1, 24, 56, 56],<br>List[int] stride = [75264, 3136, 56, 1],<br>Optional[int] storage_offset = 0                | Done     | Done       | 1.0   | 0      |
| 26 | Tensor<[75264]> self = ?,<br>List[int] size = [24, 56, 56],<br>List[int] stride = [3136, 56, 1],<br>Optional[int] storage_offset = 0                          | Removed  | Done       | 1.0   | 0      |
| 27 | Tensor<[7840]> self = ?,<br>List[int] size = [1, 160, 7, 7],<br>List[int] stride = [7840, 49, 7, 1],<br>Optional[int] storage_offset = 0                      | Done     | Done       | 1.0   | 0      |
| 28 | Tensor<[7840]> self = ?,<br>List[int] size = [160, 7, 7],<br>List[int] stride = [49, 7, 1],<br>Optional[int] storage_offset = 0                               | Removed  | Done       | 1.0   | 0      |

