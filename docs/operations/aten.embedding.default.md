### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | Done     | Done       | True  |
|  1 | Tensor<[1024, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A   |
|  2 | Tensor<[1024, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                              | Removed  | Done       | True  |
|  3 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                              | Done     | Done       | True  |
|  4 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | Done     | Done       | True  |
|  5 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | Done     | Done       | True  |
|  6 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | Done     | Done       | True  |
|  7 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | Done     | Done       | True  |
|  8 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                 | Done     | Done       | True  |
|  9 | Tensor<[2048, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A   |
| 10 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                              | Unknown  | Done       | True  |
| 11 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                             | Unknown  | Done       | True  |
| 12 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[2048]> indices = ?                              | Removed  | Done       | True  |
| 13 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | True  |
| 14 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                            | Done     | Done       | True  |
| 15 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | None     | Fallback   | True  |
| 16 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Done     | Done       | True  |
| 17 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1  | Done     | Done       | True  |
| 18 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ?                            | Done     | Done       | True  |
| 19 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | True  |
| 20 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | True  |
| 21 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | True  |
| 22 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0  | Done     | Done       | True  |
| 23 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | True  |
| 24 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | True  |
| 25 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | Done     | Done       | True  |
| 26 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | True  |
| 27 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Done     | Done       | True  |
| 28 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Done     | Done       | True  |
| 29 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | True  |
| 30 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A   |
| 31 | Tensor<[32, 16]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Done     | Done       | True  |
| 32 | Tensor<[32, 16]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Done     | Done       | True  |
| 33 | Tensor<[32, 16]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | True  |
| 34 | Tensor<[32, 16]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A   |
| 35 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Done     | Done       | True  |
| 36 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?                                | Done     | Done       | False |
| 37 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?                                | Unknown  | Done       | False |
| 38 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | True  |
| 39 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A   |
| 40 | Tensor<[32, 8]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Done     | Done       | True  |
| 41 | Tensor<[32, 8]> weight = ?,<br>Tensor<[10, 10]> indices = ?                                | Done     | Done       | True  |
| 42 | Tensor<[32, 8]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | True  |
| 43 | Tensor<[32, 8]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A   |
| 44 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                              | Done     | Done       | True  |
| 45 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Done     | Done       | True  |
| 46 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | Done     | Done       | True  |
| 47 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | True  |
| 48 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Done     | Done       | True  |
| 49 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | Done     | Done       | True  |
| 50 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | True  |
| 51 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Done     | Done       | True  |
| 52 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | True  |
| 53 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                | Done     | Done       | True  |
| 54 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ?                             | Done     | Done       | True  |
| 55 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | Done     | Done       | True  |
| 56 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | True  |
| 57 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                            | Unknown  | Done       | True  |
| 58 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | Done     | Done       | True  |
| 59 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1     | Unknown  | Done       | True  |
| 60 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1    | Done     | Done       | True  |
| 61 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                            | Done     | Done       | True  |
| 62 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                              | Done     | Done       | True  |
| 63 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                              | Done     | Done       | True  |
| 64 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                               | Done     | Done       | True  |
| 65 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | Done     | Done       | True  |
| 66 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                              | Done     | Done       | True  |
| 67 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | Done     | Done       | True  |
| 68 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | True  |
| 69 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  | Done       | True  |
| 70 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1      | Done     | Done       | True  |
| 71 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Done     | Done       | True  |
| 72 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | True  |
| 73 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | Done     | Done       | True  |
| 74 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?                                | Done     | Done       | True  |
| 75 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1       | Done     | Done       | True  |

