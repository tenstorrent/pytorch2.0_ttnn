### aten.sub.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC                 | Host   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?                    | Done     | Unknown    | N/A                 | N/A    |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.999983295198952   | 0      |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999772175856515  | 0      |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999977401305099  | 0      |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999978247305389  | 0      |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999778790309996  | 0      |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999729385754629  | 0      |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999995430230482  | 0      |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999968706636687  | 0      |
| 10 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Done     | Done       | 0.9999978654677739  | 0      |
| 11 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.5000524453327189  | 0      |
| 12 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Done     | Done       | 0.9999961982157245  | 0      |
| 13 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.7113313413437282  | 0      |
| 14 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.8225429571172622  | 0      |
| 15 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                 | 0      |
| 16 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Done     | Done       | 0.9999980013647514  | 0      |
| 17 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Done     | Done       | 0.9999971542367087  | 0      |
| 18 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 0.9783696859592457  | 0      |
| 19 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999958101001826  | 0      |
| 20 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999988981328971  | 0      |
| 21 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Done     | Done       | 0.9999979685763244  | 0      |
| 22 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.999993133151181   | 0      |
| 23 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 0.9999826420617361  | 0      |
| 24 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999951060982513  | 0      |
| 25 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Done     | Done       | 0.9999972932496476  | 0      |
| 26 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                 | N/A    |
| 27 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                 | N/A    |
| 28 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                 | N/A    |
| 29 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.4482416479867026  | 0      |
| 30 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.45298791528884075 | 0      |
| 31 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                 | 0      |
| 32 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Done     | Done       | 0.8378164318088146  | 0      |
| 33 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Removed  | Done       | 0.9999972204828484  | 0      |
| 34 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Removed  | Done       | 0.9999994781238238  | 0      |
| 35 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999977588634938  | 0      |
| 36 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.5543439038639034  | 0      |
| 37 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.4844772773696062  | 0      |
| 38 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.3631106318163386  | 0      |
| 39 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.35161979079994127 | 0      |
| 40 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | 0.9999979974708183  | 0      |

