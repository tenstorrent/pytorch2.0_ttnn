### aten.bmm.default
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ?       | Done     | Done       | 0.999975192433454  | 0      |
|   1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?        | Done     | Done       | 0.9999894657299474 | 0      |
|   2 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ?       | Done     | Done       | 0.9999761823636505 | 0      |
|   3 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?        | Done     | Done       | 0.9999864336577772 | 0      |
|   4 | Tensor<[1, 256, 16384]> self = ?,<br>Tensor<[1, 16384, 32]> mat2 = ?     | Done     | Done       | 0.9998105207639524 | 0      |
|   5 | Tensor<[1, 32, 16384]> self = ?,<br>Tensor<[1, 16384, 256]> mat2 = ?     | Done     | Done       | 0.9997974107490945 | 0      |
|   6 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ?              | Done     | Done       | 0.9999928968168139 | 0      |
|   7 | Tensor<[12, 1, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?           | Unknown  | Done       | 0.9999925456607062 | 0      |
|   8 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  | Done       | 0.9999927406973116 | 0      |
|   9 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  | Done       | 0.9999935271372492 | 0      |
|  10 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  | Done       | 0.9999863827322327 | 0      |
|  11 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?           | Unknown  | Done       | 0.9999859229023169 | 0      |
|  12 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  | Done       | 0.9999889114108748 | 0      |
|  13 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  | Done       | 0.9999918391177673 | 0      |
|  14 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  | Done       | 0.9999859607499926 | 0      |
|  15 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  16 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  17 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  18 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  19 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?          | Done     | Done       | 0.9999915959491168 | 0      |
|  20 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?          | Done     | Done       | 0.9999868030251118 | 0      |
|  21 | Tensor<[12, 12, 12]> self = ?,<br>Tensor<[12, 12, 64]> mat2 = ?          | Done     | Done       | 0.9999916545979889 | 0      |
|  22 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?          | Done     | Done       | 0.9999874717676211 | 0      |
|  23 | Tensor<[12, 14, 14]> self = ?,<br>Tensor<[12, 14, 64]> mat2 = ?          | Done     | Done       | 0.9999915798621121 | 0      |
|  24 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ?          | Done     | Done       | 0.9999865436558142 | 0      |
|  25 | Tensor<[12, 16, 16]> self = ?,<br>Tensor<[12, 16, 64]> mat2 = ?          | Done     | Done       | 0.9999912716120577 | 0      |
|  26 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?          | Done     | Done       | 0.9999858506357059 | 0      |
|  27 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ?       | Done     | Done       | 0.9999820757257989 | 0      |
|  28 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?        | Done     | Done       | 0.9999864322200953 | 0      |
|  29 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Done     | Done       | 0.9999895046872574 | 0      |
|  30 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Done     | Done       | 0.9999863358212642 | 0      |
|  31 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ?          | Done     | Done       | 0.999989186433961  | 0      |
|  32 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ?          | Done     | Done       | 0.9999866941999862 | 0      |
|  33 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  | Done       | 0.9999879126950555 | 0      |
|  34 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  | Done       | 0.9999863977800686 | 0      |
|  35 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ?          | Done     | Done       | 0.9999860047275761 | 0      |
|  36 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ?          | Done     | Done       | 0.999986292306712  | 0      |
|  37 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ?       | Done     | Done       | 0.9999820203790222 | 0      |
|  38 | Tensor<[12, 64, 50]> self = ?,<br>Tensor<[12, 50, 50]> mat2 = ?          | Unknown  | Done       | 0.9999860856476964 | 0      |
|  39 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?            | Done     | Done       | 0.9999852515144317 | 0      |
|  40 | Tensor<[12, 7, 7]> self = ?,<br>Tensor<[12, 7, 64]> mat2 = ?             | Done     | Done       | 0.9999914011937    | 0      |
|  41 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999863192444303 | 0      |
|  42 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?             | Done     | Done       | 0.999991390901058  | 0      |
|  43 | Tensor<[128, 49, 32]> self = ?,<br>Tensor<[128, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999894797717932 | 0      |
|  44 | Tensor<[128, 49, 49]> self = ?,<br>Tensor<[128, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999861844010888 | 0      |
|  45 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999894427370354 | 0      |
|  46 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ?        | Done     | Done       | 0.999986449320223  | 0      |
|  47 | Tensor<[16, 1, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?           | Unknown  | Done       | 0.9999914887913843 | 0      |
|  48 | Tensor<[16, 1, 1]> self = ?,<br>Tensor<[16, 1, 64]> mat2 = ?             | Unknown  | Done       | 0.9999926603753367 | 0      |
|  49 | Tensor<[16, 1, 2]> self = ?,<br>Tensor<[16, 2, 64]> mat2 = ?             | Unknown  | Done       | 0.9999936403322444 | 0      |
|  50 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | Done       | 0.9999863138981621 | 0      |
|  51 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?           | Unknown  | Done       | 0.9999889410226743 | 0      |
|  52 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> mat2 = ?            | Unknown  | Done       | 0.9999808294841097 | 0      |
|  53 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 2]> mat2 = ?            | Unknown  | Done       | 0.9999901303528406 | 0      |
|  54 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | Done       | 0.9999865165502523 | 0      |
|  55 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 6]> mat2 = ?            | Unknown  | Done       | 0.9999818863014931 | 0      |
|  56 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  57 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  58 | Tensor<[16, 1, 6]> self = ?,<br>Tensor<[16, 6, 64]> mat2 = ?             | Unknown  | Done       | 0.9999915899091992 | 0      |
|  59 | Tensor<[16, 1, s0 + 1]> self = ?,<br>Tensor<[16, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  60 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  61 | Tensor<[16, 10, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?          | Unknown  | Done       | 0.999991550901239  | 0      |
|  62 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?          | Unknown  | Done       | 0.9999862526608944 | 0      |
|  63 | Tensor<[16, 19, 19]> self = ?,<br>Tensor<[16, 19, 64]> mat2 = ?          | Done     | Done       | 0.9999891299231505 | 0      |
|  64 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ?          | Done     | Done       | 0.9999858909791198 | 0      |
|  65 | Tensor<[16, 197, 197]> self = ?,<br>Tensor<[16, 197, 64]> mat2 = ?       | Done     | Done       | 0.9999820738517318 | 0      |
|  66 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ?        | Done     | Done       | 0.9999864414847206 | 0      |
|  67 | Tensor<[16, 256, 256]> self = ?,<br>Tensor<[16, 256, 64]> mat2 = ?       | Done     | Done       | 0.9999793530862569 | 0      |
|  68 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ?        | Done     | Done       | 0.9999864059497263 | 0      |
|  69 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?          | Unknown  | Done       | 0.9999896794356353 | 0      |
|  70 | Tensor<[16, 5, 5]> self = ?,<br>Tensor<[16, 5, 64]> mat2 = ?             | Unknown  | Done       | 0.9999911859022433 | 0      |
|  71 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?            | Unknown  | Done       | 0.9999865123116753 | 0      |
|  72 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Unknown  | Done       | 0.9999862941253423 | 0      |
|  73 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Unknown  | Done       | 0.9999864128162373 | 0      |
|  74 | Tensor<[16, 64, 197]> self = ?,<br>Tensor<[16, 197, 197]> mat2 = ?       | Done     | Done       | 0.9999820261418789 | 0      |
|  75 | Tensor<[16, 64, 7]> self = ?,<br>Tensor<[16, 7, 7]> mat2 = ?             | Unknown  | Done       | 0.9999914380347821 | 0      |
|  76 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?            | Done     | Done       | 0.9999854484582681 | 0      |
|  77 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?             | Done     | Done       | 0.99999136541474   | 0      |
|  78 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?          | Done     | Done       | 0.9999787827468319 | 0      |
|  79 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999856644202826 | 0      |
|  80 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 128]> mat2 = ?            | Done     | Done       | 0.9999914390901519 | 0      |
|  81 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?             | Done     | Done       | 0.9999917427646794 | 0      |
|  82 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ?        | Done     | Done       | 0.999989460348068  | 0      |
|  83 | Tensor<[192, 49, 49]> self = ?,<br>Tensor<[192, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999861845353738 | 0      |
|  84 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999894694245213 | 0      |
|  85 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999864462562024 | 0      |
|  86 | Tensor<[2, 256, 4096]> self = ?,<br>Tensor<[2, 4096, 32]> mat2 = ?       | Done     | Done       | 0.9999345598286432 | 0      |
|  87 | Tensor<[2, 32, 4096]> self = ?,<br>Tensor<[2, 4096, 256]> mat2 = ?       | Done     | Done       | 0.9999329510335029 | 0      |
|  88 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?        | Done     | Done       | 0.9999753691751043 | 0      |
|  89 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894655862046 | 0      |
|  90 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?        | Done     | Done       | 0.9999760875663657 | 0      |
|  91 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?         | Done     | Done       | 0.9999864370089109 | 0      |
|  92 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Done     | Done       | 0.9999861855128293 | 0      |
|  93 | Tensor<[24, 49, 32]> self = ?,<br>Tensor<[24, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895623342064 | 0      |
|  94 | Tensor<[24, 49, 49]> self = ?,<br>Tensor<[24, 49, 32]> mat2 = ?          | Done     | Done       | 0.999986463706385  | 0      |
|  95 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894006844513 | 0      |
|  96 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?          | Done     | Done       | 0.999986435854571  | 0      |
|  97 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999895013748097 | 0      |
|  98 | Tensor<[256, 49, 49]> self = ?,<br>Tensor<[256, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999863143961761 | 0      |
|  99 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999894560585018 | 0      |
| 100 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999864093335787 | 0      |
| 101 | Tensor<[3, 1445, 1445]> self = ?,<br>Tensor<[3, 1445, 64]> mat2 = ?      | Done     | Done       | 0.9999634242026816 | 0      |
| 102 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ?        | Done     | Done       | 0.9999863897052087 | 0      |
| 103 | Tensor<[32, 49, 32]> self = ?,<br>Tensor<[32, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999893945916316 | 0      |
| 104 | Tensor<[32, 49, 49]> self = ?,<br>Tensor<[32, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862223080955 | 0      |
| 105 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999895682521516 | 0      |
| 106 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999864744880262 | 0      |
| 107 | Tensor<[48, 49, 32]> self = ?,<br>Tensor<[48, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895315524052 | 0      |
| 108 | Tensor<[48, 49, 49]> self = ?,<br>Tensor<[48, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999861709145129 | 0      |
| 109 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894384514041 | 0      |
| 110 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999863313947205 | 0      |
| 111 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?        | Done     | Done       | 0.9999753359128651 | 0      |
| 112 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894941112245 | 0      |
| 113 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?        | Done     | Done       | 0.9999761344967725 | 0      |
| 114 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?         | Done     | Done       | 0.9999864046130659 | 0      |
| 115 | Tensor<[5, 256, 1024]> self = ?,<br>Tensor<[5, 1024, 32]> mat2 = ?       | Done     | Done       | 0.9999657317882927 | 0      |
| 116 | Tensor<[5, 32, 1024]> self = ?,<br>Tensor<[5, 1024, 256]> mat2 = ?       | Done     | Done       | 0.99996611595487   | 0      |
| 117 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?             | Unknown  | Done       | 0.9999920672758035 | 0      |
| 118 | Tensor<[6, 1, 17]> self = ?,<br>Tensor<[6, 17, 64]> mat2 = ?             | Unknown  | Done       | 0.9999890238774715 | 0      |
| 119 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?               | Unknown  | Done       | 0.9999892832846463 | 0      |
| 120 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?               | Unknown  | Done       | 0.9999934316213883 | 0      |
| 121 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?             | Unknown  | Done       | 0.9999898332833582 | 0      |
| 122 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 17]> mat2 = ?             | Unknown  | Done       | 0.9999865206754108 | 0      |
| 123 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?              | Unknown  | Done       | 0.9999955012123231 | 0      |
| 124 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?              | Unknown  | Done       | 0.9999803809859148 | 0      |
| 125 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 126 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 127 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?            | Unknown  | Done       | 0.9999920043507706 | 0      |
| 128 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?            | Unknown  | Done       | 0.9999857898050521 | 0      |
| 129 | Tensor<[64, 49, 32]> self = ?,<br>Tensor<[64, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895840477271 | 0      |
| 130 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999861956029744 | 0      |
| 131 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999895410475256 | 0      |
| 132 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999864506445199 | 0      |
| 133 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999862178739023 | 0      |
| 134 | Tensor<[64, 9, 9]> self = ?,<br>Tensor<[64, 9, 64]> mat2 = ?             | Done     | Done       | 0.9999914380154857 | 0      |
| 135 | Tensor<[8, 1, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?             | Unknown  | Done       | 0.9999921802753607 | 0      |
| 136 | Tensor<[8, 1, 1]> self = ?,<br>Tensor<[8, 1, 64]> mat2 = ?               | Unknown  | Done       | 0.9999932866181874 | 0      |
| 137 | Tensor<[8, 1, 2]> self = ?,<br>Tensor<[8, 2, 64]> mat2 = ?               | Unknown  | Done       | 0.9999924038159848 | 0      |
| 138 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?             | Unknown  | Done       | 0.9999867869107399 | 0      |
| 139 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 1]> mat2 = ?              | Unknown  | Done       | 0.9999910616161197 | 0      |
| 140 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 2]> mat2 = ?              | Unknown  | Done       | 0.9999815625240845 | 0      |
| 141 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 142 | Tensor<[8, 1, s0 + 1]> self = ?,<br>Tensor<[8, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 143 | Tensor<[8, 10, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?            | Unknown  | Done       | 0.9999916743794097 | 0      |
| 144 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?            | Unknown  | Done       | 0.9999872368507066 | 0      |
| 145 | Tensor<[8, 100, 100]> self = ?,<br>Tensor<[8, 100, 32]> mat2 = ?         | Unknown  | Done       | 0.9999808927135964 | 0      |
| 146 | Tensor<[8, 100, 32]> self = ?,<br>Tensor<[8, 32, 100]> mat2 = ?          | Unknown  | Done       | 0.9999894979735771 | 0      |
| 147 | Tensor<[8, 100, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Unknown  | Done       | 0.9999643751663411 | 0      |
| 148 | Tensor<[8, 2048, 256]> self = ?,<br>Tensor<[8, 256, 96]> mat2 = ?        | Done     | Done       | 0.9999753491025942 | 0      |
| 149 | Tensor<[8, 2048, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894726748507 | 0      |
| 150 | Tensor<[8, 256, 2048]> self = ?,<br>Tensor<[8, 2048, 160]> mat2 = ?      | Done     | Done       | 0.999921412234284  | 0      |
| 151 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 160]> mat2 = ?        | Done     | Done       | 0.9999791550188193 | 0      |
| 152 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?         | Done     | Done       | 0.9999756044811334 | 0      |
| 153 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?         | Done     | Done       | 0.9999895172935671 | 0      |
| 154 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?          | Done     | Done       | 0.9999894465254979 | 0      |
| 155 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?         | Done     | Done       | 0.9999796783470364 | 0      |
| 156 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?          | Done     | Done       | 0.9999864319399983 | 0      |
| 157 | Tensor<[8, 32, 256]> self = ?,<br>Tensor<[8, 256, 256]> mat2 = ?         | Done     | Done       | 0.9999752716531899 | 0      |
| 158 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Unknown  | Done       | 0.9999642764047346 | 0      |
| 159 | Tensor<[96, 49, 32]> self = ?,<br>Tensor<[96, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895822120057 | 0      |
| 160 | Tensor<[96, 49, 49]> self = ?,<br>Tensor<[96, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999861702538525 | 0      |
| 161 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999895196004018 | 0      |
| 162 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999864239025675 | 0      |

