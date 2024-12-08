### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  | Fallback   | 1.0                | -1     |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  | Fallback   | 1.0                | -1     |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.999984681205765  | 0      |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999669794472139 | 0      |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                  | Done     | Done       | 0.999994993048604  | 0      |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999893388417034 | 0      |
|  6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.999989000365047  | 0      |
|  7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?     | Done     | Done       | 0.9999976009539231 | 0      |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999749065366818 | 0      |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999914623127033 | 0      |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                  | Done     | Done       | 1.0                | 0      |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999944158636109 | 0      |
| 12 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999933039836427 | 0      |
| 13 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?     | Done     | Done       | 0.9999988665804442 | 0      |
| 14 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.9999975835849052 | 0      |
| 15 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | None     | Fallback   | 1.0                | -1     |
| 16 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | 0.9999976555659811 | 0      |
| 17 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | None     | Fallback   | 1.0                | -1     |
| 18 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Fallback   | 1.0                | -1     |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | 1.0                | 0      |
| 20 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.9999979840938051 | 0      |
| 21 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.9999978054862736 | 0      |
| 22 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Fallback   | 1.0                | -1     |
| 23 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999879571995804 | 0      |
| 24 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999930105552601 | 0      |
| 25 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999977200110215 | 0      |
| 26 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999933969754105 | 0      |
| 27 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999967135094336 | 0      |
| 28 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999956780552673 | 0      |
| 29 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | 0.9999976643814114 | 0      |
| 30 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 31 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                | N/A    |
| 32 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                | N/A    |
| 33 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                         | Done     | Done       | 0.9999970571108581 | 0      |
| 34 | Tensor<[1066]> self = ?,<br>Tensor<[1066]> other = ?                   | Done     | Done       | 0.9999977919470493 | 0      |
| 35 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ?               | Done     | Done       | 0.99999841356456   | 0      |
| 36 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 0.9999990395549611 | 0      |
| 37 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?               | Done     | Done       | 0.9999973327592385 | 0      |
| 38 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 0.9999981488765095 | 0      |
| 39 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?                     | Done     | Done       | 0.9999983464247665 | 0      |
| 40 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | None     | Fallback   | 1.0                | -1     |
| 41 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | None     | Fallback   | 1.0                | -1     |
| 42 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 0.9999975062948386 | 0      |
| 43 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?                     | Done     | Done       | 0.9999984009406886 | 0      |
| 44 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | None     | Done       | 1.0                | 0      |
| 45 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | None     | Fallback   | 1.0                | -1     |
| 46 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ?               | Done     | Done       | 0.9999975610416422 | 0      |
| 47 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 0.9999978411742311 | 0      |
| 48 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999981648581614 | 0      |
| 49 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999978368319008 | 0      |
| 50 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | 0.9999991042704423 | 0      |
| 51 | Tensor<[300, 1]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     | Done       | 0.9999985629071857 | 0      |
| 52 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                          | None     | Fallback   | 1.0                | -1     |
| 53 | Tensor<[300]> self = ?,<br>Tensor<[300]> other = ?                     | Done     | Done       | 0.9999985008019198 | 0      |
| 54 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 0.9999972929398201 | 0      |
| 55 | Tensor<[320, 1]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | Done       | 0.9999979367661022 | 0      |
| 56 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                          | None     | Fallback   | 1.0                | -1     |
| 57 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?                     | Done     | Done       | 0.9999974558809256 | 0      |
| 58 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  | Done       | 0.9999981658914638 | 0      |
| 59 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999980043216012 | 0      |
| 60 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Unknown  | Done       | 0.9999978821642491 | 0      |
| 61 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | None     | Fallback   | 1.0                | -1     |
| 62 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | None     | Fallback   | 1.0                | -1     |
| 63 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 0.999997270679657  | 0      |
| 64 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?                       | Done     | Done       | 0.9999982912011696 | 0      |
| 65 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ?               | Done     | Done       | 0.9999981021283663 | 0      |
| 66 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 0.9999974949433066 | 0      |
| 67 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | 0.999999246375469  | 0      |
| 68 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 0.9999973525336564 | 0      |
| 69 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | None     | Fallback   | 1.0                | -1     |
| 70 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | None     | Fallback   | 1.0                | -1     |
| 71 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 0.999997097986159  | 0      |
| 72 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?                     | Done     | Done       | 0.9999981508959702 | 0      |
| 73 | Tensor<[800, 1]> self = ?,<br>Tensor<[800, 1]> other = ?               | Done     | Done       | 0.9999985181410261 | 0      |
| 74 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                          | None     | Fallback   | 1.0                | -1     |
| 75 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 0.9999980156268711 | 0      |
| 76 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?                       | Done     | Done       | 0.9999985805390604 | 0      |
| 77 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | Done       | 0.9999979465664429 | 0      |
| 78 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | 0.9999978948560514 | 0      |
| 79 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | Done       | 0.9999979694851535 | 0      |

