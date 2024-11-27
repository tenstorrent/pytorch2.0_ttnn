### aten.div.Tensor
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor other = 1.0                           | Unknown  | Done       | True  |
|   1 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | True  |
|   2 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | True  |
|   3 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | True  |
|   4 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | True  |
|   5 | Tensor<[1, 1024, 640]> self = ?,<br>Tensor other = 1.0                   | Unknown  | Done       | True  |
|   6 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | True  |
|   7 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | True  |
|   8 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | True  |
|   9 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | True  |
|  10 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | True  |
|  11 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | None     | Fallback   | True  |
|  12 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | None     | Fallback   | True  |
|  13 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | None     | Fallback   | True  |
|  14 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor other = 1.0                | Unknown  | Done       | True  |
|  15 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1                    | Unknown  | Fallback   | True  |
|  16 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Done       | True  |
|  17 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | True  |
|  18 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ?            | Unknown  | Unknown    | N/A   |
|  19 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | True  |
|  20 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | True  |
|  21 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | True  |
|  22 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | None     | Fallback   | True  |
|  23 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | None     | Fallback   | True  |
|  24 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | True  |
|  25 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.8999999985098839    | Done     | Done       | True  |
|  26 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9043478220701218    | Done     | Done       | True  |
|  27 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9086956530809402    | Done     | Done       | True  |
|  28 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9130434766411781    | Done     | Done       | True  |
|  29 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.917391300201416     | Done     | Done       | True  |
|  30 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9217391312122345    | Done     | Done       | True  |
|  31 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9260869547724724    | Done     | Done       | True  |
|  32 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9304347857832909    | Done     | Done       | True  |
|  33 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9347826093435287    | Done     | Done       | True  |
|  34 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9391304366290569    | Done     | Done       | True  |
|  35 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9434782639145851    | Done     | Done       | True  |
|  36 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.947826087474823     | Done     | Done       | True  |
|  37 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9521739110350609    | Done     | Done       | True  |
|  38 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9565217345952988    | Done     | Done       | True  |
|  39 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.960869561880827     | Done     | Done       | True  |
|  40 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9652173891663551    | Done     | Done       | True  |
|  41 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9695652164518833    | Done     | Done       | True  |
|  42 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9739130418747663    | Done     | Done       | True  |
|  43 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9782608672976494    | Done     | Done       | True  |
|  44 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9826086945831776    | Done     | Done       | True  |
|  45 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9869565209373832    | Done     | Done       | True  |
|  46 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9913043472915888    | Done     | Done       | True  |
|  47 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9956521736457944    | Done     | Done       | True  |
|  48 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | True  |
|  49 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9090909063816071     | Done     | Done       | True  |
|  50 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9181818142533302     | Done     | Done       | True  |
|  51 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9272727221250534     | Done     | Done       | True  |
|  52 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9363636374473572     | Done     | Done       | True  |
|  53 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.94545454159379       | Done     | Done       | True  |
|  54 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9545454569160938     | Done     | Done       | True  |
|  55 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.963636364787817      | Done     | Done       | True  |
|  56 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9727272726595402     | Done     | Done       | True  |
|  57 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9818181823939085     | Done     | Done       | True  |
|  58 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9909090911969543     | Done     | Done       | True  |
|  59 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Done     | Failed     | N/A   |
|  60 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357            | Done     | Done       | True  |
|  61 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | True  |
|  62 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | True  |
|  63 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?              | None     | Fallback   | True  |
|  64 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Done     | Done       | True  |
|  65 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 23, 1]> other = ?            | Done     | Done       | True  |
|  66 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ?   | Done     | Done       | True  |
|  67 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor other = 1.0                   | Unknown  | Done       | True  |
|  68 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | True  |
|  69 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | True  |
|  70 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | True  |
|  71 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ?   | Done     | Done       | True  |
|  72 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Done       | True  |
|  73 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0                   | Unknown  | Done       | True  |
|  74 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | True  |
|  75 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | True  |
|  76 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | True  |
|  77 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | True  |
|  78 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  | Done       | True  |
|  79 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Unknown  | Done       | True  |
|  80 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | True  |
|  81 | Tensor<[1, 64, 1280]> self = ?,<br>Tensor other = 1.0                    | Unknown  | Done       | True  |
|  82 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | None     | Fallback   | True  |
|  83 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Done       | True  |
|  84 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | True  |
|  85 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | True  |
|  86 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | True  |
|  87 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0                 | Done     | Done       | True  |
|  88 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781           | Done     | Done       | True  |
|  89 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | None     | Fallback   | True  |
|  90 | Tensor<[10]> self = ?,<br>Tensor other = 10                              | Unknown  | Failed     | N/A   |
|  91 | Tensor<[10]> self = ?,<br>Tensor other = 9.375                           | Unknown  | Done       | True  |
|  92 | Tensor<[128]> self = ?,<br>Tensor other = 128                            | Done     | Failed     | N/A   |
|  93 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781           | None     | Fallback   | True  |
|  94 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | None     | Fallback   | True  |
|  95 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ?   | Done     | Done       | True  |
|  96 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ?   | Done     | Done       | False |
|  97 | Tensor<[160]> self = ?,<br>Tensor other = 160                            | Unknown  | Failed     | N/A   |
|  98 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                          | Unknown  | Fallback   | True  |
|  99 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357          | Unknown  | Fallback   | True  |
| 100 | Tensor<[19]> self = ?,<br>Tensor other = 18.75                           | Unknown  | Done       | True  |
| 101 | Tensor<[1]> self = ?,<br>Tensor other = 1                                | Unknown  | Failed     | N/A   |
| 102 | Tensor<[1]> self = ?,<br>Tensor other = 1.0                              | Unknown  | Done       | True  |
| 103 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                            | Unknown  | Fallback   | True  |
| 104 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | True  |
| 105 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Done     | Done       | True  |
| 106 | Tensor<[20]> self = ?,<br>Tensor other = 20                              | Unknown  | Failed     | N/A   |
| 107 | Tensor<[2]> self = ?,<br>Tensor other = 2                                | Unknown  | Failed     | N/A   |
| 108 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Unknown  | Done       | True  |
| 109 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Unknown  | Done       | True  |
| 110 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  | Done       | True  |
| 111 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 5.0                        | Unknown  | Done       | True  |
| 112 | Tensor<[38]> self = ?,<br>Tensor other = 37.5                            | Unknown  | Done       | True  |
| 113 | Tensor<[3]> self = ?,<br>Tensor other = 3                                | Unknown  | Failed     | N/A   |
| 114 | Tensor<[3]> self = ?,<br>Tensor other = 3.0                              | Unknown  | Done       | True  |
| 115 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ?   | Done     | Done       | True  |
| 116 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ?   | Done     | Done       | True  |
| 117 | Tensor<[5]> self = ?,<br>Tensor other = 4.6875                           | Unknown  | Done       | True  |
| 118 | Tensor<[5]> self = ?,<br>Tensor other = 5                                | Unknown  | Failed     | N/A   |
| 119 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Done     | Done       | True  |
| 120 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Done     | Done       | True  |
| 121 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | True  |
| 122 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | True  |
| 123 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  | Done       | True  |
| 124 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 5.0                        | Unknown  | Done       | True  |
| 125 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                             | Unknown  | Fallback   | True  |
| 126 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                  | Unknown  | Unknown    | N/A   |
| 127 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357  | Unknown  | Unknown    | N/A   |

