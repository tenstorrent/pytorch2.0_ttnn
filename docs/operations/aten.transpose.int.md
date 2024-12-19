### aten.transpose.int
|     | ATen Input Variations                                                     | Status   | Isolated   | PCC   | Host   |
|----:|:--------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|   1 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|   2 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|   3 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|   4 | Tensor<[1, 1, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|   5 | Tensor<[1, 1, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
|   6 | Tensor<[1, 1, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
|   7 | Tensor<[1, 10, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
|   8 | Tensor<[1, 10, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
|   9 | Tensor<[1, 10, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  10 | Tensor<[1, 1024, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Unknown    | N/A   | N/A    |
|  11 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  12 | Tensor<[1, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  13 | Tensor<[1, 1024, 640]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  14 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  15 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  16 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|  17 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
|  18 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
|  19 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|  20 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | Done       | 1.0   | 0      |
|  21 | Tensor<[1, 12, 14, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|  22 | Tensor<[1, 12, 14, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | Done       | 1.0   | 0      |
|  23 | Tensor<[1, 12, 1500, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  24 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  25 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 3        | Done     | Done       | 1.0   | 0      |
|  26 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | 1.0   | 0      |
|  27 | Tensor<[1, 12, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  28 | Tensor<[1, 12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  29 | Tensor<[1, 12, 25, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|  30 | Tensor<[1, 12, 4, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  31 | Tensor<[1, 12, 45, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | 1.0   | 0      |
|  32 | Tensor<[1, 12, 46, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | Done       | 1.0   | 0      |
|  33 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  34 | Tensor<[1, 12, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | 1.0   | 0      |
|  35 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | Done       | 1.0   | 0      |
|  36 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | Done       | 1.0   | 0      |
|  37 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | Done       | 1.0   | 0      |
|  38 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2    | Unknown  | Unknown    | N/A   | N/A    |
|  39 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  40 | Tensor<[1, 1200, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  41 | Tensor<[1, 128, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  42 | Tensor<[1, 128, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  43 | Tensor<[1, 1280, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  44 | Tensor<[1, 1370, 1, 3, 1280]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | Done     | Done       | 1.0   | 1      |
|  45 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       | 1.0   | 0      |
|  46 | Tensor<[1, 144, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
|  47 | Tensor<[1, 15, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  48 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Done       | 1.0   | 0      |
|  49 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  50 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  51 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
|  52 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
|  53 | Tensor<[1, 16, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  54 | Tensor<[1, 16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  55 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | 1.0   | 0      |
|  56 | Tensor<[1, 16, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
|  57 | Tensor<[1, 16, 256, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | 1.0   | 0      |
|  58 | Tensor<[1, 16, 5, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | Done       | 1.0   | 0      |
|  59 | Tensor<[1, 16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
|  60 | Tensor<[1, 16, 6, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | Done       | 1.0   | 0      |
|  61 | Tensor<[1, 16, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | 1.0   | 0      |
|  62 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|  63 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | Done       | 1.0   | 0      |
|  64 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | Done       | 1.0   | 0      |
|  65 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | Done       | 1.0   | 0      |
|  66 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2    | Unknown  | Unknown    | N/A   | N/A    |
|  67 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | Unknown    | N/A   | N/A    |
|  68 | Tensor<[1, 160, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  69 | Tensor<[1, 16384, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  70 | Tensor<[1, 16384, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  71 | Tensor<[1, 16384, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Unknown    | N/A   | N/A    |
|  72 | Tensor<[1, 19, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  73 | Tensor<[1, 192, 1344]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  74 | Tensor<[1, 19200, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  75 | Tensor<[1, 196, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  76 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
|  77 | Tensor<[1, 197, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2  | Done     | Done       | 1.0   | 1      |
|  78 | Tensor<[1, 197, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2   | Done     | Done       | 1.0   | 1      |
|  79 | Tensor<[1, 197, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0         | Done     | Done       | 1.0   | 0      |
|  80 | Tensor<[1, 197, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | Done       | 1.0   | 0      |
|  81 | Tensor<[1, 2, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|  82 | Tensor<[1, 2, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|  83 | Tensor<[1, 2, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
|  84 | Tensor<[1, 2048, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  85 | Tensor<[1, 24, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  86 | Tensor<[1, 24, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
|  87 | Tensor<[1, 24, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  88 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
|  89 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  90 | Tensor<[1, 256, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  91 | Tensor<[1, 256, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  92 | Tensor<[1, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
|  93 | Tensor<[1, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
|  94 | Tensor<[1, 256, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  95 | Tensor<[1, 3, 1445, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | 1.0   | 0      |
|  96 | Tensor<[1, 300, 2048]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  97 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
|  98 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
|  99 | Tensor<[1, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 100 | Tensor<[1, 32, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 101 | Tensor<[1, 32, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 102 | Tensor<[1, 32, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 103 | Tensor<[1, 32, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 104 | Tensor<[1, 320, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 105 | Tensor<[1, 4, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
| 106 | Tensor<[1, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 107 | Tensor<[1, 4096, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Unknown    | N/A   | N/A    |
| 108 | Tensor<[1, 4096, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | Done       | 1.0   | 0      |
| 109 | Tensor<[1, 4150, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 110 | Tensor<[1, 4800, 512]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 111 | Tensor<[1, 49, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | 1.0   | 0      |
| 112 | Tensor<[1, 5, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
| 113 | Tensor<[1, 5, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
| 114 | Tensor<[1, 5, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
| 115 | Tensor<[1, 50, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2   | Done     | Done       | 1.0   | 1      |
| 116 | Tensor<[1, 50, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2    | Done     | Done       | 1.0   | 1      |
| 117 | Tensor<[1, 50, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | Done       | 1.0   | 0      |
| 118 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 119 | Tensor<[1, 50, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0           | Done     | Done       | 1.0   | 0      |
| 120 | Tensor<[1, 512, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 121 | Tensor<[1, 512, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 122 | Tensor<[1, 59, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | Done       | 1.0   | 0      |
| 123 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
| 124 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
| 125 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
| 126 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
| 127 | Tensor<[1, 6, 17, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
| 128 | Tensor<[1, 6, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
| 129 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   | N/A    |
| 130 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 131 | Tensor<[1, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Done     | Done       | 1.0   | 0      |
| 132 | Tensor<[1, 64, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 133 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | Done       | 1.0   | 0      |
| 134 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | Done       | 1.0   | 0      |
| 135 | Tensor<[1, 640, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 136 | Tensor<[1, 768, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 137 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 138 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 139 | Tensor<[1, 8, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
| 140 | Tensor<[1, 8, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
| 141 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
| 142 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
| 143 | Tensor<[1, 8, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
| 144 | Tensor<[1, 8, 2048, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | Done       | 1.0   | 0      |
| 145 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
| 146 | Tensor<[1, 8, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
| 147 | Tensor<[1, 8, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | Done       | 1.0   | 0      |
| 148 | Tensor<[1, 8, 4096, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | Done       | 1.0   | 0      |
| 149 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   | N/A    |
| 150 | Tensor<[1, 8, s0*s1, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   | N/A    |
| 151 | Tensor<[1, 8, s0*s1, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   | N/A    |
| 152 | Tensor<[1, 8, s1*s2, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   | N/A    |
| 153 | Tensor<[1, 8, s1*s2, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   | N/A    |
| 154 | Tensor<[1, 8, s1*s2, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   | N/A    |
| 155 | Tensor<[1, 9, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | Done       | 1.0   | 0      |
| 156 | Tensor<[1, 9, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
| 157 | Tensor<[1, 9, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | Done       | 1.0   | 0      |
| 158 | Tensor<[1, s0*s1, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   | N/A    |
| 159 | Tensor<[1, s0*s1, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   | N/A    |
| 160 | Tensor<[1, s1*s2, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Unknown    | N/A   | N/A    |
| 161 | Tensor<[1, s1*s2, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   | N/A    |
| 162 | Tensor<[1, s1*s2, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   | N/A    |
| 163 | Tensor<[100, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | 1.0   | 0      |
| 164 | Tensor<[12, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 165 | Tensor<[12, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 166 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | 1.0   | 0      |
| 167 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 168 | Tensor<[12, 50, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | 1.0   | 0      |
| 169 | Tensor<[12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 170 | Tensor<[12, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 171 | Tensor<[12, 64, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | 1.0   | 0      |
| 172 | Tensor<[1370, 1, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | Done       | 1.0   | 0      |
| 173 | Tensor<[1370, 16, 80]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Done     | Done       | 1.0   | 0      |
| 174 | Tensor<[16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 175 | Tensor<[16, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 176 | Tensor<[16, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 177 | Tensor<[16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | 1.0   | 0      |
| 178 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 179 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 180 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 181 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 182 | Tensor<[16, 60, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | Done       | 1.0   | 0      |
| 183 | Tensor<[16, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 184 | Tensor<[16, 64, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Unknown  | Done       | 1.0   | 0      |
| 185 | Tensor<[16, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Done     | Done       | 1.0   | 0      |
| 186 | Tensor<[16, 7, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2             | Unknown  | Done       | 1.0   | 0      |
| 187 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 188 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 189 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 190 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 191 | Tensor<[16, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Unknown    | N/A   | N/A    |
| 192 | Tensor<[197, 1, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0         | Done     | Done       | 1.0   | 0      |
| 193 | Tensor<[197, 1, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | Done       | 1.0   | 0      |
| 194 | Tensor<[197, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1          | Done     | Done       | 1.0   | 0      |
| 195 | Tensor<[197, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1          | Done     | Done       | 1.0   | 0      |
| 196 | Tensor<[2, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 197 | Tensor<[2, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 198 | Tensor<[2, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 199 | Tensor<[2, 4096, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 200 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 201 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 202 | Tensor<[24, 12, 24]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | 1.0   | 0      |
| 203 | Tensor<[24, 24, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | Done       | 1.0   | 0      |
| 204 | Tensor<[262, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1             | Done     | Done       | 1.0   | 0      |
| 205 | Tensor<[4, 12, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 206 | Tensor<[4, 12, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 207 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 208 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 209 | Tensor<[4, 16, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 210 | Tensor<[4, 16, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 211 | Tensor<[4, 16, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 212 | Tensor<[4, 16, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 213 | Tensor<[5, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | Done       | 1.0   | 0      |
| 214 | Tensor<[5, 1024, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 215 | Tensor<[5, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 216 | Tensor<[5, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 217 | Tensor<[50, 1, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | Done       | 1.0   | 0      |
| 218 | Tensor<[50, 1, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0           | Done     | Done       | 1.0   | 0      |
| 219 | Tensor<[50, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | 1.0   | 0      |
| 220 | Tensor<[50, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | 1.0   | 0      |
| 221 | Tensor<[6, 100, 1, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | Done       | 1.0   | 0      |
| 222 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 223 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 224 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 225 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 226 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 227 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 228 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | Done       | 1.0   | 0      |
| 229 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | Done       | 1.0   | 0      |
| 230 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | Done       | 1.0   | 0      |
| 231 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | 1.0   | 0      |
| 232 | Tensor<[8, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | Done       | 1.0   | 0      |
| 233 | Tensor<[8, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 234 | Tensor<[8, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | Done       | 1.0   | 0      |
| 235 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | Done       | 1.0   | 0      |
| 236 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | 1.0   | 0      |
| 237 | Tensor<[920, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | Done       | 1.0   | 0      |

