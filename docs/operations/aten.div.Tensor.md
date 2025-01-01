### aten.div.Tensor
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC                    | Host   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:-----------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor other = 1                                     | Done     | Unknown    | N/A                    | N/A    |
|   1 | Tensor self = ?,<br>Tensor other = 1.0                                   | Done     | Unknown    | N/A                    | N/A    |
|   2 | Tensor self = ?,<br>Tensor other = 10                                    | Done     | Unknown    | N/A                    | N/A    |
|   3 | Tensor self = ?,<br>Tensor other = 128                                   | Done     | Unknown    | N/A                    | N/A    |
|   4 | Tensor self = ?,<br>Tensor other = 160                                   | Unknown  | Unknown    | N/A                    | N/A    |
|   5 | Tensor self = ?,<br>Tensor other = 18.75                                 | Done     | Unknown    | N/A                    | N/A    |
|   6 | Tensor self = ?,<br>Tensor other = 2                                     | Done     | Unknown    | N/A                    | N/A    |
|   7 | Tensor self = ?,<br>Tensor other = 20                                    | Done     | Unknown    | N/A                    | N/A    |
|   8 | Tensor self = ?,<br>Tensor other = 3                                     | Done     | Unknown    | N/A                    | N/A    |
|   9 | Tensor self = ?,<br>Tensor other = 3.0                                   | Done     | Unknown    | N/A                    | N/A    |
|  10 | Tensor self = ?,<br>Tensor other = 37.5                                  | Done     | Unknown    | N/A                    | N/A    |
|  11 | Tensor self = ?,<br>Tensor other = 4.6875                                | Done     | Unknown    | N/A                    | N/A    |
|  12 | Tensor self = ?,<br>Tensor other = 5                                     | Done     | Unknown    | N/A                    | N/A    |
|  13 | Tensor self = ?,<br>Tensor other = 9.375                                 | Done     | Unknown    | N/A                    | N/A    |
|  14 | Tensor self = ?,<br>Tensor<[1, 1, 40]> other = ?                         | Done     | Unknown    | N/A                    | N/A    |
|  15 | Tensor self = ?,<br>Tensor<[1, 23, 1]> other = ?                         | Done     | Unknown    | N/A                    | N/A    |
|  16 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.9999958353496856     | 0      |
|  17 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                    | 0      |
|  18 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | 0.999995915334419      | 0      |
|  19 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | 0.9999962107286755     | 0      |
|  20 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  21 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  22 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  23 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  24 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  25 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                    | 0      |
|  26 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | Done     | Fallback   | 1.0                    | -1     |
|  27 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | 0      |
|  28 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Done       | 1.0                    | 0      |
|  29 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1                  | Unknown  | Unknown    | N/A                    | N/A    |
|  30 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1.0                | Unknown  | Unknown    | N/A                    | N/A    |
|  31 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor other = 1.0                | Unknown  | Unknown    | N/A                    | N/A    |
|  32 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | 1.0                    | -1     |
|  33 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ?            | Unknown  | Unknown    | N/A                    | N/A    |
|  34 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  35 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  36 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Fallback   | 1.0                    | -1     |
|  37 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | Done     | Done       | 0.9999959552221348     | 0      |
|  38 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | 0      |
|  39 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | 0.9999979559288262     | 0      |
|  40 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.8999999985098839    | Done     | Done       | 0.9999964630040654     | 0      |
|  41 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9043478220701218    | Done     | Done       | 0.9999954978121599     | 0      |
|  42 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9086956530809402    | Done     | Done       | 0.9999959309598231     | 0      |
|  43 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9130434766411781    | Done     | Done       | 0.9999956837675884     | 0      |
|  44 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.917391300201416     | Done     | Done       | 0.9999952270129658     | 0      |
|  45 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9217391312122345    | Done     | Done       | 0.9999958958204596     | 0      |
|  46 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9260869547724724    | Done     | Done       | 0.9999952315593894     | 0      |
|  47 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9304347857832909    | Done     | Done       | 0.9999955911051551     | 0      |
|  48 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9347826093435287    | Done     | Done       | 0.9999971334723411     | 0      |
|  49 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9391304366290569    | Done     | Done       | 0.9999961512940432     | 0      |
|  50 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9434782639145851    | Done     | Done       | 0.9999965073510221     | 0      |
|  51 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.947826087474823     | Done     | Done       | 0.9999952415597427     | 0      |
|  52 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9521739110350609    | Done     | Done       | 0.9999963959305554     | 0      |
|  53 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9565217345952988    | Done     | Done       | 0.9999968502798888     | 0      |
|  54 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.960869561880827     | Done     | Done       | 0.9999960918771701     | 0      |
|  55 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9652173891663551    | Done     | Done       | 0.999997224747349      | 0      |
|  56 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9695652164518833    | Done     | Done       | 0.9999994339103032     | 0      |
|  57 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9739130418747663    | Done     | Done       | 0.9999956328886296     | 0      |
|  58 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9782608672976494    | Done     | Done       | 0.9999982122982984     | 0      |
|  59 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9826086945831776    | Done     | Done       | 0.9999962369160827     | 0      |
|  60 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9869565209373832    | Done     | Done       | 0.9999988918936097     | 0      |
|  61 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9913043472915888    | Done     | Done       | 0.9999982733009584     | 0      |
|  62 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor other = 0.9956521736457944    | Done     | Done       | 0.9999993672401412     | 0      |
|  63 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999964809967257     | 0      |
|  64 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9090909063816071     | Done     | Done       | 0.9999958079735025     | 0      |
|  65 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9181818142533302     | Done     | Done       | 0.9999949288303782     | 0      |
|  66 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9272727221250534     | Done     | Done       | 0.9999962000689796     | 0      |
|  67 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9363636374473572     | Done     | Done       | 0.9999970683285088     | 0      |
|  68 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.94545454159379       | Done     | Done       | 0.9999956674102998     | 0      |
|  69 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9545454569160938     | Done     | Done       | 0.9999968072764326     | 0      |
|  70 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.963636364787817      | Done     | Done       | 0.9999977949552488     | 0      |
|  71 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9727272726595402     | Done     | Done       | 0.9999974801264246     | 0      |
|  72 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9818181823939085     | Done     | Done       | 0.9999957603867095     | 0      |
|  73 | Tensor<[1, 197, 768]> self = ?,<br>Tensor other = 0.9909090911969543     | Done     | Done       | 0.999997396251481      | 0      |
|  74 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                    | 0      |
|  75 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                    | 0      |
|  76 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958424114732     | 0      |
|  77 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  78 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?              | Done     | Done       | 0.00024465973809213135 | 0      |
|  79 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ?   | Done     | Done       | 0.9999997678345013     | 0      |
|  80 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999964604868178     | 0      |
|  81 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | 0.9999962245836652     | 0      |
|  82 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                    | 0      |
|  83 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ?   | Done     | Done       | 0.99999766159316       | 0      |
|  84 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Done       | 1.0                    | 0      |
|  85 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
|  86 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0                   | Unknown  | Done       | 1.0                    | 0      |
|  87 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | 0.9999966811413903     | 0      |
|  88 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | 0.9999972660341616     | 0      |
|  89 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958285528219     | 0      |
|  90 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                    | 0      |
|  91 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  | Done       | 0.99999635905723       | 0      |
|  92 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Done     | Done       | 0.9999994462120121     | 0      |
|  93 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | 0.9999968002223454     | 0      |
|  94 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Done     | Done       | 1.0                    | 0      |
|  95 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
|  96 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
|  97 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.999995842743421      | 0      |
|  98 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.999995849771399      | 0      |
|  99 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.9999958219904195     | 0      |
| 100 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0                 | Done     | Done       | 1.0                    | 0      |
| 101 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
| 102 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                    | N/A    |
| 103 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                    | N/A    |
| 104 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                    | N/A    |
| 105 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                    | N/A    |
| 106 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999950977036134     | 0      |
| 107 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                    | 0      |
| 108 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999957948879469     | 0      |
| 109 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                    | 0      |
| 110 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ?   | Done     | Done       | 0.9999999830265722     | 0      |
| 111 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ?   | Done     | Done       | 0.9999999980821431     | 0      |
| 112 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                          | Unknown  | Done       | 1.0                    | 0      |
| 113 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357          | Unknown  | Done       | 0.9999988428665602     | 0      |
| 114 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                    | 0      |
| 115 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                    | 0      |
| 116 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Done     | Done       | 0.9999961792549854     | 0      |
| 117 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Removed  | Done       | 0.9999949985324148     | 0      |
| 118 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Removed  | Done       | 0.9999939802247989     | 0      |
| 119 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ?   | Done     | Done       | 0.9999989069746718     | 0      |
| 120 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ?   | Done     | Done       | 0.9999974720796553     | 0      |
| 121 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Done     | Done       | 2.133492813602036e-06  | 0      |
| 122 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Done     | Done       | 0.9999950041385524     | 0      |
| 123 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999957883721762     | 0      |
| 124 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999958181015361     | 0      |
| 125 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                  | Unknown  | Unknown    | N/A                    | N/A    |
| 126 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357  | Unknown  | Unknown    | N/A                    | N/A    |

