### aten.add.Tensor
|     | ATen Input Variations                                                         | Status   | Isolated   | PCC                 | Host   |
|----:|:------------------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                          | Unknown  | Done       | 1.0                 | 0      |
|   1 | Tensor<[0]> self = ?,<br>Tensor<[0]> other = ?                                | Unknown  | Done       | 1.0                 | 0      |
|   2 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999403329575649  | 0      |
|   3 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 0.5                         | Removed  | Done       | 0.9999983881128662  | 0      |
|   4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999923355303051  | 0      |
|   5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.999995162198666   | 0      |
|   6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999899209701585  | 0      |
|   7 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.999994067068337   | 0      |
|   8 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999980601466993  | 0      |
|   9 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?          | Unknown  | Done       | 0.9999981954259018  | 0      |
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
|  50 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027    | Done     | Done       | 0.9999999964051073  | 0      |
|  51 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997     | Done     | Done       | 0.9999990437660946  | 0      |
|  52 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994     | Done     | Done       | 0.9999998612531936  | 0      |
|  53 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.999994431630992   | 0      |
|  54 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | 0.999997917770796   | 0      |
|  55 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999865819666647  | 0      |
|  56 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 0.5                         | Removed  | Done       | 0.9999964747838009  | 0      |
|  57 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999959205106701  | 0      |
|  58 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.999994347776001   | 0      |
|  59 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999976298007639  | 0      |
|  60 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999953891458433  | 0      |
|  61 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?              | Unknown  | Done       | 0.9999980350520704  | 0      |
|  62 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                 | 0      |
|  63 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                | Unknown  | Done       | 0.9999979169798231  | 0      |
|  64 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Done     | Done       | 0.9999978992415126  | 0      |
|  65 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                   | Done     | Done       | 0.9999974892294966  | 0      |
|  66 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?            | Done     | Done       | 0.9999980719610716  | 0      |
|  67 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                 | 0      |
|  68 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?              | Done     | Done       | 0.9999980462387389  | 0      |
|  69 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?              | Done     | Done       | 0.9999978051142099  | 0      |
|  70 | Tensor<[1, 100, 14, 14]> self = ?,<br>Tensor<[1, 100, 14, 14]> other = ?      | Done     | Done       | 0.9999980247640111  | 0      |
|  71 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?        | Done     | Done       | 0.9999979651145122  | 0      |
|  72 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1.0                 | 0      |
|  73 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Done     | Done       | 1.0                 | 0      |
|  74 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ?    | Done     | Done       | 0.9999979382155313  | 0      |
|  75 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ?    | Done     | Done       | 0.9999979891533428  | 0      |
|  76 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?    | Done     | Done       | 0.9999980052563078  | 0      |
|  77 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?          | Done     | Done       | 0.9999980010131682  | 0      |
|  78 | Tensor<[1, 1024, 17, 17]> self = ?,<br>Tensor<[1, 1024, 17, 17]> other = ?    | Done     | Done       | 0.9999979944857064  | 0      |
|  79 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999980042173411  | 0      |
|  80 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999980056477203  | 0      |
|  81 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?    | Done     | Done       | 0.9999979903616004  | 0      |
|  82 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999980144121692  | 0      |
|  83 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 50, 68]> other = ?    | Done     | Done       | 0.999997995216498   | 0      |
|  84 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?        | Done     | Done       | 0.9999979692997802  | 0      |
|  85 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999978329064404  | 0      |
|  86 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?      | Done     | Done       | 0.9999979679843202  | 0      |
|  87 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?    | Done     | Done       | 0.9999980018134265  | 0      |
|  88 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                                 | Done     | Done       | 1.0                 | 0      |
|  89 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | 1.0                 | 0      |
|  90 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?      | Done     | Done       | 0.9999979749788358  | 0      |
|  91 | Tensor<[1, 112, 15, 15]> self = ?,<br>Tensor<[1, 112, 15, 15]> other = ?      | Done     | Done       | 0.9999980489831088  | 0      |
|  92 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?      | Done     | Done       | 0.9999980189895409  | 0      |
|  93 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ?      | Done     | Done       | 0.9999979896355535  | 0      |
|  94 | Tensor<[1, 116, 14, 14]> self = ?,<br>Tensor<[1, 116, 14, 14]> other = ?      | Done     | Done       | 0.9999981398833658  | 0      |
|  95 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999963509109555  | 0      |
|  96 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?          | Unknown  | Done       | 0.9999977495739082  | 0      |
|  97 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999999011917734  | 0      |
|  98 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?            | Unknown  | Done       | 0.9999982347377033  | 0      |
|  99 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999997443799384  | 0      |
| 100 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?            | Unknown  | Done       | 1.0                 | 0      |
| 101 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | 0.9999978232567046  | 0      |
| 102 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                 | N/A    |
| 103 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                 | N/A    |
| 104 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                 | N/A    |
| 105 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Done     | Done       | 0.9999974276848997  | 0      |
| 106 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?        | Done     | Done       | 0.9999980328900852  | 0      |
| 107 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ?          | Done     | Done       | 0.9999982088162928  | 0      |
| 108 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?              | Done     | Done       | 0.9999981306833439  | 0      |
| 109 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<[1, 1, 1, 14]> other = ?          | Done     | Done       | 0.9999976648676443  | 0      |
| 110 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor<[1, 12, 197, 197]> other = ?    | Done     | Done       | 0.9999979873160388  | 0      |
| 111 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?         | Done     | Done       | 0.999997910865257   | 0      |
| 112 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ?          | Done     | Done       | 0.9999979656804797  | 0      |
| 113 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999946974734026  | 0      |
| 114 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?            | Done     | Done       | 0.9999979658596655  | 0      |
| 115 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | 0.9999979914291809  | 0      |
| 116 | Tensor<[1, 12, 56, 56]> self = ?,<br>Tensor<[1, 12, 56, 56]> other = ?        | Done     | Done       | 0.9999980185442545  | 0      |
| 117 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ?             | Done     | Done       | 0.9999983340671043  | 0      |
| 118 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?              | Done     | Done       | 0.9999980044760093  | 0      |
| 119 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999980481676243  | 0      |
| 120 | Tensor<[1, 120, 17, 17]> self = ?,<br>Tensor<[1, 120, 17, 17]> other = ?      | Done     | Done       | 0.999998021392141   | 0      |
| 121 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?      | Done     | Done       | 0.9999979399882809  | 0      |
| 122 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?          | Done     | Done       | 0.9999979965544854  | 0      |
| 123 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?    | Done     | Done       | 0.9999979969551805  | 0      |
| 124 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                 | 0      |
| 125 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                 | 0      |
| 126 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979021420708  | 0      |
| 127 | Tensor<[1, 128, 112, 112]> self = ?,<br>Tensor<[1, 128, 112, 112]> other = ?  | Done     | Done       | 0.9999979999776926  | 0      |
| 128 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ?  | Done     | Done       | 0.9999979893178813  | 0      |
| 129 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979384762154  | 0      |
| 130 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979448677137  | 0      |
| 131 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ?      | Done     | Done       | 0.9999979691989863  | 0      |
| 132 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ?      | Done     | Done       | 0.999997977942687   | 0      |
| 133 | Tensor<[1, 128, 64, 64]> self = ?,<br>Tensor<[1, 128, 64, 64]> other = ?      | Done     | Done       | 0.9999979833960464  | 0      |
| 134 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?      | Done     | Done       | 0.9999979852869952  | 0      |
| 135 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999978729185132  | 0      |
| 136 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979605556881  | 0      |
| 137 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?        | Unknown  | Done       | 0.9999979918972566  | 0      |
| 138 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 139 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor<[1, 1280, s0, s1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 140 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 141 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor<[1, 1280, s1, s2]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 142 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ?    | Done     | Done       | 0.9999979957587924  | 0      |
| 143 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ?      | Done     | Done       | 0.9999979977975874  | 0      |
| 144 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?        | Done     | Done       | 0.9999979905436938  | 0      |
| 145 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?    | Done     | Done       | 0.9999979864974515  | 0      |
| 146 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?              | Done     | Done       | 0.999997877078289   | 0      |
| 147 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?      | Done     | Done       | 0.9999980175062916  | 0      |
| 148 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?      | Done     | Done       | 0.9999980068613151  | 0      |
| 149 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947628443471  | 0      |
| 150 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?            | Done     | Done       | 0.9999979914206016  | 0      |
| 151 | Tensor<[1, 14, 56, 56]> self = ?,<br>Tensor<[1, 14, 56, 56]> other = ?        | Done     | Done       | 0.9999979915735268  | 0      |
| 152 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?              | Done     | Done       | 0.9999979295970577  | 0      |
| 153 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?      | Done     | Done       | 0.9999980071364424  | 0      |
| 154 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?          | Done     | Done       | 0.9999979304999455  | 0      |
| 155 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?          | Done     | Done       | 0.9999979990810423  | 0      |
| 156 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999950001961427  | 0      |
| 157 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Done     | Done       | 0.9999979589891465  | 0      |
| 158 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                 | 0      |
| 159 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?              | Done     | Done       | 0.9999979942956224  | 0      |
| 160 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ?          | Done     | Done       | 0.999997990529395   | 0      |
| 161 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?             | Done     | Done       | 0.9999979947770984  | 0      |
| 162 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?        | Done     | Done       | 0.9999979691642715  | 0      |
| 163 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Tensor<[1, 1536, 8, 8]> other = ?        | Done     | Done       | 0.9999979904273241  | 0      |
| 164 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999963822301441  | 0      |
| 165 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?          | Unknown  | Done       | 0.9999980875865225  | 0      |
| 166 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999966496365543  | 0      |
| 167 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?            | Unknown  | Done       | 1.0                 | 0      |
| 168 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999953317919815  | 0      |
| 169 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?            | Unknown  | Done       | 0.9999999768847452  | 0      |
| 170 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999978853934685  | 0      |
| 171 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Done       | 0.9999955477008928  | 0      |
| 172 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                 | N/A    |
| 173 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                 | N/A    |
| 174 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                 | N/A    |
| 175 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Done     | Done       | 0.9999978651653738  | 0      |
| 176 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?        | Done     | Done       | 0.9999980493395021  | 0      |
| 177 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ?    | Done     | Done       | 0.9999980023618251  | 0      |
| 178 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?      | Done     | Done       | 0.9999980276365275  | 0      |
| 179 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?      | Done     | Done       | 0.9999980036233745  | 0      |
| 180 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ?    | Done     | Done       | 0.9999979797495919  | 0      |
| 181 | Tensor<[1, 16, 19, 19]> self = ?,<br>Tensor<[1, 1, 19, 19]> other = ?         | Done     | Done       | 0.9999980062842577  | 0      |
| 182 | Tensor<[1, 16, 197, 197]> self = ?,<br>Tensor<[1, 16, 197, 197]> other = ?    | Done     | Done       | 0.9999979940970825  | 0      |
| 183 | Tensor<[1, 16, 256, 256]> self = ?,<br>Tensor<[1, 1, 1, 256]> other = ?       | Done     | Done       | 0.9999980199387396  | 0      |
| 184 | Tensor<[1, 16, 28, 28]> self = ?,<br>Tensor<[1, 16, 28, 28]> other = ?        | Done     | Done       | 0.9999981020975113  | 0      |
| 185 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Done       | 0.9999973512199649  | 0      |
| 186 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Done     | Done       | 0.9999979818727253  | 0      |
| 187 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 188 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 189 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?              | Done     | Done       | 0.9999981190850272  | 0      |
| 190 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 191 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 192 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999983589475391  | 0      |
| 193 | Tensor<[1, 160, 14, 14]> self = ?,<br>Tensor<[1, 160, 14, 14]> other = ?      | Done     | Done       | 0.9999979587465702  | 0      |
| 194 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ?      | Done     | Done       | 0.9999979722564553  | 0      |
| 195 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ?      | Done     | Done       | 0.9999979929358817  | 0      |
| 196 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?      | Done     | Done       | 0.9999979654931002  | 0      |
| 197 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?          | Done     | Done       | 0.9999979321920744  | 0      |
| 198 | Tensor<[1, 160, 73, 73]> self = ?,<br>Tensor<[1, 160, 73, 73]> other = ?      | Done     | Done       | 0.9999979914885606  | 0      |
| 199 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999980688718999  | 0      |
| 200 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?          | Done     | Done       | 0.9999979903339593  | 0      |
| 201 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ?      | Done     | Done       | 0.9999979950993334  | 0      |
| 202 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?        | Done     | Done       | 0.9999979494962494  | 0      |
| 203 | Tensor<[1, 185, 28, 28]> self = ?,<br>Tensor<[1, 185, 28, 28]> other = ?      | Done     | Done       | 0.9999980239872124  | 0      |
| 204 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<[1, 19, 1024]> other = ?            | Done     | Done       | 0.9999979111495652  | 0      |
| 205 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ?      | Done     | Done       | 0.999998013496829   | 0      |
| 206 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ?      | Done     | Done       | 0.9999980220814496  | 0      |
| 207 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?      | Done     | Done       | 0.999998001869609   | 0      |
| 208 | Tensor<[1, 192, 7, 7]> self = ?,<br>Tensor<[1, 192, 7, 7]> other = ?          | Done     | Done       | 0.9999978032393929  | 0      |
| 209 | Tensor<[1, 192, 71, 71]> self = ?,<br>Tensor<[1, 192, 71, 71]> other = ?      | Done     | Done       | 0.9999979969478419  | 0      |
| 210 | Tensor<[1, 192, 8, 8]> self = ?,<br>Tensor<[1, 192, 8, 8]> other = ?          | Done     | Done       | 0.9999979944960706  | 0      |
| 211 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?        | Done     | Done       | 0.9999979895445453  | 0      |
| 212 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?          | Done     | Done       | 0.9999979910542297  | 0      |
| 213 | Tensor<[1, 196, 14, 14]> self = ?,<br>Tensor<[1, 196, 14, 14]> other = ?      | Done     | Done       | 0.9999979744999474  | 0      |
| 214 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ?            | Done     | Done       | 0.9999979580592875  | 0      |
| 215 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?          | Done     | Done       | 0.9999979776772058  | 0      |
| 216 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?            | Done     | Done       | 0.9999979898671736  | 0      |
| 217 | Tensor<[1, 19]> self = ?,<br>Tensor other = 2                                 | Removed  | Done       | 1.0                 | 0      |
| 218 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                 | 0      |
| 219 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                 | 0      |
| 220 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Done       | 1.0                 | 0      |
| 221 | Tensor<[1, 20, 28, 28]> self = ?,<br>Tensor<[1, 20, 28, 28]> other = ?        | Done     | Done       | 0.9999980195400705  | 0      |
| 222 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?        | Done     | Done       | 0.9999980297446255  | 0      |
| 223 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 0.0                       | Done     | Done       | 1.0                 | 0      |
| 224 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Done     | Done       | 1.0                 | 0      |
| 225 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.999997979716796   | 0      |
| 226 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?    | Done     | Done       | 0.9999979917063192  | 0      |
| 227 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999979852080767  | 0      |
| 228 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 25, 34]> other = ?    | Done     | Done       | 0.9999979813044714  | 0      |
| 229 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?        | Done     | Done       | 0.9999979780999484  | 0      |
| 230 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?          | Done     | Done       | 0.9999980036755088  | 0      |
| 231 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?             | Done     | Done       | 0.9999979962791887  | 0      |
| 232 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?      | Done     | Done       | 0.9999979644457788  | 0      |
| 233 | Tensor<[1, 208, 9, 9]> self = ?,<br>Tensor<[1, 208, 9, 9]> other = ?          | Done     | Done       | 0.9999979779353003  | 0      |
| 234 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?      | Done     | Done       | 0.9999979941018473  | 0      |
| 235 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?      | Done     | Done       | 0.9999979952578386  | 0      |
| 236 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?          | Done     | Done       | 0.9999977956500239  | 0      |
| 237 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                 | 0      |
| 238 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ?      | Done     | Done       | 0.9999980681103531  | 0      |
| 239 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?      | Done     | Done       | 0.9999979995221391  | 0      |
| 240 | Tensor<[1, 24, 112, 112]> self = ?,<br>Tensor<[1, 24, 112, 112]> other = ?    | Done     | Done       | 0.9999979852908724  | 0      |
| 241 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?        | Done     | Done       | 0.9999979904955573  | 0      |
| 242 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?        | Done     | Done       | 0.9999979847120917  | 0      |
| 243 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?        | Done     | Done       | 0.9999980109556541  | 0      |
| 244 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?        | Done     | Done       | 0.9999979970251809  | 0      |
| 245 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?        | Done     | Done       | 0.999998046487923   | 0      |
| 246 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?        | Done     | Done       | 0.9999979640154815  | 0      |
| 247 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?              | Done     | Done       | 0.9999978637893033  | 0      |
| 248 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?        | Done     | Done       | 0.9999980123313578  | 0      |
| 249 | Tensor<[1, 240, 14, 14]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?      | Done     | Done       | 0.9999979776949833  | 0      |
| 250 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?      | Done     | Done       | 0.9999979871595448  | 0      |
| 251 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?              | Done     | Done       | 0.999998110399808   | 0      |
| 252 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?        | Done     | Done       | 0.9999980369934718  | 0      |
| 253 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                 | 0      |
| 254 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                 | 0      |
| 255 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979636649209  | 0      |
| 256 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 100, 136]> other = ?  | Done     | Done       | 0.9999979913039619  | 0      |
| 257 | Tensor<[1, 256, 1024]> self = ?,<br>Tensor<[1, 256, 1024]> other = ?          | Done     | Done       | 0.9999979979977355  | 0      |
| 258 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ?  | Done     | Done       | 0.9999979921853928  | 0      |
| 259 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?          | Done     | Done       | 0.9999979823942858  | 0      |
| 260 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ?      | Done     | Done       | 0.9999979638098261  | 0      |
| 261 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?      | Done     | Done       | 0.9999980288095387  | 0      |
| 262 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?            | Done     | Done       | 0.9999980171218669  | 0      |
| 263 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979713489839  | 0      |
| 264 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ?  | Done     | Done       | 0.99999799553951    | 0      |
| 265 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979922410369  | 0      |
| 266 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 200, 272]> other = ?  | Done     | Done       | 0.9999979915294973  | 0      |
| 267 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?            | Done     | Done       | 0.9999979995753823  | 0      |
| 268 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.9999979693289607  | 0      |
| 269 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ?      | Done     | Done       | 0.9999979842356277  | 0      |
| 270 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?      | Done     | Done       | 0.9999979820092889  | 0      |
| 271 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?              | Done     | Done       | 0.9999979926805391  | 0      |
| 272 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?      | Done     | Done       | 0.9999979878159649  | 0      |
| 273 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999979670924816  | 0      |
| 274 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999980248871656  | 0      |
| 275 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 50, 68]> other = ?      | Done     | Done       | 0.999997991261555   | 0      |
| 276 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ?            | Done     | Done       | 0.9999979892022343  | 0      |
| 277 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?      | Done     | Done       | 0.9999979969476726  | 0      |
| 278 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?      | Done     | Done       | 0.9999979887417386  | 0      |
| 279 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?              | Done     | Done       | 0.9999980623642983  | 0      |
| 280 | Tensor<[1, 256, 7, 7]> self = ?,<br>Tensor<[1, 256, 7, 7]> other = ?          | Done     | Done       | 0.9999980024398026  | 0      |
| 281 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?      | Done     | Done       | 0.9999979939537428  | 0      |
| 282 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999979710818162  | 0      |
| 283 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ?      | Done     | Done       | 0.9999979661008799  | 0      |
| 284 | Tensor<[1, 272, 7, 7]> self = ?,<br>Tensor<[1, 272, 7, 7]> other = ?          | Done     | Done       | 0.999998030155547   | 0      |
| 285 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?      | Done     | Done       | 0.9999980123188051  | 0      |
| 286 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?      | Done     | Done       | 0.9999980004983701  | 0      |
| 287 | Tensor<[1, 28, 28, 28]> self = ?,<br>Tensor<[1, 28, 28, 28]> other = ?        | Done     | Done       | 0.9999979429169974  | 0      |
| 288 | Tensor<[1, 288, 14, 14]> self = ?,<br>Tensor<[1, 288, 14, 14]> other = ?      | Done     | Done       | 0.9999980183138185  | 0      |
| 289 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?    | Done     | Done       | 0.9999979955186351  | 0      |
| 290 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?      | Done     | Done       | 0.9999979797373844  | 0      |
| 291 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?      | Done     | Done       | 0.9999979755108143  | 0      |
| 292 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1, 3, 800, 1066]> other = ?    | Done     | Done       | 0.9999979949831873  | 0      |
| 293 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?            | Done     | Done       | 0.9999980059175421  | 0      |
| 294 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?        | Done     | Done       | 0.9999980204098673  | 0      |
| 295 | Tensor<[1, 32, 112, 112]> self = ?,<br>Tensor<[1, 32, 112, 112]> other = ?    | Done     | Done       | 0.9999979690183566  | 0      |
| 296 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?    | Done     | Done       | 0.9999979913505551  | 0      |
| 297 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?            | Done     | Done       | 0.9999979386710902  | 0      |
| 298 | Tensor<[1, 32, 256, 256]> self = ?,<br>Tensor<[1, 32, 256, 256]> other = ?    | Done     | Done       | 0.9999979879084027  | 0      |
| 299 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ?        | Done     | Done       | 0.9999980134774542  | 0      |
| 300 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?      | Done     | Done       | 0.9999980226163322  | 0      |
| 301 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?      | Done     | Done       | 0.9999979897242325  | 0      |
| 302 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?        | Done     | Done       | 0.9999980177974362  | 0      |
| 303 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?        | Done     | Done       | 0.9999979741162635  | 0      |
| 304 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999948197074546  | 0      |
| 305 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947376916347  | 0      |
| 306 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?        | Done     | Done       | 0.9999980178419529  | 0      |
| 307 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?        | Done     | Done       | 0.9999979960259591  | 0      |
| 308 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?        | Done     | Done       | 0.9999980004035895  | 0      |
| 309 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?      | Done     | Done       | 0.9999980092163738  | 0      |
| 310 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Done       | 0.9999979214959268  | 0      |
| 311 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?      | Unknown  | Done       | 0.9999979924588559  | 0      |
| 312 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 313 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor<[1, 320, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 314 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?      | Done     | Done       | 0.9999979788435109  | 0      |
| 315 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?      | Done     | Done       | 0.9999979931152712  | 0      |
| 316 | Tensor<[1, 34, 28, 28]> self = ?,<br>Tensor<[1, 34, 28, 28]> other = ?        | Done     | Done       | 0.999997969699875   | 0      |
| 317 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?        | Done     | Done       | 0.9999980250201632  | 0      |
| 318 | Tensor<[1, 36, 56, 56]> self = ?,<br>Tensor<[1, 36, 56, 56]> other = ?        | Done     | Done       | 0.9999979983162135  | 0      |
| 319 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?        | Done     | Done       | 0.999997990979237   | 0      |
| 320 | Tensor<[1, 384, 35, 35]> self = ?,<br>Tensor<[1, 384, 35, 35]> other = ?      | Done     | Done       | 0.9999979900948246  | 0      |
| 321 | Tensor<[1, 384, 8, 8]> self = ?,<br>Tensor<[1, 384, 8, 8]> other = ?          | Done     | Done       | 0.9999978691424428  | 0      |
| 322 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 323 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 324 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 325 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 326 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?                | Unknown  | Done       | 0.999997999924708   | 0      |
| 327 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?                   | Unknown  | Done       | 0.99999809146781    | 0      |
| 328 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ?        | Done     | Done       | 0.9999979911760976  | 0      |
| 329 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?        | Done     | Done       | 0.9999979829307587  | 0      |
| 330 | Tensor<[1, 40, 30, 30]> self = ?,<br>Tensor<[1, 40, 30, 30]> other = ?        | Done     | Done       | 0.9999979879452255  | 0      |
| 331 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?        | Done     | Done       | 0.9999979859970289  | 0      |
| 332 | Tensor<[1, 40, 56, 56]> self = ?,<br>Tensor<[1, 40, 56, 56]> other = ?        | Done     | Done       | 0.9999979860023281  | 0      |
| 333 | Tensor<[1, 400, 7, 7]> self = ?,<br>Tensor<[1, 400, 7, 7]> other = ?          | Done     | Done       | 0.999997991396671   | 0      |
| 334 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ?      | Done     | Done       | 0.9999979358796126  | 0      |
| 335 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999980248212259  | 0      |
| 336 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?          | Unknown  | Done       | 0.9999979827389629  | 0      |
| 337 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?            | Done     | Done       | 0.9999980018148169  | 0      |
| 338 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ?      | Done     | Done       | 0.9999979752995338  | 0      |
| 339 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?          | Done     | Done       | 0.99999797877503    | 0      |
| 340 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?      | Done     | Done       | 0.9999979753542997  | 0      |
| 341 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999947511170575  | 0      |
| 342 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | 0.9999980284987776  | 0      |
| 343 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | 0.9999980398823691  | 0      |
| 344 | Tensor<[1, 46, 28, 28]> self = ?,<br>Tensor<[1, 46, 28, 28]> other = ?        | Done     | Done       | 0.9999979791369568  | 0      |
| 345 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ?        | Done     | Done       | 0.9999980762239176  | 0      |
| 346 | Tensor<[1, 48, 33, 33]> self = ?,<br>Tensor<[1, 48, 33, 33]> other = ?        | Done     | Done       | 0.999998066650305   | 0      |
| 347 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?        | Done     | Done       | 0.9999979770481046  | 0      |
| 348 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?        | Done     | Done       | 0.9999979984718801  | 0      |
| 349 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?      | Done     | Done       | 0.9999980403105172  | 0      |
| 350 | Tensor<[1, 480, 7, 7]> self = ?,<br>Tensor<[1, 480, 7, 7]> other = ?          | Done     | Done       | 0.9999978830653096  | 0      |
| 351 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?          | Done     | Done       | 0.9999979731852919  | 0      |
| 352 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?              | Unknown  | Done       | 0.9999980860823431  | 0      |
| 353 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?          | Unknown  | Done       | 0.9999981381335903  | 0      |
| 354 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999946418275472  | 0      |
| 355 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?              | Unknown  | Done       | 0.999997964941018   | 0      |
| 356 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?            | Done     | Done       | 0.9999979594353351  | 0      |
| 357 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?            | Unknown  | Done       | 0.9999979989198576  | 0      |
| 358 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?              | Done     | Done       | 0.9999979904246081  | 0      |
| 359 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 0.0                        | Done     | Done       | 1.0                 | 0      |
| 360 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Done     | Done       | 1.0                 | 0      |
| 361 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | Done       | 0.9999980178697161  | 0      |
| 362 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 100, 136]> other = ?  | Done     | Done       | 0.9999979921393842  | 0      |
| 363 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ?      | Done     | Done       | 0.9999980347034145  | 0      |
| 364 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979489217057  | 0      |
| 365 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979712879763  | 0      |
| 366 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?      | Done     | Done       | 0.9999979789418691  | 0      |
| 367 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?      | Done     | Done       | 0.9999979844949576  | 0      |
| 368 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.999997960017966   | 0      |
| 369 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999979633312019  | 0      |
| 370 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?          | Done     | Done       | 0.9999980075555349  | 0      |
| 371 | Tensor<[1, 512, 8, 8]> self = ?,<br>Tensor<[1, 512, 8, 8]> other = ?          | Done     | Done       | 0.9999980156573097  | 0      |
| 372 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999979662954176  | 0      |
| 373 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?    | Done     | Done       | 0.9999979954917234  | 0      |
| 374 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                      | Unknown  | Done       | 0.9999981841363043  | 0      |
| 375 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?      | Done     | Done       | 0.9999979933562345  | 0      |
| 376 | Tensor<[1, 56, 14, 14]> self = ?,<br>Tensor<[1, 56, 14, 14]> other = ?        | Done     | Done       | 0.9999978814816401  | 0      |
| 377 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?        | Done     | Done       | 0.9999979748555958  | 0      |
| 378 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?      | Done     | Done       | 0.9999979942583627  | 0      |
| 379 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?        | Done     | Done       | 0.9999980193390794  | 0      |
| 380 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?      | Done     | Done       | 0.9999979607860117  | 0      |
| 381 | Tensor<[1, 58, 28, 28]> self = ?,<br>Tensor<[1, 58, 28, 28]> other = ?        | Done     | Done       | 0.9999979809553472  | 0      |
| 382 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Done     | Done       | 0.9999980502955028  | 0      |
| 383 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Done     | Done       | 0.9999956462656946  | 0      |
| 384 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?            | Unknown  | Done       | 0.9999970003531187  | 0      |
| 385 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?            | Unknown  | Done       | 0.9999982264542434  | 0      |
| 386 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | Done       | 0.9999976925512529  | 0      |
| 387 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?            | Unknown  | Done       | 0.9999990056807485  | 0      |
| 388 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 1.0                 | 0      |
| 389 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?              | Unknown  | Done       | 1.0                 | 0      |
| 390 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999985411961273  | 0      |
| 391 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?              | Unknown  | Done       | 0.999998627681759   | 0      |
| 392 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 393 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 394 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?           | Done     | Done       | 0.9999975503498385  | 0      |
| 395 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?          | Done     | Done       | 0.9999982636507398  | 0      |
| 396 | Tensor<[1, 60, 28, 28]> self = ?,<br>Tensor<[1, 60, 28, 28]> other = ?        | Done     | Done       | 0.9999979815550055  | 0      |
| 397 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 0.0                         | Done     | Done       | 1.0                 | 0      |
| 398 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                       | Done     | Done       | 1.0                 | 0      |
| 399 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?    | Done     | Done       | 0.999997986410919   | 0      |
| 400 | Tensor<[1, 64, 128, 128]> self = ?,<br>Tensor<[1, 64, 128, 128]> other = ?    | Done     | Done       | 0.9999979948408458  | 0      |
| 401 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ?        | Done     | Done       | 0.9999978917144378  | 0      |
| 402 | Tensor<[1, 64, 147, 147]> self = ?,<br>Tensor<[1, 64, 147, 147]> other = ?    | Done     | Done       | 0.9999980028297588  | 0      |
| 403 | Tensor<[1, 64, 150, 150]> self = ?,<br>Tensor<[1, 64, 150, 150]> other = ?    | Done     | Done       | 0.9999979936613551  | 0      |
| 404 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999980025949797  | 0      |
| 405 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999979597533164  | 0      |
| 406 | Tensor<[1, 64, 224, 224]> self = ?,<br>Tensor<[1, 64, 224, 224]> other = ?    | Done     | Done       | 0.9999979922834098  | 0      |
| 407 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?    | Done     | Done       | 0.9999979930971692  | 0      |
| 408 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?    | Done     | Done       | 0.9999979894460157  | 0      |
| 409 | Tensor<[1, 64, 28, 28]> self = ?,<br>Tensor<[1, 64, 28, 28]> other = ?        | Done     | Done       | 0.9999980555400622  | 0      |
| 410 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 411 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 412 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?        | Done     | Done       | 0.9999980016337491  | 0      |
| 413 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999979177831645  | 0      |
| 414 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 415 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 416 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999980315495921  | 0      |
| 417 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?    | Done     | Done       | 0.9999979917078581  | 0      |
| 418 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?        | Done     | Done       | 0.9999980363016934  | 0      |
| 419 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?        | Done     | Done       | 0.9999980049872604  | 0      |
| 420 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?      | Done     | Done       | 0.9999979952117374  | 0      |
| 421 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?        | Done     | Done       | 0.9999979811423234  | 0      |
| 422 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?        | Done     | Done       | 0.9999979932337857  | 0      |
| 423 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Done     | Done       | 0.9999981841231586  | 0      |
| 424 | Tensor<[1, 640, 7, 7]> self = ?,<br>Tensor<[1, 640, 7, 7]> other = ?          | Done     | Done       | 0.9999980234175901  | 0      |
| 425 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 426 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor<[1, 640, s0, s1]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 427 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 428 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor<[1, 640, s1, s2]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 429 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?      | Done     | Done       | 0.9999980132247951  | 0      |
| 430 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?      | Done     | Done       | 0.9999979873391268  | 0      |
| 431 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?          | Done     | Done       | 0.9999980652373861  | 0      |
| 432 | Tensor<[1, 68, 14, 14]> self = ?,<br>Tensor<[1, 68, 14, 14]> other = ?        | Done     | Done       | 0.999998005139318   | 0      |
| 433 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?      | Done     | Done       | 0.9999979801486292  | 0      |
| 434 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947667797813  | 0      |
| 435 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?              | Done     | Done       | 0.9999979147127731  | 0      |
| 436 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?        | Done     | Done       | 0.999997991394337   | 0      |
| 437 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?          | Done     | Done       | 0.9999979905369538  | 0      |
| 438 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?                | Done     | Done       | 0.9999978357811641  | 0      |
| 439 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?        | Done     | Done       | 0.9999980427166981  | 0      |
| 440 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?        | Done     | Done       | 0.9999979798671862  | 0      |
| 441 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?        | Done     | Done       | 0.9999979930332826  | 0      |
| 442 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ?      | Done     | Done       | 0.9999979953084595  | 0      |
| 443 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?      | Done     | Done       | 0.9999980004898772  | 0      |
| 444 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?      | Done     | Done       | 0.9999979820637543  | 0      |
| 445 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?    | Done     | Done       | 0.9999980009714172  | 0      |
| 446 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?      | Done     | Done       | 0.9999980253189686  | 0      |
| 447 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                    | Done     | Done       | 0.9999979910754414  | 0      |
| 448 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?          | Done     | Done       | 0.999997963336995   | 0      |
| 449 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                      | Unknown  | Done       | 0.9999978211004577  | 0      |
| 450 | Tensor<[1, 78, 28, 28]> self = ?,<br>Tensor<[1, 78, 28, 28]> other = ?        | Done     | Done       | 0.9999979899556716  | 0      |
| 451 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?          | Done     | Done       | 0.9999980491064218  | 0      |
| 452 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?            | Unknown  | Done       | 0.9999982340403667  | 0      |
| 453 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?            | Unknown  | Done       | 0.9999984309107387  | 0      |
| 454 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.999995975360423   | 0      |
| 455 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?              | Unknown  | Done       | 0.999995234272442   | 0      |
| 456 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999999926464752  | 0      |
| 457 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?              | Unknown  | Done       | 0.99999685028697    | 0      |
| 458 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 459 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 460 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Done     | Done       | 0.9999978171824867  | 0      |
| 461 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?          | Done     | Done       | 0.9999978597808101  | 0      |
| 462 | Tensor<[1, 8, 112, 112]> self = ?,<br>Tensor<[1, 8, 112, 112]> other = ?      | Done     | Done       | 0.999997947470499   | 0      |
| 463 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ?      | Done     | Done       | 0.999997986547152   | 0      |
| 464 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?                | Done     | Done       | 0.9999978268696296  | 0      |
| 465 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?        | Done     | Done       | 0.9999979574662351  | 0      |
| 466 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?          | Done     | Done       | 0.9999979795676001  | 0      |
| 467 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?        | Done     | Done       | 0.9999980112013657  | 0      |
| 468 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?        | Done     | Done       | 0.9999980746202946  | 0      |
| 469 | Tensor<[1, 80, 15, 15]> self = ?,<br>Tensor<[1, 80, 15, 15]> other = ?        | Done     | Done       | 0.9999979491043065  | 0      |
| 470 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?        | Done     | Done       | 0.9999980131244075  | 0      |
| 471 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?        | Done     | Done       | 0.9999980035778623  | 0      |
| 472 | Tensor<[1, 80, 7, 7]> self = ?,<br>Tensor<[1, 80, 7, 7]> other = ?            | Done     | Done       | 0.9999981554154735  | 0      |
| 473 | Tensor<[1, 88, 17, 17]> self = ?,<br>Tensor<[1, 88, 17, 17]> other = ?        | Done     | Done       | 0.9999980255215684  | 0      |
| 474 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?          | Done     | Done       | 0.9999980015746097  | 0      |
| 475 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?      | Done     | Done       | 0.9999979995729097  | 0      |
| 476 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?              | Done     | Done       | 0.9999978405429754  | 0      |
| 477 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                           | Done     | Done       | 0.9999949916859182  | 0      |
| 478 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                | Done     | Done       | 0.9999980984280317  | 0      |
| 479 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999948486886469  | 0      |
| 480 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?            | Done     | Done       | 0.9999979424161385  | 0      |
| 481 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?              | Done     | Done       | 0.9999979896565163  | 0      |
| 482 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947312272445  | 0      |
| 483 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?              | Done     | Done       | 0.9999979826393244  | 0      |
| 484 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999948925813544  | 0      |
| 485 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?              | Done     | Done       | 0.9999979238926485  | 0      |
| 486 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?                | Done     | Done       | 0.9999978567423009  | 0      |
| 487 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999949038748598  | 0      |
| 488 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?              | Done     | Done       | 0.9999980055519375  | 0      |
| 489 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?          | Done     | Done       | 0.999997977856168   | 0      |
| 490 | Tensor<[1, 92, 14, 14]> self = ?,<br>Tensor<[1, 92, 14, 14]> other = ?        | Done     | Done       | 0.9999980614686115  | 0      |
| 491 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?        | Done     | Done       | 0.9999980536415903  | 0      |
| 492 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?        | Done     | Done       | 0.9999980073408552  | 0      |
| 493 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?        | Done     | Done       | 0.9999979880200164  | 0      |
| 494 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?            | Done     | Done       | 0.9999978165054955  | 0      |
| 495 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?          | Done     | Done       | 0.9999979521473653  | 0      |
| 496 | Tensor<[1, 98, 28, 28]> self = ?,<br>Tensor<[1, 98, 28, 28]> other = ?        | Done     | Done       | 0.9999980019003891  | 0      |
| 497 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor<[1, s0*s1, 1280]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 498 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor<[1, s0*s1, 640]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 499 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?      | Unknown  | Unknown    | N/A                 | N/A    |
| 500 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor<[1, s1*s2, 320]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 501 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor<[1, s1*s2, 640]> other = ?        | Unknown  | Unknown    | N/A                 | N/A    |
| 502 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                                | Done     | Done       | 1.0                 | 0      |
| 503 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Done     | Done       | 0.9999147741713915  | 0      |
| 504 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                      | Done     | Done       | 0.9999953012300904  | 0      |
| 505 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?            | Done     | Done       | 0.9999979609955767  | 0      |
| 506 | Tensor<[100]> self = ?,<br>Tensor other = 0.0                                 | Unknown  | Done       | 1.0                 | 0      |
| 507 | Tensor<[1066]> self = ?,<br>Tensor other = 0.5                                | Unknown  | Done       | 0.9999978105621979  | 0      |
| 508 | Tensor<[10]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | 1.0                 | 0      |
| 509 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?              | Done     | Done       | 0.9999978024352657  | 0      |
| 510 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999986440275246  | 0      |
| 511 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999981055742865  | 0      |
| 512 | Tensor<[12]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 513 | Tensor<[13600, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                | Done     | Done       | 0.9999979051932177  | 0      |
| 514 | Tensor<[136]> self = ?,<br>Tensor other = 0.0                                 | Unknown  | Done       | 1.0                 | 0      |
| 515 | Tensor<[14]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                 | -1     |
| 516 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                                | Done     | Done       | 1.0                 | 0      |
| 517 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | Done     | Done       | 0.9999145437711364  | 0      |
| 518 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                      | Done     | Done       | 0.9999975108843723  | 0      |
| 519 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?         | Done     | Done       | 0.9999980006692812  | 0      |
| 520 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?         | Done     | Done       | 0.9999980034665829  | 0      |
| 521 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?         | Done     | Done       | 0.999997958329505   | 0      |
| 522 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?         | Done     | Done       | 0.9999979840120842  | 0      |
| 523 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999986577990738  | 0      |
| 524 | Tensor<[16]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 525 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                 | 0      |
| 526 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 0.9996145707702705  | 0      |
| 527 | Tensor<[19]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | 0.9999955783120569  | 0      |
| 528 | Tensor<[1]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | 1.0                 | 0      |
| 529 | Tensor<[2*s0]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                 | N/A    |
| 530 | Tensor<[2*s1]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                 | N/A    |
| 531 | Tensor<[2*s2]> self = ?,<br>Tensor other = 0.0                                | Unknown  | Unknown    | N/A                 | N/A    |
| 532 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                 | 0      |
| 533 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 0.9991246950819502  | 0      |
| 534 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                      | Unknown  | Done       | 0.9999978962943459  | 0      |
| 535 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?              | Unknown  | Done       | 0.9999979833298629  | 0      |
| 536 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?                | Done     | Done       | 0.9999980555268976  | 0      |
| 537 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?                | Done     | Done       | 0.99999801524226    | 0      |
| 538 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?              | Done     | Done       | 0.9999978028289437  | 0      |
| 539 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                      | Done     | Done       | 0.9999979833234193  | 0      |
| 540 | Tensor<[20]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | 0.9999967904773326  | 0      |
| 541 | Tensor<[221, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.9999978022965509  | 0      |
| 542 | Tensor<[23]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 543 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                              | Done     | Done       | 0.9780332958628277  | 0      |
| 544 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999961264881245  | 0      |
| 545 | Tensor<[25, 4]> self = ?,<br>Tensor<[25, 1]> other = ?                        | Unknown  | Done       | 0.9999963748789835  | 0      |
| 546 | Tensor<[28]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                 | -1     |
| 547 | Tensor<[2]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | 1.0                 | 0      |
| 548 | Tensor<[300]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Fallback   | 1.0                 | -1     |
| 549 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Done       | 0.9999974257611856  | 0      |
| 550 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Fallback   | 1.0                 | -1     |
| 551 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                    | Unknown  | Done       | 0.9999978530694664  | 0      |
| 552 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                    | Done     | Done       | 0.9999980115165081  | 0      |
| 553 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                          | Unknown  | Done       | 0.9999978637828961  | 0      |
| 554 | Tensor<[32]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 555 | Tensor<[3400, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                 | Done     | Done       | 0.9999981338252035  | 0      |
| 556 | Tensor<[38]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | 0.9999968466440099  | 0      |
| 557 | Tensor<[3]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | 0.9998578137049026  | 0      |
| 558 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?        | Done     | Done       | 0.9999980076100536  | 0      |
| 559 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?        | Done     | Done       | 0.9999979835619875  | 0      |
| 560 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?        | Done     | Done       | 0.9999980103678934  | 0      |
| 561 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?        | Done     | Done       | 0.9999979787345454  | 0      |
| 562 | Tensor<[40]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 563 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Done       | 0.999999616578335   | 0      |
| 564 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.9999974708676947  | 0      |
| 565 | Tensor<[50]> self = ?,<br>Tensor other = 0.0                                  | Unknown  | Done       | 1.0                 | 0      |
| 566 | Tensor<[56]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Fallback   | 1.0                 | -1     |
| 567 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Done     | Done       | 0.9999980385139176  | 0      |
| 568 | Tensor<[5]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | 0.9999976858496179  | 0      |
| 569 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Done       | 0.999998731232328   | 0      |
| 570 | Tensor<[63, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                   | Done     | Done       | 0.9999981638401365  | 0      |
| 571 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?         | Done     | Done       | 0.9999980007052698  | 0      |
| 572 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?         | Done     | Done       | 0.9999979898447867  | 0      |
| 573 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?         | Done     | Done       | 0.9999980082046186  | 0      |
| 574 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?         | Done     | Done       | 0.9999979876284751  | 0      |
| 575 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                                 | Removed  | Done       | 0.999997974218532   | 0      |
| 576 | Tensor<[64]> self = ?,<br>Tensor other = 0.0                                  | Removed  | Done       | 1.0                 | 0      |
| 577 | Tensor<[68]> self = ?,<br>Tensor other = 0.0                                  | Unknown  | Done       | 1.0                 | 0      |
| 578 | Tensor<[7]> self = ?,<br>Tensor other = 0.0                                   | Removed  | Fallback   | 1.0                 | -1     |
| 579 | Tensor<[800]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Fallback   | 1.0                 | -1     |
| 580 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Done       | 0.9999978635974058  | 0      |
| 581 | Tensor<[850, 1, 4]> self = ?,<br>Tensor<[1, 9, 4]> other = ?                  | Done     | Done       | 0.9999979644410567  | 0      |
| 582 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                    | Unknown  | Done       | 0.9999979591265226  | 0      |
| 583 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                    | Done     | Done       | 0.999998014910837   | 0      |
| 584 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                          | Unknown  | Done       | 0.9999979867921044  | 0      |
| 585 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.27030540951579346 | 0      |
| 586 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?            | Done     | Done       | 0.9999979921323088  | 0      |
| 587 | Tensor<[]> self = ?,<br>Tensor other = 1                                      | None     | Fallback   | 1.0                 | -1     |
| 588 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | 1.0                 | -1     |
| 589 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                        | Unknown  | Unknown    | N/A                 | N/A    |
| 590 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                 | N/A    |

