### aten.sub.Tensor
|    | ATen Input Variations                                          | Status   | Isolated   | PCC                 | Host   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?            | Done     | Unknown    | N/A                 | N/A    |
|  1 | Tensor self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?            | Done     | Unknown    | N/A                 | N/A    |
|  2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0         | Done     | Done       | 0.9999780324003936  | 0      |
|  3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75        | Done     | Done       | 0.9999652251835551  | 0      |
|  4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1            | Done     | Done       | 0.9999970970718275  | 0      |
|  5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25         | Done     | Done       | 0.9999959122442086  | 0      |
|  6 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0         | Done     | Done       | 1.0                 | 0      |
|  7 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75        | Done     | Done       | 0.9999929915306097  | 0      |
|  8 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1            | Done     | Done       | 0.9999932320686169  | 0      |
|  9 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25         | Done     | Done       | 0.9999937942929833  | 0      |
| 10 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?         | Unknown  | Done       | 0.7259906641335709  | 0      |
| 11 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?           | Unknown  | Done       | 1.0                 | 0      |
| 12 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?           | Unknown  | Done       | 0.9971416520793507  | 0      |
| 13 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                  | Done     | Done       | 0.9999988732516574  | 0      |
| 14 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                  | Unknown  | Done       | 0.9999949550119719  | 0      |
| 15 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                  | Unknown  | Done       | 0.9999963735047268  | 0      |
| 16 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                   | Unknown  | Done       | 1.0                 | 0      |
| 17 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                  | Unknown  | Done       | 0.9999939080838511  | 0      |
| 18 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ? | Unknown  | Unknown    | N/A                 | N/A    |
| 19 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                  | Unknown  | Unknown    | N/A                 | N/A    |
| 20 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1             | Unknown  | Unknown    | N/A                 | N/A    |
| 21 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ? | Done     | Done       | 0.43174600946071273 | 0      |
| 22 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ? | Done     | Done       | 0.47591432183638127 | 0      |
| 23 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     | Done       | 0.9999984431198267  | 0      |
| 24 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ? | Done     | Done       | 0.9999967411457373  | 0      |
| 25 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?     | Done     | Done       | 0.9999980411344755  | 0      |
| 26 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?   | Done     | Done       | 0.48244155937924105 | 0      |
| 27 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?   | Done     | Done       | 0.47721004621252816 | 0      |
| 28 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ? | Done     | Done       | 0.33788815479010825 | 0      |
| 29 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ? | Done     | Done       | 0.34650560784922263 | 0      |
| 30 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?     | Done     | Done       | 0.9999980708968458  | 0      |

