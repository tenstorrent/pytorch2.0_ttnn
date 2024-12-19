### aten.add.Tensor
|     | ATen Input Variations                                                         | Status   | Isolated   | PCC                 | Host   |
|----:|:------------------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                          | Unknown  | Done       | 1.0                 | 0      |
|   1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                                | Unknown  | Done       | 1.0                 | 0      |
|   2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999742745701751  | 0      |
|   3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                         | Removed  | Done       | 0.999997680157874   | 0      |
|   4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999971327467381  | 0      |
|   5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.99999142500258    | 0      |
|   6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999933043001605  | 0      |
|   7 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999945078545313  | 0      |
|   8 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999979483755521  | 0      |
|   9 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?          | Unknown  | Done       | 0.9999982890471871  | 0      |
|  10 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839              | Done     | Done       | 1.0                 | 0      |
|  11 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9043478220701218              | Done     | Done       | 1.0                 | 0      |
|  12 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9086956530809402              | Done     | Done       | 1.0                 | 0      |
|  13 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9090909063816071              | Done     | Done       | 1.0                 | 0      |
|  14 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9130434766411781              | Done     | Done       | 1.0                 | 0      |
|  15 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032              | Done     | Done       | 1.0                 | 0      |
|  16 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.917391300201416               | Done     | Done       | 1.0                 | 0      |
|  17 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9181818142533302              | Done     | Done       | 1.0                 | 0      |
|  18 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9217391312122345              | Done     | Done       | 1.0                 | 0      |
|  19 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9260869547724724              | Done     | Done       | 1.0                 | 0      |
|  20 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9272727221250534              | Done     | Done       | 1.0                 | 0      |
|  21 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226              | Done     | Done       | 1.0                 | 0      |
|  22 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9304347857832909              | Done     | Done       | 1.0                 | 0      |
|  23 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9347826093435287              | Done     | Done       | 1.0                 | 0      |
|  24 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9363636374473572              | Done     | Done       | 1.0                 | 0      |
|  25 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9391304366290569              | Done     | Done       | 1.0                 | 0      |
|  26 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323              | Done     | Done       | 1.0                 | 0      |
|  27 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9434782639145851              | Done     | Done       | 1.0                 | 0      |
|  28 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.94545454159379                | Done     | Done       | 1.0                 | 0      |
|  29 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.947826087474823               | Done     | Done       | 1.0                 | 0      |
|  30 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9521739110350609              | Done     | Done       | 1.0                 | 0      |
|  31 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9545454569160938              | Done     | Done       | 1.0                 | 0      |
|  32 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9565217345952988              | Done     | Done       | 1.0                 | 0      |
|  33 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516              | Done     | Done       | 1.0                 | 0      |
|  34 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.960869561880827               | Done     | Done       | 1.0                 | 0      |
|  35 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.963636364787817               | Done     | Done       | 1.0                 | 0      |
|  36 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9652173891663551              | Done     | Done       | 1.0                 | 0      |
|  37 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9695652164518833              | Done     | Done       | 1.0                 | 0      |
|  38 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161              | Done     | Done       | 1.0                 | 0      |
|  39 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9727272726595402              | Done     | Done       | 1.0                 | 0      |
|  40 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9739130418747663              | Done     | Done       | 1.0                 | 0      |
|  41 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9782608672976494              | Done     | Done       | 1.0                 | 0      |
|  42 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9818181823939085              | Done     | Done       | 1.0                 | 0      |
|  43 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9826086945831776              | Done     | Done       | 1.0                 | 0      |
|  44 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581              | Done     | Done       | 1.0                 | 0      |
|  45 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9869565209373832              | Done     | Done       | 1.0                 | 0      |
|  46 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9909090911969543              | Done     | Done       | 1.0                 | 0      |
|  47 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9913043472915888              | Done     | Done       | 1.0                 | 0      |
|  48 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9956521736457944              | Done     | Done       | 1.0                 | 0      |
|  49 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                           | Unknown  | Done       | 1.0                 | 0      |
|  50 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027    | Done     | Done       | 0.9999999962281633  | 0      |
|  51 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997     | Done     | Done       | 0.9999990259946119  | 0      |
|  52 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994     | Done     | Done       | 0.9999998586988053  | 0      |
|  53 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999950213163262  | 0      |
|  54 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | 0.9999981089769171  | 0      |
|  55 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999841189992104  | 0      |
|  56 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                         | Removed  | Done       | 0.9999965677514877  | 0      |
|  57 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999969122468443  | 0      |
|  58 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999949330808247  | 0      |
|  59 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999950219207511  | 0      |
|  60 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999946651703949  | 0      |
|  61 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?              | Unknown  | Done       | 0.9999979772425144  | 0      |
|  62 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                 | 0      |
|  63 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                | Unknown  | Done       | 0.9999979517245148  | 0      |
|  64 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Unknown  | Done       | 0.9999981091399921  | 0      |
|  65 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                   | Unknown  | Done       | 0.9999981241935065  | 0      |
|  66 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?            | Unknown  | Done       | 0.9999981336034405  | 0      |
|  67 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                 | 0      |
|  68 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?              | Unknown  | Done       | 0.9999980083282572  | 0      |
|  69 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?              | Done     | Done       | 0.9999979287961775  | 0      |
|  70 | Tensor<[1, 100, 14, 14]> self = ?,<br>Tensor<[1, 100, 14, 14]> other = ?      | Done     | Done       | 0.9999979433156924  | 0      |
|  71 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?        | Done     | Done       | 0.9999979839248446  | 0      |
|  72 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Unknown  | Done       | 1.0                 | 0      |
|  73 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Done     | Done       | 1.0                 | 0      |
|  74 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ?    | Done     | Done       | 0.9999979424812522  | 0      |
|  75 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ?    | Done     | Done       | 0.9999979849894184  | 0      |
|  76 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?    | Done     | Done       | 0.9999979947038757  | 0      |
|  77 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?          | Done     | Done       | 0.9999980147156349  | 0      |
|  78 | Tensor<[1, 1024, 17, 17]> self = ?,<br>Tensor<[1, 1024, 17, 17]> other = ?    | Done     | Done       | 0.999998017773145   | 0      |
|  79 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999980284032748  | 0      |
|  80 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.999997981623318   | 0      |
|  81 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?    | Done     | Done       | 0.9999979997796519  | 0      |
|  82 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Unknown  | Done       | 0.9999980153969688  | 0      |
|  83 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?    | Unknown  | Done       | 0.9999979943137977  | 0      |
|  84 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?        | Done     | Done       | 0.9999979670282654  | 0      |
|  85 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999980393590372  | 0      |
|  86 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?      | Done     | Done       | 0.9999980327132697  | 0      |
|  87 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?    | Done     | Done       | 0.9999979949453519  | 0      |
|  88 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                                 | Done     | Done       | 1.0                 | 0      |
|  89 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | 0.9999972447059502  | 0      |
|  90 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?      | Done     | Done       | 0.9999979763125632  | 0      |
|  91 | Tensor<[1, 112, 15, 15]> self = ?,<br>Tensor<[1, 112, 15, 15]> other = ?      | Done     | Done       | 0.9999979719745542  | 0      |
|  92 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?      | Unknown  | Done       | 0.9999979489498029  | 0      |
|  93 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ?      | Unknown  | Done       | 0.9999979601267324  | 0      |
|  94 | Tensor<[1, 116, 14, 14]> self = ?,<br>Tensor<[1, 116, 14, 14]> other = ?      | Done     | Done       | 0.9999979866977656  | 0      |
|  95 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999987485533297  | 0      |
|  96 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?          | Unknown  | Done       | 0.9999969392274477  | 0      |
|  97 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999897394486489  | 0      |
|  98 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?            | Unknown  | Done       | 0.9999986947473336  | 0      |
|  99 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999971806573986  | 0      |
| 100 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?            | Unknown  | Done       | 0.9999976225131197  | 0      |
| 101 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | 0.9999980506588315  | 0      |
| 102 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                 | N/A    |
| 103 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                 | N/A    |
| 104 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                 | N/A    |
| 105 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Done     | Done       | 0.9999975057450685  | 0      |
| 106 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?        | Unknown  | Done       | 0.9999976661239999  | 0      |
| 107 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ?          | Done     | Done       | 0.9999982498189246  | 0      |
| 108 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?              | Done     | Done       | 0.9999976827107772  | 0      |
| 109 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<[1, 1, 1, 14]> other = ?          | Done     | Done       | 0.9999982266476777  | 0      |
| 110 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ?    | Done     | Done       | 0.9999979965564514  | 0      |
| 111 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?         | Done     | Done       | 0.9999980328377899  | 0      |
| 112 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ?          | Done     | Done       | 0.9999979872731595  | 0      |
| 113 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947053310628  | 0      |
| 114 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?            | Done     | Done       | 0.9999979702262163  | 0      |
| 115 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | 0.9999979794104071  | 0      |
| 116 | Tensor<[1, 12, 56, 56]> self = ?,<br>Tensor<[1, 12, 56, 56]> other = ?        | Done     | Done       | 0.9999980618529349  | 0      |
| 117 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ?             | Done     | Done       | 0.9999970337494425  | 0      |
| 118 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?              | Done     | Done       | 0.9999980363356091  | 0      |
| 119 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999976583350192  | 0      |
| 120 | Tensor<[1, 120, 17, 17]> self = ?,<br>Tensor<[1, 120, 17, 17]> other = ?      | Done     | Done       | 0.9999980541703645  | 0      |
| 121 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?      | Done     | Done       | 0.9999979537710747  | 0      |
| 122 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?          | Done     | Done       | 0.999998005307567   | 0      |
| 123 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?    | Done     | Done       | 0.999997971815829   | 0      |
| 124 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Unknown  | Done       | 1.0                 | 0      |
| 125 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                 | 0      |
| 126 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Unknown  | Done       | 0.9999979425555441  | 0      |
| 127 | Tensor<[1, 128, 112, 112]> self = ?,<br>Tensor<[1, 128, 112, 112]> other = ?  | Done     | Done       | 0.9999979935450006  | 0      |
| 128 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ?  | Done     | Done       | 0.9999979952235464  | 0      |
| 129 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999980530402939  | 0      |
| 130 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Unknown  | Done       | 0.9999979812442207  | 0      |
| 131 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ?      | Done     | Done       | 0.9999980564025743  | 0      |
| 132 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ?      | Done     | Done       | 0.9999980002424452  | 0      |
| 133 | Tensor<[1, 128, 64, 64]> self = ?,<br>Tensor<[1, 128, 64, 64]> other = ?      | Done     | Done       | 0.9999979796138203  | 0      |
| 134 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?      | Done     | Done       | 0.9999980022255881  | 0      |
| 135 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999980074378428  | 0      |
| 136 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979967991267  | 0      |
| 137 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?        | Unknown  | Done       | 0.9999980402659504  | 0      |
| 138 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 139 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, s0, s1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 140 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 141 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, s1, s2]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 142 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ?    | Done     | Done       | 0.9999980055628032  | 0      |
| 143 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ?      | Done     | Done       | 0.9999980459365754  | 0      |
| 144 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?        | Done     | Done       | 0.9999980099496235  | 0      |
| 145 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?    | Done     | Done       | 0.9999979669298842  | 0      |
| 146 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?              | Done     | Done       | 0.9999977209860252  | 0      |
| 147 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?      | Done     | Done       | 0.9999979739989299  | 0      |
| 148 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?      | Done     | Done       | 0.9999979649992241  | 0      |
| 149 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947107275657  | 0      |
| 150 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?            | Done     | Done       | 0.9999979896931674  | 0      |
| 151 | Tensor<[1, 14, 56, 56]> self = ?,<br>Tensor<[1, 14, 56, 56]> other = ?        | Done     | Done       | 0.9999979811067083  | 0      |
| 152 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?              | Done     | Done       | 0.9999980223214435  | 0      |
| 153 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?      | Done     | Done       | 0.9999980090397308  | 0      |
| 154 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?          | Done     | Done       | 0.9999980709223664  | 0      |
| 155 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?          | Done     | Done       | 0.9999980054830245  | 0      |
| 156 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999948746022616  | 0      |
| 157 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Unknown  | Done       | 0.999998006795814   | 0      |
| 158 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                 | 0      |
| 159 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?              | Unknown  | Done       | 0.9999980348388698  | 0      |
| 160 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ?          | Unknown  | Done       | 0.9999979878895525  | 0      |
| 161 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?             | Unknown  | Done       | 0.9999979859658473  | 0      |
| 162 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?        | Done     | Done       | 0.9999979608937742  | 0      |
| 163 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Tensor<[1, 1536, 8, 8]> other = ?        | Done     | Done       | 0.9999979387412062  | 0      |
| 164 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999979631182355  | 0      |
| 165 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?          | Unknown  | Done       | 0.9999980967652198  | 0      |
| 166 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999992388853446  | 0      |
| 167 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?            | Unknown  | Done       | 0.9999993236535982  | 0      |
| 168 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999968172281823  | 0      |
| 169 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?            | Unknown  | Done       | 0.9999973730959666  | 0      |
| 170 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999983437011741  | 0      |
| 171 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Done       | 0.9999974110798198  | 0      |
| 172 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                 | N/A    |
| 173 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                 | N/A    |
| 174 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                 | N/A    |
| 175 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.9999975999884292  | 0      |
| 176 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?        | Unknown  | Done       | 0.9999978119622887  | 0      |
| 177 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ?    | Done     | Done       | 0.9999979984137654  | 0      |
| 178 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?      | Done     | Done       | 0.9999979647825293  | 0      |
| 179 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?      | Done     | Done       | 0.9999980087446386  | 0      |
| 180 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ?    | Unknown  | Done       | 0.9999979842317647  | 0      |
| 181 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> other = ?         | Done     | Done       | 0.9999982480380263  | 0      |
| 182 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ?    | Done     | Done       | 0.9999979840496563  | 0      |
| 183 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor<[1, 1, 1, 256]> other = ?       | Done     | Done       | 0.99999799660985    | 0      |
| 184 | Tensor<[1, 16, 28, 28]> self = ?,<br>Tensor<[1, 16, 28, 28]> other = ?        | Done     | Done       | 0.9999979840245792  | 0      |
| 185 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Done       | 0.9999979745785598  | 0      |
| 186 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Unknown  | Done       | 0.9999979744630485  | 0      |
| 187 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 188 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 189 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?              | Done     | Done       | 0.9999979305256745  | 0      |
| 190 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 191 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 192 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999979327072693  | 0      |
| 193 | Tensor<[1, 160, 14, 14]> self = ?,<br>Tensor<[1, 160, 14, 14]> other = ?      | Done     | Done       | 0.9999980427062988  | 0      |
| 194 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ?      | Unknown  | Done       | 0.999997995690381   | 0      |
| 195 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ?      | Done     | Done       | 0.9999980120240352  | 0      |
| 196 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?      | Done     | Done       | 0.9999979750587155  | 0      |
| 197 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?          | Done     | Done       | 0.999998013835442   | 0      |
| 198 | Tensor<[1, 160, 73, 73]> self = ?,<br>Tensor<[1, 160, 73, 73]> other = ?      | Done     | Done       | 0.9999979987609056  | 0      |
| 199 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999978891299917  | 0      |
| 200 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?          | Done     | Done       | 0.9999979964112997  | 0      |
| 201 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ?      | Done     | Done       | 0.9999980122974091  | 0      |
| 202 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?        | Done     | Done       | 0.9999979570631121  | 0      |
| 203 | Tensor<[1, 185, 28, 28]> self = ?,<br>Tensor<[1, 185, 28, 28]> other = ?      | Done     | Done       | 0.9999979654149049  | 0      |
| 204 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ?            | Done     | Done       | 0.9999980157188518  | 0      |
| 205 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ?      | Done     | Done       | 0.9999980311071931  | 0      |
| 206 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ?      | Done     | Done       | 0.999998008323426   | 0      |
| 207 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?      | Done     | Done       | 0.9999979862653583  | 0      |
| 208 | Tensor<[1, 192, 7, 7]> self = ?,<br>Tensor<[1, 192, 7, 7]> other = ?          | Done     | Done       | 0.9999980087266465  | 0      |
| 209 | Tensor<[1, 192, 71, 71]> self = ?,<br>Tensor<[1, 192, 71, 71]> other = ?      | Done     | Done       | 0.9999979976388017  | 0      |
| 210 | Tensor<[1, 192, 8, 8]> self = ?,<br>Tensor<[1, 192, 8, 8]> other = ?          | Done     | Done       | 0.9999980751643454  | 0      |
| 211 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?        | Done     | Done       | 0.999997987661702   | 0      |
| 212 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?          | Done     | Done       | 0.9999979911297834  | 0      |
| 213 | Tensor<[1, 196, 14, 14]> self = ?,<br>Tensor<[1, 196, 14, 14]> other = ?      | Done     | Done       | 0.9999980074805941  | 0      |
| 214 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ?            | Done     | Done       | 0.9999980066467153  | 0      |
| 215 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?          | Done     | Done       | 0.9999979852624465  | 0      |
| 216 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?            | Done     | Done       | 0.9999980314639956  | 0      |
| 217 | Tensor<[1, 19]> self = ?,<br>Tensor other = 2                                 | Removed  | Done       | 0.9999727105426975  | 0      |
| 218 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                 | 0      |
| 219 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                 | 0      |
| 220 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Done       | 1.0                 | 0      |
| 221 | Tensor<[1, 20, 28, 28]> self = ?,<br>Tensor<[1, 20, 28, 28]> other = ?        | Done     | Done       | 0.9999979126022032  | 0      |
| 222 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?        | Done     | Done       | 0.9999980314968463  | 0      |
| 223 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Unknown  | Done       | 1.0                 | 0      |
| 224 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Done     | Done       | 1.0                 | 0      |
| 225 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999980159167453  | 0      |
| 226 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?    | Done     | Done       | 0.9999979861756085  | 0      |
| 227 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Unknown  | Done       | 0.9999979860754001  | 0      |
| 228 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?    | Unknown  | Done       | 0.999997999197622   | 0      |
| 229 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?        | Done     | Done       | 0.9999979758731603  | 0      |
| 230 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?          | Done     | Done       | 0.9999979941163674  | 0      |
| 231 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?             | Done     | Done       | 0.999997988754394   | 0      |
| 232 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?      | Done     | Done       | 0.9999979262225179  | 0      |
| 233 | Tensor<[1, 208, 9, 9]> self = ?,<br>Tensor<[1, 208, 9, 9]> other = ?          | Done     | Done       | 0.9999980692493714  | 0      |
| 234 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?      | Done     | Done       | 0.9999979670883187  | 0      |
| 235 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?      | Done     | Done       | 0.9999979919597024  | 0      |
| 236 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?          | Done     | Done       | 0.9999979324023665  | 0      |
| 237 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                 | 0      |
| 238 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ?      | Done     | Done       | 0.9999979910545779  | 0      |
| 239 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?      | Done     | Done       | 0.9999979816715433  | 0      |
| 240 | Tensor<[1, 24, 112, 112]> self = ?,<br>Tensor<[1, 24, 112, 112]> other = ?    | Done     | Done       | 0.9999979795136547  | 0      |
| 241 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?        | Done     | Done       | 0.9999979642823809  | 0      |
| 242 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?        | Done     | Done       | 0.9999980530759613  | 0      |
| 243 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?        | Done     | Done       | 0.9999979951118549  | 0      |
| 244 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?        | Done     | Done       | 0.9999980144569931  | 0      |
| 245 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?        | Done     | Done       | 0.99999798979052    | 0      |
| 246 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?        | Done     | Done       | 0.9999979845637696  | 0      |
| 247 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?              | Done     | Done       | 0.9999978640363363  | 0      |
| 248 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?        | Unknown  | Done       | 0.9999979978647268  | 0      |
| 249 | Tensor<[1, 240, 14, 14]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?      | Done     | Done       | 0.9999980448268107  | 0      |
| 250 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?      | Done     | Done       | 0.9999979978899645  | 0      |
| 251 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?              | Done     | Done       | 0.9999980247205309  | 0      |
| 252 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?        | Done     | Done       | 0.9999979986311572  | 0      |
| 253 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Unknown  | Done       | 1.0                 | 0      |
| 254 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                 | 0      |
| 255 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Unknown  | Done       | 0.9999980058116108  | 0      |
| 256 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ?  | Unknown  | Done       | 0.9999980029967687  | 0      |
| 257 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?          | Done     | Done       | 0.9999979984116752  | 0      |
| 258 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ?  | Done     | Done       | 0.9999979921291625  | 0      |
| 259 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?          | Done     | Done       | 0.9999980225298573  | 0      |
| 260 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ?      | Done     | Done       | 0.9999980115729673  | 0      |
| 261 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?      | Done     | Done       | 0.999998013764669   | 0      |
| 262 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?            | Done     | Done       | 0.9999980054545754  | 0      |
| 263 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979931308265  | 0      |
| 264 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ?  | Done     | Done       | 0.9999979914177142  | 0      |
| 265 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Unknown  | Done       | 0.9999979729013962  | 0      |
| 266 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ?  | Unknown  | Done       | 0.9999979944645291  | 0      |
| 267 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?            | Done     | Done       | 0.9999979748623634  | 0      |
| 268 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.9999980728396499  | 0      |
| 269 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ?      | Done     | Done       | 0.9999979833269673  | 0      |
| 270 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?      | Done     | Done       | 0.9999979825042415  | 0      |
| 271 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?              | Done     | Done       | 0.9999979593174828  | 0      |
| 272 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?      | Done     | Done       | 0.9999979882540672  | 0      |
| 273 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999980271877497  | 0      |
| 274 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979403788269  | 0      |
| 275 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?      | Unknown  | Done       | 0.9999979881948484  | 0      |
| 276 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ?            | Done     | Done       | 0.999997978227144   | 0      |
| 277 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?      | Done     | Done       | 0.9999980079832638  | 0      |
| 278 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?      | Done     | Done       | 0.9999980002146701  | 0      |
| 279 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?              | Done     | Done       | 0.9999979662842823  | 0      |
| 280 | Tensor<[1, 256, 7, 7]> self = ?,<br>Tensor<[1, 256, 7, 7]> other = ?          | Done     | Done       | 0.9999979380577405  | 0      |
| 281 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?      | Done     | Done       | 0.9999979880517259  | 0      |
| 282 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999979341672731  | 0      |
| 283 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ?      | Unknown  | Done       | 0.9999980397175275  | 0      |
| 284 | Tensor<[1, 272, 7, 7]> self = ?,<br>Tensor<[1, 272, 7, 7]> other = ?          | Done     | Done       | 0.9999979627341795  | 0      |
| 285 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?      | Done     | Done       | 0.9999980148851016  | 0      |
| 286 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?      | Done     | Done       | 0.9999979804814809  | 0      |
| 287 | Tensor<[1, 28, 28, 28]> self = ?,<br>Tensor<[1, 28, 28, 28]> other = ?        | Done     | Done       | 0.9999979798243487  | 0      |
| 288 | Tensor<[1, 288, 14, 14]> self = ?,<br>Tensor<[1, 288, 14, 14]> other = ?      | Done     | Done       | 0.9999980129585313  | 0      |
| 289 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?    | Done     | Done       | 0.9999979837980061  | 0      |
| 290 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?      | Unknown  | Done       | 0.9999979938755716  | 0      |
| 291 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?      | Unknown  | Done       | 0.9999979996098699  | 0      |
| 292 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?    | Unknown  | Done       | 0.9999979895703298  | 0      |
| 293 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?            | Done     | Done       | 0.9999979897990645  | 0      |
| 294 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?        | Done     | Done       | 0.9999979694443157  | 0      |
| 295 | Tensor<[1, 32, 112, 112]> self = ?,<br>Tensor<[1, 32, 112, 112]> other = ?    | Done     | Done       | 0.9999979937231539  | 0      |
| 296 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?    | Done     | Done       | 0.9999979881385819  | 0      |
| 297 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?            | Done     | Done       | 0.9999979735956717  | 0      |
| 298 | Tensor<[1, 32, 256, 256]> self = ?,<br>Tensor<[1, 32, 256, 256]> other = ?    | Done     | Done       | 0.9999979949630005  | 0      |
| 299 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ?        | Done     | Done       | 0.9999979941681922  | 0      |
| 300 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?      | Done     | Done       | 0.9999979789459801  | 0      |
| 301 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?      | Done     | Done       | 0.9999979758781579  | 0      |
| 302 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?        | Done     | Done       | 0.9999980126030974  | 0      |
| 303 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?        | Done     | Done       | 0.9999980160714034  | 0      |
| 304 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999947859294283  | 0      |
| 305 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947620030127  | 0      |
| 306 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?        | Done     | Done       | 0.9999980239727743  | 0      |
| 307 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?        | Done     | Done       | 0.9999979833472699  | 0      |
| 308 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?        | Unknown  | Done       | 0.9999979816113793  | 0      |
| 309 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?      | Done     | Done       | 0.9999979967342324  | 0      |
| 310 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979370341803  | 0      |
| 311 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?      | Unknown  | Done       | 0.9999979954224102  | 0      |
| 312 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 313 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 314 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?      | Done     | Done       | 0.9999980060249796  | 0      |
| 315 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?      | Done     | Done       | 0.9999980001716822  | 0      |
| 316 | Tensor<[1, 34, 28, 28]> self = ?,<br>Tensor<[1, 34, 28, 28]> other = ?        | Done     | Done       | 0.9999980051987275  | 0      |
| 317 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?        | Done     | Done       | 0.9999979575676228  | 0      |
| 318 | Tensor<[1, 36, 56, 56]> self = ?,<br>Tensor<[1, 36, 56, 56]> other = ?        | Done     | Done       | 0.9999979904455042  | 0      |
| 319 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?        | Done     | Done       | 0.9999979958542956  | 0      |
| 320 | Tensor<[1, 384, 35, 35]> self = ?,<br>Tensor<[1, 384, 35, 35]> other = ?      | Done     | Done       | 0.9999979825684923  | 0      |
| 321 | Tensor<[1, 384, 8, 8]> self = ?,<br>Tensor<[1, 384, 8, 8]> other = ?          | Done     | Done       | 0.9999979660957182  | 0      |
| 322 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 323 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 324 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 325 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 326 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?                | Unknown  | Done       | 0.9999980150559394  | 0      |
| 327 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?                   | Unknown  | Done       | 0.9999977913364925  | 0      |
| 328 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ?        | Done     | Done       | 0.9999980702622687  | 0      |
| 329 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?        | Done     | Done       | 0.9999979959836907  | 0      |
| 330 | Tensor<[1, 40, 30, 30]> self = ?,<br>Tensor<[1, 40, 30, 30]> other = ?        | Done     | Done       | 0.999997919814988   | 0      |
| 331 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?        | Unknown  | Done       | 0.9999979920539646  | 0      |
| 332 | Tensor<[1, 40, 56, 56]> self = ?,<br>Tensor<[1, 40, 56, 56]> other = ?        | Done     | Done       | 0.9999979881171782  | 0      |
| 333 | Tensor<[1, 400, 7, 7]> self = ?,<br>Tensor<[1, 400, 7, 7]> other = ?          | Done     | Done       | 0.9999979790342577  | 0      |
| 334 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ?      | Done     | Done       | 0.9999980015374738  | 0      |
| 335 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999979505405365  | 0      |
| 336 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?          | Unknown  | Done       | 0.9999979815735344  | 0      |
| 337 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?            | Done     | Done       | 0.9999980153789999  | 0      |
| 338 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ?      | Done     | Done       | 0.9999979560520409  | 0      |
| 339 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?          | Done     | Done       | 0.9999980138070542  | 0      |
| 340 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?      | Done     | Done       | 0.999998007258294   | 0      |
| 341 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.99999486220242    | 0      |
| 342 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | 0.9999979634714647  | 0      |
| 343 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | 0.9999980070124482  | 0      |
| 344 | Tensor<[1, 46, 28, 28]> self = ?,<br>Tensor<[1, 46, 28, 28]> other = ?        | Done     | Done       | 0.9999979984997104  | 0      |
| 345 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ?        | Done     | Done       | 0.9999979778363549  | 0      |
| 346 | Tensor<[1, 48, 33, 33]> self = ?,<br>Tensor<[1, 48, 33, 33]> other = ?        | Done     | Done       | 0.9999979358301219  | 0      |
| 347 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?        | Done     | Done       | 0.9999979992166068  | 0      |
| 348 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?        | Done     | Done       | 0.9999979714799719  | 0      |
| 349 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?      | Done     | Done       | 0.9999980279909071  | 0      |
| 350 | Tensor<[1, 480, 7, 7]> self = ?,<br>Tensor<[1, 480, 7, 7]> other = ?          | Done     | Done       | 0.9999979695623592  | 0      |
| 351 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?          | Done     | Done       | 0.99999797693514    | 0      |
| 352 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?              | Unknown  | Done       | 0.9999980188758638  | 0      |
| 353 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?          | Unknown  | Done       | 0.9999981870073593  | 0      |
| 354 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999945403378752  | 0      |
| 355 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?              | Unknown  | Done       | 0.9999979211409834  | 0      |
| 356 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?            | Done     | Done       | 0.9999980071043806  | 0      |
| 357 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?            | Unknown  | Done       | 0.999997968656341   | 0      |
| 358 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?              | Done     | Done       | 0.9999980199455936  | 0      |
| 359 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Unknown  | Done       | 1.0                 | 0      |
| 360 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                 | 0      |
| 361 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Unknown  | Done       | 0.9999979627174395  | 0      |
| 362 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ?  | Unknown  | Done       | 0.9999979874185452  | 0      |
| 363 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ?      | Done     | Done       | 0.9999979774469843  | 0      |
| 364 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979449052461  | 0      |
| 365 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979682649899  | 0      |
| 366 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?      | Done     | Done       | 0.9999979947638067  | 0      |
| 367 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?      | Done     | Done       | 0.9999979880805091  | 0      |
| 368 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979550069451  | 0      |
| 369 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979921744279  | 0      |
| 370 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?          | Done     | Done       | 0.9999979441651199  | 0      |
| 371 | Tensor<[1, 512, 8, 8]> self = ?,<br>Tensor<[1, 512, 8, 8]> other = ?          | Done     | Done       | 0.9999980062079266  | 0      |
| 372 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999979441992531  | 0      |
| 373 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?    | Done     | Done       | 0.9999979923773727  | 0      |
| 374 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                      | Unknown  | Done       | 0.9999980053687588  | 0      |
| 375 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?      | Done     | Done       | 0.999997993527567   | 0      |
| 376 | Tensor<[1, 56, 14, 14]> self = ?,<br>Tensor<[1, 56, 14, 14]> other = ?        | Done     | Done       | 0.9999979792561904  | 0      |
| 377 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?        | Unknown  | Done       | 0.9999979802246864  | 0      |
| 378 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?      | Done     | Done       | 0.9999979965463338  | 0      |
| 379 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?        | Done     | Done       | 0.9999980066120625  | 0      |
| 380 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?      | Done     | Done       | 0.9999979976768146  | 0      |
| 381 | Tensor<[1, 58, 28, 28]> self = ?,<br>Tensor<[1, 58, 28, 28]> other = ?        | Done     | Done       | 0.9999979316154409  | 0      |
| 382 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Unknown  | Done       | 0.9999979797074529  | 0      |
| 383 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Unknown  | Done       | 0.9999939560153238  | 0      |
| 384 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?            | Unknown  | Done       | 0.9999981396812471  | 0      |
| 385 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?            | Unknown  | Done       | 0.9999963514607277  | 0      |
| 386 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | Done       | 0.9999989496656689  | 0      |
| 387 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?            | Unknown  | Done       | 0.9999984140022421  | 0      |
| 388 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999927074846563  | 0      |
| 389 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?              | Unknown  | Done       | 1.0                 | 0      |
| 390 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.999996398093261   | 0      |
| 391 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?              | Unknown  | Done       | 1.0                 | 0      |
| 392 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 393 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 394 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?           | Unknown  | Done       | 0.9999978635356143  | 0      |
| 395 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?          | Unknown  | Done       | 0.9999977338721302  | 0      |
| 396 | Tensor<[1, 60, 28, 28]> self = ?,<br>Tensor<[1, 60, 28, 28]> other = ?        | Done     | Done       | 0.9999980344874467  | 0      |
| 397 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                         | Unknown  | Done       | 1.0                 | 0      |
| 398 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                       | Done     | Done       | 1.0                 | 0      |
| 399 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?    | Done     | Done       | 0.9999979995134356  | 0      |
| 400 | Tensor<[1, 64, 128, 128]> self = ?,<br>Tensor<[1, 64, 128, 128]> other = ?    | Done     | Done       | 0.9999979967882752  | 0      |
| 401 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ?        | Done     | Done       | 0.9999978569743629  | 0      |
| 402 | Tensor<[1, 64, 147, 147]> self = ?,<br>Tensor<[1, 64, 147, 147]> other = ?    | Done     | Done       | 0.9999979997787998  | 0      |
| 403 | Tensor<[1, 64, 150, 150]> self = ?,<br>Tensor<[1, 64, 150, 150]> other = ?    | Done     | Done       | 0.9999979893406827  | 0      |
| 404 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999979595109743  | 0      |
| 405 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979188328157  | 0      |
| 406 | Tensor<[1, 64, 224, 224]> self = ?,<br>Tensor<[1, 64, 224, 224]> other = ?    | Done     | Done       | 0.9999979972823297  | 0      |
| 407 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?    | Done     | Done       | 0.9999979958970115  | 0      |
| 408 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?    | Done     | Done       | 0.999997995179187   | 0      |
| 409 | Tensor<[1, 64, 28, 28]> self = ?,<br>Tensor<[1, 64, 28, 28]> other = ?        | Done     | Done       | 0.9999979699309606  | 0      |
| 410 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 411 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 412 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?        | Done     | Done       | 0.9999979969771694  | 0      |
| 413 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999979280512695  | 0      |
| 414 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 415 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 416 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979373933947  | 0      |
| 417 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?    | Done     | Done       | 0.9999979951563721  | 0      |
| 418 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?        | Done     | Done       | 0.9999980024233623  | 0      |
| 419 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?        | Done     | Done       | 0.9999979833899176  | 0      |
| 420 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?      | Done     | Done       | 0.9999979939736529  | 0      |
| 421 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?        | Done     | Done       | 0.9999980005458761  | 0      |
| 422 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?        | Done     | Done       | 0.9999979722032137  | 0      |
| 423 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999981897480229  | 0      |
| 424 | Tensor<[1, 640, 7, 7]> self = ?,<br>Tensor<[1, 640, 7, 7]> other = ?          | Done     | Done       | 0.9999979442816762  | 0      |
| 425 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 426 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, s0, s1]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 427 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 428 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 429 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?      | Done     | Done       | 0.9999980472563476  | 0      |
| 430 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?      | Done     | Done       | 0.9999979823442973  | 0      |
| 431 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?          | Done     | Done       | 0.9999979429104642  | 0      |
| 432 | Tensor<[1, 68, 14, 14]> self = ?,<br>Tensor<[1, 68, 14, 14]> other = ?        | Done     | Done       | 0.999998119251079   | 0      |
| 433 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?      | Done     | Done       | 0.9999979887285766  | 0      |
| 434 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947861893598  | 0      |
| 435 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?              | Done     | Done       | 0.9999979480431542  | 0      |
| 436 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?        | Done     | Done       | 0.9999979701902042  | 0      |
| 437 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?          | Done     | Done       | 0.9999980680652885  | 0      |
| 438 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?                | Done     | Done       | 0.9999977825679555  | 0      |
| 439 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?        | Done     | Done       | 0.9999979283123656  | 0      |
| 440 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?        | Done     | Done       | 0.9999979976949911  | 0      |
| 441 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?        | Done     | Done       | 0.9999979651018088  | 0      |
| 442 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ?      | Done     | Done       | 0.9999979999294518  | 0      |
| 443 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?      | Done     | Done       | 0.9999980053125627  | 0      |
| 444 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?      | Done     | Done       | 0.9999979943067713  | 0      |
| 445 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?    | Done     | Done       | 0.9999979868467024  | 0      |
| 446 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?      | Done     | Done       | 0.9999979889801496  | 0      |
| 447 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                    | Done     | Done       | 0.9999980355093994  | 0      |
| 448 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?          | Done     | Done       | 0.9999979457899681  | 0      |
| 449 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                      | Unknown  | Done       | 0.9999972366889543  | 0      |
| 450 | Tensor<[1, 78, 28, 28]> self = ?,<br>Tensor<[1, 78, 28, 28]> other = ?        | Done     | Done       | 0.9999980126294984  | 0      |
| 451 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?          | Done     | Done       | 0.9999979994675329  | 0      |
| 452 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?            | Unknown  | Done       | 0.9999979855103546  | 0      |
| 453 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?            | Unknown  | Done       | 0.9999977640728108  | 0      |
| 454 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999964908367523  | 0      |
| 455 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?              | Unknown  | Done       | 0.9999960792746743  | 0      |
| 456 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999959790869518  | 0      |
| 457 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?              | Unknown  | Done       | 0.9999990664702576  | 0      |
| 458 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 459 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 460 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999978711412286  | 0      |
| 461 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?          | Unknown  | Done       | 0.9999979701436918  | 0      |
| 462 | Tensor<[1, 8, 112, 112]> self = ?,<br>Tensor<[1, 8, 112, 112]> other = ?      | Done     | Done       | 0.9999979527117904  | 0      |
| 463 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ?      | Done     | Done       | 0.9999979960317469  | 0      |
| 464 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?                | Done     | Done       | 0.9999976279952624  | 0      |
| 465 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?        | Done     | Done       | 0.9999979872914828  | 0      |
| 466 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?          | Done     | Done       | 0.9999979809148896  | 0      |
| 467 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?        | Unknown  | Done       | 0.9999979253905279  | 0      |
| 468 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?        | Done     | Done       | 0.9999978850249018  | 0      |
| 469 | Tensor<[1, 80, 15, 15]> self = ?,<br>Tensor<[1, 80, 15, 15]> other = ?        | Done     | Done       | 0.999998040133234   | 0      |
| 470 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?        | Unknown  | Done       | 0.9999980604102431  | 0      |
| 471 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?        | Done     | Done       | 0.9999979910372723  | 0      |
| 472 | Tensor<[1, 80, 7, 7]> self = ?,<br>Tensor<[1, 80, 7, 7]> other = ?            | Done     | Done       | 0.9999981105695068  | 0      |
| 473 | Tensor<[1, 88, 17, 17]> self = ?,<br>Tensor<[1, 88, 17, 17]> other = ?        | Done     | Done       | 0.9999979771119254  | 0      |
| 474 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?          | Done     | Done       | 0.999997992370935   | 0      |
| 475 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?      | Done     | Done       | 0.9999979925958736  | 0      |
| 476 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?              | Done     | Done       | 0.9999980714294429  | 0      |
| 477 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                           | Done     | Done       | 0.9999951682486453  | 0      |
| 478 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                | Done     | Done       | 0.9999974760901021  | 0      |
| 479 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947743656381  | 0      |
| 480 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?            | Done     | Done       | 0.9999979674186574  | 0      |
| 481 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?              | Done     | Done       | 0.9999980461039866  | 0      |
| 482 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947971601032  | 0      |
| 483 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?              | Done     | Done       | 0.9999980189290401  | 0      |
| 484 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999948573687557  | 0      |
| 485 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?              | Done     | Done       | 0.9999980209710274  | 0      |
| 486 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?                | Done     | Done       | 0.9999978505070751  | 0      |
| 487 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999946016835198  | 0      |
| 488 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?              | Done     | Done       | 0.9999979870171778  | 0      |
| 489 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?          | Done     | Done       | 0.9999980239842501  | 0      |
| 490 | Tensor<[1, 92, 14, 14]> self = ?,<br>Tensor<[1, 92, 14, 14]> other = ?        | Done     | Done       | 0.9999979228334999  | 0      |
| 491 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?        | Done     | Done       | 0.9999979472686966  | 0      |
| 492 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?        | Done     | Done       | 0.9999980185394656  | 0      |
| 493 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?        | Done     | Done       | 0.9999979873000536  | 0      |
| 494 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?            | Done     | Done       | 0.9999981020101607  | 0      |
| 495 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?          | Done     | Done       | 0.999998001550995   | 0      |
| 496 | Tensor<[1, 98, 28, 28]> self = ?,<br>Tensor<[1, 98, 28, 28]> other = ?        | Done     | Done       | 0.9999980230950638  | 0      |
| 497 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor<[1, s0*s1, 1280]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 498 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor<[1, s0*s1, 640]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 499 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 500 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor<[1, s1*s2, 320]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 501 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor<[1, s1*s2, 640]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 502 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                 | 0      |
| 503 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.9999111531971948  | 0      |
| 504 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                      | Unknown  | Done       | 0.9999984742222651  | 0      |
| 505 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?            | Done     | Done       | 0.9999979818221042  | 0      |
| 506 | Tensor<[100]> self = ?,<br>Tensor other = 0.0                                 | Unknown  | Done       | 1.0                 | 0      |
| 507 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                                | Unknown  | Done       | 0.9999971487768716  | 0      |
| 508 | Tensor<[10]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | 1.0                 | 0      |
| 509 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?              | Done     | Done       | 0.9999978568915073  | 0      |
| 510 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999976000335414  | 0      |
| 511 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999990563909161  | 0      |
| 512 | Tensor<[12]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 513 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Unknown  | Done       | 0.9999980416802614  | 0      |
| 514 | Tensor<[136]> self = ?,<br>Tensor other = 0.0                                 | Unknown  | Done       | 1.0                 | 0      |
| 515 | Tensor<[14]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                 | -1     |
| 516 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                 | 0      |
| 517 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.9999335459487656  | 0      |
| 518 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                      | Unknown  | Done       | 0.999998340964522   | 0      |
| 519 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?         | Done     | Done       | 0.9999980498845507  | 0      |
| 520 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?         | Done     | Done       | 0.9999979969563447  | 0      |
| 521 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?         | Done     | Done       | 0.9999979690588547  | 0      |
| 522 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?         | Done     | Done       | 0.9999979851646783  | 0      |
| 523 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999988902637694  | 0      |
| 524 | Tensor<[16]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 525 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                 | 0      |
| 526 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 0.9996852263549599  | 0      |
| 527 | Tensor<[19]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | 0.9999977455431327  | 0      |
| 528 | Tensor<[1]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | 1.0                 | 0      |
| 529 | Tensor<[2*s0]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                 | N/A    |
| 530 | Tensor<[2*s1]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                 | N/A    |
| 531 | Tensor<[2*s2]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                 | N/A    |
| 532 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                 | 0      |
| 533 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 0.9999748681080515  | 0      |
| 534 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                      | Unknown  | Done       | 0.9999982037703791  | 0      |
| 535 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?              | Unknown  | Done       | 0.9999979405776492  | 0      |
| 536 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?                | Done     | Done       | 0.999997916438179   | 0      |
| 537 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?                | Done     | Done       | 0.9999979266766325  | 0      |
| 538 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?              | Done     | Done       | 0.9999980591250174  | 0      |
| 539 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                      | Done     | Done       | 0.9999980216483124  | 0      |
| 540 | Tensor<[20]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | 0.9999988790957628  | 0      |
| 541 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Unknown  | Done       | 0.9999982787496423  | 0      |
| 542 | Tensor<[23]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 543 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                              | Done     | Done       | 0.9765772729570835  | 0      |
| 544 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999979085794547  | 0      |
| 545 | Tensor<[25, 4]> self = ?,<br>Tensor<[25, 1]> other = ?                        | Unknown  | Done       | 0.9999983610194296  | 0      |
| 546 | Tensor<[28]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                 | -1     |
| 547 | Tensor<[2]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | 1.0                 | 0      |
| 548 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Fallback   | 1.0                 | -1     |
| 549 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Done       | 0.9999960557964076  | 0      |
| 550 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                 | -1     |
| 551 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                    | Unknown  | Done       | 0.9999979402576933  | 0      |
| 552 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                    | Unknown  | Done       | 0.9999979845888706  | 0      |
| 553 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                          | Unknown  | Done       | 0.9999978908475927  | 0      |
| 554 | Tensor<[32]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 555 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Unknown  | Done       | 0.9999981296701734  | 0      |
| 556 | Tensor<[38]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | 0.9999938146093568  | 0      |
| 557 | Tensor<[3]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | 0.9999701598774023  | 0      |
| 558 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?        | Done     | Done       | 0.9999979689750279  | 0      |
| 559 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?        | Done     | Done       | 0.999997976507023   | 0      |
| 560 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?        | Done     | Done       | 0.999997990353205   | 0      |
| 561 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?        | Done     | Done       | 0.9999979755268243  | 0      |
| 562 | Tensor<[40]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 563 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Done       | 0.9999973200479726  | 0      |
| 564 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999975494909228  | 0      |
| 565 | Tensor<[50]> self = ?,<br>Tensor other = 0.0                                  | Unknown  | Done       | 1.0                 | 0      |
| 566 | Tensor<[56]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                 | -1     |
| 567 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Unknown  | Done       | 0.9999979956456394  | 0      |
| 568 | Tensor<[5]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | 1.0                 | 0      |
| 569 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Done       | 0.9999948534533756  | 0      |
| 570 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                   | Unknown  | Done       | 0.9999979064916825  | 0      |
| 571 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?         | Done     | Done       | 0.9999979859151645  | 0      |
| 572 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?         | Done     | Done       | 0.9999979982687216  | 0      |
| 573 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?         | Done     | Done       | 0.9999980035896383  | 0      |
| 574 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?         | Done     | Done       | 0.9999979711507314  | 0      |
| 575 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999969978455158  | 0      |
| 576 | Tensor<[64]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 577 | Tensor<[68]> self = ?,<br>Tensor other = 0.0                                  | Unknown  | Done       | 1.0                 | 0      |
| 578 | Tensor<[7]> self = ?,<br>Tensor other = 0.0                                   | Removed  | Fallback   | 1.0                 | -1     |
| 579 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Fallback   | 1.0                 | -1     |
| 580 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Done       | 0.9999963019585074  | 0      |
| 581 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Unknown  | Done       | 0.999997955803492   | 0      |
| 582 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                    | Unknown  | Done       | 0.9999978793232966  | 0      |
| 583 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                    | Unknown  | Done       | 0.9999980494129319  | 0      |
| 584 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                          | Unknown  | Done       | 0.9999981167136487  | 0      |
| 585 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.29007922241819173 | 0      |
| 586 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?            | Done     | Done       | 0.9999979945263819  | 0      |
| 587 | Tensor<[]> self = ?,<br>Tensor other = 1                                      | None     | Fallback   | 1.0                 | -1     |
| 588 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | 1.0                 | -1     |
| 589 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                        | Unknown  | Unknown    | N/A                 | N/A    |
| 590 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                 | N/A    |

