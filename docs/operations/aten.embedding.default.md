### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC                   | Host   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:----------------------|:-------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | Done     | Done       | 1.0                   | 0      |
|  1 | Tensor<[1024, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A                   | N/A    |
|  2 | Tensor<[169, 12]> weight = ?,<br>Tensor<[2401]> indices = ?                                | Done     | Unknown    | N/A                   | N/A    |
|  3 | Tensor<[169, 16]> weight = ?,<br>Tensor<[2401]> indices = ?                                | Done     | Unknown    | N/A                   | N/A    |
|  4 | Tensor<[169, 24]> weight = ?,<br>Tensor<[2401]> indices = ?                                | Done     | Unknown    | N/A                   | N/A    |
|  5 | Tensor<[169, 32]> weight = ?,<br>Tensor<[2401]> indices = ?                                | Done     | Unknown    | N/A                   | N/A    |
|  6 | Tensor<[169, 3]> weight = ?,<br>Tensor<[2401]> indices = ?                                 | Done     | Unknown    | N/A                   | N/A    |
|  7 | Tensor<[169, 4]> weight = ?,<br>Tensor<[2401]> indices = ?                                 | Done     | Unknown    | N/A                   | N/A    |
|  8 | Tensor<[169, 6]> weight = ?,<br>Tensor<[2401]> indices = ?                                 | Done     | Unknown    | N/A                   | N/A    |
|  9 | Tensor<[169, 8]> weight = ?,<br>Tensor<[2401]> indices = ?                                 | Done     | Unknown    | N/A                   | N/A    |
| 10 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                              | Done     | Done       | 1.0                   | 0      |
| 11 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | Done     | Done       | 1.0                   | 0      |
| 12 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | Done     | Done       | 1.0                   | 0      |
| 13 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | Done     | Done       | 1.0                   | 0      |
| 14 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | Done     | Done       | 1.0                   | 0      |
| 15 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                 | Done     | Done       | 1.0                   | 0      |
| 16 | Tensor<[2048, 768]> weight = ?,<br>Tensor indices = ?                                      | Done     | Unknown    | N/A                   | N/A    |
| 17 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                              | Unknown  | Done       | 1.0                   | 0      |
| 18 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                             | Unknown  | Done       | 1.0                   | 0      |
| 19 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                   | 0      |
| 20 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                            | Unknown  | Done       | 1.0                   | 0      |
| 21 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[19]> indices = ?                               | Done     | Unknown    | N/A                   | N/A    |
| 22 | Tensor<[225, 12]> weight = ?,<br>Tensor<[4096]> indices = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 23 | Tensor<[225, 16]> weight = ?,<br>Tensor<[4096]> indices = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 24 | Tensor<[225, 24]> weight = ?,<br>Tensor<[4096]> indices = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 25 | Tensor<[225, 32]> weight = ?,<br>Tensor<[4096]> indices = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 26 | Tensor<[225, 3]> weight = ?,<br>Tensor<[4096]> indices = ?                                 | Done     | Unknown    | N/A                   | N/A    |
| 27 | Tensor<[225, 4]> weight = ?,<br>Tensor<[4096]> indices = ?                                 | Done     | Unknown    | N/A                   | N/A    |
| 28 | Tensor<[225, 6]> weight = ?,<br>Tensor<[4096]> indices = ?                                 | Done     | Unknown    | N/A                   | N/A    |
| 29 | Tensor<[225, 8]> weight = ?,<br>Tensor<[4096]> indices = ?                                 | Done     | Unknown    | N/A                   | N/A    |
| 30 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | Done     | Done       | 1.0                   | 0      |
| 31 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Done     | Done       | 1.0                   | 0      |
| 32 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1  | Done     | Done       | 1.0                   | 0      |
| 33 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ?                            | Done     | Done       | 1.0                   | 0      |
| 34 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                   | 0      |
| 35 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                   | 0      |
| 36 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | 1.0                   | 0      |
| 37 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0  | Done     | Done       | 1.0                   | 0      |
| 38 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                   | 0      |
| 39 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | Done     | Done       | 1.0                   | 0      |
| 40 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | Done     | Done       | 1.0                   | 0      |
| 41 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0     | Done     | Done       | 1.0                   | 0      |
| 42 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | Done       | 1.0                   | 0      |
| 43 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Unknown  | Done       | 1.0                   | 0      |
| 44 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | 1.0                   | 0      |
| 45 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A                   | N/A    |
| 46 | Tensor<[32, 16]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | Done       | 1.0                   | 0      |
| 47 | Tensor<[32, 16]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | Unknown  | Done       | 1.0                   | 0      |
| 48 | Tensor<[32, 16]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | Done       | 1.0                   | 0      |
| 49 | Tensor<[32, 16]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | Unknown    | N/A                   | N/A    |
| 50 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | Done       | 1.0                   | 0      |
| 51 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?                                | Unknown  | Done       | 0.9606883638359601    | 0      |
| 52 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?                                | Unknown  | Done       | 0.0029971971533548822 | 0      |
| 53 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | 1.0                   | 0      |
| 54 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A                   | N/A    |
| 55 | Tensor<[32, 8]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | Done       | 1.0                   | 0      |
| 56 | Tensor<[32, 8]> weight = ?,<br>Tensor<[10, 10]> indices = ?                                | Unknown  | Done       | 1.0                   | 0      |
| 57 | Tensor<[32, 8]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | Done       | 1.0                   | 0      |
| 58 | Tensor<[32, 8]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | Unknown    | N/A                   | N/A    |
| 59 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                              | Done     | Done       | 1.0                   | 0      |
| 60 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Done     | Done       | 1.0                   | 0      |
| 61 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | Unknown  | Done       | 1.0                   | 0      |
| 62 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | 1.0                   | 0      |
| 63 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  | Done       | 1.0                   | 0      |
| 64 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | Unknown  | Done       | 1.0                   | 0      |
| 65 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                   | 0      |
| 66 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | Unknown  | Done       | 1.0                   | 0      |
| 67 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                   | 0      |
| 68 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                | Done     | Done       | 1.0                   | 0      |
| 69 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ?                             | Done     | Done       | 1.0                   | 0      |
| 70 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | Done     | Done       | 1.0                   | 0      |
| 71 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | Done       | 1.0                   | 0      |
| 72 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                            | Unknown  | Done       | 1.0                   | 0      |
| 73 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | Done     | Done       | 1.0                   | 0      |
| 74 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1     | Unknown  | Done       | 1.0                   | 0      |
| 75 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1    | Unknown  | Done       | 1.0                   | 0      |
| 76 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                            | Done     | Done       | 1.0                   | 0      |
| 77 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                              | Done     | Done       | 1.0                   | 0      |
| 78 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                              | Done     | Done       | 1.0                   | 0      |
| 79 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                               | Done     | Done       | 1.0                   | 0      |
| 80 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | Done     | Done       | 1.0                   | 0      |
| 81 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                              | Done     | Done       | 1.0                   | 0      |
| 82 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | Done     | Done       | 1.0                   | 0      |
| 83 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | Done       | 1.0                   | 0      |
| 84 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  | Done       | 1.0                   | 0      |
| 85 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1      | Done     | Done       | 1.0                   | 0      |
| 86 | Tensor<[51865, 768]> weight = ?,<br>Tensor indices = ?,<br>int padding_idx = 50257         | Unknown  | Unknown    | N/A                   | N/A    |
| 87 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0                   | 0      |
| 88 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | Done       | 1.0                   | 0      |
| 89 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | Done     | Done       | 1.0                   | 0      |
| 90 | Tensor<[7, 64]> weight = ?,<br>Tensor<[1, 7]> indices = ?                                  | Done     | Unknown    | N/A                   | N/A    |
| 91 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?                                | Done     | Done       | 1.0                   | 0      |
| 92 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1       | Done     | Done       | 1.0                   | 0      |

