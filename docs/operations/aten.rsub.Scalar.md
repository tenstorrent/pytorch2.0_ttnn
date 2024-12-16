### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 1.0                | 0      |
|  2 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999993287037305  | 0      |
|  3 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999991118468793 | 0      |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999932655472222 | 0      |
|  5 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.999991151804003  | 0      |
|  6 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
|  7 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999931423770714 | 0      |
|  8 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999916254409925 | 0      |
|  9 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999924332275347 | 0      |
| 10 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999979137395817 | 0      |
| 11 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 12 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999912677340099 | 0      |
| 13 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999707573220222 | 0      |
| 14 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999929175225554 | 0      |
| 15 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 16 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999940801601043 | 0      |
| 17 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999895988836175 | 0      |
| 18 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999230747500724 | 0      |
| 19 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999970961650901 | 0      |
| 20 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999954098392032 | 0      |
| 21 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999945113970755 | 0      |
| 24 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999917566693735 | 0      |
| 25 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999991343546474  | 0      |
| 26 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999936937713435 | 0      |
| 27 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999940855756682 | 0      |
| 28 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999933740075981 | 0      |
| 29 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999939000762893 | 0      |
| 30 | Tensor<[1066]> self = ?,<br>number other = 1.0             | Unknown  | Done       | 0.9999934467739187 | 0      |
| 31 | Tensor<[120, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999935649184094 | 0      |
| 32 | Tensor<[128, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999913632535309 | 0      |
| 33 | Tensor<[128]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999936180812434 | 0      |
| 34 | Tensor<[160]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999909421930226 | 0      |
| 35 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.99999682689818   | 0      |
| 36 | Tensor<[240, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999953448743524 | 0      |
| 37 | Tensor<[30, 1]> self = ?,<br>number other = 1.0            | Removed  | Done       | 0.9999974812542047 | 0      |
| 38 | Tensor<[300, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999947200796043 | 0      |
| 39 | Tensor<[300]> self = ?,<br>number other = 1.0              | Unknown  | Done       | 0.9999925573115563 | 0      |
| 40 | Tensor<[320, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999949574921293 | 0      |
| 41 | Tensor<[320]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999942092287085 | 0      |
| 42 | Tensor<[40]> self = ?,<br>number other = 1.0               | Removed  | Done       | 0.9999920115213194 | 0      |
| 43 | Tensor<[480, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999941047336    | 0      |
| 44 | Tensor<[60, 1]> self = ?,<br>number other = 1.0            | Removed  | Done       | 0.9999907125695677 | 0      |
| 45 | Tensor<[640]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999934442580577 | 0      |
| 46 | Tensor<[800, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999928922424477 | 0      |
| 47 | Tensor<[80]> self = ?,<br>number other = 1.0               | Removed  | Done       | 0.9999929030380841 | 0      |

