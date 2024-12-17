### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                 | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
|  1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  | Done       | 1.0                 | 0      |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.999984006697153   | 0      |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.99998018772364    | 0      |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                  | Removed  | Done       | 0.9999957356548896  | 0      |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999974936687406  | 0      |
|  6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999920778157896  | 0      |
|  7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?     | Removed  | Done       | 0.9999972302841111  | 0      |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999835112602086  | 0      |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999639432127284  | 0      |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                  | Removed  | Done       | 0.9999967532665371  | 0      |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999938945115615  | 0      |
| 12 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999950488615601  | 0      |
| 13 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?     | Removed  | Done       | 0.9999973338172247  | 0      |
| 14 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.9999985743780677  | 0      |
| 15 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | None     | Done       | 0.8233136038848756  | 0      |
| 16 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | 0.9999985285878786  | 0      |
| 17 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | None     | Done       | 0.8141329431359955  | 0      |
| 18 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.4793594695416081  | 0      |
| 19 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
| 20 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.9999979819199548  | 0      |
| 21 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.9999976873402389  | 0      |
| 22 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.825692351752887   | 0      |
| 23 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999944651035241  | 0      |
| 24 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999934261923835  | 0      |
| 25 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999982039389101  | 0      |
| 26 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999966231230086  | 0      |
| 27 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 1.0                 | 0      |
| 28 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999958764043831  | 0      |
| 29 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | 0.9999983119305519  | 0      |
| 30 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 31 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 32 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 33 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                         | Unknown  | Done       | 0.9999976355515116  | 0      |
| 34 | Tensor<[1066]> self = ?,<br>Tensor<[1066]> other = ?                   | Unknown  | Done       | 0.9999979837902634  | 0      |
| 35 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ?               | Removed  | Done       | 0.9999970628350019  | 0      |
| 36 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999963756610144  | 0      |
| 37 | Tensor<[128, 1]> self = ?,<br>Tensor<[128, 1]> other = ?               | Removed  | Done       | 0.9999973468791401  | 0      |
| 38 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999978090207421  | 0      |
| 39 | Tensor<[128]> self = ?,<br>Tensor<[128]> other = ?                     | Removed  | Done       | 0.9999983100424529  | 0      |
| 40 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.4659103720245983  | 0      |
| 41 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.48977788358711444 | 0      |
| 42 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999972073785048  | 0      |
| 43 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?                     | Removed  | Done       | 0.9999983121412789  | 0      |
| 44 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                 | 0      |
| 45 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | None     | Done       | 0.5824125515233141  | 0      |
| 46 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ?               | Removed  | Done       | 0.9999982126892879  | 0      |
| 47 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.999996117749646   | 0      |
| 48 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999979897352141  | 0      |
| 49 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999991833958097  | 0      |
| 50 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Removed  | Done       | 1.0                 | 0      |
| 51 | Tensor<[300, 1]> self = ?,<br>Tensor<[300, 1]> other = ?               | Unknown  | Done       | 0.9999974491753393  | 0      |
| 52 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 0.9999976935248694  | 0      |
| 53 | Tensor<[300]> self = ?,<br>Tensor<[300]> other = ?                     | Unknown  | Done       | 0.9999983325242893  | 0      |
| 54 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                           | Removed  | Done       | 0.9999978545710688  | 0      |
| 55 | Tensor<[320, 1]> self = ?,<br>Tensor<[320, 1]> other = ?               | Unknown  | Done       | 0.9999989024561446  | 0      |
| 56 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999976489056894  | 0      |
| 57 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?                     | Removed  | Done       | 0.9999982214161888  | 0      |
| 58 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  | Done       | 0.9999978751211523  | 0      |
| 59 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999979529910996  | 0      |
| 60 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Unknown  | Done       | 0.999998091206171   | 0      |
| 61 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.47444324056300585 | 0      |
| 62 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.5325523895950496  | 0      |
| 63 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                           | Removed  | Done       | 0.9999986918408716  | 0      |
| 64 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?                       | Removed  | Done       | 0.9999983890959037  | 0      |
| 65 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ?               | Removed  | Done       | 0.999997967432366   | 0      |
| 66 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999981638657582  | 0      |
| 67 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Removed  | Done       | 0.999997524852202   | 0      |
| 68 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                           | Removed  | Done       | 0.9999972175746361  | 0      |
| 69 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.359340543910519   | 0      |
| 70 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.3451878220132915  | 0      |
| 71 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                          | Removed  | Done       | 0.9999973370157481  | 0      |
| 72 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?                     | Removed  | Done       | 0.9999980189645907  | 0      |
| 73 | Tensor<[800, 1]> self = ?,<br>Tensor<[800, 1]> other = ?               | Unknown  | Done       | 0.9999980070056423  | 0      |
| 74 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 0.9999981435757019  | 0      |
| 75 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                           | Removed  | Done       | 0.9999961831003795  | 0      |
| 76 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?                       | Removed  | Done       | 0.9999978784230622  | 0      |
| 77 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | Done       | 0.9999979372519274  | 0      |
| 78 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | 0.9999979249534543  | 0      |
| 79 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | Done       | 0.9999980195818937  | 0      |

