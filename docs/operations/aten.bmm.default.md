### aten.bmm.default
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ?       | Done     | Done       | 0.9999753719981601 | 0      |
|   1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?        | Done     | Done       | 0.9999894449669428 | 0      |
|   2 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ?       | Done     | Done       | 0.9999760973965289 | 0      |
|   3 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?        | Done     | Done       | 0.9999863634573315 | 0      |
|   4 | Tensor<[1, 256, 16384]> self = ?,<br>Tensor<[1, 16384, 32]> mat2 = ?     | Done     | Done       | 0.9998090557122363 | 0      |
|   5 | Tensor<[1, 32, 16384]> self = ?,<br>Tensor<[1, 16384, 256]> mat2 = ?     | Done     | Done       | 0.9998089444802388 | 0      |
|   6 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ?              | Done     | Done       | 0.9999937889095419 | 0      |
|   7 | Tensor<[12, 1, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?           | Unknown  | Done       | 0.9999899573483569 | 0      |
|   8 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  | Done       | 0.9999912775061477 | 0      |
|   9 | Tensor<[12, 1, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?           | Unknown  | Unknown    | N/A                | N/A    |
|  10 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  | Done       | 0.9999945364363826 | 0      |
|  11 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  | Done       | 0.9999879017065886 | 0      |
|  12 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?           | Unknown  | Done       | 0.9999847778360892 | 0      |
|  13 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  | Done       | 0.9999782366562558 | 0      |
|  14 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?           | Unknown  | Unknown    | N/A                | N/A    |
|  15 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  | Done       | 0.9999946444584565 | 0      |
|  16 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  | Done       | 0.9999851252904679 | 0      |
|  17 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  18 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  19 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s2 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  20 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s4 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  21 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s6 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  22 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s8 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  23 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  24 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  25 | Tensor<[12, 1, s2 + 1]> self = ?,<br>Tensor<[12, s2 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  26 | Tensor<[12, 1, s4 + 1]> self = ?,<br>Tensor<[12, s4 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  27 | Tensor<[12, 1, s6 + 1]> self = ?,<br>Tensor<[12, s6 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  28 | Tensor<[12, 1, s8 + 1]> self = ?,<br>Tensor<[12, s8 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  29 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?          | Removed  | Done       | 0.9999914266062119 | 0      |
|  30 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?          | Removed  | Done       | 0.9999868867672467 | 0      |
|  31 | Tensor<[12, 12, 12]> self = ?,<br>Tensor<[12, 12, 64]> mat2 = ?          | Done     | Done       | 0.9999916508217875 | 0      |
|  32 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?          | Done     | Done       | 0.9999873652074336 | 0      |
|  33 | Tensor<[12, 14, 14]> self = ?,<br>Tensor<[12, 14, 64]> mat2 = ?          | Done     | Done       | 0.999991671104596  | 0      |
|  34 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ?          | Done     | Done       | 0.9999861902286139 | 0      |
|  35 | Tensor<[12, 16, 16]> self = ?,<br>Tensor<[12, 16, 64]> mat2 = ?          | Done     | Done       | 0.9999913710999792 | 0      |
|  36 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?          | Done     | Done       | 0.9999855501122591 | 0      |
|  37 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ?       | Done     | Done       | 0.9999822160400731 | 0      |
|  38 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?        | Done     | Done       | 0.9999863729417787 | 0      |
|  39 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Unknown  | Done       | 0.9999891278196453 | 0      |
|  40 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Unknown  | Done       | 0.9999869697410311 | 0      |
|  41 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ?          | Removed  | Done       | 0.9999892704509181 | 0      |
|  42 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ?          | Removed  | Done       | 0.9999867644993442 | 0      |
|  43 | Tensor<[12, 257, 257]> self = ?,<br>Tensor<[12, 257, 64]> mat2 = ?       | Done     | Unknown    | N/A                | N/A    |
|  44 | Tensor<[12, 257, 64]> self = ?,<br>Tensor<[12, 64, 257]> mat2 = ?        | Done     | Unknown    | N/A                | N/A    |
|  45 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  | Done       | 0.9999882253037112 | 0      |
|  46 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  | Done       | 0.9999863757937473 | 0      |
|  47 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ?          | Done     | Done       | 0.9999859212201538 | 0      |
|  48 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ?          | Done     | Done       | 0.9999866367327757 | 0      |
|  49 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ?       | Done     | Done       | 0.9999819794640477 | 0      |
|  50 | Tensor<[12, 64, 50]> self = ?,<br>Tensor<[12, 50, 50]> mat2 = ?          | Done     | Done       | 0.9999858762621449 | 0      |
|  51 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?            | Done     | Done       | 0.9999863719214457 | 0      |
|  52 | Tensor<[12, 7, 7]> self = ?,<br>Tensor<[12, 7, 64]> mat2 = ?             | Done     | Done       | 0.9999913795758996 | 0      |
|  53 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999868734810997 | 0      |
|  54 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?             | Done     | Done       | 0.9999916060985439 | 0      |
|  55 | Tensor<[128, 49, 32]> self = ?,<br>Tensor<[128, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999894641279674 | 0      |
|  56 | Tensor<[128, 49, 49]> self = ?,<br>Tensor<[128, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999863407506265 | 0      |
|  57 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ?        | Done     | Done       | 0.999989447102543  | 0      |
|  58 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999864614301942 | 0      |
|  59 | Tensor<[16, 1, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?           | Unknown  | Done       | 0.999991250511043  | 0      |
|  60 | Tensor<[16, 1, 1]> self = ?,<br>Tensor<[16, 1, 64]> mat2 = ?             | Unknown  | Done       | 0.999995374840356  | 0      |
|  61 | Tensor<[16, 1, 2]> self = ?,<br>Tensor<[16, 2, 64]> mat2 = ?             | Unknown  | Done       | 0.9999914170336747 | 0      |
|  62 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | Done       | 0.9999865973960358 | 0      |
|  63 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?           | Unknown  | Done       | 0.9999876362502564 | 0      |
|  64 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> mat2 = ?            | Unknown  | Done       | 0.9999972006410968 | 0      |
|  65 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 2]> mat2 = ?            | Unknown  | Done       | 0.9999786024564932 | 0      |
|  66 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | Done       | 0.9999870038367277 | 0      |
|  67 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 6]> mat2 = ?            | Unknown  | Done       | 0.9999862840341474 | 0      |
|  68 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  69 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  70 | Tensor<[16, 1, 6]> self = ?,<br>Tensor<[16, 6, 64]> mat2 = ?             | Unknown  | Done       | 0.9999927420893451 | 0      |
|  71 | Tensor<[16, 1, s0 + 1]> self = ?,<br>Tensor<[16, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  72 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  73 | Tensor<[16, 10, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?          | Unknown  | Done       | 0.9999915907562394 | 0      |
|  74 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?          | Unknown  | Done       | 0.9999868139777268 | 0      |
|  75 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?          | Done     | Done       | 0.9999897248686834 | 0      |
|  76 | Tensor<[16, 384, 384]> self = ?,<br>Tensor<[16, 384, 64]> mat2 = ?       | Removed  | Unknown    | N/A                | N/A    |
|  77 | Tensor<[16, 384, 64]> self = ?,<br>Tensor<[16, 64, 384]> mat2 = ?        | Removed  | Unknown    | N/A                | N/A    |
|  78 | Tensor<[16, 5, 5]> self = ?,<br>Tensor<[16, 5, 64]> mat2 = ?             | Unknown  | Done       | 0.9999912153224628 | 0      |
|  79 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?            | Unknown  | Done       | 0.9999870930215058 | 0      |
|  80 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Unknown  | Done       | 0.9999860310423176 | 0      |
|  81 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Unknown  | Done       | 0.9999863132397449 | 0      |
|  82 | Tensor<[16, 64, 7]> self = ?,<br>Tensor<[16, 7, 7]> mat2 = ?             | Done     | Done       | 0.9999916952214182 | 0      |
|  83 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?            | Done     | Done       | 0.9999854770279292 | 0      |
|  84 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?             | Done     | Done       | 0.9999917952906378 | 0      |
|  85 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?          | Done     | Done       | 0.9999800799109029 | 0      |
|  86 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999874885906495 | 0      |
|  87 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 128]> mat2 = ?            | Done     | Done       | 0.9999913317990766 | 0      |
|  88 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?             | Done     | Done       | 0.9999916351348251 | 0      |
|  89 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999894556652038 | 0      |
|  90 | Tensor<[192, 49, 49]> self = ?,<br>Tensor<[192, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999862118233354 | 0      |
|  91 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999895168085784 | 0      |
|  92 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999864369979286 | 0      |
|  93 | Tensor<[2, 256, 4096]> self = ?,<br>Tensor<[2, 4096, 32]> mat2 = ?       | Done     | Done       | 0.9999343020778545 | 0      |
|  94 | Tensor<[2, 32, 4096]> self = ?,<br>Tensor<[2, 4096, 256]> mat2 = ?       | Done     | Done       | 0.9999321819269305 | 0      |
|  95 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?        | Done     | Done       | 0.9999752156253043 | 0      |
|  96 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894634273756 | 0      |
|  97 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?        | Done     | Done       | 0.999976220113588  | 0      |
|  98 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?         | Done     | Done       | 0.9999864145592492 | 0      |
|  99 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Unknown  | Done       | 0.9999864467524674 | 0      |
| 100 | Tensor<[24, 49, 32]> self = ?,<br>Tensor<[24, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895047786461 | 0      |
| 101 | Tensor<[24, 49, 49]> self = ?,<br>Tensor<[24, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999863332969152 | 0      |
| 102 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?          | Done     | Done       | 0.999989443208185  | 0      |
| 103 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999862033160923 | 0      |
| 104 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999894906417852 | 0      |
| 105 | Tensor<[256, 49, 49]> self = ?,<br>Tensor<[256, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999862054564552 | 0      |
| 106 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999894812873146 | 0      |
| 107 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999863221442029 | 0      |
| 108 | Tensor<[3, 1445, 1445]> self = ?,<br>Tensor<[3, 1445, 64]> mat2 = ?      | Done     | Done       | 0.9999631651471566 | 0      |
| 109 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ?        | Done     | Done       | 0.9999864131961147 | 0      |
| 110 | Tensor<[32, 49, 32]> self = ?,<br>Tensor<[32, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999894912142385 | 0      |
| 111 | Tensor<[32, 49, 49]> self = ?,<br>Tensor<[32, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999864231029915 | 0      |
| 112 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999895366488916 | 0      |
| 113 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999865219156068 | 0      |
| 114 | Tensor<[48, 49, 32]> self = ?,<br>Tensor<[48, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895095706923 | 0      |
| 115 | Tensor<[48, 49, 49]> self = ?,<br>Tensor<[48, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999860492556876 | 0      |
| 116 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894364304963 | 0      |
| 117 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999863722691856 | 0      |
| 118 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?        | Done     | Done       | 0.9999754643297109 | 0      |
| 119 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894684038274 | 0      |
| 120 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?        | Done     | Done       | 0.9999761830485008 | 0      |
| 121 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?         | Done     | Done       | 0.9999864594323656 | 0      |
| 122 | Tensor<[5, 256, 1024]> self = ?,<br>Tensor<[5, 1024, 32]> mat2 = ?       | Done     | Done       | 0.999966174513566  | 0      |
| 123 | Tensor<[5, 32, 1024]> self = ?,<br>Tensor<[5, 1024, 256]> mat2 = ?       | Done     | Done       | 0.9999649418494088 | 0      |
| 124 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?             | Unknown  | Done       | 0.9999927430666484 | 0      |
| 125 | Tensor<[6, 1, 17]> self = ?,<br>Tensor<[6, 17, 64]> mat2 = ?             | Unknown  | Done       | 0.9999899571193008 | 0      |
| 126 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?               | Unknown  | Done       | 0.9999910430819399 | 0      |
| 127 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?               | Unknown  | Done       | 0.9999926669061532 | 0      |
| 128 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?             | Unknown  | Done       | 0.9999880071835004 | 0      |
| 129 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 17]> mat2 = ?             | Unknown  | Done       | 0.9999879723638098 | 0      |
| 130 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?              | Unknown  | Done       | 0.9999962999203236 | 0      |
| 131 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?              | Unknown  | Done       | 0.9999853007241113 | 0      |
| 132 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 133 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 134 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?            | Unknown  | Done       | 0.9999914926317339 | 0      |
| 135 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?            | Unknown  | Done       | 0.9999866185451209 | 0      |
| 136 | Tensor<[64, 49, 32]> self = ?,<br>Tensor<[64, 32, 49]> mat2 = ?          | Done     | Done       | 0.999989494087171  | 0      |
| 137 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999863048410517 | 0      |
| 138 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894833522225 | 0      |
| 139 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?          | Done     | Done       | 0.999986428078351  | 0      |
| 140 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999860512968931 | 0      |
| 141 | Tensor<[64, 9, 9]> self = ?,<br>Tensor<[64, 9, 64]> mat2 = ?             | Done     | Done       | 0.9999915492085258 | 0      |
| 142 | Tensor<[8, 1, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?             | Unknown  | Done       | 0.9999919153864384 | 0      |
| 143 | Tensor<[8, 1, 1]> self = ?,<br>Tensor<[8, 1, 64]> mat2 = ?               | Unknown  | Done       | 0.9999953000829032 | 0      |
| 144 | Tensor<[8, 1, 2]> self = ?,<br>Tensor<[8, 2, 64]> mat2 = ?               | Unknown  | Done       | 0.9999933662274442 | 0      |
| 145 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?             | Unknown  | Done       | 0.9999865930067818 | 0      |
| 146 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 1]> mat2 = ?              | Unknown  | Done       | 0.9999972528475695 | 0      |
| 147 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 2]> mat2 = ?              | Unknown  | Done       | 0.9999834315780847 | 0      |
| 148 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 149 | Tensor<[8, 1, s0 + 1]> self = ?,<br>Tensor<[8, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 150 | Tensor<[8, 10, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?            | Unknown  | Done       | 0.9999917446212718 | 0      |
| 151 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?            | Unknown  | Done       | 0.9999860627852745 | 0      |
| 152 | Tensor<[8, 100, 100]> self = ?,<br>Tensor<[8, 100, 32]> mat2 = ?         | Done     | Done       | 0.9999808411101406 | 0      |
| 153 | Tensor<[8, 100, 32]> self = ?,<br>Tensor<[8, 32, 100]> mat2 = ?          | Done     | Done       | 0.9999893567302331 | 0      |
| 154 | Tensor<[8, 100, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Done     | Done       | 0.9999647120860179 | 0      |
| 155 | Tensor<[8, 2048, 256]> self = ?,<br>Tensor<[8, 256, 96]> mat2 = ?        | Done     | Done       | 0.9999753577105208 | 0      |
| 156 | Tensor<[8, 2048, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894840971177 | 0      |
| 157 | Tensor<[8, 256, 2048]> self = ?,<br>Tensor<[8, 2048, 160]> mat2 = ?      | Done     | Done       | 0.999920366910353  | 0      |
| 158 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 160]> mat2 = ?        | Done     | Done       | 0.9999792384759463 | 0      |
| 159 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?         | Done     | Done       | 0.9999754655854153 | 0      |
| 160 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?         | Done     | Done       | 0.9999894722122136 | 0      |
| 161 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?          | Done     | Done       | 0.9999894500899684 | 0      |
| 162 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?         | Done     | Done       | 0.9999796735067381 | 0      |
| 163 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?          | Done     | Done       | 0.9999864115299387 | 0      |
| 164 | Tensor<[8, 32, 256]> self = ?,<br>Tensor<[8, 256, 256]> mat2 = ?         | Done     | Done       | 0.9999751416162569 | 0      |
| 165 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Done     | Done       | 0.999964366324935  | 0      |
| 166 | Tensor<[96, 49, 32]> self = ?,<br>Tensor<[96, 32, 49]> mat2 = ?          | Done     | Done       | 0.999989533874164  | 0      |
| 167 | Tensor<[96, 49, 49]> self = ?,<br>Tensor<[96, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999861360611085 | 0      |
| 168 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894740904085 | 0      |
| 169 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999864744935628 | 0      |

