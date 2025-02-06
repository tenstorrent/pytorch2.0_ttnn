### aten.add.Tensor
|     | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|----:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999831948677038 | 0      |
|   1 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999965423501332 | 0      |
|   2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999972994642339 | 0      |
|   3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999868594569414 | 0      |
|   4 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.999993941082666  | 0      |
|   5 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999982525756698 | 0      |
|   6 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?          | Unknown  | Done       | 0.9999978153592569 | 0      |
|   7 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839              | Done     | Done       | 1.0                | 0      |
|   8 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9043478220701218              | Done     | Unknown    | N/A                | N/A    |
|   9 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9086956530809402              | Done     | Unknown    | N/A                | N/A    |
|  10 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9090909063816071              | Done     | Done       | 1.0                | 0      |
|  11 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9130434766411781              | Done     | Unknown    | N/A                | N/A    |
|  12 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032              | Done     | Done       | 1.0                | 0      |
|  13 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.917391300201416               | Done     | Unknown    | N/A                | N/A    |
|  14 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9181818142533302              | Done     | Done       | 1.0                | 0      |
|  15 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9217391312122345              | Done     | Unknown    | N/A                | N/A    |
|  16 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9260869547724724              | Done     | Unknown    | N/A                | N/A    |
|  17 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9272727221250534              | Done     | Done       | 1.0                | 0      |
|  18 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226              | Done     | Done       | 1.0                | 0      |
|  19 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9304347857832909              | Done     | Unknown    | N/A                | N/A    |
|  20 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9347826093435287              | Done     | Unknown    | N/A                | N/A    |
|  21 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9363636374473572              | Done     | Done       | 1.0                | 0      |
|  22 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9391304366290569              | Done     | Unknown    | N/A                | N/A    |
|  23 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323              | Done     | Done       | 1.0                | 0      |
|  24 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9434782639145851              | Done     | Unknown    | N/A                | N/A    |
|  25 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.94545454159379                | Done     | Done       | 1.0                | 0      |
|  26 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.947826087474823               | Done     | Done       | 1.0                | 0      |
|  27 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9521739110350609              | Done     | Done       | 1.0                | 0      |
|  28 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9545454569160938              | Done     | Done       | 1.0                | 0      |
|  29 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9565217345952988              | Done     | Done       | 1.0                | 0      |
|  30 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516              | Done     | Done       | 1.0                | 0      |
|  31 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.960869561880827               | Done     | Done       | 1.0                | 0      |
|  32 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.963636364787817               | Done     | Done       | 1.0                | 0      |
|  33 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9652173891663551              | Done     | Done       | 1.0                | 0      |
|  34 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9695652164518833              | Done     | Done       | 1.0                | 0      |
|  35 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161              | Done     | Done       | 1.0                | 0      |
|  36 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9727272726595402              | Done     | Done       | 1.0                | 0      |
|  37 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9739130418747663              | Done     | Done       | 1.0                | 0      |
|  38 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9782608672976494              | Done     | Done       | 1.0                | 0      |
|  39 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9818181823939085              | Done     | Done       | 1.0                | 0      |
|  40 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9826086945831776              | Done     | Done       | 1.0                | 0      |
|  41 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581              | Done     | Done       | 1.0                | 0      |
|  42 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9869565209373832              | Done     | Done       | 1.0                | 0      |
|  43 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9909090911969543              | Done     | Done       | 1.0                | 0      |
|  44 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9913043472915888              | Done     | Done       | 1.0                | 0      |
|  45 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9956521736457944              | Done     | Done       | 1.0                | 0      |
|  46 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                           | Unknown  | Done       | 1.0                | 0      |
|  47 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027    | Done     | Done       | 0.9999999961833478 | 0      |
|  48 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997     | Done     | Done       | 0.9999990442537776 | 0      |
|  49 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994     | Done     | Done       | 0.9999998635790378 | 0      |
|  50 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999950628300782 | 0      |
|  51 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | 0.9999980270073373 | 0      |
|  52 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999439813310392 | 0      |
|  53 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999951753002168 | 0      |
|  54 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999931043598059 | 0      |
|  55 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999916134794952 | 0      |
|  56 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999945429241028 | 0      |
|  57 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?              | Unknown  | Done       | 0.9999978851862629 | 0      |
|  58 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                | 0      |
|  59 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                | Unknown  | Done       | 0.9999976154372205 | 0      |
|  60 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Unknown  | Done       | 0.999998176205155  | 0      |
|  61 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                   | Unknown  | Done       | 0.9999980637810666 | 0      |
|  62 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?            | Unknown  | Done       | 0.999998005592038  | 0      |
|  63 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
|  64 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?              | Unknown  | Done       | 0.9999979571240494 | 0      |
|  65 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?              | Done     | Done       | 0.9999980386149995 | 0      |
|  66 | Tensor<[1, 100, 14, 14]> self = ?,<br>Tensor<[1, 100, 14, 14]> other = ?      | Done     | Done       | 0.9999980138196193 | 0      |
|  67 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?        | Done     | Done       | 0.9999979769633275 | 0      |
|  68 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1.0                | 0      |
|  69 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Done     | Done       | 1.0                | 0      |
|  70 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ?    | Done     | Done       | 0.9999979690643852 | 0      |
|  71 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ?    | Done     | Done       | 0.9999979950674686 | 0      |
|  72 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?    | Done     | Done       | 0.9999979864619292 | 0      |
|  73 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?          | Done     | Done       | 0.9999980088674597 | 0      |
|  74 | Tensor<[1, 1024, 17, 17]> self = ?,<br>Tensor<[1, 1024, 17, 17]> other = ?    | Done     | Unknown    | N/A                | N/A    |
|  75 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999979983513159 | 0      |
|  76 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999979620493715 | 0      |
|  77 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?    | Done     | Done       | 0.9999979910259417 | 0      |
|  78 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999979961131533 | 0      |
|  79 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?    | Done     | Done       | 0.9999979922376792 | 0      |
|  80 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?        | Done     | Done       | 0.9999980906787064 | 0      |
|  81 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999973695485573 | 0      |
|  82 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?      | Done     | Done       | 0.9999979962719872 | 0      |
|  83 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?    | Done     | Done       | 0.9999979898250928 | 0      |
|  84 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                                 | Done     | Done       | 1.0                | 0      |
|  85 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | 0.9999936006422098 | 0      |
|  86 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?      | Done     | Done       | 0.9999980705547107 | 0      |
|  87 | Tensor<[1, 112, 15, 15]> self = ?,<br>Tensor<[1, 112, 15, 15]> other = ?      | Done     | Done       | 0.9999979959804398 | 0      |
|  88 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?      | Done     | Done       | 0.9999979947944686 | 0      |
|  89 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ?      | Done     | Done       | 0.9999979719727252 | 0      |
|  90 | Tensor<[1, 116, 14, 14]> self = ?,<br>Tensor<[1, 116, 14, 14]> other = ?      | Done     | Done       | 0.9999980518031453 | 0      |
|  91 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999992964801168 | 0      |
|  92 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?          | Unknown  | Done       | 0.9999990374005131 | 0      |
|  93 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 1.0                | 0      |
|  94 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?            | Unknown  | Done       | 1.0                | 0      |
|  95 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999989968117878 | 0      |
|  96 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?            | Unknown  | Done       | 0.9999983297297076 | 0      |
|  97 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | 0.9999982186879564 | 0      |
|  98 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  99 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 100 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 101 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Done     | Done       | 0.9999976203703504 | 0      |
| 102 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?        | Unknown  | Done       | 0.9999975802599294 | 0      |
| 103 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ?          | Done     | Done       | 0.999998126055538  | 0      |
| 104 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?              | Done     | Done       | 0.9999980352303087 | 0      |
| 105 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<[1, 1, 1, 14]> other = ?          | Done     | Done       | 0.999997667715479  | 0      |
| 106 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ?    | Done     | Done       | 0.9999979912668555 | 0      |
| 107 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?         | Done     | Done       | 0.9999977267526187 | 0      |
| 108 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ?          | Done     | Done       | 0.9999980176411302 | 0      |
| 109 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999948795472903 | 0      |
| 110 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?            | Done     | Done       | 0.9999979714989823 | 0      |
| 111 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | 0.9999980005467562 | 0      |
| 112 | Tensor<[1, 12, 56, 56]> self = ?,<br>Tensor<[1, 12, 56, 56]> other = ?        | Done     | Done       | 0.9999980165068821 | 0      |
| 113 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ?             | Done     | Done       | 0.9999980701797596 | 0      |
| 114 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?              | Done     | Done       | 0.9999980693631635 | 0      |
| 115 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999976572945265 | 0      |
| 116 | Tensor<[1, 120, 17, 17]> self = ?,<br>Tensor<[1, 120, 17, 17]> other = ?      | Done     | Done       | 0.9999979840197704 | 0      |
| 117 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?      | Done     | Done       | 0.999997981867287  | 0      |
| 118 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?          | Done     | Done       | 0.9999979898097057 | 0      |
| 119 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?    | Done     | Done       | 0.9999980067306546 | 0      |
| 120 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                | 0      |
| 121 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                | 0      |
| 122 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979192599163 | 0      |
| 123 | Tensor<[1, 128, 112, 112]> self = ?,<br>Tensor<[1, 128, 112, 112]> other = ?  | Done     | Done       | 0.9999979882437836 | 0      |
| 124 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ?  | Done     | Done       | 0.9999979970839771 | 0      |
| 125 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999980634582348 | 0      |
| 126 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979479960741 | 0      |
| 127 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ?      | Done     | Done       | 0.9999979770672318 | 0      |
| 128 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ?      | Done     | Done       | 0.9999979994423828 | 0      |
| 129 | Tensor<[1, 128, 64, 64]> self = ?,<br>Tensor<[1, 128, 64, 64]> other = ?      | Done     | Done       | 0.9999979639101049 | 0      |
| 130 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?      | Done     | Done       | 0.9999979820696214 | 0      |
| 131 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999980058316352 | 0      |
| 132 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979855876309 | 0      |
| 133 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?        | Unknown  | Done       | 0.999998041723944  | 0      |
| 134 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 135 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, s0, s1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 136 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 137 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, s1, s2]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 138 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ?    | Done     | Done       | 0.9999979924187351 | 0      |
| 139 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ?      | Done     | Done       | 0.9999979701327846 | 0      |
| 140 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?        | Done     | Done       | 0.9999979972187517 | 0      |
| 141 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?    | Done     | Done       | 0.9999980128594813 | 0      |
| 142 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?              | Done     | Done       | 0.9999982932839849 | 0      |
| 143 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?      | Done     | Done       | 0.9999980176661674 | 0      |
| 144 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?      | Done     | Done       | 0.9999979910746608 | 0      |
| 145 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999948004468554 | 0      |
| 146 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?            | Done     | Done       | 0.9999979972078646 | 0      |
| 147 | Tensor<[1, 14, 56, 56]> self = ?,<br>Tensor<[1, 14, 56, 56]> other = ?        | Done     | Done       | 0.999998025805801  | 0      |
| 148 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?              | Done     | Done       | 0.9999979832238943 | 0      |
| 149 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?      | Done     | Done       | 0.9999980208654968 | 0      |
| 150 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?          | Done     | Done       | 0.9999979781784065 | 0      |
| 151 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?          | Done     | Done       | 0.9999979814038279 | 0      |
| 152 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999950468203374 | 0      |
| 153 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Unknown  | Done       | 0.9999980093512855 | 0      |
| 154 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
| 155 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?              | Unknown  | Done       | 0.9999980859600626 | 0      |
| 156 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ?          | Unknown  | Done       | 0.9999979998719313 | 0      |
| 157 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?             | Unknown  | Done       | 0.999998002456236  | 0      |
| 158 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?        | Done     | Done       | 0.9999980139505288 | 0      |
| 159 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Tensor<[1, 1536, 8, 8]> other = ?        | Done     | Done       | 0.9999979679149494 | 0      |
| 160 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999978564196698 | 0      |
| 161 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?          | Unknown  | Done       | 0.9999980303304472 | 0      |
| 162 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999947759654279 | 0      |
| 163 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?            | Unknown  | Done       | 0.9999976849679804 | 0      |
| 164 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999990326545656 | 0      |
| 165 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?            | Unknown  | Done       | 0.9999992820942976 | 0      |
| 166 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999974873229747 | 0      |
| 167 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Done       | 0.9999986248764536 | 0      |
| 168 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 169 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 170 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 171 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.999998326610279  | 0      |
| 172 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?        | Unknown  | Done       | 0.9999976731823844 | 0      |
| 173 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ?    | Done     | Done       | 0.9999979620783302 | 0      |
| 174 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?      | Done     | Done       | 0.9999980166203507 | 0      |
| 175 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?      | Done     | Done       | 0.9999979898984889 | 0      |
| 176 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ?    | Done     | Done       | 0.9999979905127134 | 0      |
| 177 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> other = ?         | Done     | Done       | 0.9999979973476393 | 0      |
| 178 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ?    | Done     | Done       | 0.9999979922884286 | 0      |
| 179 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor<[1, 1, 1, 256]> other = ?       | Done     | Done       | 0.9999979959696202 | 0      |
| 180 | Tensor<[1, 16, 28, 28]> self = ?,<br>Tensor<[1, 16, 28, 28]> other = ?        | Done     | Done       | 0.9999979622902524 | 0      |
| 181 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Done       | 0.9999978772843718 | 0      |
| 182 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Unknown  | Done       | 0.9999980051583671 | 0      |
| 183 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 184 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 185 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?              | Done     | Done       | 0.9999978717270797 | 0      |
| 186 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 187 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 188 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999978849500903 | 0      |
| 189 | Tensor<[1, 160, 14, 14]> self = ?,<br>Tensor<[1, 160, 14, 14]> other = ?      | Done     | Done       | 0.9999979926843314 | 0      |
| 190 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ?      | Done     | Done       | 0.9999979967648855 | 0      |
| 191 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ?      | Done     | Done       | 0.9999979816888888 | 0      |
| 192 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?      | Done     | Done       | 0.999997981857295  | 0      |
| 193 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?          | Done     | Done       | 0.999998060719466  | 0      |
| 194 | Tensor<[1, 160, 73, 73]> self = ?,<br>Tensor<[1, 160, 73, 73]> other = ?      | Done     | Unknown    | N/A                | N/A    |
| 195 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999980252804724 | 0      |
| 196 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?          | Done     | Done       | 0.9999979851805663 | 0      |
| 197 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ?      | Done     | Done       | 0.9999979937824536 | 0      |
| 198 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?        | Done     | Done       | 0.9999980191899172 | 0      |
| 199 | Tensor<[1, 185, 28, 28]> self = ?,<br>Tensor<[1, 185, 28, 28]> other = ?      | Done     | Done       | 0.9999980133650267 | 0      |
| 200 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ?            | Done     | Done       | 0.9999979842812442 | 0      |
| 201 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ?      | Done     | Done       | 0.9999979899642315 | 0      |
| 202 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ?      | Done     | Done       | 0.999998000271343  | 0      |
| 203 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?      | Done     | Done       | 0.999997990023105  | 0      |
| 204 | Tensor<[1, 192, 7, 7]> self = ?,<br>Tensor<[1, 192, 7, 7]> other = ?          | Done     | Done       | 0.9999980210744256 | 0      |
| 205 | Tensor<[1, 192, 71, 71]> self = ?,<br>Tensor<[1, 192, 71, 71]> other = ?      | Done     | Unknown    | N/A                | N/A    |
| 206 | Tensor<[1, 192, 8, 8]> self = ?,<br>Tensor<[1, 192, 8, 8]> other = ?          | Done     | Done       | 0.9999979839351494 | 0      |
| 207 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?        | Done     | Done       | 0.9999979922265477 | 0      |
| 208 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?          | Done     | Done       | 0.9999979970214413 | 0      |
| 209 | Tensor<[1, 196, 14, 14]> self = ?,<br>Tensor<[1, 196, 14, 14]> other = ?      | Done     | Done       | 0.999997953927493  | 0      |
| 210 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ?            | Done     | Done       | 0.9999979851252363 | 0      |
| 211 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?          | Done     | Done       | 0.9999979729448137 | 0      |
| 212 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?            | Done     | Done       | 0.9999980092832325 | 0      |
| 213 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                | 0      |
| 214 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 215 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Done       | 1.0                | 0      |
| 216 | Tensor<[1, 20, 28, 28]> self = ?,<br>Tensor<[1, 20, 28, 28]> other = ?        | Done     | Done       | 0.9999980695618556 | 0      |
| 217 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?        | Done     | Done       | 0.9999979796434495 | 0      |
| 218 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1.0                | 0      |
| 219 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Done     | Done       | 1.0                | 0      |
| 220 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999980036617505 | 0      |
| 221 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?    | Done     | Done       | 0.9999979832598751 | 0      |
| 222 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999980069617534 | 0      |
| 223 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?    | Done     | Done       | 0.9999979890296247 | 0      |
| 224 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?        | Done     | Done       | 0.9999979821646675 | 0      |
| 225 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?          | Done     | Done       | 0.9999980020515605 | 0      |
| 226 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?             | Done     | Done       | 0.9999979979730516 | 0      |
| 227 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?      | Done     | Done       | 0.9999980260461752 | 0      |
| 228 | Tensor<[1, 208, 9, 9]> self = ?,<br>Tensor<[1, 208, 9, 9]> other = ?          | Done     | Done       | 0.9999980053312922 | 0      |
| 229 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?      | Done     | Done       | 0.9999979952002523 | 0      |
| 230 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?      | Done     | Done       | 0.9999979961318447 | 0      |
| 231 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?          | Done     | Done       | 0.9999980191235415 | 0      |
| 232 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                | 0      |
| 233 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ?      | Done     | Done       | 0.9999979631982422 | 0      |
| 234 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?      | Done     | Done       | 0.9999979992050522 | 0      |
| 235 | Tensor<[1, 24, 112, 112]> self = ?,<br>Tensor<[1, 24, 112, 112]> other = ?    | Done     | Done       | 0.9999979949504735 | 0      |
| 236 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?        | Done     | Done       | 0.9999980093172195 | 0      |
| 237 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?        | Done     | Done       | 0.9999979900336747 | 0      |
| 238 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?        | Done     | Done       | 0.9999980091846029 | 0      |
| 239 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?        | Done     | Done       | 0.9999980346576698 | 0      |
| 240 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?        | Done     | Done       | 0.9999980002327158 | 0      |
| 241 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?        | Done     | Done       | 0.9999980013153991 | 0      |
| 242 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?              | Done     | Done       | 0.9999979919775548 | 0      |
| 243 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?        | Done     | Done       | 0.999998018940413  | 0      |
| 244 | Tensor<[1, 240, 14, 14]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?      | Done     | Done       | 0.9999979873512348 | 0      |
| 245 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?      | Done     | Done       | 0.9999980178598452 | 0      |
| 246 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?              | Done     | Done       | 0.9999980328028109 | 0      |
| 247 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?        | Done     | Done       | 0.9999980073461793 | 0      |
| 248 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                | 0      |
| 249 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                | 0      |
| 250 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979593640073 | 0      |
| 251 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ?  | Done     | Done       | 0.9999979905947328 | 0      |
| 252 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?          | Done     | Done       | 0.9999979861327076 | 0      |
| 253 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ?  | Done     | Done       | 0.999997991359285  | 0      |
| 254 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?          | Done     | Done       | 0.9999979802997    | 0      |
| 255 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ?      | Done     | Done       | 0.9999979827532793 | 0      |
| 256 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?      | Done     | Done       | 0.9999980095266815 | 0      |
| 257 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?            | Done     | Done       | 0.9999980584546337 | 0      |
| 258 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999980239703101 | 0      |
| 259 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ?  | Done     | Done       | 0.9999979927189506 | 0      |
| 260 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999980302207339 | 0      |
| 261 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ?  | Done     | Done       | 0.9999979858826048 | 0      |
| 262 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?            | Done     | Done       | 0.9999979961108524 | 0      |
| 263 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.9999980049071687 | 0      |
| 264 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ?      | Done     | Done       | 0.9999979694680561 | 0      |
| 265 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?      | Done     | Done       | 0.9999979876394142 | 0      |
| 266 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?              | Done     | Done       | 0.999997876412867  | 0      |
| 267 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?      | Done     | Done       | 0.9999979663103362 | 0      |
| 268 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999979971133353 | 0      |
| 269 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999979683612681 | 0      |
| 270 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?      | Done     | Done       | 0.9999979797981893 | 0      |
| 271 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ?            | Done     | Done       | 0.999997975785595  | 0      |
| 272 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?      | Done     | Done       | 0.9999980021276503 | 0      |
| 273 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?      | Done     | Done       | 0.99999798301738   | 0      |
| 274 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?              | Done     | Done       | 0.9999979161020195 | 0      |
| 275 | Tensor<[1, 256, 7, 7]> self = ?,<br>Tensor<[1, 256, 7, 7]> other = ?          | Done     | Done       | 0.9999979406713457 | 0      |
| 276 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?      | Done     | Done       | 0.9999979922131883 | 0      |
| 277 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.999997988796854  | 0      |
| 278 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ?      | Done     | Done       | 0.9999978701938919 | 0      |
| 279 | Tensor<[1, 272, 7, 7]> self = ?,<br>Tensor<[1, 272, 7, 7]> other = ?          | Done     | Done       | 0.9999980600105102 | 0      |
| 280 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?      | Done     | Done       | 0.9999979957791715 | 0      |
| 281 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?      | Done     | Done       | 0.999997984133926  | 0      |
| 282 | Tensor<[1, 28, 28, 28]> self = ?,<br>Tensor<[1, 28, 28, 28]> other = ?        | Done     | Done       | 0.9999980371479625 | 0      |
| 283 | Tensor<[1, 288, 14, 14]> self = ?,<br>Tensor<[1, 288, 14, 14]> other = ?      | Done     | Done       | 0.9999979832442465 | 0      |
| 284 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?    | Done     | Done       | 0.9999979846561606 | 0      |
| 285 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?      | Removed  | Done       | 0.9999979809207364 | 0      |
| 286 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?      | Removed  | Done       | 0.9999979914388399 | 0      |
| 287 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?    | Removed  | Done       | 0.9999980025732284 | 0      |
| 288 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?            | Done     | Done       | 0.9999980065475217 | 0      |
| 289 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?        | Done     | Done       | 0.9999979977017371 | 0      |
| 290 | Tensor<[1, 32, 112, 112]> self = ?,<br>Tensor<[1, 32, 112, 112]> other = ?    | Done     | Done       | 0.9999979737568931 | 0      |
| 291 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?    | Done     | Done       | 0.9999979924729757 | 0      |
| 292 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?            | Done     | Done       | 0.9999980325154105 | 0      |
| 293 | Tensor<[1, 32, 256, 256]> self = ?,<br>Tensor<[1, 32, 256, 256]> other = ?    | Done     | Done       | 0.9999979913494931 | 0      |
| 294 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ?        | Done     | Done       | 0.9999980612637471 | 0      |
| 295 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?      | Done     | Done       | 0.9999980007171752 | 0      |
| 296 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?      | Done     | Done       | 0.9999979689482896 | 0      |
| 297 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?        | Done     | Done       | 0.9999980007941452 | 0      |
| 298 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?        | Done     | Done       | 0.999998018705443  | 0      |
| 299 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999947402229779 | 0      |
| 300 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.999994786162572  | 0      |
| 301 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?        | Done     | Done       | 0.9999980103176401 | 0      |
| 302 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?        | Done     | Done       | 0.9999979974559821 | 0      |
| 303 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?        | Done     | Done       | 0.9999979876867928 | 0      |
| 304 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?      | Done     | Done       | 0.999997976072835  | 0      |
| 305 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Done       | 0.9999980208007747 | 0      |
| 306 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?      | Unknown  | Done       | 0.9999979844754517 | 0      |
| 307 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 308 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 309 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?      | Done     | Done       | 0.9999980025012801 | 0      |
| 310 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?      | Done     | Done       | 0.9999979918023936 | 0      |
| 311 | Tensor<[1, 34, 28, 28]> self = ?,<br>Tensor<[1, 34, 28, 28]> other = ?        | Done     | Done       | 0.9999980463398527 | 0      |
| 312 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?        | Done     | Done       | 0.9999979105550608 | 0      |
| 313 | Tensor<[1, 36, 56, 56]> self = ?,<br>Tensor<[1, 36, 56, 56]> other = ?        | Done     | Done       | 0.9999980285719371 | 0      |
| 314 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?        | Done     | Done       | 0.9999979977036567 | 0      |
| 315 | Tensor<[1, 384, 35, 35]> self = ?,<br>Tensor<[1, 384, 35, 35]> other = ?      | Done     | Unknown    | N/A                | N/A    |
| 316 | Tensor<[1, 384, 8, 8]> self = ?,<br>Tensor<[1, 384, 8, 8]> other = ?          | Done     | Unknown    | N/A                | N/A    |
| 317 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 318 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 319 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 320 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 321 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?                | Unknown  | Done       | 0.9999976918151583 | 0      |
| 322 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?                   | Unknown  | Done       | 0.9999980677501572 | 0      |
| 323 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ?        | Done     | Done       | 0.9999979473078302 | 0      |
| 324 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?        | Done     | Done       | 0.9999979986896972 | 0      |
| 325 | Tensor<[1, 40, 30, 30]> self = ?,<br>Tensor<[1, 40, 30, 30]> other = ?        | Done     | Done       | 0.9999980164501419 | 0      |
| 326 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?        | Done     | Done       | 0.9999979661222113 | 0      |
| 327 | Tensor<[1, 40, 56, 56]> self = ?,<br>Tensor<[1, 40, 56, 56]> other = ?        | Done     | Done       | 0.9999979930444073 | 0      |
| 328 | Tensor<[1, 400, 7, 7]> self = ?,<br>Tensor<[1, 400, 7, 7]> other = ?          | Done     | Done       | 0.9999979222841566 | 0      |
| 329 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ?      | Done     | Done       | 0.999998023019366  | 0      |
| 330 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999979638334392 | 0      |
| 331 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?          | Unknown  | Done       | 0.9999979738349024 | 0      |
| 332 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?            | Done     | Done       | 0.9999979865294757 | 0      |
| 333 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ?      | Done     | Done       | 0.9999979669054756 | 0      |
| 334 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?          | Done     | Done       | 0.9999980297820257 | 0      |
| 335 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?      | Done     | Done       | 0.9999979895288466 | 0      |
| 336 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999948607180017 | 0      |
| 337 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | 0.9999979863940525 | 0      |
| 338 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | 0.9999980307696114 | 0      |
| 339 | Tensor<[1, 46, 28, 28]> self = ?,<br>Tensor<[1, 46, 28, 28]> other = ?        | Done     | Done       | 0.999998006226913  | 0      |
| 340 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ?        | Done     | Done       | 0.9999981143583648 | 0      |
| 341 | Tensor<[1, 48, 33, 33]> self = ?,<br>Tensor<[1, 48, 33, 33]> other = ?        | Done     | Done       | 0.9999979927281152 | 0      |
| 342 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?        | Done     | Done       | 0.9999980131363235 | 0      |
| 343 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?        | Done     | Done       | 0.9999979668519394 | 0      |
| 344 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?      | Done     | Done       | 0.9999979564289825 | 0      |
| 345 | Tensor<[1, 480, 7, 7]> self = ?,<br>Tensor<[1, 480, 7, 7]> other = ?          | Done     | Done       | 0.9999979629410697 | 0      |
| 346 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?          | Done     | Done       | 0.9999980015633507 | 0      |
| 347 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?              | Unknown  | Done       | 0.9999981313468304 | 0      |
| 348 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?          | Unknown  | Done       | 0.9999980329844506 | 0      |
| 349 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999947140560701 | 0      |
| 350 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?              | Unknown  | Done       | 0.9999980291213235 | 0      |
| 351 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?            | Done     | Done       | 0.9999980057043264 | 0      |
| 352 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?            | Unknown  | Done       | 0.9999979664306944 | 0      |
| 353 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?              | Done     | Done       | 0.9999980022640509 | 0      |
| 354 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                | 0      |
| 355 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                | 0      |
| 356 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | Done       | 0.9999979746771426 | 0      |
| 357 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ?  | Done     | Done       | 0.9999979902594927 | 0      |
| 358 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ?      | Done     | Done       | 0.9999979772174684 | 0      |
| 359 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979976021609 | 0      |
| 360 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979877211981 | 0      |
| 361 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?      | Done     | Done       | 0.9999980110563087 | 0      |
| 362 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?      | Done     | Done       | 0.9999979954568476 | 0      |
| 363 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.999997987716671  | 0      |
| 364 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979600993052 | 0      |
| 365 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?          | Done     | Done       | 0.9999979713363392 | 0      |
| 366 | Tensor<[1, 512, 8, 8]> self = ?,<br>Tensor<[1, 512, 8, 8]> other = ?          | Done     | Done       | 0.9999980057158192 | 0      |
| 367 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999979930214565 | 0      |
| 368 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?    | Done     | Done       | 0.9999979936929646 | 0      |
| 369 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                      | Unknown  | Done       | 0.9999978497949588 | 0      |
| 370 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?      | Done     | Done       | 0.9999979893615794 | 0      |
| 371 | Tensor<[1, 56, 14, 14]> self = ?,<br>Tensor<[1, 56, 14, 14]> other = ?        | Done     | Done       | 0.9999980020759631 | 0      |
| 372 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?        | Done     | Done       | 0.9999979787453525 | 0      |
| 373 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?      | Done     | Done       | 0.9999979813691504 | 0      |
| 374 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?        | Done     | Done       | 0.9999979932263184 | 0      |
| 375 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?      | Done     | Done       | 0.9999980020327185 | 0      |
| 376 | Tensor<[1, 58, 28, 28]> self = ?,<br>Tensor<[1, 58, 28, 28]> other = ?        | Done     | Done       | 0.9999980184462944 | 0      |
| 377 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Unknown  | Done       | 0.9999980127665965 | 0      |
| 378 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Unknown  | Done       | 0.9999854827640448 | 0      |
| 379 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?            | Unknown  | Done       | 0.9999971459988932 | 0      |
| 380 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?            | Unknown  | Done       | 0.9999988569878229 | 0      |
| 381 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | Done       | 0.9999985317255073 | 0      |
| 382 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?            | Unknown  | Done       | 0.9999965995370714 | 0      |
| 383 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999868878341666 | 0      |
| 384 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?              | Unknown  | Done       | 0.9999987337652044 | 0      |
| 385 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999895559993616 | 0      |
| 386 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 387 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 388 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 389 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?           | Unknown  | Done       | 0.9999981091287121 | 0      |
| 390 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?          | Unknown  | Done       | 0.9999982930119845 | 0      |
| 391 | Tensor<[1, 60, 28, 28]> self = ?,<br>Tensor<[1, 60, 28, 28]> other = ?        | Done     | Done       | 0.9999980254278187 | 0      |
| 392 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                         | Done     | Done       | 1.0                | 0      |
| 393 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                       | Done     | Done       | 1.0                | 0      |
| 394 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?    | Done     | Done       | 0.9999979942160098 | 0      |
| 395 | Tensor<[1, 64, 128, 128]> self = ?,<br>Tensor<[1, 64, 128, 128]> other = ?    | Done     | Done       | 0.99999798342445   | 0      |
| 396 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ?        | Done     | Done       | 0.9999979732801174 | 0      |
| 397 | Tensor<[1, 64, 147, 147]> self = ?,<br>Tensor<[1, 64, 147, 147]> other = ?    | Done     | Unknown    | N/A                | N/A    |
| 398 | Tensor<[1, 64, 150, 150]> self = ?,<br>Tensor<[1, 64, 150, 150]> other = ?    | Done     | Done       | 0.9999979860394317 | 0      |
| 399 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999979714697949 | 0      |
| 400 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999981010153753 | 0      |
| 401 | Tensor<[1, 64, 224, 224]> self = ?,<br>Tensor<[1, 64, 224, 224]> other = ?    | Done     | Done       | 0.999997989310615  | 0      |
| 402 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?    | Done     | Done       | 0.9999979919987404 | 0      |
| 403 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?    | Done     | Done       | 0.9999979878750641 | 0      |
| 404 | Tensor<[1, 64, 28, 28]> self = ?,<br>Tensor<[1, 64, 28, 28]> other = ?        | Done     | Done       | 0.999997950375315  | 0      |
| 405 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 406 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 407 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?        | Done     | Done       | 0.9999980050156315 | 0      |
| 408 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999980993897162 | 0      |
| 409 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 410 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 411 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999980066951818 | 0      |
| 412 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?    | Done     | Done       | 0.9999979930709069 | 0      |
| 413 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?        | Done     | Done       | 0.9999979913914049 | 0      |
| 414 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?        | Done     | Done       | 0.9999980012919141 | 0      |
| 415 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?      | Done     | Done       | 0.9999979833684476 | 0      |
| 416 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?        | Done     | Done       | 0.9999979626510537 | 0      |
| 417 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?        | Done     | Done       | 0.9999979876441503 | 0      |
| 418 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999976419336706 | 0      |
| 419 | Tensor<[1, 640, 7, 7]> self = ?,<br>Tensor<[1, 640, 7, 7]> other = ?          | Done     | Done       | 0.999997984390958  | 0      |
| 420 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 421 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, s0, s1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 422 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 423 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 424 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?      | Done     | Done       | 0.9999980164818068 | 0      |
| 425 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?      | Done     | Done       | 0.999997985412199  | 0      |
| 426 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?          | Done     | Done       | 0.9999980841726944 | 0      |
| 427 | Tensor<[1, 68, 14, 14]> self = ?,<br>Tensor<[1, 68, 14, 14]> other = ?        | Done     | Done       | 0.9999980219134328 | 0      |
| 428 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?      | Done     | Done       | 0.9999979945734846 | 0      |
| 429 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947523226449 | 0      |
| 430 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?              | Done     | Done       | 0.9999979394074263 | 0      |
| 431 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?        | Done     | Done       | 0.9999979515112943 | 0      |
| 432 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?          | Done     | Done       | 0.999997973426286  | 0      |
| 433 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?                | Done     | Done       | 0.9999981357921925 | 0      |
| 434 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?        | Done     | Done       | 0.9999979954100796 | 0      |
| 435 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?        | Done     | Done       | 0.9999980049360925 | 0      |
| 436 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?        | Done     | Done       | 0.9999979923773145 | 0      |
| 437 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ?      | Done     | Done       | 0.9999980086456508 | 0      |
| 438 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?      | Done     | Done       | 0.9999979781664522 | 0      |
| 439 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?      | Done     | Done       | 0.999997992714481  | 0      |
| 440 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?    | Done     | Done       | 0.9999979808573953 | 0      |
| 441 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?      | Done     | Done       | 0.9999980022908637 | 0      |
| 442 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                    | Done     | Done       | 0.9999979633011613 | 0      |
| 443 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?          | Done     | Done       | 0.999998026235554  | 0      |
| 444 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                      | Unknown  | Done       | 0.9999978444600015 | 0      |
| 445 | Tensor<[1, 78, 28, 28]> self = ?,<br>Tensor<[1, 78, 28, 28]> other = ?        | Done     | Done       | 0.9999980267415488 | 0      |
| 446 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?          | Done     | Done       | 0.9999980205535005 | 0      |
| 447 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?            | Unknown  | Done       | 0.9999972810188745 | 0      |
| 448 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?            | Unknown  | Done       | 0.9999981828544188 | 0      |
| 449 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 450 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?              | Unknown  | Done       | 0.9999987240540028 | 0      |
| 451 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 452 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 453 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 454 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 455 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.999997313314201  | 0      |
| 456 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?          | Unknown  | Done       | 0.999998362606243  | 0      |
| 457 | Tensor<[1, 8, 112, 112]> self = ?,<br>Tensor<[1, 8, 112, 112]> other = ?      | Done     | Done       | 0.9999979688249975 | 0      |
| 458 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ?      | Done     | Done       | 0.9999979916188297 | 0      |
| 459 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?                | Done     | Done       | 0.999997976350346  | 0      |
| 460 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?        | Done     | Done       | 0.9999978839452703 | 0      |
| 461 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?          | Done     | Done       | 0.9999980011777341 | 0      |
| 462 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?        | Done     | Done       | 0.9999980034788204 | 0      |
| 463 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?        | Done     | Done       | 0.9999979489338794 | 0      |
| 464 | Tensor<[1, 80, 15, 15]> self = ?,<br>Tensor<[1, 80, 15, 15]> other = ?        | Done     | Done       | 0.9999979057932723 | 0      |
| 465 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?        | Done     | Done       | 0.9999980260517434 | 0      |
| 466 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?        | Done     | Done       | 0.9999979858808219 | 0      |
| 467 | Tensor<[1, 80, 7, 7]> self = ?,<br>Tensor<[1, 80, 7, 7]> other = ?            | Done     | Done       | 0.9999979874846434 | 0      |
| 468 | Tensor<[1, 88, 17, 17]> self = ?,<br>Tensor<[1, 88, 17, 17]> other = ?        | Done     | Done       | 0.9999979635321047 | 0      |
| 469 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?          | Done     | Done       | 0.9999979659365528 | 0      |
| 470 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?      | Done     | Done       | 0.999998028402083  | 0      |
| 471 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?              | Done     | Done       | 0.9999979944602567 | 0      |
| 472 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                           | Done     | Done       | 0.9999946889573095 | 0      |
| 473 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                | Done     | Done       | 0.9999984916154796 | 0      |
| 474 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947909348474 | 0      |
| 475 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?            | Done     | Done       | 0.9999980024557165 | 0      |
| 476 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?              | Done     | Done       | 0.9999978391992734 | 0      |
| 477 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999948586992649 | 0      |
| 478 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?              | Done     | Done       | 0.9999979682471202 | 0      |
| 479 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.999994853015573  | 0      |
| 480 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?              | Done     | Done       | 0.9999979415672231 | 0      |
| 481 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?                | Done     | Done       | 0.9999981344404496 | 0      |
| 482 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999948091641688 | 0      |
| 483 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?              | Done     | Done       | 0.9999980043153273 | 0      |
| 484 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?          | Done     | Done       | 0.9999980286886129 | 0      |
| 485 | Tensor<[1, 92, 14, 14]> self = ?,<br>Tensor<[1, 92, 14, 14]> other = ?        | Done     | Done       | 0.9999979821231993 | 0      |
| 486 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?        | Done     | Done       | 0.9999980457396314 | 0      |
| 487 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?        | Done     | Done       | 0.999998086338656  | 0      |
| 488 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?        | Done     | Done       | 0.9999980010686119 | 0      |
| 489 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?            | Done     | Done       | 0.9999982413837172 | 0      |
| 490 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?          | Done     | Done       | 0.9999979616416674 | 0      |
| 491 | Tensor<[1, 98, 28, 28]> self = ?,<br>Tensor<[1, 98, 28, 28]> other = ?        | Done     | Done       | 0.9999980303099802 | 0      |
| 492 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor<[1, s0*s1, 1280]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 493 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor<[1, s0*s1, 640]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 494 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 495 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor<[1, s1*s2, 320]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 496 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor<[1, s1*s2, 640]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 497 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 498 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.9999031135758222 | 0      |
| 499 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                      | Unknown  | Done       | 0.9999985836533718 | 0      |
| 500 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?            | Done     | Done       | 0.9999979877255321 | 0      |
| 501 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?              | Done     | Done       | 0.999998072172213  | 0      |
| 502 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Done     | Done       | 0.9999978249374742 | 0      |
| 503 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 504 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.999835603514961  | 0      |
| 505 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                      | Unknown  | Done       | 0.9999990377042735 | 0      |
| 506 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?         | Done     | Done       | 0.9999980023814445 | 0      |
| 507 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?         | Done     | Done       | 0.9999979791907659 | 0      |
| 508 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?         | Done     | Done       | 0.9999979783719012 | 0      |
| 509 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?         | Done     | Done       | 0.9999979757077951 | 0      |
| 510 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 511 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 0.9995606688735804 | 0      |
| 512 | Tensor<[2*s0]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 513 | Tensor<[2*s1]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 514 | Tensor<[2*s2]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 515 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                | 0      |
| 516 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 517 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                      | Unknown  | Done       | 0.9999981007597407 | 0      |
| 518 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?              | Unknown  | Done       | 0.9999979218944015 | 0      |
| 519 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?                | Done     | Done       | 0.9999980114701991 | 0      |
| 520 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?                | Done     | Done       | 0.9999979439648354 | 0      |
| 521 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?              | Done     | Done       | 0.9999981552438044 | 0      |
| 522 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                      | Done     | Done       | 0.9999979847306057 | 0      |
| 523 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.9999981477596095 | 0      |
| 524 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                              | Done     | Done       | 0.9777240880369812 | 0      |
| 525 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                    | Done     | Done       | 0.9999981165740073 | 0      |
| 526 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Done     | Done       | 0.9999977098085315 | 0      |
| 527 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?        | Done     | Done       | 0.9999980377323368 | 0      |
| 528 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?        | Done     | Done       | 0.9999979922183897 | 0      |
| 529 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?        | Done     | Done       | 0.9999980150184902 | 0      |
| 530 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?        | Done     | Done       | 0.9999980066152141 | 0      |
| 531 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Unknown  | Done       | 0.9999979920084229 | 0      |
| 532 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                   | Done     | Done       | 0.99999794775035   | 0      |
| 533 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?         | Done     | Done       | 0.9999979720237935 | 0      |
| 534 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?         | Done     | Done       | 0.9999979984318594 | 0      |
| 535 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?         | Done     | Done       | 0.9999979964916537 | 0      |
| 536 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?         | Done     | Done       | 0.999997999376577  | 0      |
| 537 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.9999980575207456 | 0      |
| 538 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                    | Done     | Done       | 0.999998023853239  | 0      |
| 539 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.2881005439171842 | 0      |
| 540 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?            | Done     | Done       | 0.9999979946697435 | 0      |
| 541 | Tensor<[]> self = ?,<br>Tensor other = 1                                      | None     | Fallback   | 1.0                | -1     |
| 542 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                        | Unknown  | Unknown    | N/A                | N/A    |
| 543 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |

