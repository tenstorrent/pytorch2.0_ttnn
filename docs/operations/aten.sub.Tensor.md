### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                 | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  2 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                   | Unknown  | Unknown    | N/A                 | N/A    |
|  3 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                         | Unknown  | Unknown    | N/A                 | N/A    |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999884228936096  | 0      |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999699594727713  | 0      |
|  6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999925994257263  | 0      |
|  7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999937693663652  | 0      |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999801631457735  | 0      |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.999976473674657   | 0      |
| 10 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.999990475038518   | 0      |
| 11 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999776600913368  | 0      |
| 12 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.999997745945796   | 0      |
| 13 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.7755848137199917  | 0      |
| 14 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | 0.9999993848264372  | 0      |
| 15 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.8154574749718381  | 0      |
| 16 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.7079996138536342  | 0      |
| 17 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
| 18 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.9999983231925157  | 0      |
| 19 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.9999973672765853  | 0      |
| 20 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.9557167624632799  | 0      |
| 21 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999946101611638  | 0      |
| 22 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999955384692216  | 0      |
| 23 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999980106602661  | 0      |
| 24 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999943544059529  | 0      |
| 25 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 1.0                 | 0      |
| 26 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999956501600038  | 0      |
| 27 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | 0.9999978807154879  | 0      |
| 28 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 29 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 30 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 31 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.47124994375692975 | 0      |
| 32 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.47363467098469064 | 0      |
| 33 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                 | 0      |
| 34 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Done     | Done       | 0.671157366336343   | 0      |
| 35 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Unknown  | Done       | 0.9999977604047658  | 0      |
| 36 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Unknown  | Done       | 0.9999978995422072  | 0      |
| 37 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Unknown  | Done       | 0.9999979485863456  | 0      |
| 38 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Unknown  | Done       | 0.9999981396674739  | 0      |
| 39 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Unknown  | Done       | 0.9999980133652198  | 0      |
| 40 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.5165982296370566  | 0      |
| 41 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.5021298421646404  | 0      |
| 42 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.3449326552029225  | 0      |
| 43 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.34945494969686686 | 0      |
| 44 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | Done       | 0.9999980926678117  | 0      |
| 45 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Unknown  | Done       | 0.9999979605375271  | 0      |
| 46 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | Done       | 0.9999980502154401  | 0      |

