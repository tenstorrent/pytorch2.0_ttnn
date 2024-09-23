### aten._scaled_dot_product_flash_attention.default
|    | ATen Input Variations                                                                                                                                            | Status   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1, 64]> key = ?,<br>Tensor<[1, 12, 1, 64]> value = ?                                                         | Unknown  |
|  1 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                                   | Unknown  |
|  2 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, 5, 64]> key = ?,<br>Tensor<[1, 12, 5, 64]> value = ?                                                         | Unknown  |
|  3 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s10 + 1, 64]> key = ?,<br>Tensor<[1, 12, s11 + 1, 64]> value = ?                                             | Unknown  |
|  4 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s12 + 1, 64]> key = ?,<br>Tensor<[1, 12, s13 + 1, 64]> value = ?                                             | Unknown  |
|  5 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s14 + 1, 64]> key = ?,<br>Tensor<[1, 12, s15 + 1, 64]> value = ?                                             | Unknown  |
|  6 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s16 + 1, 64]> key = ?,<br>Tensor<[1, 12, s17 + 1, 64]> value = ?                                             | Unknown  |
|  7 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s18 + 1, 64]> key = ?,<br>Tensor<[1, 12, s19 + 1, 64]> value = ?                                             | Unknown  |
|  8 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s2 + 1, 64]> key = ?,<br>Tensor<[1, 12, s3 + 1, 64]> value = ?                                               | Unknown  |
|  9 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s20 + 1, 64]> key = ?,<br>Tensor<[1, 12, s21 + 1, 64]> value = ?                                             | Unknown  |
| 10 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s22 + 1, 64]> key = ?,<br>Tensor<[1, 12, s23 + 1, 64]> value = ?                                             | Unknown  |
| 11 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s24 + 1, 64]> key = ?,<br>Tensor<[1, 12, s25 + 1, 64]> value = ?                                             | Unknown  |
| 12 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s4 + 1, 64]> key = ?,<br>Tensor<[1, 12, s5 + 1, 64]> value = ?                                               | Unknown  |
| 13 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s6 + 1, 64]> key = ?,<br>Tensor<[1, 12, s7 + 1, 64]> value = ?                                               | Unknown  |
| 14 | Tensor<[1, 12, 1, 64]> query = ?,<br>Tensor<[1, 12, s8 + 1, 64]> key = ?,<br>Tensor<[1, 12, s9 + 1, 64]> value = ?                                               | Unknown  |
| 15 | Tensor<[1, 12, 1500, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                                | Unknown  |
| 16 | Tensor<[1, 12, 197, 64]> query = ?,<br>Tensor<[1, 12, 197, 64]> key = ?,<br>Tensor<[1, 12, 197, 64]> value = ?                                                   | Unknown  |
| 17 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 1500, 64]> key = ?,<br>Tensor<[1, 12, 1500, 64]> value = ?                                                   | Unknown  |
| 18 | Tensor<[1, 12, 4, 64]> query = ?,<br>Tensor<[1, 12, 4, 64]> key = ?,<br>Tensor<[1, 12, 4, 64]> value = ?,<br>float<> dropout_p = 0.0,<br>bool<> is_causal = True | Unknown  |
| 19 | Tensor<[1, 12, 50, 64]> query = ?,<br>Tensor<[1, 12, 50, 64]> key = ?,<br>Tensor<[1, 12, 50, 64]> value = ?                                                      | Unknown  |
| 20 | Tensor<[1, 16, 1370, 80]> query = ?,<br>Tensor<[1, 16, 1370, 80]> key = ?,<br>Tensor<[1, 16, 1370, 80]> value = ?                                                | Unknown  |
| 21 | Tensor<[1, 16, 197, 64]> query = ?,<br>Tensor<[1, 16, 197, 64]> key = ?,<br>Tensor<[1, 16, 197, 64]> value = ?                                                   | Unknown  |
| 22 | Tensor<[1, 16, 50, 64]> query = ?,<br>Tensor<[1, 16, 50, 64]> key = ?,<br>Tensor<[1, 16, 50, 64]> value = ?                                                      | Unknown  |
| 23 | Tensor<[1, 8, 1024, 80]> query = ?,<br>Tensor<[1, 8, 1024, 80]> key = ?,<br>Tensor<[1, 8, 1024, 80]> value = ?                                                   | Unknown  |
| 24 | Tensor<[1, 8, 1024, 80]> query = ?,<br>Tensor<[1, 8, 9, 80]> key = ?,<br>Tensor<[1, 8, 9, 80]> value = ?                                                         | Unknown  |
| 25 | Tensor<[1, 8, 256, 160]> query = ?,<br>Tensor<[1, 8, 256, 160]> key = ?,<br>Tensor<[1, 8, 256, 160]> value = ?                                                   | Unknown  |
| 26 | Tensor<[1, 8, 256, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?                                                       | Unknown  |
| 27 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 4096, 40]> key = ?,<br>Tensor<[1, 8, 4096, 40]> value = ?                                                   | Unknown  |
| 28 | Tensor<[1, 8, 4096, 40]> query = ?,<br>Tensor<[1, 8, 9, 40]> key = ?,<br>Tensor<[1, 8, 9, 40]> value = ?                                                         | Unknown  |
| 29 | Tensor<[1, 8, 64, 160]> query = ?,<br>Tensor<[1, 8, 64, 160]> key = ?,<br>Tensor<[1, 8, 64, 160]> value = ?                                                      | Unknown  |
| 30 | Tensor<[1, 8, 64, 160]> query = ?,<br>Tensor<[1, 8, 9, 160]> key = ?,<br>Tensor<[1, 8, 9, 160]> value = ?                                                        | Unknown  |

