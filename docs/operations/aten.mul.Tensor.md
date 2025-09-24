### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC                   | Host   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:----------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                               | Done     | Unknown    | N/A                   | N/A    |
|   1 | Tensor self = ?,<br>Tensor<[3234, 1]> other = ?                                | Done     | Unknown    | N/A                   | N/A    |
|   2 | Tensor self = ?,<br>Tensor<[8732, 1]> other = ?                                | Done     | Unknown    | N/A                   | N/A    |
|   3 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999954814535158    | 0      |
|   4 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999963594398462    | 0      |
|   5 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999938811562556    | 0      |
|   6 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999953492976037    | 0      |
|   7 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                   | N/A    |
|   8 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                   | N/A    |
|   9 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?             | Done     | Unknown    | N/A                   | N/A    |
|  10 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999955054804089    | 0      |
|  11 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Done       | 0.9999984235864335    | 0      |
|  12 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                   | 0      |
|  13 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | 1.0                   | 0      |
|  14 | Tensor<[1, 1, 1, 201]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Unknown  | Unknown    | N/A                   | N/A    |
|  15 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | Done       | 0.9999954783347782    | 0      |
|  16 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999955396480055    | 0      |
|  17 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                   | 0      |
|  18 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | 1.0                   | 0      |
|  19 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999974943792187    | 0      |
|  20 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999987086669093    | 0      |
|  21 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | 0.9999944611161031    | 0      |
|  22 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999999997038875    | 0      |
|  23 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999996548716541    | 0      |
|  24 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999970313842548    | 0      |
|  25 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999999907067711    | 0      |
|  26 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                   | N/A    |
|  27 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A                   | N/A    |
|  28 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                   | N/A    |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Done       | 1.0                   | 0      |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953109534758    | 0      |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                   | 0      |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999977415827034    | 0      |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Done       | 0.9999962607230394    | 0      |
|  35 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999949019850781    | 0      |
|  36 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                   | N/A    |
|  37 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                   | N/A    |
|  38 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?             | Done     | Unknown    | N/A                   | N/A    |
|  39 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.9999955406076123    | 0      |
|  40 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                   | N/A    |
|  41 | Tensor<[1, 1, 2048, 2048]> self = ?,<br>Tensor<[1, 1, 2048, 1]> other = ?      | Unknown  | Unknown    | N/A                   | N/A    |
|  42 | Tensor<[1, 1, 2048, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?          | Unknown  | Unknown    | N/A                   | N/A    |
|  43 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | Done       | 0.9999952033907838    | 0      |
|  44 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | Done       | 0.9999954838656776    | 0      |
|  45 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | Done       | 0.9999964980027549    | 0      |
|  46 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1                              | Unknown  | Unknown    | N/A                   | N/A    |
|  47 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999950948201852    | 0      |
|  48 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  49 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999971436440307    | 0      |
|  50 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | 0.9999954551770222    | 0      |
|  51 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999969867638022    | 0      |
|  52 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999987301920568    | 0      |
|  53 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | 0.9999977417588035    | 0      |
|  54 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.999995540804481     | 0      |
|  55 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  56 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999973343355593    | 0      |
|  57 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.9999958493357382    | 0      |
|  58 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Done     | Done       | 0.9999985339447091    | 0      |
|  59 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Done       | 0.9999958284295839    | 0      |
|  60 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999960850120266    | 0      |
|  61 | Tensor<[1, 1, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?             | Unknown  | Unknown    | N/A                   | N/A    |
|  62 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Done       | 0.9999958356117049    | 0      |
|  63 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125                          | Unknown  | Unknown    | N/A                   | N/A    |
|  64 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999996112941435    | 0      |
|  65 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  | Done       | 0.9999954768461013    | 0      |
|  66 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999953881529013    | 0      |
|  67 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999956700205134    | 0      |
|  68 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Removed  | Done       | 0.9999950492270084    | 0      |
|  69 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999990211747312    | 0      |
|  70 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.9999960341046056    | 0      |
|  71 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999959745641742    | 0      |
|  72 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | 0.9999959682543063    | 0      |
|  73 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | 0.9999956302230711    | 0      |
|  74 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | 0.9999958612346219    | 0      |
|  75 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | 0.999997338139842     | 0      |
|  76 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953372228888    | 0      |
|  77 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
|  78 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972324250292    | 0      |
|  79 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | 0.999995862620512     | 0      |
|  80 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                   | 0      |
|  81 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | 0.9999958030566782    | 0      |
|  82 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | 0.9999958801536069    | 0      |
|  83 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | Done       | 0.9999960594808397    | 0      |
|  84 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | 0.999996118844512     | 0      |
|  85 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | 0.9999959199644045    | 0      |
|  86 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | 0.9999960243809837    | 0      |
|  87 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Removed  | Done       | 0.9999976042282087    | 0      |
|  88 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999954947099128    | 0      |
|  89 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | Done       | 0.9999958584716203    | 0      |
|  90 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | 0.9999959825841837    | 0      |
|  91 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953559535814    | 0      |
|  92 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
|  93 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.999997203842384     | 0      |
|  94 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | 0.9999958098381555    | 0      |
|  95 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | 0.9999959595903526    | 0      |
|  96 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | 0.9999959337546782    | 0      |
|  97 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999954968354238    | 0      |
|  98 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                   | 0      |
|  99 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999970533513566    | 0      |
| 100 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Unknown  | Done       | 0.9999961457873363    | 0      |
| 101 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Unknown  | Done       | 0.99999560579081      | 0      |
| 102 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | 0.9999958985553831    | 0      |
| 103 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | 0.999995350644106     | 0      |
| 104 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                   | 0      |
| 105 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Unknown  | Done       | 1.0                   | 0      |
| 106 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999947947125382    | 0      |
| 107 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | 0.9999960800312482    | 0      |
| 108 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | 0.9999953023591065    | 0      |
| 109 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | 0.9999958150430743    | 0      |
| 110 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                   | 0      |
| 111 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Unknown  | Done       | 0.9999997971689598    | 0      |
| 112 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Done     | Done       | 0.9999954896726824    | 0      |
| 113 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | 0.9999959263029299    | 0      |
| 114 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Done       | 0.9999960001193846    | 0      |
| 115 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Removed  | Done       | 0.9999953622991679    | 0      |
| 116 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999959404762448    | 0      |
| 117 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | 0.9999959190363278    | 0      |
| 118 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | 0.9999957718558297    | 0      |
| 119 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | 0.9999957497345103    | 0      |
| 120 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Done     | Done       | 0.9999952394800213    | 0      |
| 121 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | 0.9999960153167176    | 0      |
| 122 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958617871114    | 0      |
| 123 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                   | 0      |
| 124 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | 0.999995916011674     | 0      |
| 125 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                   | 0      |
| 126 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | 0.9999957671101545    | 0      |
| 127 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | 0.9999959771318184    | 0      |
| 128 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Removed  | Done       | 0.9999971343596454    | 0      |
| 129 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                   | N/A    |
| 130 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | 0.9999956629701885    | 0      |
| 131 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | 0.9999961597589262    | 0      |
| 132 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999960874856769    | 0      |
| 133 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999960457583152    | 0      |
| 134 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999960490347116    | 0      |
| 135 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.999996034943227     | 0      |
| 136 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | 0.9999959367513822    | 0      |
| 137 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999959913548346    | 0      |
| 138 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Unknown    | N/A                   | N/A    |
| 139 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | 0.9999960356574636    | 0      |
| 140 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | 0.9999959604942548    | 0      |
| 141 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor other = 2                        | Unknown  | Unknown    | N/A                   | N/A    |
| 142 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[1, 3, 16, 16, 2]> other = ?     | Unknown  | Unknown    | N/A                   | N/A    |
| 143 | Tensor<[1, 3, 16, 16, 2]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  | Unknown    | N/A                   | N/A    |
| 144 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor other = ?                         | Done     | Unknown    | N/A                   | N/A    |
| 145 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     | Done       | 0.9999958003323742    | 0      |
| 146 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Done     | Done       | 0.9999960000414901    | 0      |
| 147 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor other = 2                        | Unknown  | Unknown    | N/A                   | N/A    |
| 148 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[1, 3, 32, 32, 2]> other = ?     | Unknown  | Unknown    | N/A                   | N/A    |
| 149 | Tensor<[1, 3, 32, 32, 2]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  | Unknown    | N/A                   | N/A    |
| 150 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                         | Done     | Unknown    | N/A                   | N/A    |
| 151 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | Done       | 0.9999961185738542    | 0      |
| 152 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Done     | Done       | 0.9999960321874518    | 0      |
| 153 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor other = 2                        | Unknown  | Unknown    | N/A                   | N/A    |
| 154 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[1, 3, 64, 64, 2]> other = ?     | Unknown  | Unknown    | N/A                   | N/A    |
| 155 | Tensor<[1, 3, 64, 64, 2]> self = ?,<br>Tensor<[]> other = ?                    | Unknown  | Unknown    | N/A                   | N/A    |
| 156 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                   | 0      |
| 157 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | 0.9999959043884283    | 0      |
| 158 | Tensor<[1, 32, 11008]> self = ?,<br>Tensor<[1, 32, 11008]> other = ?           | Unknown  | Unknown    | N/A                   | N/A    |
| 159 | Tensor<[1, 32, 32, 128]> self = ?,<br>Tensor<[1, 1, 32, 128]> other = ?        | Unknown  | Unknown    | N/A                   | N/A    |
| 160 | Tensor<[1, 32, 4096]> self = ?,<br>Tensor<[1, 32, 1]> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 161 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958474861761    | 0      |
| 162 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953606775384    | 0      |
| 163 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
| 164 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | Done       | 0.999997211066903     | 0      |
| 165 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | 0.9999959544293581    | 0      |
| 166 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                   | 0      |
| 167 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | 0.99999551489095      | 0      |
| 168 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | 0.9999960231383269    | 0      |
| 169 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | 0.9999977521498615    | 0      |
| 170 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Done       | 0.9999959383744458    | 0      |
| 171 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | 0.9999959255965811    | 0      |
| 172 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                   | 0      |
| 173 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?         | Unknown  | Done       | 0.9999959468668336    | 0      |
| 174 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999990403033293    | 0      |
| 175 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | 0.9999955379641164    | 0      |
| 176 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | 0.9999958822930297    | 0      |
| 177 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999953882868031    | 0      |
| 178 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                   | 0      |
| 179 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999972190670342    | 0      |
| 180 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | 0.9999959069596314    | 0      |
| 181 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | 0.9999956756575482    | 0      |
| 182 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | Done       | 0.9999959402285769    | 0      |
| 183 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | 0.9999958732420606    | 0      |
| 184 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | Done       | 0.9999960237197452    | 0      |
| 185 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | 0.9999960711694681    | 0      |
| 186 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | 0.9999958726463225    | 0      |
| 187 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.9999962948279919    | 0      |
| 188 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999952323183469    | 0      |
| 189 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
| 190 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972466842547    | 0      |
| 191 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999962540366457    | 0      |
| 192 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | Done     | Done       | 0.9999960186571679    | 0      |
| 193 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Done     | Done       | 0.9999960658414675    | 0      |
| 194 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                   | 0      |
| 195 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Removed  | Done       | 0.9999962111064051    | 0      |
| 196 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Done     | Done       | 0.9999958706366631    | 0      |
| 197 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999957523628336    | 0      |
| 198 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.99999599271667      | 0      |
| 199 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | 0.9999959680180641    | 0      |
| 200 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999959479086785    | 0      |
| 201 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999959067179599    | 0      |
| 202 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Done     | Done       | 0.9999959082983008    | 0      |
| 203 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | 0.9999959615413071    | 0      |
| 204 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | 0.9999959978140258    | 0      |
| 205 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | 0.999995818324575     | 0      |
| 206 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Unknown  | Done       | 1.0                   | 0      |
| 207 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Unknown  | Done       | 0.9999969369513799    | 0      |
| 208 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                   | 0      |
| 209 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | 0.9999975127745784    | 0      |
| 210 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Removed  | Done       | 0.9999935960047237    | 0      |
| 211 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | 0.9999952451769111    | 0      |
| 212 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 213 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | Done     | Done       | 0.9999959436895212    | 0      |
| 214 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | Done       | 0.9999959067527143    | 0      |
| 215 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | Done       | 0.9999957772718273    | 0      |
| 216 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999957103185227    | 0      |
| 217 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 218 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | Done       | 0.9999958559233204    | 0      |
| 219 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | Done       | 0.9999959223166495    | 0      |
| 220 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                   | N/A    |
| 221 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | Done     | Done       | 0.9999959904106126    | 0      |
| 222 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | 0.9999962775317561    | 0      |
| 223 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | Done       | 0.999996370909997     | 0      |
| 224 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999957564069339    | 0      |
| 225 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 226 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | Done       | 0.9999958272014561    | 0      |
| 227 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | Done       | 0.9999961195476988    | 0      |
| 228 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                   | N/A    |
| 229 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | Done     | Done       | 0.999995930523487     | 0      |
| 230 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | 0.9999959770909764    | 0      |
| 231 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | Done       | 0.999996042380101     | 0      |
| 232 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | Done       | 0.9999960164343756    | 0      |
| 233 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | 0.9999960284183381    | 0      |
| 234 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | Done       | 0.9999960161271377    | 0      |
| 235 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999959633134984    | 0      |
| 236 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | 0.9999958552616689    | 0      |
| 237 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | 0.9999958826677183    | 0      |
| 238 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | 0.9999959163129981    | 0      |
| 239 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999960261112715    | 0      |
| 240 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | 0.9999959746363506    | 0      |
| 241 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953879260386    | 0      |
| 242 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 243 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971215145675    | 0      |
| 244 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | 0.9999961618230703    | 0      |
| 245 | Tensor<[1, 71, 7, 64]> self = ?,<br>Tensor<[1, 1, 7, 64]> other = ?            | Unknown  | Unknown    | N/A                   | N/A    |
| 246 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | 0.9999960214105937    | 0      |
| 247 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | Done       | 0.9999962119172939    | 0      |
| 248 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | 0.9999959470980737    | 0      |
| 249 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | 0.9999954790243923    | 0      |
| 250 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | 0.9999960394165395    | 0      |
| 251 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | 0.9999960180873916    | 0      |
| 252 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | 0.9999959357196742    | 0      |
| 253 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | 0.9999959864642647    | 0      |
| 254 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | 0.9999959506498997    | 0      |
| 255 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?          | Done     | Unknown    | N/A                   | N/A    |
| 256 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?          | Done     | Unknown    | N/A                   | N/A    |
| 257 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | 0.999996048989102     | 0      |
| 258 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                   | 0      |
| 259 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | 0.9999959246610635    | 0      |
| 260 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Done       | 0.9999958993046302    | 0      |
| 261 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | Done       | 0.9999954618344337    | 0      |
| 262 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | Done       | 1.0                   | 0      |
| 263 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | Done       | 0.9999970209004634    | 0      |
| 264 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | 0.9999962436128499    | 0      |
| 265 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953674905909    | 0      |
| 266 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
| 267 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972153153897    | 0      |
| 268 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | 0.9999959757815564    | 0      |
| 269 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999952943762411    | 0      |
| 270 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 271 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972292505097    | 0      |
| 272 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | 0.9999961510206911    | 0      |
| 273 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999952687626376    | 0      |
| 274 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 275 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972801015116    | 0      |
| 276 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | 0.9999960289350351    | 0      |
| 277 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953635355817    | 0      |
| 278 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 279 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972604145171    | 0      |
| 280 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | 0.9999958803238214    | 0      |
| 281 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | 0.9999956504072086    | 0      |
| 282 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999958114177587    | 0      |
| 283 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | 0.999996162502319     | 0      |
| 284 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999961567379962    | 0      |
| 285 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 286 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 287 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 1                             | Unknown  | Unknown    | N/A                   | N/A    |
| 288 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 289 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 290 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 291 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A                   | N/A    |
| 292 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 293 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                   | 0      |
| 294 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | 0.9999970770896583    | 0      |
| 295 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Unknown  | Done       | 0.9999957834358263    | 0      |
| 296 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 297 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                   | 0      |
| 298 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958228744572    | 0      |
| 299 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | Done     | Done       | 0.010731759748937425  | 0      |
| 300 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958592500234    | 0      |
| 301 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | Done     | Done       | 0.04703556418469716   | 0      |
| 302 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 303 | Tensor<[1]> self = ?,<br>Tensor<[1]> other = ?                                 | Unknown  | Unknown    | N/A                   | N/A    |
| 304 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 305 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 306 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 307 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Done     | Done       | 1.0                   | 0      |
| 308 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Done     | Done       | 0.9999954858900713    | 0      |
| 309 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | Done     | Done       | 1.0                   | 0      |
| 310 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                   | 0      |
| 311 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Done     | Done       | 0.9999943109690709    | 0      |
| 312 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | Done     | Done       | 0.9999960834460268    | 0      |
| 313 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | Done     | Done       | 0.999996156537344     | 0      |
| 314 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | Done     | Done       | 1.0                   | 0      |
| 315 | Tensor<[200]> self = ?,<br>Tensor<[]> other = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 316 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 317 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                     | Done     | Unknown    | N/A                   | N/A    |
| 318 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                   | 0      |
| 319 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 320 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                                 | Done     | Unknown    | N/A                   | N/A    |
| 321 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958690078304    | 0      |
| 322 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | Done     | Done       | 0.4382156430631212    | 0      |
| 323 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.999995871807393     | 0      |
| 324 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | Done     | Done       | 0.014963712485359569  | 0      |
| 325 | Tensor<[4096]> self = ?,<br>Tensor<[1, 32, 4096]> other = ?                    | Unknown  | Unknown    | N/A                   | N/A    |
| 326 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | 0.9999959800488462    | 0      |
| 327 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Unknown  | Done       | 0.999995614761684     | 0      |
| 328 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Unknown  | Done       | 0.9999961953194432    | 0      |
| 329 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.999995829791785     | 0      |
| 330 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | -0.033097693219864034 | 0      |
| 331 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958529177024    | 0      |
| 332 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Done     | Done       | -0.04178642518370424  | 0      |
| 333 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | 0.9999954324081511    | 0      |
| 334 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Unknown  | Done       | 0.9999959251145535    | 0      |
| 335 | Tensor<[8, 1, 1, 384]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Unknown    | N/A                   | N/A    |
| 336 | Tensor<[851]> self = ?,<br>Tensor<[]> other = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 337 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                     | Done     | Unknown    | N/A                   | N/A    |
| 338 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                   | 0      |
| 339 | Tensor<[8732, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 340 | Tensor<[8732]> self = ?,<br>Tensor other = 0.5                                 | Done     | Unknown    | N/A                   | N/A    |
| 341 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                          | Unknown  | Unknown    | N/A                   | N/A    |
| 342 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | Unknown  | Done       | 0.9999977007830533    | 0      |
| 343 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ?                         | Unknown  | Unknown    | N/A                   | N/A    |
| 344 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | Done     | Done       | 1.0                   | 0      |
| 345 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                   | N/A    |

