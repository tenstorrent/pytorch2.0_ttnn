### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  | Fallback   | True  |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | True  |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | True  |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                  | Done     | Done       | True  |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | True  |
|  6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | True  |
|  7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?     | Fallback | Done       | True  |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | True  |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | True  |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                  | Done     | Done       | True  |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | True  |
| 12 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | True  |
| 13 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?     | Fallback | Done       | True  |
| 14 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | True  |
| 15 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | None     | Fallback   | True  |
| 16 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | True  |
| 17 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | None     | Fallback   | True  |
| 18 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Fallback   | True  |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Fallback | Done       | True  |
| 20 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | True  |
| 21 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | True  |
| 22 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Fallback   | True  |
| 23 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | True  |
| 24 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | True  |
| 25 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | True  |
| 26 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Done     | Done       | True  |
| 27 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Fallback | Done       | True  |
| 28 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | True  |
| 29 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | True  |
| 30 | Tensor<[1, 6]> self = ?,<br>Tensor other = 1                           | Fallback | Unknown    | N/A   |
| 31 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A   |
| 32 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A   |
| 33 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A   |
| 34 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                         | Fallback | Done       | True  |
| 35 | Tensor<[1066]> self = ?,<br>Tensor<[1066]> other = ?                   | Fallback | Done       | True  |
| 36 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ?               | Fallback | Done       | True  |
| 37 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 38 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?               | Fallback | Done       | True  |
| 39 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 40 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?                     | Fallback | Done       | True  |
| 41 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | None     | Fallback   | True  |
| 42 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | None     | Fallback   | True  |
| 43 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 44 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?                     | Fallback | Done       | True  |
| 45 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Unknown  | Done       | True  |
| 46 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | None     | Fallback   | True  |
| 47 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ?               | Fallback | Done       | True  |
| 48 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 49 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | True  |
| 50 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | True  |
| 51 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Fallback | Done       | True  |
| 52 | Tensor<[300, 1]> self = ?,<br>Tensor<[300, 1]> other = ?               | Fallback | Done       | True  |
| 53 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 54 | Tensor<[300]> self = ?,<br>Tensor<[300]> other = ?                     | Fallback | Done       | True  |
| 55 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                           | Fallback | Done       | True  |
| 56 | Tensor<[320, 1]> self = ?,<br>Tensor<[320, 1]> other = ?               | Fallback | Done       | True  |
| 57 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 58 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?                     | Fallback | Done       | True  |
| 59 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  | Done       | True  |
| 60 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | True  |
| 61 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Unknown  | Done       | True  |
| 62 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | None     | Fallback   | True  |
| 63 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | None     | Fallback   | True  |
| 64 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                           | Fallback | Done       | True  |
| 65 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?                       | Fallback | Done       | True  |
| 66 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ?               | Fallback | Done       | True  |
| 67 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 68 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Fallback | Done       | True  |
| 69 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                           | Fallback | Done       | True  |
| 70 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | None     | Fallback   | True  |
| 71 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | None     | Fallback   | True  |
| 72 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 73 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?                     | Fallback | Done       | True  |
| 74 | Tensor<[800, 1]> self = ?,<br>Tensor<[800, 1]> other = ?               | Fallback | Done       | True  |
| 75 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                          | Fallback | Done       | True  |
| 76 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                           | Fallback | Done       | True  |
| 77 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?                       | Fallback | Done       | True  |
| 78 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | Done       | True  |
| 79 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | True  |
| 80 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | Done       | True  |

