### aten.transpose.int
|     | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|----:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Fallback | Done       | True  |
|   1 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
|   2 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|   3 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|   4 | Tensor<[1, 1, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | True  |
|   5 | Tensor<[1, 1, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
|   6 | Tensor<[1, 1, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
|   7 | Tensor<[1, 10, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|   8 | Tensor<[1, 10, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|   9 | Tensor<[1, 10, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  10 | Tensor<[1, 1024, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
|  11 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Fallback | Done       | True  |
|  12 | Tensor<[1, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  13 | Tensor<[1, 1024, 640]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  14 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  15 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | True  |
|  16 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|  17 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  18 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2        | Done     | Done       | True  |
|  19 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|  20 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | Done       | True  |
|  21 | Tensor<[1, 12, 14, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|  22 | Tensor<[1, 12, 14, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | Done       | True  |
|  23 | Tensor<[1, 12, 1500, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       | True  |
|  24 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  25 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 3        | Done     | Done       | True  |
|  26 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Fallback | Done       | True  |
|  27 | Tensor<[1, 12, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | True  |
|  28 | Tensor<[1, 12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  29 | Tensor<[1, 12, 25, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|  30 | Tensor<[1, 12, 4, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
|  31 | Tensor<[1, 12, 45, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | True  |
|  32 | Tensor<[1, 12, 46, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | True  |
|  33 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  34 | Tensor<[1, 12, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | None     | Fallback   | True  |
|  35 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | Done       | True  |
|  36 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | Done       | True  |
|  37 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | Done       | True  |
|  38 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2    | Unknown  | Unknown    | N/A   |
|  39 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Unknown    | N/A   |
|  40 | Tensor<[1, 1200, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  41 | Tensor<[1, 128, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  42 | Tensor<[1, 128, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  43 | Tensor<[1, 1280, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  44 | Tensor<[1, 1370, 1, 3, 1280]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | None     | Fallback   | True  |
|  45 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       | True  |
|  46 | Tensor<[1, 144, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
|  47 | Tensor<[1, 15, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  48 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | Done       | True  |
|  49 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
|  50 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | True  |
|  51 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  52 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2        | Done     | Done       | True  |
|  53 | Tensor<[1, 16, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  54 | Tensor<[1, 16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  55 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Fallback | Done       | True  |
|  56 | Tensor<[1, 16, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | True  |
|  57 | Tensor<[1, 16, 256, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | True  |
|  58 | Tensor<[1, 16, 5, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | Done       | True  |
|  59 | Tensor<[1, 16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  60 | Tensor<[1, 16, 6, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | Done       | True  |
|  61 | Tensor<[1, 16, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | None     | Fallback   | True  |
|  62 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|  63 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | Done       | True  |
|  64 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | Done       | True  |
|  65 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | Done       | True  |
|  66 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2    | Unknown  | Unknown    | N/A   |
|  67 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Unknown    | N/A   |
|  68 | Tensor<[1, 160, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  69 | Tensor<[1, 16384, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  70 | Tensor<[1, 16384, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | Done       | True  |
|  71 | Tensor<[1, 16384, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
|  72 | Tensor<[1, 19, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  73 | Tensor<[1, 192, 1344]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Fallback | Done       | True  |
|  74 | Tensor<[1, 19200, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  75 | Tensor<[1, 196, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  76 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
|  77 | Tensor<[1, 197, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2  | None     | Fallback   | True  |
|  78 | Tensor<[1, 197, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2   | None     | Fallback   | True  |
|  79 | Tensor<[1, 197, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0         | Done     | Done       | True  |
|  80 | Tensor<[1, 197, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | Done       | True  |
|  81 | Tensor<[1, 2, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|  82 | Tensor<[1, 2, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
|  83 | Tensor<[1, 2, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | True  |
|  84 | Tensor<[1, 2048, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  85 | Tensor<[1, 24, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  86 | Tensor<[1, 24, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
|  87 | Tensor<[1, 24, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  88 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
|  89 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  90 | Tensor<[1, 256, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  91 | Tensor<[1, 256, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  92 | Tensor<[1, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
|  93 | Tensor<[1, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
|  94 | Tensor<[1, 256, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  95 | Tensor<[1, 3, 1445, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | True  |
|  96 | Tensor<[1, 300, 2048]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  97 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
|  98 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
|  99 | Tensor<[1, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
| 100 | Tensor<[1, 32, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 101 | Tensor<[1, 32, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 102 | Tensor<[1, 32, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 103 | Tensor<[1, 32, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 104 | Tensor<[1, 320, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 105 | Tensor<[1, 4, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
| 106 | Tensor<[1, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 107 | Tensor<[1, 4096, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 108 | Tensor<[1, 4096, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | Done       | True  |
| 109 | Tensor<[1, 4150, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 110 | Tensor<[1, 4800, 512]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 111 | Tensor<[1, 49, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Unknown    | N/A   |
| 112 | Tensor<[1, 5, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
| 113 | Tensor<[1, 5, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
| 114 | Tensor<[1, 5, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | True  |
| 115 | Tensor<[1, 50, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2   | None     | Fallback   | True  |
| 116 | Tensor<[1, 50, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2    | None     | Fallback   | True  |
| 117 | Tensor<[1, 50, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | Done       | True  |
| 118 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 119 | Tensor<[1, 50, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0           | Done     | Done       | True  |
| 120 | Tensor<[1, 512, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
| 121 | Tensor<[1, 512, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 122 | Tensor<[1, 59, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 123 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 124 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 125 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 126 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Done     | Done       | True  |
| 127 | Tensor<[1, 6, 17, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | True  |
| 128 | Tensor<[1, 6, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 129 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   |
| 130 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 131 | Tensor<[1, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Fallback | Unknown    | N/A   |
| 132 | Tensor<[1, 64, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
| 133 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | Done       | True  |
| 134 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | Done       | True  |
| 135 | Tensor<[1, 640, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 136 | Tensor<[1, 768, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Fallback | Done       | True  |
| 137 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Fallback | Done       | True  |
| 138 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | None     | Fallback   | True  |
| 139 | Tensor<[1, 8, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 140 | Tensor<[1, 8, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 141 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | True  |
| 142 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Done     | Done       | True  |
| 143 | Tensor<[1, 8, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 144 | Tensor<[1, 8, 2048, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | True  |
| 145 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
| 146 | Tensor<[1, 8, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | True  |
| 147 | Tensor<[1, 8, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | True  |
| 148 | Tensor<[1, 8, 4096, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | Done       | True  |
| 149 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   |
| 150 | Tensor<[1, 8, s0*s1, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   |
| 151 | Tensor<[1, 8, s0*s1, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   |
| 152 | Tensor<[1, 8, s1*s2, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   |
| 153 | Tensor<[1, 8, s1*s2, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   |
| 154 | Tensor<[1, 8, s1*s2, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   |
| 155 | Tensor<[1, 9, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
| 156 | Tensor<[1, 9, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 157 | Tensor<[1, 9, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 158 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   |
| 159 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   |
| 160 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   |
| 161 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   |
| 162 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   |
| 163 | Tensor<[100, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | True  |
| 164 | Tensor<[12, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | None     | Fallback   | True  |
| 165 | Tensor<[12, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
| 166 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | True  |
| 167 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | True  |
| 168 | Tensor<[12, 50, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Unknown    | N/A   |
| 169 | Tensor<[12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | True  |
| 170 | Tensor<[12, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | None     | Fallback   | True  |
| 171 | Tensor<[12, 64, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Fallback | Unknown    | N/A   |
| 172 | Tensor<[1370, 1, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       | True  |
| 173 | Tensor<[1370, 16, 80]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Done     | Done       | True  |
| 174 | Tensor<[16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | True  |
| 175 | Tensor<[16, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | None     | Fallback   | True  |
| 176 | Tensor<[16, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
| 177 | Tensor<[16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | True  |
| 178 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 179 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 180 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 181 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 182 | Tensor<[16, 60, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
| 183 | Tensor<[16, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | None     | Fallback   | True  |
| 184 | Tensor<[16, 64, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | None     | Unknown    | N/A   |
| 185 | Tensor<[16, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Done     | Done       | True  |
| 186 | Tensor<[16, 7, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2             | None     | Unknown    | N/A   |
| 187 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 188 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 189 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 190 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 191 | Tensor<[16, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   |
| 192 | Tensor<[197, 1, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0         | Done     | Done       | True  |
| 193 | Tensor<[197, 1, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | Done       | True  |
| 194 | Tensor<[197, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1          | Fallback | Done       | True  |
| 195 | Tensor<[197, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1          | Fallback | Done       | True  |
| 196 | Tensor<[2, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
| 197 | Tensor<[2, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
| 198 | Tensor<[2, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
| 199 | Tensor<[2, 4096, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 200 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
| 201 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | True  |
| 202 | Tensor<[24, 12, 24]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | True  |
| 203 | Tensor<[24, 24, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | Done       | True  |
| 204 | Tensor<[262, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1             | Done     | Done       | True  |
| 205 | Tensor<[4, 12, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 206 | Tensor<[4, 12, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 207 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 208 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 209 | Tensor<[4, 16, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 210 | Tensor<[4, 16, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 211 | Tensor<[4, 16, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 212 | Tensor<[4, 16, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 213 | Tensor<[5, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | True  |
| 214 | Tensor<[5, 1024, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 215 | Tensor<[5, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
| 216 | Tensor<[5, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
| 217 | Tensor<[50, 1, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | Done       | True  |
| 218 | Tensor<[50, 1, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0           | Done     | Done       | True  |
| 219 | Tensor<[50, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Fallback | Done       | True  |
| 220 | Tensor<[50, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | True  |
| 221 | Tensor<[6, 100, 1, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | Done       | True  |
| 222 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 223 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 224 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 225 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 226 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 227 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 228 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | True  |
| 229 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | True  |
| 230 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | Done       | True  |
| 231 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | True  |
| 232 | Tensor<[8, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | True  |
| 233 | Tensor<[8, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
| 234 | Tensor<[8, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | True  |
| 235 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | Done       | True  |
| 236 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | True  |
| 237 | Tensor<[920, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | True  |

