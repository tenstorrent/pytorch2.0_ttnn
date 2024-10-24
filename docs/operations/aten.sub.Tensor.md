### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-----------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                  | Done     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[1066]> self = ?,<br>Tensor<[1066]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 38 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 39 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 40 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | None     | N/A                 | N/A          | N/A               | N/A                |
| 41 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | None     | N/A                 | N/A          | N/A               | N/A                |
| 42 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 43 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 44 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | None     | N/A                 | N/A          | N/A               | N/A                |
| 45 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 46 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 47 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 48 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 49 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 50 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 51 | Tensor<[300, 1]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 52 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 53 | Tensor<[300]> self = ?,<br>Tensor<[300]> other = ?                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 54 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 55 | Tensor<[320, 1]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 56 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 57 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 58 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 59 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 60 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 61 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | None     | N/A                 | N/A          | N/A               | N/A                |
| 62 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | None     | N/A                 | N/A          | N/A               | N/A                |
| 63 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 64 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?                       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 65 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 66 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 67 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 68 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 69 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | None     | N/A                 | N/A          | N/A               | N/A                |
| 70 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | None     | N/A                 | N/A          | N/A               | N/A                |
| 71 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 72 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 73 | Tensor<[800, 1]> self = ?,<br>Tensor<[800, 1]> other = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 74 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 75 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 76 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?                       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 77 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 78 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 79 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 80 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |

