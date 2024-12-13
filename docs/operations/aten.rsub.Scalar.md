### aten.rsub.Scalar
|    | ATen Input Variations                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>number other = 1.0                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor<[1, 1, 1, 10]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999995349791064  | 0      |
|  2 | Tensor<[1, 1, 1, 12]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999962928312499 | 0      |
|  3 | Tensor<[1, 1, 1, 14]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999971306194576 | 0      |
|  4 | Tensor<[1, 1, 1, 15]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999956369653931 | 0      |
|  5 | Tensor<[1, 1, 1, 17]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999922125262466 | 0      |
|  6 | Tensor<[1, 1, 1, 1]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
|  7 | Tensor<[1, 1, 1, 2048]> self = ?,<br>number other = 1.0    | Done     | Done       | 0.9999935881457128 | 0      |
|  8 | Tensor<[1, 1, 1, 24]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999992123932128  | 0      |
|  9 | Tensor<[1, 1, 1, 256]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999940415323928 | 0      |
| 10 | Tensor<[1, 1, 1, 25]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999864310638981 | 0      |
| 11 | Tensor<[1, 1, 1, 2]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 12 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.999996394687442  | 0      |
| 13 | Tensor<[1, 1, 1, 42]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999880730015285 | 0      |
| 14 | Tensor<[1, 1, 1, 46]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999916048261457 | 0      |
| 15 | Tensor<[1, 1, 1, 5]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 1.0                | 0      |
| 16 | Tensor<[1, 1, 1, 60]> self = ?,<br>number other = 1.0      | Unknown  | Done       | 0.9999938835958047 | 0      |
| 17 | Tensor<[1, 1, 1, 6]> self = ?,<br>number other = 1.0       | Unknown  | Done       | 0.9999982588467092 | 0      |
| 18 | Tensor<[1, 1, 1, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999866276789197 | 0      |
| 19 | Tensor<[1, 1, 1, 8]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999950281914315 | 0      |
| 20 | Tensor<[1, 1, 1, 9]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999973181369282 | 0      |
| 21 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>number other = 1.0  | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>number other = 1.0 | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 1, 19, 19]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999921241563016 | 0      |
| 24 | Tensor<[1, 1, 24, 24]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999931411749846 | 0      |
| 25 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 1.0      | Done     | Done       | 0.9999925151449992 | 0      |
| 26 | Tensor<[1, 1, 32, 1]> self = ?,<br>number other = 2.0      | Done     | Done       | 0.9999901532359339 | 0      |
| 27 | Tensor<[1, 1, 32, 32]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.999993258788928  | 0      |
| 28 | Tensor<[1, 1, 45, 45]> self = ?,<br>number other = 1.0     | Unknown  | Done       | 0.9999940542656776 | 0      |
| 29 | Tensor<[1, 1, 59, 59]> self = ?,<br>number other = 1.0     | Done     | Done       | 0.9999938092306682 | 0      |
| 30 | Tensor<[1066]> self = ?,<br>number other = 1.0             | Unknown  | Done       | 0.9999933769363931 | 0      |
| 31 | Tensor<[120, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999959147026893 | 0      |
| 32 | Tensor<[128, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999919915851336 | 0      |
| 33 | Tensor<[128]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999948044572541 | 0      |
| 34 | Tensor<[160]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999943430887991 | 0      |
| 35 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0       | Done     | Done       | 0.9999905502398142 | 0      |
| 36 | Tensor<[240, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999934417354996 | 0      |
| 37 | Tensor<[30, 1]> self = ?,<br>number other = 1.0            | Removed  | Done       | 0.9999944650670421 | 0      |
| 38 | Tensor<[300, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999947082272237 | 0      |
| 39 | Tensor<[300]> self = ?,<br>number other = 1.0              | Unknown  | Done       | 0.9999931916189779 | 0      |
| 40 | Tensor<[320, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999936847371257 | 0      |
| 41 | Tensor<[320]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999943159011164 | 0      |
| 42 | Tensor<[40]> self = ?,<br>number other = 1.0               | Removed  | Done       | 0.9999936877008094 | 0      |
| 43 | Tensor<[480, 1]> self = ?,<br>number other = 1.0           | Removed  | Done       | 0.9999928123599747 | 0      |
| 44 | Tensor<[60, 1]> self = ?,<br>number other = 1.0            | Removed  | Done       | 0.9999960657347324 | 0      |
| 45 | Tensor<[640]> self = ?,<br>number other = 1.0              | Removed  | Done       | 0.9999940898046077 | 0      |
| 46 | Tensor<[800, 1]> self = ?,<br>number other = 1.0           | Unknown  | Done       | 0.9999932138075062 | 0      |
| 47 | Tensor<[80]> self = ?,<br>number other = 1.0               | Removed  | Done       | 0.9999909623438852 | 0      |

