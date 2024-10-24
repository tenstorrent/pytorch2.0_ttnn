### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|----:|:-------------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   1 | Tensor<[0]> self = ?,<br>Tensor other = 0.5                                    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   2 | Tensor<[0]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   3 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | N/A                 | N/A          | N/A               | N/A                |
|   4 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | N/A                 | N/A          | N/A               | N/A                |
|   5 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | N/A                 | N/A          | N/A               | N/A                |
|   6 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | N/A                 | N/A          | N/A               | N/A                |
|   7 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   8 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   9 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  10 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  11 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  12 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | N/A                 | N/A          | N/A               | N/A                |
|  13 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  14 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  15 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  16 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  17 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  18 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  19 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.9761904761904763           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  20 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  21 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  22 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  23 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  24 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  25 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  26 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  27 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  28 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  35 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  36 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  37 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  38 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  39 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  40 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1                              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  41 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  42 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  43 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  44 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  45 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  46 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  47 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.5625                       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  48 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  49 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  50 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  51 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  52 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  53 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  54 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  55 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  56 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  57 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  58 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  59 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  60 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  61 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  62 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
|  63 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  64 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | N/A                 | N/A          | N/A               | N/A                |
|  65 | Tensor<[1, 1024, 2560]> self = ?,<br>Tensor<[1, 1024, 2560]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  66 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  67 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  68 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  69 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  70 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  71 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  72 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  73 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  74 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  75 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  76 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  77 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  78 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  79 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  80 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  81 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  82 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  83 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  84 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  85 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  86 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  87 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  88 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  89 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  90 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  91 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  92 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  93 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
|  94 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  95 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  96 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  97 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  98 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | N/A                 | N/A          | N/A               | N/A                |
|  99 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 100 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 101 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 102 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 103 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 104 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 105 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 106 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 107 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125                        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 108 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 109 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 110 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 111 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 112 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 113 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1024]> other = ?                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 114 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 115 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 116 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 117 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 118 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 119 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50258                               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 120 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50259                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 121 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50359                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 122 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50363                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 123 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 124 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 125 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 126 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 127 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 128 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 129 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 130 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 131 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 132 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 133 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 134 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 135 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 136 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 137 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 138 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 139 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 140 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 141 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 142 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 143 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 144 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 145 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 146 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 147 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 148 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 149 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 150 | Tensor<[1, 256, 5120]> self = ?,<br>Tensor<[1, 256, 5120]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 151 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 152 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 153 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 154 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 155 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 156 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 157 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 158 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 159 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 160 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 161 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 162 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?              | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 163 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 164 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 165 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 166 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 167 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 168 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 169 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 170 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 171 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 172 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 173 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 174 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 175 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 176 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 177 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 178 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 179 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 180 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 181 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 182 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 183 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 184 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 185 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 186 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 187 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 188 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 189 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 190 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 191 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 192 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 193 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 194 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 195 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | None     | N/A                 | N/A          | N/A               | N/A                |
| 196 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | None     | N/A                 | N/A          | N/A               | N/A                |
| 197 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | None     | N/A                 | N/A          | N/A               | N/A                |
| 198 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 199 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 200 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 201 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 202 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 203 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 204 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 205 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 206 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 207 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 208 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 209 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 210 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 211 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 212 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 213 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 214 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 215 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 216 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 217 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 218 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | None     | N/A                 | N/A          | N/A               | N/A                |
| 219 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 220 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 221 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 222 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 223 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 224 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 225 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | None     | N/A                 | N/A          | N/A               | N/A                |
| 226 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 227 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 228 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 229 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 230 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 231 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 232 | Tensor<[1, 64, 5120]> self = ?,<br>Tensor<[1, 64, 5120]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 233 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | None     | N/A                 | N/A          | N/A               | N/A                |
| 234 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 235 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 236 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 237 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 238 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 239 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 240 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 241 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 242 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 243 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 244 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 245 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 246 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 247 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 248 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 249 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 250 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 251 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 252 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 253 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 254 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 255 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 256 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 257 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 258 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 259 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 260 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 261 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 262 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 263 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 264 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 265 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 266 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 267 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 268 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 269 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 270 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 271 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 272 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 273 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 274 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 275 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 276 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 277 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 278 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 279 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 280 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 281 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 282 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | N/A                 | N/A          | N/A               | N/A                |
| 283 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 284 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 285 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 286 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 287 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 1                             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 288 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 289 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 290 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 291 | Tensor<[100]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 292 | Tensor<[100]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 293 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 294 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 295 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 296 | Tensor<[1066]> self = ?,<br>Tensor other = 0.600375234521576                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 297 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 298 | Tensor<[128]> self = ?,<br>Tensor other = 0.125                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 299 | Tensor<[128]> self = ?,<br>Tensor other = 0.25                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 300 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 301 | Tensor<[128]> self = ?,<br>Tensor other = 1.0                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 302 | Tensor<[128]> self = ?,<br>Tensor other = 2                                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 303 | Tensor<[12]> self = ?,<br>Tensor other = 32.0                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 304 | Tensor<[12]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 305 | Tensor<[136]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 306 | Tensor<[136]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 307 | Tensor<[13]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 308 | Tensor<[14]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 309 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Done     | N/A                 | N/A          | N/A               | N/A                |
| 310 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 311 | Tensor<[16, 1]> self = ?,<br>Tensor<[1, 1, 32]> other = ?                      | None     | N/A                 | N/A          | N/A               | N/A                |
| 312 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 313 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | None     | N/A                 | N/A          | N/A               | N/A                |
| 314 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 315 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | None     | N/A                 | N/A          | N/A               | N/A                |
| 316 | Tensor<[160]> self = ?,<br>Tensor other = -9.210340371976184                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 317 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 318 | Tensor<[16]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 319 | Tensor<[16]> self = ?,<br>Tensor other = 32.0                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 320 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 321 | Tensor<[17]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 322 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 323 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 324 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 325 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | None     | N/A                 | N/A          | N/A               | N/A                |
| 326 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 327 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 328 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | None     | N/A                 | N/A          | N/A               | N/A                |
| 329 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | None     | N/A                 | N/A          | N/A               | N/A                |
| 330 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | None     | N/A                 | N/A          | N/A               | N/A                |
| 331 | Tensor<[23]> self = ?,<br>Tensor other = 31.304347826086957                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 332 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 333 | Tensor<[25]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 334 | Tensor<[28]> self = ?,<br>Tensor other = 0.25                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 335 | Tensor<[28]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 336 | Tensor<[300]> self = ?,<br>Tensor other = 1.6                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 337 | Tensor<[300]> self = ?,<br>Tensor other = 2.1333333333333333                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 338 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 339 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 340 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 341 | Tensor<[320]> self = ?,<br>Tensor other = 1.0                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 342 | Tensor<[320]> self = ?,<br>Tensor other = 1.5                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 343 | Tensor<[320]> self = ?,<br>Tensor other = 2.0                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 344 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 345 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 346 | Tensor<[3234, 2]> self = ?,<br>Tensor<[2]> other = ?                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 347 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 348 | Tensor<[32]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 349 | Tensor<[34]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 350 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 351 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | None     | N/A                 | N/A          | N/A               | N/A                |
| 352 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 353 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | None     | N/A                 | N/A          | N/A               | N/A                |
| 354 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 355 | Tensor<[40]> self = ?,<br>Tensor other = 32.0                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 356 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 357 | Tensor<[50]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 358 | Tensor<[50]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 359 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 360 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 361 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 362 | Tensor<[56]> self = ?,<br>Tensor other = 0.125                                 | Done     | N/A                 | N/A          | N/A               | N/A                |
| 363 | Tensor<[56]> self = ?,<br>Tensor other = 0.25                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 364 | Tensor<[56]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 365 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 366 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 367 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | None     | N/A                 | N/A          | N/A               | N/A                |
| 368 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 369 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | None     | N/A                 | N/A          | N/A               | N/A                |
| 370 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                                  | Done     | N/A                 | N/A          | N/A               | N/A                |
| 371 | Tensor<[64]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 372 | Tensor<[68]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 373 | Tensor<[68]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 374 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 375 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 376 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 377 | Tensor<[7]> self = ?,<br>Tensor other = 0.42857142857142855                    | Done     | N/A                 | N/A          | N/A               | N/A                |
| 378 | Tensor<[7]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 379 | Tensor<[800]> self = ?,<br>Tensor other = 0.6                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 380 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                                   | Done     | N/A                 | N/A          | N/A               | N/A                |
| 381 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 382 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | N/A                 | N/A          | N/A               | N/A                |
| 383 | Tensor<[8732, 2]> self = ?,<br>Tensor<[2]> other = ?                           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 384 | Tensor<[8732]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 385 | Tensor<[9]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 386 | Tensor<[]> self = ?,<br>Tensor<[0, 1]> other = ?                               | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 387 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 388 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 389 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ?                         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 390 | Tensor<[]> self = ?,<br>Tensor<[3234, 1]> other = ?                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 391 | Tensor<[]> self = ?,<br>Tensor<[8732, 1]> other = ?                            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 392 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | None     | N/A                 | N/A          | N/A               | N/A                |
| 393 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | N/A                 | N/A          | N/A               | N/A                |

