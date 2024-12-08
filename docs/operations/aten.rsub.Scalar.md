### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999596956322135 | 0      |
|  1 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999958086921708 | 0      |
|  2 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999973904795901 | 0      |
|  3 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999969256605247 | 0      |
|  4 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.999993882207609  | 0      |
|  5 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Done     | Done       | 1.0                | 0      |
|  6 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999929908919234 | 0      |
|  7 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999913428836283 | 0      |
|  8 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999920678560228 | 0      |
|  9 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999942110152779 | 0      |
| 10 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 11 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999941085748334 | 0      |
| 12 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.999974496765761  | 0      |
| 13 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999937241066438 | 0      |
| 14 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999993205158546 | 0      |
| 15 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999938831207593 | 0      |
| 16 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 17 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999952083184137 | 0      |
| 18 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999968534693725 | 0      |
| 19 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999961481208242 | 0      |
| 20 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 21 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.999993611969228  | 0      |
| 23 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999942311564854 | 0      |
| 24 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999995846720163  | 0      |
| 25 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.99997523474052   | 0      |
| 26 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.999994060948735  | 0      |
| 27 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999941537924442 | 0      |
| 28 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999936612089609 | 0      |
| 29 | Tensor<[1066]> self = ?,<br>number other = 1.0             | Done     | Done       | 0.999992753339491  | 0      |
| 30 | Tensor<[120, 1]> self = ?,<br>number other = 1.0           | Done     | Done       | 0.9999940964690665 | 0      |
| 31 | Tensor<[128, 1]> self = ?,<br>number other = 1.0           | Done     | Done       | 0.999992572385261  | 0      |
| 32 | Tensor<[128]> self = ?,<br>number other = 1.0              | Done     | Done       | 0.9999930913382195 | 0      |
| 33 | Tensor<[160]> self = ?,<br>number other = 1.0              | Done     | Done       | 0.9999930495216219 | 0      |
| 34 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999945079586161 | 0      |
| 35 | Tensor<[240, 1]> self = ?,<br>number other = 1.0           | Done     | Done       | 0.9999934334972345 | 0      |
| 36 | Tensor<[30, 1]> self = ?,<br>number other = 1.0            | Done     | Done       | 0.9999950838063046 | 0      |
| 37 | Tensor<[300, 1]> self = ?,<br>number other = 1.0           | Done     | Done       | 0.9999942229648737 | 0      |
| 38 | Tensor<[300]> self = ?,<br>number other = 1.0              | Done     | Done       | 0.999994746240498  | 0      |
| 39 | Tensor<[320, 1]> self = ?,<br>number other = 1.0           | Done     | Done       | 0.9999941335921247 | 0      |
| 40 | Tensor<[320]> self = ?,<br>number other = 1.0              | Done     | Done       | 0.9999925686004039 | 0      |
| 41 | Tensor<[40]> self = ?,<br>number other = 1.0               | Done     | Done       | 0.9999892821658735 | 0      |
| 42 | Tensor<[480, 1]> self = ?,<br>number other = 1.0           | Done     | Done       | 0.9999930652672983 | 0      |
| 43 | Tensor<[60, 1]> self = ?,<br>number other = 1.0            | Done     | Done       | 0.9999934378311879 | 0      |
| 44 | Tensor<[640]> self = ?,<br>number other = 1.0              | Done     | Done       | 0.9999934847416396 | 0      |
| 45 | Tensor<[800, 1]> self = ?,<br>number other = 1.0           | Done     | Done       | 0.999993940900421  | 0      |
| 46 | Tensor<[80]> self = ?,<br>number other = 1.0               | Done     | Done       | 0.9999965195534918 | 0      |

