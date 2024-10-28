### aten.bmm.default
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ?       | Done     | Done       | True  |
|   1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?        | Done     | Done       | True  |
|   2 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ?       | Done     | Done       | True  |
|   3 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?        | Done     | Done       | True  |
|   4 | Tensor<[1, 256, 16384]> self = ?,<br>Tensor<[1, 16384, 32]> mat2 = ?     | Unknown  | Done       | True  |
|   5 | Tensor<[1, 32, 16384]> self = ?,<br>Tensor<[1, 16384, 256]> mat2 = ?     | Unknown  | Done       | True  |
|   6 | Tensor<[12, 1, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?           | Unknown  | Done       | True  |
|   7 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  | Done       | True  |
|   8 | Tensor<[12, 1, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?           | Unknown  | Done       | True  |
|   9 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  | Done       | True  |
|  10 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  | Done       | True  |
|  11 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?           | Unknown  | Done       | True  |
|  12 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  | Done       | True  |
|  13 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?           | Unknown  | Done       | True  |
|  14 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  | Done       | True  |
|  15 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  | Done       | True  |
|  16 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A   |
|  17 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A   |
|  18 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s2 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A   |
|  19 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s4 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A   |
|  20 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s6 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A   |
|  21 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s8 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A   |
|  22 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  23 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A   |
|  24 | Tensor<[12, 1, s2 + 1]> self = ?,<br>Tensor<[12, s2 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  25 | Tensor<[12, 1, s4 + 1]> self = ?,<br>Tensor<[12, s4 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  26 | Tensor<[12, 1, s6 + 1]> self = ?,<br>Tensor<[12, s6 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  27 | Tensor<[12, 1, s8 + 1]> self = ?,<br>Tensor<[12, s8 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  28 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?          | Done     | Done       | True  |
|  29 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?          | Done     | Done       | True  |
|  30 | Tensor<[12, 12, 12]> self = ?,<br>Tensor<[12, 12, 64]> mat2 = ?          | Done     | Done       | True  |
|  31 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?          | Done     | Done       | True  |
|  32 | Tensor<[12, 14, 14]> self = ?,<br>Tensor<[12, 14, 64]> mat2 = ?          | Done     | Done       | True  |
|  33 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ?          | Done     | Done       | True  |
|  34 | Tensor<[12, 16, 16]> self = ?,<br>Tensor<[12, 16, 64]> mat2 = ?          | Done     | Done       | True  |
|  35 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?          | Done     | Done       | True  |
|  36 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ?       | Done     | Done       | True  |
|  37 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?        | Done     | Done       | True  |
|  38 | Tensor<[12, 201, 201]> self = ?,<br>Tensor<[12, 201, 64]> mat2 = ?       | Unknown  | Done       | True  |
|  39 | Tensor<[12, 201, 64]> self = ?,<br>Tensor<[12, 64, 201]> mat2 = ?        | Unknown  | Done       | True  |
|  40 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Done     | Done       | True  |
|  41 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Done     | Done       | True  |
|  42 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ?          | Done     | Done       | True  |
|  43 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ?          | Done     | Done       | True  |
|  44 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  | Done       | True  |
|  45 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  | Done       | True  |
|  46 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ?          | Done     | Done       | True  |
|  47 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ?          | Done     | Done       | True  |
|  48 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ?       | Done     | Done       | True  |
|  49 | Tensor<[12, 64, 50]> self = ?,<br>Tensor<[12, 50, 50]> mat2 = ?          | Done     | Done       | True  |
|  50 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?            | Done     | Done       | True  |
|  51 | Tensor<[12, 7, 7]> self = ?,<br>Tensor<[12, 7, 64]> mat2 = ?             | Done     | Done       | True  |
|  52 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?            | Done     | Done       | True  |
|  53 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?             | Done     | Done       | True  |
|  54 | Tensor<[128, 49, 32]> self = ?,<br>Tensor<[128, 32, 49]> mat2 = ?        | Done     | Done       | True  |
|  55 | Tensor<[128, 49, 49]> self = ?,<br>Tensor<[128, 49, 32]> mat2 = ?        | Done     | Done       | True  |
|  56 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ?        | Done     | Done       | True  |
|  57 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ?        | Done     | Done       | True  |
|  58 | Tensor<[16, 1, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?           | Unknown  | Done       | True  |
|  59 | Tensor<[16, 1, 1]> self = ?,<br>Tensor<[16, 1, 64]> mat2 = ?             | Unknown  | Done       | True  |
|  60 | Tensor<[16, 1, 2]> self = ?,<br>Tensor<[16, 2, 64]> mat2 = ?             | Unknown  | Done       | True  |
|  61 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | Done       | True  |
|  62 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?           | Unknown  | Done       | True  |
|  63 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> mat2 = ?            | Unknown  | Done       | True  |
|  64 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 2]> mat2 = ?            | Unknown  | Done       | True  |
|  65 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | Done       | True  |
|  66 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 6]> mat2 = ?            | Unknown  | Done       | True  |
|  67 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s0 + 1]> mat2 = ?       | Unknown  | Unknown    | N/A   |
|  68 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | Unknown    | N/A   |
|  69 | Tensor<[16, 1, 6]> self = ?,<br>Tensor<[16, 6, 64]> mat2 = ?             | Unknown  | Done       | True  |
|  70 | Tensor<[16, 1, s0 + 1]> self = ?,<br>Tensor<[16, s0 + 1, 64]> mat2 = ?   | Unknown  | Unknown    | N/A   |
|  71 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | Unknown    | N/A   |
|  72 | Tensor<[16, 10, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?          | Done     | Done       | True  |
|  73 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?          | Done     | Done       | True  |
|  74 | Tensor<[16, 19, 19]> self = ?,<br>Tensor<[16, 19, 64]> mat2 = ?          | Done     | Done       | True  |
|  75 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ?          | Done     | Done       | True  |
|  76 | Tensor<[16, 197, 197]> self = ?,<br>Tensor<[16, 197, 64]> mat2 = ?       | Done     | Done       | True  |
|  77 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ?        | Done     | Done       | True  |
|  78 | Tensor<[16, 256, 256]> self = ?,<br>Tensor<[16, 256, 64]> mat2 = ?       | Done     | Done       | True  |
|  79 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ?        | Done     | Done       | True  |
|  80 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?          | Done     | Done       | True  |
|  81 | Tensor<[16, 5, 5]> self = ?,<br>Tensor<[16, 5, 64]> mat2 = ?             | Unknown  | Done       | True  |
|  82 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?            | Unknown  | Done       | True  |
|  83 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Done     | Done       | True  |
|  84 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Done     | Done       | True  |
|  85 | Tensor<[16, 64, 197]> self = ?,<br>Tensor<[16, 197, 197]> mat2 = ?       | Done     | Done       | True  |
|  86 | Tensor<[16, 64, 7]> self = ?,<br>Tensor<[16, 7, 7]> mat2 = ?             | Done     | Done       | True  |
|  87 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?            | Done     | Done       | True  |
|  88 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?             | Done     | Done       | True  |
|  89 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?          | Done     | Done       | True  |
|  90 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?            | Done     | Done       | True  |
|  91 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 128]> mat2 = ?            | Done     | Done       | True  |
|  92 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?             | Done     | Done       | True  |
|  93 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ?        | Done     | Done       | True  |
|  94 | Tensor<[192, 49, 49]> self = ?,<br>Tensor<[192, 49, 32]> mat2 = ?        | Done     | Done       | True  |
|  95 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ?        | Done     | Done       | True  |
|  96 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ?        | Done     | Done       | True  |
|  97 | Tensor<[2, 256, 4096]> self = ?,<br>Tensor<[2, 4096, 32]> mat2 = ?       | Unknown  | Done       | True  |
|  98 | Tensor<[2, 32, 4096]> self = ?,<br>Tensor<[2, 4096, 256]> mat2 = ?       | Unknown  | Done       | True  |
|  99 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?        | Done     | Done       | True  |
| 100 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?         | Done     | Done       | True  |
| 101 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?        | Done     | Done       | True  |
| 102 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?         | Done     | Done       | True  |
| 103 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Done     | Done       | True  |
| 104 | Tensor<[24, 49, 32]> self = ?,<br>Tensor<[24, 32, 49]> mat2 = ?          | Done     | Done       | True  |
| 105 | Tensor<[24, 49, 49]> self = ?,<br>Tensor<[24, 49, 32]> mat2 = ?          | Done     | Done       | True  |
| 106 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?          | Done     | Done       | True  |
| 107 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?          | Done     | Done       | True  |
| 108 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ?        | Done     | Done       | True  |
| 109 | Tensor<[256, 49, 49]> self = ?,<br>Tensor<[256, 49, 32]> mat2 = ?        | Done     | Done       | True  |
| 110 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ?        | Done     | Done       | True  |
| 111 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ?        | Done     | Done       | True  |
| 112 | Tensor<[3, 1445, 1445]> self = ?,<br>Tensor<[3, 1445, 64]> mat2 = ?      | Done     | Done       | True  |
| 113 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ?        | Done     | Done       | True  |
| 114 | Tensor<[32, 49, 32]> self = ?,<br>Tensor<[32, 32, 49]> mat2 = ?          | Done     | Done       | True  |
| 115 | Tensor<[32, 49, 49]> self = ?,<br>Tensor<[32, 49, 32]> mat2 = ?          | Done     | Done       | True  |
| 116 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?          | Done     | Done       | True  |
| 117 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?          | Done     | Done       | True  |
| 118 | Tensor<[48, 49, 32]> self = ?,<br>Tensor<[48, 32, 49]> mat2 = ?          | Done     | Done       | True  |
| 119 | Tensor<[48, 49, 49]> self = ?,<br>Tensor<[48, 49, 32]> mat2 = ?          | Done     | Done       | True  |
| 120 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?          | Done     | Done       | True  |
| 121 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?          | Done     | Done       | True  |
| 122 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?        | Done     | Done       | True  |
| 123 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?         | Done     | Done       | True  |
| 124 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?        | Done     | Done       | True  |
| 125 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?         | Done     | Done       | True  |
| 126 | Tensor<[5, 256, 1024]> self = ?,<br>Tensor<[5, 1024, 32]> mat2 = ?       | Unknown  | Done       | True  |
| 127 | Tensor<[5, 32, 1024]> self = ?,<br>Tensor<[5, 1024, 256]> mat2 = ?       | Unknown  | Done       | True  |
| 128 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?             | Unknown  | Done       | True  |
| 129 | Tensor<[6, 1, 17]> self = ?,<br>Tensor<[6, 17, 64]> mat2 = ?             | Unknown  | Done       | True  |
| 130 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?               | Unknown  | Done       | True  |
| 131 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?               | Unknown  | Done       | True  |
| 132 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?             | Unknown  | Done       | True  |
| 133 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 17]> mat2 = ?             | Unknown  | Done       | True  |
| 134 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?              | Unknown  | Done       | True  |
| 135 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?              | Unknown  | Done       | True  |
| 136 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A   |
| 137 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A   |
| 138 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?            | Done     | Done       | True  |
| 139 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?            | Done     | Done       | True  |
| 140 | Tensor<[64, 49, 32]> self = ?,<br>Tensor<[64, 32, 49]> mat2 = ?          | Done     | Done       | True  |
| 141 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 32]> mat2 = ?          | Done     | Done       | True  |
| 142 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?          | Done     | Done       | True  |
| 143 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?          | Done     | Done       | True  |
| 144 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?            | Done     | Done       | True  |
| 145 | Tensor<[64, 9, 9]> self = ?,<br>Tensor<[64, 9, 64]> mat2 = ?             | Done     | Done       | True  |
| 146 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ?            | Unknown  | Done       | True  |
| 147 | Tensor<[71, 7, 7]> self = ?,<br>Tensor<[71, 7, 64]> mat2 = ?             | Unknown  | Done       | True  |
| 148 | Tensor<[8, 1, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?             | Unknown  | Done       | True  |
| 149 | Tensor<[8, 1, 1]> self = ?,<br>Tensor<[8, 1, 64]> mat2 = ?               | Unknown  | Done       | True  |
| 150 | Tensor<[8, 1, 2]> self = ?,<br>Tensor<[8, 2, 64]> mat2 = ?               | Unknown  | Done       | True  |
| 151 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?             | Unknown  | Done       | True  |
| 152 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 1]> mat2 = ?              | Unknown  | Done       | True  |
| 153 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 2]> mat2 = ?              | Unknown  | Done       | True  |
| 154 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, s0 + 1]> mat2 = ?         | Unknown  | Unknown    | N/A   |
| 155 | Tensor<[8, 1, s0 + 1]> self = ?,<br>Tensor<[8, s0 + 1, 64]> mat2 = ?     | Unknown  | Unknown    | N/A   |
| 156 | Tensor<[8, 10, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?            | Done     | Done       | True  |
| 157 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?            | Done     | Done       | True  |
| 158 | Tensor<[8, 100, 100]> self = ?,<br>Tensor<[8, 100, 32]> mat2 = ?         | Done     | Done       | True  |
| 159 | Tensor<[8, 100, 32]> self = ?,<br>Tensor<[8, 32, 100]> mat2 = ?          | Done     | Done       | True  |
| 160 | Tensor<[8, 100, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Done     | Done       | True  |
| 161 | Tensor<[8, 2048, 256]> self = ?,<br>Tensor<[8, 256, 96]> mat2 = ?        | Done     | Done       | True  |
| 162 | Tensor<[8, 2048, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?         | Done     | Done       | True  |
| 163 | Tensor<[8, 256, 2048]> self = ?,<br>Tensor<[8, 2048, 160]> mat2 = ?      | Done     | Done       | True  |
| 164 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 160]> mat2 = ?        | Done     | Done       | True  |
| 165 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?         | Done     | Done       | True  |
| 166 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?         | Done     | Done       | True  |
| 167 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?          | Done     | Done       | True  |
| 168 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?         | Done     | Done       | True  |
| 169 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?          | Done     | Done       | True  |
| 170 | Tensor<[8, 32, 256]> self = ?,<br>Tensor<[8, 256, 256]> mat2 = ?         | Unknown  | Done       | True  |
| 171 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Done     | Done       | True  |
| 172 | Tensor<[96, 49, 32]> self = ?,<br>Tensor<[96, 32, 49]> mat2 = ?          | Done     | Done       | True  |
| 173 | Tensor<[96, 49, 49]> self = ?,<br>Tensor<[96, 49, 32]> mat2 = ?          | Done     | Done       | True  |
| 174 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?          | Done     | Done       | True  |
| 175 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?          | Done     | Done       | True  |

