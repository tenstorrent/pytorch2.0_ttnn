### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                           | Unknown  | Fallback   | True  |
|   1 | Tensor<[0]> self = ?,<br>Tensor other = 0.5                                    | Unknown  | Fallback   | True  |
|   2 | Tensor<[0]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | True  |
|   3 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | True  |
|   4 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | True  |
|   5 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | True  |
|   6 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | True  |
|   7 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Unknown    | N/A   |
|   8 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Unknown    | N/A   |
|   9 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | True  |
|  10 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | True  |
|  11 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  | Done       | True  |
|  12 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | Done       | True  |
|  13 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Done       | True  |
|  14 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | True  |
|  15 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | True  |
|  16 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | True  |
|  17 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | True  |
|  18 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | True  |
|  19 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.9761904761904763           | Done     | Done       | True  |
|  20 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | True  |
|  21 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | True  |
|  22 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | True  |
|  23 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | True  |
|  24 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | True  |
|  25 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | True  |
|  26 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A   |
|  27 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A   |
|  28 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A   |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Done       | True  |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Unknown    | N/A   |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | True  |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Unknown    | N/A   |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Unknown    | N/A   |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Unknown    | N/A   |
|  35 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | True  |
|  36 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | True  |
|  37 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | Done       | True  |
|  38 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | Done       | True  |
|  39 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | Done       | True  |
|  40 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1                              | Unknown  | Done       | True  |
|  41 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | True  |
|  42 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | True  |
|  43 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | True  |
|  44 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | True  |
|  45 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | True  |
|  46 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | True  |
|  47 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.5625                       | Done     | Done       | True  |
|  48 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | True  |
|  49 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | True  |
|  50 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | True  |
|  51 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | True  |
|  52 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | True  |
|  53 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Done     | Done       | True  |
|  54 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Done       | True  |
|  55 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | True  |
|  56 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?             | Unknown  | Done       | True  |
|  57 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Done       | True  |
|  58 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125                          | Unknown  | Done       | True  |
|  59 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | True  |
|  60 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Done     | Done       | True  |
|  61 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Done     | Done       | True  |
|  62 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Done     | Done       | True  |
|  63 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | True  |
|  64 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | True  |
|  65 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | True  |
|  66 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Unknown  | Done       | True  |
|  67 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | True  |
|  68 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | True  |
|  69 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | True  |
|  70 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | True  |
|  71 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | True  |
|  72 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | True  |
|  73 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | True  |
|  74 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | True  |
|  75 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | True  |
|  76 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | True  |
|  77 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | True  |
|  78 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | True  |
|  79 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | Done       | True  |
|  80 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | True  |
|  81 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | True  |
|  82 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | True  |
|  83 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Done     | Done       | True  |
|  84 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Unknown  | Done       | True  |
|  85 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | True  |
|  86 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Unknown  | Done       | True  |
|  87 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | Done       | True  |
|  88 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | True  |
|  89 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | True  |
|  90 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | True  |
|  91 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | True  |
|  92 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | True  |
|  93 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | True  |
|  94 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | True  |
|  95 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Done     | Unknown    | N/A   |
|  96 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | True  |
|  97 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Unknown    | N/A   |
|  98 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Done     | Unknown    | N/A   |
|  99 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Done     | Done       | True  |
| 100 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | True  |
| 101 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | True  |
| 102 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | True  |
| 103 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | True  |
| 104 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | True  |
| 105 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | True  |
| 106 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125                        | Done     | Done       | True  |
| 107 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0                         | Done     | Done       | True  |
| 108 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | True  |
| 109 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | True  |
| 110 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | True  |
| 111 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?           | Done     | Done       | True  |
| 112 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1024]> other = ?                   | Done     | Done       | True  |
| 113 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | True  |
| 114 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?             | Done     | Done       | True  |
| 115 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Done       | True  |
| 116 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                   | Done     | Done       | True  |
| 117 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | True  |
| 118 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50258                               | Done     | Done       | True  |
| 119 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50259                               | Unknown  | Done       | True  |
| 120 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50359                               | Done     | Done       | True  |
| 121 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50363                               | Done     | Done       | True  |
| 122 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Done     | Done       | True  |
| 123 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Done     | Done       | True  |
| 124 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | True  |
| 125 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Done       | True  |
| 126 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Done     | Done       | True  |
| 127 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | True  |
| 128 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Unknown  | Done       | True  |
| 129 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | True  |
| 130 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | True  |
| 131 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | True  |
| 132 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Done     | Done       | True  |
| 133 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | True  |
| 134 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | True  |
| 135 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | True  |
| 136 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | True  |
| 137 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | True  |
| 138 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | True  |
| 139 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | True  |
| 140 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Done     | Done       | True  |
| 141 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | Done       | True  |
| 142 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | True  |
| 143 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | True  |
| 144 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | True  |
| 145 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | Done       | True  |
| 146 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | True  |
| 147 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | True  |
| 148 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Unknown  | Done       | True  |
| 149 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | True  |
| 150 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | True  |
| 151 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | True  |
| 152 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | True  |
| 153 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | True  |
| 154 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     | Done       | True  |
| 155 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Done     | Done       | True  |
| 156 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | Done       | True  |
| 157 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Done     | Done       | True  |
| 158 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | True  |
| 159 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?                | Unknown  | Done       | True  |
| 160 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?              | Unknown  | Done       | True  |
| 161 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | True  |
| 162 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | True  |
| 163 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | True  |
| 164 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | True  |
| 165 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | Done       | True  |
| 166 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | True  |
| 167 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | True  |
| 168 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | True  |
| 169 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | True  |
| 170 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | True  |
| 171 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Unknown    | N/A   |
| 172 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | True  |
| 173 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | True  |
| 174 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?         | Unknown  | Done       | True  |
| 175 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | True  |
| 176 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | True  |
| 177 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | True  |
| 178 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | True  |
| 179 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | True  |
| 180 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | True  |
| 181 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | True  |
| 182 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | True  |
| 183 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | Done       | True  |
| 184 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | True  |
| 185 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | Done       | True  |
| 186 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | True  |
| 187 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | True  |
| 188 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | True  |
| 189 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | True  |
| 190 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | True  |
| 191 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | True  |
| 192 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | True  |
| 193 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | None     | Fallback   | True  |
| 194 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | None     | Fallback   | True  |
| 195 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | None     | Fallback   | True  |
| 196 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Done     | Done       | True  |
| 197 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Done     | Done       | True  |
| 198 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Unknown  | Done       | True  |
| 199 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | True  |
| 200 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  | Done       | True  |
| 201 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | True  |
| 202 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | True  |
| 203 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | True  |
| 204 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  | Done       | True  |
| 205 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | True  |
| 206 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Done     | Done       | True  |
| 207 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | True  |
| 208 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | True  |
| 209 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | True  |
| 210 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Done     | Done       | True  |
| 211 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Done     | Done       | True  |
| 212 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | True  |
| 213 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | True  |
| 214 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Done     | Done       | True  |
| 215 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | True  |
| 216 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | None     | Fallback   | True  |
| 217 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | Done       | True  |
| 218 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | Done       | True  |
| 219 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | True  |
| 220 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  | Done       | True  |
| 221 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | Done       | True  |
| 222 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | Done       | True  |
| 223 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | None     | Fallback   | True  |
| 224 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | True  |
| 225 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | Done       | True  |
| 226 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | True  |
| 227 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  | Done       | True  |
| 228 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | Done       | True  |
| 229 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | Done       | True  |
| 230 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | None     | Fallback   | True  |
| 231 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | True  |
| 232 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | Done       | True  |
| 233 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | Done       | True  |
| 234 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | True  |
| 235 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | Done       | True  |
| 236 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | True  |
| 237 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | True  |
| 238 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | True  |
| 239 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | True  |
| 240 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | True  |
| 241 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | True  |
| 242 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | True  |
| 243 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | True  |
| 244 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | True  |
| 245 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | True  |
| 246 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?            | Unknown  | Fallback   | True  |
| 247 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | True  |
| 248 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | Done       | True  |
| 249 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | True  |
| 250 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | True  |
| 251 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | True  |
| 252 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | True  |
| 253 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | True  |
| 254 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | True  |
| 255 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | True  |
| 256 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | True  |
| 257 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | True  |
| 258 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | True  |
| 259 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Done       | True  |
| 260 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | Done       | True  |
| 261 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | Done       | True  |
| 262 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | Done       | True  |
| 263 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | True  |
| 264 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | True  |
| 265 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | True  |
| 266 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | True  |
| 267 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | True  |
| 268 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | True  |
| 269 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | True  |
| 270 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | True  |
| 271 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | True  |
| 272 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | True  |
| 273 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | True  |
| 274 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | True  |
| 275 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | True  |
| 276 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | True  |
| 277 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | True  |
| 278 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | True  |
| 279 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | True  |
| 280 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | True  |
| 281 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | True  |
| 282 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | True  |
| 283 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | True  |
| 284 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ?       | Unknown  | Unknown    | N/A   |
| 285 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ?       | Unknown  | Unknown    | N/A   |
| 286 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 1                             | Unknown  | Unknown    | N/A   |
| 287 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?       | Unknown  | Unknown    | N/A   |
| 288 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ?       | Unknown  | Unknown    | N/A   |
| 289 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ?       | Unknown  | Unknown    | N/A   |
| 290 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A   |
| 291 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Done     | Done       | True  |
| 292 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Done     | Done       | True  |
| 293 | Tensor<[100]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | True  |
| 294 | Tensor<[100]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | Fallback   | True  |
| 295 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | True  |
| 296 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Done     | Done       | True  |
| 297 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                   | Done     | Done       | True  |
| 298 | Tensor<[1066]> self = ?,<br>Tensor other = 0.600375234521576                   | Unknown  | Done       | True  |
| 299 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                                  | Done     | Done       | True  |
| 300 | Tensor<[128]> self = ?,<br>Tensor other = 0.125                                | Done     | Done       | True  |
| 301 | Tensor<[128]> self = ?,<br>Tensor other = 0.25                                 | Done     | Done       | True  |
| 302 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                                  | Done     | Done       | True  |
| 303 | Tensor<[128]> self = ?,<br>Tensor other = 1.0                                  | Done     | Done       | True  |
| 304 | Tensor<[128]> self = ?,<br>Tensor other = 2                                    | Done     | Done       | True  |
| 305 | Tensor<[12]> self = ?,<br>Tensor other = 32.0                                  | Done     | Done       | True  |
| 306 | Tensor<[12]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | True  |
| 307 | Tensor<[136]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Done       | True  |
| 308 | Tensor<[136]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | Fallback   | True  |
| 309 | Tensor<[13]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | True  |
| 310 | Tensor<[14]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 311 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Done     | Done       | True  |
| 312 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Done     | Done       | True  |
| 313 | Tensor<[16, 1]> self = ?,<br>Tensor<[1, 1, 32]> other = ?                      | None     | Fallback   | True  |
| 314 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | True  |
| 315 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | None     | Fallback   | True  |
| 316 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | True  |
| 317 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | None     | Fallback   | True  |
| 318 | Tensor<[160]> self = ?,<br>Tensor other = -9.210340371976184                   | Done     | Done       | True  |
| 319 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                                  | Done     | Done       | True  |
| 320 | Tensor<[16]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | True  |
| 321 | Tensor<[16]> self = ?,<br>Tensor other = 32.0                                  | Done     | Done       | True  |
| 322 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Unknown    | N/A   |
| 323 | Tensor<[17]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | True  |
| 324 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                                 | Unknown  | Done       | True  |
| 325 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A   |
| 326 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A   |
| 327 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A   |
| 328 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Done     | Done       | True  |
| 329 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Done     | Done       | True  |
| 330 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | None     | Fallback   | True  |
| 331 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | True  |
| 332 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Done     | Done       | True  |
| 333 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | None     | Fallback   | True  |
| 334 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | None     | Fallback   | True  |
| 335 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | None     | Fallback   | True  |
| 336 | Tensor<[23]> self = ?,<br>Tensor other = 31.304347826086957                    | Done     | Done       | True  |
| 337 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                                  | Done     | Done       | True  |
| 338 | Tensor<[25]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | True  |
| 339 | Tensor<[28]> self = ?,<br>Tensor other = 0.25                                  | Done     | Done       | True  |
| 340 | Tensor<[28]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 341 | Tensor<[300]> self = ?,<br>Tensor other = 1.6                                  | Done     | Done       | True  |
| 342 | Tensor<[300]> self = ?,<br>Tensor other = 2.1333333333333333                   | Done     | Done       | True  |
| 343 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | Fallback   | True  |
| 344 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 345 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                                  | Done     | Done       | True  |
| 346 | Tensor<[320]> self = ?,<br>Tensor other = 1.0                                  | Done     | Done       | True  |
| 347 | Tensor<[320]> self = ?,<br>Tensor other = 1.5                                  | Done     | Done       | True  |
| 348 | Tensor<[320]> self = ?,<br>Tensor other = 2.0                                  | Done     | Done       | True  |
| 349 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                     | Unknown  | Done       | True  |
| 350 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 351 | Tensor<[3234, 2]> self = ?,<br>Tensor<[2]> other = ?                           | Done     | Done       | True  |
| 352 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Done       | True  |
| 353 | Tensor<[32]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 354 | Tensor<[34]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | True  |
| 355 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | True  |
| 356 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | None     | Fallback   | True  |
| 357 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | True  |
| 358 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | None     | Fallback   | True  |
| 359 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 360 | Tensor<[40]> self = ?,<br>Tensor other = 32.0                                  | Done     | Done       | True  |
| 361 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                                  | Done     | Done       | True  |
| 362 | Tensor<[50]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | True  |
| 363 | Tensor<[50]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | True  |
| 364 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | True  |
| 365 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Done     | Done       | True  |
| 366 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Done     | Done       | True  |
| 367 | Tensor<[56]> self = ?,<br>Tensor other = 0.125                                 | Done     | Done       | True  |
| 368 | Tensor<[56]> self = ?,<br>Tensor other = 0.25                                  | Done     | Done       | True  |
| 369 | Tensor<[56]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 370 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 371 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | True  |
| 372 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | None     | Fallback   | True  |
| 373 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | True  |
| 374 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | None     | Fallback   | True  |
| 375 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                                  | Done     | Done       | True  |
| 376 | Tensor<[64]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 377 | Tensor<[68]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Done       | True  |
| 378 | Tensor<[68]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | True  |
| 379 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | True  |
| 380 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Done     | Done       | True  |
| 381 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                     | Done     | Done       | True  |
| 382 | Tensor<[7]> self = ?,<br>Tensor other = 0.42857142857142855                    | Done     | Done       | True  |
| 383 | Tensor<[7]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | True  |
| 384 | Tensor<[800]> self = ?,<br>Tensor other = 0.6                                  | Unknown  | Done       | True  |
| 385 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                                   | Done     | Done       | True  |
| 386 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                     | Unknown  | Done       | True  |
| 387 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 388 | Tensor<[8732, 2]> self = ?,<br>Tensor<[2]> other = ?                           | Done     | Done       | True  |
| 389 | Tensor<[8732]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Done       | True  |
| 390 | Tensor<[9]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | True  |
| 391 | Tensor<[]> self = ?,<br>Tensor<[0, 1]> other = ?                               | Unknown  | Fallback   | True  |
| 392 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                          | Unknown  | Fallback   | True  |
| 393 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | None     | Fallback   | True  |
| 394 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ?                         | Unknown  | Unknown    | N/A   |
| 395 | Tensor<[]> self = ?,<br>Tensor<[3234, 1]> other = ?                            | Unknown  | Fallback   | True  |
| 396 | Tensor<[]> self = ?,<br>Tensor<[8732, 1]> other = ?                            | Unknown  | Fallback   | True  |
| 397 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | None     | Fallback   | True  |
| 398 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A   |

