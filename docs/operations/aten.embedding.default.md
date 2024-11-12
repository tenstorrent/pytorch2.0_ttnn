### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | None     | Fallback   | True  |
|  1 | Tensor<[1024, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                              | Unknown  | Fallback   | True  |
|  2 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                              | Done     | Done       | True  |
|  3 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | None     | Fallback   | True  |
|  4 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | None     | Unknown    | N/A   |
|  5 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | None     | Fallback   | True  |
|  6 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | None     | Fallback   | True  |
|  7 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                 | None     | Fallback   | True  |
|  8 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                              | Unknown  | Fallback   | True  |
|  9 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                             | Unknown  | Fallback   | True  |
| 10 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[2048]> indices = ?                              | Removed  | Done       | True  |
| 11 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Fallback   | True  |
| 12 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                            | None     | Fallback   | True  |
| 13 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | None     | Fallback   | True  |
| 14 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Done     | Done       | True  |
| 15 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1  | None     | Fallback   | True  |
| 16 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ?                            | Done     | Done       | True  |
| 17 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | None     | Fallback   | True  |
| 18 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | None     | Unknown    | N/A   |
| 19 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | None     | Fallback   | True  |
| 20 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0  | Done     | Done       | True  |
| 21 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | None     | Unknown    | N/A   |
| 22 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | None     | Fallback   | True  |
| 23 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | None     | Fallback   | True  |
| 24 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0     | None     | Unknown    | N/A   |
| 25 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | None     | Fallback   | True  |
| 26 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | None     | Fallback   | True  |
| 27 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Fallback   | True  |
| 28 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A   |
| 29 | Tensor<[32, 16]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | None     | Fallback   | True  |
| 30 | Tensor<[32, 16]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | None     | Fallback   | True  |
| 31 | Tensor<[32, 16]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Fallback   | True  |
| 32 | Tensor<[32, 16]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A   |
| 33 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | None     | Fallback   | True  |
| 34 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?                                | None     | Fallback   | True  |
| 35 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?                                | Unknown  | Fallback   | True  |
| 36 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Fallback   | True  |
| 37 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A   |
| 38 | Tensor<[32, 8]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | None     | Unknown    | N/A   |
| 39 | Tensor<[32, 8]> weight = ?,<br>Tensor<[10, 10]> indices = ?                                | None     | Unknown    | N/A   |
| 40 | Tensor<[32, 8]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Unknown    | N/A   |
| 41 | Tensor<[32, 8]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A   |
| 42 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                              | None     | Fallback   | True  |
| 43 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Fallback | Unknown    | N/A   |
| 44 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | None     | Fallback   | True  |
| 45 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Fallback   | True  |
| 46 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | None     | Unknown    | N/A   |
| 47 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | None     | Fallback   | True  |
| 48 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Fallback   | True  |
| 49 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | None     | Fallback   | True  |
| 50 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Fallback   | True  |
| 51 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                | None     | Fallback   | True  |
| 52 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ?                             | None     | Fallback   | True  |
| 53 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | None     | Fallback   | True  |
| 54 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Fallback   | True  |
| 55 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                            | Unknown  | Fallback   | True  |
| 56 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | Unknown  | Fallback   | True  |
| 57 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1     | Unknown  | Fallback   | True  |
| 58 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1    | None     | Fallback   | True  |
| 59 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                            | Done     | Done       | True  |
| 60 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                              | None     | Fallback   | True  |
| 61 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                              | None     | Unknown    | N/A   |
| 62 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                               | None     | Fallback   | True  |
| 63 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | None     | Unknown    | N/A   |
| 64 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                              | None     | Fallback   | True  |
| 65 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | None     | Unknown    | N/A   |
| 66 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Fallback   | True  |
| 67 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  | Fallback   | True  |
| 68 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1      | None     | Fallback   | True  |
| 69 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | None     | Fallback   | True  |
| 70 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Fallback   | True  |
| 71 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | None     | Fallback   | True  |
| 72 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?                                | None     | Fallback   | True  |
| 73 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1       | None     | Fallback   | True  |

