### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999982263414897 | 0      |
|  2 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999989729531533 | 0      |
|  3 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999994610597123 | 0      |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.999991884366441  | 0      |
|  5 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, 16]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999948231466672 | 0      |
|  8 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 1, 1, 201]> self = ?,<br>number other = 1.0     | Unknown  | Unknown    | N/A                | N/A    |
| 10 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999945992635407 | 0      |
| 11 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999900885681069 | 0      |
| 12 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999978794092971 | 0      |
| 13 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 14 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999951357482797 | 0      |
| 15 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999876500491267 | 0      |
| 16 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999944833138168 | 0      |
| 17 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 18 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999921594261029 | 0      |
| 19 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 20 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.999999534365618  | 0      |
| 21 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999856799933269 | 0      |
| 22 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 1.0      | Done     | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 1, 16, 1]> self = ?,<br>number other = 2.0      | Done     | Unknown    | N/A                | N/A    |
| 26 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.999995011349279  | 0      |
| 27 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999900825077663 | 0      |
| 28 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.999980979682059  | 0      |
| 29 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999938834006272 | 0      |
| 30 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999948298382071 | 0      |
| 31 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999941248345604 | 0      |
| 32 | Tensor<[1, 192]> self = ?,<br>number other = 1             | Unknown  | Unknown    | N/A                | N/A    |
| 33 | Tensor<[16384]> self = ?,<br>number other = 1              | Done     | Unknown    | N/A                | N/A    |
| 34 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999933077885587 | 0      |
| 35 | Tensor<[8, 1, 1, 384]> self = ?,<br>number other = 1.0     | Done     | Unknown    | N/A                | N/A    |

