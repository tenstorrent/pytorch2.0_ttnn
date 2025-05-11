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
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999771734017697  | -1     |
|  9 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.999972612388387   | -1     |
| 10 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.99999372436574    | -1     |
| 11 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999943887182302  | -1     |
| 12 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Unknown    | N/A                 | N/A    |
| 13 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Unknown    | N/A                 | N/A    |
| 14 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                    | Done     | Unknown    | N/A                 | N/A    |
| 15 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Unknown    | N/A                 | N/A    |
| 16 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999656054158962  | -1     |
| 17 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999835964721334  | -1     |
| 18 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999937677579372  | -1     |
| 19 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999830391075268  | -1     |
| 20 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Unknown  | Done       | 0.9999981019787797  | -1     |
| 21 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.7639298757885314  | -1     |
| 22 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Unknown  | Done       | 0.9999973857396126  | -1     |
| 23 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.7335934180400184  | -1     |
| 24 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.840054985372959   | -1     |
| 25 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | -1     |
| 26 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Unknown  | Done       | 0.9999982095372796  | -1     |
| 27 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Unknown  | Done       | 0.9999974017669292  | -1     |
| 28 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.517644191723447   | -1     |
| 29 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999933333946341  | -1     |
| 30 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999988025698954  | -1     |
| 31 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  | Done       | 0.9999986522358832  | -1     |
| 32 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999997235254992  | -1     |
| 33 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 1.0                 | -1     |
| 34 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999975032031787  | -1     |
| 35 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Unknown  | Done       | 0.9999982510242376  | -1     |
| 36 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 37 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 38 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 39 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.4637415594634708  | -1     |
| 40 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.46770905548911706 | -1     |
| 41 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                 | -1     |
| 42 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Done     | Done       | 0.719951034667372   | -1     |
| 43 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999971406226089  | -1     |
| 44 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999972378755381  | -1     |
| 45 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999980092858398  | -1     |
| 46 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.5267873751584519  | -1     |
| 47 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.5228178936250358  | -1     |
| 48 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.34911022158266547 | -1     |
| 49 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.35230075125977584 | -1     |
| 50 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | Unknown    | N/A                 | N/A    |
| 51 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Unknown  | Done       | 0.9999979526498867  | -1     |
| 52 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | Unknown    | N/A                 | N/A    |

