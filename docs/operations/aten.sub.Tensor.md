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
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999826852234254  | -1     |
|  9 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999778060983657  | -1     |
| 10 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999982629276005  | -1     |
| 11 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999776494348209  | -1     |
| 12 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Unknown    | N/A                 | N/A    |
| 13 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Unknown    | N/A                 | N/A    |
| 14 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                    | Done     | Unknown    | N/A                 | N/A    |
| 15 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Unknown    | N/A                 | N/A    |
| 16 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999738276051862  | -1     |
| 17 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 1.0                 | -1     |
| 18 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999978830649362  | -1     |
| 19 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999837980705101  | -1     |
| 20 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Unknown  | Done       | 0.9999976223763664  | -1     |
| 21 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.8375594978747734  | -1     |
| 22 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Unknown  | Done       | 0.9999987383127619  | -1     |
| 23 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.7210841051656802  | -1     |
| 24 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.6659784562019686  | -1     |
| 25 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | -1     |
| 26 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Unknown  | Done       | 0.9999980653306918  | -1     |
| 27 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Unknown  | Done       | 0.9999974600734379  | -1     |
| 28 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.9159424214984362  | -1     |
| 29 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.99999577587472    | -1     |
| 30 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999984823162086  | -1     |
| 31 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Unknown  | Done       | 0.9999981392324463  | -1     |
| 32 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999929137969817  | -1     |
| 33 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 0.9999982991601568  | -1     |
| 34 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999986651229965  | -1     |
| 35 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Unknown  | Done       | 0.9999984554613781  | -1     |
| 36 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 37 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 38 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 39 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.47210616260268035 | -1     |
| 40 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.49730768702774414 | -1     |
| 41 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                 | -1     |
| 42 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Done     | Done       | 0.751283714373252   | -1     |
| 43 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999970283854361  | -1     |
| 44 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999983492277893  | -1     |
| 45 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999979450617559  | -1     |
| 46 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.4603162535919398  | -1     |
| 47 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.47896935347387404 | -1     |
| 48 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.35774207242453515 | -1     |
| 49 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.35117264238670587 | -1     |
| 50 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Unknown  | Unknown    | N/A                 | N/A    |
| 51 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Unknown  | Done       | 0.9999979543605987  | -1     |
| 52 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Unknown  | Unknown    | N/A                 | N/A    |

