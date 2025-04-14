### aten.bmm.default
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ?       | Done     | Done       | 0.999975478066486  | 0      |
|   1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?        | Done     | Done       | 0.9999894956149029 | 0      |
|   2 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ?       | Done     | Done       | 0.9999761597361836 | 0      |
|   3 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?        | Done     | Done       | 0.9999864234110167 | 0      |
|   4 | Tensor<[1, 256, 16384]> self = ?,<br>Tensor<[1, 16384, 32]> mat2 = ?     | Done     | Done       | 0.9998103696361321 | 0      |
|   5 | Tensor<[1, 32, 16384]> self = ?,<br>Tensor<[1, 16384, 256]> mat2 = ?     | Done     | Done       | 0.9998119622987677 | 0      |
|   6 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ?              | Done     | Done       | 0.9999924104887573 | 0      |
|   7 | Tensor<[12, 1, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?           | Unknown  | Done       | 0.9999910651888813 | 0      |
|   8 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  | Done       | 0.9999914728286062 | 0      |
|   9 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  | Done       | 0.9999954299293425 | 0      |
|  10 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  | Done       | 0.9999889011185824 | 0      |
|  11 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?           | Unknown  | Done       | 0.9999864065866647 | 0      |
|  12 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  | Done       | 0.9999897472451993 | 0      |
|  13 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  | Done       | 0.9999957786589216 | 0      |
|  14 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  | Done       | 0.9999868374648078 | 0      |
|  15 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  16 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  17 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  18 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  19 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?          | Done     | Done       | 0.999991763175161  | 0      |
|  20 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?          | Done     | Done       | 0.9999867745440723 | 0      |
|  21 | Tensor<[12, 12, 12]> self = ?,<br>Tensor<[12, 12, 64]> mat2 = ?          | Done     | Done       | 0.9999912119397946 | 0      |
|  22 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?          | Done     | Done       | 0.9999862514142149 | 0      |
|  23 | Tensor<[12, 14, 14]> self = ?,<br>Tensor<[12, 14, 64]> mat2 = ?          | Done     | Done       | 0.9999918318754689 | 0      |
|  24 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ?          | Done     | Done       | 0.9999864345556766 | 0      |
|  25 | Tensor<[12, 16, 16]> self = ?,<br>Tensor<[12, 16, 64]> mat2 = ?          | Done     | Done       | 0.9999918045046481 | 0      |
|  26 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?          | Done     | Done       | 0.9999862674762205 | 0      |
|  27 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ?       | Done     | Done       | 0.9999821027799508 | 0      |
|  28 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?        | Done     | Done       | 0.9999864823027941 | 0      |
|  29 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Done     | Done       | 0.9999891419314596 | 0      |
|  30 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Done     | Done       | 0.9999862263574024 | 0      |
|  31 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ?          | Done     | Done       | 0.9999891167667299 | 0      |
|  32 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ?          | Done     | Done       | 0.9999863709185621 | 0      |
|  33 | Tensor<[12, 257, 257]> self = ?,<br>Tensor<[12, 257, 64]> mat2 = ?       | Done     | Unknown    | N/A                | N/A    |
|  34 | Tensor<[12, 257, 64]> self = ?,<br>Tensor<[12, 64, 257]> mat2 = ?        | Done     | Unknown    | N/A                | N/A    |
|  35 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  | Done       | 0.9999880619123936 | 0      |
|  36 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  | Done       | 0.9999868199520703 | 0      |
|  37 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ?          | Done     | Done       | 0.9999860003143493 | 0      |
|  38 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ?          | Done     | Done       | 0.9999865935415017 | 0      |
|  39 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ?       | Done     | Done       | 0.9999821099031171 | 0      |
|  40 | Tensor<[12, 64, 50]> self = ?,<br>Tensor<[12, 50, 50]> mat2 = ?          | Done     | Done       | 0.9999860900288162 | 0      |
|  41 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?            | Done     | Done       | 0.99998750393334   | 0      |
|  42 | Tensor<[12, 7, 7]> self = ?,<br>Tensor<[12, 7, 64]> mat2 = ?             | Done     | Done       | 0.9999920896262003 | 0      |
|  43 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999859755288122 | 0      |
|  44 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?             | Done     | Done       | 0.9999917731577831 | 0      |
|  45 | Tensor<[128, 49, 32]> self = ?,<br>Tensor<[128, 32, 49]> mat2 = ?        | Done     | Done       | 0.999989565300935  | 0      |
|  46 | Tensor<[128, 49, 49]> self = ?,<br>Tensor<[128, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999861698384193 | 0      |
|  47 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999894857257289 | 0      |
|  48 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999864337434771 | 0      |
|  49 | Tensor<[16, 1, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?           | Unknown  | Done       | 0.9999904410646235 | 0      |
|  50 | Tensor<[16, 1, 1]> self = ?,<br>Tensor<[16, 1, 64]> mat2 = ?             | Unknown  | Done       | 0.9999945739032658 | 0      |
|  51 | Tensor<[16, 1, 2]> self = ?,<br>Tensor<[16, 2, 64]> mat2 = ?             | Unknown  | Done       | 0.9999944314274597 | 0      |
|  52 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | Done       | 0.999986710515889  | 0      |
|  53 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?           | Unknown  | Done       | 0.9999857034274753 | 0      |
|  54 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> mat2 = ?            | Unknown  | Done       | 0.9999852611985035 | 0      |
|  55 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 2]> mat2 = ?            | Unknown  | Done       | 0.9999943570973384 | 0      |
|  56 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | Done       | 0.9999870697147665 | 0      |
|  57 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 6]> mat2 = ?            | Unknown  | Done       | 0.999984303201932  | 0      |
|  58 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  59 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  60 | Tensor<[16, 1, 6]> self = ?,<br>Tensor<[16, 6, 64]> mat2 = ?             | Unknown  | Done       | 0.9999922545818537 | 0      |
|  61 | Tensor<[16, 1, s0 + 1]> self = ?,<br>Tensor<[16, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  62 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  63 | Tensor<[16, 10, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?          | Unknown  | Done       | 0.9999912668930794 | 0      |
|  64 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?          | Unknown  | Done       | 0.9999859957670192 | 0      |
|  65 | Tensor<[16, 19, 19]> self = ?,<br>Tensor<[16, 19, 64]> mat2 = ?          | Done     | Done       | 0.9999891316509929 | 0      |
|  66 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ?          | Done     | Done       | 0.9999863279112852 | 0      |
|  67 | Tensor<[16, 256, 256]> self = ?,<br>Tensor<[16, 256, 64]> mat2 = ?       | Done     | Done       | 0.9999792910918254 | 0      |
|  68 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ?        | Done     | Done       | 0.9999864634523747 | 0      |
|  69 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?          | Unknown  | Done       | 0.9999892190629348 | 0      |
|  70 | Tensor<[16, 5, 5]> self = ?,<br>Tensor<[16, 5, 64]> mat2 = ?             | Unknown  | Done       | 0.9999911579078049 | 0      |
|  71 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?            | Unknown  | Done       | 0.9999860242786224 | 0      |
|  72 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Unknown  | Done       | 0.9999862516667121 | 0      |
|  73 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Unknown  | Done       | 0.9999863516333889 | 0      |
|  74 | Tensor<[16, 64, 7]> self = ?,<br>Tensor<[16, 7, 7]> mat2 = ?             | Done     | Done       | 0.9999921298083942 | 0      |
|  75 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?            | Done     | Done       | 0.9999859310627326 | 0      |
|  76 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?             | Done     | Done       | 0.9999917152855661 | 0      |
|  77 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?          | Done     | Done       | 0.9999794520460712 | 0      |
|  78 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999870150590441 | 0      |
|  79 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 128]> mat2 = ?            | Done     | Done       | 0.9999913070472582 | 0      |
|  80 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?             | Done     | Done       | 0.9999915711627045 | 0      |
|  81 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999895067769113 | 0      |
|  82 | Tensor<[192, 49, 49]> self = ?,<br>Tensor<[192, 49, 32]> mat2 = ?        | Done     | Done       | 0.999986280299447  | 0      |
|  83 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ?        | Done     | Done       | 0.999989447526865  | 0      |
|  84 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999863639521374 | 0      |
|  85 | Tensor<[2, 256, 4096]> self = ?,<br>Tensor<[2, 4096, 32]> mat2 = ?       | Done     | Done       | 0.999933159952009  | 0      |
|  86 | Tensor<[2, 32, 4096]> self = ?,<br>Tensor<[2, 4096, 256]> mat2 = ?       | Done     | Done       | 0.999934211566644  | 0      |
|  87 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?        | Done     | Done       | 0.9999755424115007 | 0      |
|  88 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894598118562 | 0      |
|  89 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?        | Done     | Done       | 0.9999761052411196 | 0      |
|  90 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?         | Done     | Done       | 0.9999864452255566 | 0      |
|  91 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Done     | Done       | 0.9999861729020163 | 0      |
|  92 | Tensor<[24, 49, 32]> self = ?,<br>Tensor<[24, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895666024543 | 0      |
|  93 | Tensor<[24, 49, 49]> self = ?,<br>Tensor<[24, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862887003402 | 0      |
|  94 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894519827992 | 0      |
|  95 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999864485219807 | 0      |
|  96 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999895236379668 | 0      |
|  97 | Tensor<[256, 49, 49]> self = ?,<br>Tensor<[256, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999861941571333 | 0      |
|  98 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999894911052968 | 0      |
|  99 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999863986762499 | 0      |
| 100 | Tensor<[3, 1445, 1445]> self = ?,<br>Tensor<[3, 1445, 64]> mat2 = ?      | Done     | Done       | 0.9999633126892541 | 0      |
| 101 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ?        | Done     | Done       | 0.9999864030698773 | 0      |
| 102 | Tensor<[32, 49, 32]> self = ?,<br>Tensor<[32, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895493756938 | 0      |
| 103 | Tensor<[32, 49, 49]> self = ?,<br>Tensor<[32, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862769167456 | 0      |
| 104 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999895100881067 | 0      |
| 105 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999863068675803 | 0      |
| 106 | Tensor<[48, 49, 32]> self = ?,<br>Tensor<[48, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999894689203568 | 0      |
| 107 | Tensor<[48, 49, 49]> self = ?,<br>Tensor<[48, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862423102427 | 0      |
| 108 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999895074855779 | 0      |
| 109 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999863014628715 | 0      |
| 110 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?        | Done     | Done       | 0.9999752356155421 | 0      |
| 111 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894604426969 | 0      |
| 112 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?        | Done     | Done       | 0.9999761468562637 | 0      |
| 113 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?         | Done     | Done       | 0.9999864266430382 | 0      |
| 114 | Tensor<[5, 256, 1024]> self = ?,<br>Tensor<[5, 1024, 32]> mat2 = ?       | Done     | Done       | 0.9999652820296875 | 0      |
| 115 | Tensor<[5, 32, 1024]> self = ?,<br>Tensor<[5, 1024, 256]> mat2 = ?       | Done     | Done       | 0.9999651972680829 | 0      |
| 116 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?             | Unknown  | Done       | 0.999991781613259  | 0      |
| 117 | Tensor<[6, 1, 17]> self = ?,<br>Tensor<[6, 17, 64]> mat2 = ?             | Unknown  | Done       | 0.999988901177279  | 0      |
| 118 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?               | Unknown  | Done       | 0.9999937307419553 | 0      |
| 119 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?               | Unknown  | Done       | 0.9999922724375087 | 0      |
| 120 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?             | Unknown  | Done       | 0.9999900604924276 | 0      |
| 121 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 17]> mat2 = ?             | Unknown  | Done       | 0.9999870907992963 | 0      |
| 122 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?              | Unknown  | Done       | 0.999991932149198  | 0      |
| 123 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?              | Unknown  | Done       | 0.9999921118424303 | 0      |
| 124 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 125 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 126 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?            | Unknown  | Done       | 0.99999126906139   | 0      |
| 127 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?            | Unknown  | Done       | 0.9999866535690286 | 0      |
| 128 | Tensor<[64, 49, 32]> self = ?,<br>Tensor<[64, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895107853949 | 0      |
| 129 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862498354597 | 0      |
| 130 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999895346439768 | 0      |
| 131 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999865181342956 | 0      |
| 132 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999869025598626 | 0      |
| 133 | Tensor<[64, 9, 9]> self = ?,<br>Tensor<[64, 9, 64]> mat2 = ?             | Done     | Done       | 0.999991515796829  | 0      |
| 134 | Tensor<[8, 1, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?             | Unknown  | Done       | 0.9999917580564178 | 0      |
| 135 | Tensor<[8, 1, 1]> self = ?,<br>Tensor<[8, 1, 64]> mat2 = ?               | Unknown  | Done       | 0.9999938641896149 | 0      |
| 136 | Tensor<[8, 1, 2]> self = ?,<br>Tensor<[8, 2, 64]> mat2 = ?               | Unknown  | Done       | 0.9999900090466715 | 0      |
| 137 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?             | Unknown  | Done       | 0.9999860525229025 | 0      |
| 138 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 1]> mat2 = ?              | Unknown  | Done       | 0.9999793835192332 | 0      |
| 139 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 2]> mat2 = ?              | Unknown  | Done       | 0.9999934467277498 | 0      |
| 140 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 141 | Tensor<[8, 1, s0 + 1]> self = ?,<br>Tensor<[8, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 142 | Tensor<[8, 10, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?            | Unknown  | Done       | 0.9999917715392928 | 0      |
| 143 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?            | Unknown  | Done       | 0.9999862574201799 | 0      |
| 144 | Tensor<[8, 100, 100]> self = ?,<br>Tensor<[8, 100, 32]> mat2 = ?         | Unknown  | Done       | 0.9999811960349879 | 0      |
| 145 | Tensor<[8, 100, 32]> self = ?,<br>Tensor<[8, 32, 100]> mat2 = ?          | Unknown  | Done       | 0.9999893973485624 | 0      |
| 146 | Tensor<[8, 100, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Unknown  | Done       | 0.9999640136852586 | 0      |
| 147 | Tensor<[8, 2048, 256]> self = ?,<br>Tensor<[8, 256, 96]> mat2 = ?        | Done     | Done       | 0.9999753509217838 | 0      |
| 148 | Tensor<[8, 2048, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?         | Done     | Done       | 0.99998947953141   | 0      |
| 149 | Tensor<[8, 256, 2048]> self = ?,<br>Tensor<[8, 2048, 160]> mat2 = ?      | Done     | Done       | 0.9999211055157846 | 0      |
| 150 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 160]> mat2 = ?        | Done     | Done       | 0.9999791865897676 | 0      |
| 151 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?         | Done     | Done       | 0.9999754921491336 | 0      |
| 152 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?         | Done     | Done       | 0.9999895089158367 | 0      |
| 153 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?          | Done     | Done       | 0.9999895101610423 | 0      |
| 154 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?         | Done     | Done       | 0.9999797259692152 | 0      |
| 155 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?          | Done     | Done       | 0.9999864566019641 | 0      |
| 156 | Tensor<[8, 32, 256]> self = ?,<br>Tensor<[8, 256, 256]> mat2 = ?         | Done     | Done       | 0.999975391635454  | 0      |
| 157 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Unknown  | Done       | 0.9999645446366832 | 0      |
| 158 | Tensor<[96, 49, 32]> self = ?,<br>Tensor<[96, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999894308456331 | 0      |
| 159 | Tensor<[96, 49, 49]> self = ?,<br>Tensor<[96, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862268526669 | 0      |
| 160 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894624709312 | 0      |
| 161 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999863244901495 | 0      |

