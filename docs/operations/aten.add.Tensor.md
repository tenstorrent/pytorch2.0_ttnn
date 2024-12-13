### aten.add.Tensor
|     | ATen Input Variations                                                         | Status   | Isolated   | PCC                | Host   |
|----:|:------------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                          | Unknown  | Done       | 1.0                | 0      |
|   1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                                | Unknown  | Done       | 1.0                | 0      |
|   2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -6.0                        | None     | Fallback   | 1.0                | -1     |
|   3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                         | Removed  | Fallback   | 1.0                | -1     |
|   4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                           | None     | Fallback   | 1.0                | -1     |
|   5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.0                         | None     | Fallback   | 1.0                | -1     |
|   6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2                           | None     | Fallback   | 1.0                | -1     |
|   7 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Fallback   | 1.0                | -1     |
|   8 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999977327921716 | 0      |
|   9 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?          | Unknown  | Done       | 0.9999970763476301 | 0      |
|  10 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839              | None     | Fallback   | 1.0                | -1     |
|  11 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9043478220701218              | None     | Fallback   | 1.0                | -1     |
|  12 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9086956530809402              | None     | Fallback   | 1.0                | -1     |
|  13 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9090909063816071              | None     | Fallback   | 1.0                | -1     |
|  14 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9130434766411781              | None     | Fallback   | 1.0                | -1     |
|  15 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032              | None     | Fallback   | 1.0                | -1     |
|  16 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.917391300201416               | None     | Fallback   | 1.0                | -1     |
|  17 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9181818142533302              | None     | Fallback   | 1.0                | -1     |
|  18 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9217391312122345              | None     | Fallback   | 1.0                | -1     |
|  19 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9260869547724724              | None     | Fallback   | 1.0                | -1     |
|  20 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9272727221250534              | None     | Fallback   | 1.0                | -1     |
|  21 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226              | None     | Fallback   | 1.0                | -1     |
|  22 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9304347857832909              | None     | Fallback   | 1.0                | -1     |
|  23 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9347826093435287              | None     | Fallback   | 1.0                | -1     |
|  24 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9363636374473572              | None     | Fallback   | 1.0                | -1     |
|  25 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9391304366290569              | None     | Fallback   | 1.0                | -1     |
|  26 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323              | None     | Fallback   | 1.0                | -1     |
|  27 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9434782639145851              | None     | Fallback   | 1.0                | -1     |
|  28 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.94545454159379                | None     | Fallback   | 1.0                | -1     |
|  29 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.947826087474823               | None     | Fallback   | 1.0                | -1     |
|  30 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9521739110350609              | None     | Fallback   | 1.0                | -1     |
|  31 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9545454569160938              | None     | Fallback   | 1.0                | -1     |
|  32 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9565217345952988              | None     | Fallback   | 1.0                | -1     |
|  33 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516              | None     | Fallback   | 1.0                | -1     |
|  34 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.960869561880827               | None     | Fallback   | 1.0                | -1     |
|  35 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.963636364787817               | None     | Fallback   | 1.0                | -1     |
|  36 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9652173891663551              | None     | Fallback   | 1.0                | -1     |
|  37 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9695652164518833              | None     | Fallback   | 1.0                | -1     |
|  38 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161              | None     | Fallback   | 1.0                | -1     |
|  39 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9727272726595402              | None     | Fallback   | 1.0                | -1     |
|  40 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9739130418747663              | None     | Fallback   | 1.0                | -1     |
|  41 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9782608672976494              | None     | Fallback   | 1.0                | -1     |
|  42 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9818181823939085              | None     | Fallback   | 1.0                | -1     |
|  43 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9826086945831776              | None     | Fallback   | 1.0                | -1     |
|  44 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581              | None     | Fallback   | 1.0                | -1     |
|  45 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9869565209373832              | None     | Fallback   | 1.0                | -1     |
|  46 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9909090911969543              | None     | Fallback   | 1.0                | -1     |
|  47 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9913043472915888              | None     | Fallback   | 1.0                | -1     |
|  48 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9956521736457944              | None     | Fallback   | 1.0                | -1     |
|  49 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                           | Unknown  | Fallback   | 1.0                | -1     |
|  50 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027    | None     | Fallback   | 1.0                | -1     |
|  51 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997     | None     | Fallback   | 1.0                | -1     |
|  52 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994     | None     | Fallback   | 1.0                | -1     |
|  53 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Fallback   | 1.0                | -1     |
|  54 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | 0.9999981519869657 | 0      |
|  55 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -6.0                        | None     | Fallback   | 1.0                | -1     |
|  56 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                         | Removed  | Fallback   | 1.0                | -1     |
|  57 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                           | None     | Fallback   | 1.0                | -1     |
|  58 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.0                         | None     | Fallback   | 1.0                | -1     |
|  59 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2                           | None     | Fallback   | 1.0                | -1     |
|  60 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Fallback   | 1.0                | -1     |
|  61 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?              | Unknown  | Done       | 0.9999981245360253 | 0      |
|  62 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                          | None     | Fallback   | 1.0                | -1     |
|  63 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                | Unknown  | Done       | 0.9999977341451037 | 0      |
|  64 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Done     | Done       | 0.9999981056877411 | 0      |
|  65 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                   | Done     | Done       | 0.9999976300678828 | 0      |
|  66 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?            | Done     | Done       | 0.9999978632782042 | 0      |
|  67 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                          | None     | Fallback   | 1.0                | -1     |
|  68 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?              | Done     | Done       | 0.9999979731297183 | 0      |
|  69 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?              | Done     | Done       | 0.9999980563746921 | 0      |
|  70 | Tensor<[1, 100, 14, 14]> self = ?,<br>Tensor<[1, 100, 14, 14]> other = ?      | Done     | Done       | 0.9999979352895412 | 0      |
|  71 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?        | Done     | Done       | 0.9999980201775567 | 0      |
|  72 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 0.0                       | None     | Fallback   | 1.0                | -1     |
|  73 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | None     | Fallback   | 1.0                | -1     |
|  74 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ?    | Done     | Done       | 0.9999979621166266 | 0      |
|  75 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ?    | Done     | Done       | 0.9999980256598666 | 0      |
|  76 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?    | Done     | Done       | 0.999997981536894  | 0      |
|  77 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?          | Done     | Done       | 0.9999979646586404 | 0      |
|  78 | Tensor<[1, 1024, 17, 17]> self = ?,<br>Tensor<[1, 1024, 17, 17]> other = ?    | Done     | Done       | 0.9999980054534008 | 0      |
|  79 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999979364951613 | 0      |
|  80 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999979775297773 | 0      |
|  81 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?    | Done     | Done       | 0.9999979928763482 | 0      |
|  82 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999979832964062 | 0      |
|  83 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?    | Done     | Done       | 0.9999979903252847 | 0      |
|  84 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?        | Done     | Done       | 0.9999980066207321 | 0      |
|  85 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999977993225732 | 0      |
|  86 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?      | Done     | Done       | 0.9999979743109306 | 0      |
|  87 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?    | Done     | Done       | 0.999998000897714  | 0      |
|  88 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                                 | None     | Fallback   | 1.0                | -1     |
|  89 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                                 | None     | Fallback   | 1.0                | -1     |
|  90 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?      | Done     | Done       | 0.999998077631052  | 0      |
|  91 | Tensor<[1, 112, 15, 15]> self = ?,<br>Tensor<[1, 112, 15, 15]> other = ?      | Done     | Done       | 0.9999979528895376 | 0      |
|  92 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?      | Done     | Done       | 0.9999979138489634 | 0      |
|  93 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ?      | Done     | Done       | 0.9999980120679288 | 0      |
|  94 | Tensor<[1, 116, 14, 14]> self = ?,<br>Tensor<[1, 116, 14, 14]> other = ?      | Done     | Done       | 0.9999979854553299 | 0      |
|  95 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999977951444633 | 0      |
|  96 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?          | Unknown  | Done       | 0.9999990420574281 | 0      |
|  97 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999957265201601 | 0      |
|  98 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?            | Unknown  | Done       | 0.9999962782440515 | 0      |
|  99 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999974328251383 | 0      |
| 100 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?            | Unknown  | Done       | 0.9999994280231091 | 0      |
| 101 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | 0.9999980609641428 | 0      |
| 102 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 103 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 104 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 105 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Done     | Done       | 0.9999982434103092 | 0      |
| 106 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?        | Done     | Done       | 0.9999983186428284 | 0      |
| 107 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ?          | Done     | Done       | 0.9999981663726308 | 0      |
| 108 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?              | Done     | Done       | 0.9999981236524131 | 0      |
| 109 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<[1, 1, 1, 14]> other = ?          | Done     | Done       | 0.9999979815613691 | 0      |
| 110 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ?    | Done     | Done       | 0.9999979730627941 | 0      |
| 111 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?         | Done     | Done       | 0.9999978267705519 | 0      |
| 112 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ?          | Done     | Done       | 0.9999982278948505 | 0      |
| 113 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                         | None     | Fallback   | 1.0                | -1     |
| 114 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?            | Done     | Done       | 0.9999979497385362 | 0      |
| 115 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | 0.999997997809254  | 0      |
| 116 | Tensor<[1, 12, 56, 56]> self = ?,<br>Tensor<[1, 12, 56, 56]> other = ?        | Done     | Done       | 0.9999980415527858 | 0      |
| 117 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ?             | Done     | Done       | 0.9999979798077114 | 0      |
| 118 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?              | Done     | Done       | 0.9999980246113366 | 0      |
| 119 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999983221459993 | 0      |
| 120 | Tensor<[1, 120, 17, 17]> self = ?,<br>Tensor<[1, 120, 17, 17]> other = ?      | Done     | Done       | 0.9999979854924225 | 0      |
| 121 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?      | Done     | Done       | 0.9999979693183778 | 0      |
| 122 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?          | Done     | Done       | 0.9999979945588684 | 0      |
| 123 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?    | Done     | Done       | 0.9999979632702897 | 0      |
| 124 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 0.0                        | None     | Fallback   | 1.0                | -1     |
| 125 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | None     | Fallback   | 1.0                | -1     |
| 126 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979593719193 | 0      |
| 127 | Tensor<[1, 128, 112, 112]> self = ?,<br>Tensor<[1, 128, 112, 112]> other = ?  | Done     | Done       | 0.9999979802649938 | 0      |
| 128 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ?  | Done     | Done       | 0.9999979864052736 | 0      |
| 129 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979489380019 | 0      |
| 130 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979907206717 | 0      |
| 131 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ?      | Done     | Done       | 0.9999979780177984 | 0      |
| 132 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ?      | Done     | Done       | 0.9999979704156994 | 0      |
| 133 | Tensor<[1, 128, 64, 64]> self = ?,<br>Tensor<[1, 128, 64, 64]> other = ?      | Done     | Done       | 0.9999980166109379 | 0      |
| 134 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?      | Done     | Done       | 0.9999980060264312 | 0      |
| 135 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999979528052441 | 0      |
| 136 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?        | Unknown  | Done       | 0.9999980010624754 | 0      |
| 137 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?        | Unknown  | Done       | 0.9999979839951084 | 0      |
| 138 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 139 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, s0, s1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 140 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 141 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, s1, s2]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 142 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ?    | Done     | Done       | 0.9999980274433257 | 0      |
| 143 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ?      | Done     | Done       | 0.9999980439048477 | 0      |
| 144 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?        | Done     | Done       | 0.9999979927297679 | 0      |
| 145 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?    | Done     | Done       | 0.9999980026602705 | 0      |
| 146 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?              | Done     | Done       | 0.9999981431630964 | 0      |
| 147 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?      | Done     | Done       | 0.9999979890136735 | 0      |
| 148 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?      | Done     | Done       | 0.9999980318222286 | 0      |
| 149 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                         | None     | Fallback   | 1.0                | -1     |
| 150 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?            | Done     | Done       | 0.9999979924383817 | 0      |
| 151 | Tensor<[1, 14, 56, 56]> self = ?,<br>Tensor<[1, 14, 56, 56]> other = ?        | Done     | Done       | 0.9999979515746065 | 0      |
| 152 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?              | Done     | Done       | 0.9999980102041983 | 0      |
| 153 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?      | Done     | Done       | 0.9999980013529355 | 0      |
| 154 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?          | Done     | Done       | 0.9999980806535047 | 0      |
| 155 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?          | Done     | Done       | 0.9999980321477521 | 0      |
| 156 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                         | None     | Fallback   | 1.0                | -1     |
| 157 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Done     | Done       | 0.9999978845457522 | 0      |
| 158 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                          | None     | Fallback   | 1.0                | -1     |
| 159 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?              | Done     | Done       | 0.9999979480330137 | 0      |
| 160 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ?          | Done     | Done       | 0.9999979818930939 | 0      |
| 161 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?             | Done     | Done       | 0.9999979982923213 | 0      |
| 162 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?        | Done     | Done       | 0.9999980020552355 | 0      |
| 163 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Tensor<[1, 1536, 8, 8]> other = ?        | Done     | Done       | 0.999998028812372  | 0      |
| 164 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999969120883911 | 0      |
| 165 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?          | Unknown  | Done       | 0.9999982491513834 | 0      |
| 166 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999968208587516 | 0      |
| 167 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?            | Unknown  | Done       | 0.9999987238920787 | 0      |
| 168 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999982005056568 | 0      |
| 169 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?            | Unknown  | Done       | 0.9999960059362573 | 0      |
| 170 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999982004063869 | 0      |
| 171 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Done       | 0.9999987353162166 | 0      |
| 172 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 173 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 174 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 175 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Done     | Done       | 0.999997892013087  | 0      |
| 176 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?        | Done     | Done       | 0.9999980679030598 | 0      |
| 177 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ?    | Done     | Done       | 0.9999979936875713 | 0      |
| 178 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?      | Done     | Done       | 0.9999979632228189 | 0      |
| 179 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?      | Done     | Done       | 0.9999979597296382 | 0      |
| 180 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ?    | Done     | Done       | 0.9999979888062459 | 0      |
| 181 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> other = ?         | Done     | Done       | 0.999997940389078  | 0      |
| 182 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ?    | Done     | Done       | 0.9999979888033084 | 0      |
| 183 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor<[1, 1, 1, 256]> other = ?       | Done     | Done       | 0.9999979931718868 | 0      |
| 184 | Tensor<[1, 16, 28, 28]> self = ?,<br>Tensor<[1, 16, 28, 28]> other = ?        | Done     | Done       | 0.9999980646485537 | 0      |
| 185 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Done       | 0.999998200695085  | 0      |
| 186 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Done     | Done       | 0.9999979872447933 | 0      |
| 187 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 188 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 189 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?              | Done     | Done       | 0.9999979784299566 | 0      |
| 190 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 191 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 192 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999980808943607 | 0      |
| 193 | Tensor<[1, 160, 14, 14]> self = ?,<br>Tensor<[1, 160, 14, 14]> other = ?      | Done     | Done       | 0.9999980018770461 | 0      |
| 194 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ?      | Done     | Done       | 0.999998059494645  | 0      |
| 195 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ?      | Done     | Done       | 0.9999979826833099 | 0      |
| 196 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?      | Done     | Done       | 0.9999980150068708 | 0      |
| 197 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?          | Done     | Done       | 0.9999978646824085 | 0      |
| 198 | Tensor<[1, 160, 73, 73]> self = ?,<br>Tensor<[1, 160, 73, 73]> other = ?      | Done     | Done       | 0.9999979910614103 | 0      |
| 199 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999979742609948 | 0      |
| 200 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?          | Done     | Done       | 0.9999979943383137 | 0      |
| 201 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ?      | Done     | Done       | 0.9999979903464946 | 0      |
| 202 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?        | Done     | Done       | 0.9999980354009613 | 0      |
| 203 | Tensor<[1, 185, 28, 28]> self = ?,<br>Tensor<[1, 185, 28, 28]> other = ?      | Done     | Done       | 0.9999979778638747 | 0      |
| 204 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ?            | Done     | Done       | 0.9999979777803109 | 0      |
| 205 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ?      | Done     | Done       | 0.9999979398329186 | 0      |
| 206 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ?      | Done     | Done       | 0.9999980010879862 | 0      |
| 207 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?      | Done     | Done       | 0.9999980261569336 | 0      |
| 208 | Tensor<[1, 192, 7, 7]> self = ?,<br>Tensor<[1, 192, 7, 7]> other = ?          | Done     | Done       | 0.9999980270160342 | 0      |
| 209 | Tensor<[1, 192, 71, 71]> self = ?,<br>Tensor<[1, 192, 71, 71]> other = ?      | Done     | Done       | 0.9999979823623767 | 0      |
| 210 | Tensor<[1, 192, 8, 8]> self = ?,<br>Tensor<[1, 192, 8, 8]> other = ?          | Done     | Done       | 0.9999980015521439 | 0      |
| 211 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?        | Done     | Done       | 0.9999980009543895 | 0      |
| 212 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?          | Done     | Done       | 0.9999979911429516 | 0      |
| 213 | Tensor<[1, 196, 14, 14]> self = ?,<br>Tensor<[1, 196, 14, 14]> other = ?      | Done     | Done       | 0.9999980042236247 | 0      |
| 214 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ?            | Done     | Done       | 0.9999979704671547 | 0      |
| 215 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?          | Done     | Done       | 0.9999979868446575 | 0      |
| 216 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?            | Done     | Done       | 0.9999979999440294 | 0      |
| 217 | Tensor<[1, 19]> self = ?,<br>Tensor other = 2                                 | Removed  | Fallback   | 1.0                | -1     |
| 218 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Unknown  | Fallback   | 1.0                | -1     |
| 219 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Fallback   | 1.0                | -1     |
| 220 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Fallback   | 1.0                | -1     |
| 221 | Tensor<[1, 20, 28, 28]> self = ?,<br>Tensor<[1, 20, 28, 28]> other = ?        | Done     | Done       | 0.9999980007114513 | 0      |
| 222 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?        | Done     | Done       | 0.9999979674693228 | 0      |
| 223 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 0.0                       | None     | Fallback   | 1.0                | -1     |
| 224 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | None     | Fallback   | 1.0                | -1     |
| 225 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999979755221111 | 0      |
| 226 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?    | Done     | Done       | 0.999997990488909  | 0      |
| 227 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999979842903398 | 0      |
| 228 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?    | Done     | Done       | 0.9999979931633828 | 0      |
| 229 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?        | Done     | Done       | 0.9999980030787361 | 0      |
| 230 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?          | Done     | Done       | 0.9999979863233884 | 0      |
| 231 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?             | Done     | Done       | 0.9999979926241497 | 0      |
| 232 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?      | Done     | Done       | 0.9999979535183187 | 0      |
| 233 | Tensor<[1, 208, 9, 9]> self = ?,<br>Tensor<[1, 208, 9, 9]> other = ?          | Done     | Done       | 0.9999978634433292 | 0      |
| 234 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?      | Done     | Done       | 0.999997953011954  | 0      |
| 235 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?      | Done     | Done       | 0.9999979812715025 | 0      |
| 236 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?          | Done     | Done       | 0.9999981628265867 | 0      |
| 237 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                          | None     | Fallback   | 1.0                | -1     |
| 238 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ?      | Done     | Done       | 0.9999980232560074 | 0      |
| 239 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?      | Done     | Done       | 0.9999979721942207 | 0      |
| 240 | Tensor<[1, 24, 112, 112]> self = ?,<br>Tensor<[1, 24, 112, 112]> other = ?    | Done     | Done       | 0.9999979932560314 | 0      |
| 241 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?        | Done     | Done       | 0.9999979544212295 | 0      |
| 242 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?        | Done     | Done       | 0.9999980383501893 | 0      |
| 243 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?        | Done     | Done       | 0.9999979983402433 | 0      |
| 244 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?        | Done     | Done       | 0.9999979727490448 | 0      |
| 245 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?        | Done     | Done       | 0.9999980462985416 | 0      |
| 246 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?        | Done     | Done       | 0.9999979769718    | 0      |
| 247 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?              | Done     | Done       | 0.9999979636125056 | 0      |
| 248 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?        | Done     | Done       | 0.9999980028772533 | 0      |
| 249 | Tensor<[1, 240, 14, 14]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?      | Done     | Done       | 0.9999980929807553 | 0      |
| 250 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?      | Done     | Done       | 0.999997974185552  | 0      |
| 251 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?              | Done     | Done       | 0.9999979390945293 | 0      |
| 252 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?        | Done     | Done       | 0.9999980297739777 | 0      |
| 253 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 0.0                        | None     | Fallback   | 1.0                | -1     |
| 254 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | None     | Fallback   | 1.0                | -1     |
| 255 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979869000569 | 0      |
| 256 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ?  | Done     | Done       | 0.9999979864688198 | 0      |
| 257 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?          | Done     | Done       | 0.9999980234649103 | 0      |
| 258 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ?  | Done     | Done       | 0.9999979929431125 | 0      |
| 259 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?          | Done     | Done       | 0.9999980034830033 | 0      |
| 260 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ?      | Done     | Done       | 0.9999979459531279 | 0      |
| 261 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?      | Done     | Done       | 0.9999980343122798 | 0      |
| 262 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?            | Done     | Done       | 0.9999979928657411 | 0      |
| 263 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979923800998 | 0      |
| 264 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ?  | Done     | Done       | 0.9999979912303661 | 0      |
| 265 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999980060720255 | 0      |
| 266 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ?  | Done     | Done       | 0.9999979898487464 | 0      |
| 267 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?            | Done     | Done       | 0.999998001954135  | 0      |
| 268 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.9999980391641156 | 0      |
| 269 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ?      | Done     | Done       | 0.9999979927319551 | 0      |
| 270 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?      | Done     | Done       | 0.9999979862563262 | 0      |
| 271 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?              | Done     | Done       | 0.9999981206736898 | 0      |
| 272 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?      | Done     | Done       | 0.9999979990169767 | 0      |
| 273 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999980336053572 | 0      |
| 274 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999979603558551 | 0      |
| 275 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?      | Done     | Done       | 0.999997986569417  | 0      |
| 276 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ?            | Done     | Done       | 0.9999979762999185 | 0      |
| 277 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?      | Done     | Done       | 0.9999979979491732 | 0      |
| 278 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?      | Done     | Done       | 0.9999979970462025 | 0      |
| 279 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?              | Done     | Done       | 0.9999980003478843 | 0      |
| 280 | Tensor<[1, 256, 7, 7]> self = ?,<br>Tensor<[1, 256, 7, 7]> other = ?          | Done     | Done       | 0.999998032851924  | 0      |
| 281 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?      | Done     | Done       | 0.9999979940663032 | 0      |
| 282 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999979340689206 | 0      |
| 283 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ?      | Done     | Done       | 0.9999979644569555 | 0      |
| 284 | Tensor<[1, 272, 7, 7]> self = ?,<br>Tensor<[1, 272, 7, 7]> other = ?          | Done     | Done       | 0.9999981119836804 | 0      |
| 285 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?      | Done     | Done       | 0.9999979950830564 | 0      |
| 286 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?      | Done     | Done       | 0.999997996467076  | 0      |
| 287 | Tensor<[1, 28, 28, 28]> self = ?,<br>Tensor<[1, 28, 28, 28]> other = ?        | Done     | Done       | 0.9999980574756585 | 0      |
| 288 | Tensor<[1, 288, 14, 14]> self = ?,<br>Tensor<[1, 288, 14, 14]> other = ?      | Done     | Done       | 0.9999979492351998 | 0      |
| 289 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?    | Done     | Done       | 0.9999979956645666 | 0      |
| 290 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?      | Done     | Done       | 0.9999979888146954 | 0      |
| 291 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?      | Done     | Done       | 0.9999979904630653 | 0      |
| 292 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?    | Done     | Done       | 0.9999979912994305 | 0      |
| 293 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?            | Done     | Done       | 0.9999979798779571 | 0      |
| 294 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?        | Done     | Done       | 0.9999979418997255 | 0      |
| 295 | Tensor<[1, 32, 112, 112]> self = ?,<br>Tensor<[1, 32, 112, 112]> other = ?    | Done     | Done       | 0.9999979876286528 | 0      |
| 296 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?    | Done     | Done       | 0.9999979873515015 | 0      |
| 297 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?            | Done     | Done       | 0.9999979634343263 | 0      |
| 298 | Tensor<[1, 32, 256, 256]> self = ?,<br>Tensor<[1, 32, 256, 256]> other = ?    | Done     | Done       | 0.9999979893093099 | 0      |
| 299 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ?        | Done     | Done       | 0.9999978736574326 | 0      |
| 300 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?      | Done     | Done       | 0.9999979934509271 | 0      |
| 301 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?      | Done     | Done       | 0.999997991588042  | 0      |
| 302 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?        | Done     | Done       | 0.9999980379129523 | 0      |
| 303 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?        | Done     | Done       | 0.9999979973864004 | 0      |
| 304 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                           | None     | Fallback   | 1.0                | -1     |
| 305 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0                         | None     | Fallback   | 1.0                | -1     |
| 306 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?        | Done     | Done       | 0.9999979822000985 | 0      |
| 307 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?        | Done     | Done       | 0.999998019241144  | 0      |
| 308 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?        | Done     | Done       | 0.9999979823271403 | 0      |
| 309 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?      | Done     | Done       | 0.9999979725798703 | 0      |
| 310 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Done       | 0.9999980164969197 | 0      |
| 311 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?      | Unknown  | Done       | 0.9999979962860983 | 0      |
| 312 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 313 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 314 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?      | Done     | Done       | 0.9999980061143723 | 0      |
| 315 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?      | Done     | Done       | 0.9999979851623017 | 0      |
| 316 | Tensor<[1, 34, 28, 28]> self = ?,<br>Tensor<[1, 34, 28, 28]> other = ?        | Done     | Done       | 0.9999978770683969 | 0      |
| 317 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?        | Done     | Done       | 0.9999980431783639 | 0      |
| 318 | Tensor<[1, 36, 56, 56]> self = ?,<br>Tensor<[1, 36, 56, 56]> other = ?        | Done     | Done       | 0.9999980095300669 | 0      |
| 319 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?        | Done     | Done       | 0.9999979882939616 | 0      |
| 320 | Tensor<[1, 384, 35, 35]> self = ?,<br>Tensor<[1, 384, 35, 35]> other = ?      | Done     | Done       | 0.9999979933443541 | 0      |
| 321 | Tensor<[1, 384, 8, 8]> self = ?,<br>Tensor<[1, 384, 8, 8]> other = ?          | Done     | Done       | 0.9999979679841275 | 0      |
| 322 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 323 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 324 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 325 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                | -1     |
| 326 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?                | Unknown  | Done       | 0.9999981858511813 | 0      |
| 327 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?                   | Unknown  | Done       | 0.9999977965813301 | 0      |
| 328 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ?        | Done     | Done       | 0.9999979739009549 | 0      |
| 329 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?        | Done     | Done       | 0.9999979850876428 | 0      |
| 330 | Tensor<[1, 40, 30, 30]> self = ?,<br>Tensor<[1, 40, 30, 30]> other = ?        | Done     | Done       | 0.9999980270512357 | 0      |
| 331 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?        | Done     | Done       | 0.9999980384963035 | 0      |
| 332 | Tensor<[1, 40, 56, 56]> self = ?,<br>Tensor<[1, 40, 56, 56]> other = ?        | Done     | Done       | 0.999998000921995  | 0      |
| 333 | Tensor<[1, 400, 7, 7]> self = ?,<br>Tensor<[1, 400, 7, 7]> other = ?          | Done     | Done       | 0.9999980257497966 | 0      |
| 334 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ?      | Done     | Done       | 0.9999979706215617 | 0      |
| 335 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999979898702938 | 0      |
| 336 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?          | Unknown  | Done       | 0.9999979862215678 | 0      |
| 337 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?            | Done     | Done       | 0.9999979957654761 | 0      |
| 338 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ?      | Done     | Done       | 0.9999980006249802 | 0      |
| 339 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?          | Done     | Done       | 0.9999979692667808 | 0      |
| 340 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?      | Done     | Done       | 0.9999979760993556 | 0      |
| 341 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Fallback   | 1.0                | -1     |
| 342 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | 0.9999980097754443 | 0      |
| 343 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | 0.9999979756445717 | 0      |
| 344 | Tensor<[1, 46, 28, 28]> self = ?,<br>Tensor<[1, 46, 28, 28]> other = ?        | Done     | Done       | 0.9999980057024604 | 0      |
| 345 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ?        | Done     | Done       | 0.9999979704290191 | 0      |
| 346 | Tensor<[1, 48, 33, 33]> self = ?,<br>Tensor<[1, 48, 33, 33]> other = ?        | Done     | Done       | 0.9999979855497502 | 0      |
| 347 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?        | Done     | Done       | 0.9999979850632295 | 0      |
| 348 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?        | Done     | Done       | 0.9999979596442047 | 0      |
| 349 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?      | Done     | Done       | 0.9999980164757125 | 0      |
| 350 | Tensor<[1, 480, 7, 7]> self = ?,<br>Tensor<[1, 480, 7, 7]> other = ?          | Done     | Done       | 0.9999979759056411 | 0      |
| 351 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?          | Done     | Done       | 0.9999979789407482 | 0      |
| 352 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?              | Unknown  | Done       | 0.9999980348855904 | 0      |
| 353 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?          | Unknown  | Done       | 0.999998243328437  | 0      |
| 354 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Fallback   | 1.0                | -1     |
| 355 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?              | Unknown  | Done       | 0.9999979713153567 | 0      |
| 356 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?            | Done     | Done       | 0.9999980320345965 | 0      |
| 357 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?            | Unknown  | Done       | 0.9999979626587165 | 0      |
| 358 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?              | Done     | Done       | 0.9999980272666363 | 0      |
| 359 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 0.0                        | None     | Fallback   | 1.0                | -1     |
| 360 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | None     | Fallback   | 1.0                | -1     |
| 361 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | Done       | 0.9999979991429423 | 0      |
| 362 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ?  | Done     | Done       | 0.9999979950523759 | 0      |
| 363 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ?      | Done     | Done       | 0.9999979472284989 | 0      |
| 364 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999980090509168 | 0      |
| 365 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979599217258 | 0      |
| 366 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?      | Done     | Done       | 0.9999980259086159 | 0      |
| 367 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?      | Done     | Done       | 0.9999979828214339 | 0      |
| 368 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999980091000421 | 0      |
| 369 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.999998029718939  | 0      |
| 370 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?          | Done     | Done       | 0.9999980031579382 | 0      |
| 371 | Tensor<[1, 512, 8, 8]> self = ?,<br>Tensor<[1, 512, 8, 8]> other = ?          | Done     | Done       | 0.9999980416744585 | 0      |
| 372 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999980161727033 | 0      |
| 373 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?    | Done     | Done       | 0.9999979929445183 | 0      |
| 374 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                      | Unknown  | Done       | 0.9999980278260234 | 0      |
| 375 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?      | Done     | Done       | 0.9999979934973552 | 0      |
| 376 | Tensor<[1, 56, 14, 14]> self = ?,<br>Tensor<[1, 56, 14, 14]> other = ?        | Done     | Done       | 0.9999979463708111 | 0      |
| 377 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?        | Done     | Done       | 0.9999979965095288 | 0      |
| 378 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?      | Done     | Done       | 0.9999979807050289 | 0      |
| 379 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?        | Done     | Done       | 0.9999979780352725 | 0      |
| 380 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?      | Done     | Done       | 0.9999979595537565 | 0      |
| 381 | Tensor<[1, 58, 28, 28]> self = ?,<br>Tensor<[1, 58, 28, 28]> other = ?        | Done     | Done       | 0.9999979963824104 | 0      |
| 382 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Done     | Done       | 0.9999979600765843 | 0      |
| 383 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | None     | Fallback   | 1.0                | -1     |
| 384 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?            | Unknown  | Done       | 0.9999983569445311 | 0      |
| 385 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?            | Unknown  | Done       | 0.9999985155762835 | 0      |
| 386 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | Done       | 0.999996929001167  | 0      |
| 387 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?            | Unknown  | Done       | 0.9999974342083038 | 0      |
| 388 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999944459610067 | 0      |
| 389 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 390 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 391 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?              | Unknown  | Done       | 0.9999996496324038 | 0      |
| 392 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 393 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 394 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?           | Done     | Done       | 0.9999985000876603 | 0      |
| 395 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?          | Done     | Done       | 0.999997844231061  | 0      |
| 396 | Tensor<[1, 60, 28, 28]> self = ?,<br>Tensor<[1, 60, 28, 28]> other = ?        | Done     | Done       | 0.9999980027669921 | 0      |
| 397 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                         | None     | Fallback   | 1.0                | -1     |
| 398 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                       | None     | Fallback   | 1.0                | -1     |
| 399 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?    | Done     | Done       | 0.9999979907529472 | 0      |
| 400 | Tensor<[1, 64, 128, 128]> self = ?,<br>Tensor<[1, 64, 128, 128]> other = ?    | Done     | Done       | 0.999997989146614  | 0      |
| 401 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ?        | Done     | Done       | 0.9999980240734616 | 0      |
| 402 | Tensor<[1, 64, 147, 147]> self = ?,<br>Tensor<[1, 64, 147, 147]> other = ?    | Done     | Done       | 0.9999979867648986 | 0      |
| 403 | Tensor<[1, 64, 150, 150]> self = ?,<br>Tensor<[1, 64, 150, 150]> other = ?    | Done     | Done       | 0.9999980026512381 | 0      |
| 404 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999980480172508 | 0      |
| 405 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999978145636286 | 0      |
| 406 | Tensor<[1, 64, 224, 224]> self = ?,<br>Tensor<[1, 64, 224, 224]> other = ?    | Done     | Done       | 0.9999979941220595 | 0      |
| 407 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?    | Done     | Done       | 0.999997996683428  | 0      |
| 408 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?    | Done     | Done       | 0.9999979894071103 | 0      |
| 409 | Tensor<[1, 64, 28, 28]> self = ?,<br>Tensor<[1, 64, 28, 28]> other = ?        | Done     | Done       | 0.9999980361540406 | 0      |
| 410 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 411 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 412 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?        | Done     | Done       | 0.9999979651254484 | 0      |
| 413 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999981386259409 | 0      |
| 414 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 415 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 416 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999979218825872 | 0      |
| 417 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?    | Done     | Done       | 0.9999979911662022 | 0      |
| 418 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?        | Done     | Done       | 0.9999979457645204 | 0      |
| 419 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?        | Done     | Done       | 0.9999979964644665 | 0      |
| 420 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?      | Done     | Done       | 0.9999979793543167 | 0      |
| 421 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?        | Done     | Done       | 0.9999979738342375 | 0      |
| 422 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?        | Done     | Done       | 0.9999979726797085 | 0      |
| 423 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999977530660693 | 0      |
| 424 | Tensor<[1, 640, 7, 7]> self = ?,<br>Tensor<[1, 640, 7, 7]> other = ?          | Done     | Done       | 0.9999979723105812 | 0      |
| 425 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 426 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, s0, s1]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 427 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 428 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 429 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?      | Done     | Done       | 0.9999979881978025 | 0      |
| 430 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?      | Done     | Done       | 0.9999980000045152 | 0      |
| 431 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?          | Done     | Done       | 0.9999980168584613 | 0      |
| 432 | Tensor<[1, 68, 14, 14]> self = ?,<br>Tensor<[1, 68, 14, 14]> other = ?        | Done     | Done       | 0.9999979803342608 | 0      |
| 433 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?      | Done     | Done       | 0.9999979924137867 | 0      |
| 434 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                          | None     | Fallback   | 1.0                | -1     |
| 435 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?              | Done     | Done       | 0.9999980999615292 | 0      |
| 436 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?        | Done     | Done       | 0.9999980176854517 | 0      |
| 437 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?          | Done     | Done       | 0.999998014035343  | 0      |
| 438 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?                | Done     | Done       | 0.9999978395073386 | 0      |
| 439 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?        | Done     | Done       | 0.9999979198094642 | 0      |
| 440 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?        | Done     | Done       | 0.9999980042298175 | 0      |
| 441 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?        | Done     | Done       | 0.9999980000028573 | 0      |
| 442 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ?      | Done     | Done       | 0.9999980552952294 | 0      |
| 443 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?      | Done     | Done       | 0.9999980163890992 | 0      |
| 444 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?      | Done     | Done       | 0.9999980022332066 | 0      |
| 445 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?    | Done     | Done       | 0.9999979895149871 | 0      |
| 446 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?      | Done     | Done       | 0.9999979997063154 | 0      |
| 447 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                    | Done     | Done       | 0.9999979947850579 | 0      |
| 448 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?          | Done     | Done       | 0.9999980681170686 | 0      |
| 449 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                      | Unknown  | Done       | 0.999998500053513  | 0      |
| 450 | Tensor<[1, 78, 28, 28]> self = ?,<br>Tensor<[1, 78, 28, 28]> other = ?        | Done     | Done       | 0.9999980027225305 | 0      |
| 451 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?          | Done     | Done       | 0.9999980012969845 | 0      |
| 452 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?            | Unknown  | Done       | 0.9999982670826811 | 0      |
| 453 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?            | Unknown  | Done       | 0.9999981710284921 | 0      |
| 454 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999989782604077 | 0      |
| 455 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?              | Unknown  | Done       | 1.0                | 0      |
| 456 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999996243159248 | 0      |
| 457 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?              | Unknown  | Done       | 0.999999281575798  | 0      |
| 458 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 459 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                | N/A    |
| 460 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Done     | Done       | 0.9999979707804714 | 0      |
| 461 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?          | Done     | Done       | 0.9999982307184626 | 0      |
| 462 | Tensor<[1, 8, 112, 112]> self = ?,<br>Tensor<[1, 8, 112, 112]> other = ?      | Done     | Done       | 0.9999979667837652 | 0      |
| 463 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ?      | Done     | Done       | 0.9999979764620548 | 0      |
| 464 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?                | Done     | Done       | 0.9999979084386917 | 0      |
| 465 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?        | Done     | Done       | 0.9999980597652065 | 0      |
| 466 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?          | Done     | Done       | 0.9999980168020315 | 0      |
| 467 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?        | Done     | Done       | 0.9999980911210292 | 0      |
| 468 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?        | Done     | Done       | 0.9999979618875858 | 0      |
| 469 | Tensor<[1, 80, 15, 15]> self = ?,<br>Tensor<[1, 80, 15, 15]> other = ?        | Done     | Done       | 0.999997938326662  | 0      |
| 470 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?        | Done     | Done       | 0.9999979209088163 | 0      |
| 471 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?        | Done     | Done       | 0.9999979717214339 | 0      |
| 472 | Tensor<[1, 80, 7, 7]> self = ?,<br>Tensor<[1, 80, 7, 7]> other = ?            | Done     | Done       | 0.9999979837970092 | 0      |
| 473 | Tensor<[1, 88, 17, 17]> self = ?,<br>Tensor<[1, 88, 17, 17]> other = ?        | Done     | Done       | 0.9999979712786723 | 0      |
| 474 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?          | Done     | Done       | 0.9999979001521067 | 0      |
| 475 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?      | Done     | Done       | 0.9999979970341615 | 0      |
| 476 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?              | Done     | Done       | 0.9999981367527907 | 0      |
| 477 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                           | None     | Fallback   | 1.0                | -1     |
| 478 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                | Done     | Done       | 0.9999981446487843 | 0      |
| 479 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                         | None     | Fallback   | 1.0                | -1     |
| 480 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?            | Done     | Done       | 0.9999979877916583 | 0      |
| 481 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?              | Done     | Done       | 0.9999979232795887 | 0      |
| 482 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                          | None     | Fallback   | 1.0                | -1     |
| 483 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?              | Done     | Done       | 0.9999980190500354 | 0      |
| 484 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                          | None     | Fallback   | 1.0                | -1     |
| 485 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?              | Done     | Done       | 0.9999979354453049 | 0      |
| 486 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?                | Done     | Done       | 0.9999981236355405 | 0      |
| 487 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                          | None     | Fallback   | 1.0                | -1     |
| 488 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?              | Done     | Done       | 0.9999980207918726 | 0      |
| 489 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?          | Done     | Done       | 0.9999979781044106 | 0      |
| 490 | Tensor<[1, 92, 14, 14]> self = ?,<br>Tensor<[1, 92, 14, 14]> other = ?        | Done     | Done       | 0.9999980087120688 | 0      |
| 491 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?        | Done     | Done       | 0.99999802054857   | 0      |
| 492 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?        | Done     | Done       | 0.9999980150247698 | 0      |
| 493 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?        | Done     | Done       | 0.9999979792510061 | 0      |
| 494 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?            | Done     | Done       | 0.9999980142299395 | 0      |
| 495 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?          | Done     | Done       | 0.9999980139412686 | 0      |
| 496 | Tensor<[1, 98, 28, 28]> self = ?,<br>Tensor<[1, 98, 28, 28]> other = ?        | Done     | Done       | 0.9999979474449625 | 0      |
| 497 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor<[1, s0*s1, 1280]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 498 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor<[1, s0*s1, 640]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 499 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
| 500 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor<[1, s1*s2, 320]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 501 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor<[1, s1*s2, 640]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 502 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                                | None     | Fallback   | 1.0                | -1     |
| 503 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | None     | Fallback   | 1.0                | -1     |
| 504 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                      | Done     | Done       | 0.9999975190208793 | 0      |
| 505 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?            | Done     | Done       | 0.9999979482829765 | 0      |
| 506 | Tensor<[100]> self = ?,<br>Tensor other = 0.0                                 | Unknown  | Fallback   | 1.0                | -1     |
| 507 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                                | Unknown  | Fallback   | 1.0                | -1     |
| 508 | Tensor<[10]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Fallback   | 1.0                | -1     |
| 509 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?              | Done     | Done       | 0.9999980380306439 | 0      |
| 510 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                | -1     |
| 511 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                | -1     |
| 512 | Tensor<[12]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 513 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Done     | Done       | 0.9999979892785232 | 0      |
| 514 | Tensor<[136]> self = ?,<br>Tensor other = 0.0                                 | Unknown  | Fallback   | 1.0                | -1     |
| 515 | Tensor<[14]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 516 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                                | None     | Fallback   | 1.0                | -1     |
| 517 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | None     | Fallback   | 1.0                | -1     |
| 518 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                      | Done     | Done       | 0.9999985280598518 | 0      |
| 519 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?         | Done     | Done       | 0.999997977775861  | 0      |
| 520 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?         | Done     | Done       | 0.9999979567899965 | 0      |
| 521 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?         | Done     | Done       | 0.999997980230252  | 0      |
| 522 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?         | Done     | Done       | 0.9999979997210391 | 0      |
| 523 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                | -1     |
| 524 | Tensor<[16]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 525 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                                | Unknown  | Fallback   | 1.0                | -1     |
| 526 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | Fallback   | 1.0                | -1     |
| 527 | Tensor<[19]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Fallback   | 1.0                | -1     |
| 528 | Tensor<[1]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Fallback   | 1.0                | -1     |
| 529 | Tensor<[2*s0]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 530 | Tensor<[2*s1]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 531 | Tensor<[2*s2]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                | N/A    |
| 532 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                  | Unknown  | Fallback   | 1.0                | -1     |
| 533 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Fallback   | 1.0                | -1     |
| 534 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                      | Unknown  | Done       | 0.9999973636808396 | 0      |
| 535 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?              | Unknown  | Done       | 0.9999979506815303 | 0      |
| 536 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?                | Done     | Done       | 0.9999978776003214 | 0      |
| 537 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?                | Done     | Done       | 0.9999980464822623 | 0      |
| 538 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?              | Done     | Done       | 0.9999979239580731 | 0      |
| 539 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                      | Done     | Done       | 0.9999980498234666 | 0      |
| 540 | Tensor<[20]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Fallback   | 1.0                | -1     |
| 541 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.9999980503312109 | 0      |
| 542 | Tensor<[23]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 543 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                              | None     | Fallback   | 1.0                | -1     |
| 544 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                | -1     |
| 545 | Tensor<[25, 4]> self = ?,<br>Tensor<[25, 1]> other = ?                        | Unknown  | Done       | 0.9999977257960665 | 0      |
| 546 | Tensor<[28]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 547 | Tensor<[2]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Fallback   | 1.0                | -1     |
| 548 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Fallback   | 1.0                | -1     |
| 549 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                | -1     |
| 550 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                | -1     |
| 551 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                    | Unknown  | Done       | 0.9999979539438046 | 0      |
| 552 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                    | Done     | Done       | 0.9999979760969415 | 0      |
| 553 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                          | Unknown  | Done       | 0.9999978175740483 | 0      |
| 554 | Tensor<[32]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 555 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Done     | Done       | 0.9999980326756931 | 0      |
| 556 | Tensor<[38]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Fallback   | 1.0                | -1     |
| 557 | Tensor<[3]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Fallback   | 1.0                | -1     |
| 558 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?        | Done     | Done       | 0.9999979881350549 | 0      |
| 559 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?        | Done     | Done       | 0.9999979874678198 | 0      |
| 560 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?        | Done     | Done       | 0.9999979894903263 | 0      |
| 561 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?        | Done     | Done       | 0.9999980049034995 | 0      |
| 562 | Tensor<[40]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 563 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                | -1     |
| 564 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                | -1     |
| 565 | Tensor<[50]> self = ?,<br>Tensor other = 0.0                                  | Unknown  | Fallback   | 1.0                | -1     |
| 566 | Tensor<[56]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 567 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Done     | Done       | 0.9999979967321979 | 0      |
| 568 | Tensor<[5]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Fallback   | 1.0                | -1     |
| 569 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                | -1     |
| 570 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                   | Done     | Done       | 0.9999975552121368 | 0      |
| 571 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?         | Done     | Done       | 0.9999979784131044 | 0      |
| 572 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?         | Done     | Done       | 0.9999980095957225 | 0      |
| 573 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?         | Done     | Done       | 0.9999979885552367 | 0      |
| 574 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?         | Done     | Done       | 0.9999980048384757 | 0      |
| 575 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                | -1     |
| 576 | Tensor<[64]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                | -1     |
| 577 | Tensor<[68]> self = ?,<br>Tensor other = 0.0                                  | Unknown  | Fallback   | 1.0                | -1     |
| 578 | Tensor<[7]> self = ?,<br>Tensor other = 0.0                                   | Removed  | Fallback   | 1.0                | -1     |
| 579 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Fallback   | 1.0                | -1     |
| 580 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                | -1     |
| 581 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.9999980510707349 | 0      |
| 582 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                    | Unknown  | Done       | 0.9999981618993031 | 0      |
| 583 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                    | Done     | Done       | 0.9999980192795961 | 0      |
| 584 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                          | Unknown  | Done       | 0.9999980115736499 | 0      |
| 585 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.2697799949878862 | 0      |
| 586 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?            | Done     | Done       | 0.9999979965221099 | 0      |
| 587 | Tensor<[]> self = ?,<br>Tensor other = 1                                      | None     | Fallback   | 1.0                | -1     |
| 588 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | 1.0                | -1     |
| 589 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                        | Unknown  | Unknown    | N/A                | N/A    |
| 590 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                | N/A    |

