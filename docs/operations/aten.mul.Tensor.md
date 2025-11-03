### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC                | Host   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                               | Done     | Unknown    | N/A                | N/A    |
|   1 | Tensor self = ?,<br>Tensor<[3234, 1]> other = ?                                | Done     | Unknown    | N/A                | N/A    |
|   2 | Tensor self = ?,<br>Tensor<[8732, 1]> other = ?                                | Done     | Unknown    | N/A                | N/A    |
|   3 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.999998977126741  | 0      |
|   4 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999938539599285 | 0      |
|   5 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999951281345381 | 0      |
|   6 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999973439534706 | 0      |
|   7 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                | N/A    |
|   8 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                | N/A    |
|   9 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?             | Done     | Unknown    | N/A                | N/A    |
|  10 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999949014964679 | 0      |
|  11 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Done       | 0.9999974954402399 | 0      |
|  12 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                | 0      |
|  13 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | 1.0                | 0      |
|  14 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  | Unknown    | N/A                | N/A    |
|  15 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | Done       | 0.9999953806498769 | 0      |
|  16 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999949609431333 | 0      |
|  17 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                | 0      |
|  18 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | 1.0                | 0      |
|  19 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999991555830711 | 0      |
|  20 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999986214472559 | 0      |
|  21 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | 0.9999935207216559 | 0      |
|  22 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999987625320093 | 0      |
|  23 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999998357436033 | 0      |
|  24 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999960589057989 | 0      |
|  25 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999982102036744 | 0      |
|  26 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                | N/A    |
|  27 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  28 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                | N/A    |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Done       | 1.0                | 0      |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999954029467707 | 0      |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                | 0      |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                | 0      |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999968809758496 | 0      |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Done       | 0.999994738448292  | 0      |
|  35 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999964463146849 | 0      |
|  36 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                | N/A    |
|  37 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                | N/A    |
|  38 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
|  39 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.9999958078997677 | 0      |
|  40 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                | N/A    |
|  41 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[1, 1, 2048, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  42 | Tensor<[1, 1, 2048, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
|  43 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | Done       | 0.9999951682164835 | 0      |
|  44 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | Done       | 0.9999956034985951 | 0      |
|  45 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | Done       | 0.9999965788733296 | 0      |
|  46 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1                              | Unknown  | Unknown    | N/A                | N/A    |
|  47 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999952580897812 | 0      |
|  48 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                | 0      |
|  49 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.999997569766873  | 0      |
|  50 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | 0.9999953492786381 | 0      |
|  51 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999969451327908 | 0      |
|  52 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999997623276341 | 0      |
|  53 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | 0.9999943292993386 | 0      |
|  54 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999955673132424 | 0      |
|  55 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                | 0      |
|  56 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972600569719 | 0      |
|  57 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.9999957279029202 | 0      |
|  58 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Done     | Done       | 0.999998555822056  | 0      |
|  59 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Done       | 0.9999964150050913 | 0      |
|  60 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999946562796506 | 0      |
|  61 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?             | Unknown  | Unknown    | N/A                | N/A    |
|  62 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Done       | 0.9999958942544175 | 0      |
|  63 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125                          | Unknown  | Unknown    | N/A                | N/A    |
|  64 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999959262808458 | 0      |
|  65 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  | Done       | 0.9999957187597313 | 0      |
|  66 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.999995233933689  | 0      |
|  67 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999964629091602 | 0      |
|  68 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Removed  | Done       | 0.9999961605376995 | 0      |
|  69 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999959124569443 | 0      |
|  70 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.9999959116272442 | 0      |
|  71 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999958773128463 | 0      |
|  72 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | 0.999996061298153  | 0      |
|  73 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | 0.9999957440190214 | 0      |
|  74 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | 0.9999959394487042 | 0      |
|  75 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | 0.999999999158109  | 0      |
|  76 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999954098633861 | 0      |
|  77 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                | 0      |
|  78 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972811382549 | 0      |
|  79 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | 0.9999958350364532 | 0      |
|  80 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                | 0      |
|  81 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | 0.9999959154655018 | 0      |
|  82 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | 0.9999959448717646 | 0      |
|  83 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | Done       | 0.9999960071505503 | 0      |
|  84 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | 0.999996095091039  | 0      |
|  85 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | 0.9999958913332988 | 0      |
|  86 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | 0.9999959378057065 | 0      |
|  87 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Removed  | Done       | 0.9999976166147616 | 0      |
|  88 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999960544830825 | 0      |
|  89 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | Done       | 0.9999961700708163 | 0      |
|  90 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | 0.9999959328402617 | 0      |
|  91 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999954431483937 | 0      |
|  92 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                | 0      |
|  93 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999971704801437 | 0      |
|  94 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | 0.9999959959362172 | 0      |
|  95 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | 0.9999955911588538 | 0      |
|  96 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | 0.9999960539150944 | 0      |
|  97 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.999995294087931  | 0      |
|  98 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                | 0      |
|  99 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999971682893105 | 0      |
| 100 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Unknown  | Done       | 0.9999960943838504 | 0      |
| 101 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Unknown  | Done       | 0.999996763131516  | 0      |
| 102 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | 0.9999957239342668 | 0      |
| 103 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | 0.9999955477161827 | 0      |
| 104 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                | 0      |
| 105 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Unknown  | Done       | 1.0                | 0      |
| 106 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999961406840726 | 0      |
| 107 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | 0.9999960293679301 | 0      |
| 108 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | 0.9999957734901304 | 0      |
| 109 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | 0.9999956670990215 | 0      |
| 110 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                | 0      |
| 111 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Unknown  | Done       | 0.999997829362014  | 0      |
| 112 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Done     | Done       | 0.9999959767939828 | 0      |
| 113 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | 0.9999958613069335 | 0      |
| 114 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Done       | 0.9999959232576004 | 0      |
| 115 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Removed  | Done       | 0.9999954220407922 | 0      |
| 116 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999959803122865 | 0      |
| 117 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | 0.99999589069472   | 0      |
| 118 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | 0.9999959220926125 | 0      |
| 119 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | 0.9999959963343623 | 0      |
| 120 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Done     | Done       | 0.9999955789170737 | 0      |
| 121 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | 0.9999957105486768 | 0      |
| 122 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.999995827430283  | 0      |
| 123 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                | 0      |
| 124 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | 0.9999959115417802 | 0      |
| 125 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                | 0      |
| 126 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | 0.9999957859639322 | 0      |
| 127 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | 0.9999959463927443 | 0      |
| 128 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Removed  | Done       | 0.9999959881420807 | 0      |
| 129 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                | N/A    |
| 130 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | 0.9999963400986972 | 0      |
| 131 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | 0.9999958869328411 | 0      |
| 132 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.999995990276553  | 0      |
| 133 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999961818610523 | 0      |
| 134 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999958352778723 | 0      |
| 135 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.999995932413687  | 0      |
| 136 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | 0.999995916138014  | 0      |
| 137 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.999996074342883  | 0      |
| 138 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 139 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | 0.9999957656845321 | 0      |
| 140 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | 0.9999959458925809 | 0      |
| 141 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor other = 2                        | Unknown  | Unknown    | N/A                | N/A    |
| 142 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[1, 3, 16, 16, 2]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 143 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  | Unknown    | N/A                | N/A    |
| 144 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor other = ?                         | Done     | Unknown    | N/A                | N/A    |
| 145 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     | Done       | 0.9999962194851975 | 0      |
| 146 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Done     | Done       | 0.9999961294167513 | 0      |
| 147 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor other = 2                        | Unknown  | Unknown    | N/A                | N/A    |
| 148 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[1, 3, 32, 32, 2]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 149 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  | Unknown    | N/A                | N/A    |
| 150 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                         | Done     | Unknown    | N/A                | N/A    |
| 151 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | Done       | 0.9999959722591745 | 0      |
| 152 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Done     | Done       | 0.9999958556341383 | 0      |
| 153 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor other = 2                        | Unknown  | Unknown    | N/A                | N/A    |
| 154 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[1, 3, 64, 64, 2]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 155 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  | Unknown    | N/A                | N/A    |
| 156 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                | 0      |
| 157 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | 0.9999959026410205 | 0      |
| 158 | Tensor<[1, 32, 11008]> self = ?,<br>Tensor<[1, 32, 11008]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 159 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 1, 32, 128]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 160 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 1]> other = ?                | Unknown  | Unknown    | N/A                | N/A    |
| 161 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999957644200421 | 0      |
| 162 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953441964983 | 0      |
| 163 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                | 0      |
| 164 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | Done       | 0.9999972114423216 | 0      |
| 165 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | 0.999996009289446  | 0      |
| 166 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                | 0      |
| 167 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | 0.9999966613144562 | 0      |
| 168 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | 0.9999961052474843 | 0      |
| 169 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | 0.9999995168581681 | 0      |
| 170 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Done       | 0.9999960348661223 | 0      |
| 171 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | 0.9999959272040383 | 0      |
| 172 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                | 0      |
| 173 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?         | Unknown  | Done       | 0.9999959523149674 | 0      |
| 174 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999950238825508 | 0      |
| 175 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | 0.999995556784443  | 0      |
| 176 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | 0.9999957971974082 | 0      |
| 177 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999954018771078 | 0      |
| 178 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                | 0      |
| 179 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.999997238858972  | 0      |
| 180 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | 0.9999959254386268 | 0      |
| 181 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | 0.9999956058544023 | 0      |
| 182 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | Done       | 0.9999959125828476 | 0      |
| 183 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | 0.999996059257691  | 0      |
| 184 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | Done       | 0.9999959018476526 | 0      |
| 185 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | 0.9999960675081971 | 0      |
| 186 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | 0.9999959535043752 | 0      |
| 187 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.999996120760445  | 0      |
| 188 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953381342853 | 0      |
| 189 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                | 0      |
| 190 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972503812624 | 0      |
| 191 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999959968554517 | 0      |
| 192 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | Done     | Done       | 0.9999959817864285 | 0      |
| 193 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Done     | Done       | 0.9999959950955927 | 0      |
| 194 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                | 0      |
| 195 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Removed  | Done       | 0.9999961120730511 | 0      |
| 196 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Done     | Done       | 0.9999959783835596 | 0      |
| 197 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999960254619628 | 0      |
| 198 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999957807467347 | 0      |
| 199 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | 0.999995930751722  | 0      |
| 200 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999959438484894 | 0      |
| 201 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.999995867331082  | 0      |
| 202 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Done     | Done       | 0.9999944148645054 | 0      |
| 203 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | 0.9999958502436302 | 0      |
| 204 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | 0.9999958956410274 | 0      |
| 205 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | 0.9999959717584422 | 0      |
| 206 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Unknown  | Done       | 1.0                | 0      |
| 207 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Unknown  | Done       | 0.9999955498965948 | 0      |
| 208 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                | 0      |
| 209 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | 0.9999940579493949 | 0      |
| 210 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Removed  | Done       | 0.9999947834669144 | 0      |
| 211 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | 0.9999960082169235 | 0      |
| 212 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                | N/A    |
| 213 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | Done     | Done       | 0.9999959377700725 | 0      |
| 214 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | Done       | 0.9999960793244659 | 0      |
| 215 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | Done       | 0.9999962540081284 | 0      |
| 216 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999954910494214 | 0      |
| 217 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                | N/A    |
| 218 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | Done       | 0.9999960394181823 | 0      |
| 219 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | Done       | 0.9999962674000175 | 0      |
| 220 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                | N/A    |
| 221 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | Done     | Done       | 0.9999959305769562 | 0      |
| 222 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | 0.99999523589178   | 0      |
| 223 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | Done       | 0.9999962146918251 | 0      |
| 224 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999960748334183 | 0      |
| 225 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                | N/A    |
| 226 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | Done       | 0.9999959224999346 | 0      |
| 227 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | Done       | 0.9999958624633056 | 0      |
| 228 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                | N/A    |
| 229 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | Done     | Done       | 0.9999959521068218 | 0      |
| 230 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | 0.9999953914095229 | 0      |
| 231 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | Done       | 0.9999959404405672 | 0      |
| 232 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | Done       | 0.9999959580627565 | 0      |
| 233 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | 0.9999959484395915 | 0      |
| 234 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | Done       | 0.99999606123594   | 0      |
| 235 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999957493957415 | 0      |
| 236 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | 0.999995910021602  | 0      |
| 237 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | 0.9999959636386175 | 0      |
| 238 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | 0.9999958475859445 | 0      |
| 239 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999960991406478 | 0      |
| 240 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | 0.99999595289491   | 0      |
| 241 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953936663631 | 0      |
| 242 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                | 0      |
| 243 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972302977982 | 0      |
| 244 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | 0.9999957527122741 | 0      |
| 245 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 246 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | 0.9999954461907818 | 0      |
| 247 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | Done       | 0.9999961342631658 | 0      |
| 248 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | 0.9999961747283386 | 0      |
| 249 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | 0.9999963001208969 | 0      |
| 250 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | 0.9999959769142418 | 0      |
| 251 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | 0.9999959559538083 | 0      |
| 252 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | 0.9999959471077782 | 0      |
| 253 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | 0.9999960419508417 | 0      |
| 254 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | 0.9999959479674164 | 0      |
| 255 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?          | Done     | Unknown    | N/A                | N/A    |
| 256 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?          | Done     | Unknown    | N/A                | N/A    |
| 257 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | 0.999995812445919  | 0      |
| 258 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                | 0      |
| 259 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | 0.9999960461158142 | 0      |
| 260 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Done       | 0.9999959922583593 | 0      |
| 261 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | Done       | 0.9999959794184925 | 0      |
| 262 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | Done       | 1.0                | 0      |
| 263 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | Done       | 0.9999971204461431 | 0      |
| 264 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | 0.9999969475681392 | 0      |
| 265 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953794026377 | 0      |
| 266 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                | 0      |
| 267 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972510276963 | 0      |
| 268 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | 0.9999959111033322 | 0      |
| 269 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953029585928 | 0      |
| 270 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                | 0      |
| 271 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972484556853 | 0      |
| 272 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | 0.9999957008817448 | 0      |
| 273 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953613377539 | 0      |
| 274 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                | 0      |
| 275 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971350996684 | 0      |
| 276 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | 0.9999956031793438 | 0      |
| 277 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999954276765669 | 0      |
| 278 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                | 0      |
| 279 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972745647756 | 0      |
| 280 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | 0.9999959758082754 | 0      |
| 281 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | 0.9999961593226233 | 0      |
| 282 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999959362714053 | 0      |
| 283 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | 0.9999962600593694 | 0      |
| 284 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999960210716204 | 0      |
| 285 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 286 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 287 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 1                             | Unknown  | Unknown    | N/A                | N/A    |
| 288 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 289 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 290 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 291 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A                | N/A    |
| 292 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                | 0      |
| 293 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                | 0      |
| 294 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | 0.9999957800542754 | 0      |
| 295 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Unknown  | Done       | 0.9999956220877518 | 0      |
| 296 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                | 0      |
| 297 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                | 0      |
| 298 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958621093188 | 0      |
| 299 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | Done     | Done       | 0.9999957829673634 | 0      |
| 300 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958604596735 | 0      |
| 301 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | Done     | Done       | 0.9999965337866074 | 0      |
| 302 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -0.4570457994644658             | Done     | Unknown    | N/A                | N/A    |
| 303 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -0.5900435899266435             | Done     | Unknown    | N/A                | N/A    |
| 304 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -1.0925484305920792             | Done     | Unknown    | N/A                | N/A    |
| 305 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.31539156525252005             | Done     | Unknown    | N/A                | N/A    |
| 306 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.3731763325901154              | Done     | Unknown    | N/A                | N/A    |
| 307 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.4886025119029199              | Done     | Unknown    | N/A                | N/A    |
| 308 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.5462742152960396              | Done     | Unknown    | N/A                | N/A    |
| 309 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.0                             | Done     | Unknown    | N/A                | N/A    |
| 310 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.0925484305920792              | Done     | Unknown    | N/A                | N/A    |
| 311 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.445305721320277               | Done     | Unknown    | N/A                | N/A    |
| 312 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2                               | Removed  | Unknown    | N/A                | N/A    |
| 313 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2.0                             | Done     | Unknown    | N/A                | N/A    |
| 314 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2.890611442640554               | Done     | Unknown    | N/A                | N/A    |
| 315 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 3                               | Done     | Unknown    | N/A                | N/A    |
| 316 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 4                               | Done     | Unknown    | N/A                | N/A    |
| 317 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 1]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 318 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 3]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 319 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 4]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 320 | Tensor<[16384, 3]> self = ?,<br>Tensor other = 0.28209479177387814             | Done     | Unknown    | N/A                | N/A    |
| 321 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 1]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 322 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 3]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 323 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 1]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 324 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 4]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 325 | Tensor<[16384]> self = ?,<br>Tensor other = 0.5                                | Done     | Unknown    | N/A                | N/A    |
| 326 | Tensor<[16384]> self = ?,<br>Tensor other = 1                                  | Done     | Unknown    | N/A                | N/A    |
| 327 | Tensor<[16384]> self = ?,<br>Tensor other = 2                                  | Done     | Unknown    | N/A                | N/A    |
| 328 | Tensor<[16384]> self = ?,<br>Tensor other = 256                                | Done     | Unknown    | N/A                | N/A    |
| 329 | Tensor<[16384]> self = ?,<br>Tensor other = 3.0                                | Done     | Unknown    | N/A                | N/A    |
| 330 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
| 331 | Tensor<[16384]> self = ?,<br>Tensor<[]> other = ?                              | Done     | Unknown    | N/A                | N/A    |
| 332 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                | 0      |
| 333 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                                 | Unknown  | Unknown    | N/A                | N/A    |
| 334 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                | N/A    |
| 335 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                | N/A    |
| 336 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                | N/A    |
| 337 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Done     | Done       | 1.0                | 0      |
| 338 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Done     | Done       | 0.9999943688941296 | 0      |
| 339 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | Done     | Done       | 1.0                | 0      |
| 340 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0.3                                 | Done     | Unknown    | N/A                | N/A    |
| 341 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                | 0      |
| 342 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Done     | Done       | 0.9999959029394969 | 0      |
| 343 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | Done     | Done       | 0.9999960560645971 | 0      |
| 344 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | Done     | Done       | 0.9999958560524653 | 0      |
| 345 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | Done     | Done       | 1.0                | 0      |
| 346 | Tensor<[200]> self = ?,<br>Tensor<[]> other = ?                                | Done     | Unknown    | N/A                | N/A    |
| 347 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                                | Done     | Unknown    | N/A                | N/A    |
| 348 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 349 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                | 0      |
| 350 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                | N/A    |
| 351 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                                 | Done     | Unknown    | N/A                | N/A    |
| 352 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958437146627 | 0      |
| 353 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | Done     | Done       | 0.9999974616998372 | 0      |
| 354 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958216276297 | 0      |
| 355 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | Done     | Done       | 0.9999959432907705 | 0      |
| 356 | Tensor<[4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?                    | Unknown  | Unknown    | N/A                | N/A    |
| 357 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | 0.9999955018069072 | 0      |
| 358 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Unknown  | Done       | 0.9999957438255496 | 0      |
| 359 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Unknown  | Done       | 0.9999963846810203 | 0      |
| 360 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958529181996 | 0      |
| 361 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | 0.9999963543989212 | 0      |
| 362 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958442930621 | 0      |
| 363 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Done     | Done       | 0.9999960175340511 | 0      |
| 364 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | 0.999996812097755  | 0      |
| 365 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Unknown  | Done       | 0.9999959723392742 | 0      |
| 366 | Tensor<[8, 1, 1, 384]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Unknown    | N/A                | N/A    |
| 367 | Tensor<[813]> self = ?,<br>Tensor<[]> other = ?                                | Done     | Unknown    | N/A                | N/A    |
| 368 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 369 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                | 0      |
| 370 | Tensor<[8732, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                | N/A    |
| 371 | Tensor<[8732]> self = ?,<br>Tensor other = 0.5                                 | Done     | Unknown    | N/A                | N/A    |
| 372 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                          | Unknown  | Unknown    | N/A                | N/A    |
| 373 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | Unknown  | Done       | 0.9999951603754964 | 0      |
| 374 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ?                         | Unknown  | Unknown    | N/A                | N/A    |
| 375 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | Done     | Done       | 1.0                | 0      |
| 376 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                | N/A    |

