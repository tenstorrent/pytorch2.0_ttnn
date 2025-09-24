### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?                    | Done     | Unknown    | N/A                | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?                    | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?                    | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?                    | Done     | Unknown    | N/A                | N/A    |
|  4 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -3.0                 | Done     | Unknown    | N/A                | N/A    |
|  5 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -3.75                | Done     | Unknown    | N/A                | N/A    |
|  6 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1                    | Done     | Unknown    | N/A                | N/A    |
|  7 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 2.25                 | Done     | Unknown    | N/A                | N/A    |
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999666119272644 | 0      |
|  9 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999841251670301 | 0      |
| 10 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999992507874835 | 0      |
| 11 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999908115989408 | 0      |
| 12 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                    | Done     | Unknown    | N/A                | N/A    |
| 15 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999840190541377 | 0      |
| 17 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999823557248956 | 0      |
| 18 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999984968568354 | 0      |
| 19 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.999992474146877  | 0      |
| 20 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Removed  | Done       | 0.9999977812229848 | 0      |
| 21 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.9999989364183184 | 0      |
| 22 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Removed  | Done       | 0.99999758593918   | 0      |
| 23 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.9999977776985826 | 0      |
| 24 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.9999980173395475 | 0      |
| 25 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                | 0      |
| 26 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Removed  | Done       | 0.9999982048314761 | 0      |
| 27 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Removed  | Done       | 0.9999983869563039 | 0      |
| 28 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 1.0                | 0      |
| 29 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999922967738254 | 0      |
| 30 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999973282592459 | 0      |
| 31 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Removed  | Done       | 0.9999986432308775 | 0      |
| 32 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999915574892243 | 0      |
| 33 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 1.0                | 0      |
| 34 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999966759807019 | 0      |
| 35 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Removed  | Done       | 0.9999981078976131 | 0      |
| 36 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 37 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                | N/A    |
| 38 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                | N/A    |
| 39 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.9999979836066984 | 0      |
| 40 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.9999980047793164 | 0      |
| 41 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                | 0      |
| 42 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Unknown  | Done       | 0.9999983279788232 | 0      |
| 43 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999977595511013 | 0      |
| 44 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999996714334852 | 0      |
| 45 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 46 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999980256482266 | 0      |
| 47 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 48 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.9999981764226418 | 0      |
| 49 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.9999979930885353 | 0      |
| 50 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.9999979613851122 | 0      |
| 51 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.9999979915817057 | 0      |
| 52 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 53 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | 0.9999978375637687 | 0      |
| 54 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 55 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?                   | Unknown  | Unknown    | N/A                | N/A    |

