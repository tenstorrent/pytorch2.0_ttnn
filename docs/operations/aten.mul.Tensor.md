### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC                    | Host   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:-----------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                               | Done     | Unknown    | N/A                    | N/A    |
|   1 | Tensor self = ?,<br>Tensor<[]> other = ?                                       | None     | Unknown    | N/A                    | N/A    |
|   2 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.999998423609089      | 0      |
|   3 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999979194091629     | 0      |
|   4 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999965776618444     | 0      |
|   5 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999971922438406     | 0      |
|   6 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.99999838574232       | 0      |
|   7 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Done       | 0.9999998472692271     | 0      |
|   8 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                    | 0      |
|   9 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | 1.0                    | 0      |
|  10 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | Done       | 0.9999953490004503     | 0      |
|  11 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Done       | 0.999995408008203      | 0      |
|  12 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999952685607904     | 0      |
|  13 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                    | 0      |
|  14 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | 1.0                    | 0      |
|  15 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999984985203157     | 0      |
|  16 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999994141224104     | 0      |
|  17 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | 0.9999994123043114     | 0      |
|  18 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999999539870704     | 0      |
|  19 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999997273272393     | 0      |
|  20 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999993351236526     | 0      |
|  21 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999988125632274     | 0      |
|  22 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999929144595888     | 0      |
|  23 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                    | N/A    |
|  24 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A                    | N/A    |
|  25 | Tensor<[1, 1, 1, s0]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Unknown    | N/A                    | N/A    |
|  26 | Tensor<[1, 1, 1, s0]> self = ?,<br>Tensor<[1, 1, 1, s0]> other = ?             | Unknown  | Unknown    | N/A                    | N/A    |
|  27 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                    | N/A    |
|  28 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Done       | 1.0                    | 0      |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999945691048805     | 0      |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                    | 0      |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                    | 0      |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999975819222411     | 0      |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Done       | 0.9999967126591656     | 0      |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999952230133949     | 0      |
|  35 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.999995552632682      | 0      |
|  36 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | Done       | 0.9999951051629746     | 0      |
|  37 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | Done       | 0.9999956227572683     | 0      |
|  38 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | Done       | 0.9999965348166302     | 0      |
|  39 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999949685440989     | 0      |
|  40 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                    | 0      |
|  41 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972999325804     | 0      |
|  42 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | 0.9999960690490164     | 0      |
|  43 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999965895673789     | 0      |
|  44 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.999999706973897      | 0      |
|  45 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | 0.9999987886734184     | 0      |
|  46 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953270856927     | 0      |
|  47 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                    | 0      |
|  48 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999971031379147     | 0      |
|  49 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.9999957629808816     | 0      |
|  50 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Done     | Done       | 0.9999985735617057     | 0      |
|  51 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Done       | 0.9999962909158054     | 0      |
|  52 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999945124155478     | 0      |
|  53 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Done       | 0.999995972893642      | 0      |
|  54 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999955310840704     | 0      |
|  55 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  | Done       | 0.9999959751249384     | 0      |
|  56 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999948528556688     | 0      |
|  57 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999965299107387     | 0      |
|  58 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999956063033439     | 0      |
|  59 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999952036750239     | 0      |
|  60 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.9999960141046506     | 0      |
|  61 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.9999961122326352     | 0      |
|  62 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999959698003656     | 0      |
|  63 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | 0.9999959344332703     | 0      |
|  64 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | 0.9999959141652729     | 0      |
|  65 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | 0.9999959820141163     | 0      |
|  66 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | 0.9999963131369314     | 0      |
|  67 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953803191957     | 0      |
|  68 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                    | 0      |
|  69 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972299668427     | 0      |
|  70 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | 0.9999957055794377     | 0      |
|  71 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                    | 0      |
|  72 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | 0.9999962494265918     | 0      |
|  73 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | 0.999995810351031      | 0      |
|  74 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | Done       | 0.999995977855733      | 0      |
|  75 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | 0.999996003273669      | 0      |
|  76 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | 0.9999958339141088     | 0      |
|  77 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | 0.9999958962331706     | 0      |
|  78 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Done     | Done       | 0.9999947000306452     | 0      |
|  79 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999963519594224     | 0      |
|  80 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999957152427642     | 0      |
|  81 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999957979772883     | 0      |
|  82 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | Done       | 0.9999959705538377     | 0      |
|  83 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | 0.9999958908931266     | 0      |
|  84 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953332155211     | 0      |
|  85 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                    | 0      |
|  86 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972804556058     | 0      |
|  87 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | 0.999995929127827      | 0      |
|  88 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | 0.9999961214525878     | 0      |
|  89 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | 0.999996232033585      | 0      |
|  90 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999954980912144     | 0      |
|  91 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                    | 0      |
|  92 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999971690698285     | 0      |
|  93 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Unknown  | Done       | 0.9999958175237248     | 0      |
|  94 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Unknown  | Done       | 0.9999972789612052     | 0      |
|  95 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | 0.9999961068346395     | 0      |
|  96 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | 0.9999960773862713     | 0      |
|  97 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                    | 0      |
|  98 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Unknown  | Done       | 1.0                    | 0      |
|  99 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999979631385246     | 0      |
| 100 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | 0.9999960591062554     | 0      |
| 101 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125                        | Done     | Done       | 1.0                    | 0      |
| 102 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0                         | Done     | Done       | 1.0                    | 0      |
| 103 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | 0.9999960179884645     | 0      |
| 104 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | 0.9999966570798453     | 0      |
| 105 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999961240891135     | 0      |
| 106 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?           | Done     | Done       | 0.9999958811519406     | 0      |
| 107 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1024]> other = ?                   | Done     | Done       | 0.999996097114395      | 0      |
| 108 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999958525175007     | 0      |
| 109 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?             | Done     | Done       | 0.9999960120523597     | 0      |
| 110 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Done       | 0.9999959954786866     | 0      |
| 111 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                    | 0      |
| 112 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Unknown  | Done       | 0.9999998223835639     | 0      |
| 113 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Unknown  | Done       | 0.9999958610327067     | 0      |
| 114 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | 0.999995938039983      | 0      |
| 115 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Done       | 0.9999960205695985     | 0      |
| 116 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Done     | Done       | 0.9999954030457815     | 0      |
| 117 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999960176674282     | 0      |
| 118 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999960336621936     | 0      |
| 119 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | 0.9999958771235183     | 0      |
| 120 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | 0.9999960107129643     | 0      |
| 121 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | 0.9999958551580379     | 0      |
| 122 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Done     | Done       | 0.9999955695282866     | 0      |
| 123 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | 0.9999960496406434     | 0      |
| 124 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999959406300633     | 0      |
| 125 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                    | 0      |
| 126 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | 0.9999959694056378     | 0      |
| 127 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                    | 0      |
| 128 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | 0.9999960463725491     | 0      |
| 129 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | 0.9999960037281926     | 0      |
| 130 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Done     | Done       | 0.9999964925112573     | 0      |
| 131 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999961485528793     | 0      |
| 132 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                    | N/A    |
| 133 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | 0.9999955704468738     | 0      |
| 134 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | 0.9999961929550895     | 0      |
| 135 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999959269497684     | 0      |
| 136 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999958769661906     | 0      |
| 137 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999968000240123     | 0      |
| 138 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999959069765929     | 0      |
| 139 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999961517668143     | 0      |
| 140 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999957359170237     | 0      |
| 141 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | 0.9999959172004665     | 0      |
| 142 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999959620215263     | 0      |
| 143 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | 0.9999960398070185     | 0      |
| 144 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | 0.9999959356488537     | 0      |
| 145 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor other = ?                         | Removed  | Unknown    | N/A                    | N/A    |
| 146 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Removed  | Done       | 0.9999958463356211     | 0      |
| 147 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Removed  | Done       | 0.9999959763741603     | 0      |
| 148 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                         | Removed  | Unknown    | N/A                    | N/A    |
| 149 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Removed  | Done       | 0.9999959069812153     | 0      |
| 150 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Removed  | Done       | 0.9999961871150961     | 0      |
| 151 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                    | 0      |
| 152 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor other = ?                        | Removed  | Unknown    | N/A                    | N/A    |
| 153 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?                | Removed  | Done       | 0.9999959820169741     | 0      |
| 154 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?              | Removed  | Done       | 0.9999958174858181     | 0      |
| 155 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | 0.9999960209950751     | 0      |
| 156 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999957630068783     | 0      |
| 157 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953601591827     | 0      |
| 158 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                    | 0      |
| 159 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | Done       | 0.9999971892562363     | 0      |
| 160 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | 0.9999959250656821     | 0      |
| 161 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                    | 0      |
| 162 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | 0.9999962949983647     | 0      |
| 163 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | 0.9999962189747615     | 0      |
| 164 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | 0.9999955697267757     | 0      |
| 165 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Done       | 0.9999960388924863     | 0      |
| 166 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | 0.9999959646839706     | 0      |
| 167 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                    | 0      |
| 168 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?         | Unknown  | Done       | 0.9999959638318129     | 0      |
| 169 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999964501899589     | 0      |
| 170 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | 0.9999960496639123     | 0      |
| 171 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | 0.9999959413869154     | 0      |
| 172 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999954137121659     | 0      |
| 173 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                    | 0      |
| 174 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999971579761112     | 0      |
| 175 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | 0.9999959953834907     | 0      |
| 176 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | 0.9999962332839862     | 0      |
| 177 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | Done       | 0.9999960383560583     | 0      |
| 178 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | 0.9999962418715406     | 0      |
| 179 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | Done       | 0.9999961626938455     | 0      |
| 180 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | 0.9999958315661612     | 0      |
| 181 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | 0.999995901631475      | 0      |
| 182 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.9999961474719067     | 0      |
| 183 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999954299309215     | 0      |
| 184 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                    | 0      |
| 185 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972489214446     | 0      |
| 186 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999959282699571     | 0      |
| 187 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | Done     | Done       | 0.9999960088569122     | 0      |
| 188 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Done     | Done       | 0.9999960413115647     | 0      |
| 189 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                    | 0      |
| 190 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Done     | Done       | 0.9999969306923223     | 0      |
| 191 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Done     | Done       | 0.9999958701936363     | 0      |
| 192 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999960065703977     | 0      |
| 193 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999960065851342     | 0      |
| 194 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999959959734458     | 0      |
| 195 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999960023708597     | 0      |
| 196 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | 0.9999959428880265     | 0      |
| 197 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999960536620297     | 0      |
| 198 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999959974136229     | 0      |
| 199 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999958985329759     | 0      |
| 200 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Unknown  | Done       | 0.9999966293336022     | 0      |
| 201 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | 0.9999960432873886     | 0      |
| 202 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | 0.9999959529702265     | 0      |
| 203 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | 0.9999959099981695     | 0      |
| 204 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Unknown  | Done       | 1.0                    | 0      |
| 205 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Unknown  | Done       | 0.9999974401815722     | 0      |
| 206 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                    | 0      |
| 207 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | 0.9999974999251973     | 0      |
| 208 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Done     | Done       | 0.9999978131777213     | 0      |
| 209 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | 0.9999959982781776     | 0      |
| 210 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                    | N/A    |
| 211 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | Done     | Done       | 0.9999959967860486     | 0      |
| 212 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | Done       | 0.9999958730915675     | 0      |
| 213 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | Done       | 0.9999961872132082     | 0      |
| 214 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999956868448003     | 0      |
| 215 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999959922306451     | 0      |
| 216 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                    | N/A    |
| 217 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | Done       | 0.9999958758757388     | 0      |
| 218 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | Done       | 0.9999960072785994     | 0      |
| 219 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                    | N/A    |
| 220 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | Done     | Done       | 0.9999958276003521     | 0      |
| 221 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | 0.9999958589585285     | 0      |
| 222 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | Done       | 0.9999963181341162     | 0      |
| 223 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.999995953121208      | 0      |
| 224 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999956643332791     | 0      |
| 225 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                    | N/A    |
| 226 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | Done       | 0.9999959686747252     | 0      |
| 227 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | Done       | 0.9999961357620359     | 0      |
| 228 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                    | N/A    |
| 229 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | Done     | Done       | 0.9999960245210964     | 0      |
| 230 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | 0.9999959272470885     | 0      |
| 231 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | Done       | 0.9999955126242943     | 0      |
| 232 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | Done       | 0.9999958922246194     | 0      |
| 233 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | 0.9999959694116703     | 0      |
| 234 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | Done       | 0.9999960658840689     | 0      |
| 235 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999960828624405     | 0      |
| 236 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | 0.9999959039303477     | 0      |
| 237 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | 0.9999959589152725     | 0      |
| 238 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | 0.9999961780749327     | 0      |
| 239 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999960263119368     | 0      |
| 240 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | 0.9999958371579674     | 0      |
| 241 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999952745005204     | 0      |
| 242 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                    | 0      |
| 243 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972596061809     | 0      |
| 244 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | 0.9999960078235528     | 0      |
| 245 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | 0.9999959745340594     | 0      |
| 246 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | Done       | 0.999995686628196      | 0      |
| 247 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | 0.9999960479934886     | 0      |
| 248 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | 0.999995907552248      | 0      |
| 249 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | 0.9999959783782795     | 0      |
| 250 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | 0.9999958992317491     | 0      |
| 251 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | 0.9999959099827951     | 0      |
| 252 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | 0.9999958819732233     | 0      |
| 253 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | 0.9999958012763521     | 0      |
| 254 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | 0.9999958509093159     | 0      |
| 255 | Tensor<[1, 7]> self = ?,<br>Tensor<[7]> other = ?                              | Done     | Done       | 1.0                    | 0      |
| 256 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                    | 0      |
| 257 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | 0.9999962990279553     | 0      |
| 258 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Done       | 0.999995625518267      | 0      |
| 259 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | Done       | 0.9999950017083745     | 0      |
| 260 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | Done       | 1.0                    | 0      |
| 261 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | Done       | 0.9999969857854432     | 0      |
| 262 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | 0.999995221502723      | 0      |
| 263 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.999995374262931      | 0      |
| 264 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                    | 0      |
| 265 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972384823536     | 0      |
| 266 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | 0.9999958629132404     | 0      |
| 267 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999952254762327     | 0      |
| 268 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                    | 0      |
| 269 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971261178469     | 0      |
| 270 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | 0.9999958083759956     | 0      |
| 271 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999954717421873     | 0      |
| 272 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                    | 0      |
| 273 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971948249606     | 0      |
| 274 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | 0.9999959950730806     | 0      |
| 275 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999954124089458     | 0      |
| 276 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                    | 0      |
| 277 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972007136037     | 0      |
| 278 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | 0.9999960168060703     | 0      |
| 279 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | 0.9999963358741175     | 0      |
| 280 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999958328180919     | 0      |
| 281 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | 0.9999959916706953     | 0      |
| 282 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999959603220584     | 0      |
| 283 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ?       | Unknown  | Unknown    | N/A                    | N/A    |
| 284 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ?       | Unknown  | Unknown    | N/A                    | N/A    |
| 285 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?       | Unknown  | Unknown    | N/A                    | N/A    |
| 286 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ?       | Unknown  | Unknown    | N/A                    | N/A    |
| 287 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ?       | Unknown  | Unknown    | N/A                    | N/A    |
| 288 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A                    | N/A    |
| 289 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                    | 0      |
| 290 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                    | 0      |
| 291 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | 0.9999960173475815     | 0      |
| 292 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Unknown  | Done       | 0.9999956337250678     | 0      |
| 293 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                   | Done     | Done       | 0.999995836673441      | 0      |
| 294 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                    | 0      |
| 295 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                    | 0      |
| 296 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958448277751     | 0      |
| 297 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | Done     | Done       | -0.12620451512639844   | 0      |
| 298 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958570198184     | 0      |
| 299 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | Done     | Done       | 0.13957995004691667    | 0      |
| 300 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                    | 0      |
| 301 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                    | N/A    |
| 302 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                    | N/A    |
| 303 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                    | N/A    |
| 304 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Unknown  | Done       | 1.0                    | 0      |
| 305 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Unknown  | Done       | 0.9999963354927265     | 0      |
| 306 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | None     | Fallback   | 1.0                    | -1     |
| 307 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                    | 0      |
| 308 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Unknown  | Done       | 0.9999950047447772     | 0      |
| 309 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | Done     | Done       | 0.999995947086938      | 0      |
| 310 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | Done     | Done       | 0.9999961299491028     | 0      |
| 311 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | Done     | Done       | 1.0                    | 0      |
| 312 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                    | 0      |
| 313 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                    | N/A    |
| 314 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958626355289     | 0      |
| 315 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | Done     | Done       | 0.2600541870004483     | 0      |
| 316 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999959091406244     | 0      |
| 317 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | Done     | Done       | 0.2959096096486353     | 0      |
| 318 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | 0.9999957683920712     | 0      |
| 319 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Unknown  | Done       | 0.9999959289063547     | 0      |
| 320 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Unknown  | Done       | 0.9999962892931363     | 0      |
| 321 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958720120133     | 0      |
| 322 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | -0.0002642522527317225 | 0      |
| 323 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958081742591     | 0      |
| 324 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Done     | Done       | 0.045380225566774214   | 0      |
| 325 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | 0.9999964440259735     | 0      |
| 326 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Unknown  | Done       | 0.9999958959635339     | 0      |
| 327 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                     | Done     | Done       | 0.9999959171126224     | 0      |
| 328 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                    | 0      |
| 329 | Tensor<[8732, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                    | N/A    |
| 330 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | None     | Fallback   | 1.0                    | -1     |
| 331 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  | Fallback   | 1.0                    | -1     |
| 332 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                    | N/A    |

