### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC                  | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:---------------------|:-------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | Done     | Done       | 1.0                  | 2      |
|  1 | Tensor<[1024, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A                  | N/A    |
|  2 | Tensor<[1024, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                              | Removed  | Done       | 1.0                  | 2      |
|  3 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                              | Done     | Done       | 1.0                  | 2      |
|  4 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | Done     | Done       | 1.0                  | 2      |
|  5 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | Done     | Done       | 1.0                  | 2      |
|  6 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | Done     | Done       | 1.0                  | 2      |
|  7 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | Done     | Done       | 1.0                  | 2      |
|  8 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                 | Done     | Done       | 1.0                  | 2      |
|  9 | Tensor<[2048, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A                  | N/A    |
| 10 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                              | Unknown  | Done       | 1.0                  | 2      |
| 11 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                             | Unknown  | Done       | 1.0                  | 2      |
| 12 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[2048]> indices = ?                              | Removed  | Done       | 1.0                  | 2      |
| 13 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                  | 2      |
| 14 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                            | Done     | Done       | 1.0                  | 2      |
| 15 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | Done     | Done       | 1.0                  | 2      |
| 16 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Done     | Done       | 1.0                  | 2      |
| 17 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1  | Done     | Done       | 1.0                  | 2      |
| 18 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ?                            | Done     | Done       | 1.0                  | 2      |
| 19 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                  | 2      |
| 20 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                  | 2      |
| 21 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | 1.0                  | 2      |
| 22 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0  | Done     | Done       | 1.0                  | 2      |
| 23 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                  | 2      |
| 24 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                  | 2      |
| 25 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | Done     | Done       | 1.0                  | 2      |
| 26 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | 1.0                  | 2      |
| 27 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | Done       | 1.0                  | 2      |
| 28 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Done     | Done       | 1.0                  | 2      |
| 29 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | 1.0                  | 2      |
| 30 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A                  | N/A    |
| 31 | Tensor<[32, 16]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | Done       | 1.0                  | 2      |
| 32 | Tensor<[32, 16]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Done     | Done       | 1.0                  | 2      |
| 33 | Tensor<[32, 16]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | 1.0                  | 2      |
| 34 | Tensor<[32, 16]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A                  | N/A    |
| 35 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | Done       | 1.0                  | 2      |
| 36 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?                                | Done     | Done       | -0.03258659950815386 | 2      |
| 37 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?                                | Unknown  | Done       | 0.013087501059243445 | 2      |
| 38 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | 1.0                  | 2      |
| 39 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A                  | N/A    |
| 40 | Tensor<[32, 8]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | Done       | 1.0                  | 2      |
| 41 | Tensor<[32, 8]> weight = ?,<br>Tensor<[10, 10]> indices = ?                                | Done     | Done       | 1.0                  | 2      |
| 42 | Tensor<[32, 8]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | 1.0                  | 2      |
| 43 | Tensor<[32, 8]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A                  | N/A    |
| 44 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                              | Done     | Done       | 1.0                  | 2      |
| 45 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Done     | Done       | 1.0                  | 2      |
| 46 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | Done     | Done       | 1.0                  | 2      |
| 47 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | 1.0                  | 2      |
| 48 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Done     | Done       | 1.0                  | 2      |
| 49 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | Done     | Done       | 1.0                  | 2      |
| 50 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                  | 2      |
| 51 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Done     | Unknown    | N/A                  | N/A    |
| 52 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                  | 2      |
| 53 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                | Done     | Done       | 1.0                  | 2      |
| 54 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ?                             | Done     | Done       | 1.0                  | 2      |
| 55 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | Done     | Done       | 1.0                  | 2      |
| 56 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                  | 2      |
| 57 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                            | Unknown  | Done       | 1.0                  | 2      |
| 58 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | Done     | Done       | 1.0                  | 2      |
| 59 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1     | Unknown  | Done       | 1.0                  | 2      |
| 60 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1    | Done     | Done       | 1.0                  | 2      |
| 61 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                            | Done     | Done       | 1.0                  | 2      |
| 62 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                              | Done     | Done       | 1.0                  | 2      |
| 63 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                              | Done     | Done       | 1.0                  | 2      |
| 64 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                               | Done     | Done       | 1.0                  | 2      |
| 65 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | Done     | Done       | 1.0                  | 2      |
| 66 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                              | Done     | Done       | 1.0                  | 2      |
| 67 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | Done     | Done       | 1.0                  | 2      |
| 68 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | 1.0                  | 2      |
| 69 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  | Done       | 1.0                  | 2      |
| 70 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1      | Done     | Done       | 1.0                  | 2      |
| 71 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Done     | Done       | 1.0                  | 2      |
| 72 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0                  | 2      |
| 73 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | Done     | Done       | 1.0                  | 2      |
| 74 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?                                | Done     | Done       | 1.0                  | 2      |
| 75 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1       | Done     | Done       | 1.0                  | 2      |

