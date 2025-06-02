### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                 | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  2 | Tensor self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  3 | Tensor self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  4 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -3.0                 | Done     | Unknown    | N/A                 | N/A    |
|  5 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -3.75                | Done     | Unknown    | N/A                 | N/A    |
|  6 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1                    | Done     | Unknown    | N/A                 | N/A    |
|  7 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 2.25                 | Done     | Unknown    | N/A                 | N/A    |
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999961707086462  | 0      |
|  9 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999655834833167  | 0      |
| 10 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.999994344715934   | 0      |
| 11 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999690989661231  | 0      |
| 12 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Unknown    | N/A                 | N/A    |
| 13 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Unknown    | N/A                 | N/A    |
| 14 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                    | Done     | Unknown    | N/A                 | N/A    |
| 15 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Unknown    | N/A                 | N/A    |
| 16 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999773145519655  | 0      |
| 17 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999661338036441  | 0      |
| 18 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999948051633638  | 0      |
| 19 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999951797461327  | 0      |
| 20 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Removed  | Done       | 0.9999977924664707  | 0      |
| 21 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.8968691513448818  | 0      |
| 22 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Removed  | Done       | 0.999998307324404   | 0      |
| 23 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.8257384615683324  | 0      |
| 24 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.8607435721557167  | 0      |
| 25 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
| 26 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Removed  | Done       | 0.9999981587754131  | 0      |
| 27 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Removed  | Done       | 0.9999980648985366  | 0      |
| 28 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.9685343574082788  | 0      |
| 29 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999956601570884  | 0      |
| 30 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999946480410227  | 0      |
| 31 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Removed  | Done       | 0.9999984096369762  | 0      |
| 32 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999923261676222  | 0      |
| 33 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 0.9999981618790315  | 0      |
| 34 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.99999026500907    | 0      |
| 35 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Removed  | Done       | 0.9999981182659028  | 0      |
| 36 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 37 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 38 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 39 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.46113042737473375 | 0      |
| 40 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.4520653383441138  | 0      |
| 41 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                 | 0      |
| 42 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Unknown  | Done       | 0.7114848977981927  | 0      |
| 43 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999976803531023  | 0      |
| 44 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999979390413046  | 0      |
| 45 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999979841004712  | 0      |
| 46 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.4077403951052718  | 0      |
| 47 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.5041756654589936  | 0      |
| 48 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.3461854579200792  | 0      |
| 49 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.3560810403685995  | 0      |
| 50 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | 0.9999979145929746  | 0      |
| 51 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?                   | Unknown  | Unknown    | N/A                 | N/A    |

