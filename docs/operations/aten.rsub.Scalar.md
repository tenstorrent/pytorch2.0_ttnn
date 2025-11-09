### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999995202870321  | 0      |
|  2 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999993515841903 | 0      |
|  3 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999950099106276 | 0      |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 1.0                | 0      |
|  5 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999898640160385 | 0      |
|  8 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 1, 1, 201]> self = ?,<br>number other = 1.0     | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999949923550417 | 0      |
| 11 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999972766133727 | 0      |
| 12 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999933097923591 | 0      |
| 13 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 14 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999918462413617 | 0      |
| 15 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.999991239514937  | 0      |
| 16 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999925705885033 | 0      |
| 17 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 18 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999953000788449 | 0      |
| 19 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999975680468783 | 0      |
| 20 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999842446080766 | 0      |
| 21 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999907829774229 | 0      |
| 22 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.999994667803498  | 0      |
| 27 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999997583634473 | 0      |
| 28 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999861724459411 | 0      |
| 29 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999950680770348 | 0      |
| 30 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999949010475493 | 0      |
| 31 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.999994715058286  | 0      |
| 32 | Tensor<[1, 192]> self = ?,<br>number other = 1             | Unknown  | Unknown    | N/A                | N/A    |
| 33 | Tensor<[16384]> self = ?,<br>number other = 1              | Done     | Unknown    | N/A                | N/A    |
| 34 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999950697826485 | 0      |
| 35 | Tensor<[8, 1, 1, 384]> self = ?,<br>number other = 1.0     | Done     | Unknown    | N/A                | N/A    |

