### aten.bmm.default
|     | ATen Input Variations                                                    | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|----:|:-------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|   0 | Tensor<[1, 16384, 256]> self = ?,<br>Tensor<[1, 256, 32]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|   1 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 32, 256]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|   2 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|   3 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|   4 | Tensor<[1, 256, 16384]> self = ?,<br>Tensor<[1, 16384, 32]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   5 | Tensor<[1, 32, 16384]> self = ?,<br>Tensor<[1, 16384, 256]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   6 | Tensor<[12, 1, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   7 | Tensor<[12, 1, 1]> self = ?,<br>Tensor<[12, 1, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   8 | Tensor<[12, 1, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   9 | Tensor<[12, 1, 2]> self = ?,<br>Tensor<[12, 2, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  10 | Tensor<[12, 1, 46]> self = ?,<br>Tensor<[12, 46, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  11 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  12 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 1]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  13 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  14 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 2]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  15 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, 46]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  16 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s0 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  17 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s10 + 1]> mat2 = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  18 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s2 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  19 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s4 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  20 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s6 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  21 | Tensor<[12, 1, 64]> self = ?,<br>Tensor<[12, 64, s8 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  22 | Tensor<[12, 1, s0 + 1]> self = ?,<br>Tensor<[12, s0 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  23 | Tensor<[12, 1, s10 + 1]> self = ?,<br>Tensor<[12, s10 + 1, 64]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  24 | Tensor<[12, 1, s2 + 1]> self = ?,<br>Tensor<[12, s2 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  25 | Tensor<[12, 1, s4 + 1]> self = ?,<br>Tensor<[12, s4 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  26 | Tensor<[12, 1, s6 + 1]> self = ?,<br>Tensor<[12, s6 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  27 | Tensor<[12, 1, s8 + 1]> self = ?,<br>Tensor<[12, s8 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  28 | Tensor<[12, 10, 10]> self = ?,<br>Tensor<[12, 10, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  29 | Tensor<[12, 10, 64]> self = ?,<br>Tensor<[12, 64, 10]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  30 | Tensor<[12, 12, 12]> self = ?,<br>Tensor<[12, 12, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  31 | Tensor<[12, 12, 64]> self = ?,<br>Tensor<[12, 64, 12]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  32 | Tensor<[12, 14, 14]> self = ?,<br>Tensor<[12, 14, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  33 | Tensor<[12, 14, 64]> self = ?,<br>Tensor<[12, 64, 14]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  34 | Tensor<[12, 16, 16]> self = ?,<br>Tensor<[12, 16, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  35 | Tensor<[12, 16, 64]> self = ?,<br>Tensor<[12, 64, 16]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  36 | Tensor<[12, 197, 197]> self = ?,<br>Tensor<[12, 197, 64]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  37 | Tensor<[12, 197, 64]> self = ?,<br>Tensor<[12, 64, 197]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  38 | Tensor<[12, 201, 201]> self = ?,<br>Tensor<[12, 201, 64]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  39 | Tensor<[12, 201, 64]> self = ?,<br>Tensor<[12, 64, 201]> mat2 = ?        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  40 | Tensor<[12, 24, 24]> self = ?,<br>Tensor<[12, 24, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  41 | Tensor<[12, 24, 64]> self = ?,<br>Tensor<[12, 64, 24]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  42 | Tensor<[12, 25, 25]> self = ?,<br>Tensor<[12, 25, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  43 | Tensor<[12, 25, 64]> self = ?,<br>Tensor<[12, 64, 25]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  44 | Tensor<[12, 45, 45]> self = ?,<br>Tensor<[12, 45, 64]> mat2 = ?          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  45 | Tensor<[12, 45, 64]> self = ?,<br>Tensor<[12, 64, 45]> mat2 = ?          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  46 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  47 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  48 | Tensor<[12, 64, 197]> self = ?,<br>Tensor<[12, 197, 197]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  49 | Tensor<[12, 64, 50]> self = ?,<br>Tensor<[12, 50, 50]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  50 | Tensor<[12, 7, 64]> self = ?,<br>Tensor<[12, 64, 7]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  51 | Tensor<[12, 7, 7]> self = ?,<br>Tensor<[12, 7, 64]> mat2 = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  52 | Tensor<[12, 9, 64]> self = ?,<br>Tensor<[12, 64, 9]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  53 | Tensor<[12, 9, 9]> self = ?,<br>Tensor<[12, 9, 64]> mat2 = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  54 | Tensor<[128, 49, 32]> self = ?,<br>Tensor<[128, 32, 49]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  55 | Tensor<[128, 49, 49]> self = ?,<br>Tensor<[128, 49, 32]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  56 | Tensor<[128, 64, 32]> self = ?,<br>Tensor<[128, 32, 64]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  57 | Tensor<[128, 64, 64]> self = ?,<br>Tensor<[128, 64, 32]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  58 | Tensor<[16, 1, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  59 | Tensor<[16, 1, 1]> self = ?,<br>Tensor<[16, 1, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  60 | Tensor<[16, 1, 2]> self = ?,<br>Tensor<[16, 2, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  61 | Tensor<[16, 1, 60]> self = ?,<br>Tensor<[16, 60, 64]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  62 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  63 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 1]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  64 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 2]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  65 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 60]> mat2 = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  66 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, 6]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  67 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s0 + 1]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  68 | Tensor<[16, 1, 64]> self = ?,<br>Tensor<[16, 64, s10 + 1]> mat2 = ?      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  69 | Tensor<[16, 1, 6]> self = ?,<br>Tensor<[16, 6, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  70 | Tensor<[16, 1, s0 + 1]> self = ?,<br>Tensor<[16, s0 + 1, 64]> mat2 = ?   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  71 | Tensor<[16, 1, s10 + 1]> self = ?,<br>Tensor<[16, s10 + 1, 64]> mat2 = ? | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  72 | Tensor<[16, 10, 10]> self = ?,<br>Tensor<[16, 10, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  73 | Tensor<[16, 10, 64]> self = ?,<br>Tensor<[16, 64, 10]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  74 | Tensor<[16, 19, 19]> self = ?,<br>Tensor<[16, 19, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  75 | Tensor<[16, 19, 64]> self = ?,<br>Tensor<[16, 64, 19]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  76 | Tensor<[16, 197, 197]> self = ?,<br>Tensor<[16, 197, 64]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  77 | Tensor<[16, 197, 64]> self = ?,<br>Tensor<[16, 64, 197]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  78 | Tensor<[16, 256, 256]> self = ?,<br>Tensor<[16, 256, 64]> mat2 = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  79 | Tensor<[16, 256, 64]> self = ?,<br>Tensor<[16, 64, 256]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  80 | Tensor<[16, 32, 32]> self = ?,<br>Tensor<[16, 32, 96]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  81 | Tensor<[16, 5, 5]> self = ?,<br>Tensor<[16, 5, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  82 | Tensor<[16, 5, 64]> self = ?,<br>Tensor<[16, 64, 5]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  83 | Tensor<[16, 59, 59]> self = ?,<br>Tensor<[16, 59, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  84 | Tensor<[16, 59, 64]> self = ?,<br>Tensor<[16, 64, 59]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  85 | Tensor<[16, 64, 197]> self = ?,<br>Tensor<[16, 197, 197]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  86 | Tensor<[16, 64, 7]> self = ?,<br>Tensor<[16, 7, 7]> mat2 = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  87 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  88 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  89 | Tensor<[16, 9, 128]> self = ?,<br>Tensor<[16, 128, 9]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  90 | Tensor<[16, 9, 64]> self = ?,<br>Tensor<[16, 64, 9]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  91 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 128]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
|  92 | Tensor<[16, 9, 9]> self = ?,<br>Tensor<[16, 9, 64]> mat2 = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  93 | Tensor<[192, 49, 32]> self = ?,<br>Tensor<[192, 32, 49]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  94 | Tensor<[192, 49, 49]> self = ?,<br>Tensor<[192, 49, 32]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  95 | Tensor<[192, 64, 32]> self = ?,<br>Tensor<[192, 32, 64]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  96 | Tensor<[192, 64, 64]> self = ?,<br>Tensor<[192, 64, 32]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  97 | Tensor<[2, 256, 4096]> self = ?,<br>Tensor<[2, 4096, 32]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  98 | Tensor<[2, 32, 4096]> self = ?,<br>Tensor<[2, 4096, 256]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  99 | Tensor<[2, 4096, 256]> self = ?,<br>Tensor<[2, 256, 32]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 100 | Tensor<[2, 4096, 32]> self = ?,<br>Tensor<[2, 32, 256]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 101 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 102 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 103 | Tensor<[24, 12, 64]> self = ?,<br>Tensor<[24, 64, 24]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 104 | Tensor<[24, 49, 32]> self = ?,<br>Tensor<[24, 32, 49]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 105 | Tensor<[24, 49, 49]> self = ?,<br>Tensor<[24, 49, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 106 | Tensor<[24, 64, 32]> self = ?,<br>Tensor<[24, 32, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 107 | Tensor<[24, 64, 64]> self = ?,<br>Tensor<[24, 64, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 108 | Tensor<[256, 49, 32]> self = ?,<br>Tensor<[256, 32, 49]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 109 | Tensor<[256, 49, 49]> self = ?,<br>Tensor<[256, 49, 32]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 110 | Tensor<[256, 64, 32]> self = ?,<br>Tensor<[256, 32, 64]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 111 | Tensor<[256, 64, 64]> self = ?,<br>Tensor<[256, 64, 32]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 112 | Tensor<[3, 1445, 1445]> self = ?,<br>Tensor<[3, 1445, 64]> mat2 = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 113 | Tensor<[3, 1445, 64]> self = ?,<br>Tensor<[3, 64, 1445]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 114 | Tensor<[32, 49, 32]> self = ?,<br>Tensor<[32, 32, 49]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 115 | Tensor<[32, 49, 49]> self = ?,<br>Tensor<[32, 49, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 116 | Tensor<[32, 64, 32]> self = ?,<br>Tensor<[32, 32, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 117 | Tensor<[32, 64, 64]> self = ?,<br>Tensor<[32, 64, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 118 | Tensor<[48, 49, 32]> self = ?,<br>Tensor<[48, 32, 49]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 119 | Tensor<[48, 49, 49]> self = ?,<br>Tensor<[48, 49, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 120 | Tensor<[48, 64, 32]> self = ?,<br>Tensor<[48, 32, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 121 | Tensor<[48, 64, 64]> self = ?,<br>Tensor<[48, 64, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 122 | Tensor<[5, 1024, 256]> self = ?,<br>Tensor<[5, 256, 32]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 123 | Tensor<[5, 1024, 32]> self = ?,<br>Tensor<[5, 32, 256]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 124 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 125 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 126 | Tensor<[5, 256, 1024]> self = ?,<br>Tensor<[5, 1024, 32]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 127 | Tensor<[5, 32, 1024]> self = ?,<br>Tensor<[5, 1024, 256]> mat2 = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 128 | Tensor<[6, 1, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 129 | Tensor<[6, 1, 17]> self = ?,<br>Tensor<[6, 17, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 130 | Tensor<[6, 1, 1]> self = ?,<br>Tensor<[6, 1, 64]> mat2 = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 131 | Tensor<[6, 1, 2]> self = ?,<br>Tensor<[6, 2, 64]> mat2 = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 132 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 133 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 17]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 134 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 1]> mat2 = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 135 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, 2]> mat2 = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 136 | Tensor<[6, 1, 64]> self = ?,<br>Tensor<[6, 64, s0 + 1]> mat2 = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 137 | Tensor<[6, 1, s0 + 1]> self = ?,<br>Tensor<[6, s0 + 1, 64]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 138 | Tensor<[6, 15, 15]> self = ?,<br>Tensor<[6, 15, 64]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 139 | Tensor<[6, 15, 64]> self = ?,<br>Tensor<[6, 64, 15]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 140 | Tensor<[64, 49, 32]> self = ?,<br>Tensor<[64, 32, 49]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 141 | Tensor<[64, 49, 49]> self = ?,<br>Tensor<[64, 49, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 142 | Tensor<[64, 64, 32]> self = ?,<br>Tensor<[64, 32, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 143 | Tensor<[64, 64, 64]> self = ?,<br>Tensor<[64, 64, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 144 | Tensor<[64, 9, 64]> self = ?,<br>Tensor<[64, 64, 9]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 145 | Tensor<[64, 9, 9]> self = ?,<br>Tensor<[64, 9, 64]> mat2 = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 146 | Tensor<[71, 7, 64]> self = ?,<br>Tensor<[71, 64, 7]> mat2 = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 147 | Tensor<[71, 7, 7]> self = ?,<br>Tensor<[71, 7, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 148 | Tensor<[8, 1, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 149 | Tensor<[8, 1, 1]> self = ?,<br>Tensor<[8, 1, 64]> mat2 = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 150 | Tensor<[8, 1, 2]> self = ?,<br>Tensor<[8, 2, 64]> mat2 = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 151 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 152 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 1]> mat2 = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 153 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, 2]> mat2 = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 154 | Tensor<[8, 1, 64]> self = ?,<br>Tensor<[8, 64, s0 + 1]> mat2 = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 155 | Tensor<[8, 1, s0 + 1]> self = ?,<br>Tensor<[8, s0 + 1, 64]> mat2 = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 156 | Tensor<[8, 10, 10]> self = ?,<br>Tensor<[8, 10, 64]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 157 | Tensor<[8, 10, 64]> self = ?,<br>Tensor<[8, 64, 10]> mat2 = ?            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 158 | Tensor<[8, 100, 100]> self = ?,<br>Tensor<[8, 100, 32]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 159 | Tensor<[8, 100, 32]> self = ?,<br>Tensor<[8, 32, 100]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 160 | Tensor<[8, 100, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 161 | Tensor<[8, 2048, 256]> self = ?,<br>Tensor<[8, 256, 96]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 162 | Tensor<[8, 2048, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 163 | Tensor<[8, 256, 2048]> self = ?,<br>Tensor<[8, 2048, 160]> mat2 = ?      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 164 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 160]> mat2 = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 165 | Tensor<[8, 256, 256]> self = ?,<br>Tensor<[8, 256, 32]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 166 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 2048]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 167 | Tensor<[8, 256, 32]> self = ?,<br>Tensor<[8, 32, 256]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 168 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 169 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 170 | Tensor<[8, 32, 256]> self = ?,<br>Tensor<[8, 256, 256]> mat2 = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 171 | Tensor<[8, 920, 920]> self = ?,<br>Tensor<[8, 920, 32]> mat2 = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 172 | Tensor<[96, 49, 32]> self = ?,<br>Tensor<[96, 32, 49]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 173 | Tensor<[96, 49, 49]> self = ?,<br>Tensor<[96, 49, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 174 | Tensor<[96, 64, 32]> self = ?,<br>Tensor<[96, 32, 64]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 175 | Tensor<[96, 64, 64]> self = ?,<br>Tensor<[96, 64, 32]> mat2 = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |

