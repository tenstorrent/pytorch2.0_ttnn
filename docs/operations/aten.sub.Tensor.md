### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   |
|---:|:-----------------------------------------------------------------------|:---------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = -3.0               | Done     |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = -3.75              | Done     |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 0.5                | Done     |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 1                  | Done     |
|  6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 2.25               | Done     |
|  7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?     | Done     |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = -3.0               | Done     |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = -3.75              | Done     |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 0.5                | Done     |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 1                  | Done     |
| 12 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 2.25               | Done     |
| 13 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?     | Done     |
| 14 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Unknown  |
| 15 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Done     |
| 16 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Unknown  |
| 17 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Done     |
| 18 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  |
| 20 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Unknown  |
| 21 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Unknown  |
| 22 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  |
| 23 | Tensor<[1, 32]> self = ?,<br>Tensor<> other = 1                        | Done     |
| 24 | Tensor<[1, 45]> self = ?,<br>Tensor<> other = 1                        | Unknown  |
| 25 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  |
| 26 | Tensor<[1, 59]> self = ?,<br>Tensor<> other = 1                        | Done     |
| 27 | Tensor<[1, 5]> self = ?,<br>Tensor<> other = 1                         | Done     |
| 28 | Tensor<[1, 60]> self = ?,<br>Tensor<> other = 1                        | Unknown  |
| 29 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Unknown  |
| 30 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  |
| 31 | Tensor<[1, s0]> self = ?,<br>Tensor<> other = 1                        | Unknown  |
| 32 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<> other = 1                   | Unknown  |
| 33 | Tensor<[1066]> self = ?,<br>Tensor<> other = 0.5                       | Unknown  |
| 34 | Tensor<[1066]> self = ?,<br>Tensor<[1066]> other = ?                   | Unknown  |
| 35 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ?               | Done     |
| 36 | Tensor<[120]> self = ?,<br>Tensor<> other = 0.5                        | Done     |
| 37 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?               | Done     |
| 38 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.5                        | Done     |
| 39 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?                     | Done     |
| 40 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     |
| 41 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     |
| 42 | Tensor<[160]> self = ?,<br>Tensor<> other = 0.5                        | Done     |
| 43 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?                     | Done     |
| 44 | Tensor<[1]> self = ?,<br>Tensor<> other = 1                            | Unknown  |
| 45 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Done     |
| 46 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ?               | Done     |
| 47 | Tensor<[240]> self = ?,<br>Tensor<> other = 0.5                        | Done     |
| 48 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     |
| 49 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     |
| 50 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     |
| 51 | Tensor<[300, 1]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     |
| 52 | Tensor<[300]> self = ?,<br>Tensor<> other = 0.5                        | Done     |
| 53 | Tensor<[300]> self = ?,<br>Tensor<[300]> other = ?                     | Done     |
| 54 | Tensor<[30]> self = ?,<br>Tensor<> other = 0.5                         | Done     |
| 55 | Tensor<[320, 1]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     |
| 56 | Tensor<[320]> self = ?,<br>Tensor<> other = 0.5                        | Done     |
| 57 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?                     | Done     |
| 58 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  |
| 59 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     |
| 60 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Unknown  |
| 61 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     |
| 62 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     |
| 63 | Tensor<[40]> self = ?,<br>Tensor<> other = 0.5                         | Done     |
| 64 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?                       | Done     |
| 65 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ?               | Done     |
| 66 | Tensor<[480]> self = ?,<br>Tensor<> other = 0.5                        | Done     |
| 67 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     |
| 68 | Tensor<[60]> self = ?,<br>Tensor<> other = 0.5                         | Done     |
| 69 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     |
| 70 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     |
| 71 | Tensor<[640]> self = ?,<br>Tensor<> other = 0.5                        | Done     |
| 72 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?                     | Done     |
| 73 | Tensor<[800, 1]> self = ?,<br>Tensor<[800, 1]> other = ?               | Unknown  |
| 74 | Tensor<[800]> self = ?,<br>Tensor<> other = 0.5                        | Unknown  |
| 75 | Tensor<[80]> self = ?,<br>Tensor<> other = 0.5                         | Done     |
| 76 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?                       | Done     |
| 77 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  |
| 78 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     |
| 79 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  |
| 80 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?                   | Unknown  |

