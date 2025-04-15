### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                   | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:----------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 1                                     | Done     | Unknown    | N/A                   | N/A    |
|  1 | Tensor self = ?,<br>Tensor other = 1.0                                   | Done     | Unknown    | N/A                   | N/A    |
|  2 | Tensor self = ?,<br>Tensor other = 10                                    | Done     | Unknown    | N/A                   | N/A    |
|  3 | Tensor self = ?,<br>Tensor other = 128                                   | Done     | Unknown    | N/A                   | N/A    |
|  4 | Tensor self = ?,<br>Tensor other = 160                                   | Done     | Unknown    | N/A                   | N/A    |
|  5 | Tensor self = ?,<br>Tensor other = 18.75                                 | Done     | Unknown    | N/A                   | N/A    |
|  6 | Tensor self = ?,<br>Tensor other = 2                                     | Done     | Unknown    | N/A                   | N/A    |
|  7 | Tensor self = ?,<br>Tensor other = 20                                    | Done     | Unknown    | N/A                   | N/A    |
|  8 | Tensor self = ?,<br>Tensor other = 3                                     | Done     | Unknown    | N/A                   | N/A    |
|  9 | Tensor self = ?,<br>Tensor other = 3.0                                   | Done     | Unknown    | N/A                   | N/A    |
| 10 | Tensor self = ?,<br>Tensor other = 37.5                                  | Done     | Unknown    | N/A                   | N/A    |
| 11 | Tensor self = ?,<br>Tensor other = 4.6875                                | Done     | Unknown    | N/A                   | N/A    |
| 12 | Tensor self = ?,<br>Tensor other = 5                                     | Done     | Unknown    | N/A                   | N/A    |
| 13 | Tensor self = ?,<br>Tensor other = 9.375                                 | Done     | Unknown    | N/A                   | N/A    |
| 14 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.9999958475323415    | 0      |
| 15 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                   | 0      |
| 16 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | 0.9999958832829623    | 0      |
| 17 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | 0.9999962011293462    | 0      |
| 18 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                   | 0      |
| 19 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                   | 0      |
| 20 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                   | 0      |
| 21 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                   | 0      |
| 22 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                   | 0      |
| 23 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                   | 0      |
| 24 | Tensor<[1, 12, 257, 257]> self = ?,<br>Tensor other = 8.0                | Done     | Unknown    | N/A                   | N/A    |
| 25 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | None     | Fallback   | 1.0                   | -1     |
| 26 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                   | 0      |
| 27 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | 1.0                   | -1     |
| 28 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ?            | Unknown  | Unknown    | N/A                   | N/A    |
| 29 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                   | 0      |
| 30 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | 1.0                   | -1     |
| 31 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | Done     | Done       | 0.9999953345312311    | 0      |
| 32 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                   | 0      |
| 33 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | 0.999997944007336     | 0      |
| 34 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                   | 0      |
| 35 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                   | 0      |
| 36 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.99999584383629      | 0      |
| 37 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                   | 0      |
| 38 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?              | Done     | Done       | 0.0029161409869397615 | 0      |
| 39 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Done     | Unknown    | N/A                   | N/A    |
| 40 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 23, 1]> other = ?            | Done     | Unknown    | N/A                   | N/A    |
| 41 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ?   | Done     | Done       | 0.9999986267469269    | 0      |
| 42 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999964444964229    | 0      |
| 43 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | 0.9999962100242842    | 0      |
| 44 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                   | 0      |
| 45 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ?   | Done     | Done       | 0.9999957908043308    | 0      |
| 46 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | 0.9999967125802218    | 0      |
| 47 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | 0.9999972134281383    | 0      |
| 48 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958339733064    | 0      |
| 49 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                   | 0      |
| 50 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  | Done       | 0.9999964900212327    | 0      |
| 51 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Done     | Done       | 0.9999991614805825    | 0      |
| 52 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | 0.9999977406816252    | 0      |
| 53 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                   | 0      |
| 54 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.99999584586178      | 0      |
| 55 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958305587373    | 0      |
| 56 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.9999958425925906    | 0      |
| 57 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0                 | Done     | Done       | 1.0                   | 0      |
| 58 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.999996112685193     | 0      |
| 59 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                   | 0      |
| 60 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999955661493823    | 0      |
| 61 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                   | 0      |
| 62 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ?   | Done     | Done       | 0.9999963963780947    | 0      |
| 63 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ?   | Done     | Done       | 0.9999941815573432    | 0      |
| 64 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                          | Unknown  | Done       | 1.0                   | 0      |
| 65 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357          | Unknown  | Done       | 0.9999989418845512    | 0      |
| 66 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                   | 0      |
| 67 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                   | 0      |
| 68 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Done     | Done       | 0.9999959584790812    | 0      |
| 69 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999950889738718    | 0      |
| 70 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999961824740315    | 0      |
| 71 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ?   | Done     | Done       | 0.9999989612725857    | 0      |
| 72 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ?   | Done     | Done       | 0.9999976245838348    | 0      |
| 73 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Done     | Done       | 0.9999980990759296    | 0      |
| 74 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Done     | Done       | 0.9999995525812336    | 0      |
| 75 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999959302866215    | 0      |
| 76 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999958484628652    | 0      |
| 77 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                  | Unknown  | Unknown    | N/A                   | N/A    |
| 78 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357  | Unknown  | Unknown    | N/A                   | N/A    |

