### aten.embedding.default
|    | ATen Input Variations                                                                      | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|  0 | Tensor<[1, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                                | None     | N/A                 | N/A          | N/A               | N/A                |
|  1 | Tensor<[1024, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                              | None     | N/A                 | N/A          | N/A               | N/A                |
|  2 | Tensor<[2, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                              | Done     | N/A                 | N/A          | N/A               | N/A                |
|  3 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                                | None     | N/A                 | N/A          | N/A               | N/A                |
|  4 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                                | None     | N/A                 | N/A          | N/A               | N/A                |
|  5 | Tensor<[2, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                                 | None     | N/A                 | N/A          | N/A               | N/A                |
|  6 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 193]> indices = ?                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  7 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                                | None     | N/A                 | N/A          | N/A               | N/A                |
|  8 | Tensor<[2, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                 | None     | N/A                 | N/A          | N/A               | N/A                |
|  9 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 10 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 11 | Tensor<[2048, 768]> weight = ?,<br>Tensor<[2048]> indices = ?                              | None     | N/A                 | N/A          | N/A               | N/A                |
| 12 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 13 | Tensor<[2050, 1024]> weight = ?,<br>Tensor<[1, 59]> indices = ?                            | None     | N/A                 | N/A          | N/A               | N/A                |
| 14 | Tensor<[250002, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1   | None     | N/A                 | N/A          | N/A               | N/A                |
| 15 | Tensor<[250880, 1536]> weight = ?,<br>Tensor<[1, 32]> indices = ?                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 16 | Tensor<[256008, 1024]> weight = ?,<br>Tensor<[1, 19]> indices = ?,<br>int padding_idx = 1  | None     | N/A                 | N/A          | N/A               | N/A                |
| 17 | Tensor<[262, 768]> weight = ?,<br>Tensor<[1, 2048]> indices = ?                            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 18 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?,<br>int padding_idx = 0    | None     | N/A                 | N/A          | N/A               | N/A                |
| 19 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?,<br>int padding_idx = 0    | None     | N/A                 | N/A          | N/A               | N/A                |
| 20 | Tensor<[30000, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?,<br>int padding_idx = 0     | None     | N/A                 | N/A          | N/A               | N/A                |
| 21 | Tensor<[30522, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?,<br>int padding_idx = 0  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 22 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?,<br>int padding_idx = 0    | None     | N/A                 | N/A          | N/A               | N/A                |
| 23 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?,<br>int padding_idx = 0    | None     | N/A                 | N/A          | N/A               | N/A                |
| 24 | Tensor<[30522, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                             | None     | N/A                 | N/A          | N/A               | N/A                |
| 25 | Tensor<[30528, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?,<br>int padding_idx = 0     | None     | N/A                 | N/A          | N/A               | N/A                |
| 26 | Tensor<[32, 12]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 27 | Tensor<[32, 12]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | None     | N/A                 | N/A          | N/A               | N/A                |
| 28 | Tensor<[32, 12]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 29 | Tensor<[32, 12]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 30 | Tensor<[32, 16]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 31 | Tensor<[32, 16]> weight = ?,<br>Tensor<[10, 10]> indices = ?                               | None     | N/A                 | N/A          | N/A               | N/A                |
| 32 | Tensor<[32, 16]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 33 | Tensor<[32, 16]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 34 | Tensor<[32, 6]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 35 | Tensor<[32, 6]> weight = ?,<br>Tensor<[15, 15]> indices = ?                                | None     | N/A                 | N/A          | N/A               | N/A                |
| 36 | Tensor<[32, 6]> weight = ?,<br>Tensor<[17, 17]> indices = ?                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 37 | Tensor<[32, 6]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 38 | Tensor<[32, 6]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 39 | Tensor<[32, 8]> weight = ?,<br>Tensor<[1, 1]> indices = ?                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 40 | Tensor<[32, 8]> weight = ?,<br>Tensor<[10, 10]> indices = ?                                | None     | N/A                 | N/A          | N/A               | N/A                |
| 41 | Tensor<[32, 8]> weight = ?,<br>Tensor<[2, 2]> indices = ?                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 42 | Tensor<[32, 8]> weight = ?,<br>Tensor<[s0 + 1, s0 + 1]> indices = ?                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 43 | Tensor<[320, 64]> weight = ?,<br>Tensor<[24, 24]> indices = ?                              | None     | N/A                 | N/A          | N/A               | N/A                |
| 44 | Tensor<[32000, 4096]> weight = ?,<br>Tensor<[1, 32]> indices = ?,<br>int padding_idx = 0   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 45 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 10]> indices = ?                           | None     | N/A                 | N/A          | N/A               | N/A                |
| 46 | Tensor<[32128, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 47 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | None     | N/A                 | N/A          | N/A               | N/A                |
| 48 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 15]> indices = ?                            | None     | N/A                 | N/A          | N/A               | N/A                |
| 49 | Tensor<[32128, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 50 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?                            | None     | N/A                 | N/A          | N/A               | N/A                |
| 51 | Tensor<[32128, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 52 | Tensor<[40, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                                | None     | N/A                 | N/A          | N/A               | N/A                |
| 53 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ?                             | None     | N/A                 | N/A          | N/A               | N/A                |
| 54 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?                               | None     | N/A                 | N/A          | N/A               | N/A                |
| 55 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 56 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 45]> indices = ?                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 57 | Tensor<[50257, 768]> weight = ?,<br>Tensor<[1, 7]> indices = ?                             | None     | N/A                 | N/A          | N/A               | N/A                |
| 58 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 1     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 59 | Tensor<[50272, 512]> weight = ?,<br>Tensor<[1, 59]> indices = ?,<br>int padding_idx = 1    | None     | N/A                 | N/A          | N/A               | N/A                |
| 60 | Tensor<[512, 1024]> weight = ?,<br>Tensor<[1, 256]> indices = ?                            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 61 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 12]> indices = ?                              | None     | N/A                 | N/A          | N/A               | N/A                |
| 62 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 14]> indices = ?                              | None     | N/A                 | N/A          | N/A               | N/A                |
| 63 | Tensor<[512, 128]> weight = ?,<br>Tensor<[1, 9]> indices = ?                               | None     | N/A                 | N/A          | N/A               | N/A                |
| 64 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 16]> indices = ?                              | None     | N/A                 | N/A          | N/A               | N/A                |
| 65 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 25]> indices = ?                              | None     | N/A                 | N/A          | N/A               | N/A                |
| 66 | Tensor<[512, 768]> weight = ?,<br>Tensor<[1, 8]> indices = ?                               | None     | N/A                 | N/A          | N/A               | N/A                |
| 67 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 1]> indices = ?                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 68 | Tensor<[51200, 1024]> weight = ?,<br>Tensor<[1, 5]> indices = ?                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 69 | Tensor<[514, 768]> weight = ?,<br>Tensor<[1, 10]> indices = ?,<br>int padding_idx = 1      | None     | N/A                 | N/A          | N/A               | N/A                |
| 70 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 1]> indices = ?,<br>int padding_idx = 50257 | None     | N/A                 | N/A          | N/A               | N/A                |
| 71 | Tensor<[51865, 768]> weight = ?,<br>Tensor<[1, 4]> indices = ?,<br>int padding_idx = 50257 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 72 | Tensor<[65024, 4544]> weight = ?,<br>Tensor<[1, 7]> indices = ?                            | None     | N/A                 | N/A          | N/A               | N/A                |
| 73 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?                                | None     | N/A                 | N/A          | N/A               | N/A                |
| 74 | Tensor<[81, 768]> weight = ?,<br>Tensor<[1, 24]> indices = ?,<br>int padding_idx = 1       | None     | N/A                 | N/A          | N/A               | N/A                |

