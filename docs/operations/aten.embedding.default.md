### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC                | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | Done     | Done       | 1.0                | 0      |
|  1 | Tensor<[1024, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A                | N/A    |
|  2 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[8, 384]> indices = ?                              | Done     | Unknown    | N/A                | N/A    |
|  3 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | Done     | Done       | 1.0                | 0      |
|  4 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | Done     | Done       | 1.0                | 0      |
|  5 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | Done     | Done       | 1.0                | 0      |
|  6 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 193]> indices = ?                               | Unknown  | Unknown    | N/A                | N/A    |
|  7 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | Removed  | Done       | 1.0                | 0      |
|  8 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                 | Unknown  | Done       | 1.0                | 0      |
|  9 | Tensor<[2048, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A                | N/A    |
| 10 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                              | Unknown  | Done       | 1.0                | 0      |
| 11 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                             | Unknown  | Done       | 1.0                | 0      |
| 12 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                | 0      |
| 13 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                            | Unknown  | Done       | 1.0                | 0      |
| 14 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | Done     | Done       | 1.0                | 0      |
| 15 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Done     | Done       | 1.0                | 0      |
| 16 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ?                            | Done     | Done       | 1.0                | 0      |
| 17 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                | 0      |
| 18 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                | 0      |
| 19 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | 1.0                | 0      |
| 20 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[8, 384]> indices = ?,<br>int padding_idx = 0  | Done     | Unknown    | N/A                | N/A    |
| 21 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                | 0      |
| 22 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                | 0      |
| 23 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | Unknown  | Done       | 1.0                | 0      |
| 24 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | Done       | 1.0                | 0      |
| 25 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Unknown  | Done       | 1.0                | 0      |
| 26 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | 1.0                | 0      |
| 27 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A                | N/A    |
| 28 | Tensor<[32, 16]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | Done       | 1.0                | 0      |
| 29 | Tensor<[32, 16]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Unknown  | Done       | 1.0                | 0      |
| 30 | Tensor<[32, 16]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | 1.0                | 0      |
| 31 | Tensor<[32, 16]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A                | N/A    |
| 32 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | Done       | 1.0                | 0      |
| 33 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?                                | Unknown  | Done       | 0.9582195198088984 | 0      |
| 34 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?                                | Unknown  | Done       | 0.9286885344266481 | 0      |
| 35 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | 1.0                | 0      |
| 36 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A                | N/A    |
| 37 | Tensor<[32, 8]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | Done       | 1.0                | 0      |
| 38 | Tensor<[32, 8]> weight = ?,<br>Tensor<[10, 10]> indices = ?                                | Unknown  | Done       | 1.0                | 0      |
| 39 | Tensor<[32, 8]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | 1.0                | 0      |
| 40 | Tensor<[32, 8]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A                | N/A    |
| 41 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Unknown  | Done       | 1.0                | 0      |
| 42 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | Unknown  | Done       | 1.0                | 0      |
| 43 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | 1.0                | 0      |
| 44 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  | Done       | 1.0                | 0      |
| 45 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | Unknown  | Done       | 1.0                | 0      |
| 46 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                | 0      |
| 47 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  | Done       | 1.0                | 0      |
| 48 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                | 0      |
| 49 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                | Unknown  | Done       | 1.0                | 0      |
| 50 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ?                             | Done     | Done       | 1.0                | 0      |
| 51 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | Removed  | Done       | 1.0                | 0      |
| 52 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                | 0      |
| 53 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                            | Unknown  | Done       | 1.0                | 0      |
| 54 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | Done     | Done       | 1.0                | 0      |
| 55 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1     | Unknown  | Done       | 1.0                | 0      |
| 56 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1    | Unknown  | Done       | 1.0                | 0      |
| 57 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 384]> indices = ?                            | Removed  | Unknown    | N/A                | N/A    |
| 58 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                              | Removed  | Done       | 1.0                | 0      |
| 59 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                              | Removed  | Done       | 1.0                | 0      |
| 60 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                               | Done     | Done       | 1.0                | 0      |
| 61 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | Removed  | Done       | 1.0                | 0      |
| 62 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                              | Removed  | Done       | 1.0                | 0      |
| 63 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | 1.0                | 0      |
| 64 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  | Done       | 1.0                | 0      |
| 65 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1      | Done     | Done       | 1.0                | 0      |
| 66 | Tensor<[51865, 768]> weight = ?,<br>Tensor indices = ?,<br>int padding_idx = 50257         | Unknown  | Unknown    | N/A                | N/A    |
| 67 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0                | 0      |
| 68 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0                | 0      |
| 69 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | Unknown  | Unknown    | N/A                | N/A    |
| 70 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?                                | Removed  | Done       | 1.0                | 0      |

