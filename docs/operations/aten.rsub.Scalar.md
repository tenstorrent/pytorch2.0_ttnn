### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999921662401398 | 0      |
|  2 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999979202950194 | 0      |
|  3 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999892715045987 | 0      |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999954966249821 | 0      |
|  5 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999903960859776 | 0      |
|  6 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
|  7 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999933524995823 | 0      |
|  8 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999957295269806 | 0      |
|  9 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999955388892281 | 0      |
| 10 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999953945101941 | 0      |
| 11 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 12 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999965219205046 | 0      |
| 13 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999819433084679 | 0      |
| 14 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999960071823722 | 0      |
| 15 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999951324853193 | 0      |
| 16 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999920933761643 | 0      |
| 17 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999945648040641 | 0      |
| 18 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999935721413614 | 0      |
| 19 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999961627214684 | 0      |
| 20 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999978123926017 | 0      |
| 21 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999936062058851 | 0      |
| 24 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999935443739892 | 0      |
| 25 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999885247241564 | 0      |
| 26 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999688222317672 | 0      |
| 27 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999945314790749 | 0      |
| 28 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.999994058686145  | 0      |
| 29 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999931676661173 | 0      |
| 30 | Tensor<[1066]> self = ?,<br>number other = 1.0             | Unknown  | Done       | 0.9999923458381076 | 0      |
| 31 | Tensor<[120, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999925113897685 | 0      |
| 32 | Tensor<[128, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.999993518621321  | 0      |
| 33 | Tensor<[128]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.999993377954144  | 0      |
| 34 | Tensor<[160]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999950943181362 | 0      |
| 35 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999964580524975 | 0      |
| 36 | Tensor<[240, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999950347655374 | 0      |
| 37 | Tensor<[30, 1]> self = ?,<br>number other = 1.0            | Removed  | Done       | 0.9999911737321435 | 0      |
| 38 | Tensor<[300, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999930973212504 | 0      |
| 39 | Tensor<[300]> self = ?,<br>number other = 1.0              | Unknown  | Done       | 0.9999950805464375 | 0      |
| 40 | Tensor<[320, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999942551665676 | 0      |
| 41 | Tensor<[320]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999945508518637 | 0      |
| 42 | Tensor<[40]> self = ?,<br>number other = 1.0               | Removed  | Done       | 0.9999917506964872 | 0      |
| 43 | Tensor<[480, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999925961382937 | 0      |
| 44 | Tensor<[60, 1]> self = ?,<br>number other = 1.0            | Removed  | Done       | 0.999991071076141  | 0      |
| 45 | Tensor<[640]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999942211331171 | 0      |
| 46 | Tensor<[800, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999927837308807 | 0      |
| 47 | Tensor<[80]> self = ?,<br>number other = 1.0               | Removed  | Done       | 0.9999918643671107 | 0      |

