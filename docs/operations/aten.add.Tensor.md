### aten.add.Tensor
|     | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|----:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -6.0                        | Done     | Unknown    | N/A                | N/A    |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1                           | Done     | Unknown    | N/A                | N/A    |
|   2 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.0                         | Done     | Unknown    | N/A                | N/A    |
|   3 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 2                           | Done     | Unknown    | N/A                | N/A    |
|   4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.999987589688302  | 0      |
|   5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999927229591077 | 0      |
|   6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999969946534187 | 0      |
|   7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999845987354007 | 0      |
|   8 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999955229211595 | 0      |
|   9 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.999998364349777  | 0      |
|  10 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Unknown    | N/A                | N/A    |
|  11 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                           | Done     | Unknown    | N/A                | N/A    |
|  12 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Unknown    | N/A                | N/A    |
|  13 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2                           | Done     | Unknown    | N/A                | N/A    |
|  14 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?          | Unknown  | Done       | 0.9999981588968728 | 0      |
|  15 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839              | Done     | Done       | 1.0                | 0      |
|  16 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032              | Done     | Done       | 1.0                | 0      |
|  17 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226              | Done     | Done       | 1.0                | 0      |
|  18 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323              | Done     | Done       | 1.0                | 0      |
|  19 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516              | Done     | Done       | 1.0                | 0      |
|  20 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161              | Done     | Done       | 1.0                | 0      |
|  21 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581              | Done     | Done       | 1.0                | 0      |
|  22 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                           | Unknown  | Done       | 1.0                | 0      |
|  23 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027    | Done     | Done       | 0.9999999960917603 | 0      |
|  24 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997     | Done     | Done       | 0.9999990391758955 | 0      |
|  25 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994     | Done     | Done       | 0.9999998624153148 | 0      |
|  26 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.999995072083888  | 0      |
|  27 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | 0.9999981661909895 | 0      |
|  28 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999857583792017 | 0      |
|  29 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999917494294158 | 0      |
|  30 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999913395356413 | 0      |
|  31 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999926152155746 | 0      |
|  32 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999951337578117 | 0      |
|  33 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?              | Unknown  | Done       | 0.9999979972674791 | 0      |
|  34 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                | 0      |
|  35 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                | Unknown  | Done       | 0.9999983900027778 | 0      |
|  36 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  37 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Unknown  | Done       | 0.9999984299142968 | 0      |
|  38 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                   | Unknown  | Done       | 0.9999979616031167 | 0      |
|  39 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?            | Unknown  | Done       | 0.9999979917228656 | 0      |
|  40 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
|  41 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?              | Unknown  | Done       | 0.9999977889799181 | 0      |
|  42 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?              | Done     | Done       | 0.9999980605447549 | 0      |
|  43 | Tensor<[1, 100, 14, 14]> self = ?,<br>Tensor<[1, 100, 14, 14]> other = ?      | Done     | Done       | 0.9999980087959989 | 0      |
|  44 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?        | Done     | Done       | 0.999997947611532  | 0      |
|  45 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Removed  | Done       | 1.0                | 0      |
|  46 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ?    | Done     | Done       | 0.9999980395228962 | 0      |
|  47 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ?    | Done     | Done       | 0.9999980051521704 | 0      |
|  48 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?    | Done     | Done       | 0.9999979891894106 | 0      |
|  49 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?          | Done     | Done       | 0.9999979914121524 | 0      |
|  50 | Tensor<[1, 1024, 17, 17]> self = ?,<br>Tensor<[1, 1024, 17, 17]> other = ?    | Done     | Done       | 0.9999979873029005 | 0      |
|  51 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999980387740836 | 0      |
|  52 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999979781681183 | 0      |
|  53 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?    | Done     | Done       | 0.999997989267828  | 0      |
|  54 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?        | Done     | Done       | 0.9999980185441577 | 0      |
|  55 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999981700685815 | 0      |
|  56 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?      | Done     | Done       | 0.9999979883274935 | 0      |
|  57 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?    | Done     | Done       | 0.9999979851604405 | 0      |
|  58 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                                 | Done     | Done       | 1.0                | 0      |
|  59 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | 0.9999975160833663 | 0      |
|  60 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?      | Done     | Done       | 0.999997900002     | 0      |
|  61 | Tensor<[1, 112, 15, 15]> self = ?,<br>Tensor<[1, 112, 15, 15]> other = ?      | Done     | Done       | 0.9999979828747777 | 0      |
|  62 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?      | Done     | Done       | 0.9999979795282545 | 0      |
|  63 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ?      | Done     | Done       | 0.9999980552452327 | 0      |
|  64 | Tensor<[1, 116, 14, 14]> self = ?,<br>Tensor<[1, 116, 14, 14]> other = ?      | Done     | Done       | 0.9999979818931355 | 0      |
|  65 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999972000683104 | 0      |
|  66 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?          | Unknown  | Done       | 0.999996573938692  | 0      |
|  67 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999970466326328 | 0      |
|  68 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?            | Unknown  | Done       | 0.9999986047697067 | 0      |
|  69 | Tensor<[1, 12, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
|  70 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.99999587828062   | 0      |
|  71 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?            | Unknown  | Done       | 0.9999984900996071 | 0      |
|  72 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | 0.9999982328560125 | 0      |
|  73 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  74 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  75 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  76 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Removed  | Done       | 0.9999970603230569 | 0      |
|  77 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?        | Unknown  | Done       | 0.9999977471124366 | 0      |
|  78 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ?          | Removed  | Done       | 0.9999980328512214 | 0      |
|  79 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?              | Done     | Done       | 0.9999976956832232 | 0      |
|  80 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<[1, 1, 1, 14]> other = ?          | Removed  | Done       | 0.9999978328361286 | 0      |
|  81 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor<[1, 1, 1, 201]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  82 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?         | Unknown  | Done       | 0.9999979065721084 | 0      |
|  83 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ?          | Removed  | Done       | 0.9999980024171488 | 0      |
|  84 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999948570434655 | 0      |
|  85 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?            | Done     | Done       | 0.9999980370935713 | 0      |
|  86 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | 0.9999978765287334 | 0      |
|  87 | Tensor<[1, 12, 56, 56]> self = ?,<br>Tensor<[1, 12, 56, 56]> other = ?        | Done     | Done       | 0.9999980372234092 | 0      |
|  88 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ?             | Done     | Done       | 0.9999970208203041 | 0      |
|  89 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?              | Done     | Done       | 0.9999981514501134 | 0      |
|  90 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Removed  | Done       | 0.9999983890627977 | 0      |
|  91 | Tensor<[1, 120, 17, 17]> self = ?,<br>Tensor<[1, 120, 17, 17]> other = ?      | Done     | Done       | 0.9999980116620657 | 0      |
|  92 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?      | Done     | Done       | 0.9999979996375372 | 0      |
|  93 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?          | Done     | Done       | 0.9999980017747315 | 0      |
|  94 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?    | Done     | Done       | 0.9999979611418869 | 0      |
|  95 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Removed  | Done       | 1.0                | 0      |
|  96 | Tensor<[1, 128, 112, 112]> self = ?,<br>Tensor<[1, 128, 112, 112]> other = ?  | Done     | Done       | 0.9999979966183887 | 0      |
|  97 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ?  | Done     | Done       | 0.9999979930756345 | 0      |
|  98 | Tensor<[1, 128, 1536]> self = ?,<br>Tensor<[1, 128, 1536]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
|  99 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.999998013302055  | 0      |
| 100 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ?      | Done     | Done       | 0.9999979943196806 | 0      |
| 101 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ?      | Done     | Done       | 0.9999979894191081 | 0      |
| 102 | Tensor<[1, 128, 64, 64]> self = ?,<br>Tensor<[1, 128, 64, 64]> other = ?      | Done     | Done       | 0.9999979873077529 | 0      |
| 103 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?      | Done     | Done       | 0.9999979920414682 | 0      |
| 104 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999979359375    | 0      |
| 105 | Tensor<[1, 128, s1, s2]> self = ?,<br>Tensor<[1, 128, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 106 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?        | Unknown  | Done       | 0.9999980031862687 | 0      |
| 107 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?        | Unknown  | Done       | 0.99999799735342   | 0      |
| 108 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 109 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, s0, s1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 110 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 111 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, s1, s2]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 112 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ?    | Done     | Done       | 0.9999979600784213 | 0      |
| 113 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ?      | Done     | Done       | 0.9999980105839849 | 0      |
| 114 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?        | Done     | Done       | 0.9999979883683523 | 0      |
| 115 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?    | Done     | Done       | 0.9999980103804001 | 0      |
| 116 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?              | Done     | Done       | 0.9999978850521565 | 0      |
| 117 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?      | Done     | Done       | 0.9999980021841892 | 0      |
| 118 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?      | Done     | Done       | 0.9999979687673621 | 0      |
| 119 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999948218985504 | 0      |
| 120 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?            | Done     | Done       | 0.9999979867979717 | 0      |
| 121 | Tensor<[1, 14, 56, 56]> self = ?,<br>Tensor<[1, 14, 56, 56]> other = ?        | Done     | Done       | 0.9999979129954495 | 0      |
| 122 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?              | Done     | Done       | 0.9999979973200974 | 0      |
| 123 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?      | Done     | Done       | 0.9999979834324046 | 0      |
| 124 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?          | Done     | Done       | 0.9999979967290071 | 0      |
| 125 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?          | Done     | Done       | 0.9999979916616304 | 0      |
| 126 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999949990817644 | 0      |
| 127 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Unknown  | Done       | 0.9999980107643832 | 0      |
| 128 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
| 129 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?              | Unknown  | Done       | 0.9999981270101527 | 0      |
| 130 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ?          | Unknown  | Done       | 0.999998000715359  | 0      |
| 131 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?             | Unknown  | Done       | 0.9999979838974143 | 0      |
| 132 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?        | Done     | Done       | 0.9999979752513457 | 0      |
| 133 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Tensor<[1, 1536, 8, 8]> other = ?        | Done     | Done       | 0.9999980108427933 | 0      |
| 134 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 135 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
| 136 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999917621303557 | 0      |
| 137 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?            | Unknown  | Done       | 0.9999992444877135 | 0      |
| 138 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Unknown    | N/A                | N/A    |
| 139 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 140 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999979209864898 | 0      |
| 141 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Done       | 0.9999981879623404 | 0      |
| 142 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 143 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 144 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 145 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.999997803418997  | 0      |
| 146 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?        | Unknown  | Done       | 0.9999978207922552 | 0      |
| 147 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ?    | Done     | Done       | 0.999997973849981  | 0      |
| 148 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?      | Done     | Done       | 0.9999979775994537 | 0      |
| 149 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?      | Done     | Done       | 0.9999979757809424 | 0      |
| 150 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ?    | Done     | Done       | 0.9999979934150703 | 0      |
| 151 | Tensor<[1, 16, 28, 28]> self = ?,<br>Tensor<[1, 16, 28, 28]> other = ?        | Done     | Done       | 0.999997846967355  | 0      |
| 152 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Done       | 0.9999989162418716 | 0      |
| 153 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Unknown  | Done       | 0.9999979777317443 | 0      |
| 154 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 155 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 156 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?              | Done     | Done       | 0.9999980493597447 | 0      |
| 157 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 158 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 159 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Removed  | Done       | 0.9999981452992871 | 0      |
| 160 | Tensor<[1, 160, 14, 14]> self = ?,<br>Tensor<[1, 160, 14, 14]> other = ?      | Done     | Done       | 0.9999979276339694 | 0      |
| 161 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ?      | Done     | Done       | 0.9999980295780959 | 0      |
| 162 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ?      | Done     | Done       | 0.9999980403439316 | 0      |
| 163 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?      | Done     | Done       | 0.9999979839056895 | 0      |
| 164 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?          | Done     | Done       | 0.9999980378583114 | 0      |
| 165 | Tensor<[1, 160, 73, 73]> self = ?,<br>Tensor<[1, 160, 73, 73]> other = ?      | Done     | Done       | 0.9999979855825843 | 0      |
| 166 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999979522103877 | 0      |
| 167 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?          | Done     | Done       | 0.9999979861059989 | 0      |
| 168 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ?      | Done     | Done       | 0.9999980233820686 | 0      |
| 169 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?        | Done     | Done       | 0.9999979831018837 | 0      |
| 170 | Tensor<[1, 185, 28, 28]> self = ?,<br>Tensor<[1, 185, 28, 28]> other = ?      | Done     | Done       | 0.9999979889113073 | 0      |
| 171 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ?      | Done     | Done       | 0.9999980215941723 | 0      |
| 172 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ?      | Done     | Done       | 0.9999979918678387 | 0      |
| 173 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?      | Done     | Done       | 0.9999980087155581 | 0      |
| 174 | Tensor<[1, 192, 7, 7]> self = ?,<br>Tensor<[1, 192, 7, 7]> other = ?          | Done     | Done       | 0.999997946109431  | 0      |
| 175 | Tensor<[1, 192, 71, 71]> self = ?,<br>Tensor<[1, 192, 71, 71]> other = ?      | Done     | Done       | 0.9999979984026373 | 0      |
| 176 | Tensor<[1, 192, 8, 8]> self = ?,<br>Tensor<[1, 192, 8, 8]> other = ?          | Done     | Done       | 0.9999979374851291 | 0      |
| 177 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?        | Done     | Done       | 0.9999979772232361 | 0      |
| 178 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?          | Done     | Done       | 0.9999979919989248 | 0      |
| 179 | Tensor<[1, 193, 768]> self = ?,<br>Tensor<[1, 193, 768]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 180 | Tensor<[1, 196, 14, 14]> self = ?,<br>Tensor<[1, 196, 14, 14]> other = ?      | Done     | Done       | 0.9999980167770336 | 0      |
| 181 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ?            | Done     | Done       | 0.9999980057028194 | 0      |
| 182 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?          | Done     | Done       | 0.9999979752019554 | 0      |
| 183 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?            | Done     | Done       | 0.9999979721936081 | 0      |
| 184 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                | 0      |
| 185 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 186 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Done       | 1.0                | 0      |
| 187 | Tensor<[1, 20, 28, 28]> self = ?,<br>Tensor<[1, 20, 28, 28]> other = ?        | Done     | Done       | 0.9999979738270552 | 0      |
| 188 | Tensor<[1, 201, 768]> self = ?,<br>Tensor<[1, 201, 768]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 189 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?        | Done     | Done       | 0.9999980022996905 | 0      |
| 190 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Removed  | Done       | 1.0                | 0      |
| 191 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999980194967338 | 0      |
| 192 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?    | Done     | Done       | 0.9999979969509785 | 0      |
| 193 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?        | Done     | Done       | 0.9999980081037878 | 0      |
| 194 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?          | Done     | Done       | 0.9999979941940634 | 0      |
| 195 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?             | Done     | Done       | 0.9999979849678566 | 0      |
| 196 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?      | Done     | Done       | 0.9999979763013092 | 0      |
| 197 | Tensor<[1, 208, 9, 9]> self = ?,<br>Tensor<[1, 208, 9, 9]> other = ?          | Done     | Done       | 0.9999980635280851 | 0      |
| 198 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?      | Done     | Done       | 0.9999980059628142 | 0      |
| 199 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?      | Done     | Done       | 0.999997998617553  | 0      |
| 200 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?          | Done     | Done       | 0.9999978624165728 | 0      |
| 201 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                | 0      |
| 202 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ?      | Done     | Done       | 0.9999979324097767 | 0      |
| 203 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?      | Done     | Done       | 0.999997979762883  | 0      |
| 204 | Tensor<[1, 24, 112, 112]> self = ?,<br>Tensor<[1, 24, 112, 112]> other = ?    | Done     | Done       | 0.9999979980347881 | 0      |
| 205 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?        | Done     | Done       | 0.9999980201134776 | 0      |
| 206 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?        | Done     | Done       | 0.9999980062429947 | 0      |
| 207 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?        | Done     | Done       | 0.999997985401826  | 0      |
| 208 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?        | Done     | Done       | 0.9999980172484039 | 0      |
| 209 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?        | Done     | Done       | 0.9999979848878887 | 0      |
| 210 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?        | Done     | Done       | 0.9999980397034683 | 0      |
| 211 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?              | Unknown  | Done       | 0.9999979681545166 | 0      |
| 212 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?        | Done     | Done       | 0.9999980080910891 | 0      |
| 213 | Tensor<[1, 240, 14, 14]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?      | Done     | Done       | 0.9999980042290688 | 0      |
| 214 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?      | Done     | Done       | 0.9999979948434857 | 0      |
| 215 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?              | Done     | Done       | 0.9999979687400411 | 0      |
| 216 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?        | Done     | Done       | 0.9999980048032546 | 0      |
| 217 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Removed  | Done       | 1.0                | 0      |
| 218 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ?  | Done     | Done       | 0.999997994309169  | 0      |
| 219 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?          | Done     | Done       | 0.999997968688217  | 0      |
| 220 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ?      | Done     | Done       | 0.9999980111779109 | 0      |
| 221 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?      | Done     | Done       | 0.9999979962332537 | 0      |
| 222 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?            | Done     | Done       | 0.9999979692428462 | 0      |
| 223 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979855911496 | 0      |
| 224 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ?  | Done     | Done       | 0.9999979936581921 | 0      |
| 225 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?            | Done     | Done       | 0.9999980106715928 | 0      |
| 226 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.9999979955388011 | 0      |
| 227 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ?      | Done     | Done       | 0.9999979880269971 | 0      |
| 228 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?      | Done     | Done       | 0.9999980008791526 | 0      |
| 229 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?              | Done     | Done       | 0.9999979126617142 | 0      |
| 230 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?      | Done     | Done       | 0.9999979757185739 | 0      |
| 231 | Tensor<[1, 256, 384]> self = ?,<br>Tensor<[1, 256, 384]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 232 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999979826878493 | 0      |
| 233 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?      | Done     | Done       | 0.9999979764428507 | 0      |
| 234 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?      | Done     | Done       | 0.9999979930801751 | 0      |
| 235 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?              | Done     | Done       | 0.9999979906985396 | 0      |
| 236 | Tensor<[1, 256, 7, 7]> self = ?,<br>Tensor<[1, 256, 7, 7]> other = ?          | Done     | Done       | 0.9999981064343963 | 0      |
| 237 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?      | Done     | Done       | 0.9999980007221254 | 0      |
| 238 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999979343499404 | 0      |
| 239 | Tensor<[1, 256, s1, s2]> self = ?,<br>Tensor<[1, 256, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 240 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[1, 257, 768]> other = ?            | Done     | Unknown    | N/A                | N/A    |
| 241 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ?      | Done     | Done       | 0.9999979728200437 | 0      |
| 242 | Tensor<[1, 272, 7, 7]> self = ?,<br>Tensor<[1, 272, 7, 7]> other = ?          | Done     | Done       | 0.999997933527162  | 0      |
| 243 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?      | Done     | Done       | 0.9999979691326008 | 0      |
| 244 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?      | Done     | Done       | 0.9999979894222444 | 0      |
| 245 | Tensor<[1, 28, 28, 28]> self = ?,<br>Tensor<[1, 28, 28, 28]> other = ?        | Done     | Done       | 0.9999979576455374 | 0      |
| 246 | Tensor<[1, 288, 14, 14]> self = ?,<br>Tensor<[1, 288, 14, 14]> other = ?      | Done     | Done       | 0.9999979831563404 | 0      |
| 247 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?    | Done     | Done       | 0.999997992723832  | 0      |
| 248 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[1, 3, 16, 16, 2]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 249 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?      | Done     | Done       | 0.9999979803331238 | 0      |
| 250 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[1, 3, 32, 32, 2]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 251 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?      | Done     | Done       | 0.999997985958455  | 0      |
| 252 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[1, 3, 64, 64, 2]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 253 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?            | Done     | Done       | 0.9999979917741143 | 0      |
| 254 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?        | Done     | Done       | 0.9999979680280966 | 0      |
| 255 | Tensor<[1, 32, 112, 112]> self = ?,<br>Tensor<[1, 32, 112, 112]> other = ?    | Done     | Done       | 0.9999980032828468 | 0      |
| 256 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?    | Done     | Done       | 0.999997979643482  | 0      |
| 257 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?            | Done     | Done       | 0.9999979908355617 | 0      |
| 258 | Tensor<[1, 32, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Unknown    | N/A                | N/A    |
| 259 | Tensor<[1, 32, 24576]> self = ?,<br>Tensor<[1, 32, 24576]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
| 260 | Tensor<[1, 32, 256, 256]> self = ?,<br>Tensor<[1, 32, 256, 256]> other = ?    | Done     | Done       | 0.999997996308168  | 0      |
| 261 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ?        | Done     | Done       | 0.9999980090650035 | 0      |
| 262 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 32, 32, 128]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 263 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?      | Done     | Done       | 0.9999979888739157 | 0      |
| 264 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?      | Done     | Done       | 0.9999980020433007 | 0      |
| 265 | Tensor<[1, 32, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 266 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 267 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?        | Done     | Done       | 0.9999980625603475 | 0      |
| 268 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?        | Done     | Done       | 0.999998000830455  | 0      |
| 269 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.999994795550601  | 0      |
| 270 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999948345713635 | 0      |
| 271 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?        | Done     | Done       | 0.9999979813567563 | 0      |
| 272 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?        | Done     | Done       | 0.9999980041005838 | 0      |
| 273 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?        | Done     | Done       | 0.9999980018030363 | 0      |
| 274 | Tensor<[1, 32, s0, s1]> self = ?,<br>Tensor<[1, 32, s0, s1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 275 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?      | Done     | Done       | 0.9999979579610507 | 0      |
| 276 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979229957655 | 0      |
| 277 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?      | Unknown  | Done       | 0.99999798523891   | 0      |
| 278 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 279 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 280 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?      | Done     | Done       | 0.9999979787696662 | 0      |
| 281 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?      | Done     | Done       | 0.9999979986983123 | 0      |
| 282 | Tensor<[1, 34, 28, 28]> self = ?,<br>Tensor<[1, 34, 28, 28]> other = ?        | Done     | Done       | 0.99999809054934   | 0      |
| 283 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?        | Done     | Done       | 0.9999979967617102 | 0      |
| 284 | Tensor<[1, 36, 56, 56]> self = ?,<br>Tensor<[1, 36, 56, 56]> other = ?        | Done     | Done       | 0.9999980020291024 | 0      |
| 285 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?        | Done     | Done       | 0.9999979813496717 | 0      |
| 286 | Tensor<[1, 384, 35, 35]> self = ?,<br>Tensor<[1, 384, 35, 35]> other = ?      | Done     | Done       | 0.9999979901292311 | 0      |
| 287 | Tensor<[1, 384, 8, 8]> self = ?,<br>Tensor<[1, 384, 8, 8]> other = ?          | Done     | Done       | 0.9999979781955644 | 0      |
| 288 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 289 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 290 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 291 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 292 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?                | Unknown  | Done       | 0.9999978841578456 | 0      |
| 293 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?                   | Unknown  | Done       | 0.9999979639299601 | 0      |
| 294 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ?        | Done     | Done       | 0.999998066162409  | 0      |
| 295 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?        | Done     | Done       | 0.9999980047370639 | 0      |
| 296 | Tensor<[1, 40, 30, 30]> self = ?,<br>Tensor<[1, 40, 30, 30]> other = ?        | Done     | Done       | 0.9999979543606214 | 0      |
| 297 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?        | Done     | Done       | 0.9999980190277511 | 0      |
| 298 | Tensor<[1, 40, 56, 56]> self = ?,<br>Tensor<[1, 40, 56, 56]> other = ?        | Done     | Done       | 0.9999979541828756 | 0      |
| 299 | Tensor<[1, 400, 7, 7]> self = ?,<br>Tensor<[1, 400, 7, 7]> other = ?          | Done     | Done       | 0.9999980823330554 | 0      |
| 300 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ?      | Done     | Done       | 0.9999980399519074 | 0      |
| 301 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999980410544262 | 0      |
| 302 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?          | Unknown  | Done       | 0.9999979915757016 | 0      |
| 303 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?            | Done     | Done       | 0.9999979819505694 | 0      |
| 304 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ?      | Done     | Done       | 0.9999980099326984 | 0      |
| 305 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?          | Done     | Done       | 0.999997967539213  | 0      |
| 306 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?      | Done     | Done       | 0.9999979748825177 | 0      |
| 307 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999948811083088 | 0      |
| 308 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | 0.9999979816596822 | 0      |
| 309 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | 0.9999979214744772 | 0      |
| 310 | Tensor<[1, 46, 28, 28]> self = ?,<br>Tensor<[1, 46, 28, 28]> other = ?        | Done     | Done       | 0.9999979566946985 | 0      |
| 311 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ?        | Done     | Unknown    | N/A                | N/A    |
| 312 | Tensor<[1, 48, 33, 33]> self = ?,<br>Tensor<[1, 48, 33, 33]> other = ?        | Done     | Done       | 0.9999980379178333 | 0      |
| 313 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?        | Done     | Done       | 0.999997998778332  | 0      |
| 314 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?        | Done     | Done       | 0.9999979403619584 | 0      |
| 315 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?      | Done     | Done       | 0.9999979894905255 | 0      |
| 316 | Tensor<[1, 480, 7, 7]> self = ?,<br>Tensor<[1, 480, 7, 7]> other = ?          | Done     | Done       | 0.9999979661581191 | 0      |
| 317 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?          | Done     | Done       | 0.9999979784553598 | 0      |
| 318 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?              | Unknown  | Done       | 0.9999979041397601 | 0      |
| 319 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?          | Unknown  | Done       | 0.9999978451336308 | 0      |
| 320 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999944874845781 | 0      |
| 321 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?              | Unknown  | Done       | 0.9999980857232541 | 0      |
| 322 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?            | Done     | Done       | 0.9999980634508479 | 0      |
| 323 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?            | Done     | Done       | 0.9999979994176331 | 0      |
| 324 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?              | Done     | Done       | 0.9999980086915388 | 0      |
| 325 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Removed  | Done       | 1.0                | 0      |
| 326 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ?      | Done     | Done       | 0.9999980097196187 | 0      |
| 327 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979775004211 | 0      |
| 328 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?      | Done     | Done       | 0.9999979975574541 | 0      |
| 329 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?      | Done     | Done       | 0.9999979806755802 | 0      |
| 330 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999980036266956 | 0      |
| 331 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?          | Done     | Done       | 0.9999979901013196 | 0      |
| 332 | Tensor<[1, 512, 8, 8]> self = ?,<br>Tensor<[1, 512, 8, 8]> other = ?          | Done     | Done       | 0.9999979973557857 | 0      |
| 333 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999979805557772 | 0      |
| 334 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?    | Done     | Done       | 0.9999979887924482 | 0      |
| 335 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                      | Done     | Done       | 0.9999985099415322 | 0      |
| 336 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?      | Done     | Done       | 0.9999979931125998 | 0      |
| 337 | Tensor<[1, 56, 14, 14]> self = ?,<br>Tensor<[1, 56, 14, 14]> other = ?        | Done     | Done       | 0.9999979702107087 | 0      |
| 338 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?        | Done     | Done       | 0.9999980331962744 | 0      |
| 339 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?      | Done     | Done       | 0.9999979949550135 | 0      |
| 340 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?        | Done     | Done       | 0.9999979974766595 | 0      |
| 341 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?      | Done     | Done       | 0.9999979979497924 | 0      |
| 342 | Tensor<[1, 58, 28, 28]> self = ?,<br>Tensor<[1, 58, 28, 28]> other = ?        | Done     | Done       | 0.999998017391143  | 0      |
| 343 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Unknown  | Done       | 0.9999979515838351 | 0      |
| 344 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Unknown  | Done       | 0.9999859684070155 | 0      |
| 345 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?            | Unknown  | Done       | 0.9999975096835934 | 0      |
| 346 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?            | Unknown  | Done       | 0.999997681879288  | 0      |
| 347 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | Done       | 0.9999982203573844 | 0      |
| 348 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?            | Unknown  | Done       | 0.9999986097299634 | 0      |
| 349 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 350 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 351 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999982672923331 | 0      |
| 352 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?              | Unknown  | Done       | 0.9999991230483302 | 0      |
| 353 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 354 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 355 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?           | Unknown  | Done       | 0.9999979811119386 | 0      |
| 356 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?          | Unknown  | Done       | 0.9999978913932909 | 0      |
| 357 | Tensor<[1, 60, 28, 28]> self = ?,<br>Tensor<[1, 60, 28, 28]> other = ?        | Done     | Done       | 0.9999979545520947 | 0      |
| 358 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                       | Removed  | Done       | 1.0                | 0      |
| 359 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?    | Done     | Done       | 0.9999979971746777 | 0      |
| 360 | Tensor<[1, 64, 128, 128]> self = ?,<br>Tensor<[1, 64, 128, 128]> other = ?    | Done     | Done       | 0.9999979848544055 | 0      |
| 361 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ?        | Done     | Done       | 0.9999979529782244 | 0      |
| 362 | Tensor<[1, 64, 147, 147]> self = ?,<br>Tensor<[1, 64, 147, 147]> other = ?    | Done     | Done       | 0.9999980007591337 | 0      |
| 363 | Tensor<[1, 64, 150, 150]> self = ?,<br>Tensor<[1, 64, 150, 150]> other = ?    | Done     | Done       | 0.9999980020718272 | 0      |
| 364 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999978832413863 | 0      |
| 365 | Tensor<[1, 64, 224, 224]> self = ?,<br>Tensor<[1, 64, 224, 224]> other = ?    | Done     | Done       | 0.9999979971607665 | 0      |
| 366 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?    | Done     | Done       | 0.9999979878838061 | 0      |
| 367 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?    | Done     | Done       | 0.9999979943015052 | 0      |
| 368 | Tensor<[1, 64, 28, 28]> self = ?,<br>Tensor<[1, 64, 28, 28]> other = ?        | Done     | Done       | 0.999998000560391  | 0      |
| 369 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 370 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 371 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?        | Done     | Done       | 0.9999980020338747 | 0      |
| 372 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999979464386086 | 0      |
| 373 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 374 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 375 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?    | Done     | Done       | 0.9999979945709124 | 0      |
| 376 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?        | Done     | Done       | 0.9999979861711344 | 0      |
| 377 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?        | Done     | Done       | 0.999998003503428  | 0      |
| 378 | Tensor<[1, 64, 6144]> self = ?,<br>Tensor<[1, 64, 6144]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 379 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?      | Done     | Done       | 0.9999979735165315 | 0      |
| 380 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?        | Done     | Done       | 0.9999980029356751 | 0      |
| 381 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?        | Done     | Done       | 0.9999979756053379 | 0      |
| 382 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Removed  | Done       | 0.9999979152931233 | 0      |
| 383 | Tensor<[1, 64, s1, s2]> self = ?,<br>Tensor<[1, 64, s1, s2]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 384 | Tensor<[1, 640, 7, 7]> self = ?,<br>Tensor<[1, 640, 7, 7]> other = ?          | Done     | Done       | 0.999997969442875  | 0      |
| 385 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 386 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, s0, s1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 387 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 388 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 389 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?      | Done     | Done       | 0.9999979891285593 | 0      |
| 390 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?      | Done     | Done       | 0.9999979950886406 | 0      |
| 391 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?          | Done     | Done       | 0.9999979218765993 | 0      |
| 392 | Tensor<[1, 68, 14, 14]> self = ?,<br>Tensor<[1, 68, 14, 14]> other = ?        | Done     | Done       | 0.9999980880906045 | 0      |
| 393 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?      | Done     | Done       | 0.999997992469762  | 0      |
| 394 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947364772503 | 0      |
| 395 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?              | Done     | Done       | 0.9999979383814106 | 0      |
| 396 | Tensor<[1, 7, 4544]> self = ?,<br>Tensor<[1, 7, 4544]> other = ?              | Unknown  | Unknown    | N/A                | N/A    |
| 397 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?        | Done     | Done       | 0.9999979962136774 | 0      |
| 398 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?          | Done     | Done       | 0.9999978962481714 | 0      |
| 399 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?                | Done     | Done       | 0.999997918694316  | 0      |
| 400 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
| 401 | Tensor<[1, 71, 7, 7]> self = ?,<br>Tensor<[7, 7]> other = ?                   | Unknown  | Unknown    | N/A                | N/A    |
| 402 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?        | Done     | Done       | 0.9999979651854182 | 0      |
| 403 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?        | Done     | Done       | 0.9999979836336909 | 0      |
| 404 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?        | Done     | Done       | 0.9999979744209627 | 0      |
| 405 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ?      | Done     | Done       | 0.999998010460832  | 0      |
| 406 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?      | Done     | Done       | 0.9999979862575046 | 0      |
| 407 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?      | Done     | Done       | 0.9999979995163135 | 0      |
| 408 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?    | Done     | Done       | 0.9999979983084075 | 0      |
| 409 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?      | Done     | Done       | 0.9999979921715455 | 0      |
| 410 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 768, 16, 16]> other = ?      | Done     | Unknown    | N/A                | N/A    |
| 411 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                    | Done     | Done       | 0.9999979423884942 | 0      |
| 412 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?          | Done     | Done       | 0.9999979685550884 | 0      |
| 413 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                      | Done     | Done       | 0.9999978138634023 | 0      |
| 414 | Tensor<[1, 78, 28, 28]> self = ?,<br>Tensor<[1, 78, 28, 28]> other = ?        | Done     | Done       | 0.9999980048591751 | 0      |
| 415 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?          | Done     | Done       | 0.9999979506256839 | 0      |
| 416 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?            | Unknown  | Done       | 0.999997972072177  | 0      |
| 417 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?            | Unknown  | Done       | 0.9999988805576103 | 0      |
| 418 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999995074592053 | 0      |
| 419 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?              | Unknown  | Done       | 0.9999972184562125 | 0      |
| 420 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999979611282657 | 0      |
| 421 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?              | Unknown  | Done       | 0.9999989758428266 | 0      |
| 422 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 423 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 424 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999981079486201 | 0      |
| 425 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?          | Unknown  | Done       | 0.9999982250237532 | 0      |
| 426 | Tensor<[1, 8, 112, 112]> self = ?,<br>Tensor<[1, 8, 112, 112]> other = ?      | Done     | Done       | 0.9999980278322635 | 0      |
| 427 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ?      | Removed  | Done       | 0.9999979935168803 | 0      |
| 428 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?                | Unknown  | Done       | 0.9999980011826556 | 0      |
| 429 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?        | Done     | Done       | 0.9999980118923243 | 0      |
| 430 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?          | Done     | Done       | 0.9999979784885307 | 0      |
| 431 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?        | Done     | Done       | 0.9999977081015088 | 0      |
| 432 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?        | Done     | Done       | 0.9999979357309177 | 0      |
| 433 | Tensor<[1, 80, 15, 15]> self = ?,<br>Tensor<[1, 80, 15, 15]> other = ?        | Done     | Done       | 0.9999980026722348 | 0      |
| 434 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?        | Done     | Done       | 0.9999980004013453 | 0      |
| 435 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?        | Done     | Done       | 0.9999980177261367 | 0      |
| 436 | Tensor<[1, 80, 7, 7]> self = ?,<br>Tensor<[1, 80, 7, 7]> other = ?            | Done     | Done       | 0.9999980998815544 | 0      |
| 437 | Tensor<[1, 88, 17, 17]> self = ?,<br>Tensor<[1, 88, 17, 17]> other = ?        | Done     | Done       | 0.9999980010829255 | 0      |
| 438 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?          | Done     | Done       | 0.9999979848861219 | 0      |
| 439 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?      | Done     | Done       | 0.9999979719334035 | 0      |
| 440 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?              | Done     | Done       | 0.999997994828964  | 0      |
| 441 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                           | Done     | Done       | 0.9999951704169521 | 0      |
| 442 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                | Done     | Done       | 0.9999975493398237 | 0      |
| 443 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947946636066 | 0      |
| 444 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?            | Done     | Done       | 0.9999979854262    | 0      |
| 445 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?              | Done     | Done       | 0.9999979706555523 | 0      |
| 446 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999948777285518 | 0      |
| 447 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?              | Done     | Done       | 0.999997974290025  | 0      |
| 448 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999948029976309 | 0      |
| 449 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?              | Done     | Done       | 0.9999980082223777 | 0      |
| 450 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?                | Done     | Done       | 0.9999981026960474 | 0      |
| 451 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947119260838 | 0      |
| 452 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?              | Done     | Done       | 0.9999980101653602 | 0      |
| 453 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?          | Done     | Done       | 0.9999979926300645 | 0      |
| 454 | Tensor<[1, 92, 14, 14]> self = ?,<br>Tensor<[1, 92, 14, 14]> other = ?        | Done     | Done       | 0.9999980717635983 | 0      |
| 455 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?        | Done     | Done       | 0.9999979884759962 | 0      |
| 456 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?        | Done     | Done       | 0.9999980566318719 | 0      |
| 457 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?        | Done     | Done       | 0.9999979853629343 | 0      |
| 458 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?            | Done     | Unknown    | N/A                | N/A    |
| 459 | Tensor<[1, 96, 80]> self = ?,<br>Tensor<[1, 96, 80]> other = ?                | Unknown  | Unknown    | N/A                | N/A    |
| 460 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?          | Done     | Done       | 0.9999979912976115 | 0      |
| 461 | Tensor<[1, 98, 28, 28]> self = ?,<br>Tensor<[1, 98, 28, 28]> other = ?        | Done     | Done       | 0.9999980099249544 | 0      |
| 462 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor<[1, s0*s1, 1280]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 463 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor<[1, s0*s1, 640]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 464 | Tensor<[1, s0, 768]> self = ?,<br>Tensor<[1, s0, 768]> other = ?              | Unknown  | Unknown    | N/A                | N/A    |
| 465 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 466 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor<[1, s1*s2, 320]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 467 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor<[1, s1*s2, 640]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 468 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 469 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.999884568908813  | 0      |
| 470 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                      | Unknown  | Done       | 0.9999978519272601 | 0      |
| 471 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?            | Done     | Done       | 0.9999979069986344 | 0      |
| 472 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?              | Unknown  | Done       | 0.9999978958328003 | 0      |
| 473 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 474 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.9998958423623622 | 0      |
| 475 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                      | Unknown  | Done       | 0.9999984990651071 | 0      |
| 476 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?         | Done     | Done       | 0.9999980014711033 | 0      |
| 477 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?         | Done     | Done       | 0.9999979935228698 | 0      |
| 478 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?         | Done     | Done       | 0.9999980133802986 | 0      |
| 479 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?         | Done     | Done       | 0.9999979829804829 | 0      |
| 480 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1e-06                          | Done     | Unknown    | N/A                | N/A    |
| 481 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 1]> other = ?                  | Done     | Unknown    | N/A                | N/A    |
| 482 | Tensor<[16384, 2, 2]> self = ?,<br>Tensor<[1, 2, 2]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 483 | Tensor<[16384, 2]> self = ?,<br>Tensor<[16384, 1]> other = ?                  | Done     | Unknown    | N/A                | N/A    |
| 484 | Tensor<[16384, 3, 25]> self = ?,<br>Tensor<[16384, 3, 25]> other = ?          | Done     | Unknown    | N/A                | N/A    |
| 485 | Tensor<[16384, 3, 3]> self = ?,<br>Tensor<[16384, 3, 3]> other = ?            | Done     | Unknown    | N/A                | N/A    |
| 486 | Tensor<[16384, 3]> self = ?,<br>Tensor other = 0.5                            | Done     | Unknown    | N/A                | N/A    |
| 487 | Tensor<[16384, 3]> self = ?,<br>Tensor<[1, 3]> other = ?                      | Done     | Unknown    | N/A                | N/A    |
| 488 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 3]> other = ?                  | Done     | Unknown    | N/A                | N/A    |
| 489 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 4]> other = ?                  | Done     | Unknown    | N/A                | N/A    |
| 490 | Tensor<[16384]> self = ?,<br>Tensor other = 1                                 | Done     | Unknown    | N/A                | N/A    |
| 491 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?                        | Done     | Unknown    | N/A                | N/A    |
| 492 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 493 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 0.9997278029736545 | 0      |
| 494 | Tensor<[2*s0]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 495 | Tensor<[2*s1]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 496 | Tensor<[2*s2]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 497 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                | 0      |
| 498 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 499 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                      | Done     | Done       | 0.9999979240008341 | 0      |
| 500 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?              | Done     | Done       | 0.9999979252316418 | 0      |
| 501 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?                | Done     | Done       | 0.9999979324997742 | 0      |
| 502 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?                | Done     | Done       | 0.9999977593806564 | 0      |
| 503 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?              | Done     | Done       | 0.9999984904218592 | 0      |
| 504 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                      | Removed  | Done       | 0.999998063217789  | 0      |
| 505 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                              | Unknown  | Done       | 0.9644045618684314 | 0      |
| 506 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                    | Done     | Unknown    | N/A                | N/A    |
| 507 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                    | Done     | Done       | 0.9999981221862659 | 0      |
| 508 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                          | Done     | Unknown    | N/A                | N/A    |
| 509 | Tensor<[4, 1024, 14, 14]> self = ?,<br>Tensor<[4, 1024, 14, 14]> other = ?    | Done     | Unknown    | N/A                | N/A    |
| 510 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?        | Done     | Done       | 0.9999980219886813 | 0      |
| 511 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?        | Done     | Done       | 0.9999979818512097 | 0      |
| 512 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?        | Done     | Done       | 0.9999980219316623 | 0      |
| 513 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?        | Done     | Done       | 0.9999979894199578 | 0      |
| 514 | Tensor<[4, 2048, 7, 7]> self = ?,<br>Tensor<[4, 2048, 7, 7]> other = ?        | Done     | Unknown    | N/A                | N/A    |
| 515 | Tensor<[4, 256, 56, 56]> self = ?,<br>Tensor<[4, 256, 56, 56]> other = ?      | Done     | Unknown    | N/A                | N/A    |
| 516 | Tensor<[4, 512, 28, 28]> self = ?,<br>Tensor<[4, 512, 28, 28]> other = ?      | Done     | Unknown    | N/A                | N/A    |
| 517 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Unknown  | Done       | 0.9999979984491366 | 0      |
| 518 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?         | Done     | Done       | 0.9999979812474796 | 0      |
| 519 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?         | Done     | Done       | 0.9999979897295261 | 0      |
| 520 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?         | Done     | Done       | 0.999997991473191  | 0      |
| 521 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?         | Done     | Done       | 0.9999979953265391 | 0      |
| 522 | Tensor<[8, 16, 384, 384]> self = ?,<br>Tensor<[8, 1, 1, 384]> other = ?       | Removed  | Unknown    | N/A                | N/A    |
| 523 | Tensor<[8, 384, 1024]> self = ?,<br>Tensor<[1, 384, 1024]> other = ?          | Done     | Unknown    | N/A                | N/A    |
| 524 | Tensor<[8, 384, 1024]> self = ?,<br>Tensor<[8, 384, 1024]> other = ?          | Done     | Unknown    | N/A                | N/A    |
| 525 | Tensor<[813, 4]> self = ?,<br>Tensor<[813, 1]> other = ?                      | Done     | Unknown    | N/A                | N/A    |
| 526 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                    | Done     | Unknown    | N/A                | N/A    |
| 527 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                    | Done     | Done       | 0.9999979316713838 | 0      |
| 528 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                          | Done     | Unknown    | N/A                | N/A    |
| 529 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.9999980201483426 | 0      |
| 530 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?            | Done     | Done       | 0.9999980121220919 | 0      |
| 531 | Tensor<[]> self = ?,<br>Tensor other = 1                                      | Done     | Done       | 1.0                | 0      |
| 532 | Tensor<[]> self = ?,<br>Tensor other = ?                                      | Done     | Unknown    | N/A                | N/A    |
| 533 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                        | Unknown  | Unknown    | N/A                | N/A    |
| 534 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |

