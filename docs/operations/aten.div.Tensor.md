### aten.div.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC                    | Host   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:-----------------------|:-------|
|  0 | Tensor self = ?,<br>Tensor other = 1                                     | Done     | Unknown    | N/A                    | N/A    |
|  1 | Tensor self = ?,<br>Tensor other = 1.0                                   | Unknown  | Unknown    | N/A                    | N/A    |
|  2 | Tensor self = ?,<br>Tensor other = 10                                    | Done     | Unknown    | N/A                    | N/A    |
|  3 | Tensor self = ?,<br>Tensor other = 128                                   | Unknown  | Unknown    | N/A                    | N/A    |
|  4 | Tensor self = ?,<br>Tensor other = 160                                   | Done     | Unknown    | N/A                    | N/A    |
|  5 | Tensor self = ?,<br>Tensor other = 18.75                                 | Unknown  | Unknown    | N/A                    | N/A    |
|  6 | Tensor self = ?,<br>Tensor other = 2                                     | Done     | Unknown    | N/A                    | N/A    |
|  7 | Tensor self = ?,<br>Tensor other = 20                                    | Done     | Unknown    | N/A                    | N/A    |
|  8 | Tensor self = ?,<br>Tensor other = 3                                     | Done     | Unknown    | N/A                    | N/A    |
|  9 | Tensor self = ?,<br>Tensor other = 3.0                                   | Unknown  | Unknown    | N/A                    | N/A    |
| 10 | Tensor self = ?,<br>Tensor other = 37.5                                  | Unknown  | Unknown    | N/A                    | N/A    |
| 11 | Tensor self = ?,<br>Tensor other = 4.6875                                | Unknown  | Unknown    | N/A                    | N/A    |
| 12 | Tensor self = ?,<br>Tensor other = 5                                     | Done     | Unknown    | N/A                    | N/A    |
| 13 | Tensor self = ?,<br>Tensor other = 9.375                                 | Unknown  | Unknown    | N/A                    | N/A    |
| 14 | Tensor self = ?,<br>Tensor other = ?                                     | Unknown  | Unknown    | N/A                    | N/A    |
| 15 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.9999958459278168     | -1     |
| 16 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Unknown  | Done       | 1.0                    | -1     |
| 17 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | 0.9999959112824983     | -1     |
| 18 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | 0.9999962548687503     | -1     |
| 19 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | -1     |
| 20 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | -1     |
| 21 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | -1     |
| 22 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | -1     |
| 23 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | -1     |
| 24 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | -1     |
| 25 | Tensor<[1, 12, 257, 257]> self = ?,<br>Tensor other = 8.0                | Done     | Unknown    | N/A                    | N/A    |
| 26 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | Done     | Done       | 0.9999969511341389     | -1     |
| 27 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | -1     |
| 28 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Done       | 0.9999942028581063     | -1     |
| 29 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ?            | Unknown  | Unknown    | N/A                    | N/A    |
| 30 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | -1     |
| 31 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Done       | 0.9999963480546693     | -1     |
| 32 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | Done     | Done       | 0.9999959375741968     | -1     |
| 33 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | -1     |
| 34 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | 0.9999979431968266     | -1     |
| 35 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                    | -1     |
| 36 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                    | -1     |
| 37 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958414186999     | -1     |
| 38 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0                | Unknown  | Done       | 1.0                    | -1     |
| 39 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?              | Unknown  | Done       | -6.116434707503554e-06 | -1     |
| 40 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Unknown  | Unknown    | N/A                    | N/A    |
| 41 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 23, 1]> other = ?            | Unknown  | Unknown    | N/A                    | N/A    |
| 42 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ?   | Done     | Done       | 0.9999998832715183     | -1     |
| 43 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999964466066291     | -1     |
| 44 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | 0.999996144477293      | -1     |
| 45 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                    | -1     |
| 46 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ?   | Done     | Done       | 0.9999992963080149     | -1     |
| 47 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | 0.9999966874570727     | -1     |
| 48 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | 0.9999972790301865     | -1     |
| 49 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958509505454     | -1     |
| 50 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0                | Unknown  | Done       | 1.0                    | -1     |
| 51 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  | Done       | 0.999996479120813      | -1     |
| 52 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Unknown  | Done       | 0.9999996949116009     | -1     |
| 53 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | 0.9999965463494408     | -1     |
| 54 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | -1     |
| 55 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958438544067     | -1     |
| 56 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958351633288     | -1     |
| 57 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.9999958684854694     | -1     |
| 58 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0                 | Unknown  | Done       | 1.0                    | -1     |
| 59 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999951947318427     | -1     |
| 60 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                    | -1     |
| 61 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999961200145198     | -1     |
| 62 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                    | -1     |
| 63 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ?   | Done     | Done       | 0.9999992161595351     | -1     |
| 64 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ?   | Done     | Done       | 0.9999987269578393     | -1     |
| 65 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                          | Unknown  | Done       | 1.0                    | -1     |
| 66 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357          | Unknown  | Done       | 0.999998739274597      | -1     |
| 67 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                    | -1     |
| 68 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                    | -1     |
| 69 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Done     | Done       | 0.9999961182141723     | -1     |
| 70 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999955216972023     | -1     |
| 71 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999960387597752     | -1     |
| 72 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ?   | Done     | Done       | 0.9999987956301725     | -1     |
| 73 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ?   | Done     | Done       | 0.9999963587963625     | -1     |
| 74 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Done     | Done       | 0.9999957743116282     | -1     |
| 75 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Done     | Done       | 5.163521942070873e-07  | -1     |
| 76 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Unknown  | Done       | 0.9999957419882616     | -1     |
| 77 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Unknown  | Done       | 0.9999958153020753     | -1     |
| 78 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  | Unknown    | N/A                    | N/A    |
| 79 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 5.0                        | Unknown  | Unknown    | N/A                    | N/A    |
| 80 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                  | Unknown  | Unknown    | N/A                    | N/A    |
| 81 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357  | Unknown  | Unknown    | N/A                    | N/A    |

