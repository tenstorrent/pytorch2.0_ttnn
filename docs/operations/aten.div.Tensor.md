### aten.div.Tensor
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC                    | Host   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:-----------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor other = 1                                     | Unknown  | Unknown    | N/A                    | N/A    |
|   1 | Tensor self = ?,<br>Tensor other = 1.0                                   | Unknown  | Unknown    | N/A                    | N/A    |
|   2 | Tensor self = ?,<br>Tensor other = 10                                    | Unknown  | Unknown    | N/A                    | N/A    |
|   3 | Tensor self = ?,<br>Tensor other = 160                                   | Unknown  | Unknown    | N/A                    | N/A    |
|   4 | Tensor self = ?,<br>Tensor other = 18.75                                 | Unknown  | Unknown    | N/A                    | N/A    |
|   5 | Tensor self = ?,<br>Tensor other = 2                                     | Unknown  | Unknown    | N/A                    | N/A    |
|   6 | Tensor self = ?,<br>Tensor other = 20                                    | Unknown  | Unknown    | N/A                    | N/A    |
|   7 | Tensor self = ?,<br>Tensor other = 3                                     | Unknown  | Unknown    | N/A                    | N/A    |
|   8 | Tensor self = ?,<br>Tensor other = 3.0                                   | Unknown  | Unknown    | N/A                    | N/A    |
|   9 | Tensor self = ?,<br>Tensor other = 37.5                                  | Unknown  | Unknown    | N/A                    | N/A    |
|  10 | Tensor self = ?,<br>Tensor other = 4.6875                                | Unknown  | Unknown    | N/A                    | N/A    |
|  11 | Tensor self = ?,<br>Tensor other = 5                                     | Unknown  | Unknown    | N/A                    | N/A    |
|  12 | Tensor self = ?,<br>Tensor other = 9.375                                 | Unknown  | Unknown    | N/A                    | N/A    |
|  13 | Tensor self = ?,<br>Tensor other = ?                                     | Unknown  | Unknown    | N/A                    | N/A    |
|  14 | Tensor<[0, 1]> self = ?,<br>Tensor other = 1.0                           | Unknown  | Done       | 1.0                    | 0      |
|  15 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.9999958415619918     | 0      |
|  16 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                    | 0      |
|  17 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | 0.9999959362073743     | 0      |
|  18 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | 0.9999962291569785     | 0      |
|  19 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  20 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  21 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  22 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  23 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  24 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  25 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | None     | Fallback   | 1.0                    | -1     |
|  26 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | 0      |
|  27 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Done       | 1.0                    | 0      |
|  28 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1                  | Unknown  | Unknown    | N/A                    | N/A    |
|  29 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1.0                | Unknown  | Unknown    | N/A                    | N/A    |
|  30 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor other = 1.0                | Unknown  | Unknown    | N/A                    | N/A    |
|  31 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | 1.0                    | -1     |
|  32 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ?            | Unknown  | Unknown    | N/A                    | N/A    |
|  33 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  34 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  35 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | 1.0                    | -1     |
|  36 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | Done     | Done       | 0.9999954495785064     | 0      |
|  37 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | 0      |
|  38 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | 0.9999979539537865     | 0      |
|  39 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.8999999985098839    | Done     | Done       | 0.9999964165962231     | 0      |
|  40 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9043478220701218    | Done     | Done       | 0.9999955044279888     | 0      |
|  41 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9086956530809402    | Done     | Done       | 0.9999959480425834     | 0      |
|  42 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9130434766411781    | Done     | Done       | 0.9999956313393006     | 0      |
|  43 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.917391300201416     | Done     | Done       | 0.9999952268046333     | 0      |
|  44 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9217391312122345    | Done     | Done       | 0.9999958945237959     | 0      |
|  45 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9260869547724724    | Done     | Done       | 0.9999952679230228     | 0      |
|  46 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9304347857832909    | Done     | Done       | 0.9999955828230612     | 0      |
|  47 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9347826093435287    | Done     | Done       | 0.9999971496869475     | 0      |
|  48 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9391304366290569    | Done     | Done       | 0.9999961557328223     | 0      |
|  49 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9434782639145851    | Done     | Done       | 0.999996528042169      | 0      |
|  50 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.947826087474823     | Done     | Done       | 0.9999952658969761     | 0      |
|  51 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9521739110350609    | Done     | Done       | 0.9999963784047929     | 0      |
|  52 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9565217345952988    | Done     | Done       | 0.9999968864276214     | 0      |
|  53 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.960869561880827     | Done     | Done       | 0.9999961697758538     | 0      |
|  54 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9652173891663551    | Done     | Done       | 0.9999972288040838     | 0      |
|  55 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9695652164518833    | Done     | Done       | 0.999999432436729      | 0      |
|  56 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9739130418747663    | Done     | Done       | 0.9999956092318039     | 0      |
|  57 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9782608672976494    | Done     | Done       | 0.9999982001329918     | 0      |
|  58 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9826086945831776    | Done     | Done       | 0.9999962480688531     | 0      |
|  59 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9869565209373832    | Done     | Done       | 0.9999988960909193     | 0      |
|  60 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9913043472915888    | Done     | Done       | 0.9999983012509416     | 0      |
|  61 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9956521736457944    | Done     | Done       | 0.999999368801043      | 0      |
|  62 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999964505187591     | 0      |
|  63 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9090909063816071     | Done     | Done       | 0.9999958145139395     | 0      |
|  64 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9181818142533302     | Done     | Done       | 0.9999949678408352     | 0      |
|  65 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9272727221250534     | Done     | Done       | 0.9999961870391557     | 0      |
|  66 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9363636374473572     | Done     | Done       | 0.9999970751851508     | 0      |
|  67 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.94545454159379       | Done     | Done       | 0.9999956683794007     | 0      |
|  68 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9545454569160938     | Done     | Done       | 0.9999968103918352     | 0      |
|  69 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.963636364787817      | Done     | Done       | 0.9999978033663405     | 0      |
|  70 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9727272726595402     | Done     | Done       | 0.9999974857476418     | 0      |
|  71 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9818181823939085     | Done     | Done       | 0.9999957570441252     | 0      |
|  72 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9909090911969543     | Done     | Done       | 0.9999973963876777     | 0      |
|  73 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                    | 0      |
|  74 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                    | 0      |
|  75 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958329978246     | 0      |
|  76 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  77 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?              | None     | Fallback   | 1.0                    | -1     |
|  78 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Done     | Done       | 0.9999914167473705     | 0      |
|  79 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 23, 1]> other = ?            | Done     | Done       | 0.9999955519365475     | 0      |
|  80 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ?   | Done     | Done       | 0.999995275024988      | 0      |
|  81 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.999996450278784      | 0      |
|  82 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | 0.9999961421623229     | 0      |
|  83 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                    | 0      |
|  84 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ?   | Done     | Done       | -2.483491789693431e-06 | 0      |
|  85 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Done       | 1.0                    | 0      |
|  86 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
|  87 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0                   | Unknown  | Done       | 1.0                    | 0      |
|  88 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | 0.9999966900500675     | 0      |
|  89 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | 0.9999972439126948     | 0      |
|  90 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958191638538     | 0      |
|  91 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  92 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  | Done       | 0.9999964216579352     | 0      |
|  93 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Unknown  | Done       | 0.9999953835779557     | 0      |
|  94 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | 0.9999958648290441     | 0      |
|  95 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | 0      |
|  96 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
|  97 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
|  98 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958434424716     | 0      |
|  99 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958427489878     | 0      |
| 100 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.9999958726801931     | 0      |
| 101 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0                 | Done     | Done       | 1.0                    | 0      |
| 102 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
| 103 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                    | N/A    |
| 104 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
| 105 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                    | N/A    |
| 106 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                    | N/A    |
| 107 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999976393761879     | 0      |
| 108 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                    | 0      |
| 109 | Tensor<[128]> self = ?,<br>Tensor other = 128                            | Done     | Done       | 1.0                    | 0      |
| 110 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999958638524755     | 0      |
| 111 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                    | 0      |
| 112 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ?   | Done     | Done       | 0.9999966687634759     | 0      |
| 113 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ?   | Done     | Done       | 0.9999991640355695     | 0      |
| 114 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                          | Unknown  | Done       | 1.0                    | 0      |
| 115 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357          | Unknown  | Done       | 0.9999991673884344     | 0      |
| 116 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                    | 0      |
| 117 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                    | 0      |
| 118 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Done     | Done       | 0.999995825079207      | 0      |
| 119 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Unknown  | Done       | 0.999996335224991      | 0      |
| 120 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Unknown  | Done       | 0.9999949344838127     | 0      |
| 121 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  | Done       | 0.9999958955191186     | 0      |
| 122 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 5.0                        | Unknown  | Done       | 0.999995979861896      | 0      |
| 123 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ?   | Done     | Done       | 0.9999990191284687     | 0      |
| 124 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ?   | Done     | Done       | 0.9999999214834824     | 0      |
| 125 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Done     | Done       | 0.9999991537550148     | 0      |
| 126 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Done     | Done       | 0.9999977492411056     | 0      |
| 127 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999958387341259     | 0      |
| 128 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999957417758094     | 0      |
| 129 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 10.0                       | Unknown  | Done       | 0.9999959484673274     | 0      |
| 130 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 5.0                        | Unknown  | Done       | 0.9999959355399243     | 0      |
| 131 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                  | Unknown  | Unknown    | N/A                    | N/A    |
| 132 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357  | Unknown  | Unknown    | N/A                    | N/A    |

