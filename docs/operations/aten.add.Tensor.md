### aten.add.Tensor
|     | ATen Input Variations                                                         | Status   | Isolated   | PCC                 | Host   |
|----:|:------------------------------------------------------------------------------|:---------|:-----------|:--------------------|:-------|
|   0 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -6.0                        | Done     | Unknown    | N/A                 | N/A    |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1                           | Done     | Unknown    | N/A                 | N/A    |
|   2 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.0                         | Done     | Unknown    | N/A                 | N/A    |
|   3 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 2                           | Done     | Unknown    | N/A                 | N/A    |
|   4 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 0.9999590847375337  | 0      |
|   5 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999992356340069  | 0      |
|   6 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999932863643535  | 0      |
|   7 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999921442433064  | 0      |
|   8 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999951039539051  | 0      |
|   9 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?              | Unknown  | Done       | 0.9999983589784526  | 0      |
|  10 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Unknown    | N/A                 | N/A    |
|  11 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1                           | Done     | Unknown    | N/A                 | N/A    |
|  12 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Unknown    | N/A                 | N/A    |
|  13 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 2                           | Done     | Unknown    | N/A                 | N/A    |
|  14 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?          | Unknown  | Done       | 0.9999973718034337  | 0      |
|  15 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839              | Done     | Done       | 1.0                 | 0      |
|  16 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032              | Done     | Done       | 1.0                 | 0      |
|  17 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226              | Done     | Done       | 1.0                 | 0      |
|  18 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323              | Done     | Done       | 1.0                 | 0      |
|  19 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516              | Done     | Done       | 1.0                 | 0      |
|  20 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161              | Done     | Done       | 1.0                 | 0      |
|  21 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581              | Done     | Done       | 1.0                 | 0      |
|  22 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                           | Unknown  | Done       | 1.0                 | 0      |
|  23 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027    | Done     | Done       | 0.9999999962641166  | 0      |
|  24 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997     | Done     | Done       | 0.9999990379050482  | 0      |
|  25 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994     | Done     | Done       | 0.9999998631396838  | 0      |
|  26 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999947238267014  | 0      |
|  27 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?              | Unknown  | Done       | 0.9999979765770752  | 0      |
|  28 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -6.0                        | Done     | Done       | 1.0                 | 0      |
|  29 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.999995538247161   | 0      |
|  30 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999955814943479  | 0      |
|  31 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 2                           | Done     | Done       | 0.9999923718019323  | 0      |
|  32 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.9999946276296564  | 0      |
|  33 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?              | Unknown  | Done       | 0.9999979656697178  | 0      |
|  34 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                 | 0      |
|  35 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                | Unknown  | Done       | 0.9999971606399125  | 0      |
|  36 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                | Unknown  | Done       | 0.9999981991296445  | 0      |
|  37 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                   | Unknown  | Done       | 0.9999983992051377  | 0      |
|  38 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?            | Unknown  | Done       | 0.9999980266794716  | 0      |
|  39 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                 | 0      |
|  40 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?              | Unknown  | Done       | 0.9999977296843138  | 0      |
|  41 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?              | Done     | Done       | 0.9999978797536009  | 0      |
|  42 | Tensor<[1, 100, 14, 14]> self = ?,<br>Tensor<[1, 100, 14, 14]> other = ?      | Done     | Done       | 0.9999979797904878  | 0      |
|  43 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?        | Done     | Done       | 0.9999980283687775  | 0      |
|  44 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Removed  | Done       | 1.0                 | 0      |
|  45 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ?    | Done     | Done       | 0.9999979636424763  | 0      |
|  46 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ?    | Done     | Done       | 0.9999980024340521  | 0      |
|  47 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?    | Done     | Done       | 0.9999979883447099  | 0      |
|  48 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?          | Done     | Done       | 0.9999980266327716  | 0      |
|  49 | Tensor<[1, 1024, 17, 17]> self = ?,<br>Tensor<[1, 1024, 17, 17]> other = ?    | Done     | Done       | 0.9999979808237782  | 0      |
|  50 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999979910452989  | 0      |
|  51 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999979536240872  | 0      |
|  52 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?    | Done     | Done       | 0.9999979993810886  | 0      |
|  53 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?        | Done     | Done       | 0.9999979801233128  | 0      |
|  54 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                    | Unknown  | Done       | 0.9999980682071549  | 0      |
|  55 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?      | Done     | Done       | 0.9999979811006691  | 0      |
|  56 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?    | Done     | Done       | 0.9999979968141176  | 0      |
|  57 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                                 | Done     | Done       | 1.0                 | 0      |
|  58 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | 0.9999938235660804  | 0      |
|  59 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?      | Done     | Done       | 0.9999980897271414  | 0      |
|  60 | Tensor<[1, 112, 15, 15]> self = ?,<br>Tensor<[1, 112, 15, 15]> other = ?      | Done     | Done       | 0.9999979454390695  | 0      |
|  61 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?      | Done     | Done       | 0.9999979743391929  | 0      |
|  62 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ?      | Done     | Done       | 0.9999979303624482  | 0      |
|  63 | Tensor<[1, 116, 14, 14]> self = ?,<br>Tensor<[1, 116, 14, 14]> other = ?      | Done     | Done       | 0.9999980254945358  | 0      |
|  64 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999980885973682  | 0      |
|  65 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?          | Unknown  | Done       | 0.9999986863198629  | 0      |
|  66 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999999997443321  | 0      |
|  67 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?            | Unknown  | Done       | 0.9999994847349265  | 0      |
|  68 | Tensor<[1, 12, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> other = ?           | Unknown  | Unknown    | N/A                 | N/A    |
|  69 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 1.0                 | 0      |
|  70 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?            | Unknown  | Done       | 0.999997712671241   | 0      |
|  71 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Done       | 0.9999979916778136  | 0      |
|  72 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                 | N/A    |
|  73 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                 | N/A    |
|  74 | Tensor<[1, 12, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                 | N/A    |
|  75 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Removed  | Done       | 0.999997908950373   | 0      |
|  76 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?        | Unknown  | Done       | 0.9999981848704934  | 0      |
|  77 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor<[1, 1, 1, 12]> other = ?          | Removed  | Done       | 0.9999976363550072  | 0      |
|  78 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?              | Done     | Done       | 0.9999979500287437  | 0      |
|  79 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor<[1, 1, 1, 14]> other = ?          | Removed  | Done       | 0.9999980403034339  | 0      |
|  80 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?         | Unknown  | Done       | 0.9999980982896035  | 0      |
|  81 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor<[1, 1, 1, 25]> other = ?          | Removed  | Done       | 0.9999977759209722  | 0      |
|  82 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999949758635425  | 0      |
|  83 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?            | Done     | Done       | 0.9999979633895552  | 0      |
|  84 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?         | Unknown  | Done       | 0.9999980052966816  | 0      |
|  85 | Tensor<[1, 12, 56, 56]> self = ?,<br>Tensor<[1, 12, 56, 56]> other = ?        | Done     | Done       | 0.999998006663075   | 0      |
|  86 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ?             | Done     | Done       | 0.999998279288665   | 0      |
|  87 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?              | Done     | Done       | 0.9999980611040142  | 0      |
|  88 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Removed  | Done       | 0.9999976680262714  | 0      |
|  89 | Tensor<[1, 120, 17, 17]> self = ?,<br>Tensor<[1, 120, 17, 17]> other = ?      | Done     | Done       | 0.9999979631087182  | 0      |
|  90 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?      | Done     | Done       | 0.9999979647946113  | 0      |
|  91 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?          | Done     | Done       | 0.9999979926343563  | 0      |
|  92 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?    | Done     | Done       | 0.9999979990490178  | 0      |
|  93 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Removed  | Done       | 1.0                 | 0      |
|  94 | Tensor<[1, 128, 112, 112]> self = ?,<br>Tensor<[1, 128, 112, 112]> other = ?  | Done     | Done       | 0.9999979840583457  | 0      |
|  95 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ?  | Done     | Done       | 0.999997999609599   | 0      |
|  96 | Tensor<[1, 128, 1536]> self = ?,<br>Tensor<[1, 128, 1536]> other = ?          | Unknown  | Unknown    | N/A                 | N/A    |
|  97 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999978874855989  | 0      |
|  98 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ?      | Done     | Done       | 0.9999979673209464  | 0      |
|  99 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ?      | Done     | Done       | 0.9999979952906821  | 0      |
| 100 | Tensor<[1, 128, 64, 64]> self = ?,<br>Tensor<[1, 128, 64, 64]> other = ?      | Done     | Done       | 0.9999979830925282  | 0      |
| 101 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?      | Done     | Done       | 0.999997985923842   | 0      |
| 102 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999979571250068  | 0      |
| 103 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ?    | Done     | Done       | 0.9999980073733368  | 0      |
| 104 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ?      | Done     | Done       | 0.9999979613211886  | 0      |
| 105 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?        | Done     | Done       | 0.999997997281713   | 0      |
| 106 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?    | Done     | Done       | 0.9999980144377211  | 0      |
| 107 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?              | Done     | Done       | 0.9999981862140477  | 0      |
| 108 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?      | Done     | Done       | 0.9999979782373807  | 0      |
| 109 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?      | Done     | Done       | 0.9999979860341527  | 0      |
| 110 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.999994819444571   | 0      |
| 111 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?            | Done     | Done       | 0.9999980177013325  | 0      |
| 112 | Tensor<[1, 14, 56, 56]> self = ?,<br>Tensor<[1, 14, 56, 56]> other = ?        | Done     | Done       | 0.999998018133918   | 0      |
| 113 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?              | Done     | Done       | 0.9999979572527568  | 0      |
| 114 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?      | Done     | Done       | 0.9999980115499406  | 0      |
| 115 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?          | Done     | Done       | 0.9999981023862425  | 0      |
| 116 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?          | Done     | Done       | 0.999997987938342   | 0      |
| 117 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999946819163498  | 0      |
| 118 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?            | Unknown  | Done       | 0.999997895300383   | 0      |
| 119 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                 | 0      |
| 120 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?              | Unknown  | Done       | 0.9999979452602495  | 0      |
| 121 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ?          | Unknown  | Done       | 0.9999979974806364  | 0      |
| 122 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?             | Unknown  | Done       | 0.999997997992961   | 0      |
| 123 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?        | Done     | Done       | 0.9999979223723181  | 0      |
| 124 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Tensor<[1, 1536, 8, 8]> other = ?        | Done     | Done       | 0.9999979832584692  | 0      |
| 125 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999982885482953  | 0      |
| 126 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?          | Unknown  | Done       | 0.9999986920025352  | 0      |
| 127 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 0.9999973466765689  | 0      |
| 128 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?            | Unknown  | Done       | 0.9999998350895166  | 0      |
| 129 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999989110964282  | 0      |
| 130 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?            | Unknown  | Done       | 0.9999977986907872  | 0      |
| 131 | Tensor<[1, 16, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Done       | 0.9999978890661833  | 0      |
| 132 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Done       | 0.999997799489692   | 0      |
| 133 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                 | N/A    |
| 134 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                 | N/A    |
| 135 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[1, 1, 1, s10 + 1]> other = ? | Unknown  | Unknown    | N/A                 | N/A    |
| 136 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.999997989690739   | 0      |
| 137 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?        | Unknown  | Done       | 0.999998257189752   | 0      |
| 138 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ?    | Done     | Done       | 0.9999979593053485  | 0      |
| 139 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?      | Done     | Done       | 0.999997979688449   | 0      |
| 140 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?      | Done     | Done       | 0.999998006770582   | 0      |
| 141 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ?    | Done     | Done       | 0.9999979791223259  | 0      |
| 142 | Tensor<[1, 16, 28, 28]> self = ?,<br>Tensor<[1, 16, 28, 28]> other = ?        | Done     | Done       | 0.9999980863017791  | 0      |
| 143 | Tensor<[1, 16, 384, 384]> self = ?,<br>Tensor<[1, 1, 1, 384]> other = ?       | Removed  | Unknown    | N/A                 | N/A    |
| 144 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Done       | 0.9999981983484275  | 0      |
| 145 | Tensor<[1, 16, 59, 59]> self = ?,<br>Tensor<[1, 1, 59, 59]> other = ?         | Unknown  | Done       | 0.999998006216274   | 0      |
| 146 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 147 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 148 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?              | Done     | Done       | 0.999997960083757   | 0      |
| 149 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 150 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 151 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Removed  | Done       | 0.9999979272360835  | 0      |
| 152 | Tensor<[1, 160, 14, 14]> self = ?,<br>Tensor<[1, 160, 14, 14]> other = ?      | Done     | Done       | 0.9999979543172423  | 0      |
| 153 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ?      | Done     | Done       | 0.9999979937174938  | 0      |
| 154 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ?      | Done     | Done       | 0.9999979843172498  | 0      |
| 155 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?      | Done     | Done       | 0.9999979844613031  | 0      |
| 156 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?          | Done     | Done       | 0.9999979075077471  | 0      |
| 157 | Tensor<[1, 160, 73, 73]> self = ?,<br>Tensor<[1, 160, 73, 73]> other = ?      | Done     | Done       | 0.9999980064526978  | 0      |
| 158 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999980660684494  | 0      |
| 159 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?          | Done     | Done       | 0.9999979947122488  | 0      |
| 160 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ?      | Done     | Done       | 0.9999979895593104  | 0      |
| 161 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?        | Done     | Done       | 0.9999980076004945  | 0      |
| 162 | Tensor<[1, 185, 28, 28]> self = ?,<br>Tensor<[1, 185, 28, 28]> other = ?      | Done     | Done       | 0.9999979965017111  | 0      |
| 163 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ?      | Done     | Done       | 0.9999979483736425  | 0      |
| 164 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ?      | Done     | Done       | 0.9999979910931641  | 0      |
| 165 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?      | Done     | Done       | 0.9999980062632624  | 0      |
| 166 | Tensor<[1, 192, 7, 7]> self = ?,<br>Tensor<[1, 192, 7, 7]> other = ?          | Done     | Done       | 0.9999980787688169  | 0      |
| 167 | Tensor<[1, 192, 71, 71]> self = ?,<br>Tensor<[1, 192, 71, 71]> other = ?      | Done     | Done       | 0.9999979877724594  | 0      |
| 168 | Tensor<[1, 192, 8, 8]> self = ?,<br>Tensor<[1, 192, 8, 8]> other = ?          | Done     | Done       | 0.999997987330093   | 0      |
| 169 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?        | Done     | Done       | 0.999997977432228   | 0      |
| 170 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?          | Done     | Done       | 0.9999979942170194  | 0      |
| 171 | Tensor<[1, 196, 14, 14]> self = ?,<br>Tensor<[1, 196, 14, 14]> other = ?      | Done     | Done       | 0.9999980202901345  | 0      |
| 172 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ?            | Done     | Done       | 0.9999979958848995  | 0      |
| 173 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?          | Done     | Done       | 0.9999980018308487  | 0      |
| 174 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?            | Done     | Done       | 0.999997990554272   | 0      |
| 175 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                 | 0      |
| 176 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                 | 0      |
| 177 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                  | Unknown  | Done       | 1.0                 | 0      |
| 178 | Tensor<[1, 20, 28, 28]> self = ?,<br>Tensor<[1, 20, 28, 28]> other = ?        | Done     | Done       | 0.9999979906383282  | 0      |
| 179 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?        | Done     | Done       | 0.9999979845838202  | 0      |
| 180 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Removed  | Done       | 1.0                 | 0      |
| 181 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Done     | Done       | 0.9999979990112564  | 0      |
| 182 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?    | Done     | Done       | 0.999997992432503   | 0      |
| 183 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?        | Done     | Done       | 0.9999980039559848  | 0      |
| 184 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?          | Done     | Done       | 0.9999979954520827  | 0      |
| 185 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?             | Done     | Done       | 0.999997995463283   | 0      |
| 186 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?      | Done     | Done       | 0.999997991609759   | 0      |
| 187 | Tensor<[1, 208, 9, 9]> self = ?,<br>Tensor<[1, 208, 9, 9]> other = ?          | Done     | Done       | 0.999997950195293   | 0      |
| 188 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?      | Done     | Done       | 0.9999979963690404  | 0      |
| 189 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?      | Done     | Done       | 0.9999980015902852  | 0      |
| 190 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?          | Done     | Done       | 0.9999980701113054  | 0      |
| 191 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                          | Done     | Done       | 1.0                 | 0      |
| 192 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ?      | Done     | Done       | 0.9999980213399157  | 0      |
| 193 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?      | Done     | Done       | 0.9999979941659506  | 0      |
| 194 | Tensor<[1, 24, 112, 112]> self = ?,<br>Tensor<[1, 24, 112, 112]> other = ?    | Done     | Done       | 0.9999979941782764  | 0      |
| 195 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?        | Done     | Done       | 0.9999980117000405  | 0      |
| 196 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?        | Done     | Done       | 0.9999979838563027  | 0      |
| 197 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?        | Done     | Done       | 0.9999979834077496  | 0      |
| 198 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?        | Done     | Done       | 0.9999979818706631  | 0      |
| 199 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?        | Done     | Done       | 0.9999979684594432  | 0      |
| 200 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?        | Done     | Done       | 0.9999980141024056  | 0      |
| 201 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?              | Unknown  | Done       | 0.9999979558998362  | 0      |
| 202 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?        | Done     | Done       | 0.9999980106946504  | 0      |
| 203 | Tensor<[1, 240, 14, 14]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?      | Done     | Done       | 0.9999980580836508  | 0      |
| 204 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?      | Done     | Done       | 0.9999980033751911  | 0      |
| 205 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?              | Done     | Done       | 0.9999979476604304  | 0      |
| 206 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?        | Done     | Done       | 0.9999979867587027  | 0      |
| 207 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Removed  | Done       | 1.0                 | 0      |
| 208 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ?  | Done     | Done       | 0.9999979891710002  | 0      |
| 209 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?          | Done     | Done       | 0.9999980121071461  | 0      |
| 210 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ?      | Done     | Done       | 0.999997992633806   | 0      |
| 211 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?      | Done     | Done       | 0.9999979552522991  | 0      |
| 212 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?            | Done     | Done       | 0.9999979638094506  | 0      |
| 213 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999980446938729  | 0      |
| 214 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ?  | Done     | Done       | 0.9999979923391542  | 0      |
| 215 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?            | Done     | Done       | 0.9999979927369841  | 0      |
| 216 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.9999979861735171  | 0      |
| 217 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ?      | Done     | Done       | 0.9999980115510042  | 0      |
| 218 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?      | Done     | Done       | 0.9999980114320753  | 0      |
| 219 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?              | Done     | Done       | 0.9999980241302167  | 0      |
| 220 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?      | Done     | Done       | 0.9999979893804358  | 0      |
| 221 | Tensor<[1, 256, 384]> self = ?,<br>Tensor<[1, 256, 384]> other = ?            | Unknown  | Unknown    | N/A                 | N/A    |
| 222 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999979449314207  | 0      |
| 223 | Tensor<[1, 256, 512]> self = ?,<br>Tensor<[1, 256, 512]> other = ?            | Done     | Done       | 0.9999980231311397  | 0      |
| 224 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?      | Done     | Done       | 0.9999980054295983  | 0      |
| 225 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?      | Done     | Done       | 0.9999980033251578  | 0      |
| 226 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?              | Done     | Done       | 0.9999978911004426  | 0      |
| 227 | Tensor<[1, 256, 7, 7]> self = ?,<br>Tensor<[1, 256, 7, 7]> other = ?          | Done     | Done       | 0.9999979835565204  | 0      |
| 228 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?      | Done     | Done       | 0.9999979948670461  | 0      |
| 229 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999979300412791  | 0      |
| 230 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[1, 257, 768]> other = ?            | Done     | Unknown    | N/A                 | N/A    |
| 231 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ?      | Done     | Done       | 0.9999980048025364  | 0      |
| 232 | Tensor<[1, 272, 7, 7]> self = ?,<br>Tensor<[1, 272, 7, 7]> other = ?          | Done     | Done       | 0.9999980715735203  | 0      |
| 233 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?      | Done     | Done       | 0.9999979984623067  | 0      |
| 234 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?      | Done     | Done       | 0.9999980020648561  | 0      |
| 235 | Tensor<[1, 28, 28, 28]> self = ?,<br>Tensor<[1, 28, 28, 28]> other = ?        | Done     | Done       | 0.9999980140505608  | 0      |
| 236 | Tensor<[1, 288, 14, 14]> self = ?,<br>Tensor<[1, 288, 14, 14]> other = ?      | Done     | Done       | 0.9999980292754491  | 0      |
| 237 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?    | Done     | Done       | 0.9999979979678085  | 0      |
| 238 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?      | Done     | Done       | 0.9999980094316766  | 0      |
| 239 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?      | Done     | Done       | 0.9999979942668011  | 0      |
| 240 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?            | Done     | Done       | 0.9999979770249149  | 0      |
| 241 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?        | Done     | Done       | 0.9999979758940418  | 0      |
| 242 | Tensor<[1, 32, 112, 112]> self = ?,<br>Tensor<[1, 32, 112, 112]> other = ?    | Done     | Done       | 0.9999980208351323  | 0      |
| 243 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?    | Done     | Done       | 0.9999979946229124  | 0      |
| 244 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?            | Done     | Done       | 0.9999980637013549  | 0      |
| 245 | Tensor<[1, 32, 24576]> self = ?,<br>Tensor<[1, 32, 24576]> other = ?          | Unknown  | Unknown    | N/A                 | N/A    |
| 246 | Tensor<[1, 32, 256, 256]> self = ?,<br>Tensor<[1, 32, 256, 256]> other = ?    | Done     | Done       | 0.9999979916691298  | 0      |
| 247 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ?        | Done     | Done       | 0.9999979139343831  | 0      |
| 248 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?      | Done     | Done       | 0.9999980281411635  | 0      |
| 249 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?      | Done     | Done       | 0.9999979997245112  | 0      |
| 250 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?        | Done     | Done       | 0.999998035926595   | 0      |
| 251 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?        | Done     | Done       | 0.9999979818056798  | 0      |
| 252 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                           | Done     | Done       | 0.9999948300549955  | 0      |
| 253 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.999994781390393   | 0      |
| 254 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?        | Done     | Done       | 0.9999980366645072  | 0      |
| 255 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?        | Done     | Done       | 0.9999979784190937  | 0      |
| 256 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?        | Done     | Done       | 0.9999980124857005  | 0      |
| 257 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?      | Done     | Done       | 0.9999979667725918  | 0      |
| 258 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?      | Done     | Done       | 0.9999979534918686  | 0      |
| 259 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?      | Done     | Done       | 0.9999979976605159  | 0      |
| 260 | Tensor<[1, 34, 28, 28]> self = ?,<br>Tensor<[1, 34, 28, 28]> other = ?        | Done     | Done       | 0.9999980543425387  | 0      |
| 261 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?        | Done     | Done       | 0.9999980490276122  | 0      |
| 262 | Tensor<[1, 36, 56, 56]> self = ?,<br>Tensor<[1, 36, 56, 56]> other = ?        | Done     | Done       | 0.9999980335150969  | 0      |
| 263 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?        | Done     | Done       | 0.9999979908372648  | 0      |
| 264 | Tensor<[1, 384, 1024]> self = ?,<br>Tensor<[1, 384, 1024]> other = ?          | Done     | Unknown    | N/A                 | N/A    |
| 265 | Tensor<[1, 384, 35, 35]> self = ?,<br>Tensor<[1, 384, 35, 35]> other = ?      | Done     | Done       | 0.9999979993995324  | 0      |
| 266 | Tensor<[1, 384, 8, 8]> self = ?,<br>Tensor<[1, 384, 8, 8]> other = ?          | Done     | Done       | 0.9999979197541948  | 0      |
| 267 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 268 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 269 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 270 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?   | None     | Fallback   | 1.0                 | -1     |
| 271 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?                | Unknown  | Done       | 0.9999975661460242  | 0      |
| 272 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[4, 768]> other = ?                   | Unknown  | Done       | 0.9999979952196659  | 0      |
| 273 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ?        | Done     | Done       | 0.9999978906880729  | 0      |
| 274 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?        | Done     | Done       | 0.999997996682331   | 0      |
| 275 | Tensor<[1, 40, 30, 30]> self = ?,<br>Tensor<[1, 40, 30, 30]> other = ?        | Done     | Done       | 0.9999979813869246  | 0      |
| 276 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?        | Done     | Done       | 0.9999979747347324  | 0      |
| 277 | Tensor<[1, 40, 56, 56]> self = ?,<br>Tensor<[1, 40, 56, 56]> other = ?        | Done     | Done       | 0.9999979648556141  | 0      |
| 278 | Tensor<[1, 400, 7, 7]> self = ?,<br>Tensor<[1, 400, 7, 7]> other = ?          | Done     | Done       | 0.9999980768385487  | 0      |
| 279 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ?      | Done     | Done       | 0.9999979759223777  | 0      |
| 280 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999980208944825  | 0      |
| 281 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?            | Done     | Done       | 0.999998005230826   | 0      |
| 282 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ?      | Done     | Done       | 0.9999980220650949  | 0      |
| 283 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?          | Done     | Done       | 0.9999978947797225  | 0      |
| 284 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?      | Done     | Done       | 0.9999979860539919  | 0      |
| 285 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999948542906729  | 0      |
| 286 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?            | Unknown  | Done       | 0.9999980112796012  | 0      |
| 287 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?              | Unknown  | Done       | 0.9999979775956679  | 0      |
| 288 | Tensor<[1, 46, 28, 28]> self = ?,<br>Tensor<[1, 46, 28, 28]> other = ?        | Done     | Done       | 0.999998000569138   | 0      |
| 289 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ?        | Done     | Done       | 0.9999980103282858  | 0      |
| 290 | Tensor<[1, 48, 33, 33]> self = ?,<br>Tensor<[1, 48, 33, 33]> other = ?        | Done     | Done       | 0.9999979845843614  | 0      |
| 291 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?        | Done     | Done       | 0.9999979719301303  | 0      |
| 292 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?        | Done     | Done       | 0.9999979782419176  | 0      |
| 293 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?      | Done     | Done       | 0.9999979917557658  | 0      |
| 294 | Tensor<[1, 480, 7, 7]> self = ?,<br>Tensor<[1, 480, 7, 7]> other = ?          | Done     | Done       | 0.9999979645488264  | 0      |
| 295 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?          | Done     | Done       | 0.9999979836663195  | 0      |
| 296 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?              | Unknown  | Done       | 0.9999981559957007  | 0      |
| 297 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?          | Unknown  | Done       | 0.9999980173394072  | 0      |
| 298 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Done       | 0.999994926534975   | 0      |
| 299 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?              | Unknown  | Done       | 0.9999980114193247  | 0      |
| 300 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?            | Done     | Done       | 0.9999980099669737  | 0      |
| 301 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?            | Done     | Done       | 0.9999979945944265  | 0      |
| 302 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?              | Done     | Done       | 0.9999979413431861  | 0      |
| 303 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Removed  | Done       | 1.0                 | 0      |
| 304 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ?      | Done     | Done       | 0.9999980090492671  | 0      |
| 305 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999980074703702  | 0      |
| 306 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?      | Done     | Done       | 0.999997963764696   | 0      |
| 307 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?      | Done     | Done       | 0.9999980059517604  | 0      |
| 308 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999980046681669  | 0      |
| 309 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?          | Done     | Done       | 0.999998011749416   | 0      |
| 310 | Tensor<[1, 512, 8, 8]> self = ?,<br>Tensor<[1, 512, 8, 8]> other = ?          | Done     | Done       | 0.9999979593416292  | 0      |
| 311 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.999997957367107   | 0      |
| 312 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?    | Done     | Done       | 0.9999979910899868  | 0      |
| 313 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                      | Done     | Done       | 0.9999973035768692  | 0      |
| 314 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?      | Done     | Done       | 0.9999980025845961  | 0      |
| 315 | Tensor<[1, 56, 14, 14]> self = ?,<br>Tensor<[1, 56, 14, 14]> other = ?        | Done     | Done       | 0.9999979500060331  | 0      |
| 316 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?        | Done     | Done       | 0.9999979694325122  | 0      |
| 317 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?      | Done     | Done       | 0.9999979861711287  | 0      |
| 318 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?        | Done     | Done       | 0.999997997736586   | 0      |
| 319 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?      | Done     | Done       | 0.9999980287636941  | 0      |
| 320 | Tensor<[1, 58, 28, 28]> self = ?,<br>Tensor<[1, 58, 28, 28]> other = ?        | Done     | Done       | 0.9999979411326663  | 0      |
| 321 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?            | Unknown  | Done       | 0.9999980048741088  | 0      |
| 322 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                 | Unknown  | Done       | 0.9999897097345312  | 0      |
| 323 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?            | Unknown  | Done       | 0.9999982201568065  | 0      |
| 324 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?            | Unknown  | Done       | 0.9999990008200939  | 0      |
| 325 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?            | Unknown  | Done       | 0.999998881054511   | 0      |
| 326 | Tensor<[1, 6, 1, 17]> self = ?,<br>Tensor<[1, 6, 1, 17]> other = ?            | Unknown  | Done       | 0.9999983384622998  | 0      |
| 327 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 0.9999972043633676  | 0      |
| 328 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?              | Unknown  | Done       | 0.9999969313067056  | 0      |
| 329 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999947987584542  | 0      |
| 330 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?              | Unknown  | Done       | 1.0                 | 0      |
| 331 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 332 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 333 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?           | Unknown  | Done       | 0.99999799630848    | 0      |
| 334 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?          | Unknown  | Done       | 0.9999981982311967  | 0      |
| 335 | Tensor<[1, 60, 28, 28]> self = ?,<br>Tensor<[1, 60, 28, 28]> other = ?        | Done     | Done       | 0.9999979881598718  | 0      |
| 336 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                       | Removed  | Done       | 1.0                 | 0      |
| 337 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?    | Done     | Done       | 0.9999980005235403  | 0      |
| 338 | Tensor<[1, 64, 128, 128]> self = ?,<br>Tensor<[1, 64, 128, 128]> other = ?    | Done     | Done       | 0.9999980111108717  | 0      |
| 339 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ?        | Done     | Done       | 0.9999980672271784  | 0      |
| 340 | Tensor<[1, 64, 147, 147]> self = ?,<br>Tensor<[1, 64, 147, 147]> other = ?    | Done     | Done       | 0.9999979958283605  | 0      |
| 341 | Tensor<[1, 64, 150, 150]> self = ?,<br>Tensor<[1, 64, 150, 150]> other = ?    | Done     | Done       | 0.9999979939259388  | 0      |
| 342 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.99999793626452    | 0      |
| 343 | Tensor<[1, 64, 224, 224]> self = ?,<br>Tensor<[1, 64, 224, 224]> other = ?    | Done     | Done       | 0.9999979921257702  | 0      |
| 344 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?    | Done     | Done       | 0.9999979934640992  | 0      |
| 345 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?    | Done     | Done       | 0.9999979977118507  | 0      |
| 346 | Tensor<[1, 64, 28, 28]> self = ?,<br>Tensor<[1, 64, 28, 28]> other = ?        | Done     | Done       | 0.9999980056356892  | 0      |
| 347 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 348 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 349 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?        | Done     | Done       | 0.9999979874061272  | 0      |
| 350 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?        | Done     | Done       | 0.9999981274347132  | 0      |
| 351 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 352 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                 | -1     |
| 353 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?    | Done     | Done       | 0.9999979942973297  | 0      |
| 354 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?        | Done     | Done       | 0.9999979880728708  | 0      |
| 355 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?        | Done     | Done       | 0.999997963949813   | 0      |
| 356 | Tensor<[1, 64, 6144]> self = ?,<br>Tensor<[1, 64, 6144]> other = ?            | Unknown  | Unknown    | N/A                 | N/A    |
| 357 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?      | Done     | Done       | 0.9999979946640608  | 0      |
| 358 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?        | Done     | Done       | 0.9999979935669683  | 0      |
| 359 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?        | Done     | Done       | 0.999997989190551   | 0      |
| 360 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor<[1, 1, 1, 9]> other = ?             | Removed  | Done       | 0.9999981188999538  | 0      |
| 361 | Tensor<[1, 640, 7, 7]> self = ?,<br>Tensor<[1, 640, 7, 7]> other = ?          | Done     | Done       | 0.9999979949246635  | 0      |
| 362 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?      | Done     | Done       | 0.999998021785656   | 0      |
| 363 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?      | Done     | Done       | 0.9999979845725815  | 0      |
| 364 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?          | Done     | Done       | 0.9999980349910406  | 0      |
| 365 | Tensor<[1, 68, 14, 14]> self = ?,<br>Tensor<[1, 68, 14, 14]> other = ?        | Done     | Done       | 0.9999980353148937  | 0      |
| 366 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?      | Done     | Done       | 0.9999979860092467  | 0      |
| 367 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947051418913  | 0      |
| 368 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?              | Done     | Done       | 0.9999979643885585  | 0      |
| 369 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?        | Done     | Done       | 0.9999980077989201  | 0      |
| 370 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?          | Done     | Done       | 0.9999979992103326  | 0      |
| 371 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?                | Done     | Done       | 0.9999981030477886  | 0      |
| 372 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?        | Done     | Done       | 0.9999981289489674  | 0      |
| 373 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?        | Done     | Done       | 0.9999980271802037  | 0      |
| 374 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?        | Done     | Done       | 0.9999979902507803  | 0      |
| 375 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ?      | Done     | Done       | 0.9999979754402154  | 0      |
| 376 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?      | Done     | Done       | 0.9999979992846629  | 0      |
| 377 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?      | Done     | Done       | 0.9999979958633538  | 0      |
| 378 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?    | Done     | Done       | 0.9999979923980448  | 0      |
| 379 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?      | Done     | Done       | 0.9999979902097665  | 0      |
| 380 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 768, 16, 16]> other = ?      | Done     | Unknown    | N/A                 | N/A    |
| 381 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                    | Done     | Done       | 0.9999979808532312  | 0      |
| 382 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?          | Done     | Done       | 0.9999980201714861  | 0      |
| 383 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                      | Done     | Done       | 0.9999977813325687  | 0      |
| 384 | Tensor<[1, 78, 28, 28]> self = ?,<br>Tensor<[1, 78, 28, 28]> other = ?        | Done     | Done       | 0.9999980140359532  | 0      |
| 385 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?          | Done     | Done       | 0.999998044401343   | 0      |
| 386 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?            | Unknown  | Done       | 0.9999985587138757  | 0      |
| 387 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?            | Unknown  | Done       | 0.9999980091858827  | 0      |
| 388 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?              | Unknown  | Done       | 1.0                 | 0      |
| 389 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?              | Unknown  | Done       | 0.99999832144095    | 0      |
| 390 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?              | Unknown  | Done       | 0.9999970383010252  | 0      |
| 391 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?              | Unknown  | Done       | 0.9999983165002672  | 0      |
| 392 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 393 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ?    | Unknown  | Unknown    | N/A                 | N/A    |
| 394 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999981381485672  | 0      |
| 395 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?          | Unknown  | Done       | 0.9999982195860166  | 0      |
| 396 | Tensor<[1, 8, 112, 112]> self = ?,<br>Tensor<[1, 8, 112, 112]> other = ?      | Done     | Done       | 0.9999980068268843  | 0      |
| 397 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ?      | Removed  | Done       | 0.9999980148704546  | 0      |
| 398 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?                | Done     | Done       | 0.9999981554797571  | 0      |
| 399 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?        | Done     | Done       | 0.999997972506081   | 0      |
| 400 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?          | Done     | Done       | 0.9999980432043024  | 0      |
| 401 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?        | Done     | Done       | 0.9999980438371249  | 0      |
| 402 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?        | Done     | Done       | 0.9999980361034034  | 0      |
| 403 | Tensor<[1, 80, 15, 15]> self = ?,<br>Tensor<[1, 80, 15, 15]> other = ?        | Done     | Done       | 0.9999979995515861  | 0      |
| 404 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?        | Done     | Done       | 0.9999979935619715  | 0      |
| 405 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?        | Done     | Done       | 0.9999979897869721  | 0      |
| 406 | Tensor<[1, 80, 7, 7]> self = ?,<br>Tensor<[1, 80, 7, 7]> other = ?            | Done     | Done       | 0.999998067360396   | 0      |
| 407 | Tensor<[1, 88, 17, 17]> self = ?,<br>Tensor<[1, 88, 17, 17]> other = ?        | Done     | Done       | 0.9999980188008101  | 0      |
| 408 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?          | Done     | Done       | 0.9999979900469267  | 0      |
| 409 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?      | Done     | Done       | 0.9999979933232637  | 0      |
| 410 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?              | Done     | Done       | 0.9999979889590287  | 0      |
| 411 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                           | Done     | Done       | 0.9999947129922077  | 0      |
| 412 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                | Done     | Done       | 0.9999978564258757  | 0      |
| 413 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947458076629  | 0      |
| 414 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?            | Done     | Done       | 0.9999979794342662  | 0      |
| 415 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?              | Done     | Done       | 0.9999979705852277  | 0      |
| 416 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999946338433491  | 0      |
| 417 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?              | Done     | Done       | 0.999997948883331   | 0      |
| 418 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947180841537  | 0      |
| 419 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?              | Done     | Done       | 0.9999979658701256  | 0      |
| 420 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?                | Done     | Done       | 0.9999978952455573  | 0      |
| 421 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.9999947889229682  | 0      |
| 422 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?              | Done     | Done       | 0.9999980421901716  | 0      |
| 423 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?          | Done     | Done       | 0.9999979316641081  | 0      |
| 424 | Tensor<[1, 92, 14, 14]> self = ?,<br>Tensor<[1, 92, 14, 14]> other = ?        | Done     | Done       | 0.9999979887938438  | 0      |
| 425 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?        | Done     | Done       | 0.9999979231137933  | 0      |
| 426 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?        | Done     | Done       | 0.9999979581258045  | 0      |
| 427 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?        | Done     | Done       | 0.9999979937742876  | 0      |
| 428 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?            | Done     | Done       | 0.999998249562993   | 0      |
| 429 | Tensor<[1, 96, 80]> self = ?,<br>Tensor<[1, 96, 80]> other = ?                | Unknown  | Unknown    | N/A                 | N/A    |
| 430 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?          | Done     | Done       | 0.9999979554486828  | 0      |
| 431 | Tensor<[1, 98, 28, 28]> self = ?,<br>Tensor<[1, 98, 28, 28]> other = ?        | Done     | Done       | 0.9999980026654505  | 0      |
| 432 | Tensor<[1, s0, 768]> self = ?,<br>Tensor<[1, s0, 768]> other = ?              | Unknown  | Unknown    | N/A                 | N/A    |
| 433 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                 | 0      |
| 434 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.9999183822559585  | 0      |
| 435 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                      | Unknown  | Done       | 0.9999989241903655  | 0      |
| 436 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?            | Done     | Done       | 0.9999979659215195  | 0      |
| 437 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?              | Unknown  | Done       | 0.9999979524859278  | 0      |
| 438 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                 | 0      |
| 439 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                | Unknown  | Done       | 0.99991503165213    | 0      |
| 440 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                      | Unknown  | Done       | 0.9999975098278747  | 0      |
| 441 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?         | Done     | Done       | 0.9999980293510687  | 0      |
| 442 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?         | Done     | Done       | 0.9999979983876579  | 0      |
| 443 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?         | Done     | Done       | 0.9999979882624934  | 0      |
| 444 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?         | Done     | Done       | 0.9999979890739266  | 0      |
| 445 | Tensor<[17, 17]> self = ?,<br>Tensor other = 0                                | Unknown  | Done       | 1.0                 | 0      |
| 446 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 0.9996698254050634  | 0      |
| 447 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0                                  | Unknown  | Done       | 1.0                 | 0      |
| 448 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                 | Unknown  | Done       | 1.0                 | 0      |
| 449 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                      | Done     | Done       | 0.9999979999708103  | 0      |
| 450 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?              | Done     | Done       | 0.9999980634622128  | 0      |
| 451 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?                | Done     | Done       | 0.9999977947849462  | 0      |
| 452 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?                | Done     | Done       | 0.9999980404123113  | 0      |
| 453 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?              | Done     | Done       | 0.9999976471899985  | 0      |
| 454 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                      | Removed  | Done       | 0.9999979972988231  | 0      |
| 455 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                              | Unknown  | Done       | 0.9757271077957888  | 0      |
| 456 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                    | Done     | Done       | 0.999997927133138   | 0      |
| 457 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?        | Done     | Done       | 0.9999979861660768  | 0      |
| 458 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?        | Done     | Done       | 0.9999979806293937  | 0      |
| 459 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?        | Done     | Done       | 0.999997973521373   | 0      |
| 460 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?        | Done     | Done       | 0.9999979936034687  | 0      |
| 461 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                  | Unknown  | Done       | 0.9999980279131622  | 0      |
| 462 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?         | Done     | Done       | 0.9999979858157001  | 0      |
| 463 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?         | Done     | Done       | 0.9999979861357773  | 0      |
| 464 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?         | Done     | Done       | 0.9999979883433711  | 0      |
| 465 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?         | Done     | Done       | 0.9999979965536009  | 0      |
| 466 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                    | Done     | Done       | 0.9999980847730302  | 0      |
| 467 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                    | Done     | Done       | 0.27280755977306254 | 0      |
| 468 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?            | Done     | Done       | 0.9999980021295674  | 0      |
| 469 | Tensor<[]> self = ?,<br>Tensor other = 1                                      | Done     | Done       | 1.0                 | 0      |
| 470 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 0                        | Unknown  | Unknown    | N/A                 | N/A    |
| 471 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                       | Unknown  | Unknown    | N/A                 | N/A    |

