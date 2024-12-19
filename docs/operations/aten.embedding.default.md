### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC                  | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:---------------------|:-------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | Done     | Done       | 1.0                  | 0      |
|  1 | Tensor<[1024, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A                  | N/A    |
|  2 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                              | Done     | Done       | 1.0                  | 0      |
|  3 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | Done     | Done       | 1.0                  | 0      |
|  4 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | Done     | Done       | 1.0                  | 0      |
|  5 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | Done     | Done       | 1.0                  | 0      |
|  6 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | Done     | Done       | 1.0                  | 0      |
|  7 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                 | Done     | Done       | 1.0                  | 0      |
|  8 | Tensor<[2048, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A                  | N/A    |
|  9 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                              | Unknown  | Done       | 1.0                  | 0      |
| 10 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                             | Unknown  | Done       | 1.0                  | 0      |
| 11 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                  | 0      |
| 12 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                            | Unknown  | Done       | 1.0                  | 0      |
| 13 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | Done     | Done       | 1.0                  | 0      |
| 14 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Done     | Done       | 1.0                  | 0      |
| 15 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1  | Done     | Done       | 1.0                  | 0      |
| 16 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ?                            | Done     | Done       | 1.0                  | 0      |
| 17 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                  | 0      |
| 18 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                  | 0      |
| 19 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | 1.0                  | 0      |
| 20 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0  | Done     | Done       | 1.0                  | 0      |
| 21 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                  | 0      |
| 22 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                  | 0      |
| 23 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | Done     | Done       | 1.0                  | 0      |
| 24 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | 1.0                  | 0      |
| 25 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | Done       | 1.0                  | 0      |
| 26 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Unknown  | Done       | 1.0                  | 0      |
| 27 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | 1.0                  | 0      |
| 28 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A                  | N/A    |
| 29 | Tensor<[32, 16]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | Done       | 1.0                  | 0      |
| 30 | Tensor<[32, 16]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Unknown  | Done       | 1.0                  | 0      |
| 31 | Tensor<[32, 16]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | 1.0                  | 0      |
| 32 | Tensor<[32, 16]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A                  | N/A    |
| 33 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | Done       | 1.0                  | 0      |
| 34 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?                                | Unknown  | Done       | 0.03676860853935325  | 0      |
| 35 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?                                | Unknown  | Done       | -0.01461990464113475 | 0      |
| 36 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | 1.0                  | 0      |
| 37 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A                  | N/A    |
| 38 | Tensor<[32, 8]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | Done       | 1.0                  | 0      |
| 39 | Tensor<[32, 8]> weight = ?,<br>Tensor<[10, 10]> indices = ?                                | Unknown  | Done       | 1.0                  | 0      |
| 40 | Tensor<[32, 8]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | 1.0                  | 0      |
| 41 | Tensor<[32, 8]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A                  | N/A    |
| 42 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                              | Done     | Done       | 1.0                  | 0      |
| 43 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Done     | Done       | 1.0                  | 0      |
| 44 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | Unknown  | Done       | 1.0                  | 0      |
| 45 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | 1.0                  | 0      |
| 46 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  | Done       | 1.0                  | 0      |
| 47 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | Unknown  | Done       | 1.0                  | 0      |
| 48 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                  | 0      |
| 49 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  | Unknown    | N/A                  | N/A    |
| 50 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                  | 0      |
| 51 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                | Done     | Done       | 1.0                  | 0      |
| 52 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ?                             | Done     | Done       | 1.0                  | 0      |
| 53 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | Done     | Done       | 1.0                  | 0      |
| 54 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                  | 0      |
| 55 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                            | Unknown  | Done       | 1.0                  | 0      |
| 56 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | Done     | Done       | 1.0                  | 0      |
| 57 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1     | Unknown  | Done       | 1.0                  | 0      |
| 58 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1    | Unknown  | Done       | 1.0                  | 0      |
| 59 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                            | Done     | Done       | 1.0                  | 0      |
| 60 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                              | Done     | Done       | 1.0                  | 0      |
| 61 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                              | Done     | Done       | 1.0                  | 0      |
| 62 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                               | Done     | Done       | 1.0                  | 0      |
| 63 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | Done     | Done       | 1.0                  | 0      |
| 64 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                              | Done     | Done       | 1.0                  | 0      |
| 65 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | Done     | Done       | 1.0                  | 0      |
| 66 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | 1.0                  | 0      |
| 67 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  | Done       | 1.0                  | 0      |
| 68 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1      | Done     | Done       | 1.0                  | 0      |
| 69 | Tensor<[51865, 768]> weight = ?,<br>Tensor indices = ?,<br>int padding_idx = 50257         | Unknown  | Unknown    | N/A                  | N/A    |
| 70 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0                  | 0      |
| 71 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0                  | 0      |
| 72 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | Done     | Done       | 1.0                  | 0      |
| 73 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?                                | Done     | Done       | 1.0                  | 0      |
| 74 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1       | Done     | Done       | 1.0                  | 0      |

