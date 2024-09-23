### aten.mul.Tensor
|     | ATen Input Variations                                                            | Status   |
|----:|:---------------------------------------------------------------------------------|:---------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                             | Unknown  |
|   1 | Tensor<[0]> self = ?,<br>Tensor<> other = 0.5                                    | Unknown  |
|   2 | Tensor<[0]> self = ?,<br>Tensor<[]> other = ?                                    | Unknown  |
|   3 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38      | Unknown  |
|   4 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38      | Done     |
|   5 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38      | Done     |
|   6 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38      | Unknown  |
|   7 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38      | Unknown  |
|   8 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?               | Unknown  |
|   9 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38       | Unknown  |
|  10 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?                 | Unknown  |
|  11 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38     | Unknown  |
|  12 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38    | Unknown  |
|  13 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor<> other = -3.3895313892515355e+38     | Done     |
|  14 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38      | Done     |
|  15 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38       | Unknown  |
|  16 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?                 | Unknown  |
|  17 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = -0.75                        | Done     |
|  18 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 1.25                         | Done     |
|  19 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<> other = 1.9761904761904763           | Done     |
|  20 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?               | Done     |
|  21 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38       | Unknown  |
|  22 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38       | Unknown  |
|  23 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor<> other = -3.3895313892515355e+38       | Unknown  |
|  24 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38       | Done     |
|  25 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38       | Done     |
|  26 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38  | Unknown  |
|  27 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?       | Unknown  |
|  28 | Tensor<[1, 1, 1, s0]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38      | Unknown  |
|  29 | Tensor<[1, 1, 1, s0]> self = ?,<br>Tensor<[1, 1, 1, s0]> other = ?               | Unknown  |
|  30 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor<> other = -3.4028234663852886e+38 | Unknown  |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<> other = 0.03125                       | Unknown  |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<> other = 0.044715                      | Unknown  |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<> other = 0.125                         | Unknown  |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<> other = 0.5                           | Unknown  |
|  35 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<> other = 0.7978845608028654            | Unknown  |
|  36 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                 | Unknown  |
|  37 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                    | Unknown  |
|  38 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?              | Unknown  |
|  39 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor<> other = 0.448                     | Done     |
|  40 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor<> other = 0.45                      | Done     |
|  41 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor<> other = 0.458                     | Done     |
|  42 | Tensor<[1, 1, 256]> self = ?,<br>Tensor<> other = 1                              | Unknown  |
|  43 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<> other = 0.044715                      | Unknown  |
|  44 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<> other = 0.5                           | Unknown  |
|  45 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654            | Unknown  |
|  46 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?                 | Unknown  |
|  47 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = -0.75                        | Done     |
|  48 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 1.25                         | Done     |
|  49 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<> other = 1.5625                       | Done     |
|  50 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?               | Done     |
|  51 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<> other = 0.044715                      | Unknown  |
|  52 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<> other = 0.5                           | Unknown  |
|  53 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<> other = 0.7978845608028654            | Unknown  |
|  54 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?                 | Unknown  |
|  55 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor<> other = 10                        | Done     |
|  56 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<> other = 0.04419417382415922            | Unknown  |
|  57 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                     | Unknown  |
|  58 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?               | Unknown  |
|  59 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<> other = 0.03608439182435161            | Unknown  |
|  60 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<> other = 0.125                          | Unknown  |
|  61 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                     | Unknown  |
|  62 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                  | Unknown  |
|  63 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                   | Unknown  |
|  64 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                   | Unknown  |
|  65 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?           | Unknown  |
|  66 | Tensor<[1, 1024, 2560]> self = ?,<br>Tensor<[1, 1024, 2560]> other = ?           | Done     |
|  67 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Unknown  |
|  68 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Unknown  |
|  69 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?           | Done     |
|  70 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?           | Done     |
|  71 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?         | Done     |
|  72 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                           | Done     |
|  73 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<> other = 0.044715                     | Done     |
|  74 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<> other = 0.5                          | Done     |
|  75 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654           | Done     |
|  76 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?               | Done     |
|  77 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor<> other = 16                         | Unknown  |
|  78 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?           | Done     |
|  79 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?           | Done     |
|  80 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?           | Done     |
|  81 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?           | Done     |
|  82 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     |
|  83 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?         | Done     |
|  84 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?             | Unknown  |
|  85 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?         | Unknown  |
|  86 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?         | Unknown  |
|  87 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?         | Unknown  |
|  88 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?          | Unknown  |
|  89 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?         | Done     |
|  90 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<> other = 0.044715                     | Done     |
|  91 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<> other = 0.5                          | Done     |
|  92 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654           | Done     |
|  93 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?               | Done     |
|  94 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?           | Done     |
|  95 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?           | Done     |
|  96 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<> other = 0.044715                     | Unknown  |
|  97 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<> other = 0.5                          | Unknown  |
|  98 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<> other = 0.7978845608028654           | Unknown  |
|  99 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?               | Unknown  |
| 100 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                   | Unknown  |
| 101 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?           | Done     |
| 102 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?             | Done     |
| 103 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor<> other = 16                         | Unknown  |
| 104 | Tensor<[1, 160]> self = ?,<br>Tensor<> other = 1                                 | Done     |
| 105 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?         | Done     |
| 106 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<> other = 0.125                        | Done     |
| 107 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor<> other = 32.0                         | Done     |
| 108 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?            | Done     |
| 109 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?            | Done     |
| 110 | Tensor<[1, 1]> self = ?,<br>Tensor<> other = 0                                   | Unknown  |
| 111 | Tensor<[1, 1]> self = ?,<br>Tensor<> other = 16                                  | Unknown  |
| 112 | Tensor<[1, 1]> self = ?,<br>Tensor<> other = 50258                               | Done     |
| 113 | Tensor<[1, 1]> self = ?,<br>Tensor<> other = 50259                               | Unknown  |
| 114 | Tensor<[1, 1]> self = ?,<br>Tensor<> other = 50359                               | Unknown  |
| 115 | Tensor<[1, 1]> self = ?,<br>Tensor<> other = 50363                               | Unknown  |
| 116 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                           | Done     |
| 117 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?         | Done     |
| 118 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?           | Done     |
| 119 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?           | Unknown  |
| 120 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Unknown  |
| 121 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Unknown  |
| 122 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?           | Done     |
| 123 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?           | Done     |
| 124 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?           | Done     |
| 125 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<> other = 6.283185307179586              | Unknown  |
| 126 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?           | Done     |
| 127 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369         | Done     |
| 128 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<> other = 16                         | Unknown  |
| 129 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?                | Unknown  |
| 130 | Tensor<[1, 24, 768]> self = ?,<br>Tensor<> other = 0.125                         | Done     |
| 131 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?           | Done     |
| 132 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?         | Done     |
| 133 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?             | Unknown  |
| 134 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Unknown  |
| 135 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?               | Done     |
| 136 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                  | Done     |
| 137 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Unknown  |
| 138 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Unknown  |
| 139 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Unknown  |
| 140 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Unknown  |
| 141 | Tensor<[1, 256, 5120]> self = ?,<br>Tensor<[1, 256, 5120]> other = ?             | Done     |
| 142 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Done     |
| 143 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?          | Unknown  |
| 144 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?             | Done     |
| 145 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?         | Done     |
| 146 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<> other = 2                        | Unknown  |
| 147 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[1, 3, 16, 16, 2]> other = ?       | Unknown  |
| 148 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[]> other = ?                      | Unknown  |
| 149 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?                 | Done     |
| 150 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                    | Done     |
| 151 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<> other = 2                        | Unknown  |
| 152 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[1, 3, 32, 32, 2]> other = ?       | Unknown  |
| 153 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[]> other = ?                      | Unknown  |
| 154 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?                 | Done     |
| 155 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                    | Done     |
| 156 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<> other = 2                        | Unknown  |
| 157 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[1, 3, 64, 64, 2]> other = ?       | Unknown  |
| 158 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[]> other = ?                      | Unknown  |
| 159 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor<> other = 16                          | Unknown  |
| 160 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?                  | Unknown  |
| 161 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?                | Unknown  |
| 162 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?           | Done     |
| 163 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369         | Done     |
| 164 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<> other = 0.044715                     | Done     |
| 165 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<> other = 0.5                          | Done     |
| 166 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<> other = 0.79788456                   | Done     |
| 167 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?               | Done     |
| 168 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<> other = 16                         | Unknown  |
| 169 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?                | Unknown  |
| 170 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?           | Done     |
| 171 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                           | Done     |
| 172 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?           | Done     |
| 173 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?           | Done     |
| 174 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor<> other = 16                          | Unknown  |
| 175 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?           | Done     |
| 176 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?             | Done     |
| 177 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?           | Done     |
| 178 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<> other = 0.044715                     | Unknown  |
| 179 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<> other = 0.5                          | Unknown  |
| 180 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654           | Unknown  |
| 181 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?               | Unknown  |
| 182 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?             | Done     |
| 183 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?           | Done     |
| 184 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?           | Done     |
| 185 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?           | Done     |
| 186 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?           | Done     |
| 187 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     |
| 188 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?              | Unknown  |
| 189 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<> other = 0.044715                      | Unknown  |
| 190 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<> other = 0.5                           | Unknown  |
| 191 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<> other = 0.7978845608028654            | Unknown  |
| 192 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?                 | Unknown  |
| 193 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<> other = 1.702                        | Done     |
| 194 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?               | Done     |
| 195 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<> other = 0.125                         | Done     |
| 196 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?             | Unknown  |
| 197 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?           | Done     |
| 198 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  |
| 199 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Unknown  |
| 200 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Unknown  |
| 201 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Done     |
| 202 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Unknown  |
| 203 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Unknown  |
| 204 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?          | Unknown  |
| 205 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?           | Done     |
| 206 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?           | Done     |
| 207 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?             | Done     |
| 208 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor<> other = 0.125                        | Done     |
| 209 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                           | Done     |
| 210 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor<> other = 16                          | Unknown  |
| 211 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                           | Unknown  |
| 212 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?               | Unknown  |
| 213 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?             | Done     |
| 214 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?        | Done     |
| 215 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?                | Done     |
| 216 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                   | Done     |
| 217 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?           | Unknown  |
| 218 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?           | Unknown  |
| 219 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?                | Done     |
| 220 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                   | Done     |
| 221 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?            | Done     |
| 222 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                   | Done     |
| 223 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                      | Done     |
| 224 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?           | Unknown  |
| 225 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?           | Unknown  |
| 226 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?                | Done     |
| 227 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                   | Done     |
| 228 | Tensor<[1, 64, 5120]> self = ?,<br>Tensor<[1, 64, 5120]> other = ?               | Done     |
| 229 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?            | Done     |
| 230 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                   | Done     |
| 231 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                      | Done     |
| 232 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?           | Done     |
| 233 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?           | Done     |
| 234 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?           | Done     |
| 235 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?             | Done     |
| 236 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     |
| 237 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     |
| 238 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?             | Done     |
| 239 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?           | Done     |
| 240 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<> other = 0.044715                      | Unknown  |
| 241 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<> other = 0.5                           | Unknown  |
| 242 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654            | Unknown  |
| 243 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?                 | Unknown  |
| 244 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?              | Unknown  |
| 245 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?             | Done     |
| 246 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?             | Done     |
| 247 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?             | Done     |
| 248 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?             | Done     |
| 249 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     |
| 250 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?         | Done     |
| 251 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?           | Done     |
| 252 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?             | Done     |
| 253 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor<> other = 16                          | Unknown  |
| 254 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?             | Done     |
| 255 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?           | Done     |
| 256 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.044715                       | Done     |
| 257 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.5                            | Done     |
| 258 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<> other = 0.7978845608028654             | Done     |
| 259 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                   | Done     |
| 260 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.044715                     | Done     |
| 261 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.5                          | Done     |
| 262 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<> other = 0.7978845608028654           | Done     |
| 263 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?               | Done     |
| 264 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<> other = 0.044715                      | Done     |
| 265 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 266 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<> other = 0.7978845608028654            | Done     |
| 267 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?                 | Done     |
| 268 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<> other = 0.044715                      | Done     |
| 269 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 270 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<> other = 0.7978845608028654            | Done     |
| 271 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?                 | Done     |
| 272 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<> other = 0.044715                      | Done     |
| 273 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<> other = 0.5                           | Done     |
| 274 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<> other = 0.7978845608028654            | Done     |
| 275 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?                 | Done     |
| 276 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?             | Done     |
| 277 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?             | Done     |
| 278 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?             | Done     |
| 279 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?             | Done     |
| 280 | Tensor<[1, s0, 256]> self = ?,<br>Tensor<> other = 1                             | Unknown  |
| 281 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?                 | Unknown  |
| 282 | Tensor<[10, 10]> self = ?,<br>Tensor<> other = 16                                | Unknown  |
| 283 | Tensor<[10, 10]> self = ?,<br>Tensor<> other = 8                                 | Unknown  |
| 284 | Tensor<[100]> self = ?,<br>Tensor<> other = 0.5                                  | Unknown  |
| 285 | Tensor<[100]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  |
| 286 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                       | Unknown  |
| 287 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                      | Unknown  |
| 288 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                     | Done     |
| 289 | Tensor<[1066]> self = ?,<br>Tensor<> other = 0.600375234521576                   | Unknown  |
| 290 | Tensor<[120]> self = ?,<br>Tensor<> other = 0.5                                  | Done     |
| 291 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.125                                | Done     |
| 292 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.25                                 | Done     |
| 293 | Tensor<[128]> self = ?,<br>Tensor<> other = 0.5                                  | Done     |
| 294 | Tensor<[128]> self = ?,<br>Tensor<> other = 1.0                                  | Done     |
| 295 | Tensor<[128]> self = ?,<br>Tensor<> other = 2                                    | Unknown  |
| 296 | Tensor<[12]> self = ?,<br>Tensor<> other = 32.0                                  | Unknown  |
| 297 | Tensor<[12]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  |
| 298 | Tensor<[136]> self = ?,<br>Tensor<> other = 0.5                                  | Unknown  |
| 299 | Tensor<[136]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  |
| 300 | Tensor<[13]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  |
| 301 | Tensor<[14]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 302 | Tensor<[15, 15]> self = ?,<br>Tensor<> other = 16                                | Unknown  |
| 303 | Tensor<[15, 15]> self = ?,<br>Tensor<> other = 8                                 | Unknown  |
| 304 | Tensor<[16, 1]> self = ?,<br>Tensor<[1, 1, 32]> other = ?                        | Done     |
| 305 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369         | Done     |
| 306 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?                 | Unknown  |
| 307 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369         | Done     |
| 308 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?                 | Unknown  |
| 309 | Tensor<[160]> self = ?,<br>Tensor<> other = -9.210340371976184                   | Done     |
| 310 | Tensor<[160]> self = ?,<br>Tensor<> other = 0.5                                  | Done     |
| 311 | Tensor<[16]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 312 | Tensor<[16]> self = ?,<br>Tensor<> other = 32.0                                  | Unknown  |
| 313 | Tensor<[17, 17]> self = ?,<br>Tensor<> other = 16                                | Unknown  |
| 314 | Tensor<[17]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  |
| 315 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                                   | Unknown  |
| 316 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                                 | Done     |
| 317 | Tensor<[2, 2]> self = ?,<br>Tensor<> other = 16                                  | Unknown  |
| 318 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<> other = 1.702                         | Done     |
| 319 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?                 | Done     |
| 320 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<> other = 0.125                          | Done     |
| 321 | Tensor<[23]> self = ?,<br>Tensor<> other = 31.304347826086957                    | Unknown  |
| 322 | Tensor<[240]> self = ?,<br>Tensor<> other = 0.5                                  | Done     |
| 323 | Tensor<[25]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  |
| 324 | Tensor<[28]> self = ?,<br>Tensor<> other = 0.25                                  | Done     |
| 325 | Tensor<[28]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 326 | Tensor<[300]> self = ?,<br>Tensor<> other = 1.6                                  | Done     |
| 327 | Tensor<[300]> self = ?,<br>Tensor<> other = 2.1333333333333333                   | Done     |
| 328 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  |
| 329 | Tensor<[30]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 330 | Tensor<[320]> self = ?,<br>Tensor<> other = 0.5                                  | Done     |
| 331 | Tensor<[320]> self = ?,<br>Tensor<> other = 1.0                                  | Done     |
| 332 | Tensor<[320]> self = ?,<br>Tensor<> other = 1.5                                  | Done     |
| 333 | Tensor<[320]> self = ?,<br>Tensor<> other = 2.0                                  | Done     |
| 334 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                       | Unknown  |
| 335 | Tensor<[3234, 2]> self = ?,<br>Tensor<> other = 0.5                              | Done     |
| 336 | Tensor<[3234, 2]> self = ?,<br>Tensor<[2]> other = ?                             | Done     |
| 337 | Tensor<[3234]> self = ?,<br>Tensor<> other = 0.5                                 | Unknown  |
| 338 | Tensor<[32]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 339 | Tensor<[34]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  |
| 340 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369         | Done     |
| 341 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?                | Unknown  |
| 342 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369         | Done     |
| 343 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?                | Unknown  |
| 344 | Tensor<[40]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 345 | Tensor<[40]> self = ?,<br>Tensor<> other = 32.0                                  | Unknown  |
| 346 | Tensor<[480]> self = ?,<br>Tensor<> other = 0.5                                  | Done     |
| 347 | Tensor<[50]> self = ?,<br>Tensor<> other = 0.5                                   | Unknown  |
| 348 | Tensor<[50]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  |
| 349 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                         | Unknown  |
| 350 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                        | Unknown  |
| 351 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                        | Unknown  |
| 352 | Tensor<[56]> self = ?,<br>Tensor<> other = 0.125                                 | Done     |
| 353 | Tensor<[56]> self = ?,<br>Tensor<> other = 0.25                                  | Done     |
| 354 | Tensor<[56]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 355 | Tensor<[60]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 356 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369         | Done     |
| 357 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?                 | Unknown  |
| 358 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor<> other = 0.1767766952966369         | Done     |
| 359 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?                 | Unknown  |
| 360 | Tensor<[640]> self = ?,<br>Tensor<> other = 0.5                                  | Done     |
| 361 | Tensor<[64]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 362 | Tensor<[68]> self = ?,<br>Tensor<> other = 0.5                                   | Unknown  |
| 363 | Tensor<[68]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  |
| 364 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                         | Unknown  |
| 365 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                        | Unknown  |
| 366 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                       | Done     |
| 367 | Tensor<[7]> self = ?,<br>Tensor<> other = 0.42857142857142855                    | Done     |
| 368 | Tensor<[7]> self = ?,<br>Tensor<[]> other = ?                                    | Unknown  |
| 369 | Tensor<[800]> self = ?,<br>Tensor<> other = 0.6                                  | Unknown  |
| 370 | Tensor<[80]> self = ?,<br>Tensor<> other = 0.5                                   | Done     |
| 371 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                       | Unknown  |
| 372 | Tensor<[8732, 2]> self = ?,<br>Tensor<> other = 0.5                              | Done     |
| 373 | Tensor<[8732, 2]> self = ?,<br>Tensor<[2]> other = ?                             | Done     |
| 374 | Tensor<[8732]> self = ?,<br>Tensor<> other = 0.5                                 | Unknown  |
| 375 | Tensor<[9]> self = ?,<br>Tensor<[]> other = ?                                    | Unknown  |
| 376 | Tensor<[]> self = ?,<br>Tensor<[0, 1]> other = ?                                 | Unknown  |
| 377 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                            | Unknown  |
| 378 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                           | Done     |
| 379 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ?                           | Unknown  |
| 380 | Tensor<[]> self = ?,<br>Tensor<[3234, 1]> other = ?                              | Unknown  |
| 381 | Tensor<[]> self = ?,<br>Tensor<[8732, 1]> other = ?                              | Unknown  |
| 382 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor<> other = 16                        | Unknown  |

