### aten.mul.Tensor
|     | ATen Input Variations                                                       | Status   | Isolated   | PCC                | Host   |
|----:|:----------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                            | Done     | Unknown    | N/A                | N/A    |
|   1 | Tensor self = ?,<br>Tensor<[1, 7]> other = ?                                | Done     | Unknown    | N/A                | N/A    |
|   2 | Tensor self = ?,<br>Tensor<[3234, 1]> other = ?                             | Done     | Unknown    | N/A                | N/A    |
|   3 | Tensor self = ?,<br>Tensor<[8732, 1]> other = ?                             | Done     | Unknown    | N/A                | N/A    |
|   4 | Tensor self = ?,<br>Tensor<[]> other = ?                                    | Unknown  | Unknown    | N/A                | N/A    |
|   5 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38   | Unknown  | Done       | 0.999996347457022  | 0      |
|   6 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38   | Unknown  | Done       | 0.9999981054487544 | 0      |
|   7 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                | N/A    |
|   8 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Done     | Done       | 0.9999954391096871 | 0      |
|   9 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                    | Unknown  | Done       | 1.0                | 0      |
|  10 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                   | Unknown  | Done       | 0.9999941958840586 | 0      |
|  11 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                      | Unknown  | Done       | 1.0                | 0      |
|  12 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                        | Unknown  | Done       | 1.0                | 0      |
|  13 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654         | Unknown  | Done       | 0.9999976506375162 | 0      |
|  14 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?            | Unknown  | Done       | 0.9999959334157156 | 0      |
|  15 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?               | Unknown  | Done       | 0.9999963590761234 | 0      |
|  16 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?         | Unknown  | Done       | 0.9999956487312514 | 0      |
|  17 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                  | Done     | Done       | 0.9999951240758831 | 0      |
|  18 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                   | Done     | Done       | 0.9999955249639422 | 0      |
|  19 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                  | Done     | Done       | 0.9999966084523023 | 0      |
|  20 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1                           | Unknown  | Unknown    | N/A                | N/A    |
|  21 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                   | Unknown  | Done       | 0.9999956759206838 | 0      |
|  22 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                        | Unknown  | Done       | 1.0                | 0      |
|  23 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654         | Unknown  | Done       | 0.9999972274305036 | 0      |
|  24 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?            | Unknown  | Done       | 0.99999603426265   | 0      |
|  25 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                   | Unknown  | Done       | 0.9999952124271347 | 0      |
|  26 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                        | Unknown  | Done       | 1.0                | 0      |
|  27 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654         | Unknown  | Done       | 0.9999968453602969 | 0      |
|  28 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?            | Unknown  | Done       | 0.9999959247960075 | 0      |
|  29 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                     | Done     | Done       | 0.9999985561951461 | 0      |
|  30 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922         | Unknown  | Done       | 0.9999950911188739 | 0      |
|  31 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Unknown  | Done       | 0.9999998877312276 | 0      |
|  32 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?          | Unknown  | Unknown    | N/A                | N/A    |
|  33 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161         | Unknown  | Done       | 0.9999960678017522 | 0      |
|  34 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125                       | Unknown  | Unknown    | N/A                | N/A    |
|  35 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Unknown  | Done       | 0.9999968802032603 | 0      |
|  36 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?             | Unknown  | Done       | 0.9999961307336127 | 0      |
|  37 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?              | Unknown  | Done       | 0.9999953279907786 | 0      |
|  38 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?              | Unknown  | Done       | 0.9999951847103749 | 0      |
|  39 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Removed  | Done       | 0.9999953839284251 | 0      |
|  40 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?             | Done     | Done       | 0.9999962803496856 | 0      |
|  41 | Tensor<[1, 1024, 2560]> self = ?,<br>Tensor<[1, 1024, 2560]> other = ?      | Done     | Unknown    | N/A                | N/A    |
|  42 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?    | Done     | Done       | 0.999995953891233  | 0      |
|  43 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?      | Done     | Done       | 0.9999959388523906 | 0      |
|  44 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?      | Done     | Done       | 0.9999958430931196 | 0      |
|  45 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?      | Done     | Done       | 0.9999958460874421 | 0      |
|  46 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?    | Done     | Done       | 0.9999959532481526 | 0      |
|  47 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                      | Done     | Done       | 0.9999999955903472 | 0      |
|  48 | Tensor<[1, 10]> self = ?,<br>Tensor<[]> other = ?                           | Unknown  | Unknown    | N/A                | N/A    |
|  49 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                  | Done     | Done       | 0.9999953438542184 | 0      |
|  50 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                       | Done     | Done       | 1.0                | 0      |
|  51 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654        | Done     | Done       | 0.9999972279087104 | 0      |
|  52 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?          | Done     | Done       | 0.9999961702713334 | 0      |
|  53 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                      | Removed  | Done       | 1.0                | 0      |
|  54 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?      | Done     | Done       | 0.9999955312803298 | 0      |
|  55 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?      | Done     | Done       | 0.9999961615648014 | 0      |
|  56 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?      | Done     | Done       | 0.9999963426911054 | 0      |
|  57 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?      | Done     | Done       | 0.9999965909327604 | 0      |
|  58 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?    | Done     | Done       | 0.999995926976232  | 0      |
|  59 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?    | Done     | Done       | 0.9999959303994923 | 0      |
|  60 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Removed  | Done       | 0.9999980228388967 | 0      |
|  61 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?    | Done     | Done       | 0.9999959201736024 | 0      |
|  62 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?     | Done     | Done       | 0.9999959699862037 | 0      |
|  63 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?    | Done     | Done       | 0.9999958751969757 | 0      |
|  64 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                  | Done     | Done       | 0.9999953953697012 | 0      |
|  65 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                       | Done     | Done       | 1.0                | 0      |
|  66 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654        | Done     | Done       | 0.999997285116006  | 0      |
|  67 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?          | Done     | Done       | 0.999995883813336  | 0      |
|  68 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?      | Done     | Done       | 0.9999956906829566 | 0      |
|  69 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?      | Done     | Done       | 0.9999960856503228 | 0      |
|  70 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                  | Unknown  | Done       | 0.9999953936481457 | 0      |
|  71 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                       | Unknown  | Done       | 1.0                | 0      |
|  72 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654        | Unknown  | Done       | 0.9999971863061885 | 0      |
|  73 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?          | Unknown  | Done       | 0.9999961433535078 | 0      |
|  74 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?              | Unknown  | Done       | 0.9999954832726955 | 0      |
|  75 | Tensor<[1, 1500, 768]> self = ?,<br>Tensor other = 0.125                    | Unknown  | Unknown    | N/A                | N/A    |
|  76 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?      | Done     | Done       | 0.9999960554589187 | 0      |
|  77 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?        | Done     | Done       | 0.9999957021611684 | 0      |
|  78 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                      | Removed  | Done       | 1.0                | 0      |
|  79 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                              | Done     | Done       | 1.0                | 0      |
|  80 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?             | Done     | Done       | 0.9999955888107671 | 0      |
|  81 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?    | Done     | Done       | 0.9999959375499834 | 0      |
|  82 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[32, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
|  83 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[42]> other = ?                | Done     | Unknown    | N/A                | N/A    |
|  84 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                               | Unknown  | Done       | 1.0                | 0      |
|  85 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                      | Done     | Done       | 0.9999949620654826 | 0      |
|  86 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 1]> other = ?                        | Done     | Unknown    | N/A                | N/A    |
|  87 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?    | Done     | Done       | 0.9999959047146693 | 0      |
|  88 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?      | Done     | Done       | 0.9999960702002116 | 0      |
|  89 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?      | Removed  | Done       | 0.9999955331653405 | 0      |
|  90 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?    | Done     | Done       | 0.9999959003659639 | 0      |
|  91 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?      | Done     | Done       | 0.9999962211595584 | 0      |
|  92 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?      | Done     | Done       | 0.9999960045260567 | 0      |
|  93 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?      | Done     | Done       | 0.9999958111487793 | 0      |
|  94 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586           | Done     | Done       | 0.9999960716043853 | 0      |
|  95 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?      | Done     | Done       | 0.9999961510422675 | 0      |
|  96 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369      | Done     | Done       | 0.9999959261665237 | 0      |
|  97 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                      | Removed  | Done       | 1.0                | 0      |
|  98 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?           | Done     | Done       | 0.9999962390378123 | 0      |
|  99 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                      | Unknown  | Done       | 1.0                | 0      |
| 100 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?      | Done     | Done       | 0.9999957290640576 | 0      |
| 101 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?    | Done     | Done       | 0.9999959876644391 | 0      |
| 102 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Removed  | Done       | 0.9999975412779671 | 0      |
| 103 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?                    | Done     | Unknown    | N/A                | N/A    |
| 104 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?          | Done     | Done       | 0.999995559308509  | 0      |
| 105 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?             | Done     | Done       | 0.9999959824728232 | 0      |
| 106 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?    | Done     | Done       | 0.9999961513954033 | 0      |
| 107 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?              | Done     | Done       | 0.9999956954429947 | 0      |
| 108 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999959680591773 | 0      |
| 109 | Tensor<[1, 256, 5120]> self = ?,<br>Tensor<[1, 256, 5120]> other = ?        | Done     | Unknown    | N/A                | N/A    |
| 110 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?      | Done     | Done       | 0.9999959668048065 | 0      |
| 111 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?    | Done     | Done       | 0.9999959574674507 | 0      |
| 112 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?     | Done     | Done       | 0.9999960837002643 | 0      |
| 113 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[768]> other = ?                  | Done     | Unknown    | N/A                | N/A    |
| 114 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?        | Done     | Done       | 0.999996038433884  | 0      |
| 115 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?    | Done     | Done       | 0.9999960172637383 | 0      |
| 116 | Tensor<[1, 2]> self = ?,<br>Tensor other = 16                               | Unknown  | Unknown    | N/A                | N/A    |
| 117 | Tensor<[1, 2]> self = ?,<br>Tensor<[1, 2]> other = ?                        | Unknown  | Unknown    | N/A                | N/A    |
| 118 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor other = 2                     | Unknown  | Unknown    | N/A                | N/A    |
| 119 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[1, 3, 16, 16, 2]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 120 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[]> other = ?                 | Unknown  | Unknown    | N/A                | N/A    |
| 121 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor other = ?                      | Done     | Unknown    | N/A                | N/A    |
| 122 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor other = 2                     | Unknown  | Unknown    | N/A                | N/A    |
| 123 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[1, 3, 32, 32, 2]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 124 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[]> other = ?                 | Unknown  | Unknown    | N/A                | N/A    |
| 125 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                      | Done     | Unknown    | N/A                | N/A    |
| 126 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor other = 2                     | Unknown  | Unknown    | N/A                | N/A    |
| 127 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[1, 3, 64, 64, 2]> other = ?  | Unknown  | Unknown    | N/A                | N/A    |
| 128 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[]> other = ?                 | Unknown  | Unknown    | N/A                | N/A    |
| 129 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                       | Removed  | Done       | 1.0                | 0      |
| 130 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?      | Done     | Done       | 0.9999958816703884 | 0      |
| 131 | Tensor<[1, 32, 11008]> self = ?,<br>Tensor<[1, 32, 11008]> other = ?        | Unknown  | Unknown    | N/A                | N/A    |
| 132 | Tensor<[1, 32, 128]> self = ?,<br>Tensor other = 1.0                        | Unknown  | Unknown    | N/A                | N/A    |
| 133 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 1, 32, 128]> other = ?     | Unknown  | Unknown    | N/A                | N/A    |
| 134 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 1]> other = ?             | Unknown  | Unknown    | N/A                | N/A    |
| 135 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369      | Done     | Done       | 0.9999959318962952 | 0      |
| 136 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                  | Done     | Done       | 0.999995383906306  | 0      |
| 137 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                       | Done     | Done       | 1.0                | 0      |
| 138 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                | Done     | Done       | 0.9999972239832209 | 0      |
| 139 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?          | Done     | Done       | 0.9999959580616806 | 0      |
| 140 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                      | Removed  | Done       | 1.0                | 0      |
| 141 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?           | Done     | Done       | 0.9999968108933264 | 0      |
| 142 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?      | Done     | Done       | 0.9999957825146825 | 0      |
| 143 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                      | Done     | Done       | 0.999997534582049  | 0      |
| 144 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?      | Done     | Done       | 0.9999959827552367 | 0      |
| 145 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?      | Done     | Done       | 0.9999958764361899 | 0      |
| 146 | Tensor<[1, 3]> self = ?,<br>Tensor<[1, 3]> other = ?                        | Unknown  | Unknown    | N/A                | N/A    |
| 147 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                       | Removed  | Done       | 1.0                | 0      |
| 148 | Tensor<[1, 4, 768]> self = ?,<br>Tensor other = 0.125                       | Unknown  | Unknown    | N/A                | N/A    |
| 149 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?      | Done     | Done       | 0.9999959613130432 | 0      |
| 150 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?              | Done     | Done       | 0.9999959330556993 | 0      |
| 151 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?        | Done     | Done       | 0.9999958674375373 | 0      |
| 152 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?      | Done     | Done       | 0.999995958895567  | 0      |
| 153 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                  | Unknown  | Done       | 0.9999953327790129 | 0      |
| 154 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                       | Unknown  | Done       | 1.0                | 0      |
| 155 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654        | Unknown  | Done       | 0.9999971965477399 | 0      |
| 156 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?          | Unknown  | Done       | 0.9999959188369137 | 0      |
| 157 | Tensor<[1, 45]> self = ?,<br>Tensor<[]> other = ?                           | Unknown  | Unknown    | N/A                | N/A    |
| 158 | Tensor<[1, 46]> self = ?,<br>Tensor<[1, 46]> other = ?                      | Unknown  | Unknown    | N/A                | N/A    |
| 159 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?        | Done     | Done       | 0.9999956842469598 | 0      |
| 160 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?      | Done     | Done       | 0.9999960730829529 | 0      |
| 161 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?      | Done     | Done       | 0.9999961207086577 | 0      |
| 162 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?      | Done     | Done       | 0.9999959508572852 | 0      |
| 163 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?      | Done     | Done       | 0.9999958479328395 | 0      |
| 164 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?    | Done     | Done       | 0.9999959100261041 | 0      |
| 165 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?         | Unknown  | Done       | 0.999996444730068  | 0      |
| 166 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                   | Unknown  | Done       | 0.9999955865594777 | 0      |
| 167 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                        | Unknown  | Done       | 1.0                | 0      |
| 168 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654         | Unknown  | Done       | 0.9999971305075652 | 0      |
| 169 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?            | Unknown  | Done       | 0.9999960476081742 | 0      |
| 170 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                     | Done     | Done       | 0.999995978171268  | 0      |
| 171 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?          | Done     | Done       | 0.9999959526485594 | 0      |
| 172 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Removed  | Done       | 0.9999976736953731 | 0      |
| 173 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?      | Done     | Done       | 0.9999958828963726 | 0      |
| 174 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | Done       | 0.9999959793416728 | 0      |
| 175 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | Done       | 0.9999959969812535 | 0      |
| 176 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?    | Done     | Done       | 0.9999959312132564 | 0      |
| 177 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?      | Done     | Done       | 0.9999959667572734 | 0      |
| 178 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?     | Done     | Done       | 0.9999960716929772 | 0      |
| 179 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                    | Done     | Done       | 0.9999960530220504 | 0      |
| 180 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?      | Done     | Done       | 0.9999960498011368 | 0      |
| 181 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?      | Done     | Done       | 0.9999958447213053 | 0      |
| 182 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?        | Done     | Done       | 0.9999960374729799 | 0      |
| 183 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                     | Unknown  | Done       | 1.0                | 0      |
| 184 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                       | Removed  | Done       | 1.0                | 0      |
| 185 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                      | Unknown  | Done       | 0.9999976357827657 | 0      |
| 186 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?          | Removed  | Done       | 0.9999977533164081 | 0      |
| 187 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?        | Done     | Done       | 0.9999958882530565 | 0      |
| 188 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 189 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?   | Done     | Done       | 0.9999959926032539 | 0      |
| 190 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?      | Done     | Done       | 0.9999959819042903 | 0      |
| 191 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 192 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                | N/A    |
| 193 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?       | Done     | Done       | 0.9999960303840459 | 0      |
| 194 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?      | Done     | Done       | 0.9999966809509533 | 0      |
| 195 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                     | Done     | Unknown    | N/A                | N/A    |
| 196 | Tensor<[1, 64, 5120]> self = ?,<br>Tensor<[1, 64, 5120]> other = ?          | Done     | Unknown    | N/A                | N/A    |
| 197 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                | N/A    |
| 198 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?       | Done     | Done       | 0.9999959415083316 | 0      |
| 199 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?      | Done     | Done       | 0.9999958403064905 | 0      |
| 200 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?      | Done     | Done       | 0.9999961132985473 | 0      |
| 201 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?      | Done     | Done       | 0.9999958623575356 | 0      |
| 202 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?        | Done     | Done       | 0.999995823301574  | 0      |
| 203 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?      | Done     | Done       | 0.9999960286376044 | 0      |
| 204 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?    | Done     | Done       | 0.9999960381822409 | 0      |
| 205 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?        | Done     | Done       | 0.9999960012343885 | 0      |
| 206 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?        | Done     | Done       | 0.9999958965773394 | 0      |
| 207 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?      | Done     | Done       | 0.9999959121347887 | 0      |
| 208 | Tensor<[1, 6]> self = ?,<br>Tensor<[1, 6]> other = ?                        | Unknown  | Unknown    | N/A                | N/A    |
| 209 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                   | Done     | Done       | 0.9999952996894373 | 0      |
| 210 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                        | Done     | Done       | 1.0                | 0      |
| 211 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654         | Done     | Done       | 0.9999972097789044 | 0      |
| 212 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?            | Done     | Done       | 0.9999961414026098 | 0      |
| 213 | Tensor<[1, 7, 64]> self = ?,<br>Tensor other = 1.0                          | Unknown  | Unknown    | N/A                | N/A    |
| 214 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?         | Unknown  | Unknown    | N/A                | N/A    |
| 215 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?        | Done     | Done       | 0.999995956492517  | 0      |
| 216 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?        | Done     | Done       | 0.99999567569394   | 0      |
| 217 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?        | Done     | Done       | 0.9999957952825775 | 0      |
| 218 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?        | Done     | Done       | 0.9999952301688935 | 0      |
| 219 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?      | Done     | Done       | 0.9999959264604481 | 0      |
| 220 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?      | Done     | Done       | 0.9999959227224513 | 0      |
| 221 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?    | Done     | Done       | 0.9999959386407185 | 0      |
| 222 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?      | Done     | Done       | 0.9999959031583133 | 0      |
| 223 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?    | Done     | Done       | 0.9999960550659011 | 0      |
| 224 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[16, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
| 225 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[16]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 226 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?        | Done     | Done       | 0.9999958110279047 | 0      |
| 227 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                       | Removed  | Done       | 1.0                | 0      |
| 228 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?        | Done     | Done       | 0.9999958583416495 | 0      |
| 229 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?      | Done     | Done       | 0.9999959577189118 | 0      |
| 230 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                    | Done     | Done       | 0.999995220350184  | 0      |
| 231 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                         | Done     | Done       | 1.0                | 0      |
| 232 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654          | Done     | Done       | 0.9999974579217857 | 0      |
| 233 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?              | Done     | Done       | 0.9999962940244393 | 0      |
| 234 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                  | Done     | Done       | 0.9999953795003993 | 0      |
| 235 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                       | Done     | Done       | 1.0                | 0      |
| 236 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654        | Done     | Done       | 0.9999972276336234 | 0      |
| 237 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?          | Done     | Done       | 0.999995922963559  | 0      |
| 238 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                   | Done     | Done       | 0.9999952906622618 | 0      |
| 239 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                        | Done     | Done       | 1.0                | 0      |
| 240 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654         | Done     | Done       | 0.9999971499888298 | 0      |
| 241 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?            | Done     | Done       | 0.999996025386161  | 0      |
| 242 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                   | Done     | Done       | 0.999995406907189  | 0      |
| 243 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                        | Done     | Done       | 1.0                | 0      |
| 244 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654         | Done     | Done       | 0.9999971690323124 | 0      |
| 245 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?            | Done     | Done       | 0.9999961342098003 | 0      |
| 246 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                   | Done     | Done       | 0.9999953418247561 | 0      |
| 247 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                        | Done     | Done       | 1.0                | 0      |
| 248 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654         | Done     | Done       | 0.9999972715343857 | 0      |
| 249 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?            | Done     | Done       | 0.9999958244189144 | 0      |
| 250 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?        | Done     | Done       | 0.999995943374178  | 0      |
| 251 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?        | Done     | Done       | 0.9999961369949348 | 0      |
| 252 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?        | Done     | Done       | 0.9999958790504332 | 0      |
| 253 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?        | Done     | Done       | 0.9999959202859731 | 0      |
| 254 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor other = 16                          | Unknown  | Unknown    | N/A                | N/A    |
| 255 | Tensor<[1, s0 + 1]> self = ?,<br>Tensor<[1, s0 + 1]> other = ?              | Unknown  | Unknown    | N/A                | N/A    |
| 256 | Tensor<[1, s0 + 2]> self = ?,<br>Tensor<[1, s0 + 2]> other = ?              | Unknown  | Unknown    | N/A                | N/A    |
| 257 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 1                          | Unknown  | Unknown    | N/A                | N/A    |
| 258 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                             | Unknown  | Done       | 1.0                | 0      |
| 259 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                              | Unknown  | Done       | 1.0                | 0      |
| 260 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                  | Unknown  | Done       | 0.9999960522121397 | 0      |
| 261 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                 | Unknown  | Done       | 0.9999959719890609 | 0      |
| 262 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                             | Unknown  | Done       | 1.0                | 0      |
| 263 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                              | Unknown  | Done       | 1.0                | 0      |
| 264 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369      | Done     | Done       | 0.9999958997520273 | 0      |
| 265 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?            | Done     | Done       | 0.999996486655306  | 0      |
| 266 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369      | Done     | Done       | 0.9999958065891831 | 0      |
| 267 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?            | Done     | Done       | 0.9999977716673851 | 0      |
| 268 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -0.4570457994644658          | Done     | Unknown    | N/A                | N/A    |
| 269 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -0.5900435899266435          | Done     | Unknown    | N/A                | N/A    |
| 270 | Tensor<[16384, 1]> self = ?,<br>Tensor other = -1.0925484305920792          | Done     | Unknown    | N/A                | N/A    |
| 271 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.31539156525252005          | Done     | Unknown    | N/A                | N/A    |
| 272 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.3731763325901154           | Done     | Unknown    | N/A                | N/A    |
| 273 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.4886025119029199           | Done     | Unknown    | N/A                | N/A    |
| 274 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 0.5462742152960396           | Done     | Unknown    | N/A                | N/A    |
| 275 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.0                          | Done     | Unknown    | N/A                | N/A    |
| 276 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.0925484305920792           | Done     | Unknown    | N/A                | N/A    |
| 277 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 1.445305721320277            | Done     | Unknown    | N/A                | N/A    |
| 278 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2                            | Removed  | Unknown    | N/A                | N/A    |
| 279 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2.0                          | Done     | Unknown    | N/A                | N/A    |
| 280 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 2.890611442640554            | Done     | Unknown    | N/A                | N/A    |
| 281 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 3                            | Done     | Unknown    | N/A                | N/A    |
| 282 | Tensor<[16384, 1]> self = ?,<br>Tensor other = 4                            | Done     | Unknown    | N/A                | N/A    |
| 283 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 1]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 284 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 3]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 285 | Tensor<[16384, 1]> self = ?,<br>Tensor<[16384, 4]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 286 | Tensor<[16384, 3]> self = ?,<br>Tensor other = 0.28209479177387814          | Done     | Unknown    | N/A                | N/A    |
| 287 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 1]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 288 | Tensor<[16384, 3]> self = ?,<br>Tensor<[16384, 3]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 289 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 1]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 290 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 4]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 291 | Tensor<[16384]> self = ?,<br>Tensor other = 0.5                             | Done     | Unknown    | N/A                | N/A    |
| 292 | Tensor<[16384]> self = ?,<br>Tensor other = 1                               | Done     | Unknown    | N/A                | N/A    |
| 293 | Tensor<[16384]> self = ?,<br>Tensor other = 2                               | Done     | Unknown    | N/A                | N/A    |
| 294 | Tensor<[16384]> self = ?,<br>Tensor other = 256                             | Done     | Unknown    | N/A                | N/A    |
| 295 | Tensor<[16384]> self = ?,<br>Tensor other = 3.0                             | Done     | Unknown    | N/A                | N/A    |
| 296 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?                      | Done     | Unknown    | N/A                | N/A    |
| 297 | Tensor<[16384]> self = ?,<br>Tensor<[]> other = ?                           | Done     | Unknown    | N/A                | N/A    |
| 298 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                              | Unknown  | Unknown    | N/A                | N/A    |
| 299 | Tensor<[2, 16, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                | N/A    |
| 300 | Tensor<[2, 16, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                | N/A    |
| 301 | Tensor<[2, 16, 1]> self = ?,<br>Tensor<[2, 16, 1]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 302 | Tensor<[2, 16]> self = ?,<br>Tensor other = -0.75                           | Done     | Unknown    | N/A                | N/A    |
| 303 | Tensor<[2, 16]> self = ?,<br>Tensor other = 1.25                            | Done     | Unknown    | N/A                | N/A    |
| 304 | Tensor<[2, 16]> self = ?,<br>Tensor<[2, 16]> other = ?                      | Done     | Unknown    | N/A                | N/A    |
| 305 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                        | Done     | Done       | 1.0                | 0      |
| 306 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                            | Done     | Done       | 1.0                | 0      |
| 307 | Tensor<[2, 2]> self = ?,<br>Tensor other = 0.3                              | Done     | Unknown    | N/A                | N/A    |
| 308 | Tensor<[2, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                | N/A    |
| 309 | Tensor<[2, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                | N/A    |
| 310 | Tensor<[2, 32, 1]> self = ?,<br>Tensor<[2, 32, 1]> other = ?                | Done     | Unknown    | N/A                | N/A    |
| 311 | Tensor<[2, 42]> self = ?,<br>Tensor other = -0.75                           | Done     | Unknown    | N/A                | N/A    |
| 312 | Tensor<[2, 42]> self = ?,<br>Tensor other = 1.25                            | Done     | Unknown    | N/A                | N/A    |
| 313 | Tensor<[2, 42]> self = ?,<br>Tensor<[2, 42]> other = ?                      | Done     | Unknown    | N/A                | N/A    |
| 314 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                    | Done     | Done       | 0.9999963991411411 | 0      |
| 315 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                      | Done     | Done       | 0.9999960673678667 | 0      |
| 316 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?            | Done     | Done       | 0.99999604722731   | 0      |
| 317 | Tensor<[200]> self = ?,<br>Tensor<[]> other = ?                             | Done     | Unknown    | N/A                | N/A    |
| 318 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                             | Done     | Unknown    | N/A                | N/A    |
| 319 | Tensor<[32, 32]> self = ?,<br>Tensor<[32, 32]> other = ?                    | Done     | Unknown    | N/A                | N/A    |
| 320 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                  | Done     | Unknown    | N/A                | N/A    |
| 321 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                | 0      |
| 322 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                             | Done     | Unknown    | N/A                | N/A    |
| 323 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A                | N/A    |
| 324 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369      | Done     | Done       | 0.9999958840166357 | 0      |
| 325 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?           | Done     | Done       | 0.9999958689576917 | 0      |
| 326 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369      | Done     | Done       | 0.9999957589004113 | 0      |
| 327 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?           | Done     | Done       | 0.9999946623522789 | 0      |
| 328 | Tensor<[4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?                 | Unknown  | Unknown    | N/A                | N/A    |
| 329 | Tensor<[45, 45]> self = ?,<br>Tensor<[45, 45]> other = ?                    | Unknown  | Unknown    | N/A                | N/A    |
| 330 | Tensor<[5, 5]> self = ?,<br>Tensor<[5, 5]> other = ?                        | Unknown  | Unknown    | N/A                | N/A    |
| 331 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                    | Unknown  | Done       | 0.9999967010897297 | 0      |
| 332 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                   | Unknown  | Done       | 0.9999958794173639 | 0      |
| 333 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                   | Unknown  | Done       | 0.9999961999225291 | 0      |
| 334 | Tensor<[59, 59]> self = ?,<br>Tensor<[59, 59]> other = ?                    | Unknown  | Unknown    | N/A                | N/A    |
| 335 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369      | Done     | Done       | 0.9999958463690785 | 0      |
| 336 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?            | Done     | Done       | 0.9999956352911743 | 0      |
| 337 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369      | Done     | Done       | 0.9999958364814288 | 0      |
| 338 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?            | Done     | Done       | 0.9999970083273761 | 0      |
| 339 | Tensor<[7, 7]> self = ?,<br>Tensor<[7, 7]> other = ?                        | Done     | Unknown    | N/A                | N/A    |
| 340 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                    | Unknown  | Done       | 0.9999957969862634 | 0      |
| 341 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                   | Unknown  | Done       | 0.9999956232602167 | 0      |
| 342 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Unknown    | N/A                | N/A    |
| 343 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Unknown    | N/A                | N/A    |
| 344 | Tensor<[822]> self = ?,<br>Tensor<[]> other = ?                             | Done     | Unknown    | N/A                | N/A    |
| 345 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                  | Done     | Unknown    | N/A                | N/A    |
| 346 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                | 0      |
| 347 | Tensor<[8732, 2]> self = ?,<br>Tensor other = ?                             | Done     | Unknown    | N/A                | N/A    |
| 348 | Tensor<[8732]> self = ?,<br>Tensor other = 0.5                              | Done     | Unknown    | N/A                | N/A    |
| 349 | Tensor<[]> self = ?,<br>Tensor other = 0.01                                 | Unknown  | Unknown    | N/A                | N/A    |
| 350 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Unknown    | N/A                | N/A    |
| 351 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                      | Unknown  | Done       | 0.9999953597347219 | 0      |
| 352 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ?                      | Unknown  | Unknown    | N/A                | N/A    |
| 353 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                | Done     | Done       | 1.0                | 0      |

