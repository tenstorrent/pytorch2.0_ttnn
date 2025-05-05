### aten.bmm.default
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ?       | Done     | Done       | 0.9999756471863241 | -1     |
|   1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?        | Done     | Done       | 0.9999894810305012 | -1     |
|   2 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ?       | Unknown  | Done       | 0.9999761390933564 | -1     |
|   3 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?        | Unknown  | Done       | 0.9999864156235224 | -1     |
|   4 | Tensor<[1, 256, 16384]> self = ?,<br>Tensor<[1, 16384, 32]> mat2 = ?     | Done     | Done       | 0.9997951792839173 | -1     |
|   5 | Tensor<[1, 32, 16384]> self = ?,<br>Tensor<[1, 16384, 256]> mat2 = ?     | Done     | Done       | 0.9997998619011937 | -1     |
|   6 | Tensor<[1, 64, 1]> self = ?,<br>Tensor<[1, 1, 32]> mat2 = ?              | Done     | Done       | 0.9999939886554963 | -1     |
|   7 | Tensor<[12, 1, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?           | Unknown  | Done       | 0.9999914821284145 | -1     |
|   8 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  | Done       | 0.9999951980389981 | -1     |
|   9 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  | Done       | 0.9999934700335708 | -1     |
|  10 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  | Done       | 0.9999874333771072 | -1     |
|  11 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?           | Unknown  | Done       | 0.9999843841630305 | -1     |
|  12 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  | Done       | 0.9999843510864285 | -1     |
|  13 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  | Done       | 0.9999942324745282 | -1     |
|  14 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  | Done       | 0.9999872798727882 | -1     |
|  15 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  16 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  17 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  18 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  19 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?          | Done     | Done       | 0.9999913036863602 | -1     |
|  20 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?          | Done     | Done       | 0.9999868680331471 | -1     |
|  21 | Tensor<[12, 12, 12]> self = ?,<br>Tensor<[12, 12, 64]> mat2 = ?          | Done     | Done       | 0.9999915947718855 | -1     |
|  22 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?          | Done     | Done       | 0.9999854420000069 | -1     |
|  23 | Tensor<[12, 14, 14]> self = ?,<br>Tensor<[12, 14, 64]> mat2 = ?          | Done     | Done       | 0.9999918627206801 | -1     |
|  24 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ?          | Done     | Done       | 0.9999861369120123 | -1     |
|  25 | Tensor<[12, 16, 16]> self = ?,<br>Tensor<[12, 16, 64]> mat2 = ?          | Done     | Done       | 0.9999915570891666 | -1     |
|  26 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?          | Done     | Done       | 0.9999859896364426 | -1     |
|  27 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ?       | Done     | Done       | 0.9999820738501628 | -1     |
|  28 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?        | Done     | Done       | 0.9999863954694472 | -1     |
|  29 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Done     | Done       | 0.9999891958493866 | -1     |
|  30 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Done     | Done       | 0.9999865660077385 | -1     |
|  31 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ?          | Done     | Done       | 0.9999894980477769 | -1     |
|  32 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ?          | Done     | Done       | 0.9999864047467563 | -1     |
|  33 | Tensor<[12, 257, 257]> self = ?,<br>Tensor<[12, 257, 64]> mat2 = ?       | Done     | Unknown    | N/A                | N/A    |
|  34 | Tensor<[12, 257, 64]> self = ?,<br>Tensor<[12, 64, 257]> mat2 = ?        | Done     | Unknown    | N/A                | N/A    |
|  35 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  | Done       | 0.9999878535640915 | -1     |
|  36 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  | Done       | 0.9999865288033166 | -1     |
|  37 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ?          | Done     | Done       | 0.9999861036586144 | -1     |
|  38 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ?          | Done     | Done       | 0.9999864045967819 | -1     |
|  39 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ?       | Done     | Done       | 0.9999819045237451 | -1     |
|  40 | Tensor<[12, 64, 50]> self = ?,<br>Tensor<[12, 50, 50]> mat2 = ?          | Done     | Done       | 0.9999858228601245 | -1     |
|  41 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?            | Done     | Done       | 0.999985531291128  | -1     |
|  42 | Tensor<[12, 7, 7]> self = ?,<br>Tensor<[12, 7, 64]> mat2 = ?             | Done     | Done       | 0.999991431999196  | -1     |
|  43 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999865814002238 | -1     |
|  44 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?             | Done     | Done       | 0.9999918674648179 | -1     |
|  45 | Tensor<[128, 49, 32]> self = ?,<br>Tensor<[128, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999895323018949 | -1     |
|  46 | Tensor<[128, 49, 49]> self = ?,<br>Tensor<[128, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999862346712486 | -1     |
|  47 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999895646196055 | -1     |
|  48 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999864894188827 | -1     |
|  49 | Tensor<[16, 1, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?           | Unknown  | Done       | 0.9999923867126977 | -1     |
|  50 | Tensor<[16, 1, 1]> self = ?,<br>Tensor<[16, 1, 64]> mat2 = ?             | Unknown  | Done       | 0.999995094209372  | -1     |
|  51 | Tensor<[16, 1, 2]> self = ?,<br>Tensor<[16, 2, 64]> mat2 = ?             | Unknown  | Done       | 0.9999906364687033 | -1     |
|  52 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | Done       | 0.9999863531509114 | -1     |
|  53 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?           | Unknown  | Done       | 0.9999888304095697 | -1     |
|  54 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> mat2 = ?            | Unknown  | Done       | 0.9999862918611137 | -1     |
|  55 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 2]> mat2 = ?            | Unknown  | Done       | 0.9999863511149917 | -1     |
|  56 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | Done       | 0.9999857658741848 | -1     |
|  57 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 6]> mat2 = ?            | Unknown  | Done       | 0.9999898341572007 | -1     |
|  58 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A                | N/A    |
|  59 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A                | N/A    |
|  60 | Tensor<[16, 1, 6]> self = ?,<br>Tensor<[16, 6, 64]> mat2 = ?             | Unknown  | Done       | 0.9999922645966629 | -1     |
|  61 | Tensor<[16, 1, s0 + 1]> self = ?,<br>Tensor<[16, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A                | N/A    |
|  62 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A                | N/A    |
|  63 | Tensor<[16, 10, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?          | Unknown  | Done       | 0.9999912664997934 | -1     |
|  64 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?          | Unknown  | Done       | 0.9999878829602132 | -1     |
|  65 | Tensor<[16, 19, 19]> self = ?,<br>Tensor<[16, 19, 64]> mat2 = ?          | Done     | Done       | 0.9999889332771088 | -1     |
|  66 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ?          | Done     | Done       | 0.9999863948770734 | -1     |
|  67 | Tensor<[16, 256, 256]> self = ?,<br>Tensor<[16, 256, 64]> mat2 = ?       | Done     | Done       | 0.9999791925694365 | -1     |
|  68 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ?        | Done     | Done       | 0.9999863718353895 | -1     |
|  69 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?          | Done     | Done       | 0.9999892169138453 | -1     |
|  70 | Tensor<[16, 5, 5]> self = ?,<br>Tensor<[16, 5, 64]> mat2 = ?             | Unknown  | Done       | 0.9999915909451927 | -1     |
|  71 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?            | Unknown  | Done       | 0.9999871735884699 | -1     |
|  72 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Unknown  | Done       | 0.9999860713692946 | -1     |
|  73 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Unknown  | Done       | 0.9999863299673774 | -1     |
|  74 | Tensor<[16, 64, 7]> self = ?,<br>Tensor<[16, 7, 7]> mat2 = ?             | Done     | Done       | 0.9999919738728392 | -1     |
|  75 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?            | Done     | Done       | 0.9999861598729083 | -1     |
|  76 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?             | Done     | Done       | 0.9999912212377315 | -1     |
|  77 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?          | Done     | Done       | 0.9999800031298396 | -1     |
|  78 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999858792250605 | -1     |
|  79 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 128]> mat2 = ?            | Done     | Done       | 0.9999917187689128 | -1     |
|  80 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?             | Done     | Done       | 0.999991641942293  | -1     |
|  81 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999894806514106 | -1     |
|  82 | Tensor<[192, 49, 49]> self = ?,<br>Tensor<[192, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999861606442284 | -1     |
|  83 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ?        | Done     | Done       | 0.999989453252732  | -1     |
|  84 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999864294743266 | -1     |
|  85 | Tensor<[2, 256, 4096]> self = ?,<br>Tensor<[2, 4096, 32]> mat2 = ?       | Done     | Done       | 0.999933817791692  | -1     |
|  86 | Tensor<[2, 32, 4096]> self = ?,<br>Tensor<[2, 4096, 256]> mat2 = ?       | Done     | Done       | 0.9999329913293202 | -1     |
|  87 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?        | Done     | Done       | 0.9999752742810436 | -1     |
|  88 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894964865288 | -1     |
|  89 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?        | Unknown  | Done       | 0.999976060196923  | -1     |
|  90 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?         | Unknown  | Done       | 0.9999863996932151 | -1     |
|  91 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Done     | Done       | 0.9999858975180999 | -1     |
|  92 | Tensor<[24, 49, 32]> self = ?,<br>Tensor<[24, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999895698440466 | -1     |
|  93 | Tensor<[24, 49, 49]> self = ?,<br>Tensor<[24, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999859829322766 | -1     |
|  94 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999896804121913 | -1     |
|  95 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999865788883158 | -1     |
|  96 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ?        | Done     | Done       | 0.9999895361867691 | -1     |
|  97 | Tensor<[256, 49, 49]> self = ?,<br>Tensor<[256, 49, 32]> mat2 = ?        | Done     | Done       | 0.9999861610008934 | -1     |
|  98 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ?        | Done     | Done       | 0.9999894956047984 | -1     |
|  99 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ?        | Done     | Done       | 0.9999864741031269 | -1     |
| 100 | Tensor<[3, 1445, 1445]> self = ?,<br>Tensor<[3, 1445, 64]> mat2 = ?      | Done     | Done       | 0.9999631189869164 | -1     |
| 101 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ?        | Done     | Done       | 0.9999863690234564 | -1     |
| 102 | Tensor<[32, 49, 32]> self = ?,<br>Tensor<[32, 32, 49]> mat2 = ?          | Done     | Done       | 0.999989439010594  | -1     |
| 103 | Tensor<[32, 49, 49]> self = ?,<br>Tensor<[32, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999859461994394 | -1     |
| 104 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894850189365 | -1     |
| 105 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999863003594324 | -1     |
| 106 | Tensor<[48, 49, 32]> self = ?,<br>Tensor<[48, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999894213995139 | -1     |
| 107 | Tensor<[48, 49, 49]> self = ?,<br>Tensor<[48, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862747401228 | -1     |
| 108 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999894934099083 | -1     |
| 109 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999864440085281 | -1     |
| 110 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?        | Done     | Done       | 0.99997530986974   | -1     |
| 111 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894726373225 | -1     |
| 112 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?        | Unknown  | Done       | 0.9999762147887724 | -1     |
| 113 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?         | Unknown  | Done       | 0.9999863454192432 | -1     |
| 114 | Tensor<[5, 256, 1024]> self = ?,<br>Tensor<[5, 1024, 32]> mat2 = ?       | Done     | Done       | 0.9999654530435398 | -1     |
| 115 | Tensor<[5, 32, 1024]> self = ?,<br>Tensor<[5, 1024, 256]> mat2 = ?       | Done     | Done       | 0.9999658929241735 | -1     |
| 116 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?             | Unknown  | Done       | 0.9999931809946383 | -1     |
| 117 | Tensor<[6, 1, 17]> self = ?,<br>Tensor<[6, 17, 64]> mat2 = ?             | Unknown  | Done       | 0.9999904522856395 | -1     |
| 118 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?               | Unknown  | Done       | 0.9999936280028553 | -1     |
| 119 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?               | Unknown  | Done       | 0.9999916665173602 | -1     |
| 120 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?             | Unknown  | Done       | 0.9999891226201204 | -1     |
| 121 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 17]> mat2 = ?             | Unknown  | Done       | 0.9999909133743379 | -1     |
| 122 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?              | Unknown  | Done       | 0.9999343368663529 | -1     |
| 123 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?              | Unknown  | Done       | 0.999992339899756  | -1     |
| 124 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 125 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 126 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?            | Unknown  | Done       | 0.9999917388862369 | -1     |
| 127 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?            | Unknown  | Done       | 0.99998639228243   | -1     |
| 128 | Tensor<[64, 49, 32]> self = ?,<br>Tensor<[64, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999894314806831 | -1     |
| 129 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862153491089 | -1     |
| 130 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?          | Done     | Done       | 0.999989475943517  | -1     |
| 131 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?          | Done     | Done       | 0.9999863212379165 | -1     |
| 132 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?            | Done     | Done       | 0.9999864127303573 | -1     |
| 133 | Tensor<[64, 9, 9]> self = ?,<br>Tensor<[64, 9, 64]> mat2 = ?             | Done     | Done       | 0.999991496428511  | -1     |
| 134 | Tensor<[8, 1, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?             | Unknown  | Done       | 0.9999919239717305 | -1     |
| 135 | Tensor<[8, 1, 1]> self = ?,<br>Tensor<[8, 1, 64]> mat2 = ?               | Unknown  | Done       | 0.999992550566179  | -1     |
| 136 | Tensor<[8, 1, 2]> self = ?,<br>Tensor<[8, 2, 64]> mat2 = ?               | Unknown  | Done       | 0.999993057796983  | -1     |
| 137 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?             | Unknown  | Done       | 0.9999885854754114 | -1     |
| 138 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 1]> mat2 = ?              | Unknown  | Done       | 0.999999205186784  | -1     |
| 139 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 2]> mat2 = ?              | Unknown  | Done       | 0.9999930048613762 | -1     |
| 140 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 141 | Tensor<[8, 1, s0 + 1]> self = ?,<br>Tensor<[8, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 142 | Tensor<[8, 10, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?            | Unknown  | Done       | 0.9999915710638486 | -1     |
| 143 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?            | Unknown  | Done       | 0.9999868339217672 | -1     |
| 144 | Tensor<[8, 100, 100]> self = ?,<br>Tensor<[8, 100, 32]> mat2 = ?         | Unknown  | Done       | 0.9999809758262143 | -1     |
| 145 | Tensor<[8, 100, 32]> self = ?,<br>Tensor<[8, 32, 100]> mat2 = ?          | Unknown  | Done       | 0.9999896646073299 | -1     |
| 146 | Tensor<[8, 100, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Unknown  | Done       | 0.9999645059042922 | -1     |
| 147 | Tensor<[8, 2048, 256]> self = ?,<br>Tensor<[8, 256, 96]> mat2 = ?        | Done     | Done       | 0.999975416667732  | -1     |
| 148 | Tensor<[8, 2048, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?         | Done     | Done       | 0.9999894723816976 | -1     |
| 149 | Tensor<[8, 256, 2048]> self = ?,<br>Tensor<[8, 2048, 160]> mat2 = ?      | Done     | Done       | 0.9999210019881204 | -1     |
| 150 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 160]> mat2 = ?        | Done     | Done       | 0.9999790999077489 | -1     |
| 151 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?         | Done     | Done       | 0.9999753972689666 | -1     |
| 152 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?         | Done     | Done       | 0.9999894785179195 | -1     |
| 153 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?          | Done     | Done       | 0.9999895049808116 | -1     |
| 154 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?         | Unknown  | Done       | 0.9999796835641306 | -1     |
| 155 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?          | Unknown  | Done       | 0.999986395812676  | -1     |
| 156 | Tensor<[8, 32, 256]> self = ?,<br>Tensor<[8, 256, 256]> mat2 = ?         | Done     | Done       | 0.9999756545215557 | -1     |
| 157 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Unknown  | Done       | 0.9999642881932412 | -1     |
| 158 | Tensor<[96, 49, 32]> self = ?,<br>Tensor<[96, 32, 49]> mat2 = ?          | Done     | Done       | 0.9999894907997317 | -1     |
| 159 | Tensor<[96, 49, 49]> self = ?,<br>Tensor<[96, 49, 32]> mat2 = ?          | Done     | Done       | 0.9999862439723118 | -1     |
| 160 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?          | Done     | Done       | 0.9999895038634964 | -1     |
| 161 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?          | Done     | Done       | 0.999986508946386  | -1     |

