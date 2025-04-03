### aten.add.Tensor
|     | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|----:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -6.0                        | Done     | Unknown    | N/A                | N/A    |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1                           | Done     | Unknown    | N/A                | N/A    |
|   2 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.0                         | Done     | Unknown    | N/A                | N/A    |
|   3 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 2                           | Done     | Unknown    | N/A                | N/A    |
|   4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999619988218732 | 0      |
|   5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999932739010536 | 0      |
|   6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999946141551783 | 0      |
|   7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999920961162538 | 0      |
|   8 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999952239835618 | 0      |
|   9 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999981157047451 | 0      |
|  10 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Unknown    | N/A                | N/A    |
|  11 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                           | Done     | Unknown    | N/A                | N/A    |
|  12 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Unknown    | N/A                | N/A    |
|  13 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2                           | Done     | Unknown    | N/A                | N/A    |
|  14 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?          | Unknown  | Done       | 0.9999984841428573 | 0      |
|  15 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839              | Done     | Done       | 1.0                | 0      |
|  16 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9043478220701218              | Done     | Done       | 1.0                | 0      |
|  17 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9086956530809402              | Done     | Done       | 1.0                | 0      |
|  18 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9090909063816071              | Done     | Done       | 1.0                | 0      |
|  19 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9130434766411781              | Done     | Done       | 1.0                | 0      |
|  20 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032              | Done     | Done       | 1.0                | 0      |
|  21 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.917391300201416               | Done     | Done       | 1.0                | 0      |
|  22 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9181818142533302              | Done     | Done       | 1.0                | 0      |
|  23 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9217391312122345              | Done     | Done       | 1.0                | 0      |
|  24 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9260869547724724              | Done     | Done       | 1.0                | 0      |
|  25 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9272727221250534              | Done     | Done       | 1.0                | 0      |
|  26 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226              | Done     | Done       | 1.0                | 0      |
|  27 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9304347857832909              | Done     | Done       | 1.0                | 0      |
|  28 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9347826093435287              | Done     | Done       | 1.0                | 0      |
|  29 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9363636374473572              | Done     | Done       | 1.0                | 0      |
|  30 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9391304366290569              | Done     | Done       | 1.0                | 0      |
|  31 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323              | Done     | Done       | 1.0                | 0      |
|  32 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9434782639145851              | Done     | Done       | 1.0                | 0      |
|  33 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.94545454159379                | Done     | Done       | 1.0                | 0      |
|  34 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.947826087474823               | Done     | Done       | 1.0                | 0      |
|  35 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9521739110350609              | Done     | Done       | 1.0                | 0      |
|  36 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9545454569160938              | Done     | Done       | 1.0                | 0      |
|  37 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9565217345952988              | Done     | Done       | 1.0                | 0      |
|  38 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516              | Done     | Done       | 1.0                | 0      |
|  39 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.960869561880827               | Done     | Done       | 1.0                | 0      |
|  40 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.963636364787817               | Done     | Done       | 1.0                | 0      |
|  41 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9652173891663551              | Done     | Done       | 1.0                | 0      |
|  42 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9695652164518833              | Done     | Done       | 1.0                | 0      |
|  43 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161              | Done     | Done       | 1.0                | 0      |
|  44 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9727272726595402              | Done     | Done       | 1.0                | 0      |
|  45 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9739130418747663              | Done     | Done       | 1.0                | 0      |
|  46 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9782608672976494              | Done     | Done       | 1.0                | 0      |
|  47 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9818181823939085              | Done     | Done       | 1.0                | 0      |
|  48 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9826086945831776              | Done     | Done       | 1.0                | 0      |
|  49 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581              | Done     | Done       | 1.0                | 0      |
|  50 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9869565209373832              | Done     | Done       | 1.0                | 0      |
|  51 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9909090911969543              | Done     | Done       | 1.0                | 0      |
|  52 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9913043472915888              | Done     | Done       | 1.0                | 0      |
|  53 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9956521736457944              | Done     | Done       | 1.0                | 0      |
|  54 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                           | Unknown  | Done       | 1.0                | 0      |
|  55 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027    | Done     | Done       | 0.9999999963139996 | 0      |
|  56 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997     | Done     | Done       | 0.9999990434223498 | 0      |
|  57 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994     | Done     | Done       | 0.9999998634512991 | 0      |
|  58 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999952155525241 | 0      |
|  59 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | 0.9999978710236238 | 0      |
|  60 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9998800630646353 | 0      |
|  61 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999895933293123 | 0      |
|  62 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999960496066613 | 0      |
|  63 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999977196241456 | 0      |
|  64 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999950350283955 | 0      |
|  65 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?              | Unknown  | Done       | 0.9999979232634082 | 0      |
|  66 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
|  67 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                | Unknown  | Done       | 0.9999979035599547 | 0      |
|  68 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Unknown  | Done       | 0.9999978024431655 | 0      |
|  69 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                   | Unknown  | Done       | 0.999998115860838  | 0      |
|  70 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?            | Unknown  | Done       | 0.9999978722255191 | 0      |
|  71 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
|  72 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?              | Unknown  | Done       | 0.9999979785915502 | 0      |
|  73 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?              | Done     | Done       | 0.9999979446706532 | 0      |
|  74 | Tensor<[1, 100, 14, 14]> self = ?,<br>Tensor<[1, 100, 14, 14]> other = ?      | Done     | Done       | 0.9999980975999683 | 0      |
|  75 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?        | Done     | Done       | 0.9999979683525483 | 0      |
|  76 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1.0                | 0      |
|  77 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Unknown  | Done       | 1.0                | 0      |
|  78 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ?    | Done     | Done       | 0.9999979826348143 | 0      |
|  79 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ?    | Done     | Done       | 0.9999980164492621 | 0      |
|  80 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?    | Done     | Done       | 0.9999979815438172 | 0      |
|  81 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?          | Done     | Done       | 0.999997982703628  | 0      |
|  82 | Tensor<[1, 1024, 17, 17]> self = ?,<br>Tensor<[1, 1024, 17, 17]> other = ?    | Done     | Done       | 0.9999980002780892 | 0      |
|  83 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999980447955107 | 0      |
|  84 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Unknown  | Done       | 0.9999979989784229 | 0      |
|  85 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?    | Unknown  | Done       | 0.9999979915886309 | 0      |
|  86 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999979980431591 | 0      |
|  87 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?    | Done     | Done       | 0.9999979988948184 | 0      |
|  88 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?        | Done     | Done       | 0.9999979807322711 | 0      |
|  89 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999976141575886 | 0      |
|  90 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?      | Done     | Done       | 0.9999979791121145 | 0      |
|  91 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?    | Done     | Done       | 0.999997987720841  | 0      |
|  92 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                                 | Done     | Done       | 1.0                | 0      |
|  93 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | 0.9999930479937996 | 0      |
|  94 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?      | Done     | Done       | 0.9999980339509573 | 0      |
|  95 | Tensor<[1, 112, 15, 15]> self = ?,<br>Tensor<[1, 112, 15, 15]> other = ?      | Done     | Done       | 0.9999980812416644 | 0      |
|  96 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?      | Done     | Done       | 0.9999980173642544 | 0      |
|  97 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ?      | Done     | Done       | 0.9999979884014909 | 0      |
|  98 | Tensor<[1, 116, 14, 14]> self = ?,<br>Tensor<[1, 116, 14, 14]> other = ?      | Done     | Done       | 0.9999980350366963 | 0      |
|  99 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999985612857191 | 0      |
| 100 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?          | Unknown  | Done       | 0.9999970605211084 | 0      |
| 101 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 1.0                | 0      |
| 102 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?            | Unknown  | Done       | 0.9999996741418041 | 0      |
| 103 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 1.0                | 0      |
| 104 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?            | Unknown  | Done       | 0.9999978180929797 | 0      |
| 105 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | 0.9999981342195429 | 0      |
| 106 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 107 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 108 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 109 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Done     | Done       | 0.9999982861319874 | 0      |
| 110 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?        | Unknown  | Done       | 0.9999982453154882 | 0      |
| 111 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ?          | Done     | Done       | 0.9999980622474001 | 0      |
| 112 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?              | Done     | Done       | 0.999998068525296  | 0      |
| 113 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<[1, 1, 1, 14]> other = ?          | Done     | Done       | 0.9999979499972006 | 0      |
| 114 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ?    | Done     | Done       | 0.9999980039312156 | 0      |
| 115 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?         | Done     | Done       | 0.9999978835471708 | 0      |
| 116 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ?          | Done     | Done       | 0.9999978978700225 | 0      |
| 117 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999946805266087 | 0      |
| 118 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?            | Done     | Done       | 0.9999979613054993 | 0      |
| 119 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | 0.9999978897390345 | 0      |
| 120 | Tensor<[1, 12, 56, 56]> self = ?,<br>Tensor<[1, 12, 56, 56]> other = ?        | Done     | Done       | 0.999998013763949  | 0      |
| 121 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ?             | Done     | Done       | 0.999997471471246  | 0      |
| 122 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?              | Done     | Done       | 0.9999979604514555 | 0      |
| 123 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999966747541136 | 0      |
| 124 | Tensor<[1, 120, 17, 17]> self = ?,<br>Tensor<[1, 120, 17, 17]> other = ?      | Done     | Done       | 0.9999980051974299 | 0      |
| 125 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?      | Done     | Done       | 0.9999979223150044 | 0      |
| 126 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?          | Done     | Done       | 0.9999979741349468 | 0      |
| 127 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?    | Done     | Done       | 0.999997968083718  | 0      |
| 128 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                | 0      |
| 129 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Unknown  | Done       | 1.0                | 0      |
| 130 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999978996956226 | 0      |
| 131 | Tensor<[1, 128, 112, 112]> self = ?,<br>Tensor<[1, 128, 112, 112]> other = ?  | Done     | Done       | 0.9999979937168418 | 0      |
| 132 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ?  | Done     | Done       | 0.9999979807337406 | 0      |
| 133 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Unknown  | Done       | 0.9999979929213777 | 0      |
| 134 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.999998110229938  | 0      |
| 135 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ?      | Done     | Done       | 0.9999979594087517 | 0      |
| 136 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ?      | Done     | Done       | 0.999997994769499  | 0      |
| 137 | Tensor<[1, 128, 64, 64]> self = ?,<br>Tensor<[1, 128, 64, 64]> other = ?      | Done     | Done       | 0.9999979934864414 | 0      |
| 138 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?      | Done     | Done       | 0.9999979943076803 | 0      |
| 139 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Unknown  | Done       | 0.9999979611071957 | 0      |
| 140 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?        | Unknown  | Done       | 0.9999980040074833 | 0      |
| 141 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?        | Unknown  | Done       | 0.9999979932693868 | 0      |
| 142 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 143 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, s0, s1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 144 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 145 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, s1, s2]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 146 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ?    | Done     | Done       | 0.9999980155597334 | 0      |
| 147 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ?      | Done     | Done       | 0.9999979987219315 | 0      |
| 148 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?        | Done     | Done       | 0.9999979906835283 | 0      |
| 149 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?    | Done     | Done       | 0.9999979979584757 | 0      |
| 150 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?              | Done     | Done       | 0.9999982532220918 | 0      |
| 151 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?      | Done     | Done       | 0.9999979900167717 | 0      |
| 152 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?      | Done     | Done       | 0.9999979859883151 | 0      |
| 153 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999948311520989 | 0      |
| 154 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?            | Done     | Done       | 0.9999980393289574 | 0      |
| 155 | Tensor<[1, 14, 56, 56]> self = ?,<br>Tensor<[1, 14, 56, 56]> other = ?        | Done     | Done       | 0.9999979820196334 | 0      |
| 156 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?              | Done     | Done       | 0.9999980464408411 | 0      |
| 157 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?      | Done     | Done       | 0.9999980163129419 | 0      |
| 158 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?          | Done     | Done       | 0.9999978944898584 | 0      |
| 159 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?          | Done     | Done       | 0.99999799157322   | 0      |
| 160 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999949635611759 | 0      |
| 161 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Unknown  | Done       | 0.9999980857262801 | 0      |
| 162 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
| 163 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?              | Unknown  | Done       | 0.9999979345907964 | 0      |
| 164 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ?          | Unknown  | Done       | 0.9999980036605953 | 0      |
| 165 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?             | Unknown  | Done       | 0.9999979963117467 | 0      |
| 166 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?        | Done     | Done       | 0.9999979778210017 | 0      |
| 167 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Tensor<[1, 1536, 8, 8]> other = ?        | Done     | Done       | 0.999997981694691  | 0      |
| 168 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999990773017653 | 0      |
| 169 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?          | Unknown  | Done       | 0.9999989578352979 | 0      |
| 170 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999936440489762 | 0      |
| 171 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?            | Unknown  | Done       | 0.9999975108558734 | 0      |
| 172 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999971410428903 | 0      |
| 173 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?            | Unknown  | Done       | 0.999999421073404  | 0      |
| 174 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999975199236196 | 0      |
| 175 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Done       | 0.9999983802824824 | 0      |
| 176 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 177 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 178 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 179 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.9999983357206718 | 0      |
| 180 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?        | Unknown  | Done       | 0.9999979939583211 | 0      |
| 181 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ?    | Done     | Done       | 0.9999980299867561 | 0      |
| 182 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?      | Done     | Done       | 0.9999980215896127 | 0      |
| 183 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?      | Done     | Done       | 0.9999979875638981 | 0      |
| 184 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ?    | Done     | Done       | 0.9999979858496614 | 0      |
| 185 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> other = ?         | Done     | Done       | 0.9999979765978508 | 0      |
| 186 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ?    | Done     | Done       | 0.9999979925282488 | 0      |
| 187 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor<[1, 1, 1, 256]> other = ?       | Done     | Done       | 0.9999979621195675 | 0      |
| 188 | Tensor<[1, 16, 28, 28]> self = ?,<br>Tensor<[1, 16, 28, 28]> other = ?        | Done     | Done       | 0.9999980341145168 | 0      |
| 189 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Done       | 0.9999975789972689 | 0      |
| 190 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Unknown  | Done       | 0.9999979960558615 | 0      |
| 191 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 192 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 193 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?              | Done     | Done       | 0.9999979703986607 | 0      |
| 194 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 195 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 196 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999977253156076 | 0      |
| 197 | Tensor<[1, 160, 14, 14]> self = ?,<br>Tensor<[1, 160, 14, 14]> other = ?      | Done     | Done       | 0.999997979151478  | 0      |
| 198 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ?      | Done     | Done       | 0.9999979815061769 | 0      |
| 199 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ?      | Done     | Done       | 0.9999979922354483 | 0      |
| 200 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?      | Done     | Done       | 0.9999979873687788 | 0      |
| 201 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?          | Done     | Done       | 0.9999980120985837 | 0      |
| 202 | Tensor<[1, 160, 73, 73]> self = ?,<br>Tensor<[1, 160, 73, 73]> other = ?      | Done     | Done       | 0.9999980037115181 | 0      |
| 203 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999980210425914 | 0      |
| 204 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?          | Done     | Done       | 0.9999979926460839 | 0      |
| 205 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ?      | Done     | Done       | 0.9999979854425463 | 0      |
| 206 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?        | Done     | Done       | 0.9999979843315179 | 0      |
| 207 | Tensor<[1, 185, 28, 28]> self = ?,<br>Tensor<[1, 185, 28, 28]> other = ?      | Done     | Done       | 0.9999979870253619 | 0      |
| 208 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ?            | Done     | Done       | 0.9999979322256279 | 0      |
| 209 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ?      | Done     | Done       | 0.9999980136484509 | 0      |
| 210 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ?      | Done     | Done       | 0.9999980065570686 | 0      |
| 211 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?      | Done     | Done       | 0.9999979886005684 | 0      |
| 212 | Tensor<[1, 192, 7, 7]> self = ?,<br>Tensor<[1, 192, 7, 7]> other = ?          | Done     | Done       | 0.9999981199671986 | 0      |
| 213 | Tensor<[1, 192, 71, 71]> self = ?,<br>Tensor<[1, 192, 71, 71]> other = ?      | Done     | Done       | 0.999997989030768  | 0      |
| 214 | Tensor<[1, 192, 8, 8]> self = ?,<br>Tensor<[1, 192, 8, 8]> other = ?          | Done     | Done       | 0.9999979246869359 | 0      |
| 215 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?        | Done     | Done       | 0.9999979772018844 | 0      |
| 216 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?          | Done     | Done       | 0.9999980046821669 | 0      |
| 217 | Tensor<[1, 196, 14, 14]> self = ?,<br>Tensor<[1, 196, 14, 14]> other = ?      | Done     | Done       | 0.9999979755060358 | 0      |
| 218 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ?            | Done     | Done       | 0.9999979848010929 | 0      |
| 219 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?          | Done     | Done       | 0.9999979833137732 | 0      |
| 220 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?            | Done     | Done       | 0.9999979807309863 | 0      |
| 221 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                | 0      |
| 222 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 223 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Done       | 1.0                | 0      |
| 224 | Tensor<[1, 20, 28, 28]> self = ?,<br>Tensor<[1, 20, 28, 28]> other = ?        | Done     | Done       | 0.9999980087616589 | 0      |
| 225 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?        | Done     | Done       | 0.9999979738339404 | 0      |
| 226 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1.0                | 0      |
| 227 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Unknown  | Done       | 1.0                | 0      |
| 228 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Unknown  | Done       | 0.9999979879328555 | 0      |
| 229 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?    | Unknown  | Done       | 0.9999979955559369 | 0      |
| 230 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999979995999946 | 0      |
| 231 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?    | Done     | Done       | 0.9999979958689114 | 0      |
| 232 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?        | Done     | Done       | 0.9999980224832328 | 0      |
| 233 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?          | Done     | Done       | 0.9999979889024385 | 0      |
| 234 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?             | Done     | Done       | 0.9999979922877303 | 0      |
| 235 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?      | Done     | Done       | 0.999997918446588  | 0      |
| 236 | Tensor<[1, 208, 9, 9]> self = ?,<br>Tensor<[1, 208, 9, 9]> other = ?          | Done     | Done       | 0.9999979842206413 | 0      |
| 237 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?      | Done     | Done       | 0.999997972860337  | 0      |
| 238 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?      | Done     | Done       | 0.9999980015469804 | 0      |
| 239 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?          | Done     | Done       | 0.999997984483411  | 0      |
| 240 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
| 241 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ?      | Done     | Done       | 0.999998017612237  | 0      |
| 242 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?      | Done     | Done       | 0.9999979900621585 | 0      |
| 243 | Tensor<[1, 24, 112, 112]> self = ?,<br>Tensor<[1, 24, 112, 112]> other = ?    | Done     | Done       | 0.9999980236088855 | 0      |
| 244 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?        | Done     | Done       | 0.9999979648966998 | 0      |
| 245 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?        | Done     | Done       | 0.9999980164451886 | 0      |
| 246 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?        | Done     | Done       | 0.9999979989068476 | 0      |
| 247 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?        | Done     | Done       | 0.9999979315773636 | 0      |
| 248 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?        | Done     | Done       | 0.9999979822385384 | 0      |
| 249 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?        | Done     | Done       | 0.9999980102679408 | 0      |
| 250 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?              | Done     | Done       | 0.9999979678805394 | 0      |
| 251 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?        | Done     | Done       | 0.9999980063326477 | 0      |
| 252 | Tensor<[1, 240, 14, 14]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?      | Done     | Done       | 0.9999980057362875 | 0      |
| 253 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?      | Done     | Done       | 0.9999980447566351 | 0      |
| 254 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?              | Done     | Done       | 0.9999979971604118 | 0      |
| 255 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?        | Done     | Done       | 0.9999979888582501 | 0      |
| 256 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                | 0      |
| 257 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Unknown  | Done       | 1.0                | 0      |
| 258 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979266700166 | 0      |
| 259 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ?  | Done     | Done       | 0.9999979886293077 | 0      |
| 260 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?          | Done     | Done       | 0.9999979799850907 | 0      |
| 261 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ?  | Done     | Done       | 0.9999979955407027 | 0      |
| 262 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?          | Done     | Done       | 0.999998001586008  | 0      |
| 263 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ?      | Done     | Done       | 0.9999979764512641 | 0      |
| 264 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?      | Done     | Done       | 0.9999980036390392 | 0      |
| 265 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?            | Done     | Done       | 0.9999979579391133 | 0      |
| 266 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Unknown  | Done       | 0.999997975809388  | 0      |
| 267 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ?  | Unknown  | Done       | 0.9999979934517113 | 0      |
| 268 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.999998020586961  | 0      |
| 269 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ?  | Done     | Done       | 0.9999979908050189 | 0      |
| 270 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?            | Done     | Done       | 0.999997915017752  | 0      |
| 271 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.99999788795465   | 0      |
| 272 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ?      | Done     | Done       | 0.9999979974500499 | 0      |
| 273 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?      | Done     | Done       | 0.9999979695762862 | 0      |
| 274 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?              | Done     | Done       | 0.9999977805230897 | 0      |
| 275 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?      | Done     | Done       | 0.9999979937508753 | 0      |
| 276 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979876427401 | 0      |
| 277 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999979985256053 | 0      |
| 278 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?      | Done     | Done       | 0.9999979983537596 | 0      |
| 279 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ?            | Done     | Done       | 0.9999980188282458 | 0      |
| 280 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?      | Done     | Done       | 0.9999979974351717 | 0      |
| 281 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?      | Done     | Done       | 0.9999979827196411 | 0      |
| 282 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?              | Done     | Done       | 0.999998083109312  | 0      |
| 283 | Tensor<[1, 256, 7, 7]> self = ?,<br>Tensor<[1, 256, 7, 7]> other = ?          | Done     | Done       | 0.9999978794427467 | 0      |
| 284 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?      | Done     | Done       | 0.9999979838312634 | 0      |
| 285 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | Done       | 0.9999979841026176 | 0      |
| 286 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[1, 257, 768]> other = ?            | Done     | Unknown    | N/A                | N/A    |
| 287 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ?      | Done     | Done       | 0.9999980201290225 | 0      |
| 288 | Tensor<[1, 272, 7, 7]> self = ?,<br>Tensor<[1, 272, 7, 7]> other = ?          | Done     | Done       | 0.9999980759282356 | 0      |
| 289 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?      | Done     | Done       | 0.9999979526877035 | 0      |
| 290 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?      | Done     | Done       | 0.9999980179241961 | 0      |
| 291 | Tensor<[1, 28, 28, 28]> self = ?,<br>Tensor<[1, 28, 28, 28]> other = ?        | Done     | Done       | 0.9999979173773567 | 0      |
| 292 | Tensor<[1, 288, 14, 14]> self = ?,<br>Tensor<[1, 288, 14, 14]> other = ?      | Done     | Done       | 0.9999979829239868 | 0      |
| 293 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?    | Done     | Done       | 0.9999979916151651 | 0      |
| 294 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?      | Removed  | Done       | 0.9999980008553258 | 0      |
| 295 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?      | Removed  | Done       | 0.9999979768953281 | 0      |
| 296 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?    | Removed  | Done       | 0.9999979948738456 | 0      |
| 297 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?            | Done     | Done       | 0.999998021509487  | 0      |
| 298 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?        | Done     | Done       | 0.9999979703866207 | 0      |
| 299 | Tensor<[1, 32, 112, 112]> self = ?,<br>Tensor<[1, 32, 112, 112]> other = ?    | Done     | Done       | 0.9999979876215377 | 0      |
| 300 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?    | Done     | Done       | 0.9999980029094825 | 0      |
| 301 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?            | Unknown  | Done       | 0.9999980030637976 | 0      |
| 302 | Tensor<[1, 32, 256, 256]> self = ?,<br>Tensor<[1, 32, 256, 256]> other = ?    | Done     | Done       | 0.9999980004129599 | 0      |
| 303 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ?        | Done     | Done       | 0.9999979544400046 | 0      |
| 304 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?      | Done     | Done       | 0.9999980103094116 | 0      |
| 305 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?      | Done     | Done       | 0.9999980050118609 | 0      |
| 306 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?        | Done     | Done       | 0.9999980124787022 | 0      |
| 307 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?        | Done     | Done       | 0.9999979714655615 | 0      |
| 308 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                           | Unknown  | Done       | 0.9999948231827661 | 0      |
| 309 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999947874364892 | 0      |
| 310 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?        | Done     | Done       | 0.9999979889857175 | 0      |
| 311 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?        | Done     | Done       | 0.999997974803703  | 0      |
| 312 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?        | Done     | Done       | 0.9999979951099548 | 0      |
| 313 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?      | Done     | Done       | 0.9999980088357834 | 0      |
| 314 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Done       | 0.999997998811402  | 0      |
| 315 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?      | Unknown  | Done       | 0.9999980042409832 | 0      |
| 316 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 317 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 318 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?      | Done     | Done       | 0.9999979333868744 | 0      |
| 319 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?      | Done     | Done       | 0.9999979920075559 | 0      |
| 320 | Tensor<[1, 34, 28, 28]> self = ?,<br>Tensor<[1, 34, 28, 28]> other = ?        | Done     | Done       | 0.999998056248114  | 0      |
| 321 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?        | Done     | Done       | 0.9999979028380049 | 0      |
| 322 | Tensor<[1, 36, 56, 56]> self = ?,<br>Tensor<[1, 36, 56, 56]> other = ?        | Done     | Done       | 0.9999979816497523 | 0      |
| 323 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?        | Done     | Done       | 0.9999980003680287 | 0      |
| 324 | Tensor<[1, 384, 35, 35]> self = ?,<br>Tensor<[1, 384, 35, 35]> other = ?      | Done     | Done       | 0.9999979879164749 | 0      |
| 325 | Tensor<[1, 384, 8, 8]> self = ?,<br>Tensor<[1, 384, 8, 8]> other = ?          | Done     | Done       | 0.9999980186790071 | 0      |
| 326 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 327 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 328 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 329 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 330 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?                | Unknown  | Done       | 0.9999981174155124 | 0      |
| 331 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?                   | Unknown  | Done       | 0.999997686512061  | 0      |
| 332 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ?        | Done     | Done       | 0.9999978405314963 | 0      |
| 333 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?        | Done     | Done       | 0.9999980587467154 | 0      |
| 334 | Tensor<[1, 40, 30, 30]> self = ?,<br>Tensor<[1, 40, 30, 30]> other = ?        | Done     | Done       | 0.9999979928270354 | 0      |
| 335 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?        | Done     | Done       | 0.9999979976149381 | 0      |
| 336 | Tensor<[1, 40, 56, 56]> self = ?,<br>Tensor<[1, 40, 56, 56]> other = ?        | Done     | Done       | 0.9999979691986595 | 0      |
| 337 | Tensor<[1, 400, 7, 7]> self = ?,<br>Tensor<[1, 400, 7, 7]> other = ?          | Done     | Done       | 0.9999979230743714 | 0      |
| 338 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ?      | Done     | Done       | 0.9999979136272894 | 0      |
| 339 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999980450920324 | 0      |
| 340 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?          | Unknown  | Done       | 0.9999979915998958 | 0      |
| 341 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?            | Done     | Done       | 0.999997996041687  | 0      |
| 342 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ?      | Done     | Done       | 0.9999979948824157 | 0      |
| 343 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?          | Done     | Done       | 0.999997904359527  | 0      |
| 344 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?      | Done     | Done       | 0.9999979861588576 | 0      |
| 345 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999947244912898 | 0      |
| 346 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | 0.9999980001874889 | 0      |
| 347 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | 0.9999979928338188 | 0      |
| 348 | Tensor<[1, 46, 28, 28]> self = ?,<br>Tensor<[1, 46, 28, 28]> other = ?        | Done     | Done       | 0.9999980366867401 | 0      |
| 349 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ?        | Done     | Done       | 0.9999978959421497 | 0      |
| 350 | Tensor<[1, 48, 33, 33]> self = ?,<br>Tensor<[1, 48, 33, 33]> other = ?        | Done     | Done       | 0.9999979635412402 | 0      |
| 351 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?        | Done     | Done       | 0.9999979735677377 | 0      |
| 352 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?        | Done     | Done       | 0.9999979989728797 | 0      |
| 353 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?      | Done     | Done       | 0.9999979663817643 | 0      |
| 354 | Tensor<[1, 480, 7, 7]> self = ?,<br>Tensor<[1, 480, 7, 7]> other = ?          | Done     | Done       | 0.9999980509248028 | 0      |
| 355 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?          | Done     | Done       | 0.9999979969893165 | 0      |
| 356 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?              | Unknown  | Done       | 0.9999978716917874 | 0      |
| 357 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?          | Unknown  | Done       | 0.9999979007889371 | 0      |
| 358 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999945917948657 | 0      |
| 359 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?              | Unknown  | Done       | 0.9999980160935971 | 0      |
| 360 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?            | Done     | Done       | 0.9999980238695644 | 0      |
| 361 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?            | Unknown  | Done       | 0.9999979922732577 | 0      |
| 362 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?              | Done     | Done       | 0.9999979720198455 | 0      |
| 363 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                | 0      |
| 364 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Unknown  | Done       | 1.0                | 0      |
| 365 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | Done       | 0.9999979743117824 | 0      |
| 366 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ?  | Done     | Done       | 0.9999979908126598 | 0      |
| 367 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ?      | Done     | Done       | 0.9999979826776754 | 0      |
| 368 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979736230121 | 0      |
| 369 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979557718933 | 0      |
| 370 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?      | Done     | Done       | 0.9999979699687918 | 0      |
| 371 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?      | Done     | Done       | 0.9999979864487814 | 0      |
| 372 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979523010939 | 0      |
| 373 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979957886985 | 0      |
| 374 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?          | Done     | Done       | 0.9999979930342842 | 0      |
| 375 | Tensor<[1, 512, 8, 8]> self = ?,<br>Tensor<[1, 512, 8, 8]> other = ?          | Done     | Done       | 0.999997959151238  | 0      |
| 376 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Unknown  | Done       | 0.9999980108302444 | 0      |
| 377 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?    | Unknown  | Done       | 0.9999979935105687 | 0      |
| 378 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                      | Unknown  | Done       | 0.9999986076173061 | 0      |
| 379 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?      | Done     | Done       | 0.9999979863929866 | 0      |
| 380 | Tensor<[1, 56, 14, 14]> self = ?,<br>Tensor<[1, 56, 14, 14]> other = ?        | Done     | Done       | 0.9999980551896005 | 0      |
| 381 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?        | Done     | Done       | 0.9999979958335996 | 0      |
| 382 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?      | Done     | Done       | 0.9999979882950204 | 0      |
| 383 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?        | Done     | Done       | 0.9999980032816855 | 0      |
| 384 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?      | Done     | Done       | 0.9999980064121353 | 0      |
| 385 | Tensor<[1, 58, 28, 28]> self = ?,<br>Tensor<[1, 58, 28, 28]> other = ?        | Done     | Done       | 0.9999980614675054 | 0      |
| 386 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Unknown  | Done       | 0.999998001463153  | 0      |
| 387 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Unknown  | Done       | 0.9999910556326542 | 0      |
| 388 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?            | Unknown  | Done       | 0.9999993219213289 | 0      |
| 389 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?            | Unknown  | Done       | 0.9999982265583091 | 0      |
| 390 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | Done       | 0.9999975438341491 | 0      |
| 391 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?            | Unknown  | Done       | 0.9999976455990804 | 0      |
| 392 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999965816627383 | 0      |
| 393 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?              | Unknown  | Done       | 0.9999976624694814 | 0      |
| 394 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999988757822531 | 0      |
| 395 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?              | Unknown  | Done       | 0.9999945191941735 | 0      |
| 396 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 397 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 398 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?           | Unknown  | Done       | 0.9999976413984086 | 0      |
| 399 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?          | Unknown  | Done       | 0.9999981927499847 | 0      |
| 400 | Tensor<[1, 60, 28, 28]> self = ?,<br>Tensor<[1, 60, 28, 28]> other = ?        | Done     | Done       | 0.9999979446992914 | 0      |
| 401 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                         | Done     | Done       | 1.0                | 0      |
| 402 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                       | Unknown  | Done       | 1.0                | 0      |
| 403 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?    | Done     | Done       | 0.999997991734226  | 0      |
| 404 | Tensor<[1, 64, 128, 128]> self = ?,<br>Tensor<[1, 64, 128, 128]> other = ?    | Done     | Done       | 0.9999979969533733 | 0      |
| 405 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ?        | Done     | Done       | 0.9999980675133167 | 0      |
| 406 | Tensor<[1, 64, 147, 147]> self = ?,<br>Tensor<[1, 64, 147, 147]> other = ?    | Done     | Done       | 0.9999979958214039 | 0      |
| 407 | Tensor<[1, 64, 150, 150]> self = ?,<br>Tensor<[1, 64, 150, 150]> other = ?    | Done     | Done       | 0.9999979866198292 | 0      |
| 408 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979895983728 | 0      |
| 409 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999979527413273 | 0      |
| 410 | Tensor<[1, 64, 224, 224]> self = ?,<br>Tensor<[1, 64, 224, 224]> other = ?    | Done     | Done       | 0.9999979882296641 | 0      |
| 411 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?    | Done     | Done       | 0.9999979887386873 | 0      |
| 412 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?    | Done     | Done       | 0.9999979944787138 | 0      |
| 413 | Tensor<[1, 64, 28, 28]> self = ?,<br>Tensor<[1, 64, 28, 28]> other = ?        | Done     | Done       | 0.9999979401778861 | 0      |
| 414 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 415 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 416 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?        | Done     | Done       | 0.9999980147594152 | 0      |
| 417 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979578627982 | 0      |
| 418 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 419 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 420 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999980623162091 | 0      |
| 421 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?    | Done     | Done       | 0.9999979933468237 | 0      |
| 422 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?        | Done     | Done       | 0.9999979929716923 | 0      |
| 423 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?        | Done     | Done       | 0.9999980058845068 | 0      |
| 424 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?      | Done     | Done       | 0.9999979911572183 | 0      |
| 425 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?        | Done     | Done       | 0.9999980139086961 | 0      |
| 426 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?        | Done     | Done       | 0.9999979888638187 | 0      |
| 427 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 428 | Tensor<[1, 640, 7, 7]> self = ?,<br>Tensor<[1, 640, 7, 7]> other = ?          | Done     | Done       | 0.9999979218158519 | 0      |
| 429 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 430 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, s0, s1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 431 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 432 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 433 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?      | Done     | Done       | 0.9999980136007689 | 0      |
| 434 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?      | Done     | Done       | 0.9999979925463928 | 0      |
| 435 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?          | Done     | Done       | 0.9999980048679201 | 0      |
| 436 | Tensor<[1, 68, 14, 14]> self = ?,<br>Tensor<[1, 68, 14, 14]> other = ?        | Done     | Done       | 0.9999980823123421 | 0      |
| 437 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?      | Done     | Done       | 0.9999979986091793 | 0      |
| 438 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999946945227682 | 0      |
| 439 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?              | Done     | Done       | 0.9999979849745113 | 0      |
| 440 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?        | Done     | Done       | 0.9999979835133463 | 0      |
| 441 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?          | Done     | Done       | 0.999997978151746  | 0      |
| 442 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?                | Done     | Done       | 0.9999980382778234 | 0      |
| 443 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?        | Done     | Done       | 0.9999978862899431 | 0      |
| 444 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?        | Done     | Done       | 0.9999979943764348 | 0      |
| 445 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?        | Done     | Done       | 0.9999979765666325 | 0      |
| 446 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ?      | Done     | Done       | 0.9999979824086298 | 0      |
| 447 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?      | Done     | Done       | 0.999997990047835  | 0      |
| 448 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?      | Done     | Done       | 0.9999980019703392 | 0      |
| 449 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?    | Done     | Done       | 0.9999979848597498 | 0      |
| 450 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?      | Done     | Done       | 0.9999979933343001 | 0      |
| 451 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 768, 16, 16]> other = ?      | Done     | Unknown    | N/A                | N/A    |
| 452 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                    | Done     | Done       | 0.9999979765228485 | 0      |
| 453 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?          | Done     | Done       | 0.9999979851631556 | 0      |
| 454 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                      | Unknown  | Done       | 0.9999978212420076 | 0      |
| 455 | Tensor<[1, 78, 28, 28]> self = ?,<br>Tensor<[1, 78, 28, 28]> other = ?        | Done     | Done       | 0.9999980225836309 | 0      |
| 456 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?          | Done     | Done       | 0.9999980320060544 | 0      |
| 457 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 458 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 459 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 460 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?              | Unknown  | Done       | 0.9999973228713723 | 0      |
| 461 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Unknown    | N/A                | N/A    |
| 462 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?              | Unknown  | Unknown    | N/A                | N/A    |
| 463 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 464 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 465 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999982064698001 | 0      |
| 466 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?          | Unknown  | Done       | 0.9999982880767132 | 0      |
| 467 | Tensor<[1, 8, 112, 112]> self = ?,<br>Tensor<[1, 8, 112, 112]> other = ?      | Done     | Done       | 0.9999979625102914 | 0      |
| 468 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ?      | Done     | Done       | 0.9999979995408801 | 0      |
| 469 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?                | Done     | Done       | 0.99999797715457   | 0      |
| 470 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?        | Done     | Done       | 0.9999979809031203 | 0      |
| 471 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?          | Done     | Done       | 0.9999979863417303 | 0      |
| 472 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?        | Done     | Done       | 0.999998084933136  | 0      |
| 473 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?        | Done     | Done       | 0.9999980128496002 | 0      |
| 474 | Tensor<[1, 80, 15, 15]> self = ?,<br>Tensor<[1, 80, 15, 15]> other = ?        | Done     | Done       | 0.999998010056919  | 0      |
| 475 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?        | Done     | Done       | 0.9999980070848743 | 0      |
| 476 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?        | Done     | Done       | 0.9999979748467616 | 0      |
| 477 | Tensor<[1, 80, 7, 7]> self = ?,<br>Tensor<[1, 80, 7, 7]> other = ?            | Done     | Done       | 0.9999981005981914 | 0      |
| 478 | Tensor<[1, 88, 17, 17]> self = ?,<br>Tensor<[1, 88, 17, 17]> other = ?        | Done     | Done       | 0.999997998491495  | 0      |
| 479 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?          | Done     | Done       | 0.9999979973048414 | 0      |
| 480 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?      | Done     | Done       | 0.9999979895874659 | 0      |
| 481 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?              | Done     | Done       | 0.9999979935544122 | 0      |
| 482 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                           | Done     | Done       | 0.9999954746065055 | 0      |
| 483 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                | Done     | Done       | 0.9999981868966278 | 0      |
| 484 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947882797424 | 0      |
| 485 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?            | Done     | Unknown    | N/A                | N/A    |
| 486 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?              | Done     | Done       | 0.9999978710503966 | 0      |
| 487 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999948866147099 | 0      |
| 488 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?              | Done     | Done       | 0.9999980040361937 | 0      |
| 489 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947229759888 | 0      |
| 490 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?              | Done     | Done       | 0.9999979866064714 | 0      |
| 491 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?                | Done     | Done       | 0.9999979255765684 | 0      |
| 492 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999946152743212 | 0      |
| 493 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?              | Done     | Done       | 0.9999979934246008 | 0      |
| 494 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?          | Done     | Done       | 0.9999980333083607 | 0      |
| 495 | Tensor<[1, 92, 14, 14]> self = ?,<br>Tensor<[1, 92, 14, 14]> other = ?        | Done     | Done       | 0.9999980031010811 | 0      |
| 496 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?        | Done     | Done       | 0.9999979614043453 | 0      |
| 497 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?        | Done     | Done       | 0.9999979544560554 | 0      |
| 498 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?        | Done     | Done       | 0.9999979734664693 | 0      |
| 499 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?            | Done     | Done       | 0.9999978588392935 | 0      |
| 500 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?          | Done     | Done       | 0.9999979668443212 | 0      |
| 501 | Tensor<[1, 98, 28, 28]> self = ?,<br>Tensor<[1, 98, 28, 28]> other = ?        | Done     | Done       | 0.9999979852453171 | 0      |
| 502 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor<[1, s0*s1, 1280]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 503 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor<[1, s0*s1, 640]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 504 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 505 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor<[1, s1*s2, 320]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 506 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor<[1, s1*s2, 640]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 507 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 508 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.9998803478524045 | 0      |
| 509 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                      | Unknown  | Done       | 0.9999980389446463 | 0      |
| 510 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?            | Unknown  | Done       | 0.9999979983891356 | 0      |
| 511 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?              | Done     | Done       | 0.9999981759002722 | 0      |
| 512 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Done     | Done       | 0.9999979974738269 | 0      |
| 513 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 514 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.9999051309127422 | 0      |
| 515 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                      | Unknown  | Done       | 0.9999982105410613 | 0      |
| 516 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?         | Done     | Done       | 0.9999980241709178 | 0      |
| 517 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?         | Done     | Done       | 0.9999979930978236 | 0      |
| 518 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?         | Done     | Done       | 0.9999979962961725 | 0      |
| 519 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?         | Done     | Done       | 0.9999979680799024 | 0      |
| 520 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                | 0      |
| 521 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 0.9996090333474896 | 0      |
| 522 | Tensor<[2*s0]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 523 | Tensor<[2*s1]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 524 | Tensor<[2*s2]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 525 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                | 0      |
| 526 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                | 0      |
| 527 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                      | Unknown  | Done       | 0.999997781216852  | 0      |
| 528 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?              | Unknown  | Done       | 0.9999979531469532 | 0      |
| 529 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?                | Done     | Done       | 0.9999980583853529 | 0      |
| 530 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?                | Done     | Done       | 0.9999981502482903 | 0      |
| 531 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?              | Done     | Done       | 0.9999982106880005 | 0      |
| 532 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                      | Done     | Done       | 0.99999801789694   | 0      |
| 533 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.9999978595056985 | 0      |
| 534 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                              | Done     | Done       | 0.9741880328385558 | 0      |
| 535 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                    | Done     | Done       | 0.9999978926991213 | 0      |
| 536 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Done     | Done       | 0.999998264274553  | 0      |
| 537 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?        | Done     | Done       | 0.9999980301626128 | 0      |
| 538 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?        | Done     | Done       | 0.9999980304311885 | 0      |
| 539 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?        | Done     | Done       | 0.9999980146331895 | 0      |
| 540 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?        | Done     | Done       | 0.9999979988363454 | 0      |
| 541 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Unknown  | Done       | 0.999998022678906  | 0      |
| 542 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                   | Done     | Done       | 0.9999980494864835 | 0      |
| 543 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?         | Done     | Done       | 0.9999979851690406 | 0      |
| 544 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?         | Done     | Done       | 0.9999979787450962 | 0      |
| 545 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?         | Done     | Done       | 0.9999979924928255 | 0      |
| 546 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?         | Done     | Done       | 0.9999979927496745 | 0      |
| 547 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.9999980307421489 | 0      |
| 548 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                    | Done     | Done       | 0.9999979447137516 | 0      |
| 549 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Unknown  | Done       | 0.293087569688945  | 0      |
| 550 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?            | Unknown  | Done       | 0.9999980160903209 | 0      |
| 551 | Tensor<[]> self = ?,<br>Tensor other = 1                                      | None     | Fallback   | 1.0                | -1     |
| 552 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                        | Unknown  | Unknown    | N/A                | N/A    |
| 553 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |

