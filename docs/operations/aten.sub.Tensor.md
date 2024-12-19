### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                 | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  2 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
|  3 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  | Done       | 1.0                 | 0      |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999966090989604  | 0      |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999657057237789  | 0      |
|  6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                  | Removed  | Done       | 0.9999983866097149  | 0      |
|  7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999939350128331  | 0      |
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999861512588236  | 0      |
|  9 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?     | Removed  | Done       | 0.9999991825668579  | 0      |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999899040777738  | 0      |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999788521235101  | 0      |
| 12 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                  | Removed  | Done       | 0.9999974958297263  | 0      |
| 13 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999878287732417  | 0      |
| 14 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999932847420793  | 0      |
| 15 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?     | Removed  | Done       | 0.9999985061617579  | 0      |
| 16 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.9999978288828894  | 0      |
| 17 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.6732410812905498  | 0      |
| 18 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | 0.999998642021095   | 0      |
| 19 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.7153030870972669  | 0      |
| 20 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.6630356369164949  | 0      |
| 21 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
| 22 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.9999977072255478  | 0      |
| 23 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.9999988007089111  | 0      |
| 24 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.9623839133391264  | 0      |
| 25 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999866130309217  | 0      |
| 26 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.999994823401314   | 0      |
| 27 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999982017375676  | 0      |
| 28 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999987930649268  | 0      |
| 29 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 1.0                 | 0      |
| 30 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999909557425175  | 0      |
| 31 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | 0.9999957104597252  | 0      |
| 32 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 33 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 34 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 35 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                         | Unknown  | Done       | 0.999997832380056   | 0      |
| 36 | Tensor<[1066]> self = ?,<br>Tensor<[1066]> other = ?                   | Unknown  | Done       | 0.9999976597897743  | 0      |
| 37 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ?               | Removed  | Done       | 0.999998164188811   | 0      |
| 38 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999993416959978  | 0      |
| 39 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?               | Removed  | Done       | 0.9999980878489719  | 0      |
| 40 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999976648549224  | 0      |
| 41 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?                     | Removed  | Done       | 0.9999985472016734  | 0      |
| 42 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.48333296783256385 | 0      |
| 43 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.47350035415718245 | 0      |
| 44 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999961581016761  | 0      |
| 45 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?                     | Removed  | Done       | 0.9999976020427148  | 0      |
| 46 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                 | 0      |
| 47 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Done     | Done       | 0.8025847029292984  | 0      |
| 48 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ?               | Removed  | Done       | 0.9999981985777668  | 0      |
| 49 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999965700079736  | 0      |
| 50 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Unknown  | Done       | 0.9999977376464281  | 0      |
| 51 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Unknown  | Done       | 0.9999983625891551  | 0      |
| 52 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Removed  | Done       | 0.9999995002080319  | 0      |
| 53 | Tensor<[300, 1]> self = ?,<br>Tensor<[300, 1]> other = ?               | Unknown  | Done       | 0.9999983809733848  | 0      |
| 54 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 0.999998101426048   | 0      |
| 55 | Tensor<[300]> self = ?,<br>Tensor<[300]> other = ?                     | Unknown  | Done       | 0.9999982806535156  | 0      |
| 56 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                           | Removed  | Done       | 0.9999991982699891  | 0      |
| 57 | Tensor<[320, 1]> self = ?,<br>Tensor<[320, 1]> other = ?               | Unknown  | Done       | 0.9999977866439017  | 0      |
| 58 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999971253359187  | 0      |
| 59 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?                     | Removed  | Done       | 0.9999977408580656  | 0      |
| 60 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  | Done       | 0.9999981267674637  | 0      |
| 61 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Unknown  | Done       | 0.9999979263401408  | 0      |
| 62 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Unknown  | Done       | 0.9999980752123071  | 0      |
| 63 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.5138770398356506  | 0      |
| 64 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.5339348895331718  | 0      |
| 65 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                           | Removed  | Done       | 0.9999931826443212  | 0      |
| 66 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?                       | Removed  | Done       | 0.999999306076289   | 0      |
| 67 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ?               | Removed  | Done       | 0.9999985458003832  | 0      |
| 68 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999977519234867  | 0      |
| 69 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Removed  | Done       | 0.999997192231865   | 0      |
| 70 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                           | Removed  | Done       | 0.9999930620127138  | 0      |
| 71 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.3534300369785802  | 0      |
| 72 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.34256622400106396 | 0      |
| 73 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999971381359329  | 0      |
| 74 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?                     | Removed  | Done       | 0.9999982554940203  | 0      |
| 75 | Tensor<[800, 1]> self = ?,<br>Tensor<[800, 1]> other = ?               | Unknown  | Done       | 0.9999978741303106  | 0      |
| 76 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 0.9999977092505397  | 0      |
| 77 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                           | Removed  | Done       | 0.9999974706508583  | 0      |
| 78 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?                       | Removed  | Done       | 0.9999972586973583  | 0      |
| 79 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | Done       | 0.9999980243260567  | 0      |
| 80 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Unknown  | Done       | 0.9999979955301084  | 0      |
| 81 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | Done       | 0.9999979870776219  | 0      |

