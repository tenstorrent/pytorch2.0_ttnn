### aten.add.Tensor
|     | ATen Input Variations                                                        | Status   | Isolated   | PCC                | Host   |
|----:|:-----------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 1, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
|   1 | Tensor<[1, 1, 1, 60]> self = ?,<br>Tensor<[1, 1, 1, 60]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
|   2 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?             | Unknown  | Unknown    | N/A                | N/A    |
|   3 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
|   4 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999950840423011 | 0      |
|   5 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?             | Unknown  | Done       | 0.9999978216991892 | 0      |
|   6 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 16, 32]> other = ?         | Unknown  | Done       | 0.9999980606648985 | 0      |
|   7 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.8999999985098839             | Done     | Done       | 1.0                | 0      |
|   8 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9142857119441032             | Done     | Done       | 1.0                | 0      |
|   9 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9285714253783226             | Done     | Done       | 1.0                | 0      |
|  10 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9428571425378323             | Done     | Done       | 1.0                | 0      |
|  11 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9571428559720516             | Done     | Done       | 1.0                | 0      |
|  12 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9714285712689161             | Done     | Done       | 1.0                | 0      |
|  13 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 0.9857142856344581             | Done     | Done       | 1.0                | 0      |
|  14 | Tensor<[1, 1, 1]> self = ?,<br>Tensor other = 1e-06                          | Unknown  | Done       | 1.0                | 0      |
|  15 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.030000000000000027   | Done     | Done       | 0.9999999961723861 | 0      |
|  16 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.08799999999999997    | Done     | Done       | 0.9999990495517094 | 0      |
|  17 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = -0.18799999999999994    | Done     | Done       | 0.9999998613714416 | 0      |
|  18 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999949922544327 | 0      |
|  19 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?             | Unknown  | Done       | 0.9999978171568369 | 0      |
|  20 | Tensor<[1, 1, 32, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?          | Done     | Unknown    | N/A                | N/A    |
|  21 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999944170212539 | 0      |
|  22 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?             | Unknown  | Done       | 0.9999980492911931 | 0      |
|  23 | Tensor<[1, 1, 40]> self = ?,<br>Tensor other = 1e-06                         | Done     | Done       | 1.0                | 0      |
|  24 | Tensor<[1, 1, 45, 45]> self = ?,<br>Tensor<[1, 1, 1, 45]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
|  25 | Tensor<[1, 1, 5, 5]> self = ?,<br>Tensor<[1, 1, 1, 5]> other = ?             | Unknown  | Unknown    | N/A                | N/A    |
|  26 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?               | Unknown  | Done       | 0.9999983839309707 | 0      |
|  27 | Tensor<[1, 1, 59, 59]> self = ?,<br>Tensor<[1, 1, 1, 59]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
|  28 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
|  29 | Tensor<[1, 1, 7, 7]> self = ?,<br>Tensor<[1, 1, 1, 7]> other = ?             | Done     | Unknown    | N/A                | N/A    |
|  30 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?               | Unknown  | Done       | 0.999997651820464  | 0      |
|  31 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?           | Unknown  | Done       | 0.9999979655609763 | 0      |
|  32 | Tensor<[1, 10, 1]> self = ?,<br>Tensor other = 1e-06                         | Unknown  | Done       | 1.0                | 0      |
|  33 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?             | Unknown  | Done       | 0.9999979251867083 | 0      |
|  34 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?             | Done     | Done       | 0.9999980340845195 | 0      |
|  35 | Tensor<[1, 100, 14, 14]> self = ?,<br>Tensor<[1, 100, 14, 14]> other = ?     | Done     | Done       | 0.9999980501189172 | 0      |
|  36 | Tensor<[1, 1008, 7, 7]> self = ?,<br>Tensor<[1, 1008, 7, 7]> other = ?       | Done     | Done       | 0.9999979366837369 | 0      |
|  37 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor other = 1e-05                    | Removed  | Done       | 1.0                | 0      |
|  38 | Tensor<[1, 1024, 10, 10]> self = ?,<br>Tensor<[1, 1024, 10, 10]> other = ?   | Done     | Done       | 0.9999980279486038 | 0      |
|  39 | Tensor<[1, 1024, 14, 14]> self = ?,<br>Tensor<[1, 1024, 14, 14]> other = ?   | Done     | Done       | 0.9999980032006184 | 0      |
|  40 | Tensor<[1, 1024, 16, 16]> self = ?,<br>Tensor<[1, 1024, 16, 16]> other = ?   | Done     | Done       | 0.9999979956161581 | 0      |
|  41 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1024, 160]> other = ?         | Done     | Done       | 0.9999979765351356 | 0      |
|  42 | Tensor<[1, 1024, 17, 17]> self = ?,<br>Tensor<[1, 1024, 17, 17]> other = ?   | Done     | Done       | 0.9999979853077834 | 0      |
|  43 | Tensor<[1, 1024, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999979617084783 | 0      |
|  44 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?     | Done     | Done       | 0.9999979901016688 | 0      |
|  45 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 45, 80]> other = ?   | Done     | Done       | 0.9999979989852059 | 0      |
|  46 | Tensor<[1, 1024, 640]> self = ?,<br>Tensor<[1, 1024, 640]> other = ?         | Done     | Unknown    | N/A                | N/A    |
|  47 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?       | Done     | Done       | 0.9999979909879453 | 0      |
|  48 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1, 1024]> other = ?                   | Unknown  | Done       | 0.9999981143488617 | 0      |
|  49 | Tensor<[1, 104, 28, 28]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?     | Done     | Done       | 0.99999797622834   | 0      |
|  50 | Tensor<[1, 1056, 48, 48]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?   | Done     | Done       | 0.9999979898237449 | 0      |
|  51 | Tensor<[1, 10]> self = ?,<br>Tensor other = 0                                | Done     | Done       | 1.0                | 0      |
|  52 | Tensor<[1, 10]> self = ?,<br>Tensor other = 1                                | Done     | Done       | 0.9999991431898287 | 0      |
|  53 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                       | Unknown  | Unknown    | N/A                | N/A    |
|  54 | Tensor<[1, 112, 14, 14]> self = ?,<br>Tensor<[1, 112, 14, 14]> other = ?     | Done     | Done       | 0.9999980767587955 | 0      |
|  55 | Tensor<[1, 112, 15, 15]> self = ?,<br>Tensor<[1, 112, 15, 15]> other = ?     | Done     | Done       | 0.9999979941245599 | 0      |
|  56 | Tensor<[1, 112, 20, 20]> self = ?,<br>Tensor<[1, 112, 20, 20]> other = ?     | Done     | Done       | 0.9999979975399718 | 0      |
|  57 | Tensor<[1, 112, 24, 24]> self = ?,<br>Tensor<[1, 112, 24, 24]> other = ?     | Done     | Done       | 0.9999980066603814 | 0      |
|  58 | Tensor<[1, 116, 14, 14]> self = ?,<br>Tensor<[1, 116, 14, 14]> other = ?     | Done     | Done       | 0.999997939136494  | 0      |
|  59 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.9999983792964312 | 0      |
|  60 | Tensor<[1, 12, 1, 10]> self = ?,<br>Tensor<[1, 12, 1, 10]> other = ?         | Unknown  | Done       | 0.9999997188820785 | 0      |
|  61 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?            | Unknown  | Done       | 0.9999899272507639 | 0      |
|  62 | Tensor<[1, 12, 1, 1]> self = ?,<br>Tensor<[1, 12, 1, 1]> other = ?           | Unknown  | Done       | 0.9999956082590504 | 0      |
|  63 | Tensor<[1, 12, 1, 24]> self = ?,<br>Tensor<[1, 1, 1, 24]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
|  64 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?            | Unknown  | Done       | 0.9999997711530167 | 0      |
|  65 | Tensor<[1, 12, 1, 2]> self = ?,<br>Tensor<[1, 12, 1, 2]> other = ?           | Unknown  | Done       | 0.9999967642645885 | 0      |
|  66 | Tensor<[1, 12, 1, 46]> self = ?,<br>Tensor<[1, 1, 1, 46]> other = ?          | Unknown  | Done       | 0.9999983475569211 | 0      |
|  67 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
|  68 | Tensor<[1, 12, 1, s0 + 1]> self = ?,<br>Tensor<[1, 12, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
|  69 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?         | Unknown  | Done       | 0.9999979702251268 | 0      |
|  70 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor<[1, 12, 10, 10]> other = ?       | Unknown  | Done       | 0.9999981069703573 | 0      |
|  71 | Tensor<[1, 12, 128]> self = ?,<br>Tensor<[1, 12, 128]> other = ?             | Done     | Done       | 0.9999979843310226 | 0      |
|  72 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor<[1, 1, 1, 201]> other = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  73 | Tensor<[1, 12, 24, 24]> self = ?,<br>Tensor<[1, 1, 24, 24]> other = ?        | Unknown  | Done       | 0.9999981271224938 | 0      |
|  74 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 1.0                        | Done     | Done       | 0.999994865054074  | 0      |
|  75 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?           | Done     | Done       | 0.9999978937036484 | 0      |
|  76 | Tensor<[1, 12, 45, 45]> self = ?,<br>Tensor<[1, 1, 45, 45]> other = ?        | Unknown  | Done       | 0.9999980003714501 | 0      |
|  77 | Tensor<[1, 12, 56, 56]> self = ?,<br>Tensor<[1, 12, 56, 56]> other = ?       | Done     | Done       | 0.999997997298681  | 0      |
|  78 | Tensor<[1, 12, 768]> self = ?,<br>Tensor<[1, 12, 768]> other = ?             | Done     | Done       | 0.9999980740801346 | 0      |
|  79 | Tensor<[1, 120, 17, 17]> self = ?,<br>Tensor<[1, 120, 17, 17]> other = ?     | Done     | Done       | 0.9999979883473519 | 0      |
|  80 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?     | Done     | Done       | 0.9999979813123183 | 0      |
|  81 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?         | Done     | Done       | 0.9999979922302448 | 0      |
|  82 | Tensor<[1, 1232, 14, 14]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?   | Done     | Done       | 0.9999979838948917 | 0      |
|  83 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Removed  | Done       | 1.0                | 0      |
|  84 | Tensor<[1, 128, 112, 112]> self = ?,<br>Tensor<[1, 128, 112, 112]> other = ? | Done     | Done       | 0.9999979860401011 | 0      |
|  85 | Tensor<[1, 128, 128, 128]> self = ?,<br>Tensor<[1, 128, 128, 128]> other = ? | Done     | Done       | 0.9999979930048071 | 0      |
|  86 | Tensor<[1, 128, 1568]> self = ?,<br>Tensor<[1, 128, 1568]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
|  87 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Done     | Done       | 0.9999979901728873 | 0      |
|  88 | Tensor<[1, 128, 28, 28]> self = ?,<br>Tensor<[1, 128, 28, 28]> other = ?     | Done     | Done       | 0.9999980070937423 | 0      |
|  89 | Tensor<[1, 128, 56, 56]> self = ?,<br>Tensor<[1, 128, 56, 56]> other = ?     | Done     | Done       | 0.9999979917317474 | 0      |
|  90 | Tensor<[1, 128, 64, 64]> self = ?,<br>Tensor<[1, 128, 64, 64]> other = ?     | Done     | Done       | 0.9999980015104699 | 0      |
|  91 | Tensor<[1, 128, 75, 75]> self = ?,<br>Tensor<[1, 128, 75, 75]> other = ?     | Done     | Done       | 0.9999980022575582 | 0      |
|  92 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?      | Done     | Done       | 0.9999979073924515 | 0      |
|  93 | Tensor<[1, 128, s1, s2]> self = ?,<br>Tensor<[1, 128, s1, s2]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
|  94 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?     | Done     | Unknown    | N/A                | N/A    |
|  95 | Tensor<[1, 1280, 16, 16]> self = ?,<br>Tensor<[1, 1280, 16, 16]> other = ?   | Done     | Unknown    | N/A                | N/A    |
|  96 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 1, 1]> other = ?       | Done     | Done       | 0.9999979780730145 | 0      |
|  97 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor<[1, 1280, 8, 8]> other = ?       | Done     | Done       | 0.9999980042404504 | 0      |
|  98 | Tensor<[1, 1344, 14, 14]> self = ?,<br>Tensor<[1, 1344, 14, 14]> other = ?   | Done     | Done       | 0.9999979821072588 | 0      |
|  99 | Tensor<[1, 136, 19, 19]> self = ?,<br>Tensor<[1, 136, 19, 19]> other = ?     | Done     | Done       | 0.9999979833084801 | 0      |
| 100 | Tensor<[1, 1370, 1280]> self = ?,<br>Tensor<[1, 1370, 1280]> other = ?       | Done     | Done       | 0.9999979980654398 | 0      |
| 101 | Tensor<[1, 1392, 14, 14]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?   | Done     | Done       | 0.9999979802768829 | 0      |
| 102 | Tensor<[1, 14, 128]> self = ?,<br>Tensor<[1, 14, 128]> other = ?             | Done     | Done       | 0.9999978068675641 | 0      |
| 103 | Tensor<[1, 14, 14, 384]> self = ?,<br>Tensor<[1, 14, 14, 384]> other = ?     | Done     | Done       | 0.9999979659330713 | 0      |
| 104 | Tensor<[1, 14, 14, 512]> self = ?,<br>Tensor<[1, 14, 14, 512]> other = ?     | Done     | Done       | 0.9999979765119369 | 0      |
| 105 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 1.0                        | Done     | Done       | 0.9999947259630234 | 0      |
| 106 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?           | Done     | Done       | 0.9999980375093064 | 0      |
| 107 | Tensor<[1, 14, 56, 56]> self = ?,<br>Tensor<[1, 14, 56, 56]> other = ?       | Done     | Done       | 0.9999979848176276 | 0      |
| 108 | Tensor<[1, 14, 768]> self = ?,<br>Tensor<[1, 14, 768]> other = ?             | Done     | Done       | 0.9999979232056743 | 0      |
| 109 | Tensor<[1, 144, 28, 28]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?     | Done     | Done       | 0.9999980158318528 | 0      |
| 110 | Tensor<[1, 144, 7, 7]> self = ?,<br>Tensor<[1, 144, 7, 7]> other = ?         | Done     | Done       | 0.9999981309886272 | 0      |
| 111 | Tensor<[1, 1445, 192]> self = ?,<br>Tensor<[1, 1445, 192]> other = ?         | Done     | Done       | 0.9999979905739044 | 0      |
| 112 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 1.0                        | Unknown  | Done       | 0.9999947446058011 | 0      |
| 113 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?           | Unknown  | Done       | 0.9999980560859794 | 0      |
| 114 | Tensor<[1, 15, 1]> self = ?,<br>Tensor other = 1e-06                         | Unknown  | Done       | 1.0                | 0      |
| 115 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?             | Unknown  | Done       | 0.9999978099399699 | 0      |
| 116 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1, 1500, 768]> other = ?         | Unknown  | Done       | 0.999997978818409  | 0      |
| 117 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor<[1500, 768]> other = ?            | Unknown  | Done       | 0.9999979915743177 | 0      |
| 118 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?       | Done     | Done       | 0.999998003733222  | 0      |
| 119 | Tensor<[1, 1536, 8, 8]> self = ?,<br>Tensor<[1, 1536, 8, 8]> other = ?       | Done     | Done       | 0.9999979823457743 | 0      |
| 120 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
| 121 | Tensor<[1, 16, 1, 10]> self = ?,<br>Tensor<[1, 16, 1, 10]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 122 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?            | Unknown  | Done       | 0.99998960249902   | 0      |
| 123 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 1, 1]> other = ?           | Unknown  | Done       | 0.9999985162671678 | 0      |
| 124 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 125 | Tensor<[1, 16, 1, 2]> self = ?,<br>Tensor<[1, 16, 1, 2]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 126 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[1, 1, 1, 6]> other = ?            | Unknown  | Done       | 0.9999990576792989 | 0      |
| 127 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 128 | Tensor<[1, 16, 1, s0 + 1]> self = ?,<br>Tensor<[1, 16, 1, s0 + 1]> other = ? | Unknown  | Unknown    | N/A                | N/A    |
| 129 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?         | Unknown  | Done       | 0.9999976840476515 | 0      |
| 130 | Tensor<[1, 16, 10, 10]> self = ?,<br>Tensor<[1, 16, 10, 10]> other = ?       | Unknown  | Done       | 0.9999983237570677 | 0      |
| 131 | Tensor<[1, 16, 112, 112]> self = ?,<br>Tensor<[1, 16, 112, 112]> other = ?   | Done     | Done       | 0.9999979809051136 | 0      |
| 132 | Tensor<[1, 16, 16, 384]> self = ?,<br>Tensor<[1, 16, 16, 384]> other = ?     | Done     | Done       | 0.9999980029290743 | 0      |
| 133 | Tensor<[1, 16, 16, 512]> self = ?,<br>Tensor<[1, 16, 16, 512]> other = ?     | Done     | Done       | 0.9999979733236738 | 0      |
| 134 | Tensor<[1, 16, 160, 160]> self = ?,<br>Tensor<[1, 16, 160, 160]> other = ?   | Done     | Done       | 0.9999980108410926 | 0      |
| 135 | Tensor<[1, 16, 28, 28]> self = ?,<br>Tensor<[1, 16, 28, 28]> other = ?       | Done     | Done       | 0.9999980072591034 | 0      |
| 136 | Tensor<[1, 16, 32, 32]> self = ?,<br>Tensor<[1, 1, 32, 32]> other = ?        | Done     | Unknown    | N/A                | N/A    |
| 137 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[1, 1, 5, 5]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 138 | Tensor<[1, 16, 6, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ? | None     | Fallback   | 1.0                | -1     |
| 139 | Tensor<[1, 16, 6, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | None     | Fallback   | 1.0                | -1     |
| 140 | Tensor<[1, 16, 768]> self = ?,<br>Tensor<[1, 16, 768]> other = ?             | Done     | Done       | 0.9999979422513713 | 0      |
| 141 | Tensor<[1, 16, 8, 49, 49]> self = ?,<br>Tensor<[1, 16, 1, 49, 49]> other = ? | None     | Fallback   | 1.0                | -1     |
| 142 | Tensor<[1, 16, 8, 64, 64]> self = ?,<br>Tensor<[1, 16, 1, 64, 64]> other = ? | None     | Fallback   | 1.0                | -1     |
| 143 | Tensor<[1, 160, 14, 14]> self = ?,<br>Tensor<[1, 160, 14, 14]> other = ?     | Done     | Done       | 0.9999979147455889 | 0      |
| 144 | Tensor<[1, 160, 24, 24]> self = ?,<br>Tensor<[1, 160, 24, 24]> other = ?     | Done     | Done       | 0.9999979877126515 | 0      |
| 145 | Tensor<[1, 160, 28, 28]> self = ?,<br>Tensor<[1, 160, 28, 28]> other = ?     | Done     | Done       | 0.9999980158460512 | 0      |
| 146 | Tensor<[1, 160, 32, 32]> self = ?,<br>Tensor<[1, 160, 32, 32]> other = ?     | Done     | Done       | 0.9999979670719309 | 0      |
| 147 | Tensor<[1, 160, 7, 7]> self = ?,<br>Tensor<[1, 160, 7, 7]> other = ?         | Done     | Done       | 0.9999982099134319 | 0      |
| 148 | Tensor<[1, 160, 73, 73]> self = ?,<br>Tensor<[1, 160, 73, 73]> other = ?     | Done     | Done       | 0.9999979921248096 | 0      |
| 149 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[256]> other = ?                 | Done     | Done       | 0.9999979489932801 | 0      |
| 150 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 16384, 32]> other = ?         | Done     | Done       | 0.9999979936223977 | 0      |
| 151 | Tensor<[1, 168, 28, 28]> self = ?,<br>Tensor<[1, 168, 28, 28]> other = ?     | Done     | Done       | 0.9999979942073871 | 0      |
| 152 | Tensor<[1, 18, 56, 56]> self = ?,<br>Tensor<[1, 18, 56, 56]> other = ?       | Done     | Done       | 0.9999980046149719 | 0      |
| 153 | Tensor<[1, 185, 28, 28]> self = ?,<br>Tensor<[1, 185, 28, 28]> other = ?     | Done     | Done       | 0.9999979790041587 | 0      |
| 154 | Tensor<[1, 192, 14, 14]> self = ?,<br>Tensor<[1, 192, 14, 14]> other = ?     | Done     | Done       | 0.9999979594557559 | 0      |
| 155 | Tensor<[1, 192, 28, 28]> self = ?,<br>Tensor<[1, 192, 28, 28]> other = ?     | Done     | Done       | 0.9999979675940719 | 0      |
| 156 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 192, 32, 42]> other = ?     | Done     | Done       | 0.9999979878114481 | 0      |
| 157 | Tensor<[1, 192, 7, 7]> self = ?,<br>Tensor<[1, 192, 7, 7]> other = ?         | Done     | Done       | 0.9999979080867666 | 0      |
| 158 | Tensor<[1, 192, 71, 71]> self = ?,<br>Tensor<[1, 192, 71, 71]> other = ?     | Done     | Done       | 0.9999979918256189 | 0      |
| 159 | Tensor<[1, 192, 8, 8]> self = ?,<br>Tensor<[1, 192, 8, 8]> other = ?         | Done     | Done       | 0.9999978050756189 | 0      |
| 160 | Tensor<[1, 1920, 7, 7]> self = ?,<br>Tensor<[1, 1920, 7, 7]> other = ?       | Done     | Done       | 0.9999980038078724 | 0      |
| 161 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?         | Done     | Done       | 0.9999980010294    | 0      |
| 162 | Tensor<[1, 193, 768]> self = ?,<br>Tensor<[1, 193, 768]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 163 | Tensor<[1, 196, 14, 14]> self = ?,<br>Tensor<[1, 196, 14, 14]> other = ?     | Done     | Done       | 0.9999980000045974 | 0      |
| 164 | Tensor<[1, 196, 768]> self = ?,<br>Tensor<[1, 196, 768]> other = ?           | Done     | Done       | 0.9999979890722033 | 0      |
| 165 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?         | Done     | Done       | 0.9999979869008305 | 0      |
| 166 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?           | Done     | Done       | 0.9999980021946429 | 0      |
| 167 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                 | Unknown  | Done       | 1.0                | 0      |
| 168 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                | 0      |
| 169 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2                                 | Unknown  | Done       | 1.0                | 0      |
| 170 | Tensor<[1, 20, 28, 28]> self = ?,<br>Tensor<[1, 20, 28, 28]> other = ?       | Done     | Done       | 0.999997954630629  | 0      |
| 171 | Tensor<[1, 201, 768]> self = ?,<br>Tensor<[1, 201, 768]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 172 | Tensor<[1, 2016, 7, 7]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?       | Done     | Done       | 0.9999979568737094 | 0      |
| 173 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor other = 1e-05                    | Removed  | Done       | 1.0                | 0      |
| 174 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?     | Done     | Done       | 0.9999979900384247 | 0      |
| 175 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 23, 40]> other = ?   | Done     | Done       | 0.9999979955081977 | 0      |
| 176 | Tensor<[1, 2048, 7, 7]> self = ?,<br>Tensor<[1, 2048, 7, 7]> other = ?       | Done     | Done       | 0.9999980169505414 | 0      |
| 177 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[1, 2048, 768]> other = ?         | Done     | Done       | 0.9999979926029143 | 0      |
| 178 | Tensor<[1, 2048, 768]> self = ?,<br>Tensor<[2048, 768]> other = ?            | Done     | Done       | 0.9999979924107085 | 0      |
| 179 | Tensor<[1, 208, 14, 14]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?     | Done     | Done       | 0.9999979925653657 | 0      |
| 180 | Tensor<[1, 208, 9, 9]> self = ?,<br>Tensor<[1, 208, 9, 9]> other = ?         | Done     | Done       | 0.9999979320388682 | 0      |
| 181 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?     | Done     | Done       | 0.9999979674531391 | 0      |
| 182 | Tensor<[1, 224, 56, 56]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?     | Done     | Done       | 0.9999979862889601 | 0      |
| 183 | Tensor<[1, 224, 7, 7]> self = ?,<br>Tensor<[1, 224, 7, 7]> other = ?         | Done     | Done       | 0.999998139726348  | 0      |
| 184 | Tensor<[1, 23, 1]> self = ?,<br>Tensor other = 1e-06                         | Done     | Done       | 1.0                | 0      |
| 185 | Tensor<[1, 232, 10, 10]> self = ?,<br>Tensor<[1, 232, 10, 10]> other = ?     | Done     | Done       | 0.9999979793100816 | 0      |
| 186 | Tensor<[1, 232, 56, 56]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?     | Done     | Done       | 0.9999979917146706 | 0      |
| 187 | Tensor<[1, 24, 112, 112]> self = ?,<br>Tensor<[1, 24, 112, 112]> other = ?   | Done     | Done       | 0.9999979943975437 | 0      |
| 188 | Tensor<[1, 24, 28, 28]> self = ?,<br>Tensor<[1, 24, 28, 28]> other = ?       | Done     | Done       | 0.999998032447363  | 0      |
| 189 | Tensor<[1, 24, 49, 49]> self = ?,<br>Tensor<[1, 24, 49, 49]> other = ?       | Done     | Done       | 0.9999979794868655 | 0      |
| 190 | Tensor<[1, 24, 56, 56]> self = ?,<br>Tensor<[1, 24, 56, 56]> other = ?       | Done     | Done       | 0.9999980062173234 | 0      |
| 191 | Tensor<[1, 24, 60, 60]> self = ?,<br>Tensor<[1, 24, 60, 60]> other = ?       | Done     | Done       | 0.9999979802931823 | 0      |
| 192 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[1, 24, 64, 64]> other = ?       | Done     | Done       | 0.9999980032685525 | 0      |
| 193 | Tensor<[1, 24, 65, 65]> self = ?,<br>Tensor<[1, 24, 65, 65]> other = ?       | Done     | Done       | 0.9999979666551547 | 0      |
| 194 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<[1, 24, 768]> other = ?             | Unknown  | Done       | 0.9999979379711683 | 0      |
| 195 | Tensor<[1, 24, 80, 80]> self = ?,<br>Tensor<[1, 24, 80, 80]> other = ?       | Done     | Done       | 0.9999980121267583 | 0      |
| 196 | Tensor<[1, 240, 14, 14]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?     | Done     | Done       | 0.9999980056473237 | 0      |
| 197 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?     | Done     | Done       | 0.9999979841577176 | 0      |
| 198 | Tensor<[1, 25, 768]> self = ?,<br>Tensor<[1, 25, 768]> other = ?             | Done     | Done       | 0.9999979993567008 | 0      |
| 199 | Tensor<[1, 2520, 7, 7]> self = ?,<br>Tensor<[1, 2520, 7, 7]> other = ?       | Done     | Done       | 0.9999980569854193 | 0      |
| 200 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Removed  | Done       | 1.0                | 0      |
| 201 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[1, 256, 128, 128]> other = ? | Done     | Done       | 0.9999979970827907 | 0      |
| 202 | Tensor<[1, 256, 1280]> self = ?,<br>Tensor<[1, 256, 1280]> other = ?         | Done     | Done       | 0.9999980166361498 | 0      |
| 203 | Tensor<[1, 256, 14, 14]> self = ?,<br>Tensor<[1, 256, 14, 14]> other = ?     | Done     | Done       | 0.9999978958290596 | 0      |
| 204 | Tensor<[1, 256, 16, 16]> self = ?,<br>Tensor<[1, 256, 16, 16]> other = ?     | Done     | Done       | 0.9999979970439977 | 0      |
| 205 | Tensor<[1, 256, 160]> self = ?,<br>Tensor<[1, 256, 160]> other = ?           | Done     | Done       | 0.9999980221107344 | 0      |
| 206 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Done     | Done       | 0.9999979525318828 | 0      |
| 207 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 180, 320]> other = ? | Done     | Done       | 0.9999979913392014 | 0      |
| 208 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 256, 256]> other = ?           | Done     | Done       | 0.9999979713277076 | 0      |
| 209 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.9999979516343264 | 0      |
| 210 | Tensor<[1, 256, 28, 28]> self = ?,<br>Tensor<[1, 256, 28, 28]> other = ?     | Done     | Done       | 0.9999980364756889 | 0      |
| 211 | Tensor<[1, 256, 32, 32]> self = ?,<br>Tensor<[1, 256, 32, 32]> other = ?     | Done     | Done       | 0.9999979773420522 | 0      |
| 212 | Tensor<[1, 256, 32]> self = ?,<br>Tensor<[1, 256, 32]> other = ?             | Done     | Done       | 0.9999980684792551 | 0      |
| 213 | Tensor<[1, 256, 38, 38]> self = ?,<br>Tensor<[1, 256, 38, 38]> other = ?     | Done     | Done       | 0.999997990492088  | 0      |
| 214 | Tensor<[1, 256, 392]> self = ?,<br>Tensor<[1, 256, 392]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 215 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999980424499485 | 0      |
| 216 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?     | Done     | Done       | 0.9999979850685888 | 0      |
| 217 | Tensor<[1, 256, 64, 64]> self = ?,<br>Tensor<[1, 256, 64, 64]> other = ?     | Done     | Done       | 0.9999979938238583 | 0      |
| 218 | Tensor<[1, 256, 64]> self = ?,<br>Tensor<[1, 256, 64]> other = ?             | Done     | Done       | 0.999998004832213  | 0      |
| 219 | Tensor<[1, 256, 7, 7]> self = ?,<br>Tensor<[1, 256, 7, 7]> other = ?         | Done     | Done       | 0.9999978400850306 | 0      |
| 220 | Tensor<[1, 256, 75, 75]> self = ?,<br>Tensor<[1, 256, 75, 75]> other = ?     | Done     | Done       | 0.9999979899377041 | 0      |
| 221 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999979565354868 | 0      |
| 222 | Tensor<[1, 256, s1, s2]> self = ?,<br>Tensor<[1, 256, s1, s2]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 223 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[1, 257, 768]> other = ?           | Done     | Unknown    | N/A                | N/A    |
| 224 | Tensor<[1, 272, 12, 12]> self = ?,<br>Tensor<[1, 272, 12, 12]> other = ?     | Done     | Done       | 0.9999980265541726 | 0      |
| 225 | Tensor<[1, 272, 7, 7]> self = ?,<br>Tensor<[1, 272, 7, 7]> other = ?         | Done     | Done       | 0.9999978697969247 | 0      |
| 226 | Tensor<[1, 28, 28, 192]> self = ?,<br>Tensor<[1, 28, 28, 192]> other = ?     | Done     | Done       | 0.9999980005233472 | 0      |
| 227 | Tensor<[1, 28, 28, 256]> self = ?,<br>Tensor<[1, 28, 28, 256]> other = ?     | Done     | Done       | 0.9999980226592834 | 0      |
| 228 | Tensor<[1, 28, 28, 28]> self = ?,<br>Tensor<[1, 28, 28, 28]> other = ?       | Done     | Done       | 0.9999979786159262 | 0      |
| 229 | Tensor<[1, 288, 14, 14]> self = ?,<br>Tensor<[1, 288, 14, 14]> other = ?     | Done     | Done       | 0.99999800586373   | 0      |
| 230 | Tensor<[1, 2904, 24, 24]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?   | Done     | Done       | 0.9999979959928952 | 0      |
| 231 | Tensor<[1, 2]> self = ?,<br>Tensor other = 0                                 | Unknown  | Unknown    | N/A                | N/A    |
| 232 | Tensor<[1, 2]> self = ?,<br>Tensor other = 16                                | Unknown  | Unknown    | N/A                | N/A    |
| 233 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[1, 3, 16, 16, 2]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 234 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[1, 3, 300, 300]> other = ?     | Done     | Done       | 0.9999980032343835 | 0      |
| 235 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[1, 3, 32, 32, 2]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 236 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[1, 3, 320, 320]> other = ?     | Done     | Done       | 0.9999979936287032 | 0      |
| 237 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[1, 3, 64, 64, 2]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 238 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?           | Done     | Done       | 0.9999980185905533 | 0      |
| 239 | Tensor<[1, 3024, 7, 7]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?       | Done     | Done       | 0.9999979826546537 | 0      |
| 240 | Tensor<[1, 32, 112, 112]> self = ?,<br>Tensor<[1, 32, 112, 112]> other = ?   | Done     | Done       | 0.9999980024003217 | 0      |
| 241 | Tensor<[1, 32, 128, 128]> self = ?,<br>Tensor<[1, 32, 128, 128]> other = ?   | Done     | Done       | 0.9999980025830492 | 0      |
| 242 | Tensor<[1, 32, 1536]> self = ?,<br>Tensor<[1, 32, 1536]> other = ?           | Done     | Done       | 0.9999980058303886 | 0      |
| 243 | Tensor<[1, 32, 1]> self = ?,<br>Tensor other = 1e-06                         | Unknown  | Unknown    | N/A                | N/A    |
| 244 | Tensor<[1, 32, 25088]> self = ?,<br>Tensor<[1, 32, 25088]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 245 | Tensor<[1, 32, 256, 256]> self = ?,<br>Tensor<[1, 32, 256, 256]> other = ?   | Done     | Done       | 0.9999980026820886 | 0      |
| 246 | Tensor<[1, 32, 28, 28]> self = ?,<br>Tensor<[1, 32, 28, 28]> other = ?       | Done     | Done       | 0.9999979575694643 | 0      |
| 247 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 32, 32, 128]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 248 | Tensor<[1, 32, 32, 192]> self = ?,<br>Tensor<[1, 32, 32, 192]> other = ?     | Done     | Done       | 0.999997989821898  | 0      |
| 249 | Tensor<[1, 32, 32, 256]> self = ?,<br>Tensor<[1, 32, 32, 256]> other = ?     | Done     | Done       | 0.9999979856869272 | 0      |
| 250 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 251 | Tensor<[1, 32, 49, 49]> self = ?,<br>Tensor<[1, 32, 49, 49]> other = ?       | Done     | Done       | 0.9999979874051873 | 0      |
| 252 | Tensor<[1, 32, 56, 56]> self = ?,<br>Tensor<[1, 32, 56, 56]> other = ?       | Done     | Done       | 0.9999980248611812 | 0      |
| 253 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1                          | Done     | Done       | 0.9999948037222828 | 0      |
| 254 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 1.0                        | Done     | Done       | 0.9999948463517582 | 0      |
| 255 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[1, 32, 64, 64]> other = ?       | Done     | Done       | 0.9999979810647389 | 0      |
| 256 | Tensor<[1, 32, 75, 75]> self = ?,<br>Tensor<[1, 32, 75, 75]> other = ?       | Done     | Done       | 0.9999979801136969 | 0      |
| 257 | Tensor<[1, 32, 95, 95]> self = ?,<br>Tensor<[1, 32, 95, 95]> other = ?       | Done     | Done       | 0.9999979963587984 | 0      |
| 258 | Tensor<[1, 32, s0, s1]> self = ?,<br>Tensor<[1, 32, s0, s1]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 259 | Tensor<[1, 320, 14, 14]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?     | Done     | Done       | 0.9999979154464117 | 0      |
| 260 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 1, 1]> other = ?       | Done     | Done       | 0.9999980031160945 | 0      |
| 261 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor<[1, 320, 64, 64]> other = ?     | Done     | Done       | 0.9999979872919947 | 0      |
| 262 | Tensor<[1, 336, 14, 14]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?     | Done     | Done       | 0.9999979432394084 | 0      |
| 263 | Tensor<[1, 336, 56, 56]> self = ?,<br>Tensor<[1, 336, 56, 56]> other = ?     | Done     | Done       | 0.9999979868265428 | 0      |
| 264 | Tensor<[1, 34, 28, 28]> self = ?,<br>Tensor<[1, 34, 28, 28]> other = ?       | Done     | Done       | 0.9999980231567408 | 0      |
| 265 | Tensor<[1, 36, 28, 28]> self = ?,<br>Tensor<[1, 36, 28, 28]> other = ?       | Done     | Done       | 0.9999979904038695 | 0      |
| 266 | Tensor<[1, 36, 56, 56]> self = ?,<br>Tensor<[1, 36, 56, 56]> other = ?       | Done     | Done       | 0.9999980300587252 | 0      |
| 267 | Tensor<[1, 3712, 7, 7]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?       | Done     | Done       | 0.9999979716360131 | 0      |
| 268 | Tensor<[1, 384, 35, 35]> self = ?,<br>Tensor<[1, 384, 35, 35]> other = ?     | Done     | Done       | 0.9999979899410594 | 0      |
| 269 | Tensor<[1, 384, 8, 8]> self = ?,<br>Tensor<[1, 384, 8, 8]> other = ?         | Done     | Done       | 0.999997930290333  | 0      |
| 270 | Tensor<[1, 4, 12, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 271 | Tensor<[1, 4, 12, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 272 | Tensor<[1, 4, 16, 49, 49]> self = ?,<br>Tensor<[1, 4, 1, 49, 49]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 273 | Tensor<[1, 4, 16, 64, 64]> self = ?,<br>Tensor<[1, 4, 1, 64, 64]> other = ?  | None     | Fallback   | 1.0                | -1     |
| 274 | Tensor<[1, 4, 768]> self = ?,<br>Tensor<[1, 4, 768]> other = ?               | Unknown  | Done       | 0.9999978536711165 | 0      |
| 275 | Tensor<[1, 40, 14, 14]> self = ?,<br>Tensor<[1, 40, 14, 14]> other = ?       | Done     | Done       | 0.9999980406990658 | 0      |
| 276 | Tensor<[1, 40, 28, 28]> self = ?,<br>Tensor<[1, 40, 28, 28]> other = ?       | Done     | Done       | 0.9999980578230603 | 0      |
| 277 | Tensor<[1, 40, 30, 30]> self = ?,<br>Tensor<[1, 40, 30, 30]> other = ?       | Done     | Done       | 0.9999980527048626 | 0      |
| 278 | Tensor<[1, 40, 40, 40]> self = ?,<br>Tensor<[1, 40, 40, 40]> other = ?       | Done     | Done       | 0.999997989405623  | 0      |
| 279 | Tensor<[1, 40, 56, 56]> self = ?,<br>Tensor<[1, 40, 56, 56]> other = ?       | Done     | Done       | 0.9999980535446145 | 0      |
| 280 | Tensor<[1, 400, 7, 7]> self = ?,<br>Tensor<[1, 400, 7, 7]> other = ?         | Done     | Done       | 0.9999980418583142 | 0      |
| 281 | Tensor<[1, 408, 14, 14]> self = ?,<br>Tensor<[1, 408, 14, 14]> other = ?     | Done     | Done       | 0.9999979596834631 | 0      |
| 282 | Tensor<[1, 4096, 256]> self = ?,<br>Tensor<[256]> other = ?                  | Done     | Done       | 0.9999980160629338 | 0      |
| 283 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor<[1, 4096, 320]> other = ?         | Done     | Done       | 0.9999979839732381 | 0      |
| 284 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 4096, 64]> other = ?           | Done     | Done       | 0.9999980175179415 | 0      |
| 285 | Tensor<[1, 432, 14, 14]> self = ?,<br>Tensor<[1, 432, 14, 14]> other = ?     | Done     | Done       | 0.9999980273013738 | 0      |
| 286 | Tensor<[1, 440, 7, 7]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?         | Done     | Done       | 0.9999980019405339 | 0      |
| 287 | Tensor<[1, 448, 28, 28]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?     | Done     | Done       | 0.9999979721095986 | 0      |
| 288 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 1.0                        | Unknown  | Done       | 0.999994792299261  | 0      |
| 289 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?           | Unknown  | Done       | 0.9999979954166095 | 0      |
| 290 | Tensor<[1, 45, 768]> self = ?,<br>Tensor<[1, 45, 768]> other = ?             | Unknown  | Done       | 0.9999980647183647 | 0      |
| 291 | Tensor<[1, 45]> self = ?,<br>Tensor<[1, 45]> other = ?                       | Unknown  | Unknown    | N/A                | N/A    |
| 292 | Tensor<[1, 46, 28, 28]> self = ?,<br>Tensor<[1, 46, 28, 28]> other = ?       | Done     | Done       | 0.9999979936701304 | 0      |
| 293 | Tensor<[1, 48, 14, 14]> self = ?,<br>Tensor<[1, 48, 14, 14]> other = ?       | Done     | Unknown    | N/A                | N/A    |
| 294 | Tensor<[1, 48, 33, 33]> self = ?,<br>Tensor<[1, 48, 33, 33]> other = ?       | Done     | Done       | 0.99999801761218   | 0      |
| 295 | Tensor<[1, 48, 38, 38]> self = ?,<br>Tensor<[1, 48, 38, 38]> other = ?       | Done     | Done       | 0.9999979872621354 | 0      |
| 296 | Tensor<[1, 48, 56, 56]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?       | Done     | Done       | 0.9999980080498518 | 0      |
| 297 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?     | Done     | Done       | 0.9999979799761215 | 0      |
| 298 | Tensor<[1, 480, 7, 7]> self = ?,<br>Tensor<[1, 480, 7, 7]> other = ?         | Done     | Done       | 0.9999979146737118 | 0      |
| 299 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?         | Done     | Done       | 0.9999979894647079 | 0      |
| 300 | Tensor<[1, 5, 1024]> self = ?,<br>Tensor<[1, 5, 1024]> other = ?             | Unknown  | Done       | 0.9999981303465112 | 0      |
| 301 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 16, 32]> other = ?         | Unknown  | Done       | 0.9999980180895619 | 0      |
| 302 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 1.0                         | Unknown  | Done       | 0.9999949042737246 | 0      |
| 303 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?             | Unknown  | Done       | 0.9999980832180688 | 0      |
| 304 | Tensor<[1, 50, 1024]> self = ?,<br>Tensor<[1, 50, 1024]> other = ?           | Done     | Done       | 0.9999979817438893 | 0      |
| 305 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?           | Done     | Done       | 0.99999798390132   | 0      |
| 306 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?             | Done     | Done       | 0.9999979544533946 | 0      |
| 307 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor other = 1e-05                     | Removed  | Done       | 1.0                | 0      |
| 308 | Tensor<[1, 512, 14, 14]> self = ?,<br>Tensor<[1, 512, 14, 14]> other = ?     | Done     | Done       | 0.9999979664908696 | 0      |
| 309 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.999997941876493  | 0      |
| 310 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?     | Done     | Done       | 0.9999980047566305 | 0      |
| 311 | Tensor<[1, 512, 32, 32]> self = ?,<br>Tensor<[1, 512, 32, 32]> other = ?     | Done     | Done       | 0.9999979943167143 | 0      |
| 312 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999979945215994 | 0      |
| 313 | Tensor<[1, 512, 7, 7]> self = ?,<br>Tensor<[1, 512, 7, 7]> other = ?         | Done     | Done       | 0.9999980000081701 | 0      |
| 314 | Tensor<[1, 512, 8, 8]> self = ?,<br>Tensor<[1, 512, 8, 8]> other = ?         | Done     | Done       | 0.999998004535974  | 0      |
| 315 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | Done       | 0.9999979926416125 | 0      |
| 316 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 90, 160]> other = ?   | Done     | Done       | 0.9999979970021305 | 0      |
| 317 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                     | Done     | Done       | 0.9999983917019766 | 0      |
| 318 | Tensor<[1, 528, 96, 96]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?     | Done     | Done       | 0.9999979933979487 | 0      |
| 319 | Tensor<[1, 56, 14, 14]> self = ?,<br>Tensor<[1, 56, 14, 14]> other = ?       | Done     | Done       | 0.9999980105840923 | 0      |
| 320 | Tensor<[1, 56, 48, 48]> self = ?,<br>Tensor<[1, 56, 48, 48]> other = ?       | Done     | Done       | 0.9999979742361044 | 0      |
| 321 | Tensor<[1, 56, 56, 128]> self = ?,<br>Tensor<[1, 56, 56, 128]> other = ?     | Done     | Done       | 0.999997980980159  | 0      |
| 322 | Tensor<[1, 56, 56, 96]> self = ?,<br>Tensor<[1, 56, 56, 96]> other = ?       | Done     | Done       | 0.9999979729864181 | 0      |
| 323 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?     | Done     | Done       | 0.9999979854480209 | 0      |
| 324 | Tensor<[1, 58, 28, 28]> self = ?,<br>Tensor<[1, 58, 28, 28]> other = ?       | Done     | Done       | 0.9999980277612889 | 0      |
| 325 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<[1, 59, 1024]> other = ?           | Unknown  | Done       | 0.9999979904816403 | 0      |
| 326 | Tensor<[1, 59]> self = ?,<br>Tensor other = 2                                | Unknown  | Done       | 0.999987366877724  | 0      |
| 327 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?           | Unknown  | Done       | 0.9999983632808066 | 0      |
| 328 | Tensor<[1, 6, 1, 15]> self = ?,<br>Tensor<[1, 6, 1, 15]> other = ?           | Unknown  | Done       | 0.9999993249676742 | 0      |
| 329 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 1.0                | 0      |
| 330 | Tensor<[1, 6, 1, 1]> self = ?,<br>Tensor<[1, 6, 1, 1]> other = ?             | Unknown  | Done       | 0.9999942303957439 | 0      |
| 331 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 1.0                | 0      |
| 332 | Tensor<[1, 6, 1, 2]> self = ?,<br>Tensor<[1, 6, 1, 2]> other = ?             | Unknown  | Done       | 0.9999997494438243 | 0      |
| 333 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 334 | Tensor<[1, 6, 1, s0 + 1]> self = ?,<br>Tensor<[1, 6, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 335 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 1, 1, 15]> other = ?          | Unknown  | Done       | 0.9999971485331847 | 0      |
| 336 | Tensor<[1, 6, 15, 15]> self = ?,<br>Tensor<[1, 6, 15, 15]> other = ?         | Unknown  | Done       | 0.9999975168691554 | 0      |
| 337 | Tensor<[1, 60, 28, 28]> self = ?,<br>Tensor<[1, 60, 28, 28]> other = ?       | Done     | Done       | 0.9999980423621416 | 0      |
| 338 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor other = 1e-05                      | Removed  | Done       | 1.0                | 0      |
| 339 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ?   | Done     | Done       | 0.9999979797579367 | 0      |
| 340 | Tensor<[1, 64, 128, 128]> self = ?,<br>Tensor<[1, 64, 128, 128]> other = ?   | Done     | Done       | 0.9999979867377374 | 0      |
| 341 | Tensor<[1, 64, 1280]> self = ?,<br>Tensor<[1, 64, 1280]> other = ?           | Done     | Unknown    | N/A                | N/A    |
| 342 | Tensor<[1, 64, 14, 14]> self = ?,<br>Tensor<[1, 64, 14, 14]> other = ?       | Done     | Done       | 0.9999980713294618 | 0      |
| 343 | Tensor<[1, 64, 147, 147]> self = ?,<br>Tensor<[1, 64, 147, 147]> other = ?   | Done     | Done       | 0.9999979891928898 | 0      |
| 344 | Tensor<[1, 64, 150, 150]> self = ?,<br>Tensor<[1, 64, 150, 150]> other = ?   | Done     | Done       | 0.9999979872379281 | 0      |
| 345 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Done     | Done       | 0.9999978531040041 | 0      |
| 346 | Tensor<[1, 64, 224, 224]> self = ?,<br>Tensor<[1, 64, 224, 224]> other = ?   | Done     | Done       | 0.9999979817893433 | 0      |
| 347 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ?   | Done     | Done       | 0.9999979983431247 | 0      |
| 348 | Tensor<[1, 64, 256, 256]> self = ?,<br>Tensor<[1, 64, 256, 256]> other = ?   | Done     | Done       | 0.9999979933971226 | 0      |
| 349 | Tensor<[1, 64, 28, 28]> self = ?,<br>Tensor<[1, 64, 28, 28]> other = ?       | Done     | Done       | 0.9999979896413945 | 0      |
| 350 | Tensor<[1, 64, 3, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ? | None     | Fallback   | 1.0                | -1     |
| 351 | Tensor<[1, 64, 3, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | None     | Fallback   | 1.0                | -1     |
| 352 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?       | Done     | Done       | 0.9999979657709861 | 0      |
| 353 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?       | Done     | Done       | 0.999997970878811  | 0      |
| 354 | Tensor<[1, 64, 4, 49, 49]> self = ?,<br>Tensor<[1, 64, 1, 49, 49]> other = ? | None     | Fallback   | 1.0                | -1     |
| 355 | Tensor<[1, 64, 4, 64, 64]> self = ?,<br>Tensor<[1, 64, 1, 64, 64]> other = ? | None     | Fallback   | 1.0                | -1     |
| 356 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ?   | Done     | Done       | 0.9999979918375128 | 0      |
| 357 | Tensor<[1, 64, 56, 56]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?       | Done     | Done       | 0.9999980056510438 | 0      |
| 358 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?       | Done     | Done       | 0.9999979775038563 | 0      |
| 359 | Tensor<[1, 64, 6272]> self = ?,<br>Tensor<[1, 64, 6272]> other = ?           | Unknown  | Unknown    | N/A                | N/A    |
| 360 | Tensor<[1, 64, 64, 128]> self = ?,<br>Tensor<[1, 64, 64, 128]> other = ?     | Done     | Done       | 0.9999979822410269 | 0      |
| 361 | Tensor<[1, 64, 64, 64]> self = ?,<br>Tensor<[1, 64, 64, 64]> other = ?       | Done     | Done       | 0.9999980003158445 | 0      |
| 362 | Tensor<[1, 64, 64, 96]> self = ?,<br>Tensor<[1, 64, 64, 96]> other = ?       | Done     | Done       | 0.9999979970001256 | 0      |
| 363 | Tensor<[1, 64, s1, s2]> self = ?,<br>Tensor<[1, 64, s1, s2]> other = ?       | Unknown  | Unknown    | N/A                | N/A    |
| 364 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor<[1, 640, 1, 1]> other = ?       | Done     | Unknown    | N/A                | N/A    |
| 365 | Tensor<[1, 640, 32, 32]> self = ?,<br>Tensor<[1, 640, 32, 32]> other = ?     | Done     | Unknown    | N/A                | N/A    |
| 366 | Tensor<[1, 640, 7, 7]> self = ?,<br>Tensor<[1, 640, 7, 7]> other = ?         | Done     | Done       | 0.9999980364980041 | 0      |
| 367 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?     | Done     | Done       | 0.9999980233175243 | 0      |
| 368 | Tensor<[1, 672, 28, 28]> self = ?,<br>Tensor<[1, 672, 28, 28]> other = ?     | Done     | Done       | 0.9999980023131773 | 0      |
| 369 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?         | Done     | Done       | 0.9999979946556418 | 0      |
| 370 | Tensor<[1, 68, 14, 14]> self = ?,<br>Tensor<[1, 68, 14, 14]> other = ?       | Done     | Done       | 0.9999980775524285 | 0      |
| 371 | Tensor<[1, 696, 28, 28]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?     | Done     | Done       | 0.9999980028535463 | 0      |
| 372 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947873840198 | 0      |
| 373 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?             | Done     | Done       | 0.9999979984475087 | 0      |
| 374 | Tensor<[1, 7, 4544]> self = ?,<br>Tensor<[1, 7, 4544]> other = ?             | Unknown  | Unknown    | N/A                | N/A    |
| 375 | Tensor<[1, 7, 7, 1024]> self = ?,<br>Tensor<[1, 7, 7, 1024]> other = ?       | Done     | Done       | 0.9999980035095924 | 0      |
| 376 | Tensor<[1, 7, 7, 768]> self = ?,<br>Tensor<[1, 7, 7, 768]> other = ?         | Done     | Done       | 0.9999979450587964 | 0      |
| 377 | Tensor<[1, 7, 768]> self = ?,<br>Tensor<[1, 7, 768]> other = ?               | Done     | Done       | 0.9999981547716872 | 0      |
| 378 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 71, 7, 64]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 379 | Tensor<[1, 71, 7, 7]> self = ?,<br>Tensor<[1, 1, 7, 7]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
| 380 | Tensor<[1, 72, 14, 14]> self = ?,<br>Tensor<[1, 72, 14, 14]> other = ?       | Done     | Done       | 0.9999979557758352 | 0      |
| 381 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?       | Done     | Done       | 0.9999980077150192 | 0      |
| 382 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?       | Done     | Done       | 0.9999979934034391 | 0      |
| 383 | Tensor<[1, 720, 14, 14]> self = ?,<br>Tensor<[1, 720, 14, 14]> other = ?     | Done     | Done       | 0.999998004218882  | 0      |
| 384 | Tensor<[1, 728, 19, 19]> self = ?,<br>Tensor<[1, 728, 19, 19]> other = ?     | Done     | Done       | 0.9999979938437689 | 0      |
| 385 | Tensor<[1, 728, 38, 38]> self = ?,<br>Tensor<[1, 728, 38, 38]> other = ?     | Done     | Done       | 0.9999979958538338 | 0      |
| 386 | Tensor<[1, 7392, 12, 12]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?   | Done     | Done       | 0.9999979941709017 | 0      |
| 387 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?     | Done     | Done       | 0.9999979688815923 | 0      |
| 388 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 768, 16, 16]> other = ?     | Done     | Unknown    | N/A                | N/A    |
| 389 | Tensor<[1, 768, 384]> self = ?,<br>Tensor<[384]> other = ?                   | Done     | Done       | 0.9999980025962154 | 0      |
| 390 | Tensor<[1, 768, 7, 7]> self = ?,<br>Tensor<[1, 768, 7, 7]> other = ?         | Done     | Done       | 0.9999979425492848 | 0      |
| 391 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?                     | Done     | Done       | 0.9999981011010042 | 0      |
| 392 | Tensor<[1, 78, 28, 28]> self = ?,<br>Tensor<[1, 78, 28, 28]> other = ?       | Done     | Done       | 0.9999979898793352 | 0      |
| 393 | Tensor<[1, 784, 7, 7]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?         | Done     | Done       | 0.9999980797100537 | 0      |
| 394 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?           | Unknown  | Done       | 0.9999970748130573 | 0      |
| 395 | Tensor<[1, 8, 1, 10]> self = ?,<br>Tensor<[1, 8, 1, 10]> other = ?           | Unknown  | Done       | 0.9999986417519221 | 0      |
| 396 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?             | Unknown  | Done       | 1.0                | 0      |
| 397 | Tensor<[1, 8, 1, 1]> self = ?,<br>Tensor<[1, 8, 1, 1]> other = ?             | Unknown  | Done       | 0.9999980963335842 | 0      |
| 398 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?             | Unknown  | Done       | 0.9999970288822987 | 0      |
| 399 | Tensor<[1, 8, 1, 2]> self = ?,<br>Tensor<[1, 8, 1, 2]> other = ?             | Unknown  | Done       | 0.99999995194566   | 0      |
| 400 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 401 | Tensor<[1, 8, 1, s0 + 1]> self = ?,<br>Tensor<[1, 8, 1, s0 + 1]> other = ?   | Unknown  | Unknown    | N/A                | N/A    |
| 402 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 1, 1, 10]> other = ?          | Unknown  | Done       | 0.9999983173375463 | 0      |
| 403 | Tensor<[1, 8, 10, 10]> self = ?,<br>Tensor<[1, 8, 10, 10]> other = ?         | Unknown  | Done       | 0.9999984972088084 | 0      |
| 404 | Tensor<[1, 8, 112, 112]> self = ?,<br>Tensor<[1, 8, 112, 112]> other = ?     | Done     | Done       | 0.99999801715117   | 0      |
| 405 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor<[1, 1, 1, 2048]> other = ?     | Done     | Done       | 0.9999979868771034 | 0      |
| 406 | Tensor<[1, 8, 768]> self = ?,<br>Tensor<[1, 8, 768]> other = ?               | Unknown  | Done       | 0.9999979652250048 | 0      |
| 407 | Tensor<[1, 8, 8, 1024]> self = ?,<br>Tensor<[1, 8, 8, 1024]> other = ?       | Done     | Done       | 0.9999979474759073 | 0      |
| 408 | Tensor<[1, 8, 8, 768]> self = ?,<br>Tensor<[1, 8, 8, 768]> other = ?         | Done     | Done       | 0.9999979588290854 | 0      |
| 409 | Tensor<[1, 80, 10, 10]> self = ?,<br>Tensor<[1, 80, 10, 10]> other = ?       | Done     | Done       | 0.9999979421429619 | 0      |
| 410 | Tensor<[1, 80, 14, 14]> self = ?,<br>Tensor<[1, 80, 14, 14]> other = ?       | Done     | Done       | 0.9999979891929875 | 0      |
| 411 | Tensor<[1, 80, 15, 15]> self = ?,<br>Tensor<[1, 80, 15, 15]> other = ?       | Done     | Done       | 0.9999979107356405 | 0      |
| 412 | Tensor<[1, 80, 20, 20]> self = ?,<br>Tensor<[1, 80, 20, 20]> other = ?       | Done     | Done       | 0.9999979526518195 | 0      |
| 413 | Tensor<[1, 80, 56, 56]> self = ?,<br>Tensor<[1, 80, 56, 56]> other = ?       | Done     | Done       | 0.9999979764105904 | 0      |
| 414 | Tensor<[1, 80, 7, 7]> self = ?,<br>Tensor<[1, 80, 7, 7]> other = ?           | Done     | Done       | 0.9999978765228303 | 0      |
| 415 | Tensor<[1, 88, 17, 17]> self = ?,<br>Tensor<[1, 88, 17, 17]> other = ?       | Done     | Done       | 0.9999979741220129 | 0      |
| 416 | Tensor<[1, 888, 7, 7]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?         | Done     | Done       | 0.9999980308392837 | 0      |
| 417 | Tensor<[1, 896, 14, 14]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?     | Done     | Done       | 0.9999979628421064 | 0      |
| 418 | Tensor<[1, 9, 1024]> self = ?,<br>Tensor<[1, 9, 1024]> other = ?             | Done     | Done       | 0.9999980512658617 | 0      |
| 419 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 1.0                          | Done     | Done       | 0.99999505099179   | 0      |
| 420 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?               | Done     | Done       | 0.999998085721564  | 0      |
| 421 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 1.0                        | Done     | Done       | 0.9999948431835223 | 0      |
| 422 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?           | Done     | Done       | 0.9999979813156201 | 0      |
| 423 | Tensor<[1, 9, 2048]> self = ?,<br>Tensor<[1, 9, 2048]> other = ?             | Done     | Done       | 0.9999980125386616 | 0      |
| 424 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947694253326 | 0      |
| 425 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?             | Done     | Done       | 0.999998021269521  | 0      |
| 426 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999946945363074 | 0      |
| 427 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?             | Done     | Done       | 0.9999980248737688 | 0      |
| 428 | Tensor<[1, 9, 768]> self = ?,<br>Tensor<[1, 9, 768]> other = ?               | Done     | Done       | 0.9999978559276488 | 0      |
| 429 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 1.0                         | Done     | Done       | 0.9999947339659845 | 0      |
| 430 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?             | Done     | Done       | 0.9999979687923102 | 0      |
| 431 | Tensor<[1, 912, 7, 7]> self = ?,<br>Tensor<[1, 912, 7, 7]> other = ?         | Done     | Done       | 0.9999979773925434 | 0      |
| 432 | Tensor<[1, 92, 14, 14]> self = ?,<br>Tensor<[1, 92, 14, 14]> other = ?       | Done     | Done       | 0.9999981339448503 | 0      |
| 433 | Tensor<[1, 96, 14, 14]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?       | Done     | Done       | 0.9999979578858379 | 0      |
| 434 | Tensor<[1, 96, 19, 19]> self = ?,<br>Tensor<[1, 96, 19, 19]> other = ?       | Done     | Done       | 0.9999979801983843 | 0      |
| 435 | Tensor<[1, 96, 56, 56]> self = ?,<br>Tensor<[1, 96, 56, 56]> other = ?       | Done     | Done       | 0.9999979864199797 | 0      |
| 436 | Tensor<[1, 96, 7, 7]> self = ?,<br>Tensor<[1, 96, 7, 7]> other = ?           | Done     | Unknown    | N/A                | N/A    |
| 437 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?         | Done     | Done       | 0.9999979758750713 | 0      |
| 438 | Tensor<[1, 98, 28, 28]> self = ?,<br>Tensor<[1, 98, 28, 28]> other = ?       | Done     | Done       | 0.9999979871305006 | 0      |
| 439 | Tensor<[1, 98, 80]> self = ?,<br>Tensor<[1, 98, 80]> other = ?               | Unknown  | Unknown    | N/A                | N/A    |
| 440 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 0                            | Unknown  | Unknown    | N/A                | N/A    |
| 441 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 16                           | Unknown  | Unknown    | N/A                | N/A    |
| 442 | Tensor<[1, s0, 768]> self = ?,<br>Tensor<[1, s0, 768]> other = ?             | Unknown  | Unknown    | N/A                | N/A    |
| 443 | Tensor<[10, 10]> self = ?,<br>Tensor other = 0                               | Unknown  | Done       | 1.0                | 0      |
| 444 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                               | Unknown  | Done       | 0.999921154722502  | 0      |
| 445 | Tensor<[10, 10]> self = ?,<br>Tensor<[10, 10]> other = ?                     | Unknown  | Done       | 0.9999980495768591 | 0      |
| 446 | Tensor<[100, 1, 256]> self = ?,<br>Tensor<[100, 1, 256]> other = ?           | Done     | Done       | 0.9999980237172471 | 0      |
| 447 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 24]> other = ?             | Unknown  | Done       | 0.999997945551575  | 0      |
| 448 | Tensor<[15, 15]> self = ?,<br>Tensor other = 0                               | Unknown  | Done       | 1.0                | 0      |
| 449 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                               | Unknown  | Done       | 0.9999303823329366 | 0      |
| 450 | Tensor<[15, 15]> self = ?,<br>Tensor<[15, 15]> other = ?                     | Unknown  | Done       | 0.9999979668779759 | 0      |
| 451 | Tensor<[16, 1]> self = ?,<br>Tensor other = 1                                | Done     | Unknown    | N/A                | N/A    |
| 452 | Tensor<[16, 1]> self = ?,<br>Tensor other = 1.0                              | Done     | Unknown    | N/A                | N/A    |
| 453 | Tensor<[16, 1]> self = ?,<br>Tensor other = 2                                | Done     | Unknown    | N/A                | N/A    |
| 454 | Tensor<[16, 6, 49, 49]> self = ?,<br>Tensor<[1, 6, 49, 49]> other = ?        | Done     | Done       | 0.9999980095070551 | 0      |
| 455 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[1, 6, 64, 64]> other = ?        | Done     | Done       | 0.9999980129466388 | 0      |
| 456 | Tensor<[16, 8, 49, 49]> self = ?,<br>Tensor<[1, 8, 49, 49]> other = ?        | Done     | Done       | 0.9999979507483161 | 0      |
| 457 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[1, 8, 64, 64]> other = ?        | Done     | Done       | 0.9999979981259051 | 0      |
| 458 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1e-06                         | Done     | Unknown    | N/A                | N/A    |
| 459 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 1]> other = ?                 | Done     | Unknown    | N/A                | N/A    |
| 460 | Tensor<[16384, 2, 2]> self = ?,<br>Tensor<[1, 2, 2]> other = ?               | Done     | Unknown    | N/A                | N/A    |
| 461 | Tensor<[16384, 2]> self = ?,<br>Tensor<[16384, 1]> other = ?                 | Done     | Unknown    | N/A                | N/A    |
| 462 | Tensor<[16384, 3, 25]> self = ?,<br>Tensor<[16384, 3, 25]> other = ?         | Done     | Unknown    | N/A                | N/A    |
| 463 | Tensor<[16384, 3, 3]> self = ?,<br>Tensor<[16384, 3, 3]> other = ?           | Done     | Unknown    | N/A                | N/A    |
| 464 | Tensor<[16384, 3]> self = ?,<br>Tensor other = 0.5                           | Done     | Unknown    | N/A                | N/A    |
| 465 | Tensor<[16384, 3]> self = ?,<br>Tensor<[1, 3]> other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 466 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 3]> other = ?                 | Done     | Unknown    | N/A                | N/A    |
| 467 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 4]> other = ?                 | Done     | Unknown    | N/A                | N/A    |
| 468 | Tensor<[16384]> self = ?,<br>Tensor other = 1                                | Done     | Unknown    | N/A                | N/A    |
| 469 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?                       | Done     | Unknown    | N/A                | N/A    |
| 470 | Tensor<[16]> self = ?,<br>Tensor other = 1                                   | Done     | Unknown    | N/A                | N/A    |
| 471 | Tensor<[16]> self = ?,<br>Tensor other = 1.0                                 | Done     | Unknown    | N/A                | N/A    |
| 472 | Tensor<[16]> self = ?,<br>Tensor other = 2                                   | Done     | Unknown    | N/A                | N/A    |
| 473 | Tensor<[1]> self = ?,<br>Tensor other = 1                                    | Unknown  | Unknown    | N/A                | N/A    |
| 474 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 475 | Tensor<[2, 16, 1]> self = ?,<br>Tensor other = -6.0                          | Done     | Unknown    | N/A                | N/A    |
| 476 | Tensor<[2, 16, 1]> self = ?,<br>Tensor other = 1                             | Done     | Unknown    | N/A                | N/A    |
| 477 | Tensor<[2, 16]> self = ?,<br>Tensor other = -6.0                             | Done     | Unknown    | N/A                | N/A    |
| 478 | Tensor<[2, 16]> self = ?,<br>Tensor other = 1                                | Done     | Unknown    | N/A                | N/A    |
| 479 | Tensor<[2, 32, 1]> self = ?,<br>Tensor other = -6.0                          | Done     | Unknown    | N/A                | N/A    |
| 480 | Tensor<[2, 32, 1]> self = ?,<br>Tensor other = 1                             | Done     | Unknown    | N/A                | N/A    |
| 481 | Tensor<[2, 42]> self = ?,<br>Tensor other = -6.0                             | Done     | Unknown    | N/A                | N/A    |
| 482 | Tensor<[2, 42]> self = ?,<br>Tensor other = 1                                | Done     | Unknown    | N/A                | N/A    |
| 483 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                     | Done     | Done       | 0.9999980735903939 | 0      |
| 484 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?             | Done     | Done       | 0.9999980860029762 | 0      |
| 485 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?               | Done     | Done       | 0.9999978646673556 | 0      |
| 486 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?               | Done     | Done       | 0.9999981452836538 | 0      |
| 487 | Tensor<[2048, 262]> self = ?,<br>Tensor<[262]> other = ?                     | Removed  | Done       | 0.9999979323440211 | 0      |
| 488 | Tensor<[24, 24]> self = ?,<br>Tensor other = 160                             | Unknown  | Done       | 0.9806223398049291 | 0      |
| 489 | Tensor<[32, 1]> self = ?,<br>Tensor other = 1                                | Done     | Unknown    | N/A                | N/A    |
| 490 | Tensor<[32, 1]> self = ?,<br>Tensor other = 1.0                              | Done     | Unknown    | N/A                | N/A    |
| 491 | Tensor<[32, 1]> self = ?,<br>Tensor other = 2                                | Done     | Unknown    | N/A                | N/A    |
| 492 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 493 | Tensor<[3234, 2]> self = ?,<br>Tensor<[3234, 2]> other = ?                   | Done     | Done       | 0.9999980987330724 | 0      |
| 494 | Tensor<[3234]> self = ?,<br>Tensor<[3234]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
| 495 | Tensor<[4, 1024, 14, 14]> self = ?,<br>Tensor<[4, 1024, 14, 14]> other = ?   | Done     | Unknown    | N/A                | N/A    |
| 496 | Tensor<[4, 12, 49, 49]> self = ?,<br>Tensor<[1, 12, 49, 49]> other = ?       | Done     | Done       | 0.9999980566152108 | 0      |
| 497 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[1, 12, 64, 64]> other = ?       | Done     | Done       | 0.9999979798133609 | 0      |
| 498 | Tensor<[4, 16, 49, 49]> self = ?,<br>Tensor<[1, 16, 49, 49]> other = ?       | Done     | Done       | 0.9999980228227158 | 0      |
| 499 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[1, 16, 64, 64]> other = ?       | Done     | Done       | 0.9999979983387708 | 0      |
| 500 | Tensor<[4, 2048, 7, 7]> self = ?,<br>Tensor<[4, 2048, 7, 7]> other = ?       | Done     | Unknown    | N/A                | N/A    |
| 501 | Tensor<[4, 256, 56, 56]> self = ?,<br>Tensor<[4, 256, 56, 56]> other = ?     | Done     | Unknown    | N/A                | N/A    |
| 502 | Tensor<[4, 512, 28, 28]> self = ?,<br>Tensor<[4, 512, 28, 28]> other = ?     | Done     | Unknown    | N/A                | N/A    |
| 503 | Tensor<[42]> self = ?,<br>Tensor other = 1                                   | Done     | Unknown    | N/A                | N/A    |
| 504 | Tensor<[42]> self = ?,<br>Tensor other = 1.0                                 | Done     | Unknown    | N/A                | N/A    |
| 505 | Tensor<[42]> self = ?,<br>Tensor other = 2                                   | Done     | Unknown    | N/A                | N/A    |
| 506 | Tensor<[59, 1024]> self = ?,<br>Tensor<[59, 1024]> other = ?                 | Unknown  | Done       | 0.9999980640608037 | 0      |
| 507 | Tensor<[64, 3, 49, 49]> self = ?,<br>Tensor<[1, 3, 49, 49]> other = ?        | Done     | Done       | 0.9999980155305082 | 0      |
| 508 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[1, 3, 64, 64]> other = ?        | Done     | Done       | 0.9999979903631796 | 0      |
| 509 | Tensor<[64, 4, 49, 49]> self = ?,<br>Tensor<[1, 4, 49, 49]> other = ?        | Done     | Done       | 0.9999980164082968 | 0      |
| 510 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[1, 4, 64, 64]> other = ?        | Done     | Done       | 0.9999979982449317 | 0      |
| 511 | Tensor<[8, 384, 1024]> self = ?,<br>Tensor<[1, 384, 1024]> other = ?         | Done     | Unknown    | N/A                | N/A    |
| 512 | Tensor<[8, 384, 1024]> self = ?,<br>Tensor<[8, 384, 1024]> other = ?         | Done     | Unknown    | N/A                | N/A    |
| 513 | Tensor<[822, 4]> self = ?,<br>Tensor<[822, 1]> other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 514 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
| 515 | Tensor<[8732, 2]> self = ?,<br>Tensor<[8732, 2]> other = ?                   | Done     | Done       | 0.9999979812334001 | 0      |
| 516 | Tensor<[8732]> self = ?,<br>Tensor<[8732]> other = ?                         | Done     | Unknown    | N/A                | N/A    |
| 517 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[256]> other = ?                   | Done     | Done       | 0.999998053758786  | 0      |
| 518 | Tensor<[920, 1, 256]> self = ?,<br>Tensor<[920, 1, 256]> other = ?           | Done     | Done       | 0.9999979689119934 | 0      |
| 519 | Tensor<[]> self = ?,<br>Tensor other = 30.0                                  | Unknown  | Unknown    | N/A                | N/A    |
| 520 | Tensor<[]> self = ?,<br>Tensor other = ?                                     | Done     | Unknown    | N/A                | N/A    |
| 521 | Tensor<[s0 + 1]> self = ?,<br>Tensor other = 0                               | Unknown  | Unknown    | N/A                | N/A    |

