### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                 | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999881450831526  | 0      |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999622257577714  | 0      |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999932224557035  | 0      |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999957774866484  | 0      |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999852383325425  | 0      |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999747117503904  | 0      |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999950582380914  | 0      |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999900120531385  | 0      |
| 10 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.9999974887408466  | 0      |
| 11 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.6945852503127516  | 0      |
| 12 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | 0.9999981244571278  | 0      |
| 13 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.7555627331949348  | 0      |
| 14 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.6610536609497649  | 0      |
| 15 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
| 16 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.9999982383033347  | 0      |
| 17 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.9999987488236929  | 0      |
| 18 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.5954185347991444  | 0      |
| 19 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.999993280392168   | 0      |
| 20 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999929598695637  | 0      |
| 21 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999976453829043  | 0      |
| 22 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999978674107735  | 0      |
| 23 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 1.0                 | 0      |
| 24 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999964586109323  | 0      |
| 25 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | 0.9999999289165156  | 0      |
| 26 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 27 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 28 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 29 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.4671834403499779  | 0      |
| 30 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.46342692193400226 | 0      |
| 31 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                 | 0      |
| 32 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Done     | Done       | 0.7186992235335856  | 0      |
| 33 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Removed  | Done       | 0.9999941506494799  | 0      |
| 34 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Removed  | Done       | 0.9999987097368158  | 0      |
| 35 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999980261240174  | 0      |
| 36 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.4747629307920178  | 0      |
| 37 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.51144630679834    | 0      |
| 38 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.35726287365019294 | 0      |
| 39 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.3587241027887898  | 0      |
| 40 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | 0.999998065921215   | 0      |

