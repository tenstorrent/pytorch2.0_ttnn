### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999947822817797 | 0      |
|  2 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999951472942457 | 0      |
|  3 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999980426089593 | 0      |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999987768761183 | 0      |
|  5 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999990274130373 | 0      |
|  8 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999936884340389 | 0      |
| 10 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999961864217851 | 0      |
| 11 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999940773848972 | 0      |
| 12 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999969789870853 | 0      |
| 13 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 14 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999928437437072 | 0      |
| 15 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999817599154457 | 0      |
| 16 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999942372995863 | 0      |
| 17 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999914291874858 | 0      |
| 18 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999929380442814 | 0      |
| 19 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999966102819641 | 0      |
| 20 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999986585613534 | 0      |
| 21 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0       | Done     | Done       | 1.0                | 0      |
| 22 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999868834572346 | 0      |
| 23 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
| 27 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999950808449549 | 0      |
| 28 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999936332895528 | 0      |
| 29 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999900864608666 | 0      |
| 30 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999848092234477 | 0      |
| 31 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999942872946725 | 0      |
| 32 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999929689287935 | 0      |
| 33 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.999993949216716  | 0      |
| 34 | Tensor<[1, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Unknown    | N/A                | N/A    |
| 35 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999919297363774 | 0      |

