### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 1                                     | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor self = ?,<br>Tensor other = 1.0                                   | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor self = ?,<br>Tensor other = 10                                    | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor self = ?,<br>Tensor other = 128                                   | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor self = ?,<br>Tensor other = 160                                   | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor self = ?,<br>Tensor other = 18.75                                 | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor self = ?,<br>Tensor other = 2                                     | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor self = ?,<br>Tensor other = 20                                    | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor self = ?,<br>Tensor other = 3                                     | Done     | Unknown    | N/A                | N/A    |
|  9 | Tensor self = ?,<br>Tensor other = 3.0                                   | Done     | Unknown    | N/A                | N/A    |
| 10 | Tensor self = ?,<br>Tensor other = 37.5                                  | Done     | Unknown    | N/A                | N/A    |
| 11 | Tensor self = ?,<br>Tensor other = 4.6875                                | Done     | Unknown    | N/A                | N/A    |
| 12 | Tensor self = ?,<br>Tensor other = 5                                     | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor self = ?,<br>Tensor other = 9.375                                 | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor self = ?,<br>Tensor other = ?                                     | Done     | Unknown    | N/A                | N/A    |
| 15 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.9999958407877474 | 0      |
| 16 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                | 0      |
| 17 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 0.5                      | Unknown  | Unknown    | N/A                | N/A    |
| 18 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | 0.9999967168369842 | 0      |
| 19 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | 0.9999960181816491 | 0      |
| 20 | Tensor<[1, 1024, 640]> self = ?,<br>Tensor other = 1.0                   | Done     | Unknown    | N/A                | N/A    |
| 21 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor other = 8.0                | Unknown  | Unknown    | N/A                | N/A    |
| 22 | Tensor<[1, 128, 1568]> self = ?,<br>Tensor other = 3                     | Unknown  | Unknown    | N/A                | N/A    |
| 23 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor other = 1.0                | Done     | Unknown    | N/A                | N/A    |
| 24 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1                    | Done     | Unknown    | N/A                | N/A    |
| 25 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0                  | Done     | Done       | 1.0                | 0      |
| 26 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Done       | 0.9999969044842453 | 0      |
| 27 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[]> other = ?             | Unknown  | Unknown    | N/A                | N/A    |
| 28 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Done       | 0.9999957750458977 | 0      |
| 29 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | 0.9999974128894041 | 0      |
| 30 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                | 0      |
| 31 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                | 0      |
| 32 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958450367564 | 0      |
| 33 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
| 34 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?              | Done     | Done       | 0.9999959146685323 | 0      |
| 35 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Done     | Unknown    | N/A                | N/A    |
| 36 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 23, 1]> other = ?            | Done     | Unknown    | N/A                | N/A    |
| 37 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ?   | Done     | Done       | 0.9999976571332932 | 0      |
| 38 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor other = 1.0                   | Done     | Unknown    | N/A                | N/A    |
| 39 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999964091419387 | 0      |
| 40 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | 0.99999617541865   | 0      |
| 41 | Tensor<[1, 256, 392]> self = ?,<br>Tensor other = 3                      | Unknown  | Unknown    | N/A                | N/A    |
| 42 | Tensor<[1, 2]> self = ?,<br>Tensor other = 16                            | Unknown  | Unknown    | N/A                | N/A    |
| 43 | Tensor<[1, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Unknown    | N/A                | N/A    |
| 44 | Tensor<[1, 32, 25088]> self = ?,<br>Tensor other = 3                     | Unknown  | Unknown    | N/A                | N/A    |
| 45 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ?   | Done     | Done       | 0.9999999765246951 | 0      |
| 46 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0                 | Done     | Done       | 1.0                | 0      |
| 47 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0                   | Done     | Done       | 1.0                | 0      |
| 48 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | 0.9999971091711196 | 0      |
| 49 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | 0.9999964817518232 | 0      |
| 50 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958541896178 | 0      |
| 51 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
| 52 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  | Done       | 0.9999964801608644 | 0      |
| 53 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Done     | Done       | 0.9999996051260565 | 0      |
| 54 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | 0.9999962332753044 | 0      |
| 55 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                 | Unknown  | Unknown    | N/A                | N/A    |
| 56 | Tensor<[1, 64, 1280]> self = ?,<br>Tensor other = 1.0                    | Done     | Unknown    | N/A                | N/A    |
| 57 | Tensor<[1, 64, 6272]> self = ?,<br>Tensor other = 3                      | Unknown  | Unknown    | N/A                | N/A    |
| 58 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor other = 1.0                 | Done     | Unknown    | N/A                | N/A    |
| 59 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958621871017 | 0      |
| 60 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958463992162 | 0      |
| 61 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.9999958354067728 | 0      |
| 62 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0                 | Done     | Done       | 1.0                | 0      |
| 63 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |
| 64 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357       | Unknown  | Unknown    | N/A                | N/A    |
| 65 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 0.5                     | Unknown  | Unknown    | N/A                | N/A    |
| 66 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999953081823022 | 0      |
| 67 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                | 0      |
| 68 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999962939050889 | 0      |
| 69 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                | 0      |
| 70 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ?   | Done     | Done       | 0.9999870396515762 | 0      |
| 71 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ?   | Done     | Done       | 0.9999998297535433 | 0      |
| 72 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 73 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 4]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 74 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 75 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Done     | Done       | 0.9999948233227691 | 0      |
| 76 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999955878832296 | 0      |
| 77 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.999995781187326  | 0      |
| 78 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0                       | Done     | Unknown    | N/A                | N/A    |
| 79 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 5.0                        | Done     | Unknown    | N/A                | N/A    |
| 80 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ?   | Done     | Done       | 0.9999977948141014 | 0      |
| 81 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ?   | Done     | Done       | 0.9999939769596113 | 0      |
| 82 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Done     | Done       | 0.9999934968080412 | 0      |
| 83 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Done     | Done       | 0.9999990935506894 | 0      |
| 84 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 10.0                       | Done     | Unknown    | N/A                | N/A    |
| 85 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 5.0                        | Done     | Unknown    | N/A                | N/A    |
| 86 | Tensor<[98, 80]> self = ?,<br>Tensor<[80]> other = ?                     | Unknown  | Unknown    | N/A                | N/A    |
| 87 | Tensor<[]> self = ?,<br>Tensor other = 0.02                              | Unknown  | Unknown    | N/A                | N/A    |

