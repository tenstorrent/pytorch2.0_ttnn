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
|  8 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 1.0                | 0      |
|  9 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999782414995455 | 0      |
| 10 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999952763346133 | 0      |
| 11 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999930526611989 | 0      |
| 12 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Unknown    | N/A                | N/A    |
| 13 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Unknown    | N/A                | N/A    |
| 14 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                    | Done     | Unknown    | N/A                | N/A    |
| 15 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Unknown    | N/A                | N/A    |
| 16 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.0                 | Done     | Done       | 0.9999773465846982 | 0      |
| 17 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -3.75                | Done     | Done       | 0.9999674574599353 | 0      |
| 18 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                    | Done     | Done       | 0.9999950159893983 | 0      |
| 19 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2.25                 | Done     | Done       | 0.9999888472523598 | 0      |
| 20 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ? | Removed  | Done       | 0.9999983946630894 | 0      |
| 21 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 1]> other = ?                 | Unknown  | Done       | 0.9999986029449189 | 0      |
| 22 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?   | Removed  | Done       | 0.9999991034435673 | 0      |
| 23 | Tensor<[1, 15]> self = ?,<br>Tensor<[15, 1]> other = ?                 | Unknown  | Done       | 0.9999985434852967 | 0      |
| 24 | Tensor<[1, 17]> self = ?,<br>Tensor<[17, 1]> other = ?                 | Unknown  | Done       | 0.9999971906595898 | 0      |
| 25 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Unknown  | Done       | 1.0                | 0      |
| 26 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ? | Removed  | Done       | 0.9999979680860659 | 0      |
| 27 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?   | Removed  | Done       | 0.9999979386255017 | 0      |
| 28 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Unknown  | Done       | 1.0                | 0      |
| 29 | Tensor<[1, 32]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999961566270988 | 0      |
| 30 | Tensor<[1, 45]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999941780421367 | 0      |
| 31 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?   | Removed  | Done       | 0.999997952894577  | 0      |
| 32 | Tensor<[1, 59]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999891908609527 | 0      |
| 33 | Tensor<[1, 5]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 1.0                | 0      |
| 34 | Tensor<[1, 60]> self = ?,<br>Tensor other = 1                          | Unknown  | Done       | 0.9999980587104235 | 0      |
| 35 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?     | Removed  | Done       | 0.999998108234545  | 0      |
| 36 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[s0 + 1, 1]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 37 | Tensor<[1, s0]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                | N/A    |
| 38 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor other = 1                     | Unknown  | Unknown    | N/A                | N/A    |
| 39 | Tensor<[16, 1, 49]> self = ?,<br>Tensor<[16, 49, 1]> other = ?         | Done     | Done       | 0.9999979586985406 | 0      |
| 40 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> other = ?         | Done     | Done       | 0.9999980292159587 | 0      |
| 41 | Tensor<[1]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                | 0      |
| 42 | Tensor<[24, 1]> self = ?,<br>Tensor<[1, 24]> other = ?                 | Unknown  | Done       | 0.9999974603647298 | 0      |
| 43 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999978739149425 | 0      |
| 44 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?         | Done     | Done       | 0.9999974520389896 | 0      |
| 45 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 46 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?             | Done     | Done       | 0.9999978617922314 | 0      |
| 47 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 48 | Tensor<[4, 1, 49]> self = ?,<br>Tensor<[4, 49, 1]> other = ?           | Done     | Done       | 0.9999980357311914 | 0      |
| 49 | Tensor<[4, 1, 64]> self = ?,<br>Tensor<[4, 64, 1]> other = ?           | Done     | Done       | 0.9999979578846471 | 0      |
| 50 | Tensor<[64, 1, 49]> self = ?,<br>Tensor<[64, 49, 1]> other = ?         | Done     | Done       | 0.999997965163312  | 0      |
| 51 | Tensor<[64, 1, 64]> self = ?,<br>Tensor<[64, 64, 1]> other = ?         | Done     | Done       | 0.9999980041675012 | 0      |
| 52 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 53 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?             | Done     | Done       | 0.9999980108275006 | 0      |
| 54 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 55 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?                   | Unknown  | Unknown    | N/A                | N/A    |

