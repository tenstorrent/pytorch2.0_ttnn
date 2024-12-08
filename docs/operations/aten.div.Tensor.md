### aten.div.Tensor
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor other = 1.0                           | Unknown  | Done       | 1.0                | 0      |
|   1 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.9999958405511317 | 0      |
|   2 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                | 0      |
|   3 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | 0.999995880164483  | 0      |
|   4 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | 0.9999962188646434 | 0      |
|   5 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                | 0      |
|   6 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                | 0      |
|   7 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                | 0      |
|   8 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                | 0      |
|   9 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
|  10 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | None     | Fallback   | 1.0                | -1     |
|  11 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | None     | Fallback   | 1.0                | -1     |
|  12 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | None     | Fallback   | 1.0                | -1     |
|  13 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Done       | 1.0                | 0      |
|  14 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1                  | Unknown  | Unknown    | N/A                | N/A    |
|  15 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1.0                | Unknown  | Unknown    | N/A                | N/A    |
|  16 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor other = 1.0                | Unknown  | Unknown    | N/A                | N/A    |
|  17 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | 1.0                | -1     |
|  18 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  19 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
|  20 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
|  21 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | 1.0                | -1     |
|  22 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | None     | Fallback   | 1.0                | -1     |
|  23 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | None     | Fallback   | 1.0                | -1     |
|  24 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | 0.9999979435952258 | 0      |
|  25 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.8999999985098839    | Done     | Done       | 0.9999964470665957 | 0      |
|  26 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9043478220701218    | Done     | Done       | 0.9999955221097797 | 0      |
|  27 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9086956530809402    | Done     | Done       | 0.9999959268872209 | 0      |
|  28 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9130434766411781    | Done     | Done       | 0.999995637676343  | 0      |
|  29 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.917391300201416     | Done     | Done       | 0.9999952200472206 | 0      |
|  30 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9217391312122345    | Done     | Done       | 0.9999959330516438 | 0      |
|  31 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9260869547724724    | Done     | Done       | 0.9999952352594604 | 0      |
|  32 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9304347857832909    | Done     | Done       | 0.9999955832921716 | 0      |
|  33 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9347826093435287    | Done     | Done       | 0.999997151572926  | 0      |
|  34 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9391304366290569    | Done     | Done       | 0.9999961629274974 | 0      |
|  35 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9434782639145851    | Done     | Done       | 0.9999964812998597 | 0      |
|  36 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.947826087474823     | Done     | Done       | 0.9999952874554213 | 0      |
|  37 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9521739110350609    | Done     | Done       | 0.999996366617347  | 0      |
|  38 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9565217345952988    | Done     | Done       | 0.9999968424340807 | 0      |
|  39 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.960869561880827     | Done     | Done       | 0.9999961586330945 | 0      |
|  40 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9652173891663551    | Done     | Done       | 0.9999972338888707 | 0      |
|  41 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9695652164518833    | Done     | Done       | 0.9999994282304498 | 0      |
|  42 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9739130418747663    | Done     | Done       | 0.999995601741377  | 0      |
|  43 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9782608672976494    | Done     | Done       | 0.9999982014355224 | 0      |
|  44 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9826086945831776    | Done     | Done       | 0.9999962275381673 | 0      |
|  45 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9869565209373832    | Done     | Done       | 0.9999988858314507 | 0      |
|  46 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9913043472915888    | Done     | Done       | 0.9999982475415781 | 0      |
|  47 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9956521736457944    | Done     | Done       | 0.9999993671193093 | 0      |
|  48 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999964001111986 | 0      |
|  49 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9090909063816071     | Done     | Done       | 0.9999958493469259 | 0      |
|  50 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9181818142533302     | Done     | Done       | 0.999994946785256  | 0      |
|  51 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9272727221250534     | Done     | Done       | 0.9999961854218977 | 0      |
|  52 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9363636374473572     | Done     | Done       | 0.9999970700333767 | 0      |
|  53 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.94545454159379       | Done     | Done       | 0.9999956450538062 | 0      |
|  54 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9545454569160938     | Done     | Done       | 0.9999967710793165 | 0      |
|  55 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.963636364787817      | Done     | Done       | 0.9999978070348294 | 0      |
|  56 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9727272726595402     | Done     | Done       | 0.999997448778965  | 0      |
|  57 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9818181823939085     | Done     | Done       | 0.9999957851359215 | 0      |
|  58 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9909090911969543     | Done     | Done       | 0.9999974002855965 | 0      |
|  59 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | None     | Fallback   | 1.0                | -1     |
|  60 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357            | Done     | Done       | 1.0                | 0      |
|  61 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958269449397 | 0      |
|  62 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
|  63 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?              | None     | Fallback   | 1.0                | -1     |
|  64 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Done     | Done       | 0.9999971794939408 | 0      |
|  65 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 23, 1]> other = ?            | Done     | Done       | 0.999995445686149  | 0      |
|  66 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ?   | Done     | Done       | 0.9999998523779673 | 0      |
|  67 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999964926293035 | 0      |
|  68 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | 0.9999961692845966 | 0      |
|  69 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                | 0      |
|  70 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ?   | Done     | Done       | 0.9999998550997197 | 0      |
|  71 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Done       | 1.0                | 0      |
|  72 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  73 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0                   | Unknown  | Done       | 1.0                | 0      |
|  74 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | 0.9999967125479517 | 0      |
|  75 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | 0.9999972369176079 | 0      |
|  76 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958436568962 | 0      |
|  77 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
|  78 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  | Done       | 0.9999965691372387 | 0      |
|  79 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Done     | Done       | 0.9999999717600138 | 0      |
|  80 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | 0.9999952811378167 | 0      |
|  81 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | None     | Fallback   | 1.0                | -1     |
|  82 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  83 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  84 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.999995849446244  | 0      |
|  85 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958569096137 | 0      |
|  86 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.9999958855258891 | 0      |
|  87 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0                 | Done     | Done       | 1.0                | 0      |
|  88 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  89 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                | N/A    |
|  90 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  91 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                | N/A    |
|  92 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                | N/A    |
|  93 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781           | Done     | Done       | 0.9999956526484233 | 0      |
|  94 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | None     | Fallback   | 1.0                | -1     |
|  95 | Tensor<[10]> self = ?,<br>Tensor other = 10                              | Done     | Done       | 0.9999942924699067 | 0      |
|  96 | Tensor<[10]> self = ?,<br>Tensor other = 9.375                           | Done     | Done       | 0.9999964904909547 | 0      |
|  97 | Tensor<[128]> self = ?,<br>Tensor other = 128                            | None     | Fallback   | 1.0                | -1     |
|  98 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781           | None     | Fallback   | 1.0                | -1     |
|  99 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | None     | Fallback   | 1.0                | -1     |
| 100 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ?   | Done     | Done       | 0.9999962246680038 | 0      |
| 101 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ?   | Done     | Done       | 0.9999997829111021 | 0      |
| 102 | Tensor<[160]> self = ?,<br>Tensor other = 160                            | Done     | Done       | 0.999996173758411  | 0      |
| 103 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                          | Unknown  | Fallback   | 1.0                | -1     |
| 104 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357          | Unknown  | Fallback   | 1.0                | -1     |
| 105 | Tensor<[19]> self = ?,<br>Tensor other = 18.75                           | Done     | Done       | 0.9999961627321435 | 0      |
| 106 | Tensor<[1]> self = ?,<br>Tensor other = 1                                | Done     | Done       | 1.0                | 0      |
| 107 | Tensor<[1]> self = ?,<br>Tensor other = 1.0                              | Done     | Done       | 1.0                | 0      |
| 108 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                            | Unknown  | Fallback   | 1.0                | -1     |
| 109 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                | 0      |
| 110 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Done     | Done       | 0.9999969472025424 | 0      |
| 111 | Tensor<[20]> self = ?,<br>Tensor other = 20                              | Done     | Done       | 0.999996618765779  | 0      |
| 112 | Tensor<[2]> self = ?,<br>Tensor other = 2                                | Done     | Done       | 1.0                | 0      |
| 113 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999956026147289 | 0      |
| 114 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999953554792912 | 0      |
| 115 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  | Done       | 0.9999959851790456 | 0      |
| 116 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 5.0                        | Unknown  | Done       | 0.9999959620975359 | 0      |
| 117 | Tensor<[38]> self = ?,<br>Tensor other = 37.5                            | Done     | Done       | 0.9999985411329548 | 0      |
| 118 | Tensor<[3]> self = ?,<br>Tensor other = 3                                | Done     | Done       | 0.9999999240020481 | 0      |
| 119 | Tensor<[3]> self = ?,<br>Tensor other = 3.0                              | Done     | Done       | 0.9999977688263693 | 0      |
| 120 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ?   | Done     | Done       | 0.9999974727059786 | 0      |
| 121 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ?   | Done     | Done       | 0.9999999526098456 | 0      |
| 122 | Tensor<[5]> self = ?,<br>Tensor other = 4.6875                           | Done     | Done       | 0.9999954261452905 | 0      |
| 123 | Tensor<[5]> self = ?,<br>Tensor other = 5                                | Done     | Done       | 0.9999955724890098 | 0      |
| 124 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Done     | Done       | 0.9999999385140835 | 0      |
| 125 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Done     | Done       | 0.9999989650177519 | 0      |
| 126 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999958810931044 | 0      |
| 127 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999958115680312 | 0      |
| 128 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  | Done       | 0.9999958892252236 | 0      |
| 129 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 5.0                        | Unknown  | Done       | 0.9999958565867859 | 0      |
| 130 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                             | Unknown  | Fallback   | 1.0                | -1     |
| 131 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                  | Unknown  | Unknown    | N/A                | N/A    |
| 132 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357  | Unknown  | Unknown    | N/A                | N/A    |

