### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC                   | Host   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:----------------------|:-------|
|   0 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                           | Unknown  | Done       | 1.0                   | 0      |
|   1 | Tensor<[0]> self = ?,<br>Tensor other = 0.5                                    | Unknown  | Fallback   | 1.0                   | -1     |
|   2 | Tensor<[0]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | 1.0                   | -1     |
|   3 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | None     | Fallback   | 1.0                   | -1     |
|   4 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | None     | Fallback   | 1.0                   | -1     |
|   5 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | None     | Fallback   | 1.0                   | -1     |
|   6 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | None     | Fallback   | 1.0                   | -1     |
|   7 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Fallback   | 1.0                   | -1     |
|   8 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Done       | 0.9999980940462572    | 0      |
|   9 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Fallback   | 1.0                   | -1     |
|  10 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | 1.0                   | 0      |
|  11 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | None     | Fallback   | 1.0                   | -1     |
|  12 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | None     | Fallback   | 1.0                   | -1     |
|  13 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | None     | Fallback   | 1.0                   | -1     |
|  14 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Fallback   | 1.0                   | -1     |
|  15 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | 1.0                   | 0      |
|  16 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | None     | Fallback   | 1.0                   | -1     |
|  17 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | None     | Fallback   | 1.0                   | -1     |
|  18 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.9761904761904763           | Removed  | Fallback   | 1.0                   | -1     |
|  19 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | 0.9999975162136193    | 0      |
|  20 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Fallback   | 1.0                   | -1     |
|  21 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Fallback   | 1.0                   | -1     |
|  22 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | None     | Fallback   | 1.0                   | -1     |
|  23 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | None     | Fallback   | 1.0                   | -1     |
|  24 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | None     | Fallback   | 1.0                   | -1     |
|  25 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                   | N/A    |
|  26 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A                   | N/A    |
|  27 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                   | N/A    |
|  28 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Fallback   | 1.0                   | -1     |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Fallback   | 1.0                   | -1     |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Fallback   | 1.0                   | -1     |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Fallback   | 1.0                   | -1     |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Fallback   | 1.0                   | -1     |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Done       | 0.9999971039586969    | 0      |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999959410114563    | 0      |
|  35 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.9999952658693949    | 0      |
|  36 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | None     | Fallback   | 1.0                   | -1     |
|  37 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | None     | Fallback   | 1.0                   | -1     |
|  38 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | None     | Fallback   | 1.0                   | -1     |
|  39 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Fallback   | 1.0                   | -1     |
|  40 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Fallback   | 1.0                   | -1     |
|  41 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Fallback   | 1.0                   | -1     |
|  42 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | 0.9999962870986764    | 0      |
|  43 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | None     | Fallback   | 1.0                   | -1     |
|  44 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | None     | Fallback   | 1.0                   | -1     |
|  45 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.5625                       | Removed  | Fallback   | 1.0                   | -1     |
|  46 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | 0.9999912820141537    | 0      |
|  47 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Fallback   | 1.0                   | -1     |
|  48 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Fallback   | 1.0                   | -1     |
|  49 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Fallback   | 1.0                   | -1     |
|  50 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.9999956059141999    | 0      |
|  51 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | None     | Fallback   | 1.0                   | -1     |
|  52 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Fallback   | 1.0                   | -1     |
|  53 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.999995602692856     | 0      |
|  54 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Fallback   | 1.0                   | -1     |
|  55 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999963080703821    | 0      |
|  56 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Done     | Done       | 0.9999959420518224    | 0      |
|  57 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Done     | Done       | 0.9999953173129272    | 0      |
|  58 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Done     | Done       | 0.9999959511652443    | 0      |
|  59 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999959004214496    | 0      |
|  60 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999970877575409    | 0      |
|  61 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.9999958772923986    | 0      |
|  62 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.999996016787432     | 0      |
|  63 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999959043006943    | 0      |
|  64 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | 0.9999957868142182    | 0      |
|  65 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | 0.9999957222375556    | 0      |
|  66 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | 0.9999958908462082    | 0      |
|  67 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | 0.9999927465776149    | 0      |
|  68 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | None     | Fallback   | 1.0                   | -1     |
|  69 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | None     | Fallback   | 1.0                   | -1     |
|  70 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | None     | Fallback   | 1.0                   | -1     |
|  71 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | 0.9999960625553823    | 0      |
|  72 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | None     | Fallback   | 1.0                   | -1     |
|  73 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | 0.99999588625814      | 0      |
|  74 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | 0.9999959321132971    | 0      |
|  75 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | Done       | 0.9999961799663545    | 0      |
|  76 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | 0.9999961192000333    | 0      |
|  77 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | 0.9999959470388603    | 0      |
|  78 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | 0.9999958277899126    | 0      |
|  79 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Done     | Done       | 0.9999965532294853    | 0      |
|  80 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999958667120498    | 0      |
|  81 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999960953051084    | 0      |
|  82 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999956454052131    | 0      |
|  83 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | Done       | 0.9999958935556053    | 0      |
|  84 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | 0.999995937467203     | 0      |
|  85 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | None     | Fallback   | 1.0                   | -1     |
|  86 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | None     | Fallback   | 1.0                   | -1     |
|  87 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | None     | Fallback   | 1.0                   | -1     |
|  88 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | 0.9999958205778444    | 0      |
|  89 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | 0.9999960850225402    | 0      |
|  90 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | 0.9999956939995934    | 0      |
|  91 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | None     | Fallback   | 1.0                   | -1     |
|  92 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | None     | Fallback   | 1.0                   | -1     |
|  93 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | None     | Fallback   | 1.0                   | -1     |
|  94 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Done     | Done       | 0.999995902416199     | 0      |
|  95 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Done     | Done       | 0.9999954108993276    | 0      |
|  96 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | 0.9999959473805928    | 0      |
|  97 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | 0.999995236117323     | 0      |
|  98 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | None     | Fallback   | 1.0                   | -1     |
|  99 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | None     | Fallback   | 1.0                   | -1     |
| 100 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999959021050314    | 0      |
| 101 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | 0.999995950756887     | 0      |
| 102 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125                        | None     | Fallback   | 1.0                   | -1     |
| 103 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0                         | None     | Fallback   | 1.0                   | -1     |
| 104 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | 0.9999957541333526    | 0      |
| 105 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | 0.9999964200598997    | 0      |
| 106 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999946886925206    | 0      |
| 107 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?           | Done     | Done       | 0.9999960020861104    | 0      |
| 108 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1024]> other = ?                   | Done     | Done       | 0.9999959176354938    | 0      |
| 109 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999967871509367    | 0      |
| 110 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?             | Done     | Done       | 0.9999959519853279    | 0      |
| 111 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Done       | 0.999995785960217     | 0      |
| 112 | Tensor<[1, 1]> self = ?,<br>Tensor other = 0                                   | None     | Fallback   | 1.0                   | -1     |
| 113 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 114 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50258                               | None     | Fallback   | 1.0                   | -1     |
| 115 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50259                               | None     | Fallback   | 1.0                   | -1     |
| 116 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50359                               | None     | Fallback   | 1.0                   | -1     |
| 117 | Tensor<[1, 1]> self = ?,<br>Tensor other = 50363                               | None     | Fallback   | 1.0                   | -1     |
| 118 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Done     | Done       | 0.9999956480856479    | 0      |
| 119 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Unknown  | Done       | 0.9999947354337911    | 0      |
| 120 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | 0.9999960607486076    | 0      |
| 121 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Unknown    | N/A                   | N/A    |
| 122 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Done     | Done       | 0.9999959852736817    | 0      |
| 123 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999959718542891    | 0      |
| 124 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999959690436301    | 0      |
| 125 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | 0.9999961178321909    | 0      |
| 126 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | 0.9999959508274361    | 0      |
| 127 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | 0.9999958690732245    | 0      |
| 128 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | None     | Fallback   | 1.0                   | -1     |
| 129 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | 0.9999959063581205    | 0      |
| 130 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | None     | Fallback   | 1.0                   | -1     |
| 131 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | None     | Fallback   | 1.0                   | -1     |
| 132 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | 0.999995722847049     | 0      |
| 133 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | None     | Fallback   | 1.0                   | -1     |
| 134 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | 0.999995924716584     | 0      |
| 135 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | 0.9999959487092215    | 0      |
| 136 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Done     | Done       | 0.9999954895214935    | 0      |
| 137 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999957720005201    | 0      |
| 138 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | 0.999996012459573     | 0      |
| 139 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | 0.9999962152215107    | 0      |
| 140 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.999996015874228     | 0      |
| 141 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.999995949924906     | 0      |
| 142 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999962225403312    | 0      |
| 143 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.999995830644458     | 0      |
| 144 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999959685387035    | 0      |
| 145 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999961605580397    | 0      |
| 146 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | 0.999995964992255     | 0      |
| 147 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999961102780627    | 0      |
| 148 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | 0.9999958695167693    | 0      |
| 149 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | 0.9999958691859303    | 0      |
| 150 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     | Done       | 0.999995844002376     | 0      |
| 151 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Done     | Done       | 0.9999961249921353    | 0      |
| 152 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | Done       | 0.9999960506511479    | 0      |
| 153 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Done     | Done       | 0.999996060956497     | 0      |
| 154 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | None     | Fallback   | 1.0                   | -1     |
| 155 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?                | Done     | Done       | 0.9999959189513928    | 0      |
| 156 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?              | Done     | Done       | 0.9999959754307872    | 0      |
| 157 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | 0.9999959665451394    | 0      |
| 158 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | None     | Fallback   | 1.0                   | -1     |
| 159 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | None     | Fallback   | 1.0                   | -1     |
| 160 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | None     | Fallback   | 1.0                   | -1     |
| 161 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | None     | Fallback   | 1.0                   | -1     |
| 162 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | 0.999996018225243     | 0      |
| 163 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | None     | Fallback   | 1.0                   | -1     |
| 164 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | 0.9999971837751415    | 0      |
| 165 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | 0.9999957404118998    | 0      |
| 166 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | 0.9999969800134038    | 0      |
| 167 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Done       | 0.9999960333892697    | 0      |
| 168 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | 0.9999959476786947    | 0      |
| 169 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | None     | Fallback   | 1.0                   | -1     |
| 170 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?         | Unknown  | Done       | 0.9999959541178166    | 0      |
| 171 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999968819055061    | 0      |
| 172 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | 0.9999961281575938    | 0      |
| 173 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | 0.9999961658736022    | 0      |
| 174 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Fallback   | 1.0                   | -1     |
| 175 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Fallback   | 1.0                   | -1     |
| 176 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Fallback   | 1.0                   | -1     |
| 177 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | 0.9999960202132556    | 0      |
| 178 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | 0.9999961035640286    | 0      |
| 179 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | Done       | 0.9999957012176016    | 0      |
| 180 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | 0.9999958928880731    | 0      |
| 181 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | Done       | 0.9999960728623299    | 0      |
| 182 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | 0.9999959274257945    | 0      |
| 183 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | 0.9999959889475284    | 0      |
| 184 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.9999964048859115    | 0      |
| 185 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Fallback   | 1.0                   | -1     |
| 186 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Fallback   | 1.0                   | -1     |
| 187 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Fallback   | 1.0                   | -1     |
| 188 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999959377392796    | 0      |
| 189 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | None     | Fallback   | 1.0                   | -1     |
| 190 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Done     | Done       | 0.9999959527646785    | 0      |
| 191 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | None     | Fallback   | 1.0                   | -1     |
| 192 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Done     | Done       | 0.9999949667879224    | 0      |
| 193 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Done     | Done       | 0.9999959617223669    | 0      |
| 194 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999958313237544    | 0      |
| 195 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999959027330346    | 0      |
| 196 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999959562640366    | 0      |
| 197 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999959942900548    | 0      |
| 198 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | 0.9999959363249076    | 0      |
| 199 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999959694411445    | 0      |
| 200 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999958290490456    | 0      |
| 201 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999958679460264    | 0      |
| 202 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Unknown  | Done       | 0.9999963728891008    | 0      |
| 203 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | 0.9999958906626695    | 0      |
| 204 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | 0.9999958585602737    | 0      |
| 205 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | 0.9999959874949609    | 0      |
| 206 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | None     | Fallback   | 1.0                   | -1     |
| 207 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Done     | Done       | 0.9999987022969317    | 0      |
| 208 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | None     | Fallback   | 1.0                   | -1     |
| 209 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | 0.9999981977859261    | 0      |
| 210 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Done     | Done       | 0.9999967633258906    | 0      |
| 211 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | 0.9999956063493178    | 0      |
| 212 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | Done     | Done       | 0.9999959410536489    | 0      |
| 213 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | Done       | 0.9999959183190575    | 0      |
| 214 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | Done       | 0.9999958535096956    | 0      |
| 215 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999958376898053    | 0      |
| 216 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999963240283571    | 0      |
| 217 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | Done       | 0.9999959108777817    | 0      |
| 218 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | Done       | 0.9999960447249284    | 0      |
| 219 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | Done     | Done       | 0.9999958969275515    | 0      |
| 220 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | 0.999996044052507     | 0      |
| 221 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | Done       | 0.9999955041485878    | 0      |
| 222 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999965056951859    | 0      |
| 223 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999965861782953    | 0      |
| 224 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | Done       | 0.999995909189963     | 0      |
| 225 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | Done       | 0.9999959984466625    | 0      |
| 226 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | Done     | Done       | 0.9999959131663382    | 0      |
| 227 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | 0.9999956147016984    | 0      |
| 228 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | Done       | 0.9999962224934853    | 0      |
| 229 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | Done       | 0.9999957270984956    | 0      |
| 230 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | 0.9999959704907425    | 0      |
| 231 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | Done       | 0.9999959834377127    | 0      |
| 232 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999959526803279    | 0      |
| 233 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | 0.9999958845488479    | 0      |
| 234 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | 0.9999958604123206    | 0      |
| 235 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | 0.9999961760350619    | 0      |
| 236 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999961010529506    | 0      |
| 237 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | 0.9999958508996933    | 0      |
| 238 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | None     | Fallback   | 1.0                   | -1     |
| 239 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | None     | Fallback   | 1.0                   | -1     |
| 240 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | None     | Fallback   | 1.0                   | -1     |
| 241 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | 0.9999957597702811    | 0      |
| 242 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | 0.9999959817644626    | 0      |
| 243 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | Done       | 0.9999960800720077    | 0      |
| 244 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | 0.9999956111809004    | 0      |
| 245 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | 0.9999958596978873    | 0      |
| 246 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | 0.9999960029504077    | 0      |
| 247 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | 0.9999959756162736    | 0      |
| 248 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | 0.999995909549725     | 0      |
| 249 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | 0.9999959457037813    | 0      |
| 250 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | 0.9999958163572344    | 0      |
| 251 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | 0.9999959097061724    | 0      |
| 252 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | None     | Fallback   | 1.0                   | -1     |
| 253 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | 0.9999959086259209    | 0      |
| 254 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Unknown    | N/A                   | N/A    |
| 255 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | None     | Fallback   | 1.0                   | -1     |
| 256 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | None     | Fallback   | 1.0                   | -1     |
| 257 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | None     | Fallback   | 1.0                   | -1     |
| 258 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | 0.9999955484272928    | 0      |
| 259 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | None     | Fallback   | 1.0                   | -1     |
| 260 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | None     | Fallback   | 1.0                   | -1     |
| 261 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | None     | Fallback   | 1.0                   | -1     |
| 262 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | 0.9999959324900142    | 0      |
| 263 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | None     | Fallback   | 1.0                   | -1     |
| 264 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | None     | Fallback   | 1.0                   | -1     |
| 265 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | None     | Fallback   | 1.0                   | -1     |
| 266 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | 0.9999958196722644    | 0      |
| 267 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | None     | Fallback   | 1.0                   | -1     |
| 268 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | None     | Fallback   | 1.0                   | -1     |
| 269 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | None     | Fallback   | 1.0                   | -1     |
| 270 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | 0.9999961386805712    | 0      |
| 271 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | None     | Fallback   | 1.0                   | -1     |
| 272 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | None     | Fallback   | 1.0                   | -1     |
| 273 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | None     | Fallback   | 1.0                   | -1     |
| 274 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | 0.9999959160953279    | 0      |
| 275 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | 0.999995669680495     | 0      |
| 276 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999959117510351    | 0      |
| 277 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | 0.9999959538866833    | 0      |
| 278 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999959484100309    | 0      |
| 279 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 280 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 281 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 282 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 283 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 284 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A                   | N/A    |
| 285 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | None     | Fallback   | 1.0                   | -1     |
| 286 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | None     | Fallback   | 1.0                   | -1     |
| 287 | Tensor<[100]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 288 | Tensor<[100]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | Fallback   | 1.0                   | -1     |
| 289 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | 0.9999955628873711    | 0      |
| 290 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Done     | Done       | 0.9999960909150756    | 0      |
| 291 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                   | Done     | Done       | 0.9999958745046527    | 0      |
| 292 | Tensor<[1066]> self = ?,<br>Tensor other = 0.600375234521576                   | Unknown  | Fallback   | 1.0                   | -1     |
| 293 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                   | -1     |
| 294 | Tensor<[128]> self = ?,<br>Tensor other = 0.125                                | Removed  | Fallback   | 1.0                   | -1     |
| 295 | Tensor<[128]> self = ?,<br>Tensor other = 0.25                                 | Removed  | Fallback   | 1.0                   | -1     |
| 296 | Tensor<[128]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                   | -1     |
| 297 | Tensor<[128]> self = ?,<br>Tensor other = 1.0                                  | Removed  | Fallback   | 1.0                   | -1     |
| 298 | Tensor<[128]> self = ?,<br>Tensor other = 2                                    | None     | Fallback   | 1.0                   | -1     |
| 299 | Tensor<[12]> self = ?,<br>Tensor other = 32.0                                  | Removed  | Fallback   | 1.0                   | -1     |
| 300 | Tensor<[12]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 301 | Tensor<[136]> self = ?,<br>Tensor other = 0.5                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 302 | Tensor<[136]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | Fallback   | 1.0                   | -1     |
| 303 | Tensor<[13]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 304 | Tensor<[14]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 305 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | None     | Fallback   | 1.0                   | -1     |
| 306 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | None     | Fallback   | 1.0                   | -1     |
| 307 | Tensor<[16, 1]> self = ?,<br>Tensor<[1, 1, 32]> other = ?                      | Removed  | Done       | 0.5259595299357039    | 0      |
| 308 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | None     | Fallback   | 1.0                   | -1     |
| 309 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | Done     | Done       | 0.09920038148989248   | 0      |
| 310 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | None     | Fallback   | 1.0                   | -1     |
| 311 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | Done     | Done       | -0.020559282734044414 | 0      |
| 312 | Tensor<[160]> self = ?,<br>Tensor other = -9.210340371976184                   | Unknown  | Fallback   | 1.0                   | -1     |
| 313 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                   | -1     |
| 314 | Tensor<[16]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Fallback   | 1.0                   | -1     |
| 315 | Tensor<[16]> self = ?,<br>Tensor other = 32.0                                  | Removed  | Fallback   | 1.0                   | -1     |
| 316 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Fallback   | 1.0                   | -1     |
| 317 | Tensor<[17]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 318 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 319 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 320 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 321 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Unknown  | Done       | 1.0                   | 0      |
| 322 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Unknown  | Done       | 0.9999963231573943    | 0      |
| 323 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | None     | Fallback   | 1.0                   | -1     |
| 324 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 325 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Unknown  | Done       | 0.9999952666802057    | 0      |
| 326 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | None     | Fallback   | 1.0                   | -1     |
| 327 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | Done     | Done       | 0.9999960274370747    | 0      |
| 328 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | None     | Fallback   | 1.0                   | -1     |
| 329 | Tensor<[23]> self = ?,<br>Tensor other = 31.304347826086957                    | Removed  | Fallback   | 1.0                   | -1     |
| 330 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                   | -1     |
| 331 | Tensor<[25]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 332 | Tensor<[28]> self = ?,<br>Tensor other = 0.25                                  | Removed  | Fallback   | 1.0                   | -1     |
| 333 | Tensor<[28]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 334 | Tensor<[300]> self = ?,<br>Tensor other = 1.6                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 335 | Tensor<[300]> self = ?,<br>Tensor other = 2.1333333333333333                   | Unknown  | Fallback   | 1.0                   | -1     |
| 336 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | Fallback   | 1.0                   | -1     |
| 337 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 338 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                   | -1     |
| 339 | Tensor<[320]> self = ?,<br>Tensor other = 1.0                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 340 | Tensor<[320]> self = ?,<br>Tensor other = 1.5                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 341 | Tensor<[320]> self = ?,<br>Tensor other = 2.0                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 342 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                     | Unknown  | Done       | 0.9999970250227933    | 0      |
| 343 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | None     | Fallback   | 1.0                   | -1     |
| 344 | Tensor<[3234, 2]> self = ?,<br>Tensor<[2]> other = ?                           | Unknown  | Done       | 0.9999986764356719    | 0      |
| 345 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 346 | Tensor<[32]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 347 | Tensor<[34]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 348 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | None     | Fallback   | 1.0                   | -1     |
| 349 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | Done     | Done       | 0.13016821751078078   | 0      |
| 350 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | None     | Fallback   | 1.0                   | -1     |
| 351 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | Done     | Done       | 0.1308034971738139    | 0      |
| 352 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 353 | Tensor<[40]> self = ?,<br>Tensor other = 32.0                                  | Removed  | Fallback   | 1.0                   | -1     |
| 354 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                   | -1     |
| 355 | Tensor<[50]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Fallback   | 1.0                   | -1     |
| 356 | Tensor<[50]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 357 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | 0.9999958382696648    | 0      |
| 358 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Done     | Done       | 0.9999965279458467    | 0      |
| 359 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Done     | Done       | 0.9999958746124831    | 0      |
| 360 | Tensor<[56]> self = ?,<br>Tensor other = 0.125                                 | Removed  | Fallback   | 1.0                   | -1     |
| 361 | Tensor<[56]> self = ?,<br>Tensor other = 0.25                                  | Removed  | Fallback   | 1.0                   | -1     |
| 362 | Tensor<[56]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 363 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 364 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | None     | Fallback   | 1.0                   | -1     |
| 365 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | 0.05503929779707124   | 0      |
| 366 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | None     | Fallback   | 1.0                   | -1     |
| 367 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Done     | Done       | -0.042318522642347825 | 0      |
| 368 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                                  | Removed  | Fallback   | 1.0                   | -1     |
| 369 | Tensor<[64]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 370 | Tensor<[68]> self = ?,<br>Tensor other = 0.5                                   | Unknown  | Fallback   | 1.0                   | -1     |
| 371 | Tensor<[68]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 372 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | 0.9999967965931993    | 0      |
| 373 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Done     | Done       | 0.9999958380537193    | 0      |
| 374 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                     | Done     | Done       | 0.9999958582578861    | 0      |
| 375 | Tensor<[7]> self = ?,<br>Tensor other = 0.42857142857142855                    | Removed  | Fallback   | 1.0                   | -1     |
| 376 | Tensor<[7]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 377 | Tensor<[800]> self = ?,<br>Tensor other = 0.6                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 378 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                                   | Removed  | Fallback   | 1.0                   | -1     |
| 379 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                     | Unknown  | Done       | 0.9999959880941439    | 0      |
| 380 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | None     | Fallback   | 1.0                   | -1     |
| 381 | Tensor<[8732, 2]> self = ?,<br>Tensor<[2]> other = ?                           | Unknown  | Done       | 0.9999959090086888    | 0      |
| 382 | Tensor<[8732]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 383 | Tensor<[9]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | 1.0                   | -1     |
| 384 | Tensor<[]> self = ?,<br>Tensor<[0, 1]> other = ?                               | Unknown  | Fallback   | 1.0                   | -1     |
| 385 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | None     | Fallback   | 1.0                   | -1     |
| 386 | Tensor<[]> self = ?,<br>Tensor<[3234, 1]> other = ?                            | Unknown  | Fallback   | 1.0                   | -1     |
| 387 | Tensor<[]> self = ?,<br>Tensor<[8732, 1]> other = ?                            | Unknown  | Fallback   | 1.0                   | -1     |
| 388 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  | Fallback   | 1.0                   | -1     |
| 389 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                   | N/A    |

