### aten.sub.Tensor
|    | ATen Input Variations                                                        | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 24]> other = ?                          | Unknown  | Unknown    | N/A                | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 10, 10]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor self = ?,<br>Tensor<[1, 1, 12, 12]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor self = ?,<br>Tensor<[1, 1, 14, 14]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor self = ?,<br>Tensor<[1, 1, 16, 16]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?                         | Unknown  | Unknown    | N/A                | N/A    |
|  6 | Tensor self = ?,<br>Tensor<[1, 1, 25, 25]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor self = ?,<br>Tensor<[1, 1, 9, 9]> other = ?                           | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor self = ?,<br>Tensor<[16, 1]> other = ?                                | Done     | Unknown    | N/A                | N/A    |
|  9 | Tensor self = ?,<br>Tensor<[16]> other = ?                                   | Done     | Unknown    | N/A                | N/A    |
| 10 | Tensor self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?                           | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor self = ?,<br>Tensor<[32, 1]> other = ?                                | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor self = ?,<br>Tensor<[42]> other = ?                                   | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor self = ?,<br>Tensor<[8, 1, 384, 384]> other = ?                       | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Removed  | Done       | 0.9999982366617438 | 0      |
| 15 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                       | Unknown  | Done       | 0.9999966520098253 | 0      |
| 16 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?         | Removed  | Done       | 0.9999971310863757 | 0      |
| 17 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                       | Unknown  | Done       | 0.9999984247810844 | 0      |
| 18 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                         | Unknown  | Done       | 1.0                | 0      |
| 19 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Removed  | Done       | 0.9999977593710938 | 0      |
| 20 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Removed  | Done       | 0.9999981700902756 | 0      |
| 21 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ? | Done     | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 2]> self = ?,<br>Tensor<[1, 1]> other = ?                         | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?     | Done     | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?     | Done     | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                                | Done     | Done       | 0.9999964263480551 | 0      |
| 26 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                                | Unknown  | Done       | 0.9999973794518741 | 0      |
| 27 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Removed  | Done       | 0.99999822271729   | 0      |
| 28 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                                | Unknown  | Done       | 0.9999977546825711 | 0      |
| 29 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                                 | Unknown  | Done       | 1.0                | 0      |
| 30 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?           | Removed  | Done       | 0.9999989053903585 | 0      |
| 31 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?   | Done     | Unknown    | N/A                | N/A    |
| 32 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?   | Done     | Unknown    | N/A                | N/A    |
| 33 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?       | Done     | Unknown    | N/A                | N/A    |
| 34 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?   | Done     | Unknown    | N/A                | N/A    |
| 35 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?       | Done     | Unknown    | N/A                | N/A    |
| 36 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, 1]> other = ?                    | Unknown  | Unknown    | N/A                | N/A    |
| 37 | Tensor<[1, s1]> self = ?,<br>Tensor other = 1                                | Unknown  | Unknown    | N/A                | N/A    |
| 38 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?               | Done     | Done       | 0.9999980122083042 | 0      |
| 39 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?               | Done     | Done       | 0.9999980140894393 | 0      |
| 40 | Tensor<[16, 1]> self = ?,<br>Tensor other = 1                                | Done     | Unknown    | N/A                | N/A    |
| 41 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 1]> other = ?                 | Done     | Unknown    | N/A                | N/A    |
| 42 | Tensor<[16384, 2]> self = ?,<br>Tensor<[16384, 1]> other = ?                 | Done     | Unknown    | N/A                | N/A    |
| 43 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 3]> other = ?                 | Done     | Unknown    | N/A                | N/A    |
| 44 | Tensor<[16384, 3]> self = ?,<br>Tensor<[3]> other = ?                        | Done     | Unknown    | N/A                | N/A    |
| 45 | Tensor<[16384]> self = ?,<br>Tensor other = 1.0                              | Done     | Unknown    | N/A                | N/A    |
| 46 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?                       | Done     | Unknown    | N/A                | N/A    |
| 47 | Tensor<[16]> self = ?,<br>Tensor other = 1                                   | Done     | Unknown    | N/A                | N/A    |
| 48 | Tensor<[2, 16, 1]> self = ?,<br>Tensor other = -3.0                          | Done     | Unknown    | N/A                | N/A    |
| 49 | Tensor<[2, 16, 1]> self = ?,<br>Tensor other = -3.75                         | Done     | Unknown    | N/A                | N/A    |
| 50 | Tensor<[2, 16, 1]> self = ?,<br>Tensor other = 2.25                          | Done     | Unknown    | N/A                | N/A    |
| 51 | Tensor<[2, 16]> self = ?,<br>Tensor other = -3.0                             | Done     | Unknown    | N/A                | N/A    |
| 52 | Tensor<[2, 16]> self = ?,<br>Tensor other = -3.75                            | Done     | Unknown    | N/A                | N/A    |
| 53 | Tensor<[2, 16]> self = ?,<br>Tensor other = 2.25                             | Done     | Unknown    | N/A                | N/A    |
| 54 | Tensor<[2, 32, 1]> self = ?,<br>Tensor other = -3.0                          | Done     | Unknown    | N/A                | N/A    |
| 55 | Tensor<[2, 32, 1]> self = ?,<br>Tensor other = -3.75                         | Done     | Unknown    | N/A                | N/A    |
| 56 | Tensor<[2, 32, 1]> self = ?,<br>Tensor other = 2.25                          | Done     | Unknown    | N/A                | N/A    |
| 57 | Tensor<[2, 42]> self = ?,<br>Tensor other = -3.0                             | Done     | Unknown    | N/A                | N/A    |
| 58 | Tensor<[2, 42]> self = ?,<br>Tensor other = -3.75                            | Done     | Unknown    | N/A                | N/A    |
| 59 | Tensor<[2, 42]> self = ?,<br>Tensor other = 2.25                             | Done     | Unknown    | N/A                | N/A    |
| 60 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                       | Unknown  | Done       | 0.9999973575328647 | 0      |
| 61 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | 0.999997008938845  | 0      |
| 62 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | 0.9999983554598103 | 0      |
| 63 | Tensor<[32, 1]> self = ?,<br>Tensor other = 1                                | Done     | Unknown    | N/A                | N/A    |
| 64 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 65 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                   | Done     | Done       | 0.9999979136425077 | 0      |
| 66 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
| 67 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?                 | Done     | Done       | 0.9999980520417636 | 0      |
| 68 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?                 | Done     | Done       | 0.9999979768053364 | 0      |
| 69 | Tensor<[42]> self = ?,<br>Tensor other = 1                                   | Done     | Unknown    | N/A                | N/A    |
| 70 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?               | Done     | Done       | 0.9999979996624193 | 0      |
| 71 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?               | Done     | Done       | 0.9999979667311854 | 0      |
| 72 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 73 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                   | Done     | Done       | 0.9999979935795728 | 0      |
| 74 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
| 75 | Tensor<[98, 80]> self = ?,<br>Tensor<[80]> other = ?                         | Unknown  | Unknown    | N/A                | N/A    |

