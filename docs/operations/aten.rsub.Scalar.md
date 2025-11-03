### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999993657659829  | 0      |
|  2 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999918904117908 | 0      |
|  3 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 1.0                | 0      |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.999996796294375  | 0      |
|  5 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999896675342999 | 0      |
|  8 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 1, 1, 201]> self = ?,<br>number other = 1.0     | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999940339107027 | 0      |
| 11 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999993008650957 | 0      |
| 12 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999993234207962  | 0      |
| 13 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 14 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999953652057082 | 0      |
| 15 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999875391530572 | 0      |
| 16 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999965142346149 | 0      |
| 17 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.999986074158243  | 0      |
| 18 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999957796105807 | 0      |
| 19 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 20 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 1.0                | 0      |
| 21 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999838069359805 | 0      |
| 22 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999942389211034 | 0      |
| 27 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999962445514686 | 0      |
| 28 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999932984861286 | 0      |
| 29 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999938242530653 | 0      |
| 30 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999941879644182 | 0      |
| 31 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999944307911108 | 0      |
| 32 | Tensor<[1, 192]> self = ?,<br>number other = 1             | Unknown  | Unknown    | N/A                | N/A    |
| 33 | Tensor<[16384]> self = ?,<br>number other = 1              | Done     | Unknown    | N/A                | N/A    |
| 34 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999951802902768 | 0      |
| 35 | Tensor<[8, 1, 1, 384]> self = ?,<br>number other = 1.0     | Done     | Unknown    | N/A                | N/A    |

