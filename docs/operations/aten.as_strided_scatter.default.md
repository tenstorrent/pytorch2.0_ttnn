### aten.as_strided_scatter.default
|    | ATen Input Variations                                                                                                                                                                               | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> src = ?,<br>List[int] size = [1, 112, 14, 14],<br>List[int] stride = [21952, 196, 14, 1],<br>Optional[int] storage_offset = 0        | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> src = ?,<br>List[int] size = [1, 16, 112, 112],<br>List[int] stride = [200704, 12544, 112, 1],<br>Optional[int] storage_offset = 0 | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> src = ?,<br>List[int] size = [1, 160, 7, 7],<br>List[int] stride = [7840, 49, 7, 1],<br>Optional[int] storage_offset = 0                 | None     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> src = ?,<br>List[int] size = [1, 24, 56, 56],<br>List[int] stride = [75264, 3136, 56, 1],<br>Optional[int] storage_offset = 0          | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> src = ?,<br>List[int] size = [1, 40, 28, 28],<br>List[int] stride = [31360, 784, 28, 1],<br>Optional[int] storage_offset = 0           | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> src = ?,<br>List[int] size = [1, 80, 14, 14],<br>List[int] stride = [15680, 196, 14, 1],<br>Optional[int] storage_offset = 0           | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[15680]> self = ?,<br>Tensor<[80, 14, 14]> src = ?,<br>List[int] size = [80, 14, 14],<br>List[int] stride = [196, 14, 1],<br>Optional[int] storage_offset = 0                                | None     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[200704]> self = ?,<br>Tensor<[16, 112, 112]> src = ?,<br>List[int] size = [16, 112, 112],<br>List[int] stride = [12544, 112, 1],<br>Optional[int] storage_offset = 0                        | None     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[21952]> self = ?,<br>Tensor<[112, 14, 14]> src = ?,<br>List[int] size = [112, 14, 14],<br>List[int] stride = [196, 14, 1],<br>Optional[int] storage_offset = 0                              | None     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[31360]> self = ?,<br>Tensor<[40, 28, 28]> src = ?,<br>List[int] size = [40, 28, 28],<br>List[int] stride = [784, 28, 1],<br>Optional[int] storage_offset = 0                                | None     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[75264]> self = ?,<br>Tensor<[24, 56, 56]> src = ?,<br>List[int] size = [24, 56, 56],<br>List[int] stride = [3136, 56, 1],<br>Optional[int] storage_offset = 0                               | None     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[7840]> self = ?,<br>Tensor<[160, 7, 7]> src = ?,<br>List[int] size = [160, 7, 7],<br>List[int] stride = [49, 7, 1],<br>Optional[int] storage_offset = 0                                     | None     | N/A                 | N/A          | N/A               | N/A                |
